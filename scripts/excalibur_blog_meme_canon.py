#!/usr/bin/env python3
"""Meme canon — top-100 catalog, variety, sacred zones (docs + validators)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

MEME_CATALOG_REL = "memory/cover/meme-top100.json"
STICKER_MAX_SHARE = 0.15
SACRED_CLEARANCE_PX = 80


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
        if entry.get("id"):
            ids.add(str(entry["id"]))
    return ids


def _norm_meme_alias(value: str) -> str:
    return re.sub(r"[\s\-]+", "_", (value or "").strip().lower())


def build_meme_lookup(catalog: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    """Map catalog id → entry and normalized alias → canonical id (includes banned)."""
    by_id: dict[str, dict[str, Any]] = {}
    alias_to_id: dict[str, str] = {}
    for entry in catalog.get("entries") or []:
        if not isinstance(entry, dict):
            continue
        mid = str(entry.get("id") or "").strip()
        if not mid:
            continue
        by_id[mid] = entry
        keys = [mid, *list(entry.get("aliases") or [])]
        for key in keys:
            raw = str(key).strip()
            if not raw:
                continue
            alias_to_id[raw.lower()] = mid
            alias_to_id[_norm_meme_alias(raw)] = mid
    return by_id, alias_to_id


def resolve_meme_id(raw: str, catalog: dict[str, Any]) -> tuple[str | None, str | None]:
    """Resolve Derouter/manifest meme pick to canonical catalog id."""
    token = (raw or "").strip()
    if not token:
        return None, "meme_pick empty"

    by_id, alias_to_id = build_meme_lookup(catalog)
    canonical = alias_to_id.get(token.lower()) or alias_to_id.get(_norm_meme_alias(token))
    if not canonical and token in by_id:
        canonical = token
    if not canonical:
        return None, f"meme_pick {token!r} not in meme-top100.json (real catalog only)"

    entry = by_id[canonical]
    allowed = entry.get("allowed_on") or []
    if entry.get("category") == "banned" or not allowed:
        name = str(entry.get("name_ru") or canonical)
        return None, (
            f"meme_pick {token!r} is BANNED ({name}) — "
            "use allowed ids from meme-top100.json "
            "(e.g. roll_safe, hide_pain_harold, disaster_girl, this_is_fine_dog)"
        )
    return canonical, None


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
            canonical, resolve_err = resolve_meme_id(mid, catalog)
            if resolve_err:
                errors.append(resolve_err)
                continue
            assert canonical is not None
            if canonical not in allowed_ids:
                errors.append(f"meme_pick {mid!r} not in meme-top100.json (real catalog only)")
            cat = meme_category(catalog, canonical)
            if cat == "people":
                people += 1
            elif cat == "cat":
                cats += 1
            all_ids.append(canonical)

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
    return validate_meme_picks(picks, catalog, slot_allowed=allowed_slots)
