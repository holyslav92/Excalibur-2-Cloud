# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня
- hook (cover-text): «Переуступка сорвалась — аванс вернули частично» (highlight: «аванс»)
- sticky: «Сначала согласие застройщика»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья перевела 350 тыс. аванса цеденту на личный счёт → за 3 дня до оформления застройщик не согласовал уступку → вернули 120 тыс., 230 удержали → квартира ушла другому покупателю

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в Тюмени» — 902
- «купить новостройку в тюмени от застройщика» — 456
- «переуступка новостройки» — 18

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: wojak
- inline_5: this_is_fine_dog
- inline_7: doge

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive knit vest bank mortgage desk denied tranche (YESTERDAY — avoid bank desk duplicate)
- B25: kneeling tape measure bare apartment walls
- B23: handover room side_eye keys
- B22: lemon shirt mortgage calculator
- B20: MFC corridor two_buttons

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT sales showroom knee-up like B19.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Скидка к прайсу» — и 350 тысяч ушли первому дольщику
Labels: Цена ниже прайса | 350 тысяч аванс | Личный счёт | Не эскроу | Права по ДДУ | Офис продаж
Meme: wojak tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: 19 дней ожидания | Согласования нет | ДДУ и справка | Долг по ипотеке | Нужен письменный ответ
NO meme

### inline_3 — realistic_photo — За три дня до оформления — несогласование и цена напрямую от застройщика
Labels: За 3 дня | Уступка не согласована | Встреча не сделка | Плюс 420 тысяч | Напрямую застройщик
NO meme — sales office glass door refusal stamp vs price tag

### inline_4 — realistic_photo — Девятнадцать дней аванса: согласования в офисе продаж ещё не было
Labels: Другой покупатель | Уступку согласовали | Квартира потеряна | 230 тысяч удержали | Комиссия без прав
NO meme — calendar 19 days + empty consent folder on desk

### inline_5 — process_flow — Вернули 120 тысяч, 230 удержали: квартира ушла другому покупателю
Labels: Вернули 120 тысяч | Удержали 230 тысяч | Соглашение и переписка | Назначение платежа | Претензия по остатку
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Что проверить до перевода по переуступке — таблица
Labels: Деньги на эскроу | Аванс цеденту | Справка об оплате | Соглашение до перевода | Условия возврата
NO meme

### inline_7 — structure_diagram — Эскроу, цессия и «согласие»: где ломается цепочка
Labels: Регистрация уступки | Согласие застройщика | Полная оплата ДДУ | Защищённый расчёт | Пауза до перевода
Meme: doge tiny corner

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
