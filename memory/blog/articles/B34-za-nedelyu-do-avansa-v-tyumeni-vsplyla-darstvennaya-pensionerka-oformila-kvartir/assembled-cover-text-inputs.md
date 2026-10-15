# Cover-text B34 — вторичка Тюмень, дарственная перед авансом

## Gate rules (HARD)
- hook: ONE line, 5–7 Cyrillic words (short headline), highlight = one word FROM hook
- sticky: ≤5 words
- phone_cta on cover: +7 922 001 65 05
- wordstat_stickers: 1–3 live Wordstat Tyumen phrases (see below)
- inline_labels: inline_1 … inline_7, each 2–6 labels, each label 1–4 words, Cyrillic
- meme_picks: dict slots only — cover (1–2 ids), inline_1, inline_5, inline_7 — real ids from memory/cover/meme-top100.json; people+cats variety (not cats-only); BANNED: drake, drake_no_yes, salt_bae, stock_handsome_man; anti-repeat 14d (avoid hide_pain_harold, smudge_cat, roll_safe, grumpy_cat, confused_math_lady, disappointed_black_guy, this_is_fine_dog, two_buttons, crying_cat heavily used in last 14d)

## Wordstat (live 2026-09-29, Tyumen 55+11176)
- «оформление квартиры на родственника» — 21
- «купить квартиру в тюмени вторичка» — 3413
- «дарение близкому родственнику» — (supporting, research)

## title-brief.json
```json
{
  "h1": "В Тюмени дарственная остановила сделку за 7 дней до аванса",
  "angle": "Чистая выписка ЕГРН не сняла риск: юрист обнаружил недавний подарок квартиры от матери сыну-продавцу до внесения аванса."
}
```

## Story spine (from article.html)
- Двушка, ипотека одобрена, торг согласован, аванс 420 000 ₽ через неделю
- ЕГРН: один собственник, обременений нет — но не показывает основание права
- ~4 месяца назад мать-пенсионерка подарила квартиру сыну; сейчас продажа
- Семья не внесла аванс, сделку остановили до проверки документов
- С 13 января 2025 — нотариальная форма дарения (459-ФЗ, ст. 574 ГК)
- Давление сроков семейной ипотеки к 1 октября 2026

## H2 map for inline_labels
- inline_1: ипотека одобрена, двушка, аванс через неделю, семейная ипотека октябрь
- inline_2: ЕГРН без обременений, один собственник, не вся история
- inline_3: дарственная от матери, 4 месяца назад, пенсионерка, юрист запросил цепочку
- inline_4: аванс 420 тысяч, неделя до встречи, пауза без денег
- inline_5: нотариус с 2025, договор дарения, 459-ФЗ, сверка с ЕГРН
- inline_6: запросить договор, позиция дарительницы, не торопиться с авансом
- inline_7: таблица документов, договор дарения, выписка переходов, до передачи денег

## Hook direction (examples, do not copy verbatim if gate fails)
- «Дарственная остановила сделку за неделю» (6 words)
- «Мать подарила квартиру — аванс стоп» (5 words)

Output valid JSON only to cover/cover-text.json fields: hook, highlight, sticky, phone_cta, wordstat_stickers, inline_labels, meme_picks.
