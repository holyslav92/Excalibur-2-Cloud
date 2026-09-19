# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени в проектной декларации земля под ЖК в аренде — в брони обещали собственность
- hook (cover-text): «Обещали собственность — показали аренду» (highlight: «аренду»)
- sticky: «Переоформим потом?»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: офис продаж обещает «участок в собственности» → бронь 150 000 ₽ → за 4 дня до ДДУ вечером открыли ЕИСЖС → раздел 12: аренда до 2049, другой собственник → «подпишите ДДУ, переоформим потом» → отказ → бронь отменили, 150 000 вернули за 12 дней

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4446
- «купить новостройку в тюмени» — 1936
- «проектная декларация застройщика» — 25

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, this_is_fine_dog
- inline_1: wojak
- inline_5: sacrednik_priest
- inline_7: capybara_indifference

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: bank mortgage desk olive vest hide_pain_harold waist-up right
- B25: kneeling empty apartment tape measure confused_math_lady
- B23: newbuild handover side_eye_chloe full-body right
- B22: bank desk lemon shirt full-body center

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + this_is_fine_dog small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (evening home desk with ЕИСЖС / bright sales office with declaration contrast — NOT bank desk duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Участок наш, в собственности» — так сказали в офисе продаж (pair with inline_2)
Labels: Офис продаж | Семейная ипотека | Бронь 150 тысяч | Участок в собственности | Не юридическая проверка
Meme: wojak tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Четыре дня до ДДУ | ЕИСЖС вечером | Наш дом точка рф | Конкретный корпус | Раздел двенадцать
NO meme — table: офис «собственность» vs декларация «аренда»

### inline_3 — realistic_photo — За четыре дня до ДДУ: вечером открыли проектную декларацию
Labels: Бронь отменили | Сто пятьдесят тысяч | Вернули за двенадцать дней | Деньги не на эскроу | Соглашение о брони
NO meme — evening laptop ЕИСЖС section 12 glow

### inline_4 — realistic_photo — В разделе 12 — аренда до 2049, а не собственность застройщика
Labels: Аренда до 2049 | Государственный участок | Не собственность | Другой собственник | Зарегистрированное право
NO meme — tablet zoom on section 12 lease dates

### inline_5 — process_flow — «Подпишите ДДУ, землю переоформим потом» — покупатели отказались
Labels: Переоформим потом | ДДУ не подписали | Эскроу не открыли | Слова не совпали | Пауза до аванса
Meme: sacrednik_priest tiny corner

### inline_6 — bar_timeline_chart — Бронь отменили, сто пятьдесят тысяч вернули через двенадцать дней
Labels: Вид права 12.1.1 | Реквизиты договора | Срок окончания аренды | Собственник участка | Кадастровый номер
NO meme — bar chart section 12 fields checklist

### inline_7 — structure_diagram — Раздел 12 до подписи — таблица: что сверить по земле
Labels: Декларация до аванса | Слова и документы | Письменное объяснение | Пауза до перевода | Вопросы до эскроу
Meme: capybara_indifference tiny corner

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
