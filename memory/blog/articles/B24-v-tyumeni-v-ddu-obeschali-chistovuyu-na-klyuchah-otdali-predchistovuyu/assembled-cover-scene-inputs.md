# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую
- hook (cover-text): «Застройщик отдал квартиру без обещанного ремонта» (highlight: «обещанного»)
- sticky: «Ключи не берите сразу»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: в ДДУ чистовая (обои, ламинат, сантехника, двери) — на приёмке whitebox (стяжка, штукатурка без финиша) → предлагают акт без замечаний или доплату → семья фиксирует и уходит без ключей

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4642
- «отделка новостройка» — 260
- «чистовая отделка новостройка» — 34

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: surprised_pikachu

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: handover room light blue shirt mustard sweater DDU vs EGRN side_eye_chloe
- B22: yellow shirt bank mortgage desk disaster_girl
- B20: terracotta overshirt MFC corridor two DDU

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright unfinished apartment during acceptance walk-through — bare screed floor, plastered walls without wallpaper, empty bathroom niche; host kneeling or crouching comparing DDU appendix to actual room).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — В ДДУ написали «чистовая» — и семья ждала ключи с ремонтом (pair with inline_2)
Labels: Четыре позиции отделки | Обои и ламинат | Сантехника и двери | Сверить до брони
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Стяжка без покрытия | Стены без обоев | Санузел без сантехники | Это не дефект
NO meme — two columns «ДДУ обещано» vs «Факт на приёмке»

### inline_3 — realistic_photo — Семья зафиксировала расхождение и ушла без ключей
Labels: Акт без замечаний | Доплата за доделку | Обещанное не улучшение | Сравнить документы
NO meme — keys on tray untouched, defect list on clipboard

### inline_4 — realistic_photo — Три документа, которые нельзя оставить дома
Labels: Акт не подписан | Фото и видео | Письменная претензия | Ушли без ключей
NO meme — DDU + appendix + finish schedule on bright table

### inline_5 — process_flow — На приёмке вместо ламината и обоев — голая стяжка и штукатурка
Labels: Дефект качества | Неполная комплектация | Смена пакета отделки | Двери отдельно | Гарантия не заменяет
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — «Подпишите без замечаний» — или доплата за «доделку»
Labels: Ламинат повреждён | Раковины нет | Чистовая стала предчистовой | Ссылка на ведомость
NO meme

### inline_7 — structure_diagram — Что сверить на приёмке — таблица
Labels: Договор и приложение | Ведомость отделки | Допсоглашения | Акт осмотра отдельно | Семь рабочих дней
Meme: surprised_pikachu tiny corner

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
