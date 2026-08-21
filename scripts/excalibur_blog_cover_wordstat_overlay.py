#!/usr/bin/env python3
"""PIL overlay: 1–3 Wordstat phrases as paper investigation-board stickers.

Pretty stickers (tape, rounded paper, slight rotation, shadow) — NOT opaque bars.
Sacred zones: title left-top, meme top-right. Full phrase text, never truncated.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Any

# Нормализованные зоны без стикеров
TITLE_ZONE = (0.0, 0.0, 0.62, 0.38)
MEME_ZONE = (0.82, 0.0, 1.0, 0.20)
PHONE_ZONE = (0.55, 0.72, 1.0, 1.0)
TOPLEFT_WORDSTAT_ZONE = (0.02, 0.04, 0.40, 0.36)

# Wordstat stickers — только top-left sacred free zone (не title, не meme, не phone)
DEFAULT_POSITIONS = (
    (0.10, 0.06),
    (0.12, 0.17),
    (0.14, 0.28),
    (0.16, 0.38),
)


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


def _zone_overlap(
    x: float, y: float, w_frac: float, h_frac: float, zone: tuple[float, float, float, float]
) -> bool:
    zx0, zy0, zx1, zy1 = zone
    x1 = x + w_frac
    y1 = y + h_frac
    return not (x1 <= zx0 or x >= zx1 or y1 <= zy0 or y >= zy1)


def _load_fonts(size: int):
    from PIL import ImageFont

    try:
        bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        regular = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", max(size - 2, 10))
    except OSError:
        bold = ImageFont.load_default()
        regular = bold
    return bold, regular


def _wrap_phrase(phrase: str, font, draw, max_width: int) -> list[str]:
    words = phrase.split()
    if not words:
        return [phrase]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        trial = f"{current} {word}"
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines[:3]


def _draw_paper_sticker(
    base_rgba,
    *,
    text: str,
    anchor_x: int,
    anchor_y: int,
    max_width: int,
    rotation_deg: float,
    seed: int,
) -> tuple[Any, dict[str, Any]]:
    """Нарисовать один бумажный стикер; вернуть overlay layer + metadata."""
    from PIL import Image, ImageDraw, ImageFilter

    rng = random.Random(seed)
    pad_x, pad_y = 16, 12
    font_size = 26
    bold, regular = _load_fonts(font_size)

    # Подобрать размер шрифта под полную фразу
    for _ in range(8):
        bold, regular = _load_fonts(font_size)
        probe = ImageDraw.Draw(Image.new("RGBA", (max_width + 200, 200)))
        lines = _wrap_phrase(text, regular, probe, max_width - pad_x * 2)
        line_heights = []
        line_widths = []
        for line in lines:
            bbox = probe.textbbox((0, 0), line, font=regular)
            line_widths.append(bbox[2] - bbox[0])
            line_heights.append(bbox[3] - bbox[1])
        sticker_w = min(max(line_widths) + pad_x * 2, max_width)
        sticker_h = sum(line_heights) + pad_y * 2 + max(0, len(lines) - 1) * 4
        if sticker_w <= max_width and sticker_h <= int(base_rgba.size[1] * 0.22):
            break
        font_size = max(14, font_size - 2)

    sticker = Image.new("RGBA", (sticker_w + 40, sticker_h + 40), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sticker)
    paper = (252, 248, 238, 245)
    shadow = (40, 36, 30, 70)
    ink = (22, 26, 34, 255)
    tape = (220, 197, 161, 210)

    # Тень
    sdraw.rounded_rectangle(
        [22, 24, 22 + sticker_w + 4, 24 + sticker_h + 4],
        radius=14,
        fill=shadow,
    )
    # Бумага
    sdraw.rounded_rectangle(
        [18, 18, 18 + sticker_w, 18 + sticker_h],
        radius=12,
        fill=paper,
        outline=(200, 185, 155, 255),
        width=2,
    )
    # Скотч
    tape_w = min(sticker_w // 3, 72)
    sdraw.rectangle([24, 10, 24 + tape_w, 24], fill=tape)
    sdraw.rectangle([18 + sticker_w - tape_w - 8, 10, 18 + sticker_w - 8, 24], fill=tape)

    y_text = 18 + pad_y
    for line in lines:
        sdraw.text((18 + pad_x, y_text), line, font=regular, fill=ink)
        bbox = sdraw.textbbox((0, 0), line, font=regular)
        y_text += (bbox[3] - bbox[1]) + 4

    rotated = sticker.rotate(rotation_deg, expand=True, resample=Image.Resampling.BICUBIC)
    rotated = rotated.filter(ImageFilter.GaussianBlur(radius=0.3))

    overlay = Image.new("RGBA", base_rgba.size, (0, 0, 0, 0))
    paste_x = anchor_x - rotated.size[0] // 2
    paste_y = anchor_y - rotated.size[1] // 2
    overlay.paste(rotated, (paste_x, paste_y), rotated)

    meta = {
        "text": text,
        "lines": lines,
        "font_size": font_size,
        "rotation_deg": rotation_deg,
        "anchor": [anchor_x, anchor_y],
        "size": [sticker_w, sticker_h],
    }
    return overlay, meta


def _is_paper_pixel(r: int, g: int, b: int) -> bool:
    lum = (r + g + b) / 3.0
    if lum < 210:
        return False
    if max(r, g, b) - min(r, g, b) > 48:
        return False
    return r > 228 and g > 222 and b > 205


def _erase_paper_stickers_in_zone(base_rgba, zone: tuple[float, float, float, float]) -> int:
    """Стереть только paper Wordstat strips в зоне; не трогать лицо/title/phone/meme."""
    from collections import deque

    w, h = base_rgba.size
    rgb = base_rgba.convert("RGB")
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = int(zone[2] * w)
    y1 = int(zone[3] * h)
    board_samples: list[tuple[int, int, int]] = []
    for y in range(y0, min(y1 + 20, h)):
        for x in range(x0, min(x1 + 30, w)):
            r, g, b = rgb.getpixel((x, y))
            if not _is_paper_pixel(r, g, b):
                board_samples.append((r, g, b))
    if board_samples:
        fill = (
            sum(c[0] for c in board_samples) // len(board_samples),
            sum(c[1] for c in board_samples) // len(board_samples),
            sum(c[2] for c in board_samples) // len(board_samples),
        )
    else:
        fill = (248, 246, 240)

    visited = [[False] * (x1 - x0) for _ in range(y1 - y0)]
    erased = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            lx, ly = x - x0, y - y0
            if visited[ly][lx]:
                continue
            r, g, b = rgb.getpixel((x, y))
            if not _is_paper_pixel(r, g, b):
                continue
            q: deque[tuple[int, int]] = deque([(lx, ly)])
            visited[ly][lx] = True
            pixels = 0
            minx = maxx = lx
            miny = maxy = ly
            while q:
                cx, cy = q.popleft()
                pixels += 1
                minx, maxx = min(minx, cx), max(maxx, cx)
                miny, maxy = min(miny, cy), max(maxy, cy)
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = cx + dx, cy + dy
                    if nx < 0 or ny < 0 or nx >= x1 - x0 or ny >= y1 - y0 or visited[ny][nx]:
                        continue
                    px, py = x0 + nx, y0 + ny
                    pr, pg, pb = rgb.getpixel((px, py))
                    if _is_paper_pixel(pr, pg, pb):
                        visited[ny][nx] = True
                        q.append((nx, ny))
            bw, bh = maxx - minx + 1, maxy - miny + 1
            if pixels < 280 or bw < 60 or bh < 8:
                continue
            pad = 6
            ex0 = max(0, x0 + minx - pad)
            ey0 = max(0, y0 + miny - pad)
            ex1 = min(w, x0 + maxx + pad + 1)
            ey1 = min(h, y0 + maxy + pad + 1)
            for ey in range(ey0, ey1):
                for ex in range(ex0, ex1):
                    rgb.putpixel((ex, ey), fill)
            erased += 1
    base_rgba.paste(rgb)
    return erased


def repack_wordstat_stickers(cover_path: Path, phrases: list[str]) -> dict[str, Any]:
    """PIL-only: erase top-left paper strips on current cover, redraw spaced stickers."""
    try:
        from PIL import Image
    except ImportError:
        return {"status": "SKIP", "reason": "Pillow not installed"}
    if not cover_path.is_file():
        return {"status": "SKIP", "reason": f"{cover_path} missing"}
    img = Image.open(cover_path).convert("RGBA")
    erased = _erase_paper_stickers_in_zone(img, TOPLEFT_WORDSTAT_ZONE)
    img.convert("RGB").save(cover_path, format="PNG")
    report = stamp_wordstat_stickers(
        cover_path,
        phrases,
        force=True,
        sticker_positions=None,
        style="paper",
    )
    report["erased_components"] = erased
    report["mode"] = "repack_only"
    return report


def stamp_wordstat_stickers(
    cover_path: Path,
    phrases: list[str],
    *,
    force: bool = False,
    sticker_positions: list[Any] | None = None,
    style: str = "paper",
) -> dict[str, Any]:
    """Наложить 1–3 бумажных стикера Wordstat. Возвращает отчёт."""
    try:
        from PIL import Image
    except ImportError:
        return {"status": "SKIP", "reason": "Pillow not installed"}

    if not cover_path.is_file():
        return {"status": "SKIP", "reason": f"{cover_path} missing"}

    clean = [p.strip() for p in phrases if p.strip() and _has_cyrillic(p.strip())][:4]
    if not clean:
        return {"status": "SKIP", "reason": "no valid Cyrillic wordstat_stickers"}

    img = Image.open(cover_path).convert("RGBA")
    w, h = img.size
    max_sticker_w = int(w * 0.26)
    margin = 14

    if isinstance(sticker_positions, list) and sticker_positions:
        anchors = [
            (int(float(p[0]) * w), int(float(p[1]) * h))
            for p in sticker_positions[: len(clean)]
            if isinstance(p, (list, tuple)) and len(p) >= 2
        ]
    else:
        anchors = [(int(w * px), int(h * py)) for px, py in DEFAULT_POSITIONS[: len(clean)]]

    # Сдвинуть якоря только внутрь top-left sacred zone
    safe_anchors: list[tuple[int, int]] = []
    for idx, (ax, ay) in enumerate(anchors):
        xf = ax / w
        yf = ay / h
        if _zone_overlap(xf, yf, 0.24, 0.12, TITLE_ZONE):
            xf = 0.12 + (idx % 2) * 0.04
            yf = 0.10 + idx * 0.10
        if _zone_overlap(xf, yf, 0.20, 0.14, MEME_ZONE):
            xf = 0.14 + idx * 0.02
            yf = 0.12 + idx * 0.08
        if _zone_overlap(xf, yf, 0.24, 0.10, PHONE_ZONE) and yf > 0.78:
            xf = 0.16
            yf = 0.22 + idx * 0.08
        # clamp to top-left only
        xf = max(TOPLEFT_WORDSTAT_ZONE[0], min(xf, TOPLEFT_WORDSTAT_ZONE[2] - 0.08))
        yf = max(TOPLEFT_WORDSTAT_ZONE[1], min(yf, TOPLEFT_WORDSTAT_ZONE[3] - 0.06))
        # Вертикальный шаг ≥11% canvas — без overlap после repack
        yf = max(yf, TOPLEFT_WORDSTAT_ZONE[1] + idx * 0.11)
        ax = max(margin, min(int(xf * w), int(w * TOPLEFT_WORDSTAT_ZONE[2]) - max_sticker_w - margin))
        ay = max(margin, min(int(yf * h), int(h * TOPLEFT_WORDSTAT_ZONE[3]) - int(h * 0.08)))
        safe_anchors.append((ax, ay))

    composed = img.copy()
    stamped: list[str] = []
    metas: list[dict[str, Any]] = []
    rotations = (-3.5, 2.0, -1.5, 3.0)

    for idx, phrase in enumerate(clean):
        if idx >= len(safe_anchors):
            break
        ax, ay = safe_anchors[idx]
        layer, meta = _draw_paper_sticker(
            composed,
            text=phrase,
            anchor_x=ax,
            anchor_y=ay,
            max_width=max_sticker_w,
            rotation_deg=rotations[idx % len(rotations)],
            seed=abs(hash(phrase)) % 10_000 + idx,
        )
        composed = Image.alpha_composite(composed, layer)
        stamped.append(phrase)
        metas.append(meta)

    if not stamped and not force:
        return {"status": "SKIP", "reason": "nothing to stamp"}

    composed.convert("RGB").save(cover_path, format="PNG")
    return {
        "status": "OK",
        "style": style,
        "stamped": stamped,
        "stickers": metas,
        "file": str(cover_path.name),
    }


def restore_cover_base(article_dir: Path) -> bool:
    """Восстановить cover.png из cover-quad-raw.png (до PIL bars), если есть."""
    from PIL import Image

    cover_dir = article_dir / "cover"
    raw = cover_dir / "cover-quad-raw.png"
    out = cover_dir / "cover.png"
    if not raw.is_file():
        return False
    img = Image.open(raw).convert("RGB")
    img = img.resize((1200, 675), Image.Resampling.LANCZOS)
    img.save(out, format="PNG")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--force", action="store_true", help="Stamp even if overlay already applied")
    ap.add_argument("--skip-if-present", action="store_true", help="Skip when manifest says stickers drawn")
    ap.add_argument(
        "--restore-base",
        action="store_true",
        help="Restore cover.png from cover-quad-raw.png before stamping",
    )
    ap.add_argument(
        "--top-left-only",
        action="store_true",
        help="Force Wordstat anchors in top-left sacred zone only",
    )
    ap.add_argument(
        "--repack-only",
        action="store_true",
        help="Erase top-left paper Wordstat strips on current cover.png and redraw spaced (no restore-base)",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path

    cover_path = article_dir / "cover" / "cover.png"
    if args.restore_base:
        if restore_cover_base(article_dir):
            print("OK restored cover base from cover-quad-raw.png")
        else:
            print("WARN no cover-quad-raw.png to restore", file=sys.stderr)

    if not manifest_path.is_file():
        print(f"WARN wordstat overlay: no manifest at {manifest_path}", file=sys.stderr)
        return 0

    manifest = load_json(manifest_path)
    if args.skip_if_present and manifest.get("wordstat_stickers_pil_applied") and not args.force:
        print("OK wordstat overlay skip (already applied)")
        return 0

    phrases = manifest.get("wordstat_stickers") or []
    if args.repack_only:
        report = repack_wordstat_stickers(cover_path, phrases)
    else:
        positions = None if args.top_left_only else manifest.get("wordstat_sticker_positions")
        report = stamp_wordstat_stickers(
            cover_path,
            phrases,
            force=args.force or args.top_left_only,
            sticker_positions=positions,
            style="paper",
        )
    if report["status"] == "OK":
        manifest["wordstat_stickers_pil_applied"] = True
        manifest["wordstat_overlay_style"] = "paper_sticker_v2"
        manifest["wordstat_sticker_positions"] = [
            [round(m["anchor"][0] / 1200, 3), round(m["anchor"][1] / 675, 3)]
            for m in report.get("stickers") or []
        ]
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"OK wordstat paper stickers: {', '.join(report['stamped'])}")
        return 0
    if report["status"] == "SKIP":
        print(f"OK wordstat overlay skip: {report.get('reason')}")
        return 0
    print(f"FAIL wordstat overlay: {report}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
