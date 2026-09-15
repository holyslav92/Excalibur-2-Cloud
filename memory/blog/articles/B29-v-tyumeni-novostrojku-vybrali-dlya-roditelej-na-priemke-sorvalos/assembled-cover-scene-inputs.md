# Cover-scene inputs — B29

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B29
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени на приёмке новостройки для родителей — 10 минут до лифта, акт не подписали, ключи не взяли
- hook (cover-text): «Квартиру покупали родителям — ключи не забрали» (highlight: «родителям»)
- sticky: «Тихо только во дворе»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: На экскурсии — тихий двор, лавочка. На приёмке — парковка через проезжую часть, один малый лифт с очередью, окна на магистраль. Отделка по ДДУ сходится, но акт не подписали, ключи не выдали.

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень от застройщика» — 651
- «приемка квартиры в новостройке» — 412
- «квартира для пожилых родителей» — 28

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, crying_cat
- inline_1: james_doakes
- inline_5: wojak
- inline_7: roll_safe

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B25: kneeling left tape measure empty apartment bare walls (YESTERDAY — avoid duplicate)
- B26: olive knit vest bank mortgage desk tablet
- B23: light blue shirt mustard sweater handover room keys tray
- B22: lemon yellow shirt bank desk calculator

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT empty apartment kneeling like B25; NOT bank desk like B26.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — pair with inline_2 — «Тихий двор на экскурсии, на приёмке другая картина»
Labels: Закрытый двор | Лавочка и клумбы | Родителям 68–72 года | Парковка дальше | Один лифт
Meme: james_doakes tiny corner
Split: sunny courtyard with bench vs distant parking across road

### inline_2 — comparison_table — pair with inline_1
Labels: Парковка через дорогу | С пакетами дальше | Двор без машин | Фото маршрута | Акт осмотра
NO meme — two columns экскурсия vs приёмка

### inline_3 — realistic_photo — «Окна на магистраль: во дворе тихо, в квартире шум трассы»
Labels: Один малый лифт | Очередь у подъезда | До десяти минут | Часы пик | Видео очереди
NO meme — small elevator lobby queue, elderly with bags waiting

### inline_4 — realistic_photo — «Окна на магистраль, во дворе тихо»
Labels: Окна на магистраль | Во дворе тихо | Поток машин | Запись на телефон | Проектная декларация
NO meme — apartment window view highway vs quiet courtyard below

### inline_5 — process_flow — «Отделка сходится, акт не подписали, ключи не выдали»
Labels: Отделка по договору | Акт не подписан | Ключи не выдали | Замечания в акте | Письменный запрос
Meme: wojak tiny corner — numbered steps refuse keys → inspection act → written claim

### inline_6 — bar_timeline_chart — «214-ФЗ, проектная декларация, наш.дом.рф»
Labels: 214-ФЗ | Проектная декларация | Статьи 7 и 19 | ПП № 2226 | наш.дом.рф | Фото и видео
NO meme — legal timeline bars with evidence checkpoints

### inline_7 — structure_diagram — «Что проверить до подписи»
Labels: Маршрут от парковки | Окна в квартире | Лифт в пик | Сверка с договором | Не подписывать вслепую
Meme: roll_safe tiny corner — hub diagram 5 checkpoints before signing

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
