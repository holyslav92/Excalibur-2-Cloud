# Cover-scene inputs — B10

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B10
- tenant: The Риэлтор, Тюмень
- H1: Сделку у нотариуса провели — а суд отменил: продавца месяцами вели мошенники по телефону
- hook (cover-text): «Нотариус не спас от звонков мошенников» (highlight: «мошенников»)
- sticky: «суд вернул сделку»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: нотариальная сделка казалась чистой; полгода спустя продавец оспорил — телефонное давление месяцами; нотариус видит только момент в кабинете; обзор ВС 2026; мошенники ушли с дарения на куплю-продажу

## meme_picks (from cover-text.json)

- cover: roll_safe + smudge_cat (people + cat, small stickers ≤15%, never on hook/face/phone)
- inline_1: hide_pain_harold
- inline_5: confused_math_lady
- inline_7: two_buttons

## Wordstat (topic research only — NOT painted on cover)

- купить квартиру в тюмени — 22652
- мошенники при покупке квартиры — 404
- проверка квартиры перед покупкой — 1872

## Variety lock (HARD)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose each run.

**FORBIDDEN combo:** чёрный пиджак + бюст слева + боковой взгляд (B03/B04 pattern).

**Recent covers to differ from:** B05 terracotta right entrance; B06 lemon shirt right window; B01–B04 navy/charcoal/black blazer left bust.

**Required:** light/bright #FFF high-key, sun flare; meme roll_safe + smudge_cat small stickers; NO dark cinematic; NO daypart formula; NO Wordstat strips on canvas.

## Inline slots

### inline_1 — comparison_table — «Нотариус оформил — покупатель успокоился»
Labels: нотариус удостоверил | банк расчёт | регистрация чистая
Meme: hide_pain_harold corner

### inline_2 — process_flow — «Полгода спустя продавец сказал: меня вели по телефону»
Labels: полгода спустя | иск в суд | телефонное давление
NO meme

### inline_3 — labeled_checklist — «Типовой тюменский сценарий»
Labels: личность в кабинете | воля в моменте | не история звонков
NO meme

### inline_4 — structure_diagram — «Что нотариус удостоверяет в кабинете»
Labels: месяцы звонков | скрытое давление | не видит нотариус
NO meme

### inline_5 — comparison_table — «Что остаётся за дверью кабинета»
Labels: обзор ВС 2026 | добросовестный покупатель | ст. 178 ГК
Meme: confused_math_lady corner

### inline_6 — process_flow — «Обзор ВС 2026: когда сделку развернут»
Labels: дарение → купля | ФНП 2026 | 8,5% оспариваний
NO meme

### inline_7 — labeled_checklist — «На осмотре: нервный продавец»
Labels: чек до аванса | поведение продавца | фиксация осмотра
Meme: two_buttons corner

## JSON schema

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

scene_hint cover: 80–140 chars, named emotion, light/bright, phone CTA, pink highlight «мошенников», ZERO Wordstat on canvas.
