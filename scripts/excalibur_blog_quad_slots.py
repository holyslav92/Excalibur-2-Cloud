"""Quad canvas slot layout: 3-inline (1 canvas) or 7-inline (2 canvases, 8 panels)."""

from __future__ import annotations

from excalibur_blog_cover_slots import (
    CANVAS_FILES,
    CANVAS_SLOT_GROUPS,
    DEFAULT_SLOT_MAP,
    INLINE_COUNT,
)

CANVAS_1_SLOTS = CANVAS_SLOT_GROUPS[0]
CANVAS_2_SLOTS = CANVAS_SLOT_GROUPS[1]


def inline_count_from_tenant(tenant: dict) -> int:
    raw = tenant.get("inline_panel_count") or tenant.get("inline_count")
    if raw in (3, 7):
        return int(raw)
    pipeline = str(tenant.get("cover_pipeline") or "")
    if "8_panel" in pipeline or "dual_2k" in pipeline:
        return 7
    return 3


def inline_count_from_manifest(manifest: dict) -> int:
    raw = manifest.get("inline_count")
    if raw in (3, 7):
        return int(raw)
    pipeline = str(manifest.get("pipeline") or "")
    if "longform" in pipeline or manifest.get("canvases"):
        return 7
    return 3


def active_inline_keys(inline_count: int) -> tuple[str, ...]:
    n = max(1, min(int(inline_count), INLINE_COUNT))
    return tuple(f"inline_{i}" for i in range(1, n + 1))


def canvas_specs_for_inline_count(inline_count: int) -> list[dict]:
    if int(inline_count) == 7:
        return [
            {
                "index": 1,
                "canvas_file": CANVAS_FILES[0],
                "batch_file": "cover/quad-mcp-batch-01.json",
                "prompt_file": "cover/quad-mcp-prompt-01.txt",
                "result_file": "cover/quad-mcp-result-01.json",
                "slots": list(CANVAS_SLOT_GROUPS[0]),
                "has_cover": True,
            },
            {
                "index": 2,
                "canvas_file": CANVAS_FILES[1],
                "batch_file": "cover/quad-mcp-batch-02.json",
                "prompt_file": "cover/quad-mcp-prompt-02.txt",
                "result_file": "cover/quad-mcp-result-02.json",
                "slots": list(CANVAS_SLOT_GROUPS[1]),
                "has_cover": False,
            },
        ]
    return [
        {
            "index": 1,
            "canvas_file": "cover/canvas-quad.png",
            "batch_file": "cover/quad-mcp-batch.json",
            "prompt_file": "cover/quad-mcp-prompt.txt",
            "result_file": "cover/quad-mcp-result.json",
            "slots": list(CANVAS_SLOT_GROUPS[0]),
            "has_cover": True,
        },
    ]
