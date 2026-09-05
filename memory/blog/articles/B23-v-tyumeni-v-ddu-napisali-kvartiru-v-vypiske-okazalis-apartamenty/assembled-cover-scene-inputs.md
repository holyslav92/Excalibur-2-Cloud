# Cover-scene inputs — B23

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B23
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты
- hook (cover-text): «Выписка ЕГРН лишила семью ипотеки» (highlight: «ипотеки»)
- sticky: «Ключи не взяли»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: реклама и ДДУ — «квартира», приложение — нежилое, выписка ЕГРН подтвердила апартаменты → семейная ипотека на паузе → ключи не выдали → претензия

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3640
- «апартаменты тюмень» — 646
- «купить апартаменты» — 35

## meme_picks (from cover-text.json)

- cover: side_eye_chloe, pop_cat
- inline_1: james_doakes
- inline_5: confused_math_lady
- inline_7: sacrednik_priest

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B22: yellow shirt bank mortgage desk disaster_girl (full-body center)
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card
- B15: white shirt sand vest waist center envelope

**Required:** light/bright #FFF high-key, sun flare; side_eye_chloe people-meme + pop_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom duplicate; NEW location (bright handover/acceptance room at newbuild with EGRN extract vs DDU mismatch).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Квартира» в рекламе — и семья пошла за семейной ипотекой (pair with inline_2)
Labels: Север Тюмени | Слова «квартира» | Семейная ипотека | Двое детей | ЕГРН не подтвердил
Meme: james_doakes tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: В ДДУ — квартира | Приложение — нежилое | План в конце | Таблица характеристик | Читайте до подписи
NO meme

### inline_3 — realistic_photo — В ДДУ слово «квартира», а в приложении — другая строка
Labels: Дом уже сдан | Выписка через две недели | Нежилое назначение | В рекламе — квартира | Строка не меняется
NO meme — bright DDU appendix page with conflicting designation line

### inline_4 — realistic_photo — Через три недели после регистрации выписка ударила по ипотеке
Labels: Приложение показали | Всё указано верно | Ипотека под жильё | Кредит на паузе | Деньги в эскроу
NO meme — EGRN printout on bright desk with paused mortgage stamp

### inline_5 — structure_diagram — Застройщик сказал «всё верно», банк остановил остаток
Labels: Акт не подписан | В акте — квартира | В выписке — нежилое | Претензия застройщику | Спор до суда
Meme: confused_math_lady tiny corner

### inline_6 — process_flow — Ключи не взяли: претензия и досудебный спор
Labels: Проектная декларация | Разрешение на ввод | Текст ДДУ | План в приложении | Выписка перед приёмкой
NO meme

### inline_7 — bar_timeline_chart — Что сверить в ДДУ до подписания — таблица
Labels: Наш.дом.рф | Назначение объекта | Красный флаг | Кредитный договор | Одна строка решает
Meme: sacrednik_priest tiny corner

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
