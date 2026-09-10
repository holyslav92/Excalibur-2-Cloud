# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки
- hook (cover-text): «Выписка уменьшила участок перед ключами» (highlight: «уменьшила»)
- sticky: «Акт пока не подписывайте»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: ДДУ на дом в посёлке — 12 соток в приложении; выписка ЕГРН 10,5 соток, граница смещена; забор соседа; «домежуем потом»; ключи не взяли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3640
- «дом в тюмени» — 892
- «ипотека ижс» — 156

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: wojak
- inline_5: this_is_fine_dog
- inline_7: woman_yelling_cat

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: blue shirt mustard sweater handover room EGRN vs DDU keys
- B22: yellow shirt bank mortgage desk full-body center
- B20: terracotta overshirt MFC corridor two DDU

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO bank/MFC/handover room duplicate; NEW location (bright outdoor cottage village plot inspection table with cadastral map, fence line visible through window OR sunny veranda of new cottage with plot plan spread).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Выписка ЕГРН: 10,5 соток и забор соседа (pair with inline_2)
Labels: Двенадцать соток в договоре | Ипотека для ИЖС | Расчёты через эскроу | Генплан посёлка
Meme: wojak tiny corner

### inline_2 — structure_diagram — pair with inline_1
Labels: Контур на месте другой | Забор соседа рядом | Забор не граница | Выписка на землю
NO meme — diagram showing DDU boundary vs fence line

### inline_3 — realistic_photo — Ключи не взяли: банк, эскроу и претензия
Labels: Десять с половиной соток | Минус полторы сотки | Расхождение 12,5 процента | Граница смещена
NO meme — EGRN extract on bright desk with highlighted 10.5 sotok

### inline_4 — realistic_photo — В посёлке обещали 12 соток
Labels: Домежуем потом | Акт землю не добавит | Нужен межевой план | Согласие соседа
NO meme — developer handover act with «домежуем потом» sticky note

### inline_5 — comparison_table — В приложении граница другая
Labels: Порог пять процентов | Статья четыре | Письменный ответ застройщика | Срок исправления письменно
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — Застройщик «домежуем потом»
Labels: Ключи не взяли | Письменная претензия | Банку нужна выписка | Деньги на эскроу
NO meme

### inline_7 — bar_timeline_chart — Что сверить в ДДУ и ЕГРН
Labels: Площадь земли | Расположение границ | Номер и право | Ограничения участка | Порядок исправления
Meme: woman_yelling_cat tiny corner (cat half only)

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
