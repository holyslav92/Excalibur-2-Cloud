#!/usr/bin/env python3
"""Перегенерация только cover для live-постов (grsai GPT Image 2 i2i, face lock).

FACE: только face-studio-2026-06-23.jpg через /images/edits (grsai i2i).
Derouter gpt-6-astra — текст; DEROUTER_IMAGE_MODEL для картинок снят с платформы.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

from excalibur_blog_cover_identity import (
    BODY_LOCK,
    COVER_I2I_BANS,
    COVER_PHONE,
    FACE_PRIMARY,
    IDENTITY_SUFFIX,
    I2I_EXPRESSION_LOCK,
    ensure_face_reference,
    identity_public_url,
)
from excalibur_blog_grsai_gpt_image2_api import (
    DEFAULT_TIMEOUT_SECONDS,
    MIN_TIMEOUT_SECONDS,
    default_quality,
    generate_image,
    model_tier_standard,
    project_root,
    resolve_grsai_api_key,
    resolve_hosts,
)

SOLO_COVER_SIZE = "1200x675"

# Новые посты (скриншоты пользователя 2026-09-06)
NEW_COVER_BATCH: list[dict[str, Any]] = [
    {
        "post_id": 9640,
        "slug": "v-tyumeni-semya-perevela-avans-na-eskrou-schet-okazalsya-chuzhim",
        "hook": "Аванс ушёл на чужой счёт",
        "highlight": "чужой",
        "sticky": "QR из переписки",
        "emotion": "worried checking phone payment",
        "scene": "messenger QR wrong recipient, bank alert",
    },
    {
        "post_id": 9723,
        "slug": "v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch",
        "hook": "Аренду запретили — бронь сгорела",
        "highlight": "сгорела",
        "sticky": "ДДУ прислали слишком поздно",
        "emotion": "frustrated at rent ban in DDU",
        "scene": "DDU rent prohibited clause, keys on desk",
    },
    {
        "post_id": 9710,
        "slug": "v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela",
        "hook": "Продавец ПОДНЯЛ цену перед самой сделкой",
        "highlight": "ПОДНЯЛ",
        "sticky": "Бронь сгорела за сутки",
        "emotion": "stressed holding +280000 DDU paper",
        "scene": "assignment price jump day before signing",
    },
    {
        "post_id": 9697,
        "slug": "v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela",
        "hook": "Оценку квартиры СНИЗИЛИ — бронь сгорела",
        "highlight": "СНИЗИЛИ",
        "sticky": "-600 тыс за сутки",
        "emotion": "baffled at trade-in appraisal drop",
        "scene": "tablet appraisal graph down, reservation lost",
    },
    {
        "post_id": 9749,
        "slug": "v-tyumeni-v-ddu-napisali-kvartiru-v-vypiske-okazalis-apartamenty",
        "hook": "Выписка ЕГРН лишила семью ИПОТЕКИ",
        "highlight": "ИПОТЕКИ",
        "sticky": "Ключи не взяли",
        "emotion": "shocked EGRN says apartments not flat",
        "scene": "EGRN extract apartment vs квартира mismatch",
    },
    {
        "post_id": 9775,
        "slug": "v-tyumeni-ddu-na-45-kv-m-ostanovili-deklaratsiya-pokazala-41",
        "hook": "ДДУ написали 45 — в декларации 41",
        "highlight": "41",
        "sticky": "Четыре метра исчезли",
        "emotion": "confused comparing DDU 45 vs declaration 41",
        "scene": "floor plan area mismatch papers",
    },
]

COVER_REGEN_MANIFEST: list[dict[str, Any]] = NEW_COVER_BATCH


def build_solo_prompt(item: dict[str, Any]) -> str:
    hook = str(item["hook"])
    highlight = str(item.get("highlight") or "")
    sticky = str(item.get("sticky") or "")
    scene = str(item.get("scene") or "")
    emotion = str(item.get("emotion") or "")
    highlight_rule = (
        f'paint ONLY the word "{highlight}" in gold #dcc5a1 brush accent'
        if highlight
        else "one gold accent word max"
    )
    sticky_line = f" Yellow sticky EXACT «{sticky}» pinned left." if sticky else ""
    style_prefix = (
        "Dense RU editorial collage, WHITE #FFFFFF, BLACK #141821 Cyrillic ink, "
        "gold #dcc5a1 one accent only. Torn paper, gold tape/sticky, informative cards."
    )
    return (
        f"{style_prefix}\n"
        "ONE SINGLE 16:9 cover frame 1200x675 — NOT a 2x2 grid, NOT quad canvas.\n"
        f"{COVER_I2I_BANS}\n"
        "TEXT LOCK: Russian Cyrillic only. Allowed: headline hook, phone CTA, one sticky.\n"
        f"Headline EXACT «{hook}» bold black RIGHT zone (52–96% width), {highlight_rule}.\n"
        f"Phone EXACT «{COVER_PHONE}» white torn paper bottom-RIGHT.\n"
        f"{sticky_line}\n"
        f"Host i2i face-studio-2026-06-23 ({BODY_LOCK}); {I2I_EXPRESSION_LOCK}. "
        f"Expression: {emotion}. Scene: {scene}. "
        "Face+shoulders LEFT (~35% frame), room for headline right. "
        "Tiny thinking-cat meme ≤10% bottom-right, ≥80px from phone/headline. "
        "Sun flare, bright #FFF, perfect Cyrillic."
        f"{IDENTITY_SUFFIX}"
    )


def write_batch(article_dir: Path, prompt: str) -> Path:
    batch = {
        "pipeline": "grsai_solo_cover_regen",
        "slot": "cover",
        "prefer_local_reference": True,
        "local_reference": str(FACE_PRIMARY),
        "cover_i2i_required": True,
        "jobs": [
            {
                "slot": "cover",
                "tool": "grsai-rest",
                "mcp_args": {
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "resolution": "1K",
                    "input_urls": [identity_public_url()],
                },
            }
        ],
    }
    path = article_dir / "cover" / "grsai-solo-batch.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def generate_cover(root: Path, article_dir: Path, batch_path: Path, prompt: str) -> Path:
    api_key = resolve_grsai_api_key()
    if not api_key:
        raise RuntimeError("GRSAI_API_KEY missing — cover i2i BLOCKER")
    ref_path = ensure_face_reference(root)
    image_input = {"prompt": prompt, "aspect_ratio": "16:9", "resolution": "1K"}
    timeout = max(MIN_TIMEOUT_SECONDS, DEFAULT_TIMEOUT_SECONDS)
    image_bytes, _meta = generate_image(
        root=root,
        batch_path=batch_path,
        image_input=image_input,
        api_key=api_key,
        model=model_tier_standard(),
        quality=default_quality(),
        target_size=SOLO_COVER_SIZE,
        timeout=timeout,
        hosts=resolve_hosts(),
        max_retries=1,
        retry_wait=5,
        ref_path=ref_path,
    )
    cover_path = article_dir / "cover.png"
    cover_path.write_bytes(image_bytes)
    return cover_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--post-id", type=int, default=0)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--output-root", default="memory/blog/cover-regen")
    args = ap.parse_args()

    items = COVER_REGEN_MANIFEST
    if args.post_id:
        items = [r for r in items if int(r["post_id"]) == args.post_id]
        if not items:
            print(f"FAIL unknown post_id={args.post_id}", file=sys.stderr)
            return 2

    root = project_root()
    try:
        ensure_face_reference(root)
    except FileNotFoundError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2

    plan: list[dict[str, Any]] = []
    failures = 0

    for item in items:
        post_id = int(item["post_id"])
        slug = str(item["slug"])
        article_dir = root / args.output_root / f"{post_id}-{slug}"
        article_dir.mkdir(parents=True, exist_ok=True)
        prompt = build_solo_prompt(item)
        (article_dir / "cover-prompt.txt").write_text(prompt + "\n", encoding="utf-8")
        batch_path = write_batch(article_dir, prompt)

        entry: dict[str, Any] = {"post_id": post_id, "slug": slug, "hook": item["hook"]}

        if args.dry_run:
            entry["status"] = "dry_run"
            plan.append(entry)
            print(f"DRY post_id={post_id}")
            continue

        try:
            cover_path = generate_cover(root, article_dir, batch_path, prompt)
            entry.update(
                {
                    "status": "generated",
                    "cover_path": str(cover_path.relative_to(root)),
                    "alt_text": f"Святослав Шакин — {item['hook']}",
                    "provider": "grsai-i2i",
                }
            )
            print(f"OK generated post_id={post_id} -> {cover_path}")
        except Exception as exc:  # noqa: BLE001
            entry["status"] = "fail"
            entry["error"] = str(exc)
            failures += 1
            print(f"FAIL post_id={post_id}: {exc}", file=sys.stderr)

        plan.append(entry)
        if not args.all and args.post_id:
            break
        if args.all and item != items[-1]:
            time.sleep(5)

    plan_path = root / args.output_root / "regen-plan-new.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK plan={plan_path} failures={failures}/{len(plan)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
