#!/usr/bin/env python3
"""Probe Derouter image base URLs with minimal /images/generations request.

Records HTTP status + body snippet per host. Use before cover regen when image API fails.
Auth: DEROUTER_API_KEY (Cloud Secrets). Never print the key.
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

# Импорт канонического списка и env override из image API скрипта.
from excalibur_blog_derouter_gpt_image2_api import (
    DEFAULT_IMAGE_BASE_ENV,
    DEFAULT_MODEL_ENV,
    default_model,
    resolve_image_base_urls,
    should_failover_to_next_host,
)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def probe_host(
    base_url: str,
    api_key: str,
    model: str,
    *,
    timeout: int,
    prompt: str,
    size: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/images/generations"
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
    }
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            row["http_status"] = resp.status
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

    api_key = os.environ.get("DEROUTER_API_KEY", "").strip()
    if not api_key:
        print("❌ DEROUTER API KEY MISSING", file=sys.stderr)
        return 1

    try:
        model = default_model()
    except Exception as exc:  # noqa: BLE001
        print(f"❌ {exc}", file=sys.stderr)
        return 1

    bases = resolve_image_base_urls()
    env_override = os.environ.get(DEFAULT_IMAGE_BASE_ENV, "").strip()

    print(f"Probing {len(bases)} base URL(s), timeout={args.timeout}s")
    print()

    results: list[dict[str, Any]] = []
    first_ok: str | None = None
    for base in bases:
        row = probe_host(
            base,
            api_key,
            model,
            timeout=max(30, int(args.timeout)),
            prompt=args.prompt,
            size=args.size,
        )
        results.append(row)
        status = row.get("http_status")
        snippet = row.get("body_snippet", "")
        ok = row.get("ok")
        print(f"| {row['host']} | HTTP {status} | ok={ok} | {snippet[:120]}")
        if ok and not first_ok:
            first_ok = base

    report = {
        "env_image_base": env_override or None,
        "first_ok_base_url": first_ok,
        "results": results,
    }
    if args.json_out:
        out_path = Path(args.json_out)
        if not out_path.is_absolute():
            out_path = project_root() / out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nJSON: {out_path}")

    if first_ok:
        print(f"\nFIRST OK: {first_ok}")
        return 0

    print("\n❌ DEROUTER IMAGE BLOCKER: no base URL returned a real image", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
