#!/usr/bin/env python3
"""Канон обложки: вся типографика только PIL, модель не пишет текст.

Почему live-обложки «кривые»:
1) i2i рисует свои стикеры/заголовок где попало;
2) wordstat overlay ставит левый край стикера на x≥0.68 и НЕ зажимает правый —
   фразы обрезаются, второй слой ложится на человека и на H1;
3) Cover-QA проверяет JSON-позиции, не пиксели.

Этот скрипт — единственный слой текста на cover.png:
- левая колонка (0–38%): заголовок + highlight, без стикеров;
- правый рейл (72–98%): 1–3 Wordstat + телефон, стикер целиком внутри кадра;
- мелкий sticky не на заголовке.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

TITLE_ZONE_RIGHT = 0.38
RAIL_LEFT = 0.72
RAIL_RIGHT = 0.98
PHONE_CTA = "+7 922 001 65 05"


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _font(size: int, bold: bool = True):
    from PIL import ImageFont

    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path("/usr/share/fonts/truetype/dejavu") / name
    try:
        return ImageFont.truetype(str(path), size)
    except OSError:
        return ImageFont.load_default()


def _fit_font(draw, text: str, max_w: int, start: int, *, bold: bool = True, min_size: int = 14):
    size = start
    while size >= min_size:
        font = _font(size, bold=bold)
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_w:
            return font, bbox[2] - bbox[0], bbox[3] - bbox[1]
        size -= 2
    font = _font(min_size, bold=bold)
    bbox = draw.textbbox((0, 0), text, font=font)
    return font, bbox[2] - bbox[0], bbox[3] - bbox[1]


def compose_cover_typography(
    cover_path: Path,
    *,
    hook: str,
    highlight: str,
    phone: str,
    stickers: list[str],
    sticky: str = "",
) -> dict[str, Any]:
    from PIL import Image, ImageDraw

    if not cover_path.is_file():
        return {"status": "FAIL", "reason": f"{cover_path} missing"}

    hook = (hook or "").strip()
    highlight = (highlight or "").strip()
    phone = (phone or PHONE_CTA).strip() or PHONE_CTA
    stickers = [s.strip() for s in stickers if s and any("\u0400" <= c <= "\u04FF" for c in s)][:3]
    sticky = (sticky or "").strip()[:32]

    img = Image.open(cover_path).convert("RGBA")
    w, h = img.size
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Карточка заголовка слева (не на всю высоту) + стикеры только сверху справа.
    # Полные колонки режут героя пополам, если он стоит справа.
    title_card = [int(w * 0.02), int(h * 0.04), int(w * 0.44), int(h * 0.64)]
    draw.rounded_rectangle(title_card, radius=18, fill=(255, 255, 255, 255))

    ink = (20, 24, 33, 255)
    gold = (196, 154, 74, 255)
    gold_fill = (220, 197, 161, 245)
    pad_x, pad_y = 12, 7

    # Заголовок: две строки, если highlight внутри hook — красим только его.
    title_max = int(w * 0.34)
    lines: list[tuple[str, tuple[int, int, int, int]]] = []
    if highlight and highlight.casefold() in hook.casefold():
        idx = hook.casefold().find(highlight.casefold())
        before = hook[:idx].strip()
        after = hook[idx + len(highlight) :].strip()
        if before:
            lines.append((before, ink))
        lines.append((highlight, gold))
        if after:
            lines.append((after, ink))
    else:
        lines.append((hook, ink))

    y = int(h * 0.11)
    x0 = int(w * 0.05)
    for text, color in lines:
        if not text:
            continue
        font, tw, th = _fit_font(draw, text, title_max, 64 if color == gold else 52)
        draw.text((x0, y), text, font=font, fill=color)
        y += th + 8

    if sticky:
        font, tw, th = _fit_font(draw, sticky, title_max, 22, bold=False)
        sy = int(h * 0.50)
        rect = [x0, sy, x0 + tw + pad_x * 2, sy + th + pad_y * 2]
        draw.rounded_rectangle(rect, radius=6, fill=(255, 224, 102, 245))
        draw.text((x0 + pad_x, sy + pad_y), sticky, font=font, fill=ink)

    rail_x = int(w * RAIL_LEFT)
    rail_r = int(w * RAIL_RIGHT)
    max_sticker_w = rail_r - rail_x
    positions: list[list[float]] = []
    n = max(len(stickers), 1)
    for i, phrase in enumerate(stickers):
        font, tw, th = _fit_font(draw, phrase, max_sticker_w - pad_x * 2, 22)
        y = int(h * (0.07 + i * 0.13))
        rect = [rail_x, y, min(rail_x + tw + pad_x * 2, w - 8), y + th + pad_y * 2]
        draw.rounded_rectangle(rect, radius=8, fill=gold_fill)
        draw.text((rail_x + pad_x, y + pad_y), phrase, font=font, fill=ink)
        positions.append([round(rail_x / w, 3), round(y / h, 3)])

    font, tw, th = _fit_font(draw, phone, max_sticker_w - pad_x * 2, 22)
    py = h - th - pad_y * 2 - 18
    draw.rectangle([rail_x - 6, py - 10, w, h], fill=(255, 255, 255, 255))
    prect = [rail_x, py, min(rail_x + tw + pad_x * 2, w - 8), py + th + pad_y * 2]
    draw.rounded_rectangle(prect, radius=8, fill=(20, 24, 33, 230))
    draw.text((rail_x + pad_x, py + pad_y), phone, font=font, fill=(255, 255, 255, 255))

    composed = Image.alpha_composite(img, overlay)
    composed.convert("RGB").save(cover_path, format="PNG")
    return {
        "status": "OK",
        "file": cover_path.name,
        "sticker_positions": positions,
        "title_zone_right": TITLE_ZONE_RIGHT,
        "rail_left": RAIL_LEFT,
        "typography": "pil_only",
    }


def apply_from_article(article_dir: Path) -> dict[str, Any]:
    import shutil

    cover_dir = article_dir / "cover"
    cover_path = cover_dir / "cover.png"
    raw = cover_dir / "cover-raw.png"
    if not raw.is_file():
        raw = cover_dir / "cover-raw-solo.png"
    if raw.is_file():
        shutil.copyfile(raw, cover_path)
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    text_path = article_dir / "cover" / "cover-text.json"
    hook = highlight = sticky = ""
    phone = PHONE_CTA
    stickers: list[str] = []
    manifest: dict[str, Any] = {}
    if text_path.is_file():
        data = load_json(text_path)
        hook = str(data.get("hook") or "")
        highlight = str(data.get("highlight") or "")
        sticky = str(data.get("sticky") or "")
        phone = str(data.get("phone_cta") or phone)
        stickers = list(data.get("wordstat_stickers") or [])
    if manifest_path.is_file():
        manifest = load_json(manifest_path)
        hook = hook or str(manifest.get("cover_hook") or "")
        highlight = highlight or str(manifest.get("cover_hook_highlight") or "")
        phone = str(manifest.get("cover_phone_cta") or phone)
        if not stickers:
            stickers = list(manifest.get("wordstat_stickers") or [])
        slot = (manifest.get("slots") or {}).get("cover") or {}
        sticky = sticky or str(slot.get("sticky") or "")
    report = compose_cover_typography(
        cover_path,
        hook=hook,
        highlight=highlight,
        phone=phone,
        stickers=stickers,
        sticky=sticky,
    )
    if report.get("status") == "OK" and manifest_path.is_file():
        manifest["wordstat_sticker_positions"] = report["sticker_positions"]
        manifest["wordstat_stickers_pil_applied"] = True
        manifest["cover_typography"] = "pil_only"
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    report = apply_from_article(article_dir)
    if report.get("status") != "OK":
        print(f"❌ COVER TYPOGRAPHY BLOCKER: {report}", file=sys.stderr)
        return 1
    print(
        f"OK cover typography pil_only stickers={len(report.get('sticker_positions') or [])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
