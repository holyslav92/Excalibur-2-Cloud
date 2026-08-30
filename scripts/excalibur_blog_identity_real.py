#!/usr/bin/env python3
"""Канонические live-фото владельца для i2i identity lock (The Риэлтор)."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

IDENTITY_REAL_DIR = Path("memory/cover/assets/identity-real")
VISUAL_INBOX_DIR = Path("memory/setup/visual-inbox")
SCENE_COMPOSITION_DIR = Path("memory/cover/assets/scene-composition-only")
FACE_STUDIO_UPLOAD_REL = "/wp-content/uploads/2026/06/2026-06-23-15.57.42.jpg"

# Единственный FACE source для /images/edits — студийный портрет.
FACE_PRIMARY: dict[str, str | bool] = {
    "id": "face_studio_2026",
    "file": "face-studio-2026-06-23.jpg",
    "role": "face_primary",
    "notes": "ONLY FACE i2i input. Studio portrait: jaw, stubble, hairline, dark-brown hair, warm eyes.",
    "do_not_clone_scene": True,
}

# Только телосложение (medium-slim), НЕ лицо.
BODY_BUILD_FILES: tuple[dict[str, str | bool], ...] = (
    {
        "id": "hoodie_airpods",
        "file": "face-hoodie-airpods.jpeg",
        "role": "body_build_only",
        "notes": "Body/build reference only — NOT FACE source.",
        "do_not_clone_scene": True,
    },
    {
        "id": "office_selfie",
        "file": "face-office-selfie.jpeg",
        "role": "body_build_only",
        "notes": "Body/build reference only — NOT FACE source.",
        "do_not_clone_scene": True,
    },
)

# Только композиция/сцена — никогда FACE.
NOT_FACE_SOURCE_FILES: tuple[dict[str, str | bool], ...] = (
    {
        "id": "greenhouse_yahweh",
        "file": "face-greenhouse-yahweh.png",
        "role": "scene_composition_only",
        "notes": "Scene mood only; never FACE source; do not clone greenhouse.",
        "do_not_clone_scene": True,
    },
    {
        "id": "immortal_regiment",
        "file": "face-immortal-regiment.jpeg",
        "role": "scene_composition_only",
        "notes": "Scene mood only; never FACE source; do not clone march/portrait.",
        "do_not_clone_scene": True,
    },
)

IDENTITY_REAL_FILES: tuple[dict[str, str | bool], ...] = (
    FACE_PRIMARY,
    *BODY_BUILD_FILES,
    *NOT_FACE_SOURCE_FILES,
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
    return [base / str(spec["file"]) for spec in IDENTITY_REAL_FILES]


def missing_identity_files(root: Path | None = None) -> list[str]:
    root = root or project_root()
    missing: list[str] = []
    for spec in IDENTITY_REAL_FILES:
        rel = IDENTITY_REAL_DIR / str(spec["file"])
        if not (root / rel).is_file():
            missing.append(str(rel))
    return missing


def pick_identity_reference(topic_id: str = "", slug: str = "") -> dict[str, str | bool]:
    """FACE i2i всегда только студийный портрет (без ротации по topic_id)."""
    _ = topic_id, slug
    return FACE_PRIMARY


def resolve_identity_reference_path(
    topic_id: str = "",
    slug: str = "",
    *,
    root: Path | None = None,
) -> Path:
    root = root or project_root()
    spec = pick_identity_reference(topic_id, slug)
    return root / IDENTITY_REAL_DIR / str(spec["file"])


def canonical_face_studio_url() -> str:
    """Публичный URL студийного портрета на WP (runtime, не коммитить live host в артефакты)."""
    from excalibur_blog_site_base import normalize_public_base, resolve_public_base_from_env

    base = normalize_public_base(resolve_public_base_from_env())
    if not base:
        raise RuntimeError(
            "PUBLIC_SITE_URL (or WP_HOME/WP_SITE_URL) required to fetch canonical face studio portrait"
        )
    return f"{base}{FACE_STUDIO_UPLOAD_REL}"


def ensure_identity_reference(root: Path | None = None) -> Path:
    """FACE i2i source must exist — download canonical studio portrait if missing (FAIL closed)."""
    root = root or project_root()
    path = resolve_identity_reference_path(root=root)
    if path.is_file() and path.stat().st_size > 1024:
        return path
    from asset_download import download_url_bytes

    source_url = canonical_face_studio_url()
    data, evidence = download_url_bytes(source_url, timeout=45, retries=4)
    if len(data) < 1024:
        raise RuntimeError(
            f"identity-real FACE download too small ({len(data)} bytes) from {source_url}"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    stamp = path.with_suffix(path.suffix + ".download.json")
    stamp.write_text(
        json.dumps(
            {
                "source_url": source_url,
                "bytes": len(data),
                "content_type": evidence.get("content_type"),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def stage_from_visual_inbox(root: Path | None = None) -> list[str]:
    """Копирует canonical identity files из visual-inbox → identity-real."""
    root = root or project_root()
    staged: list[str] = []
    dest_dir = root / IDENTITY_REAL_DIR
    inbox = root / VISUAL_INBOX_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)

    for spec in IDENTITY_REAL_FILES:
        name = str(spec["file"])
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
        "face_primary": str(IDENTITY_REAL_DIR / str(FACE_PRIMARY["file"])),
        "identity_files": [str(spec["file"]) for spec in IDENTITY_REAL_FILES],
        "body_build_only": [str(spec["file"]) for spec in BODY_BUILD_FILES],
        "not_face_source": [str(spec["file"]) for spec in NOT_FACE_SOURCE_FILES],
        "scene_composition_only_dir": str(SCENE_COMPOSITION_DIR),
        "scene_composition_only": list(SCENE_COMPOSITION_ONLY_FILES),
    }


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Identity-real staging and rotation helpers")
    ap.add_argument("--stage-from-inbox", action="store_true", help="Copy from visual-inbox")
    ap.add_argument("--check", action="store_true", help="Print missing identity-real files")
    ap.add_argument(
        "--ensure-face",
        action="store_true",
        help="Ensure studio face file exists (download canonical WP URL if missing)",
    )
    ap.add_argument("--pick", metavar="TOPIC_ID", help="Show face reference for topic")
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

    if args.ensure_face:
        try:
            path = ensure_identity_reference(root)
            print(f"OK face reference: {path.relative_to(root)} ({path.stat().st_size} bytes)")
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL ensure_identity_reference: {exc}", file=sys.stderr)
            return 1
        return 0

    if args.check:
        missing = missing_identity_files(root)
        face_path = resolve_identity_reference_path(root=root)
        if not face_path.is_file():
            missing.append(str(face_path.relative_to(root)))
        if missing:
            print("FAIL missing identity-real:")
            for path in missing:
                print(f"  {path}")
            return 1
        print("OK identity-real complete")
        return 0

    if args.pick:
        spec = pick_identity_reference(args.pick)
        rel = IDENTITY_REAL_DIR / str(spec["file"])
        print(json.dumps({"topic_id": args.pick, "reference": str(rel), "id": spec["id"]}, ensure_ascii=False))
        return 0

    if args.json:
        print(json.dumps(identity_lock_summary(), ensure_ascii=False, indent=2))
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
