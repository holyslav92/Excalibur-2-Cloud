#!/usr/bin/env python3
"""Block research-brief / API-calque junk in article opening + meta description.

Opening lives in article.html (Writer). Optional orphan lead.md is scanned
if present; missing file is OK.

Also blocks TL;DR / «Быстрый инсайт» bullet-dumps in the first screen —
canon is a prose lead (4–6 sentences) before early CTA.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


# Calque of "API" that reads as machine Russian, not Lebedev.
STYK_API_RE = re.compile(
    r"стык(?:а|у|ом|е|и)?\s+(?:для\s+программ|с\s+(?:сайтом|api)|с\s+api)"
    r"|без\s+(?:готового\s+)?стыка"
    r"|где\s+стыка\s+нет"
    r"|открытого\s+стыка",
    re.IGNORECASE,
)

# Pipeline / research brief leaking into public text.
RESEARCH_BRIEF_RES = (
    re.compile(r"факты\s+запуска", re.I),
    re.compile(r"оговорк[аиуеы]\s+пресс", re.I),
    re.compile(r"смотрите\s+на\s+факты", re.I),
    re.compile(r"не\s+путайте\s+с\s+готовым", re.I),
    re.compile(r"VentureBeat\s+просит", re.I),
    re.compile(r"сверять\s+поколение", re.I),
    re.compile(r"reader_outcome|reader_problem|WORDSTAT|research_date", re.I),
    re.compile(r"^\s*\d{1,2}\s+[а-яё]+\s+20\d{2}\b", re.I | re.M),
    re.compile(r"^\s*\d{2}\.\d{2}\.20\d{2}\b", re.M),
)

TLDR_RE = re.compile(r"tl\s*;?\s*dr", re.I)
FAST_INSIGHT_RE = re.compile(r"быстрый\s+инсайт(?:ер)?", re.I)
PROSE_LEAD_MIN_SENTENCES = 4


def _plain(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "")


def first_screen_html(html: str) -> str:
    """Content before first H2 — hook + prose lead + early CTA zone."""
    m = re.search(r"<h2\b", html or "", flags=re.I)
    if m:
        return (html or "")[: m.start()]
    return html or ""


def strip_early_cta(screen: str) -> str:
    return re.sub(
        r"<div[^>]*class=\"[^\"]*excalibur-cta-early[^\"]*\"[^>]*>.*?</div>",
        " ",
        screen or "",
        flags=re.I | re.S,
    )


def count_prose_sentences(screen: str) -> int:
    prose = _plain(strip_early_cta(screen))
    prose = re.sub(r"\s+", " ", prose).strip()
    if not prose:
        return 0
    parts = re.split(r"(?<=[.!?…])\s+", prose)
    return len([p for p in parts if len(p.strip()) >= 12])


def opening_bullet_list_errors(screen: str) -> list[str]:
    errors: list[str] = []
    if re.search(r"<(?:ul|ol)\b", screen or "", flags=re.I):
        li_count = len(re.findall(r"<li\b", screen or "", flags=re.I))
        if li_count >= 2:
            errors.append(f"opening-bullet-list:{li_count}-items")
    return errors


def opening_tldr_errors(screen: str) -> list[str]:
    errors: list[str] = []
    plain = _plain(screen)
    if TLDR_RE.search(screen or "") or TLDR_RE.search(plain):
        errors.append("tldr-label")
    if FAST_INSIGHT_RE.search(plain):
        errors.append("fast-insight-block")
    errors.extend(opening_bullet_list_errors(screen))
    sentences = count_prose_sentences(screen)
    if sentences < PROSE_LEAD_MIN_SENTENCES:
        errors.append(f"prose-lead-too-short:{sentences}-sentences")
    return errors


def _hits(text: str) -> list[str]:
    found: list[str] = []
    if STYK_API_RE.search(text):
        found.append("api-calque-styk")
    for rx in RESEARCH_BRIEF_RES:
        m = rx.search(text)
        if m:
            found.append(f"research-brief:{m.group(0)[:48]}")
    return found


def check_article(article_dir: Path) -> dict[str, Any]:
    errors: list[str] = []
    orphan_lead = article_dir / "lead.md"
    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"

    if orphan_lead.is_file():
        lead = _plain(orphan_lead.read_text(encoding="utf-8"))
        for h in _hits(lead):
            errors.append(f"lead.md: {h}")
        for h in opening_tldr_errors(lead):
            errors.append(f"lead.md: {h}")

    meta: dict[str, Any] = {}
    if meta_path.is_file():
        try:
            loaded = json.loads(meta_path.read_text(encoding="utf-8"))
            meta = loaded if isinstance(loaded, dict) else {}
        except json.JSONDecodeError:
            errors.append("article.meta.json: invalid JSON")
            meta = {}
        blobs = [
            str(meta.get("description") or ""),
            str((meta.get("meta_ab") or {}).get("description_seo") or ""),
            str((meta.get("meta_ab") or {}).get("description_ctr") or ""),
            str((meta.get("meta_ab") or {}).get("description_aeo") or ""),
            str(meta.get("cover_hook") or ""),
        ]
        for i, blob in enumerate(blobs):
            for h in _hits(blob):
                errors.append(f"article.meta.json[{i}]: {h}")
    else:
        errors.append("article.meta.json missing")

    if html_path.is_file():
        html_raw = html_path.read_text(encoding="utf-8")
        html = _plain(html_raw)
        head = html[:900]
        for h in _hits(head):
            errors.append(f"article.html-head: {h}")
        if STYK_API_RE.search(html):
            errors.append("article.html: api-calque-styk")
        screen = first_screen_html(html_raw)
        for h in opening_tldr_errors(screen):
            errors.append(f"article.html-opening: {h}")
    else:
        errors.append("article.html missing")

    status = "PASS" if not errors else "BLOCK"
    return {
        "gate": "opening-meta",
        "status": status,
        "errors": errors,
        "article_dir": str(article_dir),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("-o", "--output", type=str, default="opening-meta-gate.json")
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER: article-dir not found: {article_dir}", file=sys.stderr)
        return 2
    report = check_article(article_dir)
    out_name = Path(args.output).name
    out_path = article_dir / out_name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
