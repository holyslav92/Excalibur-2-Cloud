# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: Под Тюменью коттедж не приняли — забор разошёлся с кадастром на 1,8 м
- hook (cover-text): «Коттедж не приняли: граница ушла на метры» (highlight: «граница»)
- sticky: «Ключи подождут»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья на ключи к дому в КП; кадастровый инженер показал смещение забора/межи ~1,8 м от ЕГРН; площадь в выписке меньше буклета; акт не подписали; банк стопнул транш

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «коттеджные поселки тюмень» — 1479
- «границы земельного участка» — 927
- «межевание земельного участка тюмень» — 57

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: james_doakes
- inline_5: capybara_indifference
- inline_7: sacrednik_priest

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling apartment measuring tape confused_math_lady
- B23: light blue shirt handover room side_eye_chloe
- B22: yellow shirt bank full-body center

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO bank/MFC/apartment duplicate; NEW location = bright cottage village plot handover outdoors with fence stakes and cadastre plan.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Менеджер торопит с ключами, а в ЕГРН площадь меньше (pair with inline_2)
Labels: Десять соток | Забор у калитки | Координаты в реестре | Смещение 1,8 метра | Устное «разберёмся»
Meme: james_doakes tiny corner

### inline_2 — structure_diagram — pair with inline_1
Labels: До подписания акта | Вынос границ | Прибор на участке | Линия по координатам | Не рулетка у забора
NO meme

### inline_3 — realistic_photo — В буклете десять соток, на земле забор ушёл на 1,8 метра
Labels: Ключи на столе | Площадь в реестре | Меньше буклета | Технический вопрос | Акт фиксирует результат
NO meme — bright cottage gate with fence offset vs brochure plan on clipboard

### inline_4 — realistic_photo — За два часа до акта: кадастровый инженер выносит точки
Labels: Акт не подписан | Письменная претензия | Ключи не забрали | Граница в реестре | Не акт с замечаниями
NO meme — surveyor stakes and total station on sunny plot, no faces

### inline_5 — comparison_table — Семья отказалась подписывать: претензия вместо передаточного акта
Labels: Обещание полгода | Последний транш | Банк не перевёл | Схема участка | Заключение инженера
Meme: capybara_indifference tiny corner

### inline_6 — process_flow — «Поправим межу через полгода» — банк остановил последний транш
Labels: Площадь участка | Границы по координатам | Дом и коммуникации | Передаточный акт | График платежей
NO meme

### inline_7 — bar_timeline_chart — Что сверять на приёмке дома в КП — таблица бумаги и земли
Labels: Документы до приёмки | Земля и дом | Претензия в день | Не подписывать вслепую | Консультация до акта
Meme: sacrednik_priest tiny corner

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
