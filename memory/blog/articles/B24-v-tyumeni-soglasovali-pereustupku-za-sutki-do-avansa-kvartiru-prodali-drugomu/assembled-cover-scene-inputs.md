# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса
- hook (cover-text): «Согласовали квартиру — забрали за сутки» (highlight: «забрали»)
- sticky: «Согласие ещё не бронь»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: письменное согласие застройщика на переуступку создало ощущение готовой сделки, но без резерва лота квартиру закрепили за другим покупателем за сутки до аванса

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «переуступка новостройки» — 16 (Tyumen)
- «новостройки тюмень» — 4583
- «переуступка квартиры» — demand anchor

## meme_picks (from cover-text.json)

- cover: james_doakes, long_cat
- inline_1: disappointed_black_guy
- inline_5: confused_math_lady
- inline_7: this_is_fine_dog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room full-body right side_eye_chloe
- B22: lemon yellow shirt bank mortgage desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; james_doakes people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/handover duplicate; NEW location (bright developer sales pavilion with assignment consent letter, apartment plan marked SOLD, countdown to advance payment).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Застройщик согласовал схему, но квартиру никто не резервировал (pair with inline_2)
Labels: Квартира по переуступке | Права по ДДУ | Задаток уступщику | Ипотека одобрена
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Письменное согласие | Резерва лота нет | Согласие не бронь | Ипотеку готовили
NO meme — two columns: consent YES vs reserve NO

### inline_3 — realistic_photo — Три разных «да» на переуступке
Labels: Звонок за сутки | Квартира уже чужая | Бронь прошли быстрее | Аванс на завтра
NO meme — bright sales office phone on desk with red SOLD stamp on plan

### inline_4 — realistic_photo — Переуступку нашли в строящем ЖК
Labels: Задаток вернули | Аванс не переводили | Планировка ушла | Одобрение ограничено сроком
NO meme — construction site showroom with floor plan wall, no people faces

### inline_5 — process_flow — За сутки до аванса менеджер позвонил
Labels: Согласие застройщика | Внутренняя бронь | Регистрация в ЕГРН | Этапы не заменяют
Meme: confused_math_lady tiny corner

### inline_6 — bar_timeline_chart — Планировка ушла: задаток вернули
Labels: Согласие застройщика | Бронь со сроком | Запись в ЕГРН | Аккредитив после регистрации | Проверить уступщика
NO meme

### inline_7 — structure_diagram — Что проверить до аванса по переуступке
Labels: Письменный резерв | Срок до цессии | Обязательства уступщика | Сначала бронь | Потом деньги
Meme: this_is_fine_dog tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    "inline_5": { "scene_hint", "alt", "meme_picks" },
    "inline_7": { "scene_hint", "alt", "meme_picks" }
  }
}
```
