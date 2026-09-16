# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени банк отказал созаёмщику по семейной ипотеке — за 4 дня до эскроу сделку остановили
- hook (cover-text): «Банк отказал созаёмщику перед эскроу» (highlight: «отказал»)
- sticky: «Одобрение не гарантия»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека предодобрена на двоих → за 4 дня до эскроу банк отклоняет созаёмщика → лимита без второго дохода не хватает → ДДУ не подписан → бронь снята → квартира ушла через 11 дней

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека тюмень» — 1240
- «созаемщик ипотека» — 515
- «купить новостройку в тюмени» — 902

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, crying_cat
- inline_1: roll_safe
- inline_5: wojak
- inline_7: this_is_fine_dog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive knit vest bank desk waist-up right hide_pain_harold (YESTERDAY — avoid same bank desk waist-up)
- B25: terracotta shirt kneeling apartment measuring tape
- B22: lemon yellow shirt full-body center mortgage desk
- B23: light blue shirt mustard sweater handover room

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT duplicate bank waist-up like B26.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Родителя в созаёмщики не пустили: бронь сняли, квартира ушла через 11 дней
Labels: Семейная ипотека | До шести процентов | Взнос от двадцати | Предодобрение на двоих | Бронь не кредит
Meme: roll_safe tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Четыре дня до эскроу | Финальная проверка | Отказ созаёмщику | Причина неизвестна | ДДУ не подписали
NO meme — columns «предодобрение на двоих» vs «финальная проверка отказ»

### inline_3 — realistic_photo — Почему с февраля 2026 супругов нельзя «выключить» из семейной ипотеки
Labels: Одного дохода мало | Жену убрать нельзя | С февраля вместе | Лимит не хватил | Эскроу не открыли
NO meme — bright MFC desk with dual borrower application forms, no people

### inline_4 — realistic_photo — «Одобрили на двоих» — и семья забронировала новостройку в Тюмени
Labels: Третий созаёмщик | Родитель не прошёл | Новая заявка | Бронь без штрафа | Ушла за одиннадцать дней
NO meme — newbuild sales office reservation card + family mortgage folder on bright counter

### inline_5 — structure_diagram — За четыре дня до эскроу банк отказал жене-созаёмщику
Labels: С февраля вместе | Исключения редкие | Третий не обход | Банк проверяет всех | Льготка не сумма
Meme: wojak tiny corner

### inline_6 — process_flow — Лимита без второго дохода не хватило — ДДУ так и не подписали
Labels: Оба в заявке | Запас по доходу | Срок предодобрения | Бронь письменно | Финал до подписи
NO meme — numbered steps from dual approval to co-borrower rejection to unsigned DDU

### inline_7 — bar_timeline_chart — Что проверить до брони и подписания ДДУ — таблица
Labels: Финал по всем | Срок брони | Третий — документы | Деньги не ушли | Кредит перед бронью
Meme: this_is_fine_dog tiny corner

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
