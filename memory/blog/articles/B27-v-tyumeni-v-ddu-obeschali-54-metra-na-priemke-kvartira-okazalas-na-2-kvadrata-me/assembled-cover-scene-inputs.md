# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше
- hook (cover-text): «В ДДУ обещали больше, чем построили» (highlight: «обещали»)
- sticky: «Не подписывать вслепую»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: в ДДУ 54,2 м², обмер БТИ 52,1 м² (−2,1 м², ~3,9%), застройщик предложил скидку 90 тыс. вместо перерасчёта ~210 тыс., семья не подписала акт и направила претензию

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «приемка квартиры в новостройке тюмень» — 35 (55+11176)
- «площадь квартиры меньше чем в дду» — 61 (225)
- «площадь квартиры меньше дду» — 80 (225)

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: expanding_brain
- inline_5: james_doakes
- inline_7: trollface

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling tape bare walls confused_math_lady
- B23: light blue shirt mustard sweater handover room full-body
- B22: lemon yellow shirt bank full-body center

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer acceptance office with floor-plan comparison table, NOT bank/MFC/bare walls duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — В ДДУ 54,2 квадрата — ипотека и цена завязаны на эту цифру (pair with inline_2)
Labels: ДДУ 54,2 м² | Проектная документация | Ипотечная нагрузка
Meme: expanding_brain tiny corner

### inline_2 — fact_card — pair with inline_1
Labels: Обмер БТИ | Факт 52,1 м² | Минус 2,1 м² | Рулетка на объекте
NO meme

### inline_3 — realistic_photo — На приёмке обмер показал 52,1 — минус 2,1 метра
Labels: Проектные отклонения | Предел в ДДУ | Передаточный акт | Письменная претензия
NO meme — bright empty newbuild room with tape measure on floor

### inline_4 — realistic_photo — «В пределах проектных отклонений» — менеджер зовёт подписать акт
Labels: Скидка 90 тысяч | Ориентир 210 тысяч | Цена за метр | Без ключей уехали
NO meme — handover desk with unsigned act and discount offer sheet

### inline_5 — bar_timeline_chart — Скидка 90 тысяч вместо перерасчёта — семья отказалась от акта
Labels: 11 дней на приёмку | Бронь 48 часов | Статья 214-ФЗ | Разница 3,9%
Meme: james_doakes tiny corner

### inline_6 — comparison_table — Претензия и давление сроков: 11 дней на приёмку и бронь соседней планировки
Labels: 54,2 против 52,1 | Экспликация и БТИ | Цена квадратного метра | Техплан и кадастр
NO meme

### inline_7 — process_flow — Что сверять на объекте — таблица площади по ДДУ и по обмеру
Labels: Три пункта в ДДУ | Замечание в акте | Копии документов | Право спорить
Meme: trollface tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    "inline_2": { "scene_hint", "alt" },
    "inline_3": { "scene_hint", "alt" },
    "inline_4": { "scene_hint", "alt" },
    "inline_5": { "scene_hint", "alt", "meme_picks" },
    "inline_6": { "scene_hint", "alt" },
    "inline_7": { "scene_hint", "alt", "meme_picks" }
  }
}
```
