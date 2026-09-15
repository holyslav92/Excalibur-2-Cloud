# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за 9 дней до ДДУ подорожал прайс ЖК — до аванса не дошли
- hook (cover-text): «Квартира подорожала перед подписанием: денег не хватило» (highlight: «подорожала»)
- sticky: «Ипотеку ведь уже одобрили»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья забронировала лот по прайсу ЖК, получила одобрение ипотеки → за 9 дней до ДДУ застройщик обновил прайс (+480 тыс.) → одобренной суммы не хватило → банк не расширил кредит → отказ от ДДУ до аванса

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки Тюмени цены» — 38
- «прайс лист жк» — 22
- «ипотека на новостройку Тюмень» — 47

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: disappointed_black_guy
- inline_5: stonks
- inline_7: this_is_fine_dog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: bank mortgage desk olive vest hide_pain_harold
- B25: empty apartment kneeling tape measure confused_math_lady
- B22: bank rate letter full-body center disaster_girl
- B23: showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank desk duplicate; NEW location (bright developer sales office with laminated price wall / printed pricelist stand).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — pair with inline_2 — «Ипотеку одобрили» — семья забронировала лот
Labels: Расчёт по выбранному лоту | Плата за бронь внесена | Предварительное одобрение | Свой взнос посчитан | Одобрение ≠ фиксация цены
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1 — Между одобрением и ДДУ прайс может обновиться
Labels: Проверка объекта | Подготовка документов | Одобрение не фиксирует цену | Бронь отдельным договором | Ставка не менялась
NO meme — two-column: «одобрение банка» vs «прайс застройщика»

### inline_3 — realistic_photo — За 9 дней до подписания новый прайс +480 000 ₽
Labels: 9 дней до подписания | Квартира та же | Новый прайс застройщика | Плюс 480 000 ₽ | Новая цена в ДДУ
NO meme — bright sales desk with two pricelist versions dated 9 days apart

### inline_4 — realistic_photo — Пересчёт на кухне, доплаты не хватило
Labels: Пересчёт на кухне | Плюс 480 тысяч | Свободных накоплений нет | Бюджет под старую цену | На доплату не хватило
NO meme — kitchen table spreadsheet, calculator, no faces

### inline_5 — bar_timeline_chart — Одобренной суммы не хватило
Labels: Одобрение действует | Ставку не подняли | Кредит прежнего размера | Одобренной суммы не хватило | Доплата из своих денег
Meme: stonks tiny corner — bar chart old price vs new price gap 480k

### inline_6 — structure_diagram — Сделку остановили до аванса
Labels: Отказ от новой цены | До аванса не дошли | ДДУ не подписали | Эскроу не открыли | Плата за бронь внесена | Возврат по договору брони
NO meme — money flow blocks: бронь paid → ДДУ stop → эскроу empty

### inline_7 — process_flow — Что сверять до подписания
Labels: Прайс вашего лота | Текст договора брони | Последний проект ДДУ | Решение банка | Сверить даты и суммы
Meme: this_is_fine_dog tiny corner — numbered checklist flow

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
