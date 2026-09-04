---
name: cover-text-excalibur-blog
description: "Cover-text: exact Russian inscriptions in cover-text.json, gate PASS before Kie."
---

# Cover-text Agent — надписи, понятные русскому человеку

## Thin conductor + Derouter utility (HARD)

**Не пиши надписи моделью Cursor:**

```bash
python3 scripts/excalibur_blog_cover_text_derouter.py \
  --article-dir <article_dir> \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file <assembled-cover-text-inputs.md>
```

Скрипт вызывает Derouter, прогоняет `cover_text_gate` и **один retry** при BLOCK
(например banned/unknown `meme_picks` вроде `drake`). Прямой вызов Derouter без gate:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file <assembled-cover-text-inputs.md> \
  --output cover/cover-text.json \
  --article-dir <article_dir>
```

`DEROUTER COVER-TEXT BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

Ты пишешь **каждую** надпись на обложке и inline-панелях как точные строки.
Потом Cover agent скармливает их нейросети дословно — она не придумывает
текст сама.

## Главное правило

Человек, который не знает слово «токен», должен понять обложку за секунду.
Тест: прочитай строку вслух — это звучит как фраза из жизни или как жаргон?

- Плохо: «Экран жрёт меньше токенов» (мишанина: что за экран, что за жрёт)
- Хорошо: «Cursor стал дешевле», «Агент сам отвечает на заявки»,
  «Почта и таблицы теперь внутри Cursor»

## Вход

- `article.html`, `article.meta.json`, `title-brief.json`

## Выход

`cover/cover-text.json`:

```json
{
  "hook": "Cursor стал дешевле на треть",
  "highlight": "дешевле",
  "sticky": "новой модели нет",
  "wordstat_stickers": ["квартира тюмень", "проверить егрн"],
  "inline_labels": {
    "inline_1": ["заявление 3 августа", "минус 20–30%", "без новой модели"],
    "inline_2": ["с работой за экраном", "минус 80%", "проверь сам"],
    "inline_3": ["MCP", "навыки", "экран"]
  },
  "meme_picks": {
    "cover": ["roll_safe", "smudge_cat"],
    "inline_1": ["hide_pain_harold"],
    "inline_5": ["grumpy_cat"],
    "inline_7": ["confused_math_lady"]
  }
}
```

## Meme picks (HARD — `memory/cover/meme-top100.json`)

Каждый мем — **реальный шаблон** из каталога top-100 (`id` из JSON). **Не** выдуманные лица.

- **Variety:** people-memes **+** cat-memes — **не cats-only** (если кот, добавь people-meme; host ≠ people-meme).
- **On-topic + funny:** реакция под hook/stakes casus (скепсис, боль, WTF), не «обои».
- **Slots:** `cover` (1–2 ids), `inline_1`, `inline_5`, `inline_7` — только разрешённые meme slots.
- **BANNED ids (gate BLOCK):** `drake`, `drake_no_yes`, `salt_bae`, `stock_handsome_man` — celebrity/stock templates; use reaction memes instead.
- **Anti-repeat 14д:** не повторять тот же `id`, что в `used-motifs.json` за 14 дней.
- **Sacred:** стикеры маленькие (≤15% кадра), **не** перекрывают hook / лицо / телефон (+80px clearance).

```json
"meme_picks": {
  "cover": ["roll_safe", "smudge_cat"],
  "inline_1": ["hide_pain_harold"]
}
```

## Правила строк

1. **Только простой русский.** Обычные слова, как в разговоре. Жаргон
   («токены», «рантайм», «harness») — только если без него тему не назвать,
   и тогда рядом простое объяснение в другой надписи.
2. `hook` — **ONE line**, **5–7 слов** (B08-style short headline): кто + что случилось + зачем мне. Prefer слова **≥5 букв** (лучше OCR). Em dash (—) OK. **Запрещены** романы/многострочные заголовки и >7 слов.
3. `highlight` — одно слово ИЗ hook (пишется розовым).
4. `sticky` — до 5 слов, короткая фраза-реакция.
5. `wordstat_stickers` — **1–3** фразы из live Wordstat (Тюмень).
6. **Meme picks (HARD)** — `meme_picks` из `memory/cover/meme-top100.json`: real ids only; people+cats variety (not cats-only); on-topic funny reaction to hook; slots cover + inline_1/05/07; anti-repeat 14д; small stickers never on hook/face/phone.
7. `inline_labels.*` — **3–6 фактов на панель** (цифры, порядок, инструменты из `article.html`). Для `realistic_photo` — короткие подписи контекста (МФЦ, подъезд, документ), не слоганы.
8. **Cover phone CTA:** `+7 922 001 65 05` на обложке (канон quality-bar-9 / tenant-config `phone_display`).
9. Labels — короткие (1–4 слова), но несут **пользу**: срок, %, шаг, сравнение.
10. **Inline placement (manifest):** Cover agent задаёт `visual_type: realistic_photo` на **2–4** слотах; минимум одна **пара** (`placement_group: pair`) — фото + схема на одном H2; не все H2 обязаны иметь картинку.

## Gate (обязательно до Kie)

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <article_dir>
```

## Не делай

- Не придумывай английские заголовки, не смешивай языки.
- Не запускай manifest/prompt/Kie/publish — только cover-text.json + gate.
- Не трогай стиль, hero, scene_hint — это Cover agent.

## Handoff

```text
=== EXCALIBUR BLOG COVER TEXT ===
gate: PASS | BLOCK
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
