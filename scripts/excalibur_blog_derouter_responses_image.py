#!/usr/bin/env python3
"""Solo cover regen via Derouter /responses image_generation (used when /images/* discontinued).

Core API lives in excalibur_blog_derouter_gpt_image2_api.generate_image_via_responses.
This CLI builds solo cover prompt from quad-manifest and stamps cover_qa.json.

Auth: DEROUTER_API_KEY / DEROUTE_API_KEY. Kie and PIL mashup FORBIDDEN.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_derouter_gpt_image2_api import (
    DEFAULT_TIMEOUT_SECONDS,
    MIN_TIMEOUT_SECONDS,
    PRIMARY_DIRECT_BASE,
    default_responses_model,
    generate_image_via_responses,
    project_root,
    resolve_derouter_api_key,
    resolve_image_base_urls,
)

DEFAULT_REF = "memory/cover/assets/identity-real/face-studio-2026-06-23.jpg"
SOLO_COVER_SIZE = "1200x675"


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
    ap = argparse.ArgumentParser(
        description="Generate solo 1200×675 cover via Derouter /responses image_generation"
    )
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--ref", default=DEFAULT_REF)
    ap.add_argument("--model", default="", help="Responses chat model (default: DEROUTER_RESPONSES_IMAGE_MODEL)")
    ap.add_argument("--primary-base", default=PRIMARY_DIRECT_BASE)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    ap.add_argument("--prompt-suffix", default="", help="Extra prompt lines appended")
    ap.add_argument("--max-attempts", type=int, default=3)
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    api_key = resolve_derouter_api_key()
    if not api_key:
        print("DEROUTER API KEY MISSING", file=sys.stderr)
        return 1

    responses_model = args.model.strip() or default_responses_model()
    prompt = build_prompt_for_article(article_dir, root)
    if args.prompt_suffix.strip():
        prompt = prompt + "\n" + args.prompt_suffix.strip()
    ref_path = root / args.ref
    ref_paths = [ref_path] if ref_path.is_file() else []
    base_urls = resolve_image_base_urls(primary_base=args.primary_base)
    timeout = max(MIN_TIMEOUT_SECONDS, int(args.timeout))

    print(
        f"prompt_chars={len(prompt)} ref={ref_path.is_file()} model={responses_model}",
        flush=True,
    )

    meta = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    topic_id = str(meta.get("topic_id") or "")

    last_errors: list[str] = []
    for attempt in range(1, max(1, args.max_attempts) + 1):
        print(f"attempt {attempt}/{args.max_attempts}", flush=True)
        try:
            raw_bytes, gen_meta = generate_image_via_responses(
                prompt=prompt,
                api_key=api_key,
                responses_model=responses_model,
                size=SOLO_COVER_SIZE,
                timeout=timeout,
                base_urls=base_urls,
                image_paths=ref_paths,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL generation: {exc}", file=sys.stderr)
            return 1

        cover_path = article_dir / "cover" / "cover.png"
        cover_path.parent.mkdir(parents=True, exist_ok=True)
        cover_path.write_bytes(raw_bytes)
        print(
            f"OK cover.png bytes={len(raw_bytes)} size={gen_meta.get('resized_to')} "
            f"endpoint={gen_meta.get('endpoint')}",
        )

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
