#!/usr/bin/env python3
"""Derouter Responses API image_generation fallback when /images/generations is discontinued.

Uses POST {base}/responses with tools=[{type: image_generation}] and optional
input_image for i2i identity lock. Auth: DEROUTER_API_KEY / DEROUTE_API_KEY.
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

DEFAULT_BASE = "https://api-direct.derouter.ai/openai/v1"
DEFAULT_MODEL = "gpt-5.4"
DEFAULT_TIMEOUT = 600
DEFAULT_REF = "memory/cover/assets/identity-real/face-studio-2026-06-23.jpg"
TARGET_SIZE = (1200, 675)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def resolve_api_key() -> str:
    for name in ("DEROUTER_API_KEY", "DEROUTE_API_KEY"):
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return ""


def generate_cover_bytes(
    prompt: str,
    *,
    ref_path: Path | None,
    api_key: str,
    model: str = DEFAULT_MODEL,
    base_url: str = DEFAULT_BASE,
    timeout: int = DEFAULT_TIMEOUT,
) -> bytes:
    content: list[dict[str, Any]] = [{"type": "input_text", "text": prompt}]
    if ref_path and ref_path.is_file():
        ref_b64 = base64.b64encode(ref_path.read_bytes()).decode()
        content.append(
            {
                "type": "input_image",
                "detail": "high",
                "image_url": f"data:image/jpeg;base64,{ref_b64}",
            }
        )
    payload = {
        "model": model,
        "input": [{"role": "user", "content": content}],
        "tools": [{"type": "image_generation"}],
    }
    url = base_url.rstrip("/") + "/responses"
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Derouter responses image HTTP {exc.code}: {err[:500]}") from exc

    if data.get("status") != "completed":
        raise RuntimeError(f"Derouter responses status={data.get('status')!r}")

    for item in data.get("output") or []:
        if item.get("type") == "image_generation_call" and item.get("result"):
            return base64.b64decode(item["result"])
    raise RuntimeError("Derouter responses: no image_generation_call.result in output")


def resize_cover(png_bytes: bytes, size: tuple[int, int] = TARGET_SIZE) -> bytes:
    from io import BytesIO

    from PIL import Image

    img = Image.open(BytesIO(png_bytes)).convert("RGB")
    fitted = img.resize(size, Image.Resampling.LANCZOS)
    out = BytesIO()
    fitted.save(out, format="PNG", optimize=True)
    return out.getvalue()


def build_prompt_for_article(article_dir: Path, root: Path) -> str:
    sys.path.insert(0, str(root / "scripts"))
    from excalibur_blog_cover_quad_prompt import build_solo_cover_prompt, load_json

    manifest_path = article_dir / "cover" / "quad-manifest.json"
    manifest = load_json(manifest_path)
    style = load_json(root / manifest.get("style_file", "memory/cover/quad-style-the-rieltor.json"))
    hero = load_json(root / manifest.get("blog_hero", "memory/cover/blog-hero.json"))
    design = load_json(root / "memory/cover/cover-design-code.json")
    return build_solo_cover_prompt(manifest, style, hero, design)


def stamp_qa(article_dir: Path, root: Path, topic_id: str) -> dict[str, Any]:
    sys.path.insert(0, str(root / "scripts"))
    from excalibur_blog_cover_qa_pixels import analyze_cover_pixels, load_json, stamp_cover_qa_json

    cover_path = article_dir / "cover" / "cover.png"
    manifest = load_json(article_dir / "cover" / "quad-manifest.json")
    pixel = analyze_cover_pixels(cover_path, manifest=manifest)
    stamp_cover_qa_json(article_dir, pixel, topic_id=topic_id)
    qa_path = article_dir / "cover" / "cover_qa.json"
    qa = load_json(qa_path)
    qa["gate_status"] = "PASS" if pixel.status == "PASS" else "FAIL"
    qa["gate_errors"] = pixel.errors
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": pixel.status, "errors": pixel.errors, "md5": qa.get("cover_md5")}


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate solo cover via Derouter Responses API")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--ref", default=DEFAULT_REF)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    ap.add_argument("--prompt-suffix", default="", help="Extra prompt lines appended")
    ap.add_argument("--max-attempts", type=int, default=3)
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    api_key = resolve_api_key()
    if not api_key:
        print("DEROUTER API KEY MISSING", file=sys.stderr)
        return 1

    prompt = build_prompt_for_article(article_dir, root)
    if args.prompt_suffix.strip():
        prompt = prompt + "\n" + args.prompt_suffix.strip()
    ref_path = root / args.ref
    print(f"prompt_chars={len(prompt)} ref={ref_path.is_file()}", flush=True)

    meta = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    topic_id = str(meta.get("topic_id") or "")

    last_errors: list[str] = []
    for attempt in range(1, max(1, args.max_attempts) + 1):
        print(f"attempt {attempt}/{args.max_attempts}", flush=True)
        raw = generate_cover_bytes(
            prompt,
            ref_path=ref_path,
            api_key=api_key,
            model=args.model,
            base_url=args.base_url,
            timeout=args.timeout,
        )
        png = resize_cover(raw)
        cover_path = article_dir / "cover" / "cover.png"
        cover_path.parent.mkdir(parents=True, exist_ok=True)
        cover_path.write_bytes(png)
        print(f"OK cover.png bytes={len(png)} size={TARGET_SIZE}")

        qa = stamp_qa(article_dir, root, topic_id)
        if qa["status"] == "PASS":
            print(f"OK cover_qa PASS md5={qa['md5']}")
            return 0
        last_errors = list(qa["errors"])
        print("WARN pixel QA fail:", "; ".join(last_errors), flush=True)

    print("FAIL pixel QA:", "; ".join(last_errors), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
