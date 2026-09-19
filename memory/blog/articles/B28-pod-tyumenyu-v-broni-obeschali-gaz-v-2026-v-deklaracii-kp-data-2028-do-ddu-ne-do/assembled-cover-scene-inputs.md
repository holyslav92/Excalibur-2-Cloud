# Cover-scene inputs — B28

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B28
- tenant: The Риэлтор, Тюмень
- H1: Под Тюменью в брони обещали газ в 2026 — в декларации КП дата 2028 до ДДУ не дошли
- hook (cover-text): «Обещали газ в брони декларация сдвинула срок» (highlight: «декларация»)
- sticky: «Газ к 2026?»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: готовый дом в КП под Тюменью, бронь 200 000 ₽, в офисе/брони «газ к 2026» → за 6 дней до ДДУ вечером ЕИСЖС → раздел сетей: газ IV кв. 2028 → «подпишите ДДУ, внутренний график раньше» → отказ → вернули 140 000, удержали 60 000, эскроу не открыли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4430
- «коттеджные поселки тюмень» — 1455
- «проектная декларация застройщика» — 25

## meme_picks (from cover-text.json)

- cover: roll_safe, grumpy_cat
- inline_1: side_eye_chloe
- inline_5: two_buttons
- inline_7: blinking_white_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B27: sales office terracotta overshirt declaration section 12 disappointed_black_guy
- B26: bank mortgage desk olive vest hide_pain_harold
- B25: kneeling empty apartment tape measure

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright cottage KP sales pavilion with gas pipe mockup / ready house facade — NOT sales office duplicate from B27, NOT bank desk).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Газ к 2026» — так звучало в бронировании и в офисе (pair with inline_2)
Labels: Газ к 2026 | Дом готов | Бронь двести тысяч | Коттеджный посёлок | Два ребёнка
Meme: side_eye_chloe tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Шесть дней до ДДУ | ЕИСЖС вечером | Дом точка рф | Раздел о сетях | До эскроу
NO meme — table: бронь/офис «газ 2026» vs декларация «IV кв. 2028»

### inline_3 — realistic_photo — За шесть дней до ДДУ: вечером открыли проектную декларацию
Labels: Четвёртый квартал 2028 | Не 2026 | ТУ не подключение | Временное отопление | Два ребёнка
NO meme — evening laptop ЕИСЖС networks section glow

### inline_4 — realistic_photo — В разделе о сетях — газопровод в IV квартале 2028, не в 2026
Labels: Подпишите ДДУ | Внутренний график | Семья сказала нет | Письменный запрос | Три уровня обещаний
NO meme — tablet zoom gas network row 2028

### inline_5 — bar_timeline_chart — «Подпишите ДДУ, по внутреннему графику раньше» — семья сказала нет
Labels: Вернули сто сорок | Удержали шестьдесят | Эскроу не открыли | ДДУ не подписали | Резерв лота
Meme: two_buttons tiny corner

### inline_6 — process_flow — Из двухсот тысяч брони вернули сто сорок — эскроу так и не открыли
Labels: Раздел четырнадцать | Строка газоснабжения | Номер и дата ТУ | Срок действия ТУ | Плата подключения
NO meme — flow: бронь → возврат 140k / удержание 60k → no escrow

### inline_7 — structure_diagram — Раздел 14 до подписи — что сверить по газу и инженерным сетям
Labels: Пауза до аванса | Сценарий отопления | Миллионы не ушли | Документы не слова | Вопрос до эскроу
Meme: blinking_white_guy tiny corner

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
