#!/usr/bin/env python3
"""Shared HTML merge helpers for Sol/Writer chunk+trim pipelines."""

from __future__ import annotations

import re


def normalize_h2_title(raw: str) -> str:
    text = re.sub(r"<[^>]+>", "", raw or "")
    return re.sub(r"\s+", " ", text).strip().casefold()


def h2_titles_in_order(html: str) -> list[str]:
    titles: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", html or "", flags=re.I | re.S):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if title:
            titles.append(title)
    return titles


def split_html_by_h2_sections(html: str) -> list[tuple[str | None, str]]:
    """Return (h2_title_or_none_for_preamble, section_html) in document order."""
    pattern = re.compile(r"<h2[^>]*>", re.I)
    matches = list(pattern.finditer(html or ""))
    if not matches:
        body = (html or "").strip()
        return [(None, body)] if body else []

    sections: list[tuple[str | None, str]] = []
    if matches[0].start() > 0:
        preamble = html[: matches[0].start()].strip()
        if preamble:
            sections.append((None, preamble))

    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(html)
        chunk = html[start:end].strip()
        if not chunk:
            continue
        title_match = re.search(r"<h2[^>]*>(.*?)</h2>", chunk, flags=re.I | re.S)
        title = None
        if title_match:
            title = re.sub(r"<[^>]+>", "", title_match.group(1))
            title = re.sub(r"\s+", " ", title).strip()
        sections.append((title, chunk))
    return sections


def dedupe_duplicate_h2_sections(html: str) -> tuple[str, list[str]]:
    """Drop later H2 sections with the same title (Sol chunk boundary bleed, B21).

    Keeps the first occurrence of each H2 title; preamble (pre-first-H2) is preserved once.
    """
    sections = split_html_by_h2_sections(html)
    if not sections:
        return html, []

    kept: list[str] = []
    seen_h2: set[str] = set()
    dropped: list[str] = []

    for title, chunk in sections:
        if title is None:
            kept.append(chunk)
            continue
        key = normalize_h2_title(title)
        if key in seen_h2:
            dropped.append(title)
            continue
        seen_h2.add(key)
        kept.append(chunk)

    merged = "\n\n".join(part.strip() for part in kept if part.strip())
    if merged and not merged.endswith("\n"):
        merged += "\n"
    return merged, dropped


def merge_html_fragments(fragments: list[str], *, dedupe_h2: bool = True) -> str:
    parts: list[str] = []
    for frag in fragments:
        text = frag.strip()
        if not text:
            continue
        text = re.sub(r"^```(?:html)?\s*", "", text)
        text = re.sub(r"\s*```\s*$", "", text)
        parts.append(text.strip())
    merged = "\n\n".join(parts)
    if merged and not merged.endswith("\n"):
        merged += "\n"
    if dedupe_h2:
        merged, _ = dedupe_duplicate_h2_sections(merged)
    return merged
