"""FAIL when body glues unrelated calendar/news hooks onto a casus they do not cause."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

# Календарные/медийные якоря, которые часто цепляют к чужому сюжету (B34 INC).
CALENDAR_NEWS_GLUE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"1\s+октября\s+2026", re.I),
    re.compile(r"изменени[ея]\s+условий\s+семейн\w+\s+ипотек", re.I),
    re.compile(r"новост\w*\s+обсуждал\w*\s+.{0,40}семейн\w+\s+ипотек", re.I),
    re.compile(r"семья\s+считала\s+дни", re.I),
    re.compile(r"ипотечн\w+\s+дедлайн\s+не\s+исправ", re.I),
    re.compile(r"не\s+успеть\s+из-за\s+изменени\w+\s+условий\s+семейн", re.I),
)

# Сюжет явно про семейную ипотеку / дедлайн программы — glue допустим.
CASUS_ALLOWS_FAMILY_MORTGAGE_NEWS = re.compile(
    r"семейн\w+\s+ипотек|1\s+октября\s+2026|льготн\w+\s+ипотек|"
    r"ребёнк\w+\s+исполнилось|одна\s+семья\s+—\s+одна\s+льгот",
    re.I,
)

def _strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    return re.sub(r"\s+", " ", text).strip()


def _load_title_brief(article_dir: Path) -> dict[str, Any]:
    path = article_dir / "title-brief.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _load_meta(article_dir: Path) -> dict[str, Any]:
    path = article_dir / "article.meta.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def declared_casus_text(article_dir: Path, meta: dict[str, Any], title_brief: dict[str, Any]) -> str:
    parts = [
        meta.get("h1") or meta.get("title") or "",
        title_brief.get("h1") or title_brief.get("title") or "",
        title_brief.get("subject") or "",
        title_brief.get("angle") or "",
    ]
    return " ".join(str(p) for p in parts if p)


def calendar_news_glue_hits(plain_body: str) -> list[str]:
    hits: list[str] = []
    for rx in CALENDAR_NEWS_GLUE_PATTERNS:
        if rx.search(plain_body):
            hits.append(rx.pattern)
    return hits


def casus_allows_family_mortgage_calendar(declared: str) -> bool:
    return bool(CASUS_ALLOWS_FAMILY_MORTGAGE_NEWS.search(declared))


def check_no_unrelated_calendar_news_glue(
    html: str,
    *,
    article_dir: Path | None = None,
    meta: dict[str, Any] | None = None,
    title_brief: dict[str, Any] | None = None,
) -> tuple[bool, list[str]]:
    """
    PASS, если календарные новостные якоря отсутствуют или являются механизмом casus.
    FAIL, если в теле есть glue-паттерны, а H1/subject/angle не про эту новость.
    """
    plain = _strip_html(html)
    hits = calendar_news_glue_hits(plain)
    if not hits:
        return True, []

    if article_dir is not None:
        meta = meta if meta is not None else _load_meta(article_dir)
        title_brief = title_brief if title_brief is not None else _load_title_brief(article_dir)
    meta = meta or {}
    title_brief = title_brief or {}

    declared = declared_casus_text(article_dir or Path("."), meta, title_brief)
    if casus_allows_family_mortgage_calendar(declared):
        return True, []

    errors = [
        "no_unrelated_calendar_news_glue: в теле есть календарный/медийный якорь чужой рубрики "
        f"({', '.join(hits[:3])}), не объявленный в H1/subject/angle casus"
    ]
    return False, errors
