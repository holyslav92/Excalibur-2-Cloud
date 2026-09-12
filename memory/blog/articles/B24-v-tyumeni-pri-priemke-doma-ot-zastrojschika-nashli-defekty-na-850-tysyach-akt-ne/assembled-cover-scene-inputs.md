# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: Под Тюменью дом от застройщика не приняли из-за брака на 850 тысяч
- hook (cover-text): «850 тысяч брака — дом не приняли» (highlight: «брака»)
- sticky: «Чистый акт не подписали»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: приёмка коттеджа под Тюменью — тепловизор нашёл промерзание, продувание окон, просадку утеплителя кровли; смета 850 000 ₽; прораб предлагает подписать чистый акт «устраним по гарантии»; семья остановила приёмку

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «приемка квартир тюмень» — 279
- «дома в тюмени от застройщика» — 279
- «приемка квартиры в новостройке тюмень» — 29

## meme_picks (from cover-text.json)

- cover: this_is_fine_dog, long_cat
- inline_1: james_doakes
- inline_5: wojak
- inline_7: cheems

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo:** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater newbuild handover room side_eye_chloe
- B22: lemon yellow shirt mortgage desk disaster_girl
- B20: terracotta overshirt MFC corridor

**Required:** light/bright #FFF high-key, sun flare; this_is_fine_dog + long_cat small stickers; NO Wordstat query strips; NO dark cinematic; NEW location (загородный дом на приёмке, тепловизор, дефектная ведомость, морозный свет).

## Inline slots

### inline_1 — realistic_photo (pair inline_2) — семья приехала за ключами
Labels from cover-text; meme james_doakes tiny

### inline_2 — comparison_table (pair) — тепловизор показал брак
Labels: промерзание | продувание | кровля | стяжка | 850 000 ₽

### inline_3 — realistic_photo — «подпишите сейчас, устраним по гарантии»
Labels from cover-text; NO meme

### inline_4 — realistic_photo — смета 850 тысяч, ключи не взяли
Labels from cover-text; NO meme

### inline_5 — structure_diagram — мотивированный отказ
Labels from cover-text; meme wojak tiny

### inline_6 — labeled_checklist — чеклист приёмки дома
Labels from cover-text; NO meme

### inline_7 — bar_timeline_chart — таблица проверки
Labels from cover-text; meme cheems tiny

## JSON schema

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
