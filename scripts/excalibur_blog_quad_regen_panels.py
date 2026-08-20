#!/usr/bin/env python3
"""Regenerate ONLY failed quad panels — never full 2× canvas unless cover slot.

Cover-QA FAIL → default path: regen listed slots as solo 16:9 PNGs.
Derouter REST primary; Kie fallback after 524/quota exhausted.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from excalibur_blog_quad_slots import INLINE_FILES, slot_allows_meme_sticker


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slot_negatives(slot_key: str, slot: dict[str, Any]) -> str:
    parts: list[str] = []
    if slot.get("no_host_face"):
        parts.append("NO host face / NO Святослав / БЕЗ лица ведущего")
    if slot.get("no_meme") or slot.get("no_cat"):
        parts.append("NO meme / NO cat sticker / БЕЗ мема / БЕЗ кота")
    if slot.get("no_person"):
        parts.append("NO person / NO co-host / БЕЗ человека")
    if slot_allows_meme_sticker(slot_key):
        parts.append(
            "tiny meme sticker ≤15% frame corner only from meme-top100.json"
        )
    return "; ".join(parts)


def build_panel_prompt(manifest: dict[str, Any], slot_key: str, root: Path) -> str:
    from excalibur_blog_cover_quad_prompt import (
        BOARD_STATIONERY,
        INLINE_BAN_EXTRA,
        build_prompt,
        inline_panel_prompt,
        load_json,
    )

    slots = manifest.get("slots") or {}
    slot = slots.get(slot_key) or {}
    types_path = root / manifest.get("inline_types_catalog", "memory/cover/inline-visual-types.json")
    types_catalog = load_json(types_path) if types_path.is_file() else {"types": {}}
    style_path = root / manifest.get("style_file", "memory/cover/quad-style-the-rieltor.json")
    style = load_json(style_path) if style_path.is_file() else {}
    design_path = root / "memory/cover/cover-design-code.json"
    design_code = load_json(design_path) if design_path.is_file() else {}
    hero_path = root / manifest.get("blog_hero", "memory/cover/blog-hero.json")
    hero = load_json(hero_path) if hero_path.is_file() else {}

    if slot_key == "cover":
        if manifest.get("wordstat_pil_only"):
            design_path = root / "memory/cover/cover-design-code.json"
            design_code = load_json(design_path) if design_path.is_file() else {}
            from excalibur_blog_cover_quad_prompt import build_solo_cover_prompt

            return build_solo_cover_prompt(manifest, style, hero, design_code)
        return build_prompt(
            manifest,
            style,
            hero,
            types_catalog,
            design_code,
            canvas_slots=("cover",),
            has_cover=True,
        )

    neg = slot_negatives(slot_key, slot)
    base = inline_panel_prompt(slot, types_catalog)
    return (
        f"Single 16:9 editorial infographic panel, high-key #FFF, gold/black Cyrillic.\n"
        f"{base}\n"
        f"NEGATIVE: {neg}. {INLINE_BAN_EXTRA}. {BOARD_STATIONERY}.\n"
        "TEXT LANGUAGE LOCK: Russian Cyrillic only.\n"
    )


def write_solo_batch(
    article_dir: Path,
    slot_key: str,
    prompt: str,
    *,
    with_i2i: bool,
    ref_url: str,
) -> Path:
    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)
    batch_path = cover_dir / f"quad-solo-batch-{slot_key}.json"
    api_input: dict[str, Any] = {
        "prompt": prompt,
        "aspect_ratio": "16:9",
        "resolution": "2K",
    }
    if with_i2i and ref_url:
        api_input["input_urls"] = [ref_url]
    batch = {
        "pipeline": "quad_solo_panel_regen",
        "slot": slot_key,
        "output_canvas": f"cover/{INLINE_FILES.get(slot_key, slot_key + '.png')}",
        "jobs": [{"slot": slot_key, "tool": "derouter-rest", "mcp_args": api_input}],
    }
    save_json(batch_path, batch)
    return batch_path


def run_image_api(root: Path, article_dir: Path, batch_path: Path, result_path: Path) -> int:
    derouter = root / "scripts/excalibur_blog_derouter_gpt_image2_api.py"
    cmd = [
        sys.executable,
        str(derouter),
        "--article-dir",
        str(article_dir),
        "--batch",
        str(batch_path.relative_to(article_dir)),
        "--result",
        str(result_path.relative_to(article_dir)),
        "--fallback-kie",
    ]
    return subprocess.call(cmd, cwd=str(root))


def _pick_best_cover_panel(im) -> Any:
    """Из 2×2 quad canvas выбрать панель с лучшим pixel QA score."""
    from PIL import Image

    import tempfile

    from excalibur_blog_cover_qa_pixels import analyze_cover_pixels, cover_composition_ok

    w, h = im.size
    crops = [
        im.crop((w // 2, h // 2, w, h)),
        im.crop((w // 2, 0, w, h // 2)),
        im.crop((0, h // 2, w // 2, h)),
        im.crop((0, 0, w // 2, h // 2)),
    ]
    best_panel = crops[0].convert("RGB").resize((1200, 675), Image.Resampling.LANCZOS)
    best_score = -9999
    for crop in crops:
        panel = crop.convert("RGB").resize((1200, 675), Image.Resampling.LANCZOS)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp_path = Path(tmp.name)
            panel.save(tmp_path, format="PNG")
        result = analyze_cover_pixels(tmp_path)
        tmp_path.unlink(missing_ok=True)
        if not cover_composition_ok(panel):
            continue
        score = sum(1 for v in result.checks.values() if v) * 10 - len(result.errors) * 25
        if score > best_score:
            best_score = score
            best_panel = panel
    return best_panel


def apply_solo_result(
    article_dir: Path,
    slot_key: str,
    result_path: Path,
    root: Path,
) -> int:
    from asset_download import download_url_bytes

    if not result_path.is_file():
        print(f"FAIL missing result {result_path}", file=sys.stderr)
        return 1
    data = load_json(result_path)
    url = (data.get("url") or "").strip()
    local_rel = (data.get("local_path") or "").strip()
    cover_dir = article_dir / "cover"
    if slot_key == "cover":
        out = cover_dir / "cover.png"
    else:
        out = cover_dir / INLINE_FILES.get(slot_key, f"{slot_key}.png")

    if local_rel:
        local = Path(local_rel)
        if not local.is_absolute():
            local = article_dir / local
        if local.is_file():
            out.write_bytes(local.read_bytes())
            print(f"OK solo regen {slot_key} → {out.name}")
            return 0

    if not url:
        print(f"FAIL solo regen {slot_key}: no url in result", file=sys.stderr)
        return 1
    img_bytes, _ = download_url_bytes(url)
    out.write_bytes(img_bytes)
    # Solo cover regen must be 16:9 editorial cover, not full quad canvas.
    if slot_key == "cover" and out.is_file():
        try:
            from PIL import Image

            from excalibur_blog_cover_qa_pixels import cover_composition_ok

            with Image.open(out) as im:
                raw_backup = cover_dir / "cover-quad-raw.png"
                im.convert("RGB").save(raw_backup, format="PNG")
                rgb = im.convert("RGB")
                probe = (
                    rgb
                    if rgb.size == (1200, 675)
                    else rgb.resize((1200, 675), Image.Resampling.LANCZOS)
                )
                if cover_composition_ok(probe):
                    if rgb.size != (1200, 675):
                        probe.save(out, format="PNG")
                    print(f"OK solo regen {slot_key} → single 16:9 resize → {out.name}")
                    return 0
                w, h = im.size
                if w > h * 1.4:
                    panel = _pick_best_cover_panel(im)
                    panel.save(out, format="PNG")
                    print(f"OK solo regen {slot_key} → best face panel → {out.name}")
                    return 0
                if im.size != (1200, 675):
                    im.convert("RGB").resize((1200, 675), Image.Resampling.LANCZOS).save(out, format="PNG")
        except Exception as exc:
            print(f"WARN cover resize/crop: {exc}", file=sys.stderr)
    print(f"OK solo regen {slot_key} → {out.name}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument(
        "--slots",
        required=True,
        help="Comma-separated slot keys, e.g. inline_2,inline_3",
    )
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--inject-html", action="store_true")
    ap.add_argument("--wordstat-overlay", action="store_true", help="Stamp Wordstat after cover regen")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path
    if not manifest_path.is_file():
        print(f"❌ PANEL REGEN BLOCKER: {manifest_path} missing", file=sys.stderr)
        return 1

    manifest = load_json(manifest_path)
    hero_path = root / manifest.get("blog_hero", "memory/cover/blog-hero.json")
    hero = load_json(hero_path) if hero_path.is_file() else {}
    ref_url = str(hero.get("reference_url_hosted") or "").strip()

    slot_keys = [s.strip() for s in args.slots.split(",") if s.strip()]
    if not slot_keys:
        print("❌ PANEL REGEN BLOCKER: empty --slots", file=sys.stderr)
        return 1

    for slot_key in slot_keys:
        max_attempts = 6 if slot_key == "cover" else 1
        for attempt in range(1, max_attempts + 1):
            prompt = build_panel_prompt(manifest, slot_key, root)
            with_i2i = slot_key == "cover"
            batch_path = write_solo_batch(
                article_dir, slot_key, prompt, with_i2i=with_i2i, ref_url=ref_url
            )
            result_path = article_dir / "cover" / f"quad-solo-result-{slot_key}.json"
            rc = run_image_api(root, article_dir, batch_path, result_path)
            if rc != 0:
                print(f"❌ PANEL REGEN BLOCKER: {slot_key} image API exit={rc}", file=sys.stderr)
                return rc
            rc = apply_solo_result(article_dir, slot_key, result_path, root)
            if rc != 0:
                return rc
            if slot_key != "cover":
                break
            from excalibur_blog_cover_qa_pixels import analyze_cover_pixels

            pre = analyze_cover_pixels(article_dir / "cover" / "cover.png", manifest=manifest)
            model_dirty = pre.status != "PASS" or not (
                pre.checks.get("pixel_host_close_up")
                and pre.checks.get("pixel_phone_readable")
                and pre.checks.get("pixel_no_text_on_clothing")
                and pre.checks.get("pixel_wordstat_only_top_left")
                and pre.checks.get("pixel_wordstat_not_on_host_chest")
                and pre.checks.get("pixel_meme_not_occluded_by_wordstat")
                and pre.checks.get("pixel_no_inpaint_artifacts")
            )
            if not model_dirty:
                print(f"OK cover base clean before PIL overlay (attempt {attempt})")
                break
            print(
                f"WARN cover attempt {attempt}/{max_attempts} model artifacts: "
                + "; ".join(pre.errors[:4]),
                file=sys.stderr,
            )
            if attempt >= max_attempts:
                print("❌ PANEL REGEN BLOCKER: cover base still dirty after retries", file=sys.stderr)
                return 1

    if args.wordstat_overlay and "cover" in slot_keys:
        overlay = root / "scripts/excalibur_blog_cover_wordstat_overlay.py"
        subprocess.call(
            [
                sys.executable,
                str(overlay),
                "--article-dir",
                str(article_dir.relative_to(root)),
                "--force",
                "--top-left-only",
            ],
            cwd=str(root),
        )

    if args.inject_html:
        split_script = root / "scripts/excalibur_blog_cover_quad_split.py"
        for slot_key in slot_keys:
            if slot_key == "cover":
                continue
            # inject via split script helper — canvas-index by slot
            canvas_index = 1 if slot_key in {"inline_1", "inline_2", "inline_3"} else 2
            subprocess.call(
                [
                    sys.executable,
                    str(split_script),
                    "--article-dir",
                    str(article_dir),
                    "--canvas-index",
                    str(canvas_index),
                    "--inject-html",
                ],
                cwd=str(root),
            )
            break

    print(f"OK panel regen complete: {', '.join(slot_keys)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
