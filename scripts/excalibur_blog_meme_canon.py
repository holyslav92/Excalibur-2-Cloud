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
        if allowed and entry.get("id"):
            ids.add(str(entry["id"]))
    return ids


def _meme_lookup_key(raw: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(raw or "").strip().lower()).strip("_")


def build_meme_id_index(catalog: dict[str, Any]) -> dict[str, str]:
    """Map normalized id/alias keys → canonical catalog id."""
    index: dict[str, str] = {}
    for entry in catalog_entries(catalog):
        canonical = str(entry.get("id") or "").strip()
        if not canonical:
            continue
        index[_meme_lookup_key(canonical)] = canonical
        for alias in entry.get("aliases") or []:
            key = _meme_lookup_key(str(alias))
            if key:
                index[key] = canonical
    return index


def resolve_meme_id(raw: str, catalog: dict[str, Any]) -> str | None:
    """Resolve raw Derouter id via exact id or catalog alias; None if unknown."""
    value = str(raw or "").strip()
    if not value or not catalog:
        return None
    allowed = valid_meme_ids(catalog)
    if value in allowed:
        return value
    index = build_meme_id_index(catalog)
    return index.get(_meme_lookup_key(value))


def catalog_meme_id_roster(
    catalog: dict[str, Any],
    *,
    allowed_on: str | None = None,
) -> list[str]:
    """Sorted canonical ids for Derouter prompts / gate error hints."""
    roster: list[str] = []
    for entry in catalog_entries(catalog):
        canonical = str(entry.get("id") or "").strip()
        if not canonical:
            continue
        zones = entry.get("allowed_on") or []
        if allowed_on and allowed_on not in zones:
            continue
        roster.append(canonical)
    return sorted(set(roster))


def meme_category(catalog: dict[str, Any], meme_id: str) -> str:
    for entry in catalog_entries(catalog):
        if str(entry.get("id")) == meme_id:
            return str(entry.get("category") or "")
    return ""


def normalize_meme_picks(
    raw: Any,
    catalog: dict[str, Any] | None = None,
) -> dict[str, list[str]]:
    """Normalize cover-text / manifest meme_picks to slot → list of catalog ids."""
    if not isinstance(raw, dict):
        return {}
    if catalog is None:
        catalog = load_meme_catalog()
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
        resolved: list[str] = []
        for mid in ids:
            canonical = resolve_meme_id(mid, catalog) if catalog else mid
            if canonical:
                resolved.append(canonical)
            else:
                resolved.append(mid)
        if resolved:
            out[str(slot)] = resolved
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
                roster = catalog_meme_id_roster(catalog)
                hint = ", ".join(roster[:12])
                if len(roster) > 12:
                    hint += ", …"
                errors.append(
                    f"meme_pick {mid!r} not in meme-top100.json (real catalog only); "
                    f"valid ids include: {hint}"
                )
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
    return validate_meme_picks(picks, catalog, slot_allowed=allowed_slots)
