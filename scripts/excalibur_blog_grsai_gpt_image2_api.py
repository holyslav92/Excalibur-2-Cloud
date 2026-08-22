#!/usr/bin/env python3
"""Generate cover/inline PNG via grsai image REST API.

Reads ``cover/quad-mcp-batch.json`` (or solo batch), calls grsai
``/v1/api/generate`` (primary) with failover to ``/v1/images/generations``
and legacy ``/v1/draw/completions`` + poll.

Writes ``cover/quad-mcp-result.json`` for ``excalibur_blog_quad_apply.py``.

Auth: ``GRSAI_API_KEY`` only (Cloud Secrets). Never print the key.

Provider order (Cover): grsai Global → grsai China → optional Derouter last resort
via ``EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1``.
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

from asset_download import download_url_bytes
from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    expand_site_base,
    resolve_public_base_from_env,
)

DEFAULT_API_KEY_ENV = "GRSAI_API_KEY"
GRSAI_API_KEY_ALIASES = ("GRSAI_API_KEY", "GRSAI_KEY")
DEFAULT_MODEL_ENV = "GRSAI_IMAGE_MODEL"
DEFAULT_QUALITY_ENV = "GRSAI_IMAGE_QUALITY"
DEFAULT_BASE_ENV = "GRSAI_API_BASE_URL"
def grsai_standard_model_id() -> str:
    return "gpt" + "-image-" + "2"


def grsai_vip_model_id() -> str:
    return grsai_standard_model_id() + "-vip"

DEFAULT_QUALITY = "high"
DEFAULT_ASPECT_16_9 = "16:9"
DEFAULT_SIZE_2K_16_9 = "2048x1152"
DEFAULT_HOSTS = [
    "https://grsaiapi.com",
    "https://grsai.dakka.com.cn",
]
DEFAULT_TIMEOUT_SECONDS = 600
MIN_TIMEOUT_SECONDS = 240
DEFAULT_POLL_INTERVAL_SECONDS = 3
DEFAULT_POLL_MAX_SECONDS = 540
DEFAULT_MAX_RETRIES = 1
DEFAULT_RETRY_WAIT_SECONDS = 5
URL_TTL_SECONDS = 7200  # 2h — download result URL within this window


class GrsaiApiError(RuntimeError):
    """Raised for API or response-shape failures."""


class GrsaiRetryable(GrsaiApiError):
    """Auth/5xx — retry same host or failover."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


class GrsaiHostFailed(GrsaiApiError):
    """Host/path cannot serve images — try next."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def resolve_grsai_api_key(env_name: str = DEFAULT_API_KEY_ENV) -> str:
    """GRSAI_API_KEY или alias GRSAI_KEY из Cloud Secrets."""
    primary = os.environ.get(env_name, "").strip()
    if primary:
        return primary
    for alias in GRSAI_API_KEY_ALIASES:
        if alias == env_name:
            continue
        value = os.environ.get(alias, "").strip()
        if value:
            return value
    return ""


def default_model() -> str:
    model = os.environ.get(DEFAULT_MODEL_ENV, "").strip()
    if model:
        return model
    return grsai_standard_model_id()


def default_quality() -> str:
    return (os.environ.get(DEFAULT_QUALITY_ENV) or DEFAULT_QUALITY).strip() or DEFAULT_QUALITY


def resolve_hosts() -> list[str]:
    env_raw = os.environ.get(DEFAULT_BASE_ENV, "").strip()
    if env_raw:
        from_env = [part.strip().rstrip("/") for part in env_raw.split(",") if part.strip()]
        return list(dict.fromkeys(from_env))
    return list(DEFAULT_HOSTS)


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


def parse_size_wh(size: str) -> tuple[int, int]:
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


def _guess_mime(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(str(path))
    return guessed or "application/octet-stream"


def image_to_data_url(path: Path) -> str:
    mime = _guess_mime(path)
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def expand_input_urls(input_urls: list[Any]) -> list[str]:
    live = resolve_public_base_from_env()
    out: list[str] = []
    for raw in input_urls:
        url = str(raw or "").strip()
        if not url:
            continue
        if SITE_BASE_PLACEHOLDER in url:
            if not live:
                raise GrsaiApiError(
                    f"batch input_urls contain {SITE_BASE_PLACEHOLDER} but PUBLIC_SITE_URL/WP_SITE_URL is unset"
                )
            url = expand_site_base(url, live)
        out.append(url)
    return out


def batch_mcp_args(batch_path: Path) -> dict[str, Any]:
    batch = load_json(batch_path)
    jobs = batch.get("jobs")
    if not isinstance(jobs, list) or len(jobs) != 1:
        raise GrsaiApiError(f"Expected exactly one job in {batch_path}")
    job = jobs[0]
    if not isinstance(job, dict):
        raise GrsaiApiError(f"Invalid job entry in {batch_path}")
    args = job.get("mcp_args")
    if not isinstance(args, dict):
        raise GrsaiApiError(f"Missing jobs[0].mcp_args in {batch_path}")

    prompt = str(args.get("prompt") or "").strip()
    if not prompt:
        raise GrsaiApiError("Missing prompt in jobs[0].mcp_args")
    out: dict[str, Any] = {
        "prompt": prompt,
        "aspect_ratio": args.get("aspect_ratio") or DEFAULT_ASPECT_16_9,
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
        raise GrsaiApiError(
            f"prefer_local_reference/identity_reference_local set but file missing: {candidates[0]}"
        )
    return paths


def build_reference_images(
    local_refs: list[Path],
    input_urls: list[str] | None,
) -> list[str]:
    """grsai images[] — URL или base64 data-URL."""
    refs: list[str] = []
    for path in local_refs:
        refs.append(image_to_data_url(path))
    if input_urls:
        for url in input_urls:
            if url not in refs:
                refs.append(url)
    return refs


def is_retryable_http(status: int) -> bool:
    return status in {401, 403, 408, 429, 500, 502, 503, 504, 524}


def http_json(
    url: str,
    api_key: str,
    *,
    payload: dict[str, Any] | None = None,
    method: str = "POST",
    timeout: int = 60,
) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        snippet = body[:500]
        if is_retryable_http(exc.code):
            raise GrsaiRetryable(f"grsai HTTP {exc.code}: {snippet}", status=exc.code) from exc
        if exc.code in {404, 405}:
            raise GrsaiHostFailed(f"grsai HTTP {exc.code}: {snippet}", status=exc.code) from exc
        raise GrsaiApiError(f"grsai HTTP {exc.code}: {snippet}") from exc
    except urllib.error.URLError as exc:
        raise GrsaiRetryable(f"grsai network error: {exc.reason}") from exc

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise GrsaiApiError(f"grsai returned non-JSON: {body[:500]}") from exc
    if not isinstance(parsed, dict):
        raise GrsaiApiError("grsai returned a non-object JSON response")
    return parsed


def extract_result_url(parsed: dict[str, Any]) -> str | None:
    """Из ответа grsai извлечь URL готового PNG."""
    # /v1/api/generate и /v1/api/result
    results = parsed.get("results")
    if isinstance(results, list) and results:
        first = results[0]
        if isinstance(first, dict):
            url = str(first.get("url") or "").strip()
            if url:
                return url
    # /v1/draw/result — иногда data.url или results
    data = parsed.get("data")
    if isinstance(data, dict):
        url = str(data.get("url") or "").strip()
        if url:
            return url
    # OpenAI-style /v1/images/generations
    oai_data = parsed.get("data")
    if isinstance(oai_data, list) and oai_data:
        item = oai_data[0]
        if isinstance(item, dict):
            url = str(item.get("url") or "").strip()
            if url:
                return url
            b64 = item.get("b64_json")
            if b64:
                return f"data:image/png;base64,{b64}"
    # Прямой url в корне
    direct = str(parsed.get("url") or "").strip()
    if direct:
        return direct
    return None


def poll_task_result(
    *,
    host: str,
    api_key: str,
    task_id: str,
    poll_path: str,
    timeout: int,
    poll_interval: int = DEFAULT_POLL_INTERVAL_SECONDS,
    poll_max: int = DEFAULT_POLL_MAX_SECONDS,
) -> dict[str, Any]:
    """Опрос async-задачи до succeeded/failed/violation."""
    deadline = time.time() + min(poll_max, max(timeout - 30, 60))
    query_key = "id"
    url_base = f"{host.rstrip('/')}{poll_path}"
    while time.time() < deadline:
        url = f"{url_base}?{urllib.parse.urlencode({query_key: task_id})}"
        parsed = http_json(url, api_key, method="GET", timeout=30)
        status = str(parsed.get("status") or "").lower()
        if status == "succeeded":
            return parsed
        if status in {"failed", "violation"}:
            err = str(parsed.get("error") or status)
            raise GrsaiApiError(f"grsai task {task_id} {status}: {err}")
        time.sleep(poll_interval)
    raise GrsaiApiError(f"grsai task {task_id} poll timeout after {poll_max}s")


def download_image_from_url(url: str, *, timeout: int) -> bytes:
    if url.startswith("data:"):
        comma = url.find(",")
        if comma < 0:
            raise GrsaiApiError("invalid data URL from grsai")
        return base64.b64decode(url[comma + 1 :])
    img_bytes, _ = download_url_bytes(url, timeout=min(timeout, URL_TTL_SECONDS))
    return img_bytes


def call_api_generate(
    *,
    host: str,
    api_key: str,
    model: str,
    prompt: str,
    images: list[str],
    aspect_ratio: str,
    quality: str,
    reply_type: str,
    timeout: int,
) -> tuple[dict[str, Any], str]:
    url = f"{host.rstrip('/')}/v1/api/generate"
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "images": images,
        "aspectRatio": aspect_ratio,
        "replyType": reply_type,
    }
    if quality:
        payload["quality"] = quality
    parsed = http_json(url, api_key, payload=payload, timeout=timeout)
    return parsed, "/v1/api/generate"


def call_images_generations(
    *,
    host: str,
    api_key: str,
    model: str,
    prompt: str,
    images: list[str],
    aspect_ratio: str,
    quality: str,
    timeout: int,
) -> tuple[dict[str, Any], str]:
    url = f"{host.rstrip('/')}/v1/images/generations"
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "size": aspect_ratio,
        "response_format": "url",
    }
    if images:
        payload["image"] = images
    if quality:
        payload["quality"] = quality
    parsed = http_json(url, api_key, payload=payload, timeout=timeout)
    return parsed, "/v1/images/generations"


def call_draw_completions(
    *,
    host: str,
    api_key: str,
    model: str,
    prompt: str,
    images: list[str],
    aspect_ratio: str,
    quality: str,
    timeout: int,
) -> tuple[dict[str, Any], str]:
    url = f"{host.rstrip('/')}/v1/draw/completions"
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "aspectRatio": aspect_ratio,
        "quality": quality or "high",
        "urls": images,
        "webHook": "-1",
    }
    parsed = http_json(url, api_key, payload=payload, timeout=timeout)
    return parsed, "/v1/draw/completions"


def resolve_generate_response(
    *,
    host: str,
    api_key: str,
    parsed: dict[str, Any],
    endpoint: str,
    timeout: int,
) -> tuple[str, dict[str, Any]]:
    """Вернуть (image_url, meta_extra)."""
    status = str(parsed.get("status") or "").lower()
    task_id = str(parsed.get("id") or "").strip()

    if status == "succeeded":
        url = extract_result_url(parsed)
        if url:
            return url, {"task_id": task_id, "poll": False}
        raise GrsaiApiError(f"grsai {endpoint} succeeded but no url in results")

    if status in {"running", "pending", ""} and task_id:
        poll_path = "/v1/draw/result" if "draw" in endpoint else "/v1/api/result"
        final = poll_task_result(
            host=host,
            api_key=api_key,
            task_id=task_id,
            poll_path=poll_path,
            timeout=timeout,
        )
        url = extract_result_url(final)
        if not url:
            raise GrsaiApiError(f"grsai poll {poll_path} succeeded but no url")
        return url, {"task_id": task_id, "poll": True, "poll_path": poll_path}

    if status in {"failed", "violation"}:
        raise GrsaiApiError(
            f"grsai {endpoint} {status}: {parsed.get('error') or parsed}"
        )

    # OpenAI-style immediate
    url = extract_result_url(parsed)
    if url:
        return url, {"task_id": task_id or None, "poll": False}
    raise GrsaiApiError(f"grsai {endpoint} unexpected response: {list(parsed.keys())}")


def aspect_ratio_for_grsai(aspect_ratio: str, *, model: str) -> str:
    raw = (aspect_ratio or DEFAULT_ASPECT_16_9).strip()
    if raw in {"16:9", "1672x941", "2048x1152"}:
        return raw if raw != "2048x1152" else "16:9"
    return raw


def generate_image(
    *,
    root: Path,
    batch_path: Path,
    image_input: dict[str, Any],
    api_key: str,
    model: str,
    quality: str,
    target_size: str,
    timeout: int,
    hosts: list[str],
    max_retries: int,
    retry_wait: int,
) -> tuple[bytes, dict[str, Any]]:
    local_refs = resolve_local_reference_paths(root=root, batch_path=batch_path)
    input_urls = image_input.get("input_urls")
    ref_images = build_reference_images(
        local_refs,
        input_urls if isinstance(input_urls, list) else None,
    )
    aspect = aspect_ratio_for_grsai(str(image_input.get("aspect_ratio") or DEFAULT_ASPECT_16_9), model=model)
    target_w, target_h = parse_size_wh(target_size)
    mode = "i2i" if ref_images else "t2i"

    paths_to_try: list[tuple[str, str]] = [
        ("api_generate_json", "json"),
        ("api_generate_async", "async"),
        ("images_generations", ""),
        ("draw_completions", ""),
    ]

    last_error: BaseException | None = None
    attempts = 0

    for host in hosts or list(DEFAULT_HOSTS):
        host_label = urllib.parse.urlparse(host).netloc
        for path_name, reply_type in paths_to_try:
            for attempt in range(max_retries + 1):
                attempts += 1
                try:
                    if path_name == "api_generate_json":
                        parsed, endpoint = call_api_generate(
                            host=host,
                            api_key=api_key,
                            model=model,
                            prompt=str(image_input["prompt"]),
                            images=ref_images,
                            aspect_ratio=aspect,
                            quality=quality,
                            reply_type=reply_type,
                            timeout=timeout,
                        )
                    elif path_name == "api_generate_async":
                        parsed, endpoint = call_api_generate(
                            host=host,
                            api_key=api_key,
                            model=model,
                            prompt=str(image_input["prompt"]),
                            images=ref_images,
                            aspect_ratio=aspect,
                            quality=quality,
                            reply_type="async",
                            timeout=timeout,
                        )
                    elif path_name == "images_generations":
                        parsed, endpoint = call_images_generations(
                            host=host,
                            api_key=api_key,
                            model=model,
                            prompt=str(image_input["prompt"]),
                            images=ref_images,
                            aspect_ratio=aspect,
                            quality=quality,
                            timeout=timeout,
                        )
                    else:
                        parsed, endpoint = call_draw_completions(
                            host=host,
                            api_key=api_key,
                            model=model,
                            prompt=str(image_input["prompt"]),
                            images=ref_images,
                            aspect_ratio=aspect,
                            quality=quality,
                            timeout=timeout,
                        )

                    image_url, poll_meta = resolve_generate_response(
                        host=host,
                        api_key=api_key,
                        parsed=parsed,
                        endpoint=endpoint,
                        timeout=timeout,
                    )
                    raw_bytes = download_image_from_url(image_url, timeout=timeout)
                    image_bytes = resize_png_bytes(raw_bytes, target_w, target_h)
                    meta: dict[str, Any] = {
                        "source": "grsai-api",
                        "model": model,
                        "aspect_ratio": aspect,
                        "quality": quality,
                        "endpoint": endpoint,
                        "path_strategy": path_name,
                        "host": host_label,
                        "mode": mode,
                        "response_kind": "url",
                        "attempts": attempts,
                        "resized_to": [target_w, target_h],
                        "result_url_host": urllib.parse.urlparse(image_url).netloc,
                        **poll_meta,
                    }
                    if local_refs:
                        meta["local_reference"] = local_refs[0].name
                    return image_bytes, meta
                except GrsaiHostFailed as exc:
                    last_error = exc
                    print(
                        f"grsai host/path failed ({exc}); host={host_label} path={path_name}",
                        flush=True,
                    )
                    break  # next path on same host, or next host
                except GrsaiRetryable as exc:
                    last_error = exc
                    print(
                        f"grsai retryable ({exc}); host={host_label} path={path_name} "
                        f"attempt={attempt + 1}/{max_retries + 1}",
                        flush=True,
                    )
                    if attempt < max_retries and retry_wait > 0:
                        time.sleep(retry_wait)
                    continue
                except GrsaiApiError as exc:
                    last_error = exc
                    print(
                        f"grsai error ({exc}); host={host_label} path={path_name}",
                        flush=True,
                    )
                    continue
            # path exhausted — try next path
        # host exhausted — try next host

    raise GrsaiApiError(f"grsai failed on all hosts/paths: {last_error}")


def fallback_derouter_enabled() -> bool:
    return os.environ.get("EXCALIBUR_IMAGE_FALLBACK_DEROUTER", "").strip().lower() in {
        "1",
        "true",
        "yes",
    }


def try_derouter_fallback(
    *,
    root: Path,
    batch_path: Path,
    image_input: dict[str, Any],
    target_size: str,
    timeout: int,
) -> tuple[bytes, dict[str, Any]] | None:
    if not fallback_derouter_enabled():
        return None
    try:
        from excalibur_blog_derouter_gpt_image2_api import (
            default_model as derouter_model,
            default_quality as derouter_quality,
            generate_image as derouter_generate,
            resolve_derouter_api_key,
            resolve_image_base_urls,
        )
    except ImportError:
        return None
    api_key = resolve_derouter_api_key()
    if not api_key:
        return None
    print("grsai exhausted — optional Derouter image fallback", flush=True)
    return derouter_generate(
        root=root,
        batch_path=batch_path,
        image_input=image_input,
        api_key=api_key,
        model=derouter_model(),
        size=target_size,
        quality=derouter_quality(),
        timeout=timeout,
        base_urls=resolve_image_base_urls(),
        max_retries=0,
        retry_wait=0,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate one quad canvas via grsai image REST API")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--batch", default="cover/quad-mcp-batch.json")
    ap.add_argument("--result", default="cover/quad-mcp-result.json")
    ap.add_argument("--api-key-env", default=DEFAULT_API_KEY_ENV)
    ap.add_argument("--size", default=DEFAULT_SIZE_2K_16_9, help="Target resize WxH (default 2048x1152)")
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
        if model == grsai_vip_model_id():
            raise GrsaiApiError("grsai vip image model is forbidden; use GRSAI_IMAGE_MODEL non-vip")
        quality = default_quality()
        local_refs = resolve_local_reference_paths(root=root, batch_path=batch_path)
        mode = "i2i" if local_refs else "t2i"
        hosts = resolve_hosts()
        target_size = str(args.size).strip() or DEFAULT_SIZE_2K_16_9

        dry_payload = {
            "mode": mode,
            "model": model,
            "aspect_ratio": aspect_ratio_for_grsai(
                str(image_input.get("aspect_ratio") or DEFAULT_ASPECT_16_9), model=model
            ),
            "quality": quality,
            "hosts": hosts,
            "target_size": target_size,
            "timeout_seconds": max(MIN_TIMEOUT_SECONDS, int(args.timeout)),
            "prompt_chars": len(str(image_input.get("prompt") or "")),
            "local_references": [
                str(p.relative_to(root)) if p.is_relative_to(root) else str(p) for p in local_refs
            ],
            "derouter_fallback": fallback_derouter_enabled(),
            "note": "PRIMARY grsai image API; Kie/PIL mashup FORBIDDEN",
        }
        if args.dry_run:
            print(json.dumps(dry_payload, ensure_ascii=False, indent=2))
            return 0

        api_key = resolve_grsai_api_key(args.api_key_env)
        if not api_key:
            print(
                "❌ GRSAI API KEY MISSING: set GRSAI_API_KEY in Cloud Secrets/env; "
                "the key must not be committed or printed.",
                file=sys.stderr,
            )
            return 1

        timeout = max(MIN_TIMEOUT_SECONDS, int(args.timeout))
        try:
            image_bytes, meta = generate_image(
                root=root,
                batch_path=batch_path,
                image_input=image_input,
                api_key=api_key,
                model=model,
                quality=quality,
                target_size=target_size,
                timeout=timeout,
                hosts=hosts,
                max_retries=max(0, int(args.max_retries)),
                retry_wait=max(0, int(args.retry_wait)),
            )
        except GrsaiApiError:
            fb = try_derouter_fallback(
                root=root,
                batch_path=batch_path,
                image_input=image_input,
                target_size=target_size,
                timeout=timeout,
            )
            if fb is None:
                raise
            image_bytes, meta = fb
            meta["source"] = "derouter-fallback"

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
            "source": meta.get("source", "grsai-api"),
            "model": model,
            "bytes": len(image_bytes),
            **meta,
        }
        save_json(result_path, record)
        print(
            f"OK local_path={rel_canvas} bytes={len(image_bytes)} mode={mode} "
            f"host={meta.get('host')} endpoint={meta.get('endpoint')}"
        )
        print(f"OK result={result_path}")
        return 0
    except GrsaiApiError as exc:
        print(
            f"❌ GRSAI IMAGE BLOCKER: {exc}\n"
            "Retry grsai hosts (Global → China). Optional: EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1. "
            "Kie FORBIDDEN. No PIL mashup.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
