# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей
- hook (cover-text): «Застройщик обещал больше, чем намерили» (highlight: «больше»)
- sticky: «Ключи не отдали»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья купила дом в коттеджном посёлке; в договоре 12 соток, межевание 9,7 → переплата ~850 тыс., ключи не выдали, эскроу заморожено

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «коттеджные поселки тюмень» — 1566
- «новостройки тюмень» — 3640
- «участок в коттеджном поселке» — 52

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling tape measure apartment
- B23: light blue shirt mustard sweater handover room
- B22: yellow shirt bank desk full-body center

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NEW location — bright cottage settlement sales pavilion / plot model with land survey mismatch (NOT bank/MFC/apartment).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «На презентации — двенадцать соток и дом под ключ» (pair with inline_2)
Labels: Двенадцать соток | Дом под ключ | Схема участка | Счёт эскроу | Земля в покупке
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Три дня до акта | Межевой план 9,7 | Уточнённая площадь | Дом готов | Ключи близко
NO meme

### inline_3 — realistic_photo — «Что сверять до ключей — таблица договор, декларация, межевание»
Labels: Минус 2,3 сотки | Девятнадцать процентов | Почти пятая часть | Дом не уменьшился | Порог десять процентов
NO meme — bright checklist documents on table

### inline_4 — realistic_photo — «За три дня до акта: межевой план с «уточнённой» площадью 9,7»
Labels: Доплата за соседний | Принять без пересчёта | Письменный ответ | Оформить границу | Оговорка опасна
NO meme — survey plan on bright desk with 9.7 highlighted

### inline_5 — process_flow — «Две с половиной сотки — это не «копейки», а почти пятая часть участка»
Labels: Акт не подписан | Претензия застройщику | Деньги на эскроу | Аренда продолжается | Независимое межевание
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — ««Доплатите за соседний кусок» или подпишите как есть»
Labels: Договор и схема | Проектная декларация | Планировка территории | Межевой план | ЕГРН и акт
NO meme

### inline_7 — structure_diagram — «Акт не подписали: деньги на эскроу, аренда и платежи не останавливаются»
Labels: Сверка до ключей | Площадь в договоре | Независимая съёмка | Письменное объяснение | До оплаты
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
