#!/usr/bin/env python3
"""Preflight quad-manifest.json before Derouter image API — fail cheap."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_quad_slots import (
    MEME_ALLOWED_SLOTS,
    NO_MEME_NO_CAT_SLOTS,
    active_inline_keys,
    apply_quad_canon_to_manifest,
    inline_count_from_manifest,
    slot_allows_meme_sticker,
)


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_quad_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    """Проверить meme_density, no_host_face, wordstat_stickers до image API."""
    errors: list[str] = []
    warnings: list[str] = []

    inline_count = inline_count_from_manifest(manifest)
    slots = manifest.get("slots") or {}

    stickers = manifest.get("wordstat_stickers") or []
    if not isinstance(stickers, list):
        errors.append("wordstat_stickers must be a list")
        stickers = []
    sticker_phrases = [str(x).strip() for x in stickers if str(x).strip()]
    if not (1 <= len(sticker_phrases) <= 3):
        errors.append(
            f"wordstat_stickers count {len(sticker_phrases)}; need 1–3 readable phrases"
        )

    phone = str(manifest.get("cover_phone_cta") or "").strip()
    if phone and phone != "+7 922 001 65 05":
        errors.append(f"cover_phone_cta must be '+7 922 001 65 05', got {phone!r}")

    if inline_count == 7:
        meme_on: list[str] = []
        for key in active_inline_keys(inline_count):
            slot = slots.get(key) or {}
            if slot.get("meme_sticker") is True:
                meme_on.append(key)
            if slot.get("no_host_face") is not True and key != "cover":
                errors.append(f"{key}.no_host_face must be true (host only on cover)")
            if key in NO_MEME_NO_CAT_SLOTS:
                if slot.get("meme_sticker"):
                    errors.append(f"{key}: meme_sticker forbidden (canon: no cat/meme/person)")
                if not slot.get("no_meme"):
                    errors.append(f"{key}.no_meme must be true")
                if not slot.get("no_cat"):
                    errors.append(f"{key}.no_cat must be true")

        allowed_inline_meme = {k for k in meme_on if k.startswith("inline_")}
        if len(allowed_inline_meme) > 3:
            errors.append(
                f"meme_density: {len(allowed_inline_meme)} inline meme slots; max 3 "
                f"(pattern: inline_1, inline_5, inline_7)"
            )
        bad_meme = allowed_inline_meme - {k for k in MEME_ALLOWED_SLOTS if k.startswith("inline_")}
        if bad_meme:
            errors.append(
                f"meme on disallowed inline slots: {sorted(bad_meme)}; "
                f"allowed: inline_1, inline_5, inline_7"
            )
        if len(allowed_inline_meme) < 2:
            warnings.append(
                f"meme_density low: {len(allowed_inline_meme)} inline meme slots "
                "(canon target 2–3 of 7)"
            )

        cover_slot = slots.get("cover") or {}
        if cover_slot.get("no_host_face"):
            errors.append("cover.no_host_face must be false — host only on cover")

    for key in ("cover",) + tuple(active_inline_keys(inline_count)):
        slot = slots.get(key) or {}
        if not str(slot.get("scene_hint") or "").strip():
            errors.append(f"{key}.scene_hint empty")
        if not str(slot.get("alt") or "").strip():
            errors.append(f"{key}.alt empty")
        if key != "cover" and slot_allows_meme_sticker(key) is False:
            neg = slot.get("prompt_negatives") or ""
            if "NO meme" not in neg and "БЕЗ мем" not in neg:
                warnings.append(f"{key}: prompt_negatives missing RU/EN no-meme clause")

    status = "PASS" if not errors else "FAIL"
    return {
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "wordstat_sticker_count": len(sticker_phrases),
        "inline_meme_slots": [
            k
            for k in active_inline_keys(inline_count)
            if (slots.get(k) or {}).get("meme_sticker")
        ],
    }


def cmd_doctor(root: Path) -> int:
    script = root / "scripts/excalibur_blog_quad_manifest_preflight.py"
    if not script.is_file():
        print("FAIL quad_manifest_preflight script missing", file=sys.stderr)
        return 1
    print("OK quad_manifest_preflight doctor")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", help="Article directory")
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--doctor", action="store_true")
    ap.add_argument("--apply-canon", action="store_true", help="Apply quad canon flags before validate")
    ap.add_argument("-o", "--output", help="Write preflight report JSON")
    args = ap.parse_args()

    root = project_root()
    if args.doctor:
        return cmd_doctor(root)

    if not args.article_dir:
        print("❌ QUAD PREFLIGHT BLOCKER: --article-dir required", file=sys.stderr)
        return 1

    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path
    if not manifest_path.is_file():
        print(f"❌ QUAD PREFLIGHT BLOCKER: {manifest_path} missing", file=sys.stderr)
        return 1

    manifest = load_json(manifest_path)
    if args.apply_canon:
        manifest = apply_quad_canon_to_manifest(manifest)
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    result = validate_quad_manifest(manifest)
    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = article_dir / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for w in result.get("warnings") or []:
        print(f"WARN {w}", file=sys.stderr)

    if result["status"] != "PASS":
        print("❌ QUAD MANIFEST PREFLIGHT BLOCKER:", file=sys.stderr)
        for err in result["errors"]:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"OK quad manifest preflight PASS "
        f"(stickers={result['wordstat_sticker_count']}, "
        f"inline_meme={result.get('inline_meme_slots')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
