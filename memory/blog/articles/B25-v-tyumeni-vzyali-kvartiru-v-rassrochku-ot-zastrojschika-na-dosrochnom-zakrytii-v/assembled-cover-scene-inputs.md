# Cover-scene inputs — B25

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B25
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку
- hook (cover-text): «Досрочный платёж сделал квартиру дороже» (highlight: «дороже»)
- sticky: «Вот такая рассрочка»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья 4 месяца платила рассрочку, привезла остаток досрочно — комиссия ~10%, скидка сгорела, цена по сентябрьскому прайсу, ДДУ не подписали, бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «рассрочка от застройщика тюмень» — 143
- «купить квартиру в рассрочку от застройщика» — 33
- «рассрочка от застройщика» — 21301 (РФ)

## meme_picks (from cover-text.json)

- cover: confused_math_lady, pop_cat
- inline_1: disappointed_black_guy
- inline_5: james_doakes
- inline_7: side_eye_chloe

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B22: lemon shirt mortgage desk disaster_girl keyboard_cat
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom knee-up cancel card
- B15: white shirt sand vest waist center envelope

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + pop_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer sales office with installment payment schedule / early payoff calculation printout — NOT bank/MFC/showroom duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ноль процентов» и обещание закрыть рассрочку без штрафов (pair with inline_2)
Labels: Рассрочка вместо ипотеки | Ноль процентов сверху | Скидка по акции | Штрафов не будет
Meme: disappointed_black_guy tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Деньги до регистрации | Бронь не защищает | Эскроу ещё не открыт | Разрыв в защите
NO meme

### inline_3 — realistic_photo — Через четыре месяца семья принесла остаток досрочно
Labels: Четыре месяца платежей | Продали машину | Остаток целиком | Привезли деньги
NO meme — bright sales office, family bringing cash envelope for early payoff

### inline_4 — realistic_photo — Менеджер сменился, новая распечатка
Labels: Другой менеджер | Две страницы расчёта | Досрочное закрытие | Обещание устно
NO meme — two-page printout on desk, new manager, quiet tension

### inline_5 — structure_diagram — Скидку сняли, цену пересчитали — бронь сгорела
Labels: Комиссия около 10% | Скидка сгорела | Сентябрьский прайс | Бронь сгорела
Meme: james_doakes tiny corner

### inline_6 — process_flow — Где в договоре прячется комиссия за досрочное закрытие
Labels: Четыре места проверки | Бронь и график | Раздел расчётов | Условия акции
NO meme

### inline_7 — labeled_checklist — Что спросить письменно до первого перевода
Labels: Досрочно полностью | Комиссия цифрой | Скидка сохраняется | Деньги при отказе | Срок регистрации
Meme: side_eye_chloe tiny corner

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
