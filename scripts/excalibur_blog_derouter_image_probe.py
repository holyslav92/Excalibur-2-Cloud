#!/usr/bin/env python3
"""Probe Derouter image paths: /images/generations then /responses image_generation.

Records HTTP status + body snippet per host. Optional cf-api balance check.
Auth: DEROUTER_API_KEY or DEROUTE_API_KEY (Cloud Secrets). Never print the key.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from excalibur_blog_derouter_gpt_image2_api import (
    DEFAULT_IMAGE_BASE_ENV,
    RESPONSES_SUFFIX,
    default_model,
    default_responses_model,
    resolve_derouter_api_key,
    resolve_image_base_urls,
    should_failover_to_next_host,
)

MANAGEMENT_API_BASE = "https://cf-api.derouter.ai"
IMAGE_GENERATIONS_SUFFIX = "/images/generations"


def image_api_url(base_url: str) -> tuple[str, str]:
    """base_url уже с /openai/v1 → только /images/generations; иначе полный путь."""
    base = base_url.rstrip("/")
    if base.endswith("/openai/v1"):
        return f"{base}/images/generations", "/openai/v1/images/generations"
    return f"{base}/openai/v1/images/generations", "/openai/v1/images/generations"


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def probe_balance(api_key: str) -> dict[str, Any]:
    url = f"{MANAGEMENT_API_BASE}/balance"
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    row: dict[str, Any] = {
        "host": "cf-api.derouter.ai",
        "path": "/balance",
        "method": "GET",
    }
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            row["http_status"] = resp.status
            row["body_snippet"] = body[:200]
            row["ok"] = resp.status == 200
    except urllib.error.HTTPError as exc:
        row["http_status"] = exc.code
        row["body_snippet"] = exc.read().decode("utf-8", errors="replace")[:200]
        row["ok"] = False
    except Exception as exc:  # noqa: BLE001
        row["http_status"] = None
        row["body_snippet"] = f"{type(exc).__name__}: {exc}"
        row["ok"] = False
    return row


def probe_generations(
    base_url: str,
    api_key: str,
    model: str,
    *,
    timeout: int,
    prompt: str,
    size: str,
) -> dict[str, Any]:
    path = IMAGE_GENERATIONS_SUFFIX
    url, display_path = image_api_url(base_url)
    row_path = display_path
    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": "auto",
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    row: dict[str, Any] = {
        "base_url": base_url,
        "host": urllib.parse.urlparse(base_url).netloc,
        "path": row_path,
        "method": "POST",
    }
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = response.read().decode("utf-8")
            row["http_status"] = response.status
            parsed = json.loads(body)
            data_list = parsed.get("data", [])
            b64 = ""
            if data_list and isinstance(data_list[0], dict):
                b64 = str(data_list[0].get("b64_json") or "")
            row["has_b64_json"] = bool(b64)
            row["decoded_bytes"] = len(base64.b64decode(b64)) if b64 else 0
            row["body_snippet"] = body[:240] if not b64 else f"OK b64_json len={len(b64)}"
            row["ok"] = row["has_b64_json"] and row["decoded_bytes"] > 0
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        row["http_status"] = exc.code
        row["body_snippet"] = err_body[:400]
        row["failover_candidate"] = should_failover_to_next_host(exc.code, err_body)
        row["ok"] = False
    except Exception as exc:  # noqa: BLE001
        row["http_status"] = None
        row["body_snippet"] = f"{type(exc).__name__}: {exc}"
        row["ok"] = False
    return row


def probe_responses(
    base_url: str,
    api_key: str,
    model: str,
    *,
    timeout: int,
    prompt: str,
) -> dict[str, Any]:
    """POST /openai/v1/responses + tools image_generation."""
    import urllib.parse

    path = f"/openai/v1{RESPONSES_SUFFIX}"
    url = f"{base_url.rstrip('/')}{RESPONSES_SUFFIX}"
    payload = {
        "model": model,
        "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
        "tools": [{"type": "image_generation"}],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    row: dict[str, Any] = {
        "base_url": base_url,
        "host": urllib.parse.urlparse(base_url).netloc,
        "path": path,
        "method": "POST",
        "endpoint": "responses",
        "tool": "image_generation",
    }
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = response.read().decode("utf-8")
            row["http_status"] = response.status
            parsed = json.loads(body)
            b64 = ""
            for item in parsed.get("output") or []:
                if item.get("type") == "image_generation_call" and item.get("result"):
                    b64 = str(item["result"])
                    break
            row["has_b64_json"] = bool(b64)
            row["decoded_bytes"] = len(base64.b64decode(b64)) if b64 else 0
            row["body_snippet"] = (
                body[:240] if not b64 else f"OK image_generation_call b64 len={len(b64)}"
            )
            row["ok"] = (
                parsed.get("status") == "completed"
                and row["has_b64_json"]
                and row["decoded_bytes"] > 0
            )
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        row["http_status"] = exc.code
        row["body_snippet"] = err_body[:400]
        row["failover_candidate"] = should_failover_to_next_host(exc.code, err_body)
        row["ok"] = False
    except Exception as exc:  # noqa: BLE001
        row["http_status"] = None
        row["body_snippet"] = f"{type(exc).__name__}: {exc}"
        row["ok"] = False
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description="Probe Derouter image REST base URLs")
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument(
        "--prompt",
        default="Minimal probe: simple blue square on white background, no text",
    )
    ap.add_argument("--json-out", default="", help="Optional path to write probe JSON")
    args = ap.parse_args()

    api_key = resolve_derouter_api_key()
    if not api_key:
        print("❌ DEROUTER API KEY MISSING (DEROUTER_API_KEY / DEROUTE_API_KEY)", file=sys.stderr)
        return 1

    try:
        model = default_model()
    except Exception as exc:  # noqa: BLE001
        print(f"❌ {exc}", file=sys.stderr)
        return 1

    bases = resolve_image_base_urls()
    env_override = os.environ.get(DEFAULT_IMAGE_BASE_ENV, "").strip()
    responses_model = default_responses_model()

    balance = probe_balance(api_key)
    print(
        f"Management GET {balance['host']}{balance['path']} -> HTTP {balance.get('http_status')} "
        f"ok={balance.get('ok')} {balance.get('body_snippet', '')[:120]}"
    )
    print()
    print(f"Probing {len(bases)} image base URL(s), timeout={args.timeout}s")
    print("| host | path | HTTP | ok | snippet |")
    print("|------|------|------|----|---------|")

    results: list[dict[str, Any]] = []
    first_ok: str | None = None
    first_ok_path: str | None = None
    for base in bases:
        row = probe_generations(
            base,
            api_key,
            model,
            timeout=max(30, int(args.timeout)),
            prompt=args.prompt,
            size=args.size,
        )
        results.append(row)
        status = row.get("http_status")
        snippet = str(row.get("body_snippet", ""))[:100]
        ok = row.get("ok")
        print(f"| {row['host']} | {row['path']} | {status} | {ok} | {snippet} |")
        if ok and not first_ok:
            first_ok = base
            first_ok_path = row["path"]

    responses_results: list[dict[str, Any]] = []
    if not first_ok:
        print()
        print(
            f"Probing /responses image_generation (model={responses_model}), "
            f"timeout={args.timeout}s"
        )
        print("| host | path | HTTP | ok | snippet |")
        print("|------|------|------|----|---------|")
        for base in bases:
            row = probe_responses(
                base,
                api_key,
                responses_model,
                timeout=max(30, int(args.timeout)),
                prompt=args.prompt,
            )
            responses_results.append(row)
            status = row.get("http_status")
            snippet = str(row.get("body_snippet", ""))[:100]
            ok = row.get("ok")
            print(f"| {row['host']} | {row['path']} | {status} | {ok} | {snippet} |")
            if ok and not first_ok:
                first_ok = base
                first_ok_path = row["path"]

    report = {
        "management_balance": balance,
        "env_image_base": env_override or None,
        "first_ok_base_url": first_ok,
        "first_ok_path": first_ok_path,
        "image_generations_path": "/openai/v1/images/generations",
        "responses_path": "/openai/v1/responses",
        "responses_model": responses_model,
        "image_model": model,
        "results": results,
        "responses_results": responses_results,
    }
    if args.json_out:
        out_path = Path(args.json_out)
        if not out_path.is_absolute():
            out_path = project_root() / out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nJSON: {out_path}")

    if first_ok:
        print(f"\nFIRST OK base_url: {first_ok} path={first_ok_path}")
        return 0

    print(
        "\n❌ DEROUTER IMAGE BLOCKER: no /images/generations and no /responses image_generation PNG",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
