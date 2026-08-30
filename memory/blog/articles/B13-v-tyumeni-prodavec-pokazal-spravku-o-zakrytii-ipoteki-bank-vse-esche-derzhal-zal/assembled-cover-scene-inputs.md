# Cover-scene inputs — B13

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B13
- tenant: The Риэлтор, Тюмень
- H1: Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени
- hook (cover-text): «Справка есть — залог остался в реестре» (highlight: «залог»)
- sticky: «Проверили до аванса»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: продавец показал справку о погашении кредита; за 48 часов до аванса свежая выписка ЕГРН показала действующую ипотеку; банк не подтвердил срок снятия залога; аванс не внесли, ушли на другую квартиру

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить квартиру в тюмени вторичка» — 4165
- «выписка из егрн на квартиру» — 92
- «снятие обременения с квартиры» — 31

## meme_picks (from cover-text.json)

- cover: two_buttons, grumpy_cat
- inline_1: side_eye_chloe
- inline_5: surprised_pikachu
- inline_7: pepe_frog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B12: light blue shirt waist right showroom letter+calendar
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window

**Required:** light/bright #FFF high-key, sun flare; two_buttons people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B12 showroom letter payment; B10 apartment viewing phone; B06 panoramic window price chart; B05 entrance discount tag.

## Inline slots (from quad-manifest visual types)

### inline_1 — realistic_photo (pair) — «Финал: сделку остановили, ушли на другую квартиру»
Labels: За 48 часов | Справка о погашении | Ипотека в выписке | Звонок в банк | До 4 недель
Meme: side_eye_chloe tiny corner. NO host face — realistic table with two papers.

### inline_2 — comparison_table (pair) — «Финал: сделку остановили, ушли на другую квартиру»
Labels: Кредит закрыт | Запись в ЕГРН | Справка не реестр | Раздел обременений | Свежая выписка
NO meme

### inline_3 — realistic_photo — «За два дня до аванса справку приняли — выписка сказала другое»
Labels: Обещание не документ | Банк запускает процедуру | Нет согласия банка | Аванс за намерение | Срок не подтвердили
NO meme — bright apartment viewing or document on table, Tyumen context

### inline_4 — realistic_photo — «Снимем обременение в день сделки» — обещание без гарантии»
Labels: Две бумаги | Справка честная | Ипотека в выписке | Аванс не внесли | Другая квартира
NO meme

### inline_5 — process_flow — «Кредит закрыт и залог в реестре — это не одно и то же»
Labels: Статья 37 | Согласие банка | Статья 25 | Три рабочих дня | После заявления
Meme: surprised_pikachu tiny corner

### inline_6 — structure_diagram — «Закон: согласие банка и три рабочих дня после заявления»
Labels: Автоматика банка | До 30 дней | Два рабочих дня | Проверка в ЕГРН | Сроки не совпали
NO meme

### inline_7 — bar_timeline_chart — «Автоматика банка и срок до 30 дней — не ваш календарь сделки»
Labels: Справка: долг нулевой | ЕГРН: залог есть | Разные даты | Разные вопросы | Проверить до аванса
Meme: pepe_frog tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": {
    "composition": "...",
    "location": "...",
    "meme": "...",
    "prop_set": "...",
    "sticker_set": "...",
    "joke": "...",
    "outfit": "...",
    "emotion": "...",
    "pose_framing": "...",
    "action": "..."
  },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint": "...", "alt": "...", "cover_emotion": "..." },
    "inline_1": { "scene_hint": "...", "alt": "..." },
    "inline_2": { "scene_hint": "...", "alt": "..." },
    "inline_3": { "scene_hint": "...", "alt": "..." },
    "inline_4": { "scene_hint": "...", "alt": "..." },
    "inline_5": { "scene_hint": "...", "alt": "..." },
    "inline_6": { "scene_hint": "...", "alt": "..." },
    "inline_7": { "scene_hint": "...", "alt": "..." }
  }
}
```

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «залог», ONE yellow sticky only, ZERO Wordstat strips on canvas.
