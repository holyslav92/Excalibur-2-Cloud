# Cover-scene inputs — B33

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B33
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой
- hook (cover-text): «Ребёнку семь — льгота может исчезнуть» (highlight: «льгота»)
- sticky: «Одобрили — но не финал»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека на новостройку → предварительное одобрение → бронь 150–250 тыс. → в день подписания ДДУ ребёнку 7 лет → банк на финале не подтверждает семейную программу (возраст на дату кредитного договора) → семья стопорит ДДУ/эскроу, бронь под риском

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека тюмень»
- «купить новостройку в тюмени»

## meme_picks (from cover-text.json — copy exactly)

- cover: surprised_pikachu
- inline_7: keyboard_cat
- inline_1, inline_5: no extra memes (cover-text does not assign)

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B29: ипотечный уголок лобби ЖК, two_buttons, голубая рубашка + горчичный жилет
- B28: павильон КП, roll_safe
- B27: офис продаж, terracotta overshirt

**Required:** light/bright #FFF high-key, sun flare; surprised_pikachu small sticker only on cover; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location — яркий детский праздничный уголок в светлом офисе сделки новостройки (шар «7», торт, календарь) рядом с папкой ДДУ и письмом банка о семейной ипотеке — NOT duplicate B29 mortgage corner.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Семейная ипотека на новостройку в Тюмени — пока ребёнку шесть, всё сходится» (pair with inline_2)
Labels: Ставка до 6% | Взнос от 20% | Лимит до 6 млн | ДДУ не кредит | Одобрение не финал
NO meme — светлый офис продаж, табличка условий семейной ипотеки, макет ЖК

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь 150–250 тыс | Срок по договору | День рождения — ДДУ | Предварительное одобрение | Не уже одобрили
NO meme — таблица: «до 6 лет на дату кредита» vs «день рождения = ДДУ»

### inline_3 — realistic_photo — Бронь оплачена, предварительное одобрение успокоило бюджет
Labels: Исполнилось семь | Финальная проверка | Возраст на кредит | Льготу не подтвердили | Бронь уже оплачена
NO meme — кухонный стол, чек брони, SMS банка «финальная проверка»

### inline_4 — realistic_photo — В день подписания ДДУ исполнилось семь
Labels: Семейную не подтвердили | Другая ставка | Больше своих денег | Стоп ДДУ и эскроу | Бронь не вернётся
NO meme — стол с ДДУ, торт с цифрой 7, письмо банка

### inline_5 — process_flow — Ставка и первый взнос пересчитали
Labels: День рождения | Кредитный договор | Подписание ДДУ | До шести включительно | Письменно от банка
NO meme — flowchart три даты

### inline_6 — bar_timeline_chart — Три даты, которые нельзя путать
Labels: Возраст ребёнка | Срок одобрения | Дата кредита | Порядок ДДУ | Условия брони
NO meme — timeline

### inline_7 — structure_diagram — Что зафиксировать до брони и ДДУ
Labels: Свои по кредиту | Плата за бронь | Деньги на эскроу | Сначала письмо банка | Потом бронь
Meme: keyboard_cat tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
