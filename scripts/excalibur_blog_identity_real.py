#!/usr/bin/env python3
"""Канонические live-фото владельца для i2i identity lock (The Риэлтор)."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

IDENTITY_REAL_DIR = Path("memory/cover/assets/identity-real")
VISUAL_INBOX_DIR = Path("memory/setup/visual-inbox")
SCENE_COMPOSITION_DIR = Path("memory/cover/assets/scene-composition-only")

# Единственный source of truth для лица — четыре live-фото (не AI, не hero-ref).
IDENTITY_REAL_FILES: tuple[dict[str, str], ...] = (
    {
        "id": "hoodie_airpods",
        "file": "face-hoodie-airpods.jpeg",
        "role": "identity_lock_primary",
        "notes": "Лучший facial geometry lock: крупный план, родинки на подбородке/щеке.",
        "do_not_clone_scene": True,
    },
    {
        "id": "office_selfie",
        "file": "face-office-selfie.jpeg",
        "role": "identity_lock",
        "notes": "Круглое лицо, лёгкая щетина, ~28.",
        "do_not_clone_scene": True,
    },
    {
        "id": "greenhouse_yahweh",
        "file": "face-greenhouse-yahweh.png",
        "role": "identity_lock",
        "notes": "Full body, оранжерея — только likeness, не клонировать сцену.",
        "do_not_clone_scene": True,
    },
    {
        "id": "immortal_regiment",
        "file": "face-immortal-regiment.jpeg",
        "role": "identity_lock_face_only",
        "notes": "Только лицо; никогда не клонировать марш/портрет в руках.",
        "do_not_clone_scene": True,
    },
)

# AI-стилизованные кадры — только mood/композиция, НЕ лицо.
SCENE_COMPOSITION_ONLY_FILES: tuple[str, ...] = (
    "hero-ref-office-risk-hologram.jpg",
    "hero-ref-balcony-keys-sunset.jpg",
)


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def identity_paths(root: Path | None = None) -> list[Path]:
    base = (root or project_root()) / IDENTITY_REAL_DIR
    return [base / spec["file"] for spec in IDENTITY_REAL_FILES]


def missing_identity_files(root: Path | None = None) -> list[str]:
    root = root or project_root()
    missing: list[str] = []
    for spec in IDENTITY_REAL_FILES:
        rel = IDENTITY_REAL_DIR / spec["file"]
        if not (root / rel).is_file():
            missing.append(str(rel))
    return missing


def pick_identity_reference(topic_id: str = "", slug: str = "") -> dict[str, str]:
    """Ротация i2i reference по topic_id/slug (детерминированно)."""
    seed = (topic_id or slug or "default").strip() or "default"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    index = int(digest[:8], 16) % len(IDENTITY_REAL_FILES)
    return IDENTITY_REAL_FILES[index]


def resolve_identity_reference_path(
    topic_id: str = "",
    slug: str = "",
    *,
    root: Path | None = None,
) -> Path:
    root = root or project_root()
    spec = pick_identity_reference(topic_id, slug)
    return root / IDENTITY_REAL_DIR / spec["file"]


def stage_from_visual_inbox(root: Path | None = None) -> list[str]:
    """Копирует canonical identity files из visual-inbox → identity-real (+ обратно в inbox)."""
    root = root or project_root()
    staged: list[str] = []
    dest_dir = root / IDENTITY_REAL_DIR
    inbox = root / VISUAL_INBOX_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)

    for spec in IDENTITY_REAL_FILES:
        name = spec["file"]
        src = inbox / name
        if not src.is_file():
            continue
        dest = dest_dir / name
        shutil.copy2(src, dest)
        staged.append(str(dest.relative_to(root)))
    return staged


def identity_lock_summary() -> dict:
    return {
        "identity_real_dir": str(IDENTITY_REAL_DIR),
        "identity_files": [spec["file"] for spec in IDENTITY_REAL_FILES],
        "scene_composition_only_dir": str(SCENE_COMPOSITION_DIR),
        "scene_composition_only": list(SCENE_COMPOSITION_ONLY_FILES),
    }


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Identity-real staging and rotation helpers")
    ap.add_argument("--stage-from-inbox", action="store_true", help="Copy from visual-inbox")
    ap.add_argument("--check", action="store_true", help="Print missing identity-real files")
    ap.add_argument("--pick", metavar="TOPIC_ID", help="Show rotated reference for topic")
    ap.add_argument("--json", action="store_true", help="Emit JSON summary")
    args = ap.parse_args()

    root = project_root()
    if args.stage_from_inbox:
        staged = stage_from_visual_inbox(root)
        if staged:
            print("OK staged:")
            for path in staged:
                print(f"  {path}")
        else:
            print("WARN no identity files found in visual-inbox")
        return 0

    if args.check:
        missing = missing_identity_files(root)
        if missing:
            print("FAIL missing identity-real:")
            for path in missing:
                print(f"  {path}")
            return 1
        print("OK identity-real complete")
        return 0

    if args.pick:
        spec = pick_identity_reference(args.pick)
        rel = IDENTITY_REAL_DIR / spec["file"]
        print(json.dumps({"topic_id": args.pick, "reference": str(rel), "id": spec["id"]}, ensure_ascii=False))
        return 0

    if args.json:
        print(json.dumps(identity_lock_summary(), ensure_ascii=False, indent=2))
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
