#!/usr/bin/env python3
"""Cover regen budget + short-hook canon helpers.

Hard cap on grsai solo cover attempts (default 2 full rounds, standard tier only).
Override: EXCALIBUR_COVER_MAX_ATTEMPTS env or CLI --max-attempts.
"""

from __future__ import annotations

import os
import re
from typing import Any

DEFAULT_COVER_MAX_ATTEMPTS = 2

# Слова hook: ONE line, B08-style, ~4–7 кириллических слов (цель 5–7); em dash OK.
SHORT_HOOK_MIN_WORDS = 4
SHORT_HOOK_TARGET_MIN_WORDS = 5
SHORT_HOOK_MAX_WORDS = 7
SHORT_HOOK_MAX_CHARS = 56
SHORT_HOOK_MIN_LONG_WORDS = 2  # слова ≥5 букв — лучше для OCR
CYRILLIC_WORD_RE = re.compile(r"[а-яА-ЯёЁ]+")


def resolve_cover_max_attempts(cli_value: int | None = None) -> int:
    """Бюджет полных попыток cover (каждая = standard tier only, без vip)."""
    if cli_value is not None and int(cli_value) > 0:
        return int(cli_value)
    env = os.environ.get("EXCALIBUR_COVER_MAX_ATTEMPTS", "").strip()
    if env.isdigit() and int(env) > 0:
        return int(env)
    return DEFAULT_COVER_MAX_ATTEMPTS


def split_hook_words(hook: str) -> list[str]:
    """Разбить hook на кириллические слова (тире/пробел — разделители)."""
    text = str(hook or "").replace("—", " ").replace("–", " ").replace("-", " ")
    return [w for w in CYRILLIC_WORD_RE.findall(text) if w]


def validate_short_hook(hook: str) -> dict[str, Any]:
    """Проверка short-hook canon для cover-text / manifest."""
    hook = str(hook or "").strip()
    words = split_hook_words(hook)
    long_words = [w for w in words if len(w) >= 5]
    errors: list[str] = []
    if not hook:
        errors.append("hook empty")
    elif "\n" in hook:
        errors.append("hook must be ONE line (no newlines)")
    word_count = len(words)
    if word_count < SHORT_HOOK_MIN_WORDS:
        errors.append(
            f"hook: {word_count} words, need {SHORT_HOOK_MIN_WORDS}-{SHORT_HOOK_MAX_WORDS} "
            "(short B08-style headline, not novel-length)"
        )
    elif word_count < SHORT_HOOK_TARGET_MIN_WORDS:
        # мягкое предупреждение — B09-style 4 слова допустимо, но 5–7 лучше для OCR
        pass
    elif word_count > SHORT_HOOK_MAX_WORDS:
        errors.append(
            f"hook: {word_count} words > {SHORT_HOOK_MAX_WORDS} — shorten for OCR on cover"
        )
    if len(hook) > SHORT_HOOK_MAX_CHARS:
        errors.append(f"hook: {len(hook)} chars > {SHORT_HOOK_MAX_CHARS}")
    if word_count >= SHORT_HOOK_MIN_WORDS and len(long_words) < SHORT_HOOK_MIN_LONG_WORDS:
        errors.append(
            f"hook: only {len(long_words)} word(s) ≥5 letters; prefer ≥{SHORT_HOOK_MIN_LONG_WORDS} "
            "for OCR readability"
        )
    return {
        "status": "PASS" if not errors else "BLOCK",
        "errors": errors,
        "word_count": word_count,
        "long_words": long_words,
    }


def short_hook_prompt_line() -> str:
    """Строка для solo/quad cover prompt builders."""
    return (
        f"Headline ONE line only: {SHORT_HOOK_TARGET_MIN_WORDS}–{SHORT_HOOK_MAX_WORDS} Russian words "
        f"(min {SHORT_HOOK_MIN_WORDS}, ≤{SHORT_HOOK_MAX_CHARS} chars), prefer words ≥5 letters for OCR; em dash OK; "
        "FORBIDDEN novel-length multi-line hooks."
    )
