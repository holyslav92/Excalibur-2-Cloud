---
name: cover-qa-excalibur-blog
description: "Cover-QA: visual gate after Cover, before Indexer/Publish; stamp cover_qa.json."
---

# Cover-QA — visual gate (после Cover)

## Когда

**После** `excalibur-blog-cover` (8 PNG готовы, inject в `article.html`).  
**До** Indexer и Publish.

FAIL → **вернуть Cover** (не Indexer/Publish).

**Quality bar 9/10:** `shared/quality-bar-9.md` — phone on cover, Wordstat stickers не на title, inline utility, comparison columns differ. После PASS + `quality-bar-9.json` → Publish.

**Panel-only regen (default):** не перегенерировать оба canvas целиком. Только failed slots:

```bash
python3 scripts/excalibur_blog_quad_regen_panels.py \
  --article-dir "$ARTICLE" \
  --slots inline_2,inline_3 \
  --inject-html
```

Cover slot → solo i2i; inline → utility t2i. Derouter primary, Kie после 524/quota.
Сохранить approved cover: `quad_preserve_cover.py` если regen canvas-1 inlines.

## Что проверяешь (визуально + артефакты)

1. **Лицо + телосложение хоста** — тот же человек что `face-studio-2026-06-23.jpg` (кости, hairline, глаза, щетина, 28 лет); **medium slim**. FAIL: chubby, другой человек.
2. **Эмоция НЕ копия референса** — выражение под hook статьи (шок, side-eye, гримаса, недоумение «где деньги?»…). **FAIL** если вежливая студийная closed-mouth smile 1:1 как на reference. PASS если живая мимика под тему.
3. **Light / high-key** — светлая картинка, sun flare/glow; **нет** dark cinematic / low-key / twilight.
4. **Motif 14д** — нет коллизии с `memory/cover/used-motifs.json` (composition/location/meme…).
5. **Люди в 8-set** — host на cover = единственный крупный человек; inline people-memes только как маленькие стикеры из `meme-top100.json`.
6. **Meme canon (meme_canon_v1)** — только `memory/cover/meme-top100.json`: real top memes; people+cats variety (not cats-only); on-topic+funny; stickers ≤15% never on hook/face/phone; anti-repeat 14д в `used-motifs.json`.
7. **Коты** — meme-cat на cover/inline **или** недельная каденция не просела (не 3+ статей подряд без кота).
8. **Wordstat stickers** — 1–3 читаемых стикера с live P0-фразами (из `quad-manifest.json` → `wordstat_stickers`).
9. **identity-real** — 4 live-файла на месте.
10. **Inline utility (все 7)** — каждый inline проходит тест пользы: факт/порядок/число/сравнение по H2; не ряд иконок+3 слова; не host face.
11. **inline_no_host_face** — ни на одном inline нет лица Святослава / identity-real.
12. **inline_no_co_host_human** — нет stock model / generated man / handsome realtor / large meme person как co-host или presenter на inline.
13. **inline_meme_sticker_scale** — если мем-человек на inline, он ≤15% кадра, угол/край, не герой.
14. **meme_people_real_catalog** — people-memes из `memory/cover/meme-top100.json`, не выдуманные лица.
15. **meme_variety_not_cats_only** — `meme_picks` содержит ≥1 people-meme когда есть cat-memes.
16. **meme_on_topic** — `meme_picks` / `cover_motifs.meme` соответствуют hook (не random wallpaper).
17. **meme_sacred_zones** — pixel: hook title, face, phone readable; meme не перекрывает (clearance 80px).

Канон: `memory/cover/cover-canon.json`.

## Выход: `cover/cover_qa.json`

```json
{
  "agent": "excalibur-blog-cover-qa",
  "status": "PASS",
  "checked_at": "2026-08-18",
  "topic_id": "B01",
  "checks": {
    "identity_face_28yo": true,
    "identity_body_medium_slim": true,
    "identity_expression_invented": true,
    "title_not_occluded": true,
    "outfit_invented": true,
    "action_invented": true,
    "emotion_not_copied_from_recent_covers": true,
    "cover_phone_readable": true,
    "motif_no_collision_14d": true,
    "people_in_8_set": true,
    "cats_cadence_ok": true,
    "wordstat_stickers_1_3": true,
    "identity_real_files": true,
    "inline_utility_all_7": true,
    "inline_no_host_face": true,
    "inline_no_co_host_human": true,
    "inline_meme_sticker_scale": true,
    "meme_people_real_catalog": true,
    "meme_variety_not_cats_only": true
  },
  "notes": "кратко: что смотрел"
}
```

При FAIL — `status: FAIL`, перечисли checks=false и **не** пускай дальше.

## Gate (shell)

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
# или Fixer loop (overlay/regen → re-QA bytes):
python3 scripts/excalibur_blog_cover_fixer.py --article-dir "$ARTICLE"
```

Gate читает **PNG bytes** (`cover_qa_pixels.py`), пишет `cover_qa.json` с `pixel_qa=true` и `cover_md5`. Publish блокируется без PASS + md5 match.

**OCR false-positive escape (B08/B09/B13):** если на PNG есть лицо + кириллический hook + **phone zone ink** (`pixel_phone_zone_present`), а падают только OCR flakes (truncation, clipping, opaque Wordstat bars, collage inset, designed_thumbnail) — `apply_ocr_false_positive_escape` даёт PASS без PIL mashup/Kie. Полный OCR телефона (`pixel_phone_readable`) — flaky, не блокирует escape при достаточном ink.

**Cover budget:** solo regen max **2** attempts (`EXCALIBUR_COVER_MAX_ATTEMPTS`); после бюджета — `cover-budget-result.json`, не бесконечный loop. Дирижёр: ≤15–20 мин на cover, не копать pixel source.

Только `OK cover QA stamp` → Indexer/Publish.

## Blockers

- COVER QA BLOCKER — любой check false
- identity-real missing
- dark cinematic / wrong face / reference smile clone → return Cover

Agent: `agents/excalibur-blog-cover-qa.md`
