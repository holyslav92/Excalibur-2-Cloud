#!/usr/bin/env python3
"""Emergency PIL cover compositor when image APIs are unavailable.

Rebuilds cover.png from the B06 designed-thumbnail template: preserves host face,
replaces hook/sticky/phone, clears forbidden Wordstat strips, re-stamps cat meme.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
B06_TEMPLATE = (
    ROOT
    / "memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami/cover/cover.png"
)
CAT_REF = ROOT / "tests/fixtures/cover-fail-zags-adbb30d1.png"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BLACK = (20, 24, 33)
WHITE = (255, 255, 253)
BG = (252, 252, 250)


def _font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD, size)


def _paste_cat(img: Image.Image) -> None:
    src = Image.open(CAT_REF).convert("RGB")
    sw, sh = src.size
    crop = src.crop((int(0.72 * sw), int(0.55 * sh), sw, sh))
    cat_w = 155
    cat_h = int(cat_w * crop.height / crop.width)
    cat = crop.resize((cat_w, cat_h), Image.Resampling.LANCZOS)
    w, h = img.size
    img.paste(cat, (int(w * 0.78), int(h * 0.64)))


def compose_from_template(
    *,
    hook_lines: list[str],
    sticky: str,
    phone: str,
    template: Path = B06_TEMPLATE,
) -> Image.Image:
    if not template.is_file():
        raise FileNotFoundError(f"cover template missing: {template}")
    img = Image.open(template).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    # Owner ban: Wordstat query strips top-left
    draw.rectangle((0, 0, int(w * 0.42), int(h * 0.22)), fill=BG)
    # Sacred title zone
    draw.rectangle((int(w * 0.50), int(h * 0.08), int(w * 0.98), int(h * 0.42)), fill=WHITE)
    # Phone CTA — узко, чтобы не срезать cat meme
    draw.rectangle((int(w * 0.56), int(h * 0.74), int(w * 0.96), int(h * 0.90)), fill=(255, 255, 255))

    font_s = _font(22)
    pad = 14
    tw = int(draw.textlength(sticky, font=font_s))
    sx, sy = int(w * 0.54), int(h * 0.12)
    draw.rectangle((sx, sy, sx + tw + pad * 2, sy + 52), fill=(255, 220, 120), outline=(210, 180, 90))
    draw.text((sx + pad, sy + 12), sticky, fill=BLACK, font=font_s)

    size = 50
    font = _font(size)
    y = int(h * 0.18)
    for line in hook_lines:
        draw.text((int(w * 0.54), y), line, fill=BLACK, font=font)
        y += size + 8

    font_p = _font(28)
    px, py = int(w * 0.58), int(h * 0.77)
    tw = int(draw.textlength(phone, font=font_p))
    draw.rectangle((px, py, px + tw + 32, py + 52), fill=(255, 255, 255), outline=(210, 205, 195))
    draw.text((px + 16, py + 10), phone, fill=BLACK, font=font_p)
    _paste_cat(img)
    return img


def hook_to_lines(hook: str) -> list[str]:
    if "—" in hook:
        parts = [p.strip() for p in hook.split("—", 1)]
        return parts if len(parts) == 2 else [hook]
    mid = len(hook) // 2
    sp = hook.rfind(" ", 0, mid + 12)
    return [hook[:sp].strip(), hook[sp:].strip()] if sp > 0 else [hook]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--template", type=Path, default=B06_TEMPLATE)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = ROOT / article_dir
    cover_text = json.loads((article_dir / "cover" / "cover-text.json").read_text(encoding="utf-8"))
    hook = str(cover_text.get("hook") or "")
    sticky = str(cover_text.get("sticky") or "")
    phone = str(cover_text.get("phone_cta") or "+7 922 001 65 05")
    lines = hook_to_lines(hook)
    img = compose_from_template(hook_lines=lines, sticky=sticky, phone=phone, template=args.template)
    out = article_dir / "cover" / "cover.png"
    if args.dry_run:
        print(json.dumps({"out": str(out), "lines": lines}, ensure_ascii=False))
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, format="PNG", optimize=True)
    print(f"OK composed {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
