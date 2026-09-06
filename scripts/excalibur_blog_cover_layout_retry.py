"""Shared TEXT_LAYOUT retry markers for grsai solo cover + quad panel regen."""

from __future__ import annotations

# Attempt 2+ when attempt 1 misses headline/phone/layout (B13/B20 pattern).
TEXT_LAYOUT_RETRY_SUFFIX = (
    "TEXT LAYOUT LOCK (mandatory retry): Cyrillic headline hook MUST be large and readable "
    "in RIGHT sacred zone (52–96% width, 14–40% height) — NOT face-only crop. "
    "Phone CTA digits «+7 922 001 65 05» fully readable bottom-right on white torn paper. "
    "ZERO Wordstat/search-keyword strips or beige query bars. Host face left ~35% frame width."
)

TEXT_LAYOUT_FAIL_MARKERS = (
    "pixel_hook_title_present",
    "pixel_phone_readable",
    "pixel_layout_not_collapsed",
    "pixel_no_wordstat_query_strips",
    "pixel_hook_title_not_truncated",
    "pixel_designed_thumbnail",
)


def needs_text_layout_retry(errors: list[str]) -> bool:
    blob = " ".join(errors)
    return any(marker in blob for marker in TEXT_LAYOUT_FAIL_MARKERS)
