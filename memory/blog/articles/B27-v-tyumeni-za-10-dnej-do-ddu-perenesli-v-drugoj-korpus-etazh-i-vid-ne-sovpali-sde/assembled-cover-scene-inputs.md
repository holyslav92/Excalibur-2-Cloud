# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась
- hook (cover-text): «Забронированный корпус заменили перед подписью» (highlight: «корпус»)
- sticky: «Семья отказалась»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: платная бронь 200 тыс. под корпус А 14 этаж вид на парк → за 10 дней до ДДУ корпус «заморожен» → проект ДДУ на корпус Б 6 этаж вид на кран −1,2 м² → семья отказалась → возврат брони 45 дней → до эскроу не дошли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 928
- «новостройки тюмень» — 4480
- «квартиры в тюмени новостройки» — 1137

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, crying_cat
- inline_1: woman_yelling_cat
- inline_5: wojak
- inline_7: change_my_mind

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в последних обложках.

**Recent covers to differ from:**
- B26: bank mortgage desk olive vest hide_pain_harold smudge_cat
- B25: empty apartment kneeling terracotta confused_math_lady cheems
- B22: bank mortgage desk lemon shirt disaster_girl keyboard_cat
- B23: handover room light blue shirt side_eye_chloe pop_cat

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank desk duplicate; NEW location (developer maquette room with two corps A/B swap OR bright sales pavilion with floor plan swap).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Полгода выбирали — корпус А, 14 этаж, вид на парк (pair with inline_2)
Labels: Корпус А | Четырнадцатый этаж | Вид на парк | Бронь 200 тысяч | Семейная ипотека
Meme: woman_yelling_cat tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Десять дней | Корпус заморожен | Новый проект ДДУ | Соседний корпус | Письменное объяснение
NO meme

### inline_3 — realistic_photo — «Корпус заморожен»
Labels: Корпус Б | Шестой этаж | Минус 1,2 м² | Вид на кран | Другой объект
NO meme — window view construction crane vs park

### inline_4 — realistic_photo — В проекте ДДУ другой корпус
Labels: Эскроу готовят | Срок одобрения | Другой корпус | Отказ от ДДУ | Не подписали
NO meme — bank escrow prep letter + unsigned DDU stack

### inline_5 — structure_diagram — Банк готовит эскроу — семья отказалась
Labels: Возврат 45 дней | Бронь 200 тысяч | Резерв снят | Не до эскроу | Письменное требование
Meme: wojak tiny corner

### inline_6 — bar_timeline_chart — Бронь 200 тыс, возврат 45 дней
Labels: Бронь и ДДУ | Корпус и секция | Этаж и номер | Площадь и план | наш.дом.рф
NO meme

### inline_7 — process_flow — Что сверять до подписания ДДУ
Labels: Сверка до подписи | Отказ нормален | Не под давлением | Документы рядом | Поиск продолжается
Meme: change_my_mind tiny corner

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
