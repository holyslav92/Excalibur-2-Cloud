# Cover-scene inputs — B11

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B11
- tenant: The Риэлтор, Тюмень (Святослав Шакин)
- H1: Родственники оспорили продажу: в прошлой сделке денег не было — покупатель в Тюмени лишился квартиры
- hook (cover-text): «Чистая выписка — квартиру забрал суд» (highlight: «квартиру»)
- sticky: «Выписка не видит оплату»
- phone_cta: +7 922 001 65 05 (обязательно на обложке, bottom-right)
- angle: покупатель видел чистую ЕГРН, но в цепочке была мнимая сделка между родственниками без денег; через 2 года после смерти владельца суд отменил право

## meme_picks (from cover-text.json — HARD)

- cover: disaster_girl, polite_cat
- inline_1: disappointed_black_guy
- inline_5: crying_cat
- inline_7: roll_safe

## Wordstat (manifest log ONLY — NEVER paint on cover/canvas)

- «купить квартиру в тюмени» — 17699
- «проверка недвижимости» — 122
- «росреестр проверка недвижимости» — 22

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B10: sage olive cardigan, host large left wary glance at elderly seller phone
- B06: lemon yellow shirt, host right dynamic price jump
- B05: terracotta sweater + grey overcoat, host right entrance steps
- B04/B03: black blazer left bust side-eye board

**Layout:** hook H1 RIGHT side sacred zone; phone bottom-right; host LEFT but NOT default talking-head bust formula.

**Required:** light/bright #FFFFFF high-key, sun flare, gold/black collage; meme stickers ≤15%; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NO doc-only empty office.

## Anti-repeat used-motifs (14d) — avoid collision

B10 sage cardigan viewing; B06 lemon shirt right; B05 terracotta right entrance; B04/B03 black blazer left bust board.

## Inline slots (scene_hint + alt; NO host face on inline; NO co-host human)

### inline_1 — process_flow — «В Тюмени всё выглядело чисто — пока не всплыла старая сделка»
Labels: Выписка ЕГРН чистая | Расчёт полностью | Право зарегистрировано | Без обременений | Деньги двигались?
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table_ui — «Цепочка собственников: где спряталось слабое звено»
Labels: Три звена владения | Родственник посередине | Деньги не передавались | Сделка на бумаге | Статья 170 ГК РФ
NO meme

### inline_3 — workflow_diagram — «Через два года после смерти прежнего владельца»
Labels: Два года жили | После смерти владельца | Наследники оспорили | Спор спустя годы
NO meme

### inline_4 — checklist_board — «Финал: суд признал прошлый договор фиктивным и отменил право покупателя»
Labels: Суд: сделка мнимая | Право отменили | Деньги не двигались | Владение не менялось | Статья 167 ГК РФ
NO meme

### inline_5 — structure_diagram — «Почему ЕГРН не доказывает, что в старой сделке были деньги»
Labels: Выписка не про оплату | Сделка в реестре | Деньги не видны | Пункт 3 статьи 486 | Расписка не всегда хватит
Meme: crying_cat tiny corner

### inline_6 — schema_faq_ui — «Красные флаги: родственники, цена и кто реально жил в квартире»
Labels: Переход между роднёй | Цена вне рынка | Короткое владение | Собственник жил дальше | Платил ЖКУ после продажи
NO meme

### inline_7 — tool_screenshot — «Что запросить до аванса: документы по прошлому расчёту»
Labels: История всех переходов | Договор прошлой сделки | Выписка по счёту | Кто жил после продажи | Состав наследников
Meme: roll_safe tiny corner

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

scene_hint cover: 80–140 chars, named emotion, light/bright, hook RIGHT, phone CTA bottom-right, pink highlight «квартиру», ZERO Wordstat on canvas.
