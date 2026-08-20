#!/usr/bin/env python3
"""PIL overlay: stamp 1–3 Wordstat phrases on cover.png if model omitted them.

Does not replace the invented cover — adds readable sticker labels from
quad-manifest.json → wordstat_stickers (live Scout/Research pull).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _has_cyrillic(text: str) -> bool:
    return any("\u0400" <= ch <= "\u04FF" for ch in text)


def stamp_wordstat_stickers(
    cover_path: Path,
    phrases: list[str],
    *,
    force: bool = False,
) -> dict[str, Any]:
    """Наложить 1–3 стикера Wordstat на cover.png. Возвращает отчёт."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return {"status": "SKIP", "reason": "Pillow not installed"}

    if not cover_path.is_file():
        return {"status": "SKIP", "reason": f"{cover_path} missing"}

    clean = [p.strip() for p in phrases if p.strip() and _has_cyrillic(p.strip())][:3]
    if not clean:
        return {"status": "SKIP", "reason": "no valid Cyrillic wordstat_stickers"}

    img = Image.open(cover_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    w, h = img.size

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
        font_sm = font

    # Позиции: правый верх / правый центр / нижний правый — не перекрывают host слева.
    positions = [
        (int(w * 0.58), int(h * 0.08)),
        (int(w * 0.55), int(h * 0.38)),
        (int(w * 0.52), int(h * 0.72)),
    ]
    gold = (220, 197, 161, 235)
    ink = (20, 24, 33, 255)
    pad_x, pad_y = 14, 8

    stamped: list[str] = []
    for idx, phrase in enumerate(clean):
        if idx >= len(positions):
            break
        text = phrase[:48]
        fnt = font if len(text) <= 24 else font_sm
        bbox = draw.textbbox((0, 0), text, font=fnt)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x, y = positions[idx]
        rect = [x, y, x + tw + pad_x * 2, y + th + pad_y * 2]
        draw.rounded_rectangle(rect, radius=6, fill=gold)
        draw.text((x + pad_x, y + pad_y), text, font=fnt, fill=ink)
        stamped.append(text)

    if not stamped and not force:
        return {"status": "SKIP", "reason": "nothing to stamp"}

    composed = Image.alpha_composite(img, overlay)
    composed.convert("RGB").save(cover_path, format="PNG")
    return {"status": "OK", "stamped": stamped, "file": str(cover_path.name)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--force", action="store_true", help="Stamp even if overlay already applied")
    ap.add_argument("--skip-if-present", action="store_true", help="Skip when manifest says stickers drawn")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path

    cover_path = article_dir / "cover" / "cover.png"
    if not manifest_path.is_file():
        print(f"WARN wordstat overlay: no manifest at {manifest_path}", file=sys.stderr)
        return 0

    manifest = load_json(manifest_path)
    if args.skip_if_present and manifest.get("wordstat_stickers_pil_applied"):
        print("OK wordstat overlay skip (already applied)")
        return 0

    phrases = manifest.get("wordstat_stickers") or []
    report = stamp_wordstat_stickers(cover_path, phrases, force=args.force)
    if report["status"] == "OK":
        manifest["wordstat_stickers_pil_applied"] = True
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"OK wordstat PIL overlay: {', '.join(report['stamped'])}")
        return 0
    if report["status"] == "SKIP":
        print(f"OK wordstat overlay skip: {report.get('reason')}")
        return 0
    print(f"FAIL wordstat overlay: {report}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
