# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени в ДДУ зафиксировали трёшку — перед эскроу застройщик предложил двушку, семья остановила сделку
- hook (cover-text): «Перед эскроу трёшку заменили на двушку» (highlight: «трёшку»)
- sticky: «та же цена»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: в зарегистрированном ДДУ — трёшка с планом; накануне эскроу менеджер предлагает двушку по той же цене; семья не открывает эскроу; бронь сняли, лот ушёл, ипотека истекла через 19 дней

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «планировки квартир новостройка» — 1825
- «новостройки тюмень купить» — 2410
- «эскроу новостройка» — 468

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, crying_cat
- inline_1: wojak
- inline_5: blinking_white_guy
- inline_7: james_doakes

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (waist-up right)
- B25: terracotta shirt kneeling bare apartment confused_math_lady
- B23: light blue shirt handover room side_eye_chloe
- B22: yellow shirt bank mortgage disaster_girl full-body center

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/showroom duplicate; NEW location (bright developer sales office with two floor plans side by side — 3-room vs 2-room — and escrow application folder).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «В зарегистрированном ДДУ — трёшка с планом и условным номером» (pair with inline_2)
Labels: Три комнаты | План в приложении | Условный номер | Регистрация ДДУ
Meme: wojak tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Двухкомнатная квартира | Та же цена | Банковский комплект | Меняется предмет
NO meme — table comparing 3-room DDU vs 2-room bank pack

### inline_3 — realistic_photo — «Накануне эскроу менеджер предлагает двушку по той же цене»
Labels: Два комплекта | Эскроу не открыли | Банк не подписали | Деньги не ушли
NO meme — bright desk with two document stacks DDU vs bank

### inline_4 — realistic_photo — «Семья не открывает эскроу и не подписывает банковский комплект»
Labels: Бронь сняли | Лот ушёл | 19 дней одобрения | Ипотека истекла
NO meme — calendar showing 19 days, cancelled reservation stamp

### inline_5 — bar_timeline_chart — «Бронь сняли, лот ушёл, ипотечное одобрение истекло через 19 дней»
Labels: Эскроу не предмет | ДДУ не исправит | Бронь не заменит | Разные этапы
Meme: blinking_white_guy tiny corner

### inline_6 — process_flow — «Эскроу защищает деньги, но не подменяет предмет в ДДУ»
Labels: Три комнаты | Две комнаты | Площадь меньше | Цена та же
NO meme — flow: DDU object → escrow money → different object FAIL

### inline_7 — structure_diagram — «Что сверять перед эскроу — таблица трёшки в договоре и двушки в банке»
Labels: План из ДДУ | Объект в банке | Не подписывать вслепую | Сроки договора
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
