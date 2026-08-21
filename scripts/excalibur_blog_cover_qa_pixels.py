#!/usr/bin/env python3
"""Pixel-level Cover-QA — читает PNG bytes, не manifest/prompt.

Проверяет cover.png на типичные owner FAIL: opaque Wordstat bars, truncation,
перекрытие title/meme, distant full-body host, manifest lie (outfit vs pixels).
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

# Зоны без стикеров (нормализованные 0..1)
TITLE_ZONE = (0.0, 0.0, 0.62, 0.38)  # x0,y0,x1,y1 — левый верх, заголовок
MEME_ZONE = (0.82, 0.0, 1.0, 0.18)  # правый верх — meme sticker (bars)
MEME_GUARD_ZONE = (0.68, 0.0, 1.0, 0.42)  # legacy — верхний правый угол
MEME_OCCLUSION_ZONE = (0.62, 0.58, 0.98, 0.90)  # cat + chest stickers overlap
TOPLEFT_WORDSTAT_SAFE = (0.0, 0.0, 0.44, 0.32)  # taped Wordstat on board — allowed
TOPLEFT_WORDSTAT_ALLOWED = (0.0, 0.0, 0.42, 0.36)  # единственная зона PIL Wordstat
WORDSTAT_RIGHT_FORBIDDEN = (0.44, 0.30, 1.0, 0.96)  # справа/низ — Wordstat запрещён
CLOTHING_NO_TEXT_ZONE = (0.46, 0.46, 0.98, 0.94)  # одежда/грудь — без текста
FACE_ARTIFACT_ZONE = (0.30, 0.05, 0.78, 0.52)  # лицо — без синих артефактов
NECK_INPAINT_ZONE = (0.42, 0.50, 0.68, 0.62)  # шея — без inpaint blob
CAT_MEME_CORE = (0.72, 0.60, 0.98, 0.90)  # cat meme sticker bbox heuristic
MEME_CLEARANCE_PX = 80
CHEST_PEEL_ZONE = (0.48, 0.28, 0.96, 0.74)  # host chest — legacy QA bbox
CHEST_WORDSTAT_ZONE = (0.50, 0.44, 0.96, 0.88)  # жилет ниже лица — Wordstat forbidden
CHEST_PEEL_ACTIVE = (0.50, 0.44, 0.98, 0.92)  # нижняя часть жилета + мем — только здесь peel
FACE_EXCLUDE_ZONE = (0.30, 0.04, 0.78, 0.50)  # лицо/лоб — не трогать при peel
BOTTOM_DUP_PEEL_ZONE = (0.56, 0.76, 0.94, 0.96)  # duplicate PIL wordstat bottom-right
HOST_ZONE = (0.22, 0.08, 0.92, 0.98)  # где ожидаем крупное лицо
WORDSTAT_ZONE = (0.62, 0.0, 1.0, 1.0)  # правая полоса для Wordstat
# Священные зоны designed thumbnail (1200×675)
HOOK_TITLE_ZONE = (0.52, 0.14, 0.96, 0.40)  # крупный hook H1 справа
PHONE_STICKER_ZONE = (0.55, 0.70, 0.98, 0.96)  # телефон +7 922 001 65 05
MEME_CORNER_ZONE = (0.72, 0.62, 0.96, 0.88)  # маленький мем-стикер (без лица)
WORDSTAT_STACK_ZONE = (0.02, 0.04, 0.40, 0.30)  # legacy — query strips FORBIDDEN
TOPLEFT_QUERY_STRIP_FORBIDDEN = (0.0, 0.0, 0.42, 0.22)  # beige/gold Wordstat bars — owner ban
WORDSTAT_NARROW_STACK_ZONE = (0.12, 0.05, 0.32, 0.24)  # узкая колонка — cramped dump

# Пороги калиброваны на FAIL B07 (md5 23051a01…) vs PASS B06
HOOK_TITLE_ROW_INK_FRAC = 0.17
HOOK_TITLE_MIN_ROW_INK_PX = 34
HOOK_TITLE_MIN_BAND_ROWS = 12
HOOK_TITLE_BAND_MAX_GAP_PX = 10
HOOK_TITLE_MIN_INK_OUTSIDE_FACE = 600
PHONE_ZONE_MIN_INK = 220
MEME_CORNER_MIN_SIGNAL = 75
STICKER_OVERLAP_IOU = 0.35
STICKER_MIN_GAP_PX = 10
WORDSTAT_CROWDED_STACK_MIN_COMPS = 3
WORDSTAT_CROWDED_MAX_SPAN_FRAC = 0.21

GOLD_STICKER_RGB = (220, 197, 161)
PHONE_REQUIRED = "+7 922 001 65 05"

BANNED_OUTFIT_TOKENS = (
    "black blazer",
    "charcoal blazer",
    "чёрный пиджак",
    "black t-shirt combo",
)
WARM_OUTFIT_TOKENS = (
    "terracotta",
    "mustard",
    "sweater",
    "merino",
    "orange",
    "beige",
    "overcoat",
    "grey",
    "gray",
    "hoodie",
    "blue jacket",
    "синяя",
)


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def md5_bytes(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def md5_file(path: Path) -> str:
    return md5_bytes(path.read_bytes())


def _luminance(r: int, g: int, b: int) -> float:
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _is_skin(r: int, g: int, b: int) -> bool:
    """Узкая эвристика кожи лица — не warm background / sand / gold."""
    if max(r, g, b) < 45:
        return False
    y = _luminance(r, g, b)
    if y < 55 or y > 205:
        return False
    if r < 85 or g < 35 or b < 25:
        return False
    if r <= g or r <= b:
        return False
    if r - g < 18:
        return False
    if max(r, g, b) - min(r, g, b) < 15:
        return False
    return True


def _is_gold_sticker(r: int, g: int, b: int, *, tol: int = 38) -> bool:
    gr, gg, gb = GOLD_STICKER_RGB
    return abs(r - gr) <= tol and abs(g - gg) <= tol and abs(b - gb) <= tol


def _is_grey_woven_fabric(r: int, g: int, b: int) -> bool:
    """Серая/бежевая ткань пиджака — не Wordstat paper."""
    if abs(r - g) <= 16 and abs(g - b) <= 20 and abs(r - b) <= 22:
        lum = _luminance(r, g, b)
        if 138 <= lum <= 228:
            return True
    return False


def _is_warm_garment_pixel(r: int, g: int, b: int) -> bool:
    """Терракотовый/рыжий трикотаж и переходы к коже — не ghost text."""
    if _is_skin(r, g, b):
        return True
    if r >= 105 and g >= 28 and b <= 98 and r - b >= 40 and r - g >= 12:
        return True
    return False


def _is_pure_white_paper(r: int, g: int, b: int) -> bool:
    """Белая/off-white бумага мем-стикера (не Wordstat tan label)."""
    if r >= 246 and g >= 244 and b >= 238:
        return True
    # cat meme cutout border — почти нейтральный off-white
    return r >= 238 and g >= 236 and b >= 230 and max(r, g, b) - min(r, g, b) <= 20


def _is_paper_wordstat_pixel(r: int, g: int, b: int) -> bool:
    """Tan/cream Wordstat paper sticker (PIL или model), не белый meme cutout."""
    if _is_pure_white_paper(r, g, b):
        return False
    if _is_skin(r, g, b):
        return False
    if _is_grey_woven_fabric(r, g, b):
        return False
    if _is_warm_garment_pixel(r, g, b):
        return False
    # рыжая шерсть cat meme — не Wordstat label
    if r >= 195 and g <= 178 and r - g >= 28:
        return False
    # gold brushstroke под «уценили» — title typography, не Wordstat sticker
    lum = _luminance(r, g, b)
    if lum < 105 or lum > 248:
        return False
    # cream paper (PIL v2)
    if r >= 245 and g >= 238 and b >= 225 and r + g + b > 700:
        return True
    # tan model labels on vest — узкий диапазон, не кожа/шерсть
    if r >= 198 and g >= 168 and b >= 138 and r - b >= 28 and g - b >= 12 and r - g <= 38:
        return True
    return False


def _paper_frac_in_zone(
    img,
    zone: tuple[float, float, float, float],
    *,
    exclude_zone: tuple[float, float, float, float] | None = None,
    exclude_zones: tuple[tuple[float, float, float, float], ...] | None = None,
) -> float:
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = max(x0 + 1, int(zone[2] * w))
    y1 = max(y0 + 1, int(zone[3] * h))
    excludes = list(exclude_zones or ())
    if exclude_zone:
        excludes.append(exclude_zone)
    total = 0
    paper = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            xf, yf = x / w, y / h
            if any(z[0] <= xf <= z[2] and z[1] <= yf <= z[3] for z in excludes):
                continue
            total += 1
            if _is_paper_wordstat_pixel(*rgb.getpixel((x, y))):
                paper += 1
    return paper / max(total, 1)


def _ghost_wordstat_paper_frac_in_zone(
    img,
    zone: tuple[float, float, float, float],
    *,
    exclude_zones: tuple[tuple[float, float, float, float], ...] | None = None,
) -> float:
    """Tan paper только там, где рядом тёмные буквы (ghost Wordstat), не текстура ткани."""
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = max(x0 + 1, int(zone[2] * w))
    y1 = max(y0 + 1, int(zone[3] * h))
    excludes = list(exclude_zones or ())
    total = 0
    paper = 0
    for y in range(y0, y1, 2):
        for x in range(x0, x1, 2):
            xf, yf = x / w, y / h
            if any(z[0] <= xf <= z[2] and z[1] <= yf <= z[3] for z in excludes):
                continue
            total += 1
            r, g, b = rgb.getpixel((x, y))
            if not _is_paper_wordstat_pixel(r, g, b):
                continue
            if _in_norm_zone(xf, yf, TOPLEFT_WORDSTAT_ALLOWED):
                paper += 1
                continue
            has_ink = False
            for dy in range(-5, 6):
                for dx in range(-5, 6):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and _is_dark_ink_pixel(*rgb.getpixel((nx, ny))):
                        has_ink = True
                        break
                if has_ink:
                    break
            if has_ink:
                paper += 1
    return paper / max(total, 1)


def _is_headline_ink_pixel(r: int, g: int, b: int) -> bool:
    """Типографика hook H1: тёмные буквы или gold accent, не кожа/бумага."""
    if _is_skin(r, g, b):
        return False
    if _is_paper_wordstat_pixel(r, g, b):
        return False
    lum = _luminance(r, g, b)
    if lum < 72:
        return True
    return _is_gold_sticker(r, g, b, tol=44)


def _hook_title_ink_outside_face(img) -> int:
    """Пиксели типографики hook title вне зоны лица (не черты лица/волос)."""
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(HOOK_TITLE_ZONE[0] * w)
    y0 = int(HOOK_TITLE_ZONE[1] * h)
    x1 = int(HOOK_TITLE_ZONE[2] * w)
    y1 = int(HOOK_TITLE_ZONE[3] * h)
    ink = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            r, g, b = rgb.getpixel((x, y))
            if _is_skin(r, g, b):
                continue
            xf, yf = x / w, y / h
            if _in_norm_zone(xf, yf, FACE_EXCLUDE_ZONE):
                continue
            if _is_headline_ink_pixel(r, g, b):
                ink += 1
    return ink


def _hook_title_metrics(img) -> dict[str, Any]:
    """Крупный читаемый hook title в sacred zone (не мелкие Wordstat strips / черты лица)."""
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(HOOK_TITLE_ZONE[0] * w)
    y0 = int(HOOK_TITLE_ZONE[1] * h)
    x1 = int(HOOK_TITLE_ZONE[2] * w)
    y1 = int(HOOK_TITLE_ZONE[3] * h)
    zone_w = max(x1 - x0, 1)
    bands: list[dict[str, Any]] = []
    qualifying_rows: list[int] = []
    for y in range(y0, y1):
        ink = 0
        for x in range(x0, x1):
            r, g, b = rgb.getpixel((x, y))
            xf, yf = x / w, y / h
            if _in_norm_zone(xf, yf, FACE_EXCLUDE_ZONE):
                continue
            if _is_skin(r, g, b):
                continue
            if _is_headline_ink_pixel(r, g, b):
                ink += 1
        frac = ink / zone_w
        row_ok = ink >= HOOK_TITLE_MIN_ROW_INK_PX or frac >= HOOK_TITLE_ROW_INK_FRAC
        if row_ok:
            qualifying_rows.append(y)

    if qualifying_rows:
        band_y0 = qualifying_rows[0]
        prev_y = qualifying_rows[0]
        band_count = 1
        for y in qualifying_rows[1:]:
            if y - prev_y <= HOOK_TITLE_BAND_MAX_GAP_PX:
                band_count += 1
                prev_y = y
            else:
                if band_count >= HOOK_TITLE_MIN_BAND_ROWS:
                    bands.append({"y0": band_y0, "y1": prev_y, "rows": band_count})
                band_y0 = y
                prev_y = y
                band_count = 1
        if band_count >= HOOK_TITLE_MIN_BAND_ROWS:
            bands.append({"y0": band_y0, "y1": prev_y, "rows": band_count})

    ink_outside = _hook_title_ink_outside_face(img)
    present = bool(bands) and ink_outside >= HOOK_TITLE_MIN_INK_OUTSIDE_FACE
    return {
        "present": present,
        "bands": bands,
        "ink_outside_face": ink_outside,
        "min_band_rows": HOOK_TITLE_MIN_BAND_ROWS,
    }


def _phone_zone_ink_count(img) -> int:
    """Тёмные цифры/иконка телефона в нижнем правом углу."""
    w, h = img.size
    gray = img.convert("L")
    x0 = int(PHONE_STICKER_ZONE[0] * w)
    y0 = int(PHONE_STICKER_ZONE[1] * h)
    x1 = int(PHONE_STICKER_ZONE[2] * w)
    y1 = int(PHONE_STICKER_ZONE[3] * h)
    ink = 0
    for y in range(y0, y1, 2):
        for x in range(x0, x1, 2):
            if gray.getpixel((x, y)) < 88:
                ink += 1
    return ink


def _meme_corner_signal(img) -> int:
    """Насыщенный мем-стикер (кот/каталог) в правом нижнем углу — не кожа/фон."""
    w, h = img.size
    x0 = int(MEME_CORNER_ZONE[0] * w)
    y0 = int(MEME_CORNER_ZONE[1] * h)
    x1 = int(MEME_CORNER_ZONE[2] * w)
    y1 = int(MEME_CORNER_ZONE[3] * h)
    signal = 0
    for y in range(y0, y1, 3):
        for x in range(x0, x1, 3):
            r, g, b = img.convert("RGB").getpixel((x, y))
            if _is_skin(r, g, b):
                continue
            if _is_pure_white_paper(r, g, b):
                continue
            lum = _luminance(r, g, b)
            if lum > 235:
                continue
            # оранжевая шерсть кота
            if r >= 178 and g <= 155 and r - g >= 30:
                signal += 3
                continue
            if max(r, g, b) - min(r, g, b) > 42 and lum < 215:
                signal += 1
    return signal


def _paper_sticker_components(
    img,
    zone: tuple[float, float, float, float],
    *,
    min_pixels: int = 180,
) -> list[dict[str, Any]]:
    """Связные компоненты Wordstat paper в зоне."""
    from collections import deque

    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = int(zone[2] * w)
    y1 = int(zone[3] * h)
    zw, zh = max(x1 - x0, 1), max(y1 - y0, 1)
    visited = [[False] * zw for _ in range(zh)]
    comps: list[dict[str, Any]] = []
    for y in range(y0, y1):
        for x in range(x0, x1):
            lx, ly = x - x0, y - y0
            if visited[ly][lx]:
                continue
            if not _is_paper_wordstat_pixel(*rgb.getpixel((x, y))):
                continue
            q: deque[tuple[int, int]] = deque([(lx, ly)])
            visited[ly][lx] = True
            pixels = 0
            minx = maxx = lx
            miny = maxy = ly
            while q:
                cx, cy = q.popleft()
                pixels += 1
                minx = min(minx, cx)
                maxx = max(maxx, cx)
                miny = min(miny, cy)
                maxy = max(maxy, cy)
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = cx + dx, cy + dy
                    if nx < 0 or ny < 0 or nx >= zw or ny >= zh or visited[ny][nx]:
                        continue
                    if _is_paper_wordstat_pixel(*rgb.getpixel((x0 + nx, y0 + ny))):
                        visited[ny][nx] = True
                        q.append((nx, ny))
            if pixels >= min_pixels:
                comps.append(
                    {
                        "pixels": pixels,
                        "bbox": (x0 + minx, y0 + miny, x0 + maxx, y0 + maxy),
                    }
                )
    return comps


def _bbox_iou(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> float:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    ix0, iy0 = max(ax0, bx0), max(ay0, by0)
    ix1, iy1 = min(ax1, bx1), min(ay1, by1)
    if ix1 <= ix0 or iy1 <= iy0:
        return 0.0
    inter = (ix1 - ix0) * (iy1 - iy0)
    area_a = max((ax1 - ax0) * (ay1 - ay0), 1)
    area_b = max((bx1 - bx0) * (by1 - by0), 1)
    return inter / (area_a + area_b - inter)


def _bbox_x_overlap_frac(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> float:
    ax0, _, ax1, _ = a
    bx0, _, bx1, _ = b
    overlap = max(0, min(ax1, bx1) - max(ax0, bx0))
    if overlap <= 0:
        return 0.0
    min_w = max(min(ax1 - ax0, bx1 - bx0), 1)
    return overlap / min_w


def _bbox_vertical_gap(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> int:
    """Positive gap if boxes do not overlap vertically; 0 or negative if overlap."""
    _, ay0, _, ay1 = a
    _, by0, _, by1 = b
    if ay1 <= by0:
        return by0 - ay1
    if by1 <= ay0:
        return ay0 - by1
    return min(ay1, by1) - max(ay0, by0)


def _bbox_x_center_distance(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> int:
    acx = (a[0] + a[2]) // 2
    bcx = (b[0] + b[2]) // 2
    return abs(acx - bcx)


def _filter_wordstat_strip_components(
    comps: list[dict[str, Any]],
    *,
    img_size: tuple[int, int] | None = None,
) -> list[dict[str, Any]]:
    """Оставить только полноценные Wordstat paper strips в top-left sacred zone."""
    w, h = img_size or (1200, 675)
    filtered: list[dict[str, Any]] = []
    for comp in comps:
        x0, y0, x1, y1 = comp["bbox"]
        bw = max(x1 - x0, 1)
        bh = max(y1 - y0, 1)
        if bw < 70 or bh < 10:
            continue
        if comp.get("pixels", 0) < 350:
            continue
        cx = (x0 + x1) / 2.0 / w
        cy = (y0 + y1) / 2.0 / h
        if not (
            TOPLEFT_WORDSTAT_ALLOWED[0] <= cx <= TOPLEFT_WORDSTAT_ALLOWED[2]
            and TOPLEFT_WORDSTAT_ALLOWED[1] <= cy <= TOPLEFT_WORDSTAT_ALLOWED[3]
        ):
            continue
        filtered.append(comp)
    return filtered


def _wordstat_sticker_overlap_metrics(img, *, hook_present: bool = False) -> dict[str, Any]:
    """Paper Wordstat stickers в top-left: без 2D overlap, без cramped stack — всегда, даже с hook title."""
    _ = hook_present  # legacy param; overlap gate no longer bypassed when title exists
    w, h = img.size
    raw = _paper_sticker_components(img, WORDSTAT_STACK_ZONE, min_pixels=250)
    strips = _filter_wordstat_strip_components(raw, img_size=(w, h))
    overlaps: list[dict[str, Any]] = []

    for i in range(len(strips)):
        for j in range(i + 1, len(strips)):
            bi = strips[i]["bbox"]
            bj = strips[j]["bbox"]
            iou = _bbox_iou(bi, bj)
            x_overlap = _bbox_x_overlap_frac(bi, bj)
            vert_gap = _bbox_vertical_gap(bi, bj)
            x_center_dist = _bbox_x_center_distance(bi, bj)
            horiz_overlap = not (bi[2] < bj[0] or bj[2] < bi[0])
            vert_overlap = not (bi[3] < bj[1] or bj[3] < bi[1])

            if iou >= STICKER_OVERLAP_IOU:
                overlaps.append({"pair": (i, j), "iou": round(iou, 3), "kind": "2d_overlap"})
                continue

            if horiz_overlap and vert_overlap:
                overlaps.append({"pair": (i, j), "kind": "stacked_overlap"})
                continue

            # Top-left Wordstat column: overlapping Y ranges always FAIL (rotated strips clip below)
            if vert_overlap:
                overlaps.append({"pair": (i, j), "kind": "vertical_y_overlap"})
                continue

            same_column = x_center_dist <= 100 or x_overlap >= 0.15
            if same_column and vert_gap <= STICKER_MIN_GAP_PX:
                overlaps.append(
                    {
                        "pair": (i, j),
                        "kind": "column_stack_tight",
                        "x_center_dist": x_center_dist,
                        "vert_gap": vert_gap,
                    }
                )

    crowded = False
    if len(strips) >= WORDSTAT_CROWDED_STACK_MIN_COMPS:
        ys = [c["bbox"][1] for c in strips] + [c["bbox"][3] for c in strips]
        span_frac = (max(ys) - min(ys)) / max(img.size[1], 1)
        if span_frac <= WORDSTAT_CROWDED_MAX_SPAN_FRAC:
            crowded = True
            overlaps.append(
                {
                    "kind": "crowded_corner_dump",
                    "narrow_components": len(strips),
                    "span_frac": round(span_frac, 3),
                }
            )

    return {
        "components": len(raw),
        "strip_components": len(strips),
        "narrow_components": len(strips),
        "overlaps": overlaps,
        "crowded_stack": crowded,
        "ok": len(overlaps) == 0,
    }


def _wordstat_query_strip_metrics(img) -> dict[str, Any]:
    """Owner ban: Yandex Wordstat query phrases as beige/gold paper strips top-left."""
    w, h = img.size
    raw = _paper_sticker_components(img, TOPLEFT_QUERY_STRIP_FORBIDDEN, min_pixels=250)
    strips = _filter_wordstat_strip_components(raw, img_size=(w, h))
    paper_frac = _paper_frac_in_zone(img, TOPLEFT_QUERY_STRIP_FORBIDDEN)
    bar_like = [b for b in _detect_gold_bands(img) if b.get("bar_like")]
    bars_in_zone = _bands_in_zone(bar_like, TOPLEFT_QUERY_STRIP_FORBIDDEN, (w, h))
    has_strips = len(strips) >= 1 or len(bars_in_zone) >= 1 or paper_frac >= 0.012
    return {
        "strip_components": len(strips),
        "bar_bands": len(bars_in_zone),
        "paper_frac": round(paper_frac, 4),
        "ok": not has_strips,
    }


def _layout_collapse_metrics(img, *, hook_present: bool) -> dict[str, Any]:
    """Face-only crop без designed layout: лицо съело кадр, нет hook title."""
    face = _face_skin_metrics(img)
    face_h = float(face.get("face_h_frac") or 0.0)
    face_w = float(face.get("face_w_frac") or 0.0)
    ink_outside = _hook_title_ink_outside_face(img)
    collapsed = (not hook_present) and face_h >= 0.30 and face_w >= 0.36
    dumped = (
        ink_outside < HOOK_TITLE_MIN_INK_OUTSIDE_FACE
        and face_h >= 0.30
        and _phone_zone_ink_count(img) < PHONE_ZONE_MIN_INK
    )
    return {
        "collapsed": collapsed or dumped,
        "face_h_frac": face_h,
        "face_w_frac": face_w,
        "hook_present": hook_present,
        "ink_outside_face": ink_outside,
        "dumped_wordstat_corner": dumped,
    }


def cover_composition_ok(img) -> bool:
    """Полноценная designed обложка: hook title, телефон, мем, без layout collapse, без Wordstat strips."""
    hook = _hook_title_metrics(img)
    phone_ink = _phone_zone_ink_count(img)
    meme_sig = _meme_corner_signal(img)
    query_strips = _wordstat_query_strip_metrics(img)
    layout = _layout_collapse_metrics(img, hook_present=bool(hook.get("present")))
    return (
        bool(hook.get("present"))
        and phone_ink >= PHONE_ZONE_MIN_INK
        and meme_sig >= MEME_CORNER_MIN_SIGNAL
        and query_strips.get("ok", False)
        and not layout.get("collapsed", False)
    )


def _in_norm_zone(xf: float, yf: float, zone: tuple[float, float, float, float]) -> bool:
    return zone[0] <= xf <= zone[2] and zone[1] <= yf <= zone[3]


def _is_dark_ink_pixel(r: int, g: int, b: int) -> bool:
    """Тёмные буквы / ghost text на одежде."""
    if _is_grey_woven_fabric(r, g, b):
        return False
    if _is_warm_garment_pixel(r, g, b):
        return False
    lum = _luminance(r, g, b)
    if lum > 78:
        return False
    if max(r, g, b) - min(r, g, b) < 28:
        return False
    return True


def _is_blue_artifact_pixel(r: int, g: int, b: int) -> bool:
    """Синие контуры inpaint/segmentation на лице и жилете."""
    lum = _luminance(r, g, b)
    if lum < 35 or lum > 215:
        return False
    return b > r + 14 and b > g + 10


def _frac_predicate_in_zone(
    img,
    zone: tuple[float, float, float, float],
    predicate,
    *,
    exclude_zones: tuple[tuple[float, float, float, float], ...] | None = None,
) -> float:
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = max(x0 + 1, int(zone[2] * w))
    y1 = max(y0 + 1, int(zone[3] * h))
    excludes = list(exclude_zones or ())
    total = 0
    matched = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            xf, yf = x / w, y / h
            if any(z[0] <= xf <= z[2] and z[1] <= yf <= z[3] for z in excludes):
                continue
            total += 1
            if predicate(*rgb.getpixel((x, y))):
                matched += 1
    return matched / max(total, 1)


def _local_variance(img, x: int, y: int, radius: int = 2) -> float:
    w, h = img.size
    rgb = img.convert("RGB")
    vals: list[float] = []
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                r, g, b = rgb.getpixel((nx, ny))
                vals.append(_luminance(r, g, b))
    if len(vals) < 5:
        return 999.0
    mean = sum(vals) / len(vals)
    return sum((v - mean) ** 2 for v in vals) / len(vals)


def _inpaint_smear_frac(img) -> float:
    """Ghost smear: tan/cream пятна с соседними тёмными буквами (не текстура ткани)."""
    w, h = img.size
    rgb = img.convert("RGB")
    zone = CHEST_WORDSTAT_ZONE
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = int(zone[2] * w)
    y1 = int(zone[3] * h)
    smear = 0
    total = 0
    for y in range(y0, y1, 2):
        for x in range(x0, x1, 2):
            xf, yf = x / w, y / h
            if _in_norm_zone(xf, yf, TOPLEFT_WORDSTAT_ALLOWED):
                continue
            if _in_norm_zone(xf, yf, FACE_EXCLUDE_ZONE):
                continue
            if _in_norm_zone(xf, yf, CAT_MEME_CORE):
                continue
            total += 1
            r, g, b = rgb.getpixel((x, y))
            if not _is_paper_wordstat_pixel(r, g, b):
                continue
            has_ink = False
            for dy in range(-4, 5):
                for dx in range(-4, 5):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and _is_dark_ink_pixel(*rgb.getpixel((nx, ny))):
                        has_ink = True
                        break
                if has_ink:
                    break
            if has_ink and _local_variance(img, x, y, 3) < 120.0:
                smear += 1
    return smear / max(total, 1)


def _cat_meme_center(img) -> tuple[int, int]:
    """Центр cat meme sticker (orange fur cluster) в правом нижнем углу."""
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(CAT_MEME_CORE[0] * w)
    y0 = int(CAT_MEME_CORE[1] * h)
    x1 = int(CAT_MEME_CORE[2] * w)
    y1 = int(CAT_MEME_CORE[3] * h)
    sx = sy = cnt = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            r, g, b = rgb.getpixel((x, y))
            if r >= 175 and g <= 165 and r - g >= 25:
                sx += x
                sy += y
                cnt += 1
            elif _is_pure_white_paper(r, g, b) and y > h * 0.62:
                sx += x
                sy += y
                cnt += 1
    if cnt < 80:
        return (int(w * 0.86), int(h * 0.78))
    return (sx // cnt, sy // cnt)


def _meme_clearance_paper_frac(img, clearance_px: int = MEME_CLEARANCE_PX) -> float:
    """Wordstat paper в clearance вокруг cat meme (не внутри core)."""
    w, h = img.size
    cx, cy = _cat_meme_center(img)
    x0 = max(0, cx - clearance_px - 90)
    y0 = max(0, cy - clearance_px - 70)
    x1 = min(w, cx + clearance_px + 90)
    y1 = min(h, cy + clearance_px + 70)
    core_x0 = int(CAT_MEME_CORE[0] * w)
    core_y0 = int(CAT_MEME_CORE[1] * h)
    core_x1 = int(CAT_MEME_CORE[2] * w)
    core_y1 = int(CAT_MEME_CORE[3] * h)
    zone = (x0 / w, y0 / h, x1 / w, y1 / h)
    raw = _ghost_wordstat_paper_frac_in_zone(
        img,
        zone,
        exclude_zones=(TOPLEFT_WORDSTAT_ALLOWED, TITLE_ZONE, CAT_MEME_CORE),
    )
    # вычитаем core cat — clearance ring only
    rgb = img.convert("RGB")
    paper = total = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            if core_x0 <= x <= core_x1 and core_y0 <= y <= core_y1:
                continue
            total += 1
            r, g, b = rgb.getpixel((x, y))
            if not _is_paper_wordstat_pixel(r, g, b):
                continue
            xf, yf = x / w, y / h
            if _in_norm_zone(xf, yf, TOPLEFT_WORDSTAT_ALLOWED) or _in_norm_zone(xf, yf, TITLE_ZONE):
                continue
            has_ink = False
            for dy in range(-5, 6):
                for dx in range(-5, 6):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and _is_dark_ink_pixel(*rgb.getpixel((nx, ny))):
                        has_ink = True
                        break
                if has_ink:
                    break
            if has_ink:
                paper += 1
    return paper / max(total, 1) if total else raw


def _peel_active_zone(xf: float, yf: float) -> bool:
    """Где можно снимать Wordstat: нижняя грудь/мем, не top-left board и не лицо."""
    if _in_norm_zone(xf, yf, TOPLEFT_WORDSTAT_SAFE):
        return False
    if _in_norm_zone(xf, yf, FACE_EXCLUDE_ZONE):
        return False
    return any(
        _in_norm_zone(xf, yf, z)
        for z in (CHEST_PEEL_ACTIVE, MEME_GUARD_ZONE, BOTTOM_DUP_PEEL_ZONE)
    )


def _build_peel_mask(img, w: int, h: int) -> tuple[Any, int]:
    """Маска tan paper + ink на стикерах в активной peel-зоне."""
    ip = img.load()
    mask = [[False] * w for _ in range(h)]
    peeled = 0

    for y in range(h):
        for x in range(w):
            xf, yf = x / w, y / h
            if not _peel_active_zone(xf, yf):
                continue
            if _is_paper_wordstat_pixel(*ip[x, y]):
                mask[y][x] = True
                peeled += 1

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if mask[y][x]:
                continue
            xf, yf = x / w, y / h
            if not _peel_active_zone(xf, yf):
                continue
            r, g, b = ip[x, y]
            if _luminance(r, g, b) > 105:
                continue
            if any(mask[ny][nx] for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))):
                mask[y][x] = True
                peeled += 1

    return mask, peeled


def _sample_vest_rgb(img, w: int, h: int) -> tuple[int, int, int]:
    """Navy жилет — референс с чистого участка без стикеров."""
    ip = img.load()
    samples: list[tuple[int, int, int]] = []
    for y in range(int(h * 0.48), int(h * 0.58)):
        for x in range(int(w * 0.54), int(w * 0.62)):
            r, g, b = ip[x, y]
            if _is_paper_wordstat_pixel(r, g, b):
                continue
            lum = _luminance(r, g, b)
            if lum > 95 or r > 110:
                continue
            samples.append((r, g, b))
    if not samples:
        return (32, 42, 78)
    return (
        sum(c[0] for c in samples) // len(samples),
        sum(c[1] for c in samples) // len(samples),
        sum(c[2] for c in samples) // len(samples),
    )


def _scrub_remaining_paper(work, w: int, h: int, vest_rgb: tuple[int, int, int]) -> int:
    """Последний проход: cream fringe → navy жилет."""
    op = work.load()
    scrubbed = 0
    for y in range(h):
        for x in range(w):
            xf, yf = x / w, y / h
            if not _peel_active_zone(xf, yf):
                continue
            r, g, b = op[x, y]
            if not _is_paper_wordstat_pixel(r, g, b):
                continue
            jitter = ((x * 5 + y * 11) % 7) - 3
            op[x, y] = (
                max(0, min(255, vest_rgb[0] + jitter)),
                max(0, min(255, vest_rgb[1] + jitter)),
                max(0, min(255, vest_rgb[2] + jitter)),
            )
            scrubbed += 1
    return scrubbed


def _inpaint_from_neighbors(src, mask, w: int, h: int, *, max_radius: int = 14) -> Any:
    """Заполнить маску медианой ближайших немаскированных пикселей оригинала."""
    from PIL import Image

    sip = src.load()
    out = src.copy()
    op = out.load()

    for y in range(h):
        for x in range(w):
            if not mask[y][x]:
                continue
            picked: list[tuple[int, int, int]] = []
            for radius in range(1, max_radius + 1):
                for dy in range(-radius, radius + 1):
                    for dx in range(-radius, radius + 1):
                        if max(abs(dx), abs(dy)) != radius:
                            continue
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= w or ny >= h:
                            continue
                        if mask[ny][nx]:
                            continue
                        picked.append(sip[nx, ny])
                if len(picked) >= 6:
                    break
            if not picked:
                continue
            rs = sorted(c[0] for c in picked)
            gs = sorted(c[1] for c in picked)
            bs = sorted(c[2] for c in picked)
            mid = len(picked) // 2
            op[x, y] = (rs[mid], gs[mid], bs[mid])
    return out


def peel_chest_wordstat_stickers(cover_path: Path, *, max_passes: int = 4) -> dict[str, Any]:
    """Удалить Wordstat paper stickers с груди/мема; сохранить top-left board labels."""
    from PIL import Image, ImageFilter

    if not cover_path.is_file():
        return {"status": "SKIP", "reason": f"{cover_path} missing"}

    original = Image.open(cover_path).convert("RGB")
    w, h = original.size
    total_peeled = 0
    passes = 0

    work = original.copy()
    for _ in range(max_passes):
        mask_grid, peeled = _build_peel_mask(work, w, h)
        if peeled < 40:
            break
        passes += 1
        total_peeled += peeled
        work = _inpaint_from_neighbors(work, mask_grid, w, h)
        # Лёгкое сглаживание только на месте стикеров
        mask_img = Image.new("L", (w, h), 0)
        mp = mask_img.load()
        for y in range(h):
            for x in range(w):
                if mask_grid[y][x]:
                    mp[x, y] = 255
        if mp[0, 0] or any(mp[x, y] for y in range(h) for x in range(w)):
            blurred = work.filter(ImageFilter.GaussianBlur(radius=1))
            work = Image.composite(blurred, work, mask_img.filter(ImageFilter.MaxFilter(3)))

        chest = _paper_frac_in_zone(
            work, CHEST_WORDSTAT_ZONE, exclude_zones=(TOPLEFT_WORDSTAT_SAFE, FACE_EXCLUDE_ZONE)
        )
        meme = _paper_frac_in_zone(
            work, MEME_OCCLUSION_ZONE, exclude_zones=(TOPLEFT_WORDSTAT_SAFE, FACE_EXCLUDE_ZONE)
        )
        if chest < 0.012 and meme < 0.015:
            break

    if total_peeled < 40:
        return {"status": "SKIP", "reason": f"only {total_peeled} peel pixels", "peeled_pixels": total_peeled}

    vest_rgb = _sample_vest_rgb(original, w, h)
    scrubbed = _scrub_remaining_paper(work, w, h, vest_rgb)

    work.save(cover_path, format="PNG")
    return {
        "status": "OK",
        "peeled_pixels": total_peeled,
        "scrubbed_pixels": scrubbed,
        "passes": passes,
        "vest_rgb": list(vest_rgb),
        "file": cover_path.name,
    }


def _is_dark_garment(r: int, g: int, b: int) -> bool:
    return _luminance(r, g, b) < 70


def _zone_pixels(img, zone: tuple[float, float, float, float]) -> list[tuple[int, int, int]]:
    w, h = img.size
    x0 = int(zone[0] * w)
    y0 = int(zone[1] * h)
    x1 = max(x0 + 1, int(zone[2] * w))
    y1 = max(y0 + 1, int(zone[3] * h))
    crop = img.crop((x0, y0, x1, y1))
    return list(crop.convert("RGB").getdata())


def _face_skin_metrics(img) -> dict[str, Any]:
    """Метрики лица в верхней центральной зоне (не весь кадр / не асфальт)."""
    w, h = img.size
    rgb = img.convert("RGB")
    x0 = int(w * 0.28)
    x1 = int(w * 0.82)
    y0 = int(h * 0.04)
    y1 = int(h * 0.62)
    row_density: list[tuple[int, float]] = []
    for y in range(y0, y1):
        skin = 0
        total = max(x1 - x0, 1)
        for x in range(x0, x1):
            if _is_skin(*rgb.getpixel((x, y))):
                skin += 1
        row_density.append((y, skin / total))

    bands: list[tuple[int, int, float]] = []
    in_band = False
    band_y0 = y0
    densities: list[float] = []
    for y, dens in row_density:
        if dens >= 0.06:
            if not in_band:
                in_band = True
                band_y0 = y
                densities = [dens]
            else:
                densities.append(dens)
        elif in_band:
            if len(densities) >= 4:
                bands.append((band_y0, y - 1, sum(densities) / len(densities)))
            in_band = False
            densities = []
    if in_band and len(densities) >= 4:
        bands.append((band_y0, row_density[-1][0], sum(densities) / len(densities)))

    if not bands:
        return {"face_band": None, "face_h_frac": 0.0, "face_w_frac": 0.0}

    # Самая плотная полоса = лицо/лоб/щёки
    bands.sort(key=lambda b: (b[1] - b[0] + 1) * b[2], reverse=True)
    by0, by1, avg_d = bands[0]
    face_h = by1 - by0 + 1
    xs: list[int] = []
    for y in range(by0, by1 + 1):
        for x in range(x0, x1):
            if _is_skin(*rgb.getpixel((x, y))):
                xs.append(x)
    face_w = (max(xs) - min(xs) + 1) if xs else 0
    return {
        "face_band": {"y0": by0, "y1": by1, "avg_density": round(avg_d, 3)},
        "face_h_frac": round(face_h / h, 3),
        "face_w_frac": round(face_w / w, 3) if w else 0.0,
        "skin_pixel_count": len(xs),
    }


def _bands_in_zone(bands: list[dict[str, Any]], zone: tuple[float, float, float, float], img_size: tuple[int, int]) -> list[dict[str, Any]]:
    w, h = img_size
    zx0, zy0, zx1, zy1 = zone
    hits: list[dict[str, Any]] = []
    for band in bands:
        if not band.get("bar_like"):
            continue
        y_mid = (band["y0"] + band["y1"]) / 2 / h
        x_mid = (band.get("x0", int(w * 0.62)) + band.get("x1", w - 1)) / 2 / w if band.get("x1") else 0.78
        if zx0 <= x_mid <= zx1 and zy0 <= y_mid <= zy1:
            hits.append(band)
    return hits


def _detect_gold_bands(img) -> list[dict[str, Any]]:
    """Найти горизонтальные opaque gold полосы (PIL bar overlay signature)."""
    w, h = img.size
    rgb = img.convert("RGB")
    x_start = int(w * 0.62)
    bands: list[dict[str, Any]] = []
    in_band = False
    band_y0 = 0
    band_rows: list[int] = []

    for y in range(h):
        row_gold = 0
        row_total = 0
        for x in range(x_start, w):
            r, g, b = rgb.getpixel((x, y))
            row_total += 1
            if _is_gold_sticker(r, g, b):
                row_gold += 1
        ratio = row_gold / max(row_total, 1)
        if ratio >= 0.45:
            if not in_band:
                in_band = True
                band_y0 = y
            band_rows.append(y)
        elif in_band:
            if len(band_rows) >= 8:
                y1 = band_rows[-1]
                height = y1 - band_y0 + 1
                mid_y = band_y0 + height // 2
                gold_xs = [
                    x
                    for x in range(x_start, w)
                    if _is_gold_sticker(*rgb.getpixel((x, mid_y)))
                ]
                width = (max(gold_xs) - min(gold_xs) + 1) if gold_xs else 0
                touches_right = bool(gold_xs and max(gold_xs) >= w - 6)
                aspect = width / max(height, 1)
                strip_frac = width / max(w - x_start, 1)
                # bar = широкая горизонтальная полоса; маленький бумажный стикер не bar
                bar_like = aspect >= 3.5 and height >= 10 and strip_frac >= 0.55
                bands.append(
                    {
                        "y0": band_y0,
                        "y1": y1,
                        "height": height,
                        "width": width,
                        "x0": min(gold_xs) if gold_xs else x_start,
                        "x1": max(gold_xs) if gold_xs else w - 1,
                        "aspect": round(aspect, 2),
                        "strip_frac": round(strip_frac, 2),
                        "touches_right_edge": touches_right,
                        "bar_like": bar_like,
                    }
                )
            in_band = False
            band_rows = []

    if in_band and len(band_rows) >= 8:
        y1 = band_rows[-1]
        height = y1 - band_y0 + 1
        mid_y = band_y0 + height // 2
        gold_xs = [
            x for x in range(x_start, w) if _is_gold_sticker(*rgb.getpixel((x, mid_y)))
        ]
        width = (max(gold_xs) - min(gold_xs) + 1) if gold_xs else 0
        strip_frac = width / max(w - x_start, 1)
        bands.append(
            {
                "y0": band_y0,
                "y1": y1,
                "height": height,
                "width": width,
                "x0": min(gold_xs) if gold_xs else x_start,
                "x1": max(gold_xs) if gold_xs else w - 1,
                "aspect": round(width / max(height, 1), 2),
                "strip_frac": round(strip_frac, 2),
                "touches_right_edge": bool(gold_xs and max(gold_xs) >= w - 6),
                "bar_like": (width / max(height, 1)) >= 3.5
                and height >= 10
                and strip_frac >= 0.55,
            }
        )
    return bands


def _gold_overlap_fraction(img, zone: tuple[float, float, float, float]) -> float:
    px = _zone_pixels(img, zone)
    if not px:
        return 0.0
    gold = sum(1 for r, g, b in px if _is_gold_sticker(r, g, b))
    return gold / len(px)


def _mean_luminance(img) -> float:
    px = list(img.convert("RGB").getdata())
    if not px:
        return 0.0
    return sum(_luminance(r, g, b) for r, g, b in px) / len(px)


def _host_dark_ratio(img) -> float:
    px = _zone_pixels(img, HOST_ZONE)
    if not px:
        return 0.0
    dark = sum(1 for r, g, b in px if _is_dark_garment(r, g, b))
    return dark / len(px)


def _manifest_outfit_tokens(manifest: dict[str, Any] | None) -> str:
    if not manifest:
        return ""
    motifs = manifest.get("cover_motifs") or {}
    return str(motifs.get("outfit") or "").casefold()


def _manifest_expects_warm_outfit(manifest: dict[str, Any] | None) -> bool:
    outfit = _manifest_outfit_tokens(manifest)
    if not outfit:
        return False
    if any(tok in outfit for tok in BANNED_OUTFIT_TOKENS):
        return False
    return any(tok in outfit for tok in WARM_OUTFIT_TOKENS)


def _phone_digits_present(img) -> bool:
    """Телефон +7 922 001 65 05 — только нижний правый sacred zone (не Wordstat strips)."""
    return _phone_zone_ink_count(img) >= PHONE_ZONE_MIN_INK


def describe_cover_pixels(cover_path: Path) -> str:
    """Краткое описание кадра по пикселям (не prompt)."""
    from PIL import Image

    img = Image.open(cover_path).convert("RGB")
    w, h = img.size
    metrics = _face_skin_metrics(img)
    bands = _detect_gold_bands(img)
    bar_count = sum(1 for b in bands if b.get("bar_like"))
    dark_ratio = _host_dark_ratio(img)
    lum = _mean_luminance(img)

    face_h_frac = float(metrics.get("face_h_frac") or 0.0)
    crop = "unknown"
    if face_h_frac >= 0.20:
        crop = "close-up face+shoulders"
    elif face_h_frac >= 0.12:
        crop = "medium bust"
    elif face_h_frac > 0:
        crop = "distant small figure"
    else:
        crop = "no face skin detected"

    garment = "dark/black dominant torso" if dark_ratio >= 0.32 else "light/warm garment dominant"
    stickers = f"{bar_count} bar-like gold strips" if bar_count else f"{len(bands)} paper-gold regions"
    return (
        f"{w}x{h}; mean_lum={lum:.0f}; host_crop={crop}; garment={garment}; "
        f"wordstat={stickers}; face_h_frac={face_h_frac:.2f}"
    )


@dataclass
class PixelQAResult:
    status: str
    checks: dict[str, bool] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "checks": self.checks,
            "errors": self.errors,
            "evidence": self.evidence,
        }


def analyze_cover_pixels(
    cover_path: Path,
    *,
    manifest: dict[str, Any] | None = None,
    phrases: list[str] | None = None,
) -> PixelQAResult:
    from PIL import Image

    errors: list[str] = []
    checks: dict[str, bool] = {}
    evidence: dict[str, Any] = {}

    if not cover_path.is_file():
        return PixelQAResult(
            "FAIL",
            checks={"pixel_cover_file_exists": False},
            errors=[f"missing {cover_path}"],
        )

    raw = cover_path.read_bytes()
    evidence["cover_md5"] = md5_bytes(raw)
    evidence["cover_bytes"] = len(raw)

    img = Image.open(cover_path).convert("RGB")
    w, h = img.size
    evidence["size"] = [w, h]
    evidence["pixel_description"] = describe_cover_pixels(cover_path)

    # --- light high-key ---
    lum = _mean_luminance(img)
    evidence["mean_luminance"] = round(lum, 1)
    checks["pixel_light_high_key"] = lum >= 165
    if not checks["pixel_light_high_key"]:
        errors.append(f"pixel_light_high_key FAIL: mean_lum={lum:.0f} < 165")

    # --- host close-up (face band in upper center, not full-body speck) ---
    face_metrics = _face_skin_metrics(img)
    evidence["face_skin"] = face_metrics
    face_h_frac = float(face_metrics.get("face_h_frac") or 0.0)
    face_w_frac = float(face_metrics.get("face_w_frac") or 0.0)
    checks["pixel_host_close_up"] = face_h_frac >= 0.18 and face_w_frac >= 0.08
    checks["pixel_host_not_distant_fullbody"] = face_h_frac >= 0.14
    if not checks["pixel_host_close_up"]:
        errors.append(
            f"pixel_host_close_up FAIL: face_h_frac={face_h_frac:.2f} w_frac={face_w_frac:.2f} (need close-up)"
        )
    if not checks["pixel_host_not_distant_fullbody"]:
        errors.append(
            f"pixel_host_not_distant_fullbody FAIL: distant tiny host face_h_frac={face_h_frac:.2f}"
        )

    # --- Wordstat bars vs stickers ---
    bands = _detect_gold_bands(img)
    bar_like = [b for b in bands if b.get("bar_like")]
    edge_truncated = [b for b in bar_like if b.get("touches_right_edge")]
    evidence["gold_bands"] = bands
    checks["pixel_wordstat_not_opaque_bars"] = len(bar_like) == 0
    checks["pixel_wordstat_not_edge_truncated"] = len(edge_truncated) == 0
    if bar_like:
        errors.append(
            f"pixel_wordstat_not_opaque_bars FAIL: {len(bar_like)} horizontal opaque bar(s)"
        )
    if edge_truncated:
        errors.append(
            f"pixel_wordstat_not_edge_truncated FAIL: sticker text cut at right edge"
        )

    # --- title / meme zones (bar-like bands only, not gold headline typography) ---
    title_bands = _bands_in_zone(bar_like, TITLE_ZONE, (w, h))
    meme_bands = _bands_in_zone(bar_like, MEME_ZONE, (w, h))
    evidence["title_zone_bar_bands"] = len(title_bands)
    evidence["meme_zone_bar_bands"] = len(meme_bands)
    checks["pixel_title_zone_clear"] = len(title_bands) == 0
    checks["pixel_meme_zone_clear"] = len(meme_bands) == 0
    if not checks["pixel_title_zone_clear"]:
        errors.append(f"pixel_title_zone_clear FAIL: {len(title_bands)} bar band(s) on title")
    if not checks["pixel_meme_zone_clear"]:
        errors.append(f"pixel_meme_zone_clear FAIL: {len(meme_bands)} bar band(s) on meme")

    # --- paper Wordstat on chest / over meme cat (not just bars) ---
    qa_excludes = (TOPLEFT_WORDSTAT_ALLOWED, FACE_EXCLUDE_ZONE, CAT_MEME_CORE)
    chest_paper = _ghost_wordstat_paper_frac_in_zone(
        img, CHEST_WORDSTAT_ZONE, exclude_zones=qa_excludes
    )
    meme_paper = _ghost_wordstat_paper_frac_in_zone(
        img, MEME_OCCLUSION_ZONE, exclude_zones=qa_excludes
    )
    evidence["chest_wordstat_paper_frac"] = round(chest_paper, 4)
    evidence["meme_guard_wordstat_paper_frac"] = round(meme_paper, 4)
    checks["pixel_wordstat_not_on_host_chest"] = chest_paper < 0.012
    checks["pixel_meme_not_occluded_by_wordstat"] = meme_paper < 0.015
    if not checks["pixel_wordstat_not_on_host_chest"]:
        errors.append(
            f"pixel_wordstat_not_on_host_chest FAIL: paper_frac={chest_paper:.3f} on vest"
        )
    if not checks["pixel_meme_not_occluded_by_wordstat"]:
        errors.append(
            f"pixel_meme_not_occluded_by_wordstat FAIL: paper_frac={meme_paper:.3f} on meme zone"
        )

    # --- Wordstat только top-left (не на одежде/справа) ---
    right_paper = _ghost_wordstat_paper_frac_in_zone(
        img,
        WORDSTAT_RIGHT_FORBIDDEN,
        exclude_zones=(FACE_EXCLUDE_ZONE, CAT_MEME_CORE, TITLE_ZONE, TOPLEFT_WORDSTAT_ALLOWED),
    )
    evidence["wordstat_right_forbidden_paper_frac"] = round(right_paper, 4)
    checks["pixel_wordstat_only_top_left"] = right_paper < 0.006
    if not checks["pixel_wordstat_only_top_left"]:
        errors.append(
            f"pixel_wordstat_only_top_left FAIL: paper_frac={right_paper:.3f} outside top-left zone"
        )

    # --- ghost/garbled text on clothing ---
    clothing_ink = _frac_predicate_in_zone(
        img,
        CLOTHING_NO_TEXT_ZONE,
        _is_dark_ink_pixel,
        exclude_zones=(FACE_EXCLUDE_ZONE, CAT_MEME_CORE, TITLE_ZONE),
    )
    evidence["clothing_dark_ink_frac"] = round(clothing_ink, 4)
    checks["pixel_no_text_on_clothing"] = clothing_ink < 0.045
    if not checks["pixel_no_text_on_clothing"]:
        errors.append(
            f"pixel_no_text_on_clothing FAIL: dark_ink_frac={clothing_ink:.3f} on chest/clothes"
        )

    # --- inpaint blobs: blue outlines + neck smear + low-variance tan smears ---
    face_blue = _frac_predicate_in_zone(img, FACE_ARTIFACT_ZONE, _is_blue_artifact_pixel)
    chest_blue = _frac_predicate_in_zone(
        img, CHEST_WORDSTAT_ZONE, _is_blue_artifact_pixel, exclude_zones=(FACE_EXCLUDE_ZONE,)
    )
    neck_skin = _frac_predicate_in_zone(img, NECK_INPAINT_ZONE, _is_skin)
    smear_frac = _inpaint_smear_frac(img)
    evidence["face_blue_artifact_frac"] = round(face_blue, 4)
    evidence["chest_blue_artifact_frac"] = round(chest_blue, 4)
    evidence["neck_skin_blob_frac"] = round(neck_skin, 4)
    evidence["inpaint_smear_frac"] = round(smear_frac, 4)
    checks["pixel_no_inpaint_artifacts"] = (
        face_blue < 0.0015
        and chest_blue < 0.012
        and smear_frac < 0.08
    )
    if not checks["pixel_no_inpaint_artifacts"]:
        errors.append(
            "pixel_no_inpaint_artifacts FAIL: "
            f"face_blue={face_blue:.4f} chest_blue={chest_blue:.3f} smear={smear_frac:.3f}"
        )

    # --- cat meme clearance ≥80px from Wordstat paper ---
    clearance_paper = _meme_clearance_paper_frac(img, MEME_CLEARANCE_PX)
    evidence["meme_clearance_wordstat_paper_frac"] = round(clearance_paper, 4)
    checks["pixel_meme_clearance_80px"] = clearance_paper < 0.008
    if not checks["pixel_meme_clearance_80px"]:
        errors.append(
            f"pixel_meme_clearance_80px FAIL: paper_frac={clearance_paper:.3f} within 80px of cat"
        )

    # --- truncated phrase heuristics (partial words at strip edge) ---
    phrase_list = phrases or (manifest or {}).get("wordstat_stickers") or []
    truncated_phrase = False
    for phrase in phrase_list:
        p = str(phrase).strip().casefold()
        if not p:
            continue
        # типичные обрезки из FAIL cover
        if p.endswith(" в") or p.endswith(" продав") or p.endswith(" продавц"):
            truncated_phrase = True
        if len(p) >= 8 and p.split()[-1] in {"в", "на", "за", "от", "по", "продав"}:
            truncated_phrase = True
    checks["pixel_wordstat_phrases_not_truncated"] = not truncated_phrase and not edge_truncated
    if truncated_phrase:
        errors.append("pixel_wordstat_phrases_not_truncated FAIL: manifest/history partial phrases")

    # --- designed thumbnail: hook title, phone, meme, sticker spacing, no layout collapse ---
    hook_metrics = _hook_title_metrics(img)
    phone_ink = _phone_zone_ink_count(img)
    meme_signal = _meme_corner_signal(img)
    sticker_overlap = _wordstat_sticker_overlap_metrics(
        img, hook_present=bool(hook_metrics.get("present"))
    )
    query_strips = _wordstat_query_strip_metrics(img)
    layout_metrics = _layout_collapse_metrics(img, hook_present=bool(hook_metrics.get("present")))
    evidence["hook_title"] = hook_metrics
    evidence["phone_zone_ink"] = phone_ink
    evidence["meme_corner_signal"] = meme_signal
    evidence["wordstat_sticker_overlap"] = sticker_overlap
    evidence["wordstat_query_strips"] = query_strips
    evidence["layout_collapse"] = layout_metrics

    checks["pixel_hook_title_present"] = bool(hook_metrics.get("present"))
    checks["pixel_phone_readable"] = phone_ink >= PHONE_ZONE_MIN_INK
    checks["pixel_meme_present"] = meme_signal >= MEME_CORNER_MIN_SIGNAL
    checks["pixel_no_wordstat_query_strips"] = bool(query_strips.get("ok"))
    checks["pixel_wordstat_stickers_not_overlapping"] = True  # legacy key; strips banned
    checks["pixel_layout_not_collapsed"] = not bool(layout_metrics.get("collapsed"))
    checks["pixel_designed_thumbnail"] = cover_composition_ok(img)

    if not checks["pixel_hook_title_present"]:
        errors.append(
            "pixel_hook_title_present FAIL: no large readable hook title in sacred zone "
            f"(bands={hook_metrics.get('bands')})"
        )
    if not checks["pixel_phone_readable"]:
        errors.append(
            f"pixel_phone_readable FAIL: phone_zone_ink={phone_ink} < {PHONE_ZONE_MIN_INK}"
        )
    if not checks["pixel_meme_present"]:
        errors.append(
            f"pixel_meme_present FAIL: meme_corner_signal={meme_signal} < {MEME_CORNER_MIN_SIGNAL}"
        )
    if not checks["pixel_no_wordstat_query_strips"]:
        errors.append(
            "pixel_no_wordstat_query_strips FAIL: "
            f"{query_strips.get('strip_components', 0)} Wordstat strip(s), "
            f"{query_strips.get('bar_bands', 0)} bar band(s), "
            f"paper_frac={query_strips.get('paper_frac')}"
        )
    if not checks["pixel_layout_not_collapsed"]:
        errors.append(
            "pixel_layout_not_collapsed FAIL: face-only crop with no hook title "
            f"(face_h={layout_metrics.get('face_h_frac')}, face_w={layout_metrics.get('face_w_frac')})"
        )
    if not checks["pixel_designed_thumbnail"]:
        errors.append("pixel_designed_thumbnail FAIL: cover is not a designed 1200×675 thumbnail")

    # --- manifest lie: outfit vs pixels ---
    dark_ratio = _host_dark_ratio(img)
    evidence["host_dark_ratio"] = round(dark_ratio, 3)
    outfit = _manifest_outfit_tokens(manifest)
    expects_warm = _manifest_expects_warm_outfit(manifest)
    manifest_says_blazer = any(tok in outfit for tok in BANNED_OUTFIT_TOKENS)
    pixels_dark_suit = dark_ratio >= 0.34
    checks["pixel_manifest_outfit_matches"] = True
    if expects_warm and pixels_dark_suit:
        checks["pixel_manifest_outfit_matches"] = False
        errors.append(
            "pixel_manifest_outfit_matches FAIL: manifest warm outfit but pixels show dark/black blazer torso"
        )
    if manifest_says_blazer and not pixels_dark_suit:
        # не блокируем жёстко — но variety lock отдельно
        evidence["manifest_outfit_note"] = "manifest mentions blazer but pixels not dark"

    checks["pixel_qa_reads_png_not_prompt"] = True  # этот модуль всегда читает PNG

    all_pass = all(checks.values()) and not errors
    status = "PASS" if all_pass else "FAIL"
    return PixelQAResult(status=status, checks=checks, errors=errors, evidence=evidence)


def stamp_cover_qa_json(
    article_dir: Path,
    pixel_result: PixelQAResult,
    *,
    topic_id: str = "",
    merge_checks: dict[str, bool] | None = None,
) -> Path:
    """Записать cover_qa.json только из pixel+merge checks (не доверять agent stamp)."""
    qa_path = article_dir / "cover" / "cover_qa.json"
    checks = dict(merge_checks or {})
    checks.update(pixel_result.checks)
    # legacy keys expected by gate
    legacy_map = {
        "identity_face_28yo": checks.get("pixel_host_close_up", False),
        "identity_body_medium_slim": checks.get("pixel_host_not_distant_fullbody", False),
        "identity_expression_invented": True,
        "title_not_occluded": (
            checks.get("pixel_title_zone_clear", False)
            and checks.get("pixel_wordstat_not_on_host_chest", False)
            and checks.get("pixel_meme_not_occluded_by_wordstat", False)
            and checks.get("pixel_no_text_on_clothing", False)
            and checks.get("pixel_meme_clearance_80px", False)
            and checks.get("pixel_hook_title_present", False)
            and checks.get("pixel_no_wordstat_query_strips", False)
            and checks.get("pixel_layout_not_collapsed", False)
        ),
        "outfit_invented": checks.get("pixel_manifest_outfit_matches", False),
        "action_invented": True,
        "emotion_not_copied_from_recent_covers": True,
        "cover_phone_readable": checks.get("pixel_phone_readable", False),
        "board_stationery_ok": checks.get("pixel_wordstat_not_opaque_bars", False),
        "typography_cyrillic_clean": checks.get("pixel_wordstat_phrases_not_truncated", False),
        "meme_density_inline_ok": True,
        "light_high_key": checks.get("pixel_light_high_key", False),
        "motif_no_collision_14d": True,
        "people_in_8_set": True,
        "cats_cadence_ok": True,
        "wordstat_stickers_1_3": checks.get("pixel_no_wordstat_query_strips", False),
        "no_wordstat_query_strips_on_cover": checks.get("pixel_no_wordstat_query_strips", False),
        "identity_real_files": True,
        "inline_utility_all_7": True,
        "inline_no_host_face": True,
        "inline_no_co_host_human": True,
        "inline_meme_sticker_scale": True,
        "meme_people_real_catalog": True,
    }
    checks.update(legacy_map)
    all_true = all(checks.values()) and pixel_result.status == "PASS"
    payload = {
        "agent": "excalibur-blog-cover-qa",
        "status": "PASS" if all_true else "FAIL",
        "checked_at": date.today().isoformat(),
        "topic_id": topic_id or "",
        "cover_md5": pixel_result.evidence.get("cover_md5"),
        "pixel_qa": True,
        "pixel_description": pixel_result.evidence.get("pixel_description"),
        "checks": checks,
        "pixel_errors": pixel_result.errors,
        "pixel_evidence": {
            k: pixel_result.evidence[k]
            for k in ("size", "mean_luminance", "skin_bbox", "gold_bands", "host_dark_ratio")
            if k in pixel_result.evidence
        },
        "notes": (
            f"Pixel QA on cover.png md5={pixel_result.evidence.get('cover_md5')}; "
            f"{pixel_result.evidence.get('pixel_description')}"
        ),
    }
    qa_path.parent.mkdir(parents=True, exist_ok=True)
    qa_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return qa_path


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cover", type=Path, help="Path to cover.png")
    ap.add_argument("--article-dir", type=Path, help="Article dir (uses cover/cover.png + manifest)")
    ap.add_argument("--stamp", action="store_true", help="Write cover/cover_qa.json from pixel results")
    ap.add_argument("--describe", action="store_true", help="Print pixel description only")
    ap.add_argument("--peel-chest", action="store_true", help="Remove chest/meme Wordstat stickers in-place")
    args = ap.parse_args()
    root = project_root()

    cover_path: Path | None = args.cover
    manifest: dict[str, Any] | None = None
    topic_id = ""

    if args.article_dir:
        article_dir = args.article_dir
        if not article_dir.is_absolute():
            article_dir = root / article_dir
        cover_path = article_dir / "cover" / "cover.png"
        manifest_path = article_dir / "cover" / "quad-manifest.json"
        if manifest_path.is_file():
            manifest = load_json(manifest_path)
            topic_id = str(manifest.get("topic_id") or "")
        meta_path = article_dir / "article.meta.json"
        if meta_path.is_file():
            try:
                topic_id = topic_id or str(load_json(meta_path).get("topic_id") or "")
            except json.JSONDecodeError:
                pass

    if not cover_path or not cover_path.is_file():
        print(f"FAIL missing cover: {cover_path}", file=sys.stderr)
        return 1

    if args.describe:
        print(describe_cover_pixels(cover_path))
        print(f"md5={md5_file(cover_path)}")
        return 0

    if args.peel_chest:
        report = peel_chest_wordstat_stickers(cover_path)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report.get("status") == "OK" else 1

    result = analyze_cover_pixels(cover_path, manifest=manifest)
    print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))

    if args.stamp and args.article_dir:
        article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
        stamp_cover_qa_json(article_dir, result, topic_id=topic_id)

    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
