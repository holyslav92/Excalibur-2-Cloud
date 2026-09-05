# Cover-scene inputs — B23

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B23
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени инвестор купил новостройку под сдачу — в ДДУ запретили аренду до ключей
- hook (cover-text): «Аренду запретили — бронь сгорела» (highlight: «сгорела»)
- sticky: «ДДУ прислали слишком поздно»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: инвестор бронирует однушку под аренду → ипотека одобрена → через 3 недели проект ДДУ с запретом аренды до акта + УК + комиссии → отказ от подписания → бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4660
- «переуступка новостройка» — 2469
- «сдавать квартиру в аренду в новостройке» — 55

## meme_picks (from cover-text.json)

- cover: confused_math_lady
- inline_1: success_kid (tiny corner)
- inline_5: doge (tiny corner)
- inline_7: this_is_fine_dog (tiny corner)

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B22: lemon shirt bank mortgage desk disaster_girl center full-body
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card
- B15: white shirt sand vest waist center envelope

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme small sticker; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright developer contract lounge with construction view, NOT bank/MFC/showroom duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — В договоре — запрет аренды до ключей (pair with inline_2)
Labels: Однушка под аренду | Запад Тюмени | Бронь внесена сразу | Ипотека одобрена | Доход с месяца
Meme: success_kid tiny corner — bright newbuild sales corner with reservation tablet

### inline_2 — comparison_table — pair with inline_1
Labels: Письмо за сутки | Полный проект ДДУ | Поиск слова аренда | Четыре скрытых условия | Не в буклете
NO meme — two-column table brochure vs DDU clauses

### inline_3 — realistic_photo — Инвестор бронирует однушку под сдачу
Labels: Запрет до акта | Согласование арендатора | Сдача через УК | Комиссия за сдачу | Договор при акте
NO meme — apartment floor plan with rental income calculator on desk

### inline_4 — realistic_photo — Через три недели присылают проект ДДУ
Labels: Аренда после ремонта | Комиссия сервиса | Переуступка с согласия | Комиссия 1–3 процента | Согласие банка
NO meme — email notification on laptop with thick DDU PDF stack

### inline_5 — process_flow — Доходность сдвигается, переуступка под вопросом
Labels: Отказ от подписания | Бронь невозвратная | Лот вернулся в продажу | Деньги не вернули | Сначала ДДУ
Meme: doge tiny corner — flowchart rental income vs booking loss

### inline_6 — bar_timeline_chart — Инвестор отказался от ДДУ: бронь сгорела
Labels: Урок без суда | ДДУ до брони | Второй застройщик | Полтора месяца | Деньги не заморожены
NO meme — timeline bars booking→DDU→refusal→loss

### inline_7 — structure_diagram — Что проверить в проекте ДДУ до брони
Labels: Поиск аренда и наём | Период запрета | Договор с УК | Комиссия переуступки | Договор бронирования
Meme: this_is_fine_dog tiny corner — checklist diagram with 5 nodes

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
