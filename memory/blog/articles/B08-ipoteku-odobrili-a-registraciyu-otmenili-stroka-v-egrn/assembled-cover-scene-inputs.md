# Cover-scene inputs — B08

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B08
- tenant: The Риэлтор, Тюмень
- H1: Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию
- hook (cover-text): «Ипотека одобрена, а квартиру не зарегистрировали» (highlight: «зарегистрировали»)
- sticky: «Проверь выписку до аванса»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: банк одобрил ипотеку, но действующая запись об обременении в ЕГРН остановила регистрацию; покупатель отдал аванс, не проверив выписку

## Wordstat stickers (manifest log ONLY — FORBIDDEN on cover canvas)

- «выписка егрн квартира» — 246
- «егрн» — 7543
- «купить квартиру в тюмени» — 22880

**ZERO Wordstat query strips/bars on cover PNG.** Optional one yellow sticky from hook only.

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow shirt, host right, panoramic window price chart
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; NO Wordstat painted on canvas.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt right window.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Коротко: ипотеку одобрили — а регистрацию остановили»
Labels: Банк одобрил заёмщика | Обременение стопит сделку | Погасить до подачи | До трёх месяцев | Проверка до аванса
Meme sticker: yes (small grumpy cat corner)

### inline_2 — comparison_table_ui — «Сцена: покупатель в Тюмени дошёл до Росреестра»
Labels: Одобрение не чистота | Выписку пролистали | Закрыто только на словах | Аванс уже отдан | Стоп от регистратора
NO meme

### inline_3 — structure_diagram — «Что банк реально одобряет — и чего не видит в ЕГРН»
Labels: Банк смотрит заёмщика | Одобрение не регистрация | Залог после сделки | Опасна чужая запись
NO meme

### inline_4 — process_flow — «Какая строка в выписке рвёт сделку»
Labels: Раздел обременений | Статус действует | Долг закрыт не запись | Проверяй реестр | До аванса
NO meme

### inline_5 — workflow_diagram — «Ипотека продавца, арест, залог: записи разной природы»
Labels: Ипотека продавца | Арест снимают не сразу | Иные ограничения | Проверяем запись | Схема до аванса
Meme sticker: yes (small hide_pain_harold corner)

### inline_6 — bar_timeline_chart — «Финал: приостановка, три месяца и отказ в регистрации»
Labels: Статья 26 | Три месяца на снятие | Не сняли — отказ | Пошлина сгорает | Одобрение тикает
NO meme

### inline_7 — checklist_board — «Что смотреть в ЕГРН до аванса — по шагам»
Labels: Свежая выписка самому | Раздел ограничений | Основание записи | Подтверждение прекращения | Сверить собственников | Повторить перед подачей
Meme sticker: yes (small roll_safe corner)

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
  "slots": {
    "cover": {
      "scene_hint": "...",
      "alt": "...",
      "cover_emotion": "..."
    },
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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «зарегистрировали», ZERO Wordstat on canvas.
