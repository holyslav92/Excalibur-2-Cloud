# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей
- hook (cover-text): «Маткапитал задержал ключи в новой квартире» (highlight: «задержал»)
- sticky: «Доли детям не совпали»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека + маткапитал в первом взносе, ДДУ зарегистрирован, дом сдан; за 3 недели до акта банк приостановил регистрацию из-за расхождения долей детей между ДДУ, заявлением СФР и кредитным пакетом → допсоглашение через юриста → ключи +1 месяц

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки с маткапиталом» — 175 (55+11176)
- «выделение долей детям маткапитал» — 872 (RU)
- «семейная ипотека тюмень» — локальный спрос

## meme_picks (from cover-text.json)

- cover: james_doakes, long_cat
- inline_1: confused_math_lady
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: handover room light blue shirt mustard sweater EGRN vs DDU
- B22: bank desk yellow shirt full-body center disaster_girl
- B20: MFC corridor terracotta overshirt two DDU
- B19: showroom turquoise polo cancel card

**Required:** light/bright #FFF high-key, sun flare; james_doakes people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom/handover duplicate; NEW location (bright empty newbuild apartment with folding table, DDU pages + SFR application mismatch, keys still sealed in developer envelope).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Маткапитал в первом взносе — и семья пошла к ключам (pair with inline_2)
Labels: Семейная ипотека | Маткапитал на эскроу | ДДУ зарегистрирован | Двое детей | Три недели до ключей
Meme: confused_math_lady tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: ДДУ без долей | Заявление СФР иначе | Третий пакет банка | Деньги на эскроу | Сверка до акта
NO meme

### inline_3 — realistic_photo — Ключи перенесли на месяц: как закрыли пакет
Labels: Дом уже сдан | Регистрацию остановили | Доли описаны по-разному | СФР задал вопросы | Акт отложили
NO meme — bright developer office with paused registration stamp on folder

### inline_4 — realistic_photo — В ДДУ одно, в заявлении для СФР — другое
Labels: Переподпись: отказ | Допсоглашение к ДДУ | Соглашение о долях | Юрист сверил пакет | Ключи через месяц
NO meme — two application forms side by side on bright desk

### inline_5 — bar_timeline_chart — За три недели до акта банк приостановил регистрацию
Labels: Доли в общую собственность | Банк возобновил регистрацию | Квартиру не потеряли | Маткапитал не вернули | Задержка на месяц
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — Застройщик не переподписал ДДУ — пошли через юриста
Labels: ДДУ и приложения | Заявление в СФР | Кредитный договор | Сведения об эскроу | Соглашение о долях
NO meme

### inline_7 — structure_diagram — Что сверить до акта приёма — таблица
Labels: ДДУ, СФР, банк | Письменный порядок долей | Акт после проверки | Залог банка | Пауза до акта
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
