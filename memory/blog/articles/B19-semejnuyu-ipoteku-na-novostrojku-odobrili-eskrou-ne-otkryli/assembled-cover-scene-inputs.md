# Cover-scene inputs — B19

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B19
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ипотеку одобрили — эскроу сорвал маткапитал
- hook (cover-text): «Ипотеку одобрили — бронь всё равно сняли» (highlight: «сняли»)
- sticky: «Проверка была впереди»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека на новостройку одобрена; прошлый маткапитал без детских долей — банк не открыл эскроу; бронь сняли за ~48 часов

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека тюмень» — 89
- «маткапитал на первоначальный взнос» — 156
- «эскроу счет новостройка» — 42

## meme_picks (from cover-text.json)

- cover: bad_luck_brian, grumpy_cat
- inline_1: disaster_girl
- inline_5: disappointed_black_guy
- inline_7: success_kid

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B15: white shirt sand vest waist center envelope
- B12: light blue shirt showroom waist right
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window

**Required:** light/bright #FFF high-key, sun flare; bad_luck_brian people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья пошла к ДДУ в новостройке
Labels: Семейная ипотека до 6% | Взнос от 20% | Лимит до 6 миллионов | Маткапитал во взнос | Одобрение не равно сделке
Meme: disaster_girl tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь у застройщика | Предварительное одобрение | Проверка банка | Регистрация договора | Бронь оплачивается отдельно
NO meme

### inline_3 — realistic_photo — Через 48 часов бронь сняли: эскроу так и не открыли
Labels: Срок брони вышел | Финальная проверка банка | Детских долей нет | Оформление остановили | Эскроу не открыли
NO meme — developer sales office countdown calendar

### inline_4 — realistic_photo — Почему банк копает прошлый маткапитал при новой семейной ипотеке
Labels: Закон 256-ФЗ | Доли всем детям | Обязанность осталась | Прошлое не списывается
NO meme — SFR certificate + old EGRN on bank desk

### inline_5 — process_flow — Детские доли: обязанность, которую нельзя «закрыть» новым законом
Labels: Заявление через банк | Сведения из СФР | ЕГРН прошлого жилья | Проверка детских долей | Оформление приостановят
Meme: disappointed_black_guy tiny corner

### inline_6 — bar_timeline_chart — Что сверять до брони и подписания ДДУ — таблица
Labels: ЕГРН прежней квартиры | Сведения из СФР | Документы для банка | Срок брони | Эскроу в договоре
NO meme

### inline_7 — structure_diagram — Эскроу, бронь и маткапитал: где ломается цепочка
Labels: Одобрение не выдача | Выдача не эскроу | Банк может остановиться | Деньги не ушли | Сначала документы
Meme: success_kid tiny corner (ironic — not success yet)

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
