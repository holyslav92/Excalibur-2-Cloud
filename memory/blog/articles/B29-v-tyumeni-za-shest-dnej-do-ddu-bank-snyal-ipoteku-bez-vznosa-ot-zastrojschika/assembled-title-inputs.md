# Assembled title inputs — B29 (Derouter title role, powerful tier)

## CRITICAL EXECUTION CONTEXT

You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier gpt-6-astra). Output **JSON only** per schema below. Do not refuse or emit DEROUTER TITLE BLOCKER — you ARE the Derouter title role.

## Task

Invent ONE H1/title for topic B29. `verdict` must be `"PASS"`.

**topic_id:** B29  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** `v-tyumeni-za-shest-dnej-do-ddu-bank-snyal-ipoteku-bez-vznosa-ot-zastrojschika`  
**research_date:** 2026-09-19

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_developer_zero_down_program_expired_before_ddu_tyumen`
- **top_energy_mirror:** `clock_ran_out`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none
- **newbuild_mechanism:** квартира в новостройке Тюмени; в офисе продаж обещали «ипотека без первоначального взноса от застройщика» / субсидированная банковская программа; ипотеку предварительно одобрили на этих условиях; **за 6 дней до ДДУ** банк сообщил, что программа/квота/акция закончилась; платёж вырос примерно на **18 000 ₽**; семья не успела собрать первоначальный взнос; сделка остановилась **до эскроу**; из платы за бронь удержали ориентировочно **50 000–80 000 ₽** (composite casus)
- **comment_magnet_angle (Scout):** «Если банк снимает “нулевой взнос” за неделю до ДДУ, вы бы торопились подписать или ждали, пока застройщик вернёт программу?»
- **title draft (rework allowed):** В Тюмени за шесть дней до ДДУ банк снял ипотеку без взноса от застройщика — семья не успела собрать первоначальный платёж

## Editorial spine (composite Tyumen casus — no ЖК, bank, developer names)

1. Family paid booking on Tyumen newbuild; sales office promised zero/minimal down via developer-linked subsidy
2. Preliminary mortgage approval on promo terms
3. Six days before planned DDU — bank: program/quota ended; recalculated loan
4. Monthly payment up ~18k; required down payment appears; family cannot fund in time
5. No DDU, no escrow; booking fee dispute (partial withhold 50–80k in casus model)
6. Conflict: what was in writing — booking contract, promo validity, bank decision vs manager words

## voice_angle (research)

«Нулевой взнос» в офисе продаж может быть не финальным условием, а таймером: акция и квота банка заканчиваются, пока бронь оплачена, а эскроу пустой.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| ипотека от застройщика тюмень | 514 |
| ипотека от застройщика | 715 |
| ипотека без первоначального взноса тюмень от застройщика | 197 |
| ипотека от застройщика без взноса | 210 |

Spine = ипотека от застройщика / Тюмень; механизм = нулевой ПВ, субсидия, бронь, ДДУ, эскроу.

## Anti-dupe (published siblings — not style template)

- **B22:** банк **поднял ставку** ипотеки перед ДДУ — платёж вырос, бронь сгорела (**другой механизм** — не zero-down program expiry)
- **B27:** земля аренда vs собственность в декларации, 4 дня до ДДУ
- **B28:** газ в брони vs декларация 2028, потеря 60k брони
- **B29 уникален:** исчезновение схемы «ипотека без взноса от застройщика» за 6 дней до ДДУ + невозможность собрать ПВ + стоп до эскроу

## Champion energy (formula, not copy)

Завершённое событие + дедлайн + следствие для покупателя (Klyshin news-casus rhythm).

## Klyshin scream (HARD for this slot)

- **Цифра + удар во второй такт:** «6 дней», «18 тысяч», «без взноса» — не календарный SEO «2026» в H1
- Первая часть — Тюмень/новостройка/ипотека от застройщика; вторая — банк снял условие / семья не успела / бронь
- ~50–70 символов; сильный глагол; subject = ипотека без взноса / ДДУ / новостройка

## Gates (run after JSON)

- `python3 scripts/excalibur_blog_topic_focus.py --text "<h1>"`
- `python3 scripts/excalibur_blog_scout_story_dup.py --text "<h1 + mechanism + slug>" --topic-id B29`

## FORBIDDEN H1 hooks

чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

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
- One headline; news-casus rhythm; facts only from spine above
- No SEO tail, no «чеклист», no «2026» in h1
- No naming specific ЖК/developer/bank
- Must differ clearly from B22 (rate hike) — here zero-down/subsidy program ends
- `comment_magnet_angle` = sharp Dzen debate question (adapt Scout angle)
