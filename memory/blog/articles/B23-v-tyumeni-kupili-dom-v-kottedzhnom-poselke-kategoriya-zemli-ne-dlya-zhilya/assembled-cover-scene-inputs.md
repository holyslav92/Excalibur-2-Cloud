# Cover-scene inputs — B23

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B23
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени купили дом в коттеджном посёлке — категория земли не для жилья
- hook (cover-text): «Дом готов, ипотеку остановили перед ключами» (highlight: «остановили»)
- sticky: «ЕГРН остановил сделку»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья купила дом у застройщика в КП под «ИЖС под ключ», ДДУ+эскроу, дом готов, ипотека одобрена — но в выписке ЕГРН категория земли не для жилья → банк приостановил выдачу → Росреестр стоп → акт не подписали

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «коттеджные поселки тюмень» — 1832
- «выписка егрн земельный участок» — 134
- «категории земельных участков» — 125

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: side_eye_chloe
- inline_5: this_is_fine_dog
- inline_7: cheems

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в недавних обложках.

**Recent covers to differ from:**
- B22: lemon-yellow shirt bank mortgage desk disaster_girl keyboard_cat
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom knee-up cancel card
- B15: white shirt sand vest waist center envelope

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/showroom/MFC duplicate; NEW location (bright cottage village sales pavilion / land plot map table / sunny KP model home exterior with EGRN printout).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «ИЖС под ключ» в коттеджном посёлке — и семья подписала ДДУ (pair with inline_2)
Labels: Полчаса от города | ДДУ от застройщика | Эскроу-счёт | ИЖС под ключ | Категорию не спросили
Meme: side_eye_chloe tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Взнос внесён | Деньги на эскроу | Ипотека одобрена | Год спокойствия | Эскроу не заменяет статус
NO meme

### inline_3 — realistic_photo — Дом построен, ипотека одобрена — до ключей три недели
Labels: Три недели до ключей | Дом фактически готов | Дата акта назначена | Свежая выписка ЕГРН | Одобрение не равно выдаче
NO meme — nearly finished cottage exterior keys calendar

### inline_4 — realistic_photo — Выписка ЕГРН: категория земли не для жилья
Labels: Категория не та | ВРИ не ИЖС | ИЖС только в буклете | Земли населённых пунктов | Ипотека нужна сейчас
NO meme — EGRN printout highlighted wrong land category on bright desk

### inline_5 — structure_diagram — Банк приостановил выдачу, Росреестр поставил стоп
Labels: Выдачу приостановили | Назначение не подходит | Статья 26 закона | Пауза до трёх месяцев | Деньги на эскроу
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — «Перевод категории в процессе» — акт не подписали
Labels: Сроков нет | Акт не подписан | Претензия застройщику | Запрос в банк | Рычаг до подписи
NO meme

### inline_7 — bar_timeline_chart — Что сверить по участку до ДДУ и перед актом — таблица
Labels: Категория в ЕГРН | Вид использования | Территориальная зона | Охранные зоны | Выписка до ДДУ
Meme: cheems tiny corner

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
