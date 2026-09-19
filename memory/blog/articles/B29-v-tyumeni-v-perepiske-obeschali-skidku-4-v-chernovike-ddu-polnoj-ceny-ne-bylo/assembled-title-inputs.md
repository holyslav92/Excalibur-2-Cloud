# Assembled title inputs — B29 (Derouter title role)

**topic_id:** B29  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `v-tyumeni-v-perepiske-obeschali-skidku-4-v-chernovike-ddu-polnoj-ceny-ne-bylo`  
**research_date:** 2026-09-19

## Scout title draft (starting point — sharpen to Klyshin news-casus, ~50–70 chars)

В Тюмени в переписке обещали скидку 4% — в черновике ДДУ полной цены не было

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_crm_promo_discount_not_in_ddu_draft`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none | original: none (Klyshin not used)
- **comment_magnet_angle (Scout):** «Скрин переписки со скидкой — это обещание застройщика или просто реклама?»

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank, manager)

1. Family buying **квартиру в строящемся ЖК** по **ДДУ 214-ФЗ**, ипотека, **эскроу**
2. Manager in CRM chat / messenger confirmed **скидка 4%** or promo price
3. Received **draft DDU** with **full list price** — no discount clause or price amendment
4. **3 days** before planned **escrow opening**
5. Risk: ~**580–620 тыс. ₽** overpay (illustration only) + possible **booking loss**
6. **Stopped deal**, did **not** open escrow; demanded corrected DDU or written discount before signing

## voice_angle (research)

«Скидка в чате, полная цена в ДДУ»: budget counted on promo; escrow gets **contract price**, not chat screenshot.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4430 |
| купить новостройку в тюмени | 920 (final P0) |
| новостройки в тюмени от застройщика | 663 |
| скидка застройщик новостройка | 3 (weak — not H1) |

Spine = покупка новостройки Тюмень; механизм = переписка/CRM vs **проект ДДУ** / **эскроу** / цена по 214-ФЗ.

## Anti-dupe (published siblings)

- **B28:** газ в брони vs декларация 2028 — **другой plot**
- **B27:** земля аренда vs собственность в декларации
- **B25:** отделка в ДДУ vs приёмка
- **B22:** ставка ипотеки перед ДДУ
- **B29 уникален:** скидка 4% в переписке не попала в черновик ДДУ → стоп за 3 дня до эскроу

## Published titles (anti-repeat — not style template)

- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали
- B22: В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела

## Champion energy (formula, not copy)

Завершённое событие + противоречие документов (чат vs ДДУ) + следствие (остановили сделку / не открыли эскроу).

## Klyshin scream (HARD for this slot)

- **Цифра + удар во второй такт:** «4%», «3 дня», «полная цена» — не SEO «2026»
- Первая часть — скидка/переписка/Тюмень; вторая — черновик ДДУ / эскроу / отказ
- ~50–70 символов; сильный глагол; subject = новостройка / ДДУ / скидка / эскроу
- Scout draft длинноват — **сжать**, сохранив stakes

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"`
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + hook + slug>" --topic-id B29`

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B29",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```

Constraints:
- One headline; Klyshin news-casus rhythm; truth **only** from spine above
- No SEO tail, no «чеклист», no «2026» in h1, no colon+keyword spam
- No naming specific ЖК/developer/bank/manager
- `comment_magnet_angle` = sharp debate question for Dzen (adapt Scout angle: скрин vs реклама vs договор)

## Invocation context (mandatory)

You are **gpt-6-astra**, the Derouter powerful **title** model. This request already reached you via `excalibur_blog_derouter_opus_chat.py`. You are NOT the Cursor conductor.

**Forbidden in your reply:** `DEROUTER TITLE BLOCKER`, null `h1`/`title`, excuses about missing API access.

**Required:** one JSON object only; `h1` and `title` identical non-empty Russian headline (~50–70 chars); `verdict`: `"PASS"`.
