# Cover-scene inputs — B33

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B33
- tenant: The Риэлтор, Тюмень
- H1: Под Тюменью в брони обещали 12 сotok — в кадастре оказалось 8 до подписания ДДУ
- hook (cover-text): «Двенадцать соток исчезли в кадастре» (highlight: «исчезли»)
- sticky: «Проверьте участок до ДДУ»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: дом с участком в КП под Тюменью, в брони и презентации 12 соток → за 4 дня до ДДУ выписка ЕГРН показывает 8 сotok → пауза, сверка границ, цена «дом с землёй», ДДU не подписали

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 892
- «купить дом в тюмени от застройщика» — 118
- «дома с участком от застройщика тюмень» — 24

## meme_picks (from cover-text.json)

- cover: james_doakes, long_cat
- inline_1: success_kid
- inline_5: pepe_frog
- inline_7: surprised_pikachu

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B32: sand overshirt bank DDU INN mismatch
- B31: turquoise shirt insurance payment bank
- B28: sand jacket KP gas pipe mockup roll_safe
- B27: terracotta overshirt sales office declaration rent

**Required:** light/bright #FFF high-key, sun flare; james_doakes people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright outdoor KP sales terrace with wooden land-plot maquette and ready cottage facade — NOT bank desk, NOT gas pipe repeat from B28).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Двенадцать сotok на плане — так выглядел участок в брони» (pair with inline_2)
Labels: Коттеджный посёлок | План лота двенадцать сotok | Бронь двести пятьдесят тысяч | Дом с участком | Офис продаж
Meme: success_kid tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Четыре дня до ДДU | Выписка ЕГРН вечером | Восемь сotok в строке | Минус четыреста метров | Ипотека на паузе
NO meme — table: бронь/план «12 сotok» vs выписка «8 сotok»

### inline_3 — realistic_photo — «За четыре дня до ДДU: на кухне открыли выписку ЕГРН»
Labels: Двенадцать в брони | Восемь в кадастре | Кадастровый номер | Раздел двенадцать три | Сверка приложений
NO meme — bright kitchen table evening, EGRN printout, laptop glow, no faces

### inline_4 — realistic_photo — «В кадастре восемь сotok — четыре сотки квадратов исчезли с бумаги»
Labels: Погрешность межевания | Цену не меняли | Межевой план | Схема границ | Эскроу не открывали
NO meme — cadastre boundary map on light desk, measuring tape, high-key

### inline_5 — structure_diagram — «Это погрешность межевания» — подписание поставили на паузу
Labels: Бронь двести пятьдесят | Условия возврата | Письменно застройщику | До перевода денег | Пауза сделки
Meme: pepe_frog tiny corner — diagram: pause arrow before DDU signature

### inline_6 — process_flow — «ДДU так и не подписали: цену дом с землёй не согласовали»
Labels: ДДU не подписали | Письмо застройщику | Банк ждёт объект | Дом с землёй | До визита в офис
NO meme — flow: letter → price pause → no escrow

### inline_7 — bar_timeline_chart — «До ручки на договоре: бронь, кадастр и раздел 12.3 декларации»
Labels: Раздел двенадцать три | ЕИСЖС декларация | Не общий массив | Сверка до подписи | Четыре сotki разницы
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
