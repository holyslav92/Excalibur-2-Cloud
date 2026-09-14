# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик продал одну квартиру двум дольщикам — второму оставили только возврат брони
- hook (cover-text): «Одну квартиру забронировали дважды» (highlight: «дважды»)
- sticky: «Бронь не защищает»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: две брони на один условный номер → первая семья подписала ДДУ раньше → второй семье вернули 180 тыс. и предложили доплату 390 тыс. за «похожую» квартиру

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4 502
- «договор долевого участия» — 373
- «регистрация ДДУ» — 65

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: wojak
- inline_5: this_is_fine_dog
- inline_7: pepe_frog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (YESTERDAY — avoid bank desk duplicate)
- B25: terracotta shirt kneeling empty apartment
- B19: turquoise polo showroom knee-up cancel card
- B22: lemon shirt bank desk full-body center

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank mortgage desk like B26/B22; NOT showroom model like B19.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Одну планировку забронировали дважды — в одну неделю»
Labels: Одна неделя | Один номер | Две брони | Офис продаж | Бронь не в ЕГРН
Meme: wojak tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: На 11 дней раньше | ДДУ подписан | Эскроу открыт | Регистрация в ЕГРН | Три статуса
NO meme

### inline_3 — realistic_photo — «Первая семья подписала ДДУ на 11 дней раньше»
Labels: Четыре дня до эскроу | Лот занят | Другой дольщик | 180 тысяч бронь | Цену не вносили
NO meme — sales office desk two reservation receipts same unit number

### inline_4 — realistic_photo — «За четыре дня до эскроу второй семье сказали: лот занят»
Labels: Возврат 180 тысяч | Доплата 390 тысяч | Другая секция | Похожая планировка | Претензия семьи
NO meme — document closeup refund receipt and alternate floor plan

### inline_5 — structure_diagram — «Что защищает на каждом этапе — таблица»
Labels: Бронь без ЕГРН | Подписанный ДДУ | Зарегистрированный ДДУ | Эскроу после регистрации | Условный номер
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — «Бронь, регистрация ДДУ и эскроу: где рвётся цепочка»
Labels: Выбор квартиры | ДДУ и регистрация | Эскроу и цена | Проверка каждого шага | наш.дом.рф
NO meme

### inline_7 — bar_timeline_chart — protection timeline / chain break
Labels: Сверка брони и ДДУ | Подтверждение регистрации | Замена письменно | Пауза до доплаты | Рычаг до аванса
Meme: pepe_frog tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "cover_emotion", "alt" },
    "inline_1": { "scene_hint", "visual_type", "alt", "placement_group" },
    "inline_2": { "scene_hint", "visual_type", "alt", "placement_group" },
    "inline_3": { "scene_hint", "visual_type", "alt" },
    "inline_4": { "scene_hint", "visual_type", "alt" },
    "inline_5": { "scene_hint", "visual_type", "alt" },
    "inline_6": { "scene_hint", "visual_type", "alt" },
    "inline_7": { "scene_hint", "visual_type", "alt" }
  }
}
```
