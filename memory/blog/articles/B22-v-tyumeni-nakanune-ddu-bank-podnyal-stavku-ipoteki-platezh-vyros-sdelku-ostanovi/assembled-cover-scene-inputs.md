# Cover-scene inputs — B22

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B22
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела
- hook (cover-text): «Банк поднял ставку — платёж вырос» (highlight: «ставку»)
- sticky: «Одобрение не гарантия»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительное одобрение ипотеки → бронь новостройки → за 48 часов до ДДУ банк поднял ставку → платёж +15–20 тыс. → бюджет не сходится → отказ от ДДУ → бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «ипотека в Тюмени на новостройки» — 41
- «ставка ипотеки новостройка» — 54
- «ипотека на новостройку процентная ставка» — 21

## meme_picks (from cover-text.json)

- cover: disaster_girl, keyboard_cat
- inline_1: success_kid
- inline_5: doge
- inline_7: this_is_fine_dog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B20: terracotta overshirt MFC corridor two DDU INN (two_buttons)
- B19: turquoise polo showroom knee-up cancel card
- B15: white shirt sand vest waist center envelope
- B12: light blue shirt showroom waist right

**Required:** light/bright #FFF high-key, sun flare; disaster_girl people-meme + keyboard_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT MFC/showroom duplicate; NEW location (bank rate letter / mortgage desk / bright sales office with rate chart).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Семья развернулась: бронь сгорела, квартира ушла (pair with inline_2)
Labels: Север Тюмени | Бронь оплачена | Предварительное одобрение | Платёж в бюджете | Не договор
Meme: success_kid tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь до ДДУ | Квартиру фиксирует | Ставку не фиксирует | Одобрение 30–90 дней | Ставка ЦБ 14%
NO meme

### inline_3 — realistic_photo — «Ипотеку одобрили» — и семья забронировала новостройку
Labels: Письмо в четверг | Подписание в субботу | Ставка выше | Скидку сняли | Срочный звонок
NO meme — bright newbuild sales desk reservation receipt

### inline_4 — realistic_photo — Между одобрением и ДДУ бронь отсчитывает дни
Labels: Плюс 15–20 тысяч | Бюджет не сходится | Кредит урезали | Денег нет | Нагрузка растёт
NO meme — calendar countdown + mortgage approval letter aging

### inline_5 — structure_diagram — За 48 часов до подписания банк поднял ставку
Labels: Семейная ипотека | До 6 процентов | Лимит 6 миллионов | Вторая часть дороже | Одна льготка
Meme: doge tiny corner

### inline_6 — process_flow — Платёж вырос — первоначальный взнос перестал сходиться
Labels: Платёж не тянут | Отказ от ДДУ | Бронь истекла | Деньги не вернули | Кредит не подписан
NO meme

### inline_7 — bar_timeline_chart — Что проверить до подписания ДДУ — таблица
Labels: Проверьте срок | Условия на бумаге | Причину пересчёта | Условия брони | Кредит перед бронью
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
