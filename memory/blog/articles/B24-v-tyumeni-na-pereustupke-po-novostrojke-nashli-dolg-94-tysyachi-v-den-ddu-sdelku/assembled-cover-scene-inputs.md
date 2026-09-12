# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени на переуступке нашли долг 94 тысячи — сделку остановили
- hook (cover-text): «Долг сорвал сделку с квартирой» (highlight: «сорвал»)
- sticky: «Бумаги были чистыми»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: инвестор на второй переуступке, копии ДДУ «чистые», но в день подписания застройщик находит 94 000 ₽ долга первого дольщика в цепочке — сделка стоп, бронь 50 000 не вернули

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3634
- «купить новостройку в тюмени» — 662
- «переуступка по дду» — 15

## meme_picks (from cover-text.json)

- cover: this_is_fine_dog, nihilist_penguin
- inline_1: disappointed_black_guy
- inline_5: expanding_brain
- inline_7: yelling_at_clouds

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в последних обложках.

**Recent covers to differ from:**
- B23: light blue shirt handover room EGRN vs DDU side_eye_chloe (full-body right)
- B22: yellow shirt bank mortgage desk disaster_girl (full-body center)
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; this_is_fine_dog + nihilist_penguin small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/handover room duplicate; NEW location (bright glass sales pavilion at active construction site — reassignment signing desk with developer rep folder, NOT keys handover).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Копии ДДУ лежали в папке, ключи через 11 дней (pair with inline_2)
Labels: Инвестиция в новостройку | Расчёт закрыт | Второй покупатель | Исходный ДДУ | Нужна сверка
Meme: disappointed_black_guy tiny corner

### inline_2 — bar_timeline_chart — pair with inline_1
Labels: До ключей 11 дней | Копии в папке | График не виден | Согласие застройщика | Аккредитив после регистрации
NO meme — timeline bar chart showing 11 days to keys vs hidden payment schedule gap

### inline_3 — realistic_photo — Инвестор купил переуступку — и через месяц нашёл второго покупателя
Labels: Акт сверки | Долг 94 000 ₽ | Первый дольщик | Не тот плательщик | Сделку остановили
NO meme — bright desk with reconciliation act showing 94 000 ₽ and STOP stamp, chain of DDU folders

### inline_4 — realistic_photo — В день подписания застройщик открыл 94 тысячи — не того, с кем платили
Labels: Бронь 50 000 ₽ | Покупатель ушёл | Возврат не автоматический | Договор брони | Сделка сорвана
NO meme — empty signing room with cancelled reservation card 50 000 and abandoned chair

### inline_5 — comparison_table — Бронь 50 тысяч не вернули, второй покупатель ушёл
Labels: Полная оплата ДДУ | Перевод долга | Согласие застройщика | Три стороны | Доплата
Meme: expanding_brain tiny corner — two-column comparison simple cession vs debt transfer

### inline_6 — process_flow — Простая цессия или перевод долга — где ломается цепочка
Labels: Свежий акт сверки | Первый дольщик | Тип уступки | Ипотека продавца | 7–10 дней регистрации
NO meme — flow diagram: investor → seller → first dolfshchik chain break at developer check

### inline_7 — structure_diagram — Что проверить до аванса по переуступке — таблица
Labels: Сначала сверка | Потом согласия | Безопасный расчёт | Не на карту | Проверка до аванса
Meme: yelling_at_clouds tiny corner — checklist structure before advance payment

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
