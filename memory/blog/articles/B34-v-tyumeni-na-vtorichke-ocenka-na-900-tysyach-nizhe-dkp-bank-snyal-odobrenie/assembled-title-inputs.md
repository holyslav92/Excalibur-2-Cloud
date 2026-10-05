Assembled Title inputs — B34 — 2026-10-05

You ARE inside `excalibur_blog_derouter_opus_chat.py --role title`. Output **only** valid JSON for `title-brief.json` per SKILL.

topic_id: B34
slot_rubric: vtorichka (17:00 YEKT)
research_date: 2026-10-05
P0 Wordstat: «купить вторичное жилье в тюмени» — 749 (regions 55+11176)
sibling demand: «продажа квартир в тюмени вторичка» — 724; «ипотека тюмень вторичка» — 111
cluster: secondary_bank_appraisal_below_dkp_price_tyumen
viral_mechanism / klyshin energy: paper_clean_then_broke — на бумаге чисто (ЕГРН, предодобрение), остановка **до аванса**
mechanism: вторичка Тюмень, ДКП; предварительное одобрение ипотеки по доходу; чистая выписка ЕГРН; обязательная **банковская** оценка до аванса; отчёт на **900 000 ₽** ниже цены в проекте ДКП (иллюстрация 6,0 vs 5,1 млн); банк снял/приостановил предодобрение; аванс **не внесён**; кредит считают от меньшей из цены ДКП и оценки
comment_magnet_angle (Scout): «Если оценка на 900 тысяч ниже цены в ДКП — вы успеете договориться с продавцом или банк заберёт одобрение?»
Avoid dup: B06 (автооценка ЦИАН/Домклик, не банковский отчёт); B09 (ЕГРН обременение); B31 (новостройка + страховка); B33 (долг ЖКУ); published cluster «900 тыс ниже ДДУ» = новостройка — B34 = **900 тыс ниже ДКП**, вторичка

H1: news-casus Klyshin rhythm (завершённое событие + следствие); spell «900 тысяч»; вторичка/ипотека/оценка/ДКП/Тюмень; **no checklist head**, no «N шагов», no SEO tail «2026», no colon+keyword spam; ~50–70 chars; strong verb; subject clear (ипотека на вторичке / покупатель / банковская оценка)

published-titles-only.md in article dir — no cannibalization.

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"`
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + angle + slug>" --topic-id B34`

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B34",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```

Constraints:
- One headline; truth only from research-notes.md / spine above
- No naming bank/appraiser/address
- `comment_magnet_angle` = sharp Dzen debate question (можно адаптировать Scout angle)
