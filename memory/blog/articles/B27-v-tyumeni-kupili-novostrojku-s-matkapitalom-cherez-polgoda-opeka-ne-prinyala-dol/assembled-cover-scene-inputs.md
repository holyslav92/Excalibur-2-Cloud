# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: На 47-й день срока приостановили регистрацию детских долей в новостройке с маткапиталом
- hook (cover-text): «Детские доли снова остановили регистрацию» (highlight: «остановили»)
- sticky: «Шаблон подвёл семью»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья получила ключи от новостройки, подписала соглашение «по 1/4 каждому», на 47-й день пакет вернули, Росреестр приостановил регистрацию; со 2-й попытки — 11-я неделя, ~90 тыс. ₽

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- материнский капитал на покупку жилья
- новостройки тюмень
- выделение долей детям

## meme_picks (from cover-text.json)

- cover: james_doakes, long_cat
- inline_1: wojak
- inline_5: disappointed_black_guy
- inline_7: sacrednik_priest

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo:** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk denied tranche (hide_pain_harold)
- B25: kneeling empty apartment tape measure (confused_math_lady)
- B23: light blue shirt handover room keys (side_eye_chloe)
- B22: lemon shirt bank rate desk full-body center

**Required:** light/bright #FFF high-key, sun flare; james_doakes + long_cat small stickers; NO Wordstat query strips; NO dark cinematic; NEW location — bright Rosreestr/MFC registration counter OR sunlit kitchen with children's shares agreement papers (NOT bank desk, NOT empty apartment kneeling).

## Inline slots

### inline_1 — realistic_photo — Ключи на руках — соглашение «по четверти каждому» (pair with inline_2)
Labels: ДДУ с ипотекой | Маткапитал в эскроу | Передаточный акт | По 1/4 каждому | Срок 6 месяцев
Meme: wojak tiny corner — bright newbuild keys on table with quartered agreement draft

### inline_2 — comparison_table — pair with inline_1
Labels: 47-й день срока | Пакет на доработку | Приостановка Росреестра | Не решение опеки | 11-я неделя
NO meme — table comparing «шаблон 1/4» vs «пропорция маткапитала»

### inline_3 — realistic_photo — Росреестр, опека, банк и СФР — не одна дверь
Labels: Расчёт Росреестра | Опека при продаже | Согласие банка | Маткапитал СФР | Разные двери
NO meme — four door signs/icons hallway bright MFC Tyumen

### inline_4 — structure_diagram — Почему «по 1/4» не равно закону о маткапитале
Labels: 12% маткапитал | По 4% каждому | Совместная собственность | От передаточного акта | Не от эскроу
NO meme — pie chart 12% matkapital vs 88% mortgage split

### inline_5 — process_flow — Вторая попытка: одиннадцатая неделя и счёт около 90 тысяч
Labels: 11-я неделя | Около 90 тысяч ₽ | Переделка соглашения | Повторная подача | Шаблон дорого стоит
Meme: disappointed_black_guy tiny corner — timeline flow attempt 1 STOP → rewrite → week 11 OK

### inline_6 — labeled_checklist — Таблица: что сверить до подписания
Labels: Росреестр — стоп | Опека — отчуждение | Банк — залог | СФР — срок | До подписи
NO meme — checklist table 4 participants

### inline_7 — bar_timeline_chart — Итог
Labels: Пропорция маткапитала | Схема собственности | Сразу после акта | Без повторной подачи | Доли не формальность
Meme: sacrednik_priest tiny corner — 6-month bar from transfer act deadline

## JSON schema

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "visual_type", "placement_group", "labels", "meme_picks" },
    ...
  }
}
```
