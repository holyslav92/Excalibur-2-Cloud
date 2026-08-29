# Cover-scene inputs — B13

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B13
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени обещали машино-место к квартире — в Росреестре прав на него не нашли
- hook (cover-text): «Обещанное место исчезло из реестра» (highlight: «исчезло»)
- sticky: «Проверили до аванса»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: за два дня до аванса проверили не квартиру, а машино-место; номер на схеме есть, в ЕГРН права нет; аванс не внесли; квартиру и парковку развели

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить машиноместо в Тюмени» — 59
- «купить машиноместо» — 153
- «машиноместо ЕГРН» — 1 (partial)

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, grumpy_cat
- inline_1: bad_luck_brian
- inline_5: blinking_white_guy
- inline_7: sacrednik_priest

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B12: light blue shirt waist right showroom letter payment
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window price chart

**Required:** light/bright #FFF high-key, sun flare from parking ramp; disappointed_black_guy people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic underground; NO daypart formula; parking/registry props fresh twist.

## Anti-repeat used-motifs (14d) — avoid collision

B12 showroom letter; B10 apartment viewing phone; B06 panoramic window price chart.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Машино-место в подарок» — и аванс через два дня»
Labels: Два дня до аванса | Номер на схеме | Строка в приложении | Квартира чистая | Парковка — бонус
Meme: bad_luck_brian tiny corner

### inline_2 — process_flow — «Проверили не квартиру, а место в паркинге»
Labels: Выписка на место | Квартира — отдельно | С 2017 — объект | Кадастровый номер свой | До аванса ещё можно
NO meme

### inline_3 — bar_timeline_chart — «Финал: в Росреестре права на обещанное место не нашли»
Labels: Права не нашли | Аванс не внесли | Комплект рассыпался | Сделки развели | Продавец без права
NO meme

### inline_4 — structure_diagram — «Номер на схеме — это ещё не объект в ЕГРН»
Labels: Объект с 2017 года | Не «раз есть номер» | Разметка на полу | Пользование ≠ собственность | Четыре разные конструкции
NO meme

### inline_5 — labeled_checklist — «Что должно быть в отдельной выписке на машино-место»
Labels: Своя выписка ЕГРН | Вид — машино-место | Собственник отдельно | Обременения отдельно | Схема не заменяет
Meme: blinking_white_guy tiny corner

### inline_6 — fact_card — «Квартира и парковка: разные объекты, разные проверки»
Labels: Квартира и парковка | Два кадастровых номера | Два договора | Доверенность отдельно | Чистая квартира не гарантия
NO meme

### inline_7 — workflow_diagram — «Что делать, если место не подтверждено до аванса»
Labels: Аванс не вносим | Сделки разделить | Убрать «подарок» из воздуха | Выписку повторить | Выдел — не неделя
Meme: sacrednik_priest tiny corner

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «исчезло», ONE yellow sticky only, ZERO Wordstat strips on canvas.
