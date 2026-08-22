#!/usr/bin/env python3
"""Solo cover regen via grsai standard image model (face i2i from studio portrait).

Builds solo cover prompt from quad-manifest, generates 1200×675 PNG,
stamps cover_qa.json. Kie and PIL mashup FORBIDDEN.

Model tiers (owner rule): first call non-vip; on API fail or Cover-QA FAIL
escalate to vip for the same attempt; next attempt starts non-vip again.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_grsai_gpt_image2_api import (
    DEFAULT_TIMEOUT_SECONDS,
    MIN_TIMEOUT_SECONDS,
    default_quality,
    generate_image,
    iter_model_tiers,
    model_tier_standard,
    project_root,
    resolve_grsai_api_key,
    resolve_hosts,
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


def write_temp_batch(article_dir: Path, prompt: str, ref_path: Path) -> Path:
    batch = {
        "pipeline": "grsai_solo_cover",
        "slot": "cover",
        "output_canvas": "cover/cover.png",
        "prefer_local_reference": True,
        "local_reference": str(ref_path),
        "jobs": [
            {
                "slot": "cover",
                "tool": "grsai-rest",
                "mcp_args": {
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "resolution": "2K",
                },
            }
        ],
    }
    batch_path = article_dir / "cover" / "grsai-solo-batch.json"
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return batch_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate solo 1200×675 cover via grsai standard image model")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--ref", default=DEFAULT_REF)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    ap.add_argument("--prompt-suffix", default="", help="Extra prompt lines appended")
    ap.add_argument("--max-attempts", type=int, default=6)
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    api_key = resolve_grsai_api_key()
    if not api_key:
        print("GRSAI API KEY MISSING", file=sys.stderr)
        return 1

    standard_model = model_tier_standard()
    quality = default_quality()
    prompt = build_prompt_for_article(article_dir, root)
    if args.prompt_suffix.strip():
        prompt = prompt + "\n" + args.prompt_suffix.strip()
    ref_path = root / args.ref
    if not ref_path.is_file():
        print(f"FAIL identity ref missing: {ref_path}", file=sys.stderr)
        return 1

    identity_suffix = (
        "\nIDENTITY LOCK (mandatory): exact same man as reference photo — "
        "28 years old, medium-slim build, round-oval face, dark brown short hair tapered sides, "
        "warm dark brown eyes, full dark brows, light even stubble on jaw/chin/upper lip. "
        "Bone structure, hairline, stubble pattern, eye shape MUST match studio portrait. "
        "NEW invented outfit and emotion/scene — do NOT clone reference blazer/pose/background."
    )
    prompt = prompt + identity_suffix

    timeout = max(MIN_TIMEOUT_SECONDS, int(args.timeout))
    hosts = resolve_hosts()
    model_tiers = iter_model_tiers()

    print(
        f"prompt_chars={len(prompt)} ref={ref_path.name} "
        f"model_tiers={[m for _, m in model_tiers]} hosts={hosts}",
        flush=True,
    )

    meta_json = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    topic_id = str(meta_json.get("topic_id") or "")

    last_errors: list[str] = []
    for attempt in range(1, max(1, args.max_attempts) + 1):
        print(f"attempt {attempt}/{args.max_attempts}", flush=True)
        batch_path = write_temp_batch(article_dir, prompt, ref_path)
        image_input = {
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "resolution": "2K",
        }

        attempt_passed = False
        for tier_idx, (tier_name, model) in enumerate(model_tiers):
            print(f"  tier={tier_name} model={model}", flush=True)
            try:
                raw_bytes, gen_meta = generate_image(
                    root=root,
                    batch_path=batch_path,
                    image_input=image_input,
                    api_key=api_key,
                    model=model,
                    quality=quality,
                    target_size=SOLO_COVER_SIZE,
                    timeout=timeout,
                    hosts=hosts,
                    max_retries=1,
                    retry_wait=5,
                )
            except Exception as exc:  # noqa: BLE001
                if tier_name == "standard" and len(model_tiers) > 1:
                    print(f"WARN non-vip generation failed: {exc}", flush=True)
                    continue
                print(f"FAIL generation: {exc}", file=sys.stderr)
                break

            gen_meta["model_tier"] = tier_name
            cover_path = article_dir / "cover" / "cover.png"
            cover_path.parent.mkdir(parents=True, exist_ok=True)
            cover_path.write_bytes(raw_bytes)
            print(
                f"OK cover.png bytes={len(raw_bytes)} tier={tier_name} model={model} "
                f"host={gen_meta.get('host')} endpoint={gen_meta.get('endpoint')}",
            )

            qa = stamp_qa(article_dir, root, topic_id)
            if qa["status"] == "PASS":
                print(f"OK cover_qa PASS md5={qa['md5']} tier={tier_name}")
                return 0

            last_errors = list(qa["errors"])
            print(f"WARN pixel QA fail ({tier_name}):", "; ".join(last_errors), flush=True)
            if tier_name == "standard" and len(model_tiers) > 1:
                print("  escalating to vip for same attempt", flush=True)
                continue
            attempt_passed = False
            break

        if attempt_passed:
            break

    print("FAIL pixel QA:", "; ".join(last_errors), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
