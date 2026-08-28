#!/usr/bin/env python3
"""Canonical inline visual_type ids + legacy alias normalization."""

from __future__ import annotations

# Legacy ids still emitted by Derouter / old manifests / cover-registry.
VISUAL_TYPE_ALIASES: dict[str, str] = {
    "comparison_table_ui": "comparison_table",
}

CANONICAL_VISUAL_TYPES: frozenset[str] = frozenset(
    {
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
    }
)


def normalize_visual_type(raw: str) -> str:
    value = str(raw or "").strip()
    if not value:
        return value
    return VISUAL_TYPE_ALIASES.get(value, value)


def is_valid_visual_type(raw: str) -> bool:
    return normalize_visual_type(raw) in CANONICAL_VISUAL_TYPES
