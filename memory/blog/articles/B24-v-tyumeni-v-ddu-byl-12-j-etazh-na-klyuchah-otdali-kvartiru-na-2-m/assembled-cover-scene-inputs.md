# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й
- hook (cover-text): «Договор закрепил этаж — ключи дали ниже» (highlight: «этаж»)
- sticky: «Акт не подписан»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья выбрала 12-й этаж в ДДУ и поэтажном плане; на выдаче ключей открыли дверь на 2-м; застройщик — «перераспределение секции»; акт не подписан; ипотека и регистрация на паузе

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4663
- «приемка квартиры в новостройке тюмень» — 33
- «купить новостройку в тюмени» — 865

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: james_doakes
- inline_5: this_is_fine_dog
- inline_7: expanding_brain

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room side_eye_chloe (full-body right)
- B22: yellow shirt bank mortgage desk disaster_girl (full-body center)
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT handover room duplicate B23; NEW location (bright corridor on low floor near elevator with floor indicator «2» vs DDU appendix «12»).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Двенадцатый этаж в ДДУ — и вид из окна, за который платили (pair with inline_2)
Labels: 12-й этаж в ДДУ | Поэтажный план | Тишина и вид | Этаж в 214-ФЗ | Не рекламное обещание
Meme: james_doakes tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Офис выдачи ключей | Другая секция | Второй этаж | Двор из окна | Номер не совпал
NO meme

### inline_3 — realistic_photo — На выдаче ключей открыли дверь на втором
Labels: Техническая корректировка | Согласия не было | Видео пути к двери | Акт о несоответствии | Претензия застройщику
NO meme — bright key handover corridor, door plate «2», DDU page «12» on clipboard

### inline_4 — structure_diagram — Почему этаж в договоре — не «мелочь при приёмке»
Labels: Этаж не поднимут | Статья 7 закона 214-ФЗ | Проектная декларация | наш.дом.рф | Какой объект принять
NO meme

### inline_5 — process_flow — Ипотека крутится, ключи стоят: что делать без паники
Labels: Иначе ипотека затянется | Претензия застройщику | Уведомление банку | Платежи не останавливать | Спор не закончен
Meme: this_is_fine_dog tiny corner

### inline_6 — labeled_checklist — Что сверить на ключах до подписи — таблица
Labels: Номер на двери | Этаж в ДДУ | План на этаже | Площадь и комнаты | Вид из окон
NO meme

### inline_7 — bar_timeline_chart — checklist continuation / priority bars
Labels: Табличка на двери | Фактический этаж | Графическое приложение | Замеры площади | Письменное объяснение
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
