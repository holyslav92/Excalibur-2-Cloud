#!/usr/bin/env python3
"""Перегенерация только cover для live-постов (grsai standard, face i2i).

Модель: grsai GPT Image 2 standard (НЕ VIP). FACE: face-studio-2026-06-23.jpg.
После генерации — upload-plan.json для wordpress_upload_image_from_url.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

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
from excalibur_blog_site_base import expand_site_base, resolve_public_base_from_env

DEFAULT_REF = Path("memory/cover/assets/identity-real/face-studio-2026-06-23.jpg")
IDENTITY_PUBLIC_PATH = "/wp-content/uploads/2026/06/2026-06-23-15.57.42.jpg"
SOLO_COVER_SIZE = "1200x675"
COVER_PHONE = "+7 922 001 65 05"

BODY_LOCK = (
    "medium slim build (NOT chubby/puffy/thick neck); blazer or smart-casual invented per hook"
)
I2I_EXPRESSION_LOCK = (
    "same person identity from reference photo — NEW invented expression for hook; "
    "do NOT copy reference studio smile/pose; preserve jaw/stubble/hairline/eyes"
)
IDENTITY_SUFFIX = (
    "\nIDENTITY LOCK (mandatory): exact same man as reference photo — "
    "28 years old, medium-slim build, round-oval face, dark brown short hair tapered sides, "
    "warm dark brown eyes, full dark brows. "
    "MANDATORY visible dark five-o'clock-shadow stubble on jaw, chin and upper lip — "
    "same density and pattern as reference; NEVER clean-shaven, NEVER fashion-model jaw. "
    "Bone structure, hairline, stubble pattern, eye shape MUST match studio portrait. "
    "Black blazer over black tee like reference when outfit not specified. "
    "NEW invented emotion/scene — do NOT clone reference studio smile/pose/background."
)

COVER_REGEN_MANIFEST: list[dict[str, Any]] = [
    {"post_id": 9627, "slug": "v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi", "hook": "Банк поднял ставку — платёж вырос", "highlight": "платёж", "sticky": "Одобрение не гарантия", "emotion": "shocked at calculator", "scene": "bright office, mortgage papers, calculator higher payment"},
    {"post_id": 9601, "slug": "v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela-za-tri-dnya-d", "hook": "Банк снял ипотеку перед сделкой", "highlight": "снял", "sticky": "Бронь уже не спасти", "emotion": "panicked disbelief", "scene": "bank corridor, revoked approval, 72h countdown"},
    {"post_id": 9588, "slug": "v-tyumeni-na-pokaze-byla-chistovaya-v-ddu-okazalas-predchistovaya", "hook": "В шоу-руме чистовая — в ДДУ предчистовая", "highlight": "чистовая", "sticky": "Приложение решает, не витрина", "emotion": "confused comparing finishes", "scene": "showroom laminate vs bare concrete walls"},
    {"post_id": 9575, "slug": "v-tyumeni-zastrojschik-zaderzhal-klyuchi-na-8-mesyacev-neustojku-predlozhili-ser", "hook": "Задержка ключей — сертификат вместо денег", "highlight": "сертификат", "sticky": "Сначала подпись — потом ключи", "emotion": "frustrated with certificate", "scene": "keys and certificate instead of cash"},
    {"post_id": 9562, "slug": "v-tyumeni-ploschad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry", "hook": "В квартире пропали два метра", "highlight": "пропали", "sticky": "Это не допуск", "emotion": "skeptical at laser measure", "scene": "empty new apartment, floor plan mismatch"},
    {"post_id": 9549, "slug": "v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo", "hook": "Кладовка по ДДУ исчезла на ключах", "highlight": "исчезла", "sticky": "Акт подписывать страшно", "emotion": "angry at empty storage door", "scene": "basement storage missing, keys and contract"},
    {"post_id": 9536, "slug": "v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok", "hook": "Застройщик хочет ПОДНЯТЬ остаток перед ключами", "highlight": "ПОДНЯТЬ", "sticky": "Не подписывайте с ходу", "emotion": "alarmed at +400000 balance", "scene": "installment papers surprise top-up"},
    {"post_id": 9523, "slug": "v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli", "hook": "У забора пусто — ключи не взяли", "highlight": "пусто", "sticky": "Акт не подписали", "emotion": "bewildered outdoors at empty utilities", "scene": "cottage fence, no gas/water hookups"},
    {"post_id": 9510, "slug": "v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat", "hook": "Оплатили переуступку — дольщиком не стали", "highlight": "дольщиком", "sticky": "Оплата не даёт права", "emotion": "firm stop gesture worried", "scene": "assignment contract desk, mini building model"},
    {"post_id": 9490, "slug": "v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot", "hook": "Застройщик сменил компанию — бронь зависла", "highlight": "компанию", "sticky": "Вывеска прежняя, бумаги другие", "emotion": "stressed checking phone escrow blocked", "scene": "new legal entity papers, escrow delay"},
    {"post_id": 9465, "slug": "v-tyumeni-zabronirovali-novostrojku-cherez-dvoe-sutok-cenu-podnyali-na-380-tysya", "hook": "Бронь квартиры не сохранила прежнюю цену", "highlight": "цену", "sticky": "Вот тебе и бронь", "emotion": "angry at +380000 calculator", "scene": "reservation papers, price jump weekend"},
    {"post_id": 9452, "slug": "semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli", "hook": "Ипотеку одобрили — бронь всё равно сняли", "highlight": "сняли", "sticky": "Проверка была впереди", "emotion": "shocked holding БРОНЬ СНЯТА stamp", "scene": "approval card cancelled, maternity capital check"},
    {"post_id": 9368, "slug": "v-tyumeni-poddelnoe-soglasie-suprugi-ostanovilo-sdelku-pered-avansom", "hook": "Проверка согласия супруги остановила аванс", "highlight": "остановила", "sticky": "Конверт не доказательство", "emotion": "suspicious examining envelope", "scene": "notarized consent envelope paused deal"},
    {"post_id": 9332, "slug": "v-tyumeni-kupili-dolyu-v-kommunalnoj-kvartire-sosed-sorval-sdelku-za-den-do-avan", "hook": "Сосед остановил покупку доли до аванса", "highlight": "остановил", "sticky": "Деньги не ушли зря", "emotion": "worried with neighbor refusal", "scene": "communal share papers, refusal envelope"},
    {"post_id": 9300, "slug": "v-tyumeni-obeschali-kladovku-v-podarok-v-vypiske-egrn-ee-ne-okazalos", "hook": "Кладовка остановила сделку до аванса", "highlight": "остановила", "sticky": "Словам верить нельзя", "emotion": "alert at EGRN mismatch", "scene": "EGRN extract, promised storage missing"},
    {"post_id": 9250, "slug": "zastrojschik-perenes-sroki-sdachi-zhk-v-tyumeni-na-god-ipoteka-ostalas", "hook": "Застройщик перенёс ключи — платёж идёт", "highlight": "перенёс", "sticky": "Год без квартиры", "emotion": "exhausted at delay notice", "scene": "handover delay letter, mortgage still due"},
]


def identity_public_url() -> str:
    live = resolve_public_base_from_env()
    placeholder = f"{{{{SITE_BASE}}}}{IDENTITY_PUBLIC_PATH}"
    if live:
        return expand_site_base(placeholder, live)
    return placeholder


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
    bans = (
        "BAN HARD: ANY text on clothes/chest; Wordstat/search strips; blue halos on hair; "
        "generic stock-model face; different person than reference; mustard+navy vest repeat; "
        "dark cinematic; chubby host; polite studio smile copy from reference."
    )
    return (
        f"{style_prefix}\n"
        "ONE SINGLE 16:9 cover frame 1200x675 — NOT a 2x2 grid, NOT quad canvas.\n"
        f"{bans}\n"
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


def write_batch(article_dir: Path, prompt: str, root: Path) -> Path:
    batch = {
        "pipeline": "grsai_solo_cover_regen",
        "prefer_local_reference": True,
        "local_reference": str(DEFAULT_REF),
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
        raise RuntimeError("GRSAI_API_KEY missing")
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
        ref_path=root / DEFAULT_REF,
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
    if not (root / DEFAULT_REF).is_file():
        print(f"FAIL missing {DEFAULT_REF}", file=sys.stderr)
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
        batch_path = write_batch(article_dir, prompt, root)

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

    plan_path = root / args.output_root / "regen-plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK plan={plan_path} failures={failures}/{len(plan)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
