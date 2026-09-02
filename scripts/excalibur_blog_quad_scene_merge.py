#!/usr/bin/env python3
"""Merge cover/scene-draft.json (Derouter cover-scene) into quad-manifest.json."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def merge_scene_draft_into_manifest(manifest: dict[str, Any], scene: dict[str, Any]) -> dict[str, Any]:
    """Copy cover_motifs + slot prose from scene-draft without wiping scaffold fields."""
    if scene.get("cover_motifs"):
        manifest["cover_motifs"] = scene["cover_motifs"]
    if scene.get("cover_emotion"):
        manifest["cover_emotion"] = scene["cover_emotion"]
    if scene.get("wordstat_stickers") and not manifest.get("wordstat_stickers"):
        manifest["wordstat_stickers"] = scene["wordstat_stickers"]

    manifest_slots = manifest.setdefault("slots", {})
    for key, scene_slot in (scene.get("slots") or {}).items():
        if not isinstance(scene_slot, dict):
            continue
        slot = manifest_slots.setdefault(key, {})
        for field in ("scene_hint", "alt", "cover_emotion", "meme_picks", "labels"):
            val = scene_slot.get(field)
            if val and not slot.get(field):
                slot[field] = val
    return manifest


def cover_motifs_missing_fields(manifest: dict[str, Any]) -> list[str]:
    motifs = manifest.get("cover_motifs") or {}
    missing: list[str] = []
    for key in ("outfit", "action", "emotion", "pose_framing"):
        if not str(motifs.get(key) or "").strip():
            missing.append(f"cover_motifs.{key}")
    return missing


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
