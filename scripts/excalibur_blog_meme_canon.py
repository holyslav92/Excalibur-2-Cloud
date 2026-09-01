#!/usr/bin/env python3
"""Meme canon — top-100 catalog, variety, sacred zones (docs + validators)."""

from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

MEME_CATALOG_REL = "memory/cover/meme-top100.json"
STICKER_MAX_SHARE = 0.15
SACRED_CLEARANCE_PX = 80
# Owner ban: solo-cover default thinking-paw tabby recycled on 9368/9385/9398/B16.
BANNED_DEFAULT_MEME_IDS = frozenset({"thinking_cat"})
THINKING_CAT_TOKENS = (
    "thinking_cat",
    "thinking-cat",
    "thinking cat",
    "thinking-paw",
    "thinking paw",
    "paw on chin",
    "tabby thinking",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_meme_catalog(root: Path | None = None) -> dict[str, Any]:
    root = root or project_root()
    path = root / MEME_CATALOG_REL
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def catalog_entries(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        e
        for e in (catalog.get("entries") or [])
        if isinstance(e, dict) and e.get("category") != "banned"
    ]


def valid_meme_ids(catalog: dict[str, Any]) -> set[str]:
    ids: set[str] = set()
    for entry in catalog_entries(catalog):
        allowed = entry.get("allowed_on") or []
        if allowed and entry.get("id"):
            ids.add(str(entry["id"]))
    return ids


def meme_category(catalog: dict[str, Any], meme_id: str) -> str:
    for entry in catalog_entries(catalog):
        if str(entry.get("id")) == meme_id:
            return str(entry.get("category") or "")
    return ""


def normalize_meme_picks(raw: Any) -> dict[str, list[str]]:
    """Normalize cover-text / manifest meme_picks to slot → list of catalog ids."""
    if not isinstance(raw, dict):
        return {}
    out: dict[str, list[str]] = {}
    for slot, val in raw.items():
        ids: list[str] = []
        if isinstance(val, list):
            for item in val:
                if isinstance(item, str) and item.strip():
                    ids.append(item.strip())
                elif isinstance(item, dict) and str(item.get("id") or "").strip():
                    ids.append(str(item["id"]).strip())
        elif isinstance(val, dict) and str(val.get("id") or "").strip():
            ids.append(str(val["id"]).strip())
        elif isinstance(val, str) and val.strip():
            ids.append(val.strip())
        if ids:
            out[str(slot)] = ids
    return out


def validate_meme_picks(
    picks: dict[str, list[str]],
    catalog: dict[str, Any],
    *,
    slot_allowed: dict[str, set[str]] | None = None,
) -> list[str]:
    """Validate catalog ids, variety (not cats-only), optional per-slot allowlist."""
    errors: list[str] = []
    if not catalog:
        errors.append("meme catalog missing: memory/cover/meme-top100.json")
        return errors

    allowed_ids = valid_meme_ids(catalog)
    all_ids: list[str] = []
    people = 0
    cats = 0

    for slot, ids in picks.items():
        if slot_allowed and slot not in slot_allowed:
            errors.append(f"meme_picks slot {slot} not allowed for meme stickers")
        for mid in ids:
            if mid not in allowed_ids:
                errors.append(f"meme_pick {mid!r} not in meme-top100.json (real catalog only)")
            cat = meme_category(catalog, mid)
            if cat == "people":
                people += 1
            elif cat == "cat":
                cats += 1
            all_ids.append(mid)

    if all_ids and people == 0 and cats > 0:
        errors.append(
            "meme_variety FAIL: cats-only picks — include at least one people-meme "
            "from catalog (variety: people + cats, not cats-only)"
        )

    return errors


def validate_manifest_meme_canon(manifest: dict[str, Any], root: Path | None = None) -> list[str]:
    """Validate meme_picks on quad-manifest when present."""
    root = root or project_root()
    catalog = load_meme_catalog(root)
    picks = normalize_meme_picks(manifest.get("meme_picks"))
    if not picks:
        return []
    from excalibur_blog_quad_slots import MEME_ALLOWED_SLOTS

    allowed_slots = {k for k in MEME_ALLOWED_SLOTS}
    errors = validate_meme_picks(picks, catalog, slot_allowed=allowed_slots)
    errors.extend(check_banned_default_memes(picks))
    errors.extend(check_meme_anti_repeat(manifest, root))
    return errors


def _normalize_meme_token(value: str) -> str:
    return " ".join(str(value or "").casefold().split())


def meme_field_contains_thinking_cat(value: str) -> bool:
    norm = _normalize_meme_token(value)
    return any(tok in norm for tok in THINKING_CAT_TOKENS)


def check_banned_default_memes(picks: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    for slot, ids in picks.items():
        for mid in ids:
            if mid in BANNED_DEFAULT_MEME_IDS:
                errors.append(
                    f"meme_pick {mid!r} on {slot} is BANNED_DEFAULT_REPEAT "
                    "(thinking-paw tabby — pick people-meme or other catalog cat)"
                )
    return errors


def _parse_entry_date(raw: str) -> date | None:
    text = str(raw or "").strip()
    if not text:
        return None
    try:
        if "T" in text:
            return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def recent_used_meme_tokens(root: Path | None = None, *, window_days: int = 14) -> set[str]:
    root = root or project_root()
    log_path = root / "memory/cover/used-motifs.json"
    if not log_path.is_file():
        return set()
    data = json.loads(log_path.read_text(encoding="utf-8"))
    window = int(data.get("window_days") or window_days)
    today = date.today()
    cutoff = today - timedelta(days=window - 1)
    tokens: set[str] = set()
    for entry in data.get("entries") or []:
        entry_date = _parse_entry_date(str(entry.get("date") or ""))
        if entry_date is not None and entry_date < cutoff:
            continue
        motifs = entry.get("motifs") or {}
        meme = _normalize_meme_token(str(motifs.get("meme") or ""))
        if meme:
            tokens.add(meme)
        for mid in entry.get("meme_ids") or []:
            tokens.add(_normalize_meme_token(str(mid)))
    return tokens


def check_meme_anti_repeat(manifest: dict[str, Any], root: Path | None = None) -> list[str]:
    """FAIL if cover meme id/motif repeated within 14d window."""
    root = root or project_root()
    errors: list[str] = []
    topic_id = _normalize_meme_token(str(manifest.get("topic_id") or ""))
    motifs = manifest.get("cover_motifs") or {}
    meme_field = _normalize_meme_token(str(motifs.get("meme") or ""))
    picks = normalize_meme_picks(manifest.get("meme_picks"))
    cover_ids = picks.get("cover") or list(manifest.get("meme_picks") or []) if isinstance(manifest.get("meme_picks"), list) else []
    if not cover_ids and isinstance(manifest.get("meme_picks"), list):
        cover_ids = [str(x) for x in manifest.get("meme_picks") if str(x).strip()]

    recent = recent_used_meme_tokens(root)
    for mid in cover_ids:
        token = _normalize_meme_token(mid)
        if token and token in recent:
            errors.append(f"meme anti-repeat FAIL: {mid!r} used within 14d — pick fresh catalog meme")
        if mid in BANNED_DEFAULT_MEME_IDS:
            errors.append(f"meme anti-repeat FAIL: {mid!r} is banned default sticker")
    if meme_field and meme_field in recent:
        errors.append(f"meme anti-repeat FAIL: cover_motifs.meme repeats within 14d ({meme_field!r})")
    if meme_field_contains_thinking_cat(meme_field):
        errors.append("meme BANNED: cover_motifs.meme references thinking_cat / thinking-paw tabby")
    return errors


def format_solo_cover_meme_line(manifest: dict[str, Any], catalog: dict[str, Any] | None = None) -> str:
    """Meme sticker line for solo cover — from manifest meme_picks, never thinking-cat default."""
    catalog = catalog or load_meme_catalog()
    picks = normalize_meme_picks(manifest.get("meme_picks"))
    cover_ids = picks.get("cover")
    if not cover_ids:
        slot = (manifest.get("slots") or {}).get("cover") or {}
        cover_ids = picks.get("cover") or (slot.get("meme_picks") if isinstance(slot.get("meme_picks"), list) else [])
    if not cover_ids and isinstance(manifest.get("meme_picks"), list):
        cover_ids = [str(x) for x in manifest.get("meme_picks") if str(x).strip()]

    labels: list[str] = []
    for mid in cover_ids or []:
        if mid in BANNED_DEFAULT_MEME_IDS:
            continue
        name = mid
        for entry in catalog_entries(catalog):
            if str(entry.get("id")) == mid:
                name = str(entry.get("name_ru") or mid)
                break
        labels.append(f"{name} ({mid})")

    if not labels:
        return (
            "Meme stickers: pick 1–2 tiny PEOPLE reaction memes from meme-top100 catalog only "
            "(≤12% frame, corner accent, ≥80px from hook/face/phone). "
            "FORBIDDEN: thinking_cat / thinking-paw tabby / orange tabby paw-on-chin default."
        )

    joined = "; ".join(labels[:2])
    return (
        f"Meme stickers (tiny ≤12% frame, corner accent, ≥80px from hook/face/phone): {joined}. "
        "Real catalog cutouts only — NOT thinking_cat / thinking-paw tabby. "
        "Never on host face, hook title, or phone CTA."
    )
