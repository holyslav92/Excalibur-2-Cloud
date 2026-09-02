#!/usr/bin/env python3
"""Scaffold quad-manifest.json structure only — agent writes all prose.

Script may: pick visual_type from H2 keywords, wire slots/quadrants, preserve
agent fields on --merge, keep meme_caption_ru empty.

Script must NOT invent cover_hook, scene_hint, or alt. White hoodie / face lock
live in memory/cover/blog-hero.json + style prompts, not in scene_hint boilerplate.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_quad_slots import (
    CANVAS_1_SLOTS,
    REALISTIC_H2_KEYWORDS,
    REALISTIC_INLINE_MAX,
    REALISTIC_INLINE_MIN,
    REALISTIC_INLINE_VISUAL_TYPE,
    active_inline_keys,
    apply_quad_canon_to_manifest,
    canvas_specs_for_inline_count,
    inline_count_from_tenant,
    normalize_visual_type,
)

TYPE_PRIORITY = [
    "realistic_photo",
    "comparison_table",
    "process_flow",
    "bar_timeline_chart",
    "structure_diagram",
    "labeled_checklist",
    "fact_card",
    "workflow_diagram",
    "checklist_board",
    "schema_faq_ui",
    "tool_screenshot",
    "infographic_card",
]
from excalibur_blog_quad_scene_merge import merge_scene_draft_into_manifest
from excalibur_blog_quad_slots import DEFAULT_SLOT_MAP  # noqa: E402


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def extract_h2_titles(article_html: Path) -> list[str]:
    if not article_html.is_file():
        return []
    text = article_html.read_text(encoding="utf-8")
    titles: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", text, flags=re.I | re.S):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        if title.lower() in {"частые вопросы", "faq"}:
            break
        titles.append(title)
    return titles


def score_type(h2: str, type_def: dict) -> int:
    hay = h2.lower()
    score = 0
    for kw in type_def.get("keywords") or []:
        if kw.strip().lower() in hay:
            score += 2
    return score


def score_realistic_h2(h2: str) -> int:
    hay = h2.lower()
    return sum(2 for kw in REALISTIC_H2_KEYWORDS if kw in hay)


def assign_inline_placements(
    h2s: list[str],
    inline_keys: tuple[str, ...],
    types_catalog: dict,
) -> list[dict[str, Any]]:
    """Flexible placement: 2–4 realistic_photo, pairs on same H2, some H2s with 0 images."""
    n = len(inline_keys)
    realistic_target = min(REALISTIC_INLINE_MAX, max(REALISTIC_INLINE_MIN, min(3, n // 2)))
    h2_scores = [(score_realistic_h2(h), i, h) for i, h in enumerate(h2s)]
    h2_scores.sort(key=lambda x: (-x[0], x[1]))
    realistic_h2_indices = [i for _, i, _ in h2_scores[: max(realistic_target, REALISTIC_INLINE_MIN)]]

    assignments: list[dict[str, Any]] = []
    used_types: set[str] = set()
    pair_h2: int | None = realistic_h2_indices[0] if realistic_h2_indices else None

    slot_idx = 0
    # Pair: realistic + diagram on strongest photo H2.
    if pair_h2 is not None and slot_idx < n:
        h2 = h2s[pair_h2]
        assignments.append(
            {
                "slot_key": inline_keys[slot_idx],
                "h2_anchor": h2,
                "visual_type": REALISTIC_INLINE_VISUAL_TYPE,
                "placement_group": "pair",
            }
        )
        used_types.add(REALISTIC_INLINE_VISUAL_TYPE)
        slot_idx += 1
        if slot_idx < n:
            vt = pick_visual_type(h2, types_catalog, used_types, allow_realistic=False)
            used_types.add(vt)
            assignments.append(
                {
                    "slot_key": inline_keys[slot_idx],
                    "h2_anchor": h2,
                    "visual_type": vt,
                    "placement_group": "pair",
                }
            )
            slot_idx += 1

    # Remaining realistic slots on other high-score H2s (one each).
    for h2_i in realistic_h2_indices[1:]:
        if slot_idx >= n:
            break
        if any(a["h2_anchor"] == h2s[h2_i] and a["visual_type"] == REALISTIC_INLINE_VISUAL_TYPE for a in assignments):
            continue
        if sum(1 for a in assignments if a["visual_type"] == REALISTIC_INLINE_VISUAL_TYPE) >= realistic_target:
            break
        assignments.append(
            {
                "slot_key": inline_keys[slot_idx],
                "h2_anchor": h2s[h2_i],
                "visual_type": REALISTIC_INLINE_VISUAL_TYPE,
                "placement_group": None,
            }
        )
        used_types.add(REALISTIC_INLINE_VISUAL_TYPE)
        slot_idx += 1

    # Diagram-only slots spread across H2s with lowest figure load (allow skips).
    h2_load = {h: 0 for h in h2s}
    for a in assignments:
        h2_load[a["h2_anchor"]] = h2_load.get(a["h2_anchor"], 0) + 1

    while slot_idx < n:
        # Prefer H2 with load 0, then 1 (avoid triple-stacking unless needed).
        candidates = sorted(
            range(len(h2s)),
            key=lambda i: (h2_load.get(h2s[i], 0), i),
        )
        h2_i = candidates[0]
        h2 = h2s[h2_i]
        vt = pick_visual_type(h2, types_catalog, used_types, allow_realistic=False)
        used_types.add(vt)
        assignments.append(
            {
                "slot_key": inline_keys[slot_idx],
                "h2_anchor": h2,
                "visual_type": vt,
                "placement_group": None,
            }
        )
        h2_load[h2] = h2_load.get(h2, 0) + 1
        slot_idx += 1

    return assignments


def pick_visual_type(
    h2: str,
    types_catalog: dict,
    used: set[str],
    *,
    allow_realistic: bool = True,
) -> str:
    types = types_catalog.get("types") or {}
    scored: list[tuple[int, str]] = []
    for type_id, type_def in types.items():
        if not allow_realistic and type_id == REALISTIC_INLINE_VISUAL_TYPE:
            continue
        scored.append((score_type(h2, type_def), type_id))
    scored.sort(key=lambda item: (-item[0], TYPE_PRIORITY.index(item[1]) if item[1] in TYPE_PRIORITY else 99))
    for score, type_id in scored:
        if score > 0 and type_id not in used:
            return type_id
    for type_id in TYPE_PRIORITY:
        if type_id not in used:
            return type_id
    return TYPE_PRIORITY[0]


def _load_tenant_inline_count(root: Path, preserve: dict | None) -> int:
    if preserve and preserve.get("inline_count") in (3, 7):
        return int(preserve["inline_count"])
    tenant_path = root / "shared/tenant-config.json"
    tenant = load_json(tenant_path) if tenant_path.is_file() else {}
    return inline_count_from_tenant(tenant)


def build_manifest(article_dir: Path, root: Path, preserve: dict | None) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    meta = load_json(meta_path) if meta_path.is_file() else {}
    types_catalog = load_json(root / "memory/cover/inline-visual-types.json")
    h2s = extract_h2_titles(article_dir / "article.html")
    inline_count = _load_tenant_inline_count(root, preserve)
    inline_keys = active_inline_keys(inline_count)
    min_h2 = 5
    if len(h2s) < min_h2:
        raise ValueError(
            f"article needs at least {min_h2} real H2 anchors for flexible inline placement; "
            f"found {len(h2s)}"
        )
    topic_id = meta.get("topic_id") or article_dir.name.split("-")[0]

    old_cover = ((preserve or {}).get("slots") or {}).get("cover") or {}
    # cover-text.json (Cover-text agent) owns the exact Russian inscriptions.
    cover_text_path = article_dir / "cover" / "cover-text.json"
    cover_text = load_json(cover_text_path) if cover_text_path.is_file() else {}
    ct_labels = cover_text.get("inline_labels") or {}
    # Prose fields: preserve agent text only. Never invent scene_hint/alt/hook.
    cover = {
        "quadrant": "top_left",
        "role": "cover_editorial_hero",
        "alt": str(old_cover.get("alt") or "").strip(),
        "scene_hint": str(old_cover.get("scene_hint") or "").strip(),
        "meme_caption_ru": "",
        "sticky": str(cover_text.get("sticky") or old_cover.get("sticky") or "").strip(),
    }

    used: set[str] = set()
    slots: dict[str, Any] = {"cover": cover}
    placement_plan = assign_inline_placements(h2s, inline_keys, types_catalog)
    placement_by_slot = {p["slot_key"]: p for p in placement_plan}
    for idx, slot_key in enumerate(inline_keys, start=1):
        plan = placement_by_slot.get(slot_key) or {}
        h2 = plan.get("h2_anchor") or (h2s[idx - 1] if idx - 1 < len(h2s) else f"Секция {idx}")
        old = ((preserve or {}).get("slots") or {}).get(slot_key) or {}
        visual_type = normalize_visual_type(
            str(old.get("visual_type") or "").strip()
            or plan.get("visual_type")
            or pick_visual_type(h2, types_catalog, used)
        )
        used.add(visual_type)
        labels = ct_labels.get(slot_key) or old.get("labels") or []
        slot_entry: dict[str, Any] = {
            "quadrant": DEFAULT_SLOT_MAP[slot_key],
            "h2_anchor": old.get("h2_anchor") or h2,
            "visual_type": visual_type,
            "scene_hint": str(old.get("scene_hint") or "").strip(),
            "alt": str(old.get("alt") or "").strip(),
            "labels": [str(x).strip() for x in labels if str(x).strip()],
        }
        if plan.get("placement_group"):
            slot_entry["placement_group"] = plan["placement_group"]
        slots[slot_key] = slot_entry

    hook = (
        str(cover_text.get("hook") or "").strip()
        or str((preserve or {}).get("cover_hook") or "").strip()
    )
    highlight = (
        str(cover_text.get("highlight") or "").strip()
        or str((preserve or {}).get("cover_hook_highlight") or "").strip()
    )

    wordstat_stickers = list((preserve or {}).get("wordstat_stickers") or [])
    if not wordstat_stickers and cover_text.get("wordstat_stickers"):
        wordstat_stickers = [
            str(x).strip() for x in cover_text["wordstat_stickers"] if str(x).strip()
        ]

    canvas_specs = canvas_specs_for_inline_count(inline_count)
    pipeline = (
        "quad_canvas_2x_image_api_longform"
        if inline_count == 7
        else "quad_canvas_1x_image_api"
    )
    style_file = str(
        (preserve or {}).get("style_file")
        or "memory/cover/quad-style-the-rieltor.json"
    )
    manifest: dict[str, Any] = {
        "topic_id": topic_id,
        "canvas_file": canvas_specs[0]["canvas_file"],
        "layout": "2x2",
        "pipeline": pipeline,
        "inline_count": inline_count,
        "canvases": [
            {
                "index": spec["index"],
                "canvas_file": spec["canvas_file"],
                "batch_file": spec["batch_file"],
                "prompt_file": spec["prompt_file"],
                "result_file": spec["result_file"],
                "slots": list(spec["slots"]),
                "has_cover": bool(spec.get("has_cover")),
            }
            for spec in canvas_specs
        ],
        "style_preset": "the_rieltor_twilight_gold",
        "style_file": style_file,
        "blog_hero": "memory/cover/blog-hero.json",
        "inline_types_catalog": "memory/cover/inline-visual-types.json",
        "cover_hook": hook,
        "cover_hook_highlight": highlight,
        "cover_hook_contract": "shared/blog-cover-quad-canvas-contract.md",
        "mcp_note": (
            "PRIMARY: grsai grsai standard image model (GRSAI_API_KEY) — 2K 16:9, one job per canvas "
            f"({len(canvas_specs)}×). Cover agent invents cover_hook + scene_hint/alt "
            "before --write-batch. Host lock = blog-hero.json (navy blazer, not hoodie)."
        ),
        "slots": slots,
        "cover_keys_ru": list((preserve or {}).get("cover_keys_ru") or []),
        "wordstat_stickers": wordstat_stickers[:3],
        "cover_phone_cta": str((preserve or {}).get("cover_phone_cta") or "+7 922 001 65 05"),
        "image_placement": {
            "mode": "flexible_v2",
            "not_one_per_h2": True,
            "allow_pair_same_h2": True,
            "realistic_count_target": f"{REALISTIC_INLINE_MIN}-{REALISTIC_INLINE_MAX}",
        },
    }
    if preserve:
        for key in (
            "cover_motifs",
            "cover_emotion",
            "meme_picks",
            "quad_canon",
        ):
            if preserve.get(key):
                manifest[key] = preserve[key]
    return apply_quad_canon_to_manifest(manifest)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--out", default="cover/quad-manifest.json")
    ap.add_argument("--merge", action="store_true")
    ap.add_argument(
        "--merge-scene-draft",
        action="store_true",
        help="Merge cover/scene-draft.json (Derouter cover-scene) into manifest after scaffold",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = article_dir / out_path

    preserve = load_json(out_path) if args.merge and out_path.is_file() else None
    try:
        manifest = build_manifest(article_dir, root, preserve)
    except ValueError as exc:
        print(f"❌ QUAD MANIFEST BLOCKER: {exc}", file=sys.stderr)
        return 1

    scene_path = article_dir / "cover" / "scene-draft.json"
    if args.merge_scene_draft and scene_path.is_file():
        scene = load_json(scene_path)
        manifest = merge_scene_draft_into_manifest(manifest, scene)
        print(f"OK merged scene-draft from {scene_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(out_path, manifest)
    print(f"OK manifest={out_path}")
    missing = []
    if not manifest.get("cover_hook"):
        missing.append("cover_hook")
    slot_keys = ("cover",) + active_inline_keys(manifest.get("inline_count") or 7)
    for key in slot_keys:
        slot = manifest["slots"][key]
        if not slot.get("scene_hint"):
            missing.append(f"{key}.scene_hint")
        if not slot.get("alt"):
            missing.append(f"{key}.alt")
    if missing:
        print(
            "WARN agent must invent before image API: " + ", ".join(missing),
            file=sys.stderr,
        )
    for key in active_inline_keys(manifest.get("inline_count") or 7):
        s = manifest["slots"][key]
        print(f"  {key}: {s['visual_type']} -> {s['h2_anchor']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
