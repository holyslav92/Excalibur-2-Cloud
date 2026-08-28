#!/usr/bin/env python3
"""Shared constants for Excalibur BLOG quad cover / inline slots."""

from __future__ import annotations

from typing import Any

# Longform canon (tymenrieltor.ru): cover + 7 inline = 8 images from 2 quad canvases.
INLINE_SLOT_KEYS: tuple[str, ...] = tuple(f"inline_{i}" for i in range(1, 8))
INLINE_FILES: dict[str, str] = {key: f"inline-{i:02d}.png" for i, key in enumerate(INLINE_SLOT_KEYS, start=1)}

CANVAS_1_SLOTS: tuple[str, ...] = ("cover", "inline_1", "inline_2", "inline_3")
CANVAS_2_SLOTS: tuple[str, ...] = ("inline_4", "inline_5", "inline_6", "inline_7")

DEFAULT_SLOT_MAP: dict[str, str] = {
    "cover": "top_left",
    "inline_1": "top_right",
    "inline_2": "bottom_left",
    "inline_3": "bottom_right",
    "inline_4": "top_left",
    "inline_5": "top_right",
    "inline_6": "bottom_left",
    "inline_7": "bottom_right",
}

CANVAS_SPECS: tuple[dict[str, Any], ...] = (
    {
        "index": 1,
        "canvas_file": "cover/canvas-quad-01.png",
        "batch_file": "cover/quad-mcp-batch-01.json",
        "prompt_file": "cover/quad-mcp-prompt-01.txt",
        "result_file": "cover/quad-mcp-result-01.json",
        "slots": CANVAS_1_SLOTS,
        "has_cover": True,
    },
    {
        "index": 2,
        "canvas_file": "cover/canvas-quad-02.png",
        "batch_file": "cover/quad-mcp-batch-02.json",
        "prompt_file": "cover/quad-mcp-prompt-02.txt",
        "result_file": "cover/quad-mcp-result-02.json",
        "slots": CANVAS_2_SLOTS,
        "has_cover": False,
    },
)

LEGACY_INLINE_SLOT_KEYS: tuple[str, ...] = ("inline_1", "inline_2", "inline_3")
LEGACY_CANVAS_FILE = "cover/canvas-quad.png"

# Derouter / old manifests sometimes emit legacy ids — map to catalog canon before gates.
VISUAL_TYPE_ALIASES: dict[str, str] = {
    "comparison_table_ui": "comparison_table",
}

CANONICAL_INLINE_VISUAL_TYPES: frozenset[str] = frozenset(
    {
        "comparison_table",
        "process_flow",
        "bar_timeline_chart",
        "structure_diagram",
        "labeled_checklist",
        "fact_card",
        # Legacy catalog ids (still valid; prompts map to canon rules)
        "workflow_diagram",
        "checklist_board",
        "schema_faq_ui",
        "tool_screenshot",
        "infographic_card",
    }
)


def normalize_visual_type(type_id: str) -> str:
    """Map legacy Derouter/manifest visual_type to catalog id."""
    raw = str(type_id or "").strip()
    if not raw:
        return raw
    return VISUAL_TYPE_ALIASES.get(raw, raw)
LEGACY_BATCH_FILE = "cover/quad-mcp-batch.json"
LEGACY_RESULT_FILE = "cover/quad-mcp-result.json"

# Owner canon (B03 postmortem): memes on 2–3 of 7 inlines + cover-adjacent.
# Fixed pattern: meme allowed on cover, inline_1, inline_5, inline_7 only.
MEME_ALLOWED_SLOTS: frozenset[str] = frozenset({"cover", "inline_1", "inline_5", "inline_7"})
NO_MEME_NO_CAT_SLOTS: frozenset[str] = frozenset({"inline_2", "inline_3", "inline_4", "inline_6"})
CANVAS_2_SLOTS_NO_HOST_FACE: frozenset[str] = frozenset(CANVAS_2_SLOTS)


def inline_count_from_manifest(manifest: dict[str, Any] | None) -> int:
    if not manifest:
        return 7
    if manifest.get("inline_count") in (3, 7):
        return int(manifest["inline_count"])
    canvases = manifest.get("canvases")
    if isinstance(canvases, list) and canvases:
        return 7
    pipeline = str(manifest.get("pipeline") or "")
    if "longform" in pipeline or "2x" in pipeline:
        return 7
    return 3


def inline_count_from_tenant(tenant: dict[str, Any] | None) -> int:
    if not tenant:
        return 7
    if tenant.get("inline_image_count") in (3, 7):
        return int(tenant["inline_image_count"])
    if str(tenant.get("publish_format") or "").casefold() == "longform":
        return 7
    if str(tenant.get("publish_format") or "").casefold() == "daily":
        return 0
    return 7


def active_inline_keys(inline_count: int) -> tuple[str, ...]:
    if inline_count <= 0:
        return ()
    if inline_count == 3:
        return LEGACY_INLINE_SLOT_KEYS
    return INLINE_SLOT_KEYS[:inline_count]


def canvas_specs_for_inline_count(inline_count: int) -> tuple[dict[str, Any], ...]:
    if inline_count == 3:
        return (
            {
                "index": 1,
                "canvas_file": LEGACY_CANVAS_FILE,
                "batch_file": LEGACY_BATCH_FILE,
                "prompt_file": "cover/quad-mcp-prompt.txt",
                "result_file": LEGACY_RESULT_FILE,
                "slots": CANVAS_1_SLOTS,
                "has_cover": True,
            },
        )
    return CANVAS_SPECS


def all_split_slot_keys(inline_count: int) -> tuple[str, ...]:
    if inline_count == 3:
        return CANVAS_1_SLOTS
    if inline_count == 7:
        return CANVAS_1_SLOTS + CANVAS_2_SLOTS
    return ("cover",) + active_inline_keys(inline_count)


def slot_allows_meme_sticker(slot_key: str) -> bool:
    return slot_key in MEME_ALLOWED_SLOTS


def slot_forbids_meme_cat_person(slot_key: str) -> bool:
    return slot_key in NO_MEME_NO_CAT_SLOTS


def apply_quad_canon_to_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    """HARD manifest flags: meme density, no_host_face, negatives — before image API."""
    inline_count = inline_count_from_manifest(manifest)
    if inline_count != 7:
        return manifest

    slots = manifest.setdefault("slots", {})
    for slot_key in ("cover",) + tuple(active_inline_keys(inline_count)):
        slot = slots.setdefault(slot_key, {})
        if slot_key != "cover":
            vt = normalize_visual_type(str(slot.get("visual_type") or ""))
            if vt:
                slot["visual_type"] = vt
        allows_meme = slot_allows_meme_sticker(slot_key)
        forbids = slot_forbids_meme_cat_person(slot_key)
        slot["meme_sticker"] = allows_meme
        slot["no_meme"] = forbids
        slot["no_cat"] = forbids
        slot["no_person"] = forbids
        if slot_key == "cover":
            slot["no_host_face"] = False
        else:
            slot["no_host_face"] = True

    manifest["quad_canon"] = {
        "meme_allowed_slots": sorted(MEME_ALLOWED_SLOTS),
        "no_meme_no_cat_slots": sorted(NO_MEME_NO_CAT_SLOTS),
        "canvas_2_no_host_face": True,
        "meme_inline_target": "2-3 of 7 inlines (pattern: 01, 05, 07)",
    }
    return manifest
