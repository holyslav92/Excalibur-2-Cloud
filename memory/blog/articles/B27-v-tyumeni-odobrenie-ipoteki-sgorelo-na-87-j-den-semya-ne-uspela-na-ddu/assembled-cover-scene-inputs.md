# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались
- hook (cover-text): «Ипотека сгорела — договор не дождались» (highlight: «сгорела»)
- sticky: «Три месяца ожидания зря»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительное одобрение ипотеки → бронь новостройки → три переноса «на следующей неделе» → на 87-й день пришёл проект ДДУ, но банк закрыл старое решение → переодобрение хуже → семья сняла бронь до аванса

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «ипотека тюмень новостройки от застройщика» — 100
- «срок одобрения ипотеки» — 48
- «одобрение ипотеки новостройка» — 54

## meme_picks (from cover-text.json)

- cover: wojak, woman_cat_yelling_cat_half
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: james_doakes

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (tranche denied)
- B25: terracotta shirt kneeling bare apartment measuring tape
- B22: lemon shirt bank rate letter disaster_girl
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; wojak people-meme + woman_cat_yelling_cat_half small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank desk duplicate; NEW location (bright developer sales lounge with queue ticket + wall calendar showing day 87).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — семья в очереди на ДДУ (pair with inline_2)
Labels: Бронь оформлена | Предварительное одобрение | Ставка и платёж | Ждут договор | Одобрение не выдача
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Три переноса | Переписка с менеджером | Даты подписания нет | Отсчёт банка идёт | Почти три месяца
NO meme

### inline_3 — realistic_photo — «На следующей неделе» трижды — почти три месяца
Labels: Договор пришёл | Решение закрыто | Личный кабинет банка | Файл не сохраняет ставку | Эскроу не открывали
NO meme — bright laptop showing closed bank decision + DDU PDF arriving same evening

### inline_4 — realistic_photo — На 87-й день пришёл проект ДДУ, банк закрыл решение
Labels: Новая заявка | Сумма меньше | Ставка выше | Платёж не тянут | Бронь сняли
NO meme — re-approval form with lower sum and higher rate on bright desk

### inline_5 — process_flow — Переодобрение: меньше сумма, выше ставка
Labels: Почти три месяца ждали | Договор прислали | Новый платёж | Условия брони | Отказ до подписи
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Таблица: что проверить, пока ждёте ДДУ
Labels: Срок одобрения | Продление у менеджера | Готовность договора | Условия брони | Расчёт покупки
NO meme

### inline_7 — structure_diagram — Бронь, одобрение и эскроу: три календаря
Labels: Квартира за нами | Разные сроки | Решение закрыто | Пауза до аванса | Проверка до подписи
Meme: james_doakes tiny corner

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
