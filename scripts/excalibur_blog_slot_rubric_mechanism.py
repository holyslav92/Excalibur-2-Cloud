"""FAIL when casus/news/law layer uses another slot rubric's distinctive mechanism (owner 2026-09-29)."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from excalibur_blog_unrelated_news_glue import declared_casus_text

# Отличительные механизмы рубрики — не общие слова вроде «ипотека» / «квартира».
DISTINCTIVE_MECHANISMS: dict[str, tuple[tuple[str, str], ...]] = {
    "novostroyki": (
        (r"\bброн[ьи]\w*", "бронь (новостройки)"),
        (r"\bдду\b", "ДДУ"),
        (r"эскроу", "эскроу"),
        (r"застройщик", "застройщик"),
        (r"переуступк", "переуступка"),
        (r"долгострой", "долгострой"),
        (r"при[её]мк\w*\s+(?:квартир|ключ)", "приёмка у застройщика"),
        (r"срок\s+сдач", "срок сдачи"),
        (r"ключ\w*\s+от\s+застройщик", "ключи от застройщика"),
    ),
    "vtorichka": (
        (r"дарственн", "дарственная"),
        (r"\bаванс\w*", "аванс"),
        (r"\bегрн\b", "ЕГРН"),
        (r"обременен", "обременение"),
        (r"\bдкп\b", "ДКП"),
        (r"банкрот\w*\s+продав", "банкрот продавца"),
        (r"опек\w*", "опека"),
    ),
    "arenda": (
        (r"выселен", "выселение"),
        (r"квартирант", "квартирант"),
        (r"договор\s+аренд", "договор аренды"),
        (r"залог\s+.{0,24}аренд", "залог по аренде"),
        (r"краткосрочн\w+\s+съ?[её]м", "краткосрочная съёмка"),
        (r"найм\s+жил", "найм жилья"),
    ),
}

_VALID_RUBRICS = frozenset(DISTINCTIVE_MECHANISMS)


def _strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    return re.sub(r"\s+", " ", text).strip()


def _load_meta(article_dir: Path) -> dict[str, Any]:
    path = article_dir / "article.meta.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def rubric_per_slot_enabled(root: Path | None = None) -> bool:
    root = root or _project_root()
    path = root / "shared" / "tenant-config.json"
    if not path.is_file():
        return False
    try:
        tenant = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    focus = str(tenant.get("topic_market_focus") or "").strip().lower()
    return focus in {"rubric_per_slot", "slot_rubric", "multi_rubric"}


def resolve_article_slot_rubric(article_dir: Path | None = None) -> str | None:
    """Рубрика слота для статьи: meta.slot_rubric → активный слот тенанта."""
    root = _project_root()
    if article_dir is not None:
        meta = _load_meta(article_dir)
        explicit = str(meta.get("slot_rubric") or "").strip()
        if explicit in _VALID_RUBRICS:
            return explicit
    if not rubric_per_slot_enabled(root):
        return None
    from excalibur_blog_topic_focus import active_slot_rubric

    rub = active_slot_rubric()
    return rub if rub in _VALID_RUBRICS else None


def _compiled_patterns() -> dict[str, list[tuple[re.Pattern[str], str]]]:
    out: dict[str, list[tuple[re.Pattern[str], str]]] = {}
    for rubric, items in DISTINCTIVE_MECHANISMS.items():
        out[rubric] = [(re.compile(pat, re.I), label) for pat, label in items]
    return out


_COMPILED = _compiled_patterns()


def casus_declares_rubric_mechanism(declared_casus: str, rubric: str) -> bool:
    """True, если H1/subject/angle явно про механику этой рубрики."""
    for rx, _label in _COMPILED.get(rubric, []):
        if rx.search(declared_casus or ""):
            return True
    return False


def foreign_mechanism_hits(
    text: str,
    declared_rubric: str,
    *,
    declared_casus: str = "",
) -> list[str]:
    """
    Список чужих механизмов в text. Пропускает рубрику, если casus уже объявляет её механику.
    """
    hits: list[str] = []
    if declared_rubric not in _VALID_RUBRICS:
        return hits
    blob = text or ""
    for foreign_rubric, patterns in _COMPILED.items():
        if foreign_rubric == declared_rubric:
            continue
        if declared_casus and casus_declares_rubric_mechanism(declared_casus, foreign_rubric):
            continue
        for rx, label in patterns:
            if rx.search(blob):
                hits.append(f"{foreign_rubric}:{label}")
                break
    return hits


def check_no_foreign_slot_rubric_mechanism(
    html: str,
    *,
    article_dir: Path | None = None,
    meta: dict[str, Any] | None = None,
    title_brief: dict[str, Any] | None = None,
    declared_rubric: str | None = None,
) -> tuple[bool, list[str]]:
    """
    PASS, если текст не тащит механику чужой рубрики слота.
    Для тенантов без rubric_per_slot — всегда PASS.
    """
    rubric = declared_rubric or (
        resolve_article_slot_rubric(article_dir) if article_dir else None
    )
    if not rubric:
        return True, []

    if article_dir is not None:
        meta = meta if meta is not None else _load_meta(article_dir)
        if title_brief is None:
            from excalibur_blog_unrelated_news_glue import _load_title_brief

            title_brief = _load_title_brief(article_dir)
    meta = meta or {}
    title_brief = title_brief or {}

    plain = _strip_html(html)
    h1 = str(meta.get("h1") or meta.get("title") or title_brief.get("h1") or "")
    combined = f"{h1} {plain}".strip()
    declared = declared_casus_text(article_dir or Path("."), meta, title_brief)

    hits = foreign_mechanism_hits(combined, rubric, declared_casus=declared)
    if not hits:
        return True, []

    errors = [
        "no_foreign_slot_rubric_mechanism: в H1/теле механика чужой рубрики слота "
        f"(слот={rubric}; найдено: {', '.join(hits[:4])}). "
        "Casus, новость и право — только внутри рубрики слота; см. shared/slot-rubric-lock.md"
    ]
    return False, errors


def title_has_foreign_mechanism_for_rubric(title: str, slot_rubric: str) -> bool:
    """Trend Radar / Scout: viral headline с чужой механикой."""
    return bool(foreign_mechanism_hits(title or "", slot_rubric))
