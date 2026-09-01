"""Detect banned composite-case / anonymization meta-disclaimers in article body."""
from __future__ import annotations

import re
from typing import Iterable

# Owner lock 2026-09-01: casus = конкретный день в комнате; без AI-дисклеймеров.
COMPOSITE_DISCLAIMER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"случай\s+собирательн", re.I),
    re.compile(r"собирательн\w+\s+(?:случа|сюжет|казус|casus)", re.I),
    re.compile(r"без\s+фамил(?:ий|ии)", re.I),
    re.compile(r"без\s+адреса(?:\s+жк|\s+корпуса)?", re.I),
    re.compile(r"без\s+названия\s+банка", re.I),
    re.compile(r"механика\s+в\s+тюмени\s+повторяется", re.I),
    re.compile(r"механика\s+типовая", re.I),
    re.compile(r"моделируем\w+\s+(?:финал|сюжет|вариант|casus|казус)", re.I),
    re.compile(r"смоделирован\w+\s+из\s+похож", re.I),
    re.compile(r"не\s+(?:подтверждённ|подтвержденн)\w+\s+(?:репортаж|публичн)", re.I),
    re.compile(r"\bне\s+репортаж\b", re.I),
    re.compile(r"намеренно\s+убрал\s+(?:имена|имя|адрес)", re.I),
    re.compile(r"рассказывать\s+чужую\s+сделку\s+поимённо", re.I),
    re.compile(r"рассказывать\s+чужую\s+сделку\s+поименно", re.I),
    re.compile(r"честно\s+про\s+формат", re.I),
    re.compile(r"последнее\s+ограничение.*проговор", re.I),
    re.compile(r"редакционн\w+\s+(?:casus|казус|сюжет)", re.I),
    re.compile(r"типовой\s+тюменск\w+\s+случа", re.I),
    re.compile(r"анонимиз", re.I),
    re.compile(r"composite\s+case", re.I),
    re.compile(r"modeled\s+composite", re.I),
)


def composite_disclaimer_hits(text: str) -> list[str]:
    """Return human-readable hit labels for banned meta-disclaimer phrases."""
    plain = re.sub(r"<[^>]+>", " ", text or "")
    plain = re.sub(r"\s+", " ", plain).strip()
    hits: list[str] = []
    for rx in COMPOSITE_DISCLAIMER_PATTERNS:
        m = rx.search(plain)
        if m:
            snippet = m.group(0).strip()
            if len(snippet) > 56:
                snippet = snippet[:53] + "..."
            hits.append(f"composite-disclaimer:{snippet}")
    return hits


def check_no_composite_disclaimer(html: str) -> tuple[bool, list[str]]:
    errors = composite_disclaimer_hits(html)
    return (not errors, errors)
