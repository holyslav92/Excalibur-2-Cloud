# Cover-scene inputs — B30

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B30
- tenant: The Риэлтор, Тюмень
- H1: За 5 дней до ДДУ шоу-рум на юге — в проекте северная секция
- hook (cover-text): «Шоурум обещал солнце, договор показал север» (highlight: «север»)
- sticky: «Не подписали ДДУ»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: шоу-рум с солнцем и «солнечной стороной» в брони → за 5 дней до ДДУ проект с секцией B на севере, окна на соседний корпус → «та же цена, другой подъезд» → отказ от ДДУ, часть брони удержали, эскроу не открывали

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4430
- «тюмень новостройки квартира с отделкой» — demand spine
- «новостройки» — RU compare 927399

## meme_picks (from cover-text.json)

- cover: james_doakes, long_cat
- inline_1: wojak
- inline_5: doge
- inline_7: capybara_indifference

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B29: mortgage corner lobby two_buttons crying_cat
- B28: KP pavilion sand jacket gas pipe
- B27: sales office terracotta overshirt declaration
- B26: bank mortgage desk olive vest

**Required:** light/bright #FFF high-key, sun flare; james_doakes people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NEW location (яркий шоу-рум новостройки с панорамным окном и солнечным лучом, рядом черновик ДДУ с планом секции B на севере — NOT duplicate B27 declaration desk, NOT B29 mortgage corner).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Эталонная квартира с окнами во двор (pair with inline_2)
Labels: Солнечная сторона | Заявка на бронь | Окна во двор | Демонстрационная квартира | Не та секция
Meme: wojak tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Окна во двор | Дневной свет | Та же планировка | Другой корпус | Метраж совпал
NO meme — таблица: шоу-рум «солнечная сторона» vs секция в проекте ДДУ

### inline_3 — realistic_photo — «Та же цена, просто другой подъезд»
Labels: Пять дней до ДДУ | Секция Б | Северная сторона | Окна на корпус | Площадь та же
NO meme — ноутбук с проектом ДДУ, заявка на бронь, поэтажный план без лиц

### inline_4 — realistic_photo — «Солнечная сторона» в шоу-руме и заявке
Labels: Та же цена | Другой подъезд | Вид из окна | Не равноценность | Менеджер успокаивает
NO meme — контраст вид из окна шоу-рума vs вид на корпус, без людей

### inline_5 — bar_timeline_chart — ДДУ не подписали, эскроу, бронь
Labels: ДДУ не подписали | Эскроу не открывали | Часть брони удержали | Отказ от замены | Бронь отдельный договор
Meme: doge tiny corner

### inline_6 — process_flow — Что сопоставить до подписи
Labels: Секция в ДДУ | Поэтажный план | Генплан дома | Идентификатор в ЕИСЖС | наш.дом.рф
NO meme — процесс: бронь → проект ДДУ → генплан → ЕИСЖС

### inline_7 — structure_diagram — действия до подписи
Labels: Исправленный проект | Переписку сохранить | Пауза до подписи | Не спасать бронь | Окна и вид
Meme: capybara_indifference tiny corner

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
