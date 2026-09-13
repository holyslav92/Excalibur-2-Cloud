# Cover-scene inputs — B24

ROLE: cover-scene. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень, ведущий Святослав (identity-real i2i)
- H1: На P-42 в Тюмени парковку по ДДУ отдали другому — через 3 дня чужая машина
- cover_hook: Чужая машина заняла ваше место
- cover_hook_highlight: Чужая
- sticky: Это не опечатка
- phone_cta: +7 922 001 65 05
- angle: семья получила ключи, на оплаченном месте P-42 стоит чужая машина; застройщик назвал «опечаткой» и предложил аналог

## meme_picks (из cover-text.json — ОБЯЗАТЕЛЬНО сохранить)

- cover: confused_math_lady + this_is_fine_dog
- inline_1: james_doakes
- inline_5: cheems
- inline_7: disappointed_black_guy

## Anti-repeat 14д (НЕ повторять)

B23: light blue shirt mustard sweater, handover room, side_eye_chloe + pop_cat, full-body right
B22: lemon shirt mortgage office, disaster_girl + keyboard_cat
B20: terracotta overshirt MFC corridor, two_buttons + surprised_tom

Запрещено: чёрный пиджак + бюст слева + боковой взгляд; daypart formula; dark cinematic; Wordstat query strips на cover.

## Wordstat (только для manifest log, НЕ рисовать на cover)

- новостройки тюмень (8430)
- машиноместо в новостройке (971)
- машиноместо дду (207)

## H2 и inline_labels

### inline_1 — Ключи на столе — а на P-42 стоит чужая машина (realistic_photo + james_doakes)
Через три дня, P-42 занято, Другой номер, Шлагбаум не тот, Отдельный ДДУ

### inline_2 — pair с inline_1 (comparison_table, no memes)
Акт по квартире, Парковку не проверили, Отдельный ДДУ, Акт не парковка, Эскроу отдельно

### inline_3 — Квартиру приняли, парковку отложили на потом (realistic_photo, no memes)
Опечатка застройщика, Дальше от лифта, Другой уровень, Замена места, Устное не считается

### inline_4 — Что сверить до ключей — таблица (realistic_photo, no memes)
Претензия на P-42, Регистрация стоп, Досудебный спор, Статья 398 ГК, Машина не право

### inline_5 — «Опечатка в приложении» и предложение аналога (process_flow + cheems)
С 2017 года, План и площадь, Оплата и передача, Свой акт, Табличка не объект

### inline_6 — Претензия, отказ от замены и стоп регистрации (bar_timeline_chart, no memes)
План и номер, Наш.дом.рф, Отдельный эскроу, Выписка ЕГРН, Акт отдельно

### inline_7 — Почему номер на плане — не мелочь отдела продаж (structure_diagram + disappointed_black_guy)
Эскроу не спор, Отдельный договор, Проверка до ключей, Не откладывать, Ключи не приёмка

## Требования JSON

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
    "cover": { "scene_hint": "...", "alt": "...", "cover_emotion": "...", "meme_picks": ["confused_math_lady", "this_is_fine_dog"] },
    "inline_1": { "scene_hint": "...", "alt": "...", "meme_picks": ["james_doakes"] },
    "inline_2": { "scene_hint": "...", "alt": "..." },
    "inline_3": { "scene_hint": "...", "alt": "..." },
    "inline_4": { "scene_hint": "...", "alt": "..." },
    "inline_5": { "scene_hint": "...", "alt": "...", "meme_picks": ["cheems"] },
    "inline_6": { "scene_hint": "...", "alt": "..." },
    "inline_7": { "scene_hint": "...", "alt": "...", "meme_picks": ["disappointed_black_guy"] }
  }
}
```

## Правила

- light & bright high-key, sun flare, #FFFFFF airy — NO dark cinematic
- INVENT outfit/location/action/emotion/pose — NOT black blazer left bust side-eye
- scene_hint cover ~80-140 chars + named emotion; phone +7 922 001 65 05 on cover
- alt = human Russian, NO hook/CTA/memes/scene_hint tokens
- inline realistic_photo: NO host face, NO co-host human
- meme stickers ≤15%, never on hook/face/phone
