#!/usr/bin/env python3
"""Gates and helpers: one cover at top (theme featured), inlines deep in body.

WordPress theme renders post thumbnail immediately under H1. Inlines must not
stack under the featured image (first H2 with figure flush on top, adjacent
figures, or hook-duplicating infographic).
"""

from __future__ import annotations

import re
from typing import Any

# 0-based H2 index: first inline anchor must be the 2nd H2 or later (after lead).
MIN_H2_INDEX_FOR_INLINE = 1

# Minimum visible text before the first figure inside an H2 section.
MIN_PARAGRAPH_CHARS_BEFORE_FIGURE = 48

_H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.I | re.S)
_FIGURE_RE = re.compile(
    r'<figure[^>]*class="[^"]*inline-(?:quad|visual)[^"]*"[^>]*>[\s\S]*?</figure>',
    re.I,
)
_P_TAG_RE = re.compile(r"<p\b[^>]*>[\s\S]*?</p>", re.I)


def _strip_tags(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    return re.sub(r"\s+", " ", text).strip()


def h2_titles_in_order(html: str) -> list[str]:
    titles: list[str] = []
    for match in _H2_RE.finditer(html or ""):
        title = _strip_tags(match.group(1))
        if not title:
            continue
        if title.lower() in {"частые вопросы", "faq"}:
            break
        titles.append(title)
    return titles


def _h2_section_spans(html: str) -> list[tuple[str, int, int]]:
    """(normalized title, section_start, section_end) for each H2 block."""
    spans: list[tuple[str, int, int]] = []
    matches = list(_H2_RE.finditer(html or ""))
    for idx, match in enumerate(matches):
        title = _strip_tags(match.group(1))
        if title.lower() in {"частые вопросы", "faq"}:
            break
        section_start = match.end()
        section_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(html)
        spans.append((title.casefold(), section_start, section_end))
    return spans


def h2_index_for_offset(html: str, offset: int) -> int | None:
    """0-based index of the H2 section containing ``offset``."""
    for i, (_title, start, end) in enumerate(_h2_section_spans(html)):
        if start <= offset < end:
            return i
    return None


def inline_figure_spans(html: str) -> list[tuple[int, int, str]]:
    """List of (start, end, figure_html) for inline figures in document order."""
    out: list[tuple[int, int, str]] = []
    for match in _FIGURE_RE.finditer(html or ""):
        out.append((match.start(), match.end(), match.group(0)))
    return out


def _chars_before_figure_in_section(section_html: str, figure_start_in_section: int) -> int:
    prefix = section_html[:figure_start_in_section]
    # Ignore other figures in prefix when measuring prose gap.
    prefix = _FIGURE_RE.sub(" ", prefix)
    return len(_strip_tags(prefix))


def check_inline_no_cover_stack(html: str) -> tuple[bool, list[str]]:
    """FAIL when inlines would stack under theme featured image or each other."""
    errors: list[str] = []
    figures = inline_figure_spans(html)
    if not figures:
        return True, []

    h2s = h2_titles_in_order(html)
    if not h2s:
        errors.append("inline_cover_stack: article has inline figures but no H2 sections")
        return False, errors

    first_start, first_end, _ = figures[0]
    first_h2_idx = h2_index_for_offset(html, first_start)
    if first_h2_idx is None:
        errors.append("inline_cover_stack: first inline figure is outside any H2 section")
    elif first_h2_idx < MIN_H2_INDEX_FOR_INLINE:
        errors.append(
            "inline_cover_stack: first inline under H2 #1 — theme featured already shows "
            f"cover; anchor from H2 #{MIN_H2_INDEX_FOR_INLINE + 1} onward"
        )

    for start, end, _fig in figures:
        h2_idx = h2_index_for_offset(html, start)
        if h2_idx is None:
            continue
        for _title, sec_start, sec_end in _h2_section_spans(html):
            if sec_start <= start < sec_end:
                rel = start - sec_start
                chars = _chars_before_figure_in_section(html[sec_start:sec_end], rel)
                if chars < MIN_PARAGRAPH_CHARS_BEFORE_FIGURE:
                    errors.append(
                        f"inline_cover_stack: figure under H2 #{h2_idx + 1} needs "
                        f"≥{MIN_PARAGRAPH_CHARS_BEFORE_FIGURE} chars of prose before it "
                        f"(got {chars})"
                    )
                break

    for i in range(len(figures) - 1):
        prev_end = figures[i][1]
        next_start = figures[i + 1][0]
        between = html[prev_end:next_start]
        between_no_ws = re.sub(r"\s+", "", between)
        if not between_no_ws or _FIGURE_RE.search(between):
            errors.append("inline_cover_stack: adjacent inline figures (no prose between)")

    return (not errors, errors)


def _cover_hook_tokens(article_dir: Any) -> set[str]:
    """Tokens from cover hook for duplicate-meaning check (optional article_dir Path)."""
    from pathlib import Path

    if article_dir is None:
        return set()
    path = Path(article_dir) / "cover" / "cover-text.json"
    if not path.is_file():
        return set()
    try:
        import json

        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    hook = ""
    for key in ("hook", "title_hook", "cover_hook"):
        if data.get(key):
            hook = str(data[key])
            break
    texts = data.get("texts") or {}
    if not hook and isinstance(texts, dict):
        hook = str(texts.get("hook") or texts.get("title") or "")
    words = re.findall(r"[\wа-яА-ЯёЁ]{4,}", hook.lower(), flags=re.UNICODE)
    return set(words)


def check_inline_not_duplicate_cover_hook(
    html: str, article_dir: Any = None, title_brief: str = ""
) -> tuple[bool, list[str]]:
    """FAIL if the first inline alt/text repeats the cover hook / H1 meaning."""
    errors: list[str] = []
    figures = inline_figure_spans(html)
    if not figures:
        return True, []

    first_h2_idx = h2_index_for_offset(html, figures[0][0])
    if first_h2_idx is not None and first_h2_idx >= MIN_H2_INDEX_FOR_INLINE:
        # Deep placement — hook overlap on first inline is less critical.
        pass

    hook_tokens = _cover_hook_tokens(article_dir)
    if title_brief:
        hook_tokens |= set(
            re.findall(r"[\wа-яА-ЯёЁ]{4,}", title_brief.lower(), flags=re.UNICODE)
        )
    if not hook_tokens:
        return True, []

    first_fig = figures[0][2]
    alt_m = re.search(r'\balt="([^"]*)"', first_fig, re.I)
    alt = (alt_m.group(1) if alt_m else "").lower()
    if not alt:
        return True, []

    alt_tokens = set(re.findall(r"[\wа-яА-ЯёЁ]{4,}", alt, flags=re.UNICODE))
    overlap = hook_tokens & alt_tokens
    if len(overlap) >= 3:
        errors.append(
            "inline_cover_stack: first inline alt overlaps cover hook/H1 "
            f"({len(overlap)} shared tokens) — use section-specific meaning"
        )
    return (not errors, errors)


def figure_insert_after_paragraphs(
    html: str,
    h2: str,
    *,
    paragraphs_after: int = 1,
    skip_existing_figures: int = 0,
) -> int | None:
    """Byte offset to insert inline figure after N paragraphs in the H2 section."""
    pattern = re.compile(rf"<h2[^>]*>\s*{re.escape(h2)}\s*</h2>", re.I | re.S)
    match = pattern.search(html)
    if not match:
        return None
    section_start = match.end()
    next_h2 = re.search(r"<h2\b", html[section_start:], flags=re.I)
    section_end = section_start + next_h2.start() if next_h2 else len(html)
    section = html[section_start:section_end]

    paragraphs = list(_P_TAG_RE.finditer(section))
    if not paragraphs:
        return None

    target_p = min(paragraphs_after, len(paragraphs)) - 1
    insert_at = section_start + paragraphs[target_p].end()

    if skip_existing_figures:
        figs = list(_FIGURE_RE.finditer(section))
        if len(figs) >= skip_existing_figures:
            insert_at = section_start + figs[skip_existing_figures - 1].end()
            # After that figure, prefer next paragraph if any.
            tail = section[figs[skip_existing_figures - 1].end() :]
            next_p = _P_TAG_RE.search(tail)
            if next_p:
                insert_at = section_start + figs[skip_existing_figures - 1].end() + next_p.end()

    return insert_at


def combined_inline_cover_checks(
    html: str, article_dir: Any = None, title_brief: str = ""
) -> tuple[bool, list[str]]:
    ok1, e1 = check_inline_no_cover_stack(html)
    ok2, e2 = check_inline_not_duplicate_cover_hook(html, article_dir, title_brief)
    errors = e1 + e2
    return (ok1 and ok2, errors)
