# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за 48 часов до эскроу семья сверила бронь с ДДУ — и отказалась от другой квартиры
- hook (cover-text): «Бронь обещала набережную — ДДУ показал другое» (highlight: «другое»)
- sticky: «Проверили до подписи»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: платная бронь зафиксировала этаж с видом на набережную; за 48 часов до сделки в проекте ДДУ — другая секция, этаж ниже, окна во двор; семья остановила сделку, на эскроу 0 ₽

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3536
- «купить новостройку в тюмени» — 683
- «новостройки в тюмени от застройщика» — 500

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в ранних обложках.

**Recent covers to differ from:**
- B26: bank mortgage desk olive vest hide_pain_harold waist-up right
- B25: empty apartment kneeling tape measure confused_math_lady
- B23: handover room full-body right blue shirt mustard sweater
- B22: yellow shirt bank desk disaster_girl full-body center

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom/handover duplicate; NEW location (bright developer sales lounge with panoramic window mockup of embankment view vs floor plan table showing courtyard-facing unit mismatch).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — В приложении — другая секция, этаж ниже, окна во двор (pair with inline_2)
Labels: Лист бронирования | Секция и этаж | Вид на набережную | Ипотека одобрена | Бронь не ДДУ
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: 48 часов до сделки | Проект ДДУ | Другая секция | Этаж на два ниже | Окна во двор
NO meme

### inline_3 — realistic_photo — «Аналогичная» квартира без того вида, ради которого выбирали
Labels: Приложение к ДДУ | Поэтажный план | Секция не совпала | Этаж ниже | Не опечатка
NO meme — bright DDU appendix with floor plan highlighting wrong section

### inline_4 — realistic_photo — Платная бронь — и семья уверена: этаж, секция, вид на набережную
Labels: «Аналогичная» квартира | Вид на набережную | Письменная фиксация | Переписка с менеджером | До подписания
NO meme — booking sheet and chat printout on bright desk with river view photo

### inline_5 — process_flow — За 48 часов до подписания прислали проект ДДУ
Labels: ДДУ не подписан | На эскроу 0 ₽ | Ипотека не использована | Плата за бронь | Сделку остановили
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Сверили бронь с ДДУ — и отказались: на эскроу 0 ₽
Labels: Корпус и очередь | Секция и подъезд | Номер объекта | Окна и сторона | Цена и эскроу
NO meme

### inline_7 — structure_diagram — Что сопоставить в проекте ДДУ — таблица бронь против приложения
Labels: Исправленный проект | Старые версии файлов | наш.дом.рф | Плата за бронь | До эскроу
Meme: wojak tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
