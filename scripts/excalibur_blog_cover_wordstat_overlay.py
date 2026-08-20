#!/usr/bin/env python3
"""Совместимый вход: вызывает PIL-типографику обложки (pil_only).

Не штампует стикеры поверх текста модели. Канон:
``scripts/excalibur_blog_cover_typography.py``.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--skip-if-present", action="store_true")
    args = ap.parse_args()
    root = project_root()
    sys.path.insert(0, str(root / "scripts"))
    from excalibur_blog_cover_typography import apply_from_article

    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    if args.skip_if_present:
        import json

        man = article_dir / "cover" / "quad-manifest.json"
        if man.is_file():
            data = json.loads(man.read_text(encoding="utf-8"))
            if data.get("cover_typography") == "pil_only":
                print("OK wordstat overlay skip (pil_only already applied)")
                return 0
    report = apply_from_article(article_dir)
    if report.get("status") != "OK":
        print(f"FAIL wordstat overlay: {report}", file=sys.stderr)
        return 1
    print(
        "OK wordstat PIL overlay (pil_only layout): "
        + ", ".join(str(p) for p in (report.get("sticker_positions") or []))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
