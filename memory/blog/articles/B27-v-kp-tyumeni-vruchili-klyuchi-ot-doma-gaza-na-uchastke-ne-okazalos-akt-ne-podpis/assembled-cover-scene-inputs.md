# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: За 3 дня до ключей в КП Тюмени вручили дом без газа — семья не подписала акт
- hook (cover-text): «Ключи вручили без газа акт не подписан» (highlight: «газа»)
- sticky: «котлован вместо ввода»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: торжественная выдача ключей в коттеджном посёлке → на участке котлован вместо газового ввода → акт с оговоркой «сети за квартал» → давление «все соседи приняли» → семья отказалась, ключи на хранение, претензия с фото

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «коттеджные поселки тюмень»
- «новостройки тюмень»
- «ипотека новостройка тюмень»

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: this_is_fine_dog
- inline_5: stonks
- inline_7: expanding_brain

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling bare apartment confused_math_lady
- B23: light blue mustard sweater handover room side_eye_chloe
- B22: yellow shirt bank desk disaster_girl full-body center

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom duplicate; NEW location (bright outdoor KP ceremony pavilion near Tyumen with ribbon keys tray and photo of empty gas pit on clipboard).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Торжественные ключи — и котлован вместо газового ввода» (pair with inline_2)
Labels: Торжественные ключи | Котлован под ввод | Мощность ниже договора | Техусловий не было
Meme: this_is_fine_dog tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: За три дня | Сети за квартал | Передаточный акт | Сроки из ДДУ
NO meme — bright table comparing DDU gas deadline vs «подключим за квартал» clause

### inline_3 — realistic_photo — «За три дня до выдачи прислали акт: «сети подключат в течение квартала»»
Labels: Все соседи приняли | Сети подключим позже | Ипотека и аренда | Чужая подпись
NO meme — bright desk with unsigned transfer act and calendar «3 дня»

### inline_4 — realistic_photo — «Семья отказалась: ключи «на хранение», претензия с фото»
Labels: Акт не подписан | Ключи на хранение | Претензия с фото | Пункт о газе
NO meme — keys in custody envelope, claim letter, gas pit photos on bright table

### inline_5 — process_flow — «Все соседи уже приняли» — давление перед подписью
Labels: Ипотека не ждёт | Аренда продолжается | Газ не появился | Отказ обоснован
Meme: stonks tiny corner

### inline_6 — bar_timeline_chart — «Газ в посёлке, газ у границы и газ в доме — три разные цепочки»
Labels: Газ в посёлке | Газ у участка | Газ в доме | Труба не котёл
NO meme — three-step bar chart village → plot → house

### inline_7 — structure_diagram — «Что сверять до подписи передаточного акта — таблица»
Labels: Сверка с ДДУ | Техусловия и проект | Щит и мощность | Акт о несоответствии
Meme: expanding_brain tiny corner

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
