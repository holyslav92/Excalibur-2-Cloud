#!/usr/bin/env python3
"""Cover QA gate — pixel checks on cover.png + stamp cover/cover_qa.json.

Publish/Indexer blocked unless PNG bytes PASS (not agent manifest lie).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from excalibur_blog_cover_qa_pixels import (
    analyze_cover_pixels,
    load_json,
    md5_file,
    stamp_cover_qa_json,
)
from excalibur_blog_meme_canon import load_meme_catalog, normalize_meme_picks, validate_meme_picks
from excalibur_blog_quad_slots import CANONICAL_INLINE_VISUAL_TYPES, normalize_visual_type


REQUIRED_CHECKS = (
    "identity_face_28yo",
    "identity_body_medium_slim",
    "identity_expression_invented",
    "title_not_occluded",
    "outfit_invented",
    "action_invented",
    "emotion_not_copied_from_recent_covers",
    "cover_phone_readable",
    "board_stationery_ok",
    "typography_cyrillic_clean",
    "meme_density_inline_ok",
    "light_high_key",
    "motif_no_collision_14d",
    "people_in_8_set",
    "cats_cadence_ok",
    "no_wordstat_query_strips_on_cover",
    "identity_real_files",
    "inline_utility_all_7",
    "inline_no_host_face",
    "inline_no_co_host_human",
    "inline_meme_sticker_scale",
    "meme_people_real_catalog",
    "meme_variety_not_cats_only",
    "pixel_qa_reads_png_not_prompt",
    "pixel_host_close_up",
    "pixel_wordstat_not_opaque_bars",
    "pixel_title_zone_clear",
    "pixel_meme_zone_clear",
    "pixel_wordstat_not_on_host_chest",
    "pixel_meme_not_occluded_by_wordstat",
    "pixel_wordstat_only_top_left",
    "pixel_no_text_on_clothing",
    "pixel_no_inpaint_artifacts",
    "pixel_meme_clearance_80px",
)

PIXEL_REQUIRED = (
    "pixel_qa_reads_png_not_prompt",
    "pixel_identity_matches_studio",
    "pixel_host_face_present",
    "pixel_host_close_up",
    "pixel_host_not_distant_fullbody",
    "pixel_not_services_checklist",
    "pixel_hook_title_cyrillic",
    "pixel_hook_title_not_truncated",
    "pixel_no_foreign_article_text",
    "pixel_no_blank_sticky_notes",
    "pixel_wordstat_not_opaque_bars",
    "pixel_wordstat_not_edge_truncated",
    "pixel_title_zone_clear",
    "pixel_meme_zone_clear",
    "pixel_wordstat_not_on_host_chest",
    "pixel_meme_not_occluded_by_wordstat",
    "pixel_no_text_on_clothing",
    "pixel_no_inpaint_artifacts",
    "pixel_meme_clearance_80px",
    "pixel_phone_readable",
    "pixel_phone_not_clipped",
    "pixel_light_high_key",
    "pixel_manifest_outfit_matches",
    "pixel_hook_title_present",
    "pixel_meme_present",
    "pixel_no_wordstat_query_strips",
    "pixel_no_wordstat_ocr_strips",
    "pixel_no_collage_inset",
    "pixel_layout_not_collapsed",
    "pixel_designed_thumbnail",
)

BANNED_OUTFIT_TOKENS = (
    "black blazer",
    "charcoal blazer",
    "чёрный пиджак",
    "black t shirt combo",
)
BANNED_POSE_TOKENS = (
    "left bust",
    "talking head",
    "host large left",
    "large left bust",
    "бюст слева",
)
BANNED_EMOTION_TOKENS = (
    "side-eye",
    "side eye",
    "боковой взгляд",
)

REQUIRED_IMAGES = (
    "cover/cover.png",
    "cover/inline-01.png",
    "cover/inline-02.png",
    "cover/inline-03.png",
    "cover/inline-04.png",
    "cover/inline-05.png",
    "cover/inline-06.png",
    "cover/inline-07.png",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_token(value: str) -> str:
    return " ".join(str(value or "").casefold().split())


def field_has_banned_tokens(value: str, tokens: tuple[str, ...]) -> bool:
    norm = normalize_token(value)
    return any(normalize_token(token) in norm for token in tokens)


def validate_title_not_occluded(manifest: dict) -> bool:
    positions = manifest.get("wordstat_sticker_positions")
    if not isinstance(positions, list) or not positions:
        return True
    if manifest.get("wordstat_pil_only"):
        # PIL Wordstat — только top-left sacred zone (не title center, не meme)
        for pos in positions:
            if isinstance(pos, (list, tuple)) and len(pos) >= 2:
                x, y = float(pos[0]), float(pos[1])
                if x > 0.42 or y > 0.36:
                    return False
        return True
    for pos in positions:
        if isinstance(pos, (list, tuple)) and len(pos) >= 2:
            if float(pos[0]) < 0.68:
                return False
    return True


def validate_outfit_invented(manifest: dict) -> bool:
    motifs = manifest.get("cover_motifs") or {}
    outfit = str(motifs.get("outfit") or "").strip()
    if not outfit:
        return False
    if field_has_banned_tokens(outfit, BANNED_OUTFIT_TOKENS):
        pose = str(motifs.get("pose_framing") or "")
        emotion = str(motifs.get("emotion") or "")
        if field_has_banned_tokens(pose, BANNED_POSE_TOKENS) and field_has_banned_tokens(
            emotion, BANNED_EMOTION_TOKENS
        ):
            return False
    return True


def validate_action_invented(manifest: dict) -> bool:
    motifs = manifest.get("cover_motifs") or {}
    action = str(motifs.get("action") or "").strip()
    return len(action) >= 8


def validate_emotion_not_recent_copy(manifest: dict, root: Path) -> bool:
    motifs = manifest.get("cover_motifs") or {}
    emotion = normalize_token(str(motifs.get("emotion") or ""))
    pose = normalize_token(str(motifs.get("pose_framing") or ""))
    if not emotion:
        return False
    log_path = root / "memory/cover/used-motifs.json"
    if not log_path.is_file():
        return True
    try:
        data = load_json(log_path)
    except json.JSONDecodeError:
        return True
    topic_id = normalize_token(str(manifest.get("topic_id") or ""))
    recent = list(data.get("entries") or [])[-3:]
    same_emotion = 0
    same_pose = 0
    for entry in recent:
        if normalize_token(str(entry.get("topic_id") or "")) == topic_id:
            continue
        prior = entry.get("motifs") or {}
        if normalize_token(str(prior.get("emotion") or "")) == emotion:
            same_emotion += 1
        if pose and normalize_token(str(prior.get("pose_framing") or "")) == pose:
            same_pose += 1
    if same_emotion >= 2:
        return False
    if same_pose >= 2 and field_has_banned_tokens(pose, BANNED_POSE_TOKENS):
        return False
    if field_has_banned_tokens(emotion, BANNED_EMOTION_TOKENS) and field_has_banned_tokens(
        pose, BANNED_POSE_TOKENS
    ):
        outfit = str(motifs.get("outfit") or "")
        if field_has_banned_tokens(outfit, BANNED_OUTFIT_TOKENS):
            return False
    return True


def validate_cover_qa(article_dir: Path, root: Path, *, stamp: bool = True) -> dict:
    errors: list[str] = []
    qa_path = article_dir / "cover" / "cover_qa.json"

    from excalibur_blog_identity_real import missing_identity_files

    missing_identity = missing_identity_files(root)
    if missing_identity:
        errors.append(f"identity-real missing: {', '.join(missing_identity)}")

    for rel in REQUIRED_IMAGES:
        if not (article_dir / rel).is_file():
            errors.append(f"missing image: {rel}")

    cover_path = article_dir / "cover" / "cover.png"
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    manifest = load_json(manifest_path) if manifest_path.is_file() else None
    topic_id = str((manifest or {}).get("topic_id") or "")
    meta_path = article_dir / "article.meta.json"
    if meta_path.is_file():
        try:
            topic_id = topic_id or str(load_json(meta_path).get("topic_id") or "")
        except json.JSONDecodeError:
            pass

    pixel_result = analyze_cover_pixels(cover_path, manifest=manifest)
    for key in PIXEL_REQUIRED:
        if not pixel_result.checks.get(key):
            errors.append(f"pixel check failed: {key}")
    for err in pixel_result.errors:
        if err.startswith("ocr_false_positive_escape PASS"):
            continue
        if err not in errors:
            errors.append(err)

    meme_catalog = root / "memory" / "cover" / "meme-top100.json"
    if not meme_catalog.is_file():
        errors.append("memory/cover/meme-top100.json missing — meme catalog required")

    if manifest_path.is_file() and manifest:
        phone = str(manifest.get("cover_phone_cta") or "").strip()
        if phone != "+7 922 001 65 05":
            errors.append("cover_phone_cta must be '+7 922 001 65 05' in quad-manifest")
        slots = manifest.get("slots") or {}
        allowed_types = CANONICAL_INLINE_VISUAL_TYPES
        for i in range(1, 8):
            key = f"inline_{i}"
            slot = slots.get(key) or {}
            vt_raw = str(slot.get("visual_type") or "").strip()
            vt = normalize_visual_type(vt_raw)
            if not vt:
                errors.append(f"{key}.visual_type missing in quad-manifest")
            elif vt not in allowed_types:
                errors.append(f"{key}.visual_type invalid: {slot.get('visual_type')}")
            labels = slot.get("labels") or []
            if not (2 <= len(labels) <= 6):
                errors.append(f"{key}.labels count {len(labels)}, need 2-6")
        motifs = manifest.get("cover_motifs") or {}
        if not motifs.get("outfit"):
            errors.append("cover_motifs.outfit missing — variety lock requires invented outfit")
        if not motifs.get("action"):
            errors.append("cover_motifs.action missing — variety lock requires invented action")
        if not motifs.get("emotion"):
            errors.append("cover_motifs.emotion missing — variety lock requires hook emotion")
        if not motifs.get("pose_framing"):
            errors.append("cover_motifs.pose_framing missing — variety lock requires pose/framing")
        if not validate_title_not_occluded(manifest):
            errors.append("wordstat_sticker_positions overlap title zone (x must be ≥0.68)")
        if not validate_outfit_invented(manifest):
            errors.append("outfit_invented FAIL: black-blazer+left-bust+side-eye combo or empty outfit")
        if not validate_action_invented(manifest):
            errors.append("action_invented FAIL: cover_motifs.action too short or missing")
        if not validate_emotion_not_recent_copy(manifest, root):
            errors.append(
                "emotion_not_copied_from_recent_covers FAIL: emotion/pose repeats last covers"
            )
        picks = normalize_meme_picks(manifest.get("meme_picks"))
        if picks:
            catalog = load_meme_catalog(root)
            for err in validate_meme_picks(picks, catalog):
                errors.append(err)

    status = "PASS" if not errors else "FAIL"
    meme_variety_ok = not any("meme_variety" in e for e in errors)

    if stamp:
        stamp_cover_qa_json(
            article_dir,
            pixel_result,
            topic_id=topic_id,
            merge_checks={"meme_variety_not_cats_only": meme_variety_ok},
        )
        qa = load_json(qa_path)
        qa["gate_status"] = status
        qa["gate_errors"] = errors
        qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if qa_path.is_file() and status == "PASS":
        try:
            qa = load_json(qa_path)
        except json.JSONDecodeError:
            qa = {}
        if str(qa.get("status") or "").upper() != "PASS":
            errors.append(f"cover_qa.json status must be PASS, got {qa.get('status')!r}")
            status = "FAIL"
        stamped_md5 = str(qa.get("cover_md5") or "")
        live_md5 = md5_file(cover_path) if cover_path.is_file() else ""
        if stamped_md5 and live_md5 and stamped_md5 != live_md5:
            errors.append(f"cover_qa.json cover_md5 mismatch: stamp={stamped_md5} png={live_md5}")
            status = "FAIL"
        checks = qa.get("checks") or {}
        for key in REQUIRED_CHECKS:
            if not checks.get(key):
                errors.append(f"cover_qa check failed or missing: {key}")
                status = "FAIL"
        if not qa.get("pixel_qa"):
            errors.append("cover_qa.json pixel_qa flag missing — run pixel gate")
            status = "FAIL"

    return {"status": status, "errors": errors, "pixel": pixel_result.to_dict()}


def cmd_doctor(root: Path) -> int:
    paths = (
        root / ".cursor/agents/excalibur-blog-cover-qa.md",
        root / "agents/excalibur-blog-cover-qa.md",
        root / "skills/cover-qa-excalibur-blog/SKILL.md",
        root / "scripts/excalibur_blog_cover_qa_pixels.py",
        root / "scripts/excalibur_blog_cover_fixer.py",
    )
    for path in paths:
        if not path.is_file():
            print(f"FAIL missing {path.relative_to(root)}", file=sys.stderr)
            return 1
    print("OK cover-qa agent + skill + pixel/fix scripts present")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Cover QA gate for longform 8-image set")
    parser.add_argument("--article-dir", help="Article directory to validate")
    parser.add_argument("--doctor", action="store_true", help="Repo-level doctor check")
    parser.add_argument("--no-stamp", action="store_true", help="Validate only, do not rewrite cover_qa.json")
    args = parser.parse_args()
    root = project_root()

    if args.doctor:
        return cmd_doctor(root)

    if not args.article_dir:
        print("FAIL --article-dir required", file=sys.stderr)
        return 1

    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    result = validate_cover_qa(article_dir, root, stamp=not args.no_stamp)
    if result["status"] != "PASS":
        print(f"FAIL COVER QA GATE: {'; '.join(result['errors'])}", file=sys.stderr)
        return 1
    print("OK cover QA stamp (cover_qa.json PASS + pixel bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
