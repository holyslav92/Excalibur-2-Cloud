# Description inputs — B24 — 2026-09-12

## Task
You are Derouter description agent (gpt-6-astra). Derouter API is live — write the teaser now.
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.
Forbidden: BLOCKER, null description, refusal, meta about environment/tools.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль

**subject:** ДДУ на новостройку и счёт эскроу

**angle:** Сумма 4,2 млн рублей уже указана в ДДУ, но за неделю до подписания на эскроу-счёте оказался нулевой остаток. Банк остановил сделку, а застройщик предложил заплатить повторно.

**comment_magnet_angle:** Если менеджер обещает сам положить деньги на эскроу, подписывать ДДУ или сначала требовать выписку по счёту?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За семь дней до подписания ДДУ банк увидел на эскроу ноль — хотя в проекте договора стояли 4,2 млн рублей. Семья уже отправила крупный первоначальный взнос на реквизиты застройщика и услышала от менеджера: «Потом зачтём в эскроу». На финальной проверке выяснилось, что перевод застройщику и деньги на специальном банковском счёте — разные вещи. Сделку остановили, а семье предложили внести 4,2 млн повторно, уже на эскроу.

**Para 2 (early CTA):** Я разбираю такие ситуации в Telegram The Риэлтор, Тюмень. Короткие разборы и рабочие материалы также выходят в MAX.

## Case hook (from research / article)
- Тюмень, новостройка, семья с ипотечным одобрением
- В проекте ДДУ — 4,2 млн; первый платёж ушёл на реквизиты застройщика, не на эскроу
- Менеджер: «потом зачтём в эскроу» — переписка не пополняет спецсчёт
- За 7 дней до подписания банк увидел нулевой остаток на эскроу
- Сделку остановили; застройщик предложил внести 4,2 млн повторно — риск двойной оплаты
- Бронь, аванс и цена ДДУ — три разных платежа
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 4583; «купить новостройку в тюмени в ипотеку» demand
- buyer risk: ДДУ, эскроу, бронь, первоначальный взнос, маршрут денег, ипотека

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, банк

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B24",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
