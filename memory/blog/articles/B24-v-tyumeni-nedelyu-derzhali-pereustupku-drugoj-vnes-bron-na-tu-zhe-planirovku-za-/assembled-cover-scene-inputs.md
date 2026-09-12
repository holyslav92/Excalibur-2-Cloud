# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: 7 дней держали переуступку в Тюмени — квартиру забронировали другие
- hook (cover-text): «Устная договорённость не удержала квартиру» (highlight: «договорённость»)
- sticky: «Лот забрали за день»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья согласовала переуступку, неделю готовила пакет цессии без брони у застройщика — другой покупатель внёс бронь на ту же планировку за сутки; потеряли планировку и цену, не деньги на эскроу

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 909
- «переуступка новостройка» — 2475 (RU 225)
- «новостройки тюмень» — 4560

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, doge
- inline_1: confused_math_lady
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room keys/egrn
- B22: lemon shirt bank mortgage desk disaster_girl
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + doge cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer sales office with floor plan wall + assignment folder + reservation stamp — NOT MFC/bank/handover duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Мы уже договорились» — и семья отложила бронь у застройщика (pair with inline_2)
Labels: Цена согласована | Неделя на документы | Бронь не внесли | Переписка не защищает
Meme: confused_math_lady tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: ДДУ зарегистрирован | Согласие застройщика | Цессия не зарегистрирована | Права не перешли
NO meme

### inline_3 — realistic_photo — За сутки до визита в офис продаж лот забрал другой покупатель
Labels: Брони нет | Другой внёс плату | Та же планировка | Переписка не обязывает
NO meme — bright sales desk with SOLD stamp on floor plan

### inline_4 — realistic_photo — Деньги на эскроу не зависли — планировка и цена ушли
Labels: Цессия бессмысленна | Другая планировка | Цена ушла | Один день
NO meme — empty escrow folder vs crossed-out layout card

### inline_5 — structure_diagram — Переуступка и бронь живут в разных регистрах
Labels: Аванса не было | Эскроу не открывали | Планировка потеряна | Неделя работы
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — Что проверить до оплаты по переуступке — таблица (part 1)
Labels: Цессия в Росреестре | Бронь у застройщика | Резерв по лоту | Договорённость не резерв
NO meme

### inline_7 — bar_timeline_chart — Что проверить до оплаты — timeline
Labels: Регистрация ДДУ | Действующая бронь | Номер и срок | Выписка ЕГРН | Аккредитив до регистрации
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
