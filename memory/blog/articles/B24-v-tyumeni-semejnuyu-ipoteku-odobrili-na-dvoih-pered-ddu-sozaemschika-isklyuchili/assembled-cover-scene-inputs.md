# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за 7 дней до ДДУ созaёмщика убрали — ипотеки не хватило
- hook (cover-text): «Банк убрал созaёмщика — денег не хватило» (highlight: «убрал»)
- sticky: «Одобрение ещё не деньги»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека одобрили на двоих → бронь новостройки → за 7 дней до ДДУ банк исключил второго супруга → лимит упал → на цену ДДУ и эскроу не хватает → подписание остановили

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека в тюмени» — 730
- «созaемщик ипотека» — 573
- «новостройки тюмень» — 4670

## meme_picks (from cover-text.json)

- cover: woman_yelling_cat
- inline_7: confused_math_lady

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room side_eye_chloe
- B22: lemon yellow shirt bank mortgage desk disaster_girl center full-body
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; woman_yelling_cat people-meme small sticker; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright newbuild sales lounge with floor plan — NOT bank desk duplicate, NOT handover room, NOT MFC).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Одобрили на двoих» — семья забронировала новостройку (pair with inline_2)
Labels: Новостройка на севере | Плата за бронь | Два дохода | Предварительное одобрение | Не финансы
NO meme — bright north Tyumen newbuild sales desk with reservation receipt and dual-income stamp

### inline_2 — comparison_table — pair with inline_1
Labels: Семь дней до подписи | Бронь тикает | Плата не на эскроу | Документы не деньги | Цена по ДДУ
NO meme

### inline_3 — realistic_photo — Перед подписанием банк исключил созaёмщика
Labels: В день подписания | Второго супруга убрали | Лимит пересчитали | Один доход | Проверка не закончена
NO meme — bright signing table: crossed-out co-borrower line on bank message, phone alert

### inline_4 — realistic_photo — Лимит упал — на ДДУ и эскроу не хватает
Labels: Цена ДДУ прежняя | Накопления те же | Разрыв по сумме | Не хватает денег | Эскроу ждёт сумму
NO meme — calculator gap between DDU price sticker and lowered approval amount

### inline_5 — structure_diagram — семейная ипотека, лимит, комбинированная схема
Labels: До 6 миллионов льготка | Взнос от 20 процентов | Лимит не одобрение | Схема сложнее | С февраля оба супруга
NO meme

### inline_6 — process_flow — Подписание остановили до перевода денег
Labels: ДДУ не подписан | На эскроу не перевели | Бронь может сгореть | Возврат по договору | Обязательств не появилось
NO meme

### inline_7 — labeled_checklist — Что проверить у обoих до брони
Labels: Кредитная история обoих | Состав заёмщиков письменно | Сумма и срок | Хватает ли денег | Условия возврата брони
Meme: confused_math_lady tiny corner

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
