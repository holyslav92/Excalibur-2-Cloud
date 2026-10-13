#!/usr/bin/env python3
"""Правила размещения inline-картинок относительно WP featured cover (tymenrieltor.ru).

На сайте обложка = post thumbnail сразу под H1. Inline в post_content не должны
визуально «липнуть» к обложке или друг к другу.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

# Первые N секций H2 без картинок (после featured cover в теме).
OPENING_H2_SECTIONS_WITHOUT_IMAGES = 2

# 0-based индекс первого H2, куда можно ставить inline (3-я секция).
FIRST_INLINE_H2_INDEX = 2

FIGURE_BLOCK_RE = re.compile(
    r'<figure[^>]*class="[^"]*inline-quad[^"]*"[^>]*>[\s\S]*?</figure>',
    flags=re.I,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def h2_titles_from_html(html: str) -> list[str]:
    titles: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", html or "", flags=re.I | re.S):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        if title.lower() in {"частые вопросы", "faq"}:
            break
        titles.append(title)
    return titles


def _normalize_title(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text or "")
    text = re.sub(r"[^\wа-яА-ЯёЁ]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip().lower()


def spread_h2_indices(h2_count: int, n_slots: int, first_index: int = FIRST_INLINE_H2_INDEX) -> list[int]:
    """Равномерно распределить n_slots по H2, начиная с first_index (0-based)."""
    if h2_count <= first_index:
        raise ValueError(f"need at least {first_index + 1} H2 sections for inline placement")
    eligible = list(range(first_index, h2_count))
    if len(eligible) < n_slots:
        raise ValueError(
            f"need {n_slots} distinct H2 sections from index {first_index}; "
            f"only {len(eligible)} available (h2_count={h2_count})"
        )
    if n_slots == 1:
        return [eligible[0]]
    if n_slots == len(eligible):
        return eligible
    step = (len(eligible) - 1) / (n_slots - 1)
    picked: list[int] = []
    used: set[int] = set()
    for i in range(n_slots):
        idx = eligible[int(round(i * step))]
        while idx in used and idx + 1 < h2_count:
            idx += 1
        if idx in used:
            idx = eligible[-1]
        used.add(idx)
        picked.append(idx)
    return sorted(picked)


def min_h2_count_for_inline_slots(n_inline: int) -> int:
    return max(5, FIRST_INLINE_H2_INDEX + n_inline)


def figure_insert_offset_after_lead_paragraph(section_html: str) -> int:
    """Смещение внутри секции H2: после первого абзаца, не сразу под заголовком."""
    match = re.search(r"</p>\s*", section_html, flags=re.I)
    if match:
        return match.end()
    return 0


def check_no_cover_adjacent_image_stack(
    html: str,
    *,
    article_dir: Path | None = None,
) -> tuple[bool, list[str]]:
    """FAIL: картинки в зоне обложки, соседние figure, >1 figure на H2, дубль H1 в alt."""
    errors: list[str] = []
    if not html:
        return False, ["article html empty"]

    first_h2 = re.search(r"<h2\b", html, flags=re.I)
    if first_h2:
        preamble = html[: first_h2.start()]
        if FIGURE_BLOCK_RE.search(preamble):
            errors.append(
                "cover_adjacent: inline figure before first H2 (featured cover already under H1)"
            )

    h2s = h2_titles_from_html(html)
    if h2s:
        for i in range(min(OPENING_H2_SECTIONS_WITHOUT_IMAGES, len(h2s))):
            title = h2s[i]
            pattern = re.compile(
                rf"<h2[^>]*>\s*{re.escape(title)}\s*</h2>(.*?)(?=<h2\b|$)",
                flags=re.I | re.S,
            )
            match = pattern.search(html)
            if not match:
                continue
            body = match.group(1) or ""
            if FIGURE_BLOCK_RE.search(body):
                errors.append(
                    f"cover_adjacent: figure in opening H2 section #{i + 1} «{title[:48]}» "
                    f"(first {OPENING_H2_SECTIONS_WITHOUT_IMAGES} sections must be prose-only)"
                )

    figures = list(FIGURE_BLOCK_RE.finditer(html))
    for i in range(len(figures) - 1):
        between = html[figures[i].end() : figures[i + 1].start()]
        stripped = re.sub(r"\s+", "", between)
        if not stripped:
            errors.append("cover_adjacent: two inline figures adjacent with no content between")
            break
        if not re.search(r"<h2\b", between, flags=re.I) and not re.search(
            r"</p>\s*<p\b", between, flags=re.I
        ):
            if len(stripped) < 80 and FIGURE_BLOCK_RE.search(between) is None:
                errors.append(
                    "cover_adjacent: inline figures too close — need a full paragraph between"
                )
                break

    per_h2: dict[str, int] = {}
    h2_pattern = re.compile(r"<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)", flags=re.I | re.S)
    for match in h2_pattern.finditer(html):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if title.lower() in {"частые вопросы", "faq"}:
            break
        body = match.group(2) or ""
        n = len(FIGURE_BLOCK_RE.findall(body))
        if n > 1:
            errors.append(f"cover_adjacent: H2 «{title[:48]}» has {n} inline figures (max 1)")

    if article_dir is not None:
        errors.extend(_check_h1_not_in_inline_alt(article_dir, html))

    return (not errors, errors)


def _check_h1_not_in_inline_alt(article_dir: Path, html: str) -> list[str]:
    errors: list[str] = []
    meta_path = article_dir / "article.meta.json"
    title = ""
    if meta_path.is_file():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            title = str(meta.get("title") or meta.get("h1") or "").strip()
        except json.JSONDecodeError:
            pass
    hook = ""
    for rel in ("cover/cover-text.json", "cover/quad-manifest.json"):
        path = article_dir / rel
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        hook = str(data.get("cover_hook") or data.get("hook") or hook).strip()
    needles = {_normalize_title(title), _normalize_title(hook)}
    needles = {n for n in needles if len(n) >= 12}
    if not needles:
        return errors
    for fig in FIGURE_BLOCK_RE.finditer(html):
        alt_m = re.search(r'\balt="([^"]*)"', fig.group(0), flags=re.I)
        if not alt_m:
            continue
        alt_norm = _normalize_title(alt_m.group(1))
        for needle in needles:
            if needle and needle in alt_norm:
                errors.append("cover_adjacent: inline alt repeats H1/cover_hook text")
                return errors
    return errors


def manifest_h2_index(manifest: dict[str, Any], slot_key: str, h2s: list[str]) -> int | None:
    anchor = str(((manifest.get("slots") or {}).get(slot_key) or {}).get("h2_anchor") or "").strip()
    if not anchor:
        return None
    for i, h in enumerate(h2s):
        if h == anchor:
            return i
    return None


def check_manifest_inline_h2_indices(manifest: dict[str, Any], h2s: list[str]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    inline_count = int(manifest.get("inline_count") or 7)
    slots = manifest.get("slots") or {}
    for i in range(1, inline_count + 1):
        key = f"inline_{i}"
        idx = manifest_h2_index(manifest, key, h2s)
        if idx is None:
            continue
        if idx < FIRST_INLINE_H2_INDEX:
            errors.append(f"{key} h2_anchor is in opening zone (H2 index {idx}, min {FIRST_INLINE_H2_INDEX})")
    anchors: list[str] = []
    for i in range(1, inline_count + 1):
        key = f"inline_{i}"
        anchor = str((slots.get(key) or {}).get("h2_anchor") or "").strip()
        if anchor:
            anchors.append(anchor)
    if len(anchors) != len(set(anchors)):
        errors.append("cover_adjacent: duplicate h2_anchor on multiple inline slots (max 1 image per H2)")
    return (not errors, errors)
