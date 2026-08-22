#!/usr/bin/env python3
"""Run Derouter image model through REST API (OpenAI-compatible).

Reads ``cover/quad-mcp-batch.json``, calls Derouter ``/images/generations`` (t2i)
or ``/images/edits`` (i2i with local identity-real file). When ``/images/*`` is
discontinued on all hosts, falls back to ``/openai/v1/responses`` with
``tools: [{type: image_generation}]`` (i2i via input_image when identity ref present).

Writes ``cover/quad-mcp-result.json`` for ``excalibur_blog_quad_apply.py``.

Auth: ``DEROUTER_API_KEY`` only (Cloud Secrets). Never print the key.

Provider order (Cover): images REST (4 hosts) → responses image_generation → DEROUTER MCP.
Forbidden forever: Kie, flux2-pro-*, Seedream, nano_banana*, z-image, PIL template mashup.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    expand_site_base,
    resolve_public_base_from_env,
)

DEFAULT_API_KEY_ENV = "DEROUTER_API_KEY"
DEROUTER_API_KEY_ALIASES = ("DEROUTER_API_KEY", "DEROUTE_API_KEY")
DEFAULT_MODEL_ENV = "DEROUTER_IMAGE_MODEL"
DEFAULT_SIZE_ENV = "DEROUTER_IMAGE_SIZE"
DEFAULT_QUALITY_ENV = "DEROUTER_IMAGE_QUALITY"
DEFAULT_IMAGE_BASE_ENV = "DEROUTER_IMAGE_BASE_URL"
# Quad canvas exact 2K 16:9 per Derouter Image tab (not aspect_ratio API field).
DEFAULT_SIZE_2K_16_9 = "2048x1152"
DEFAULT_QUALITY = "auto"
# Порядок failover для images REST (owner probe 2026-08-22).
# api.derouter.ai может дать HTTP 524 на длинной gen — пробуем после api-direct.
DEFAULT_IMAGE_BASE_URLS = [
    "https://api.derouter.ai/openai/v1",
    "https://api.apikey.cloud/openai/v1",
    "https://api-direct.derouter.ai/openai/v1",
    "https://api-direct.apikey.cloud/openai/v1",
]
PRIMARY_DIRECT_BASE = DEFAULT_IMAGE_BASE_URLS[0]
FALLBACK_DIRECT_BASE = DEFAULT_IMAGE_BASE_URLS[1]
DEFAULT_TIMEOUT_SECONDS = 600
MIN_TIMEOUT_SECONDS = 240
DEFAULT_MAX_RETRIES = 1
DEFAULT_RETRY_WAIT_SECONDS = 5
DEFAULT_LOCAL_REFERENCE = "memory/cover/assets/blog-hero-reference.png"
DEFAULT_RESPONSES_MODEL = "gpt-5.4"
DEFAULT_RESPONSES_MODEL_ENV = "DEROUTER_RESPONSES_IMAGE_MODEL"
RESPONSES_SUFFIX = "/responses"


class DerouterApiError(RuntimeError):
    """Raised for API or response-shape failures."""


def default_model() -> str:
    model = os.environ.get(DEFAULT_MODEL_ENV, "").strip()
    if not model:
        raise DerouterApiError(
            "DEROUTER_IMAGE_MODEL unset; set image model id in Cloud Secrets "
            "(see shared/derouter-gpt-image-api-contract.md)"
        )
    return model


class DerouterRetryable(DerouterApiError):
    """Auth/5xx/524 — retry same host; then failover to next base URL."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


class DerouterHostFailed(DerouterApiError):
    """Host cannot serve images (discontinued / model unavailable) — try next base URL."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


def resolve_derouter_api_key(env_name: str = DEFAULT_API_KEY_ENV) -> str:
    """DEROUTER_API_KEY или alias DEROUTE_API_KEY из Cloud Secrets."""
    primary = os.environ.get(env_name, "").strip()
    if primary:
        return primary
    for alias in DEROUTER_API_KEY_ALIASES:
        if alias == env_name:
            continue
        value = os.environ.get(alias, "").strip()
        if value:
            return value
    return ""


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_path(root: Path, article_dir_arg: str, path_arg: str) -> Path:
    article_dir = Path(article_dir_arg)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    path = Path(path_arg)
    if not path.is_absolute():
        path = article_dir / path
    return path


def default_size() -> str:
    return (os.environ.get(DEFAULT_SIZE_ENV) or DEFAULT_SIZE_2K_16_9).strip() or DEFAULT_SIZE_2K_16_9


def default_quality() -> str:
    return (os.environ.get(DEFAULT_QUALITY_ENV) or DEFAULT_QUALITY).strip() or DEFAULT_QUALITY


def default_responses_model() -> str:
    return (
        os.environ.get(DEFAULT_RESPONSES_MODEL_ENV, "").strip() or DEFAULT_RESPONSES_MODEL
    )


def parse_size_wh(size: str) -> tuple[int, int]:
    """Размер из DEROUTER_IMAGE_SIZE, например 2048x1152."""
    raw = (size or DEFAULT_SIZE_2K_16_9).strip().lower().replace("×", "x")
    if "x" not in raw:
        return 2048, 1152
    left, right = raw.split("x", 1)
    try:
        return max(1, int(left)), max(1, int(right))
    except ValueError:
        return 2048, 1152


def resize_png_bytes(png_bytes: bytes, width: int, height: int) -> bytes:
    from io import BytesIO

    from PIL import Image

    img = Image.open(BytesIO(png_bytes)).convert("RGB")
    if img.size == (width, height):
        out = BytesIO()
        img.save(out, format="PNG", optimize=True)
        return out.getvalue()
    fitted = img.resize((width, height), Image.Resampling.LANCZOS)
    out = BytesIO()
    fitted.save(out, format="PNG", optimize=True)
    return out.getvalue()


def call_responses_image_generation(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    image_paths: list[Path],
    timeout: int,
) -> bytes:
    """POST /responses с tools image_generation; i2i через input_image data-URL."""
    content: list[dict[str, Any]] = [{"type": "input_text", "text": prompt}]
    for path in image_paths:
        if path.is_file():
            mime = _guess_mime(path)
            ref_b64 = base64.b64encode(path.read_bytes()).decode()
            content.append(
                {
                    "type": "input_image",
                    "detail": "high",
                    "image_url": f"data:{mime};base64,{ref_b64}",
                }
            )
            break
    payload = {
        "model": model,
        "input": [{"role": "user", "content": content}],
        "tools": [{"type": "image_generation"}],
    }
    url = f"{base_url.rstrip('/')}{RESPONSES_SUFFIX}"
    parsed = http_json_post(url, api_key, payload, timeout=timeout)
    if parsed.get("status") != "completed":
        raise DerouterApiError(
            f"Derouter responses status={parsed.get('status')!r} (expected completed)"
        )
    for item in parsed.get("output") or []:
        if item.get("type") == "image_generation_call" and item.get("result"):
            try:
                return base64.b64decode(str(item["result"]))
            except Exception as exc:  # noqa: BLE001
                raise DerouterApiError("Derouter responses b64 decode failed") from exc
    raise DerouterApiError("Derouter responses missing image_generation_call.result")


def generate_image_via_responses(
    *,
    prompt: str,
    api_key: str,
    responses_model: str,
    size: str,
    timeout: int,
    base_urls: list[str],
    image_paths: list[Path],
) -> tuple[bytes, dict[str, Any]]:
    """Fallback/primary path when /images/generations is discontinued."""
    target_w, target_h = parse_size_wh(size)
    last_error: BaseException | None = None
    for base in base_urls or list(DEFAULT_IMAGE_BASE_URLS):
        host = urllib.parse.urlparse(base).netloc
        try:
            raw = call_responses_image_generation(
                base_url=base,
                api_key=api_key,
                model=responses_model,
                prompt=prompt,
                image_paths=image_paths,
                timeout=timeout,
            )
            image_bytes = resize_png_bytes(raw, target_w, target_h)
            meta = {
                "source": "derouter-responses-api",
                "model": responses_model,
                "size": size,
                "endpoint": "responses",
                "tool": "image_generation",
                "host": host,
                "response_kind": "image_generation_call.result",
                "resized_to": [target_w, target_h],
            }
            if image_paths:
                meta["local_reference"] = image_paths[0].name
            return image_bytes, meta
        except DerouterRetryable as exc:
            last_error = exc
            print(f"Derouter responses retryable ({exc}); host={host}", flush=True)
            continue
        except DerouterHostFailed as exc:
            last_error = exc
            print(f"Derouter responses host failed ({exc}); host={host}", flush=True)
            continue
        except DerouterApiError as exc:
            last_error = exc
            print(f"Derouter responses error ({exc}); host={host}", flush=True)
            continue
    raise DerouterApiError(f"Derouter responses failed on all image base URLs: {last_error}")


def is_retryable_http(status: int) -> bool:
    # 524 = Cloudflare timeout when hitting non-direct api.derouter.ai for images.
    return status in {401, 403, 408, 429, 500, 502, 503, 504, 524}


def normalize_image_base_url(raw: str) -> str:
    value = raw.strip().rstrip("/")
    if not value:
        return ""
    if value.endswith("/openai/v1"):
        return value
    return f"{value}/openai/v1"


def resolve_image_base_urls(
    *,
    primary_base: str | None = None,
    fallback_base: str | None = None,
) -> list[str]:
    """Список base URL для images failover. Env DEROUTER_IMAGE_BASE_URL — override (comma-separated)."""
    env_raw = os.environ.get(DEFAULT_IMAGE_BASE_ENV, "").strip()
    if env_raw:
        from_env = [
            normalize_image_base_url(part)
            for part in env_raw.split(",")
            if part.strip()
        ]
        return list(dict.fromkeys(u for u in from_env if u))

    ordered: list[str] = []
    for candidate in (
        primary_base,
        fallback_base,
        *DEFAULT_IMAGE_BASE_URLS,
    ):
        if not candidate:
            continue
        normalized = normalize_image_base_url(str(candidate))
        if normalized and normalized not in ordered:
            ordered.append(normalized)
    return ordered


def should_failover_to_next_host(status: int, body: str) -> bool:
    if is_retryable_http(status):
        return True
    if status == 400:
        lowered = body.lower()
        markers = (
            "discontinued",
            "not available",
            "not supported",
            "must be '",
            "must be \"",
        )
        return any(marker in lowered for marker in markers)
    return False


def _guess_mime(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(str(path))
    return guessed or "application/octet-stream"


def expand_input_urls(input_urls: list[Any]) -> list[str]:
    live = resolve_public_base_from_env()
    out: list[str] = []
    for raw in input_urls:
        url = str(raw or "").strip()
        if not url:
            continue
        if SITE_BASE_PLACEHOLDER in url:
            if not live:
                raise DerouterApiError(
                    f"batch input_urls contain {SITE_BASE_PLACEHOLDER} but PUBLIC_SITE_URL/WP_SITE_URL is unset"
                )
            url = expand_site_base(url, live)
        out.append(url)
    return out


def batch_mcp_args(batch_path: Path) -> dict[str, Any]:
    batch = load_json(batch_path)
    jobs = batch.get("jobs")
    if not isinstance(jobs, list) or len(jobs) != 1:
        raise DerouterApiError(f"Expected exactly one job in {batch_path}")
    job = jobs[0]
    if not isinstance(job, dict):
        raise DerouterApiError(f"Invalid job entry in {batch_path}")
    args = job.get("mcp_args")
    if not isinstance(args, dict):
        raise DerouterApiError(f"Missing jobs[0].mcp_args in {batch_path}")

    prompt = str(args.get("prompt") or "").strip()
    if not prompt:
        raise DerouterApiError("Missing prompt in jobs[0].mcp_args")
    out: dict[str, Any] = {
        "prompt": prompt,
        "aspect_ratio": args.get("aspect_ratio") or "16:9",
        "resolution": args.get("resolution") or "2K",
    }
    input_urls = args.get("input_urls")
    if isinstance(input_urls, list) and input_urls:
        expanded = expand_input_urls(input_urls)
        if expanded:
            out["input_urls"] = expanded
    return out


def resolve_local_reference_paths(
    *,
    root: Path,
    batch_path: Path,
) -> list[Path]:
    """Local identity-real files for /images/edits — never input_urls or data-URL JSON."""
    batch = load_json(batch_path)
    candidates: list[str] = []
    if batch.get("prefer_local_reference"):
        local_ref = str(batch.get("local_reference") or "").strip()
        if local_ref:
            candidates.append(local_ref)
    identity_local = str(batch.get("identity_reference_local") or "").strip()
    if identity_local and identity_local not in candidates:
        candidates.append(identity_local)
    if not candidates:
        return []
    paths: list[Path] = []
    for rel in candidates:
        path = Path(rel)
        if not path.is_absolute():
            path = root / path
        if path.is_file():
            paths.append(path)
            break
    if not paths:
        raise DerouterApiError(
            f"prefer_local_reference/identity_reference_local set but file missing: {candidates[0]}"
        )
    return paths


def http_json_post(
    url: str,
    api_key: str,
    payload: dict[str, Any],
    *,
    timeout: int,
) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        snippet = body[:500]
        if should_failover_to_next_host(exc.code, body):
            if exc.code == 400:
                raise DerouterHostFailed(
                    f"Derouter HTTP {exc.code}: {snippet}", status=exc.code
                ) from exc
            raise DerouterRetryable(f"Derouter HTTP {exc.code}: {snippet}", status=exc.code) from exc
        raise DerouterApiError(f"Derouter HTTP {exc.code}: {snippet}") from exc
    except urllib.error.URLError as exc:
        raise DerouterRetryable(f"Derouter network error: {exc.reason}") from exc

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise DerouterApiError(f"Derouter returned non-JSON: {body[:500]}") from exc
    if not isinstance(parsed, dict):
        raise DerouterApiError("Derouter returned a non-object JSON response")
    return parsed


def http_multipart_post(
    url: str,
    api_key: str,
    *,
    fields: dict[str, str],
    files: list[tuple[str, Path]],
    timeout: int,
) -> dict[str, Any]:
    """Multipart POST; multi-ref uses repeated image[] parts per Derouter docs."""
    boundary = "----ExcaliburDerouterBoundary"
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
                f"{value}\r\n"
            ).encode("utf-8")
        )
    for field_name, file_path in files:
        mime = _guess_mime(file_path)
        file_bytes = file_path.read_bytes()
        parts.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{field_name}"; filename="{file_path.name}"\r\n'
                f"Content-Type: {mime}\r\n\r\n"
            ).encode("utf-8")
        )
        parts.append(file_bytes)
        parts.append(b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    body = b"".join(parts)

    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        snippet = err_body[:500]
        if should_failover_to_next_host(exc.code, err_body):
            if exc.code == 400:
                raise DerouterHostFailed(
                    f"Derouter edits HTTP {exc.code}: {snippet}", status=exc.code
                ) from exc
            raise DerouterRetryable(
                f"Derouter edits HTTP {exc.code}: {snippet}", status=exc.code
            ) from exc
        raise DerouterApiError(f"Derouter edits HTTP {exc.code}: {snippet}") from exc
    except urllib.error.URLError as exc:
        raise DerouterRetryable(f"Derouter edits network error: {exc.reason}") from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DerouterApiError(f"Derouter edits returned non-JSON: {raw[:500]}") from exc
    if not isinstance(parsed, dict):
        raise DerouterApiError("Derouter edits returned a non-object JSON response")
    return parsed


def parse_image_response(parsed: dict[str, Any]) -> bytes:
    """Derouter images API returns data[0].b64_json (PNG), not a URL."""
    data = parsed.get("data")
    if not isinstance(data, list) or not data:
        raise DerouterApiError(f"Derouter response missing data[]: {list(parsed.keys())}")
    item = data[0]
    if not isinstance(item, dict):
        raise DerouterApiError("Derouter data[0] is not an object")
    b64 = item.get("b64_json")
    if not b64:
        raise DerouterApiError("Derouter response missing data[0].b64_json (URL field not used)")
    try:
        return base64.b64decode(str(b64))
    except Exception as exc:  # noqa: BLE001
        raise DerouterApiError("Derouter b64_json decode failed") from exc


def call_generations(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    size: str,
    quality: str,
    timeout: int,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/images/generations"
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
    }
    return http_json_post(url, api_key, payload, timeout=timeout)


def call_edits(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    image_paths: list[Path],
    timeout: int,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/images/edits"
    fields = {
        "model": model,
        "prompt": prompt,
    }
    file_field = "image[]" if len(image_paths) > 1 else "image"
    files = [(file_field, path) for path in image_paths]
    return http_multipart_post(
        url,
        api_key,
        fields=fields,
        files=files,
        timeout=timeout,
    )


def generate_image(
    *,
    root: Path,
    batch_path: Path,
    image_input: dict[str, Any],
    api_key: str,
    model: str,
    size: str,
    quality: str,
    timeout: int,
    base_urls: list[str],
    max_retries: int,
    retry_wait: int,
) -> tuple[bytes, dict[str, Any]]:
    local_refs = resolve_local_reference_paths(root=root, batch_path=batch_path)
    use_edits = bool(local_refs)
    bases = base_urls or list(DEFAULT_IMAGE_BASE_URLS)

    last_error: BaseException | None = None
    attempts = 0
    for base in bases:
        host = urllib.parse.urlparse(base).netloc
        for attempt in range(max_retries + 1):
            attempts += 1
            try:
                if use_edits:
                    parsed = call_edits(
                        base_url=base,
                        api_key=api_key,
                        model=model,
                        prompt=str(image_input["prompt"]),
                        image_paths=local_refs,
                        timeout=timeout,
                    )
                    kind = "edits"
                    ref_names = [p.name for p in local_refs]
                else:
                    parsed = call_generations(
                        base_url=base,
                        api_key=api_key,
                        model=model,
                        prompt=str(image_input["prompt"]),
                        size=size,
                        quality=quality,
                        timeout=timeout,
                    )
                    kind = "generations"
                    ref_names = []
                image_bytes = parse_image_response(parsed)
                meta = {
                    "source": "derouter-api",
                    "model": model,
                    "size": size,
                    "quality": quality,
                    "endpoint": kind,
                    "host": urllib.parse.urlparse(base).netloc,
                    "response_kind": "b64_json",
                    "attempts": attempts,
                }
                if ref_names:
                    meta["local_reference"] = ref_names[0]
                    if len(ref_names) > 1:
                        meta["local_references"] = ref_names
                return image_bytes, meta
            except DerouterHostFailed as exc:
                last_error = exc
                print(
                    f"Derouter host failed ({exc}); host={host} — failover to next base URL",
                    flush=True,
                )
                break
            except DerouterRetryable as exc:
                last_error = exc
                print(
                    f"Derouter retryable ({exc}); host={host} "
                    f"attempt={attempt + 1}/{max_retries + 1}",
                    flush=True,
                )
                if attempt < max_retries and retry_wait > 0:
                    time.sleep(retry_wait)
                continue
            except DerouterApiError:
                raise
        else:
            continue
        # host failed — next base URL
        continue

    print(
        "Derouter /images/* exhausted on all hosts — fallback to /responses image_generation",
        flush=True,
    )
    try:
        return generate_image_via_responses(
            prompt=str(image_input["prompt"]),
            api_key=api_key,
            responses_model=default_responses_model(),
            size=size,
            timeout=timeout,
            base_urls=bases,
            image_paths=local_refs,
        )
    except DerouterApiError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise DerouterApiError(f"Derouter responses fallback failed: {exc}") from exc


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate one quad canvas via Derouter REST image API"
    )
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--batch", default="cover/quad-mcp-batch.json")
    ap.add_argument("--result", default="cover/quad-mcp-result.json")
    ap.add_argument("--api-key-env", default=DEFAULT_API_KEY_ENV)
    ap.add_argument("--primary-base", default=PRIMARY_DIRECT_BASE)
    ap.add_argument("--fallback-base", default=FALLBACK_DIRECT_BASE)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    ap.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES)
    ap.add_argument("--retry-wait", type=int, default=DEFAULT_RETRY_WAIT_SECONDS)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    batch_path = resolve_path(root, args.article_dir, args.batch)
    result_path = resolve_path(root, args.article_dir, args.result)

    try:
        image_input = batch_mcp_args(batch_path)
        batch_meta = load_json(batch_path)
        model = default_model()
        size = default_size()
        quality = default_quality()
        local_refs = resolve_local_reference_paths(root=root, batch_path=batch_path)
        mode = "edits" if local_refs else "generations"

        base_urls = resolve_image_base_urls(
            primary_base=args.primary_base,
            fallback_base=args.fallback_base,
        )
        dry_payload = {
            "mode": mode,
            "model": model,
            "size": size,
            "quality": quality,
            "image_base_urls": base_urls,
            "timeout_seconds": max(MIN_TIMEOUT_SECONDS, int(args.timeout)),
            "prompt_chars": len(str(image_input.get("prompt") or "")),
            "local_references": [
                str(p.relative_to(root)) if p.is_relative_to(root) else str(p) for p in local_refs
            ],
            "responses_model": default_responses_model(),
            "note": "images REST failover; then /responses image_generation if discontinued",
        }
        if args.dry_run:
            print(json.dumps(dry_payload, ensure_ascii=False, indent=2))
            return 0

        api_key = resolve_derouter_api_key(args.api_key_env)
        if not api_key:
            print(
                "❌ DEROUTER API KEY MISSING: set DEROUTER_API_KEY in Cloud Secrets/env; "
                "the key must not be committed or printed.",
                file=sys.stderr,
            )
            return 1

        image_bytes, meta = generate_image(
            root=root,
            batch_path=batch_path,
            image_input=image_input,
            api_key=api_key,
            model=model,
            size=size,
            quality=quality,
            timeout=max(MIN_TIMEOUT_SECONDS, int(args.timeout)),
            base_urls=base_urls,
            max_retries=max(0, int(args.max_retries)),
            retry_wait=max(0, int(args.retry_wait)),
        )

        output_canvas = str(batch_meta.get("output_canvas") or "").strip()
        if output_canvas:
            canvas_path = article_dir / output_canvas
        else:
            canvas_index = int(batch_meta.get("canvas_index") or 1)
            canvas_path = article_dir / "cover" / f"canvas-quad-{canvas_index:02d}.png"
        canvas_path.parent.mkdir(parents=True, exist_ok=True)
        canvas_path.write_bytes(image_bytes)
        rel_canvas = str(canvas_path.relative_to(article_dir))

        record: dict[str, Any] = {
            "local_path": rel_canvas,
            "source": "derouter-api",
            "model": model,
            "size": size,
            "quality": quality,
            "bytes": len(image_bytes),
            **meta,
        }
        save_json(result_path, record)
        print(f"OK local_path={rel_canvas} bytes={len(image_bytes)} mode={mode}")
        print(f"OK result={result_path}")
        return 0
    except DerouterRetryable as exc:
        print(
            f"❌ DEROUTER IMAGE BLOCKER: {exc}\n"
            "Retry hosts; /responses image_generation is auto-fallback when /images/* discontinued. "
            "Then DEROUTER MCP. Kie FORBIDDEN. No PIL mashup.",
            file=sys.stderr,
        )
        return 1
    except DerouterApiError as exc:
        print(
            f"❌ DEROUTER IMAGE BLOCKER: {exc}\n"
            "Retry hosts; /responses image_generation is auto-fallback when /images/* discontinued. "
            "Then DEROUTER MCP. Kie FORBIDDEN. No PIL mashup.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
