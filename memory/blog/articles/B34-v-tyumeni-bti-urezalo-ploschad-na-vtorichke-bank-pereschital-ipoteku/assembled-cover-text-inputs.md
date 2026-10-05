# Cover-text B34 — vtorichka Tyumen

Slot rubric: **vtorichka** (вторичка, ипотека, ДКП, ЕГРН, БТИ).

## Casus (facts for labels)
- Свежий акт БТИ: **48 м²** вместо **54 м²** в объявлении (−6 м²) на вторичке в Тюмени.
- Ипотека одобрена под 54 м²; банк пересчитал лимит, попросил добрать взнос за сутки до нотариуса.
- ДКП не подписали; аванс не ушёл с карты.
- Порядок: обмер БТИ **до** аванса, сверка объявление / ЕГРН / БТИ.

## title-brief.json
```json
{
  "topic_id": "B34",
  "h1": "В Тюмени на вторичке акт БТИ снял 6 м² — ипотека сорвала ДКП",
  "subject": "акт БТИ, расхождение площади квартиры и пересчёт ипотеки на вторичке в Тюмени",
  "angle": "Свежий акт БТИ выявил недостачу 6 м² перед подписанием ДКП: банк пересчитал ипотеку, и сделка не состоялась."
}
```

## Hook canon
- ONE line, **5–7 кириллических слов**, prefer words ≥5 letters.
- Plain Russian: кто + что случилось (БТИ/метры/ипотека/вторичка).
- `highlight` — одно слово из hook.
- `sticky` — до 5 слов, реакция.
- Cover phone CTA: +7 922 001 65 05 (tenant canon).

## wordstat_stickers (Tyumen secondary)
- квартира тюмень вторичка
- обмер бти квартира
- проверить егрн квартира

## meme_picks (HARD)
- Only ids from `memory/cover/meme-top100.json`.
- **People + cats** (NOT cats-only). On-topic funny: shock at −6 m², bank recalc, deal collapse.
- Slots: `cover` (1–2), `inline_1`, `inline_5`, `inline_7`.
- BANNED: drake, drake_no_yes, salt_bae, stock_handsome_man.
- Avoid repeating same meme ids from recent covers in used-motifs (14d): roll_safe, smudge_cat, hide_pain_harold, confused_math_lady, grumpy_cat, two_buttons, crying_cat, disappointed_black_guy, this_is_fine_dog — prefer fresh picks like `stonks`, `this_is_fine`, `surprised_pikachu`, `woman_yelling_at_cat`, `expanding_brain`, `success_kid`, `wheezing_laugh`, `doge`, `cheems` (if not overused).

## inline_labels
3–6 коротких подписей (1–4 слова) на панель для inline_1 … inline_7 по сюжету статьи (54→48, БТИ, банк, нотариус, без аванса).

Output ONLY valid JSON matching cover-text schema (no markdown fences).
