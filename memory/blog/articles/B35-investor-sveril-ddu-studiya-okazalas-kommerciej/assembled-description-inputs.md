# Description inputs — B35 — 2026-09-27

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B35

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Инвестор в Тюмени за 2 дня до эскроу остановил сделку: студия стала коммерцией в ДДУ

**subject:** студия в тюменской новостройке и её назначение в ДДУ

**angle:** Инвестор забронировал студию под сдачу, но перед переводом денег обнаружил в ДДУ коммерческое назначение и остановил сделку.

**comment_magnet_angle:** Если в ДДУ вместо квартиры всплывает коммерция, вы торгуетесь за замену лота или уходите?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За 2 дня до открытия эскроу инвестор в Тюмени остановил покупку студии. В рекламе, на плане и в разговоре с менеджером это выглядело как компактная квартира под сдачу. Но в проекте ДДУ обнаружилась другая формулировка — нежилое помещение. Бронь уже была оформлена, ипотечный расчёт сделан, до подписи оставался один шаг. Деньги на эскроу покупатель не перевёл: сначала решил понять, что именно ему предлагают.

**Para 2 (early CTA):** Нужно спокойно проверить новостройку в Тюмени до подписи? Напишите в Telegram или в MAX.

## Case hook (from research / article)
- Тюмень, инвестор под сдачу, компактная «студия» на витрине
- Бронь оформлена, ипотечный расчёт как для жилья, эскроу через 2 дня
- В проекте ДДУ — «нежилое помещение», не квартира
- Сверка с дом.рф / декларацией — то же назначение
- ДДУ не подписан, деньги на эскроу не ушли; сделку остановили
- «Студия» в рекламе ≠ жилое назначение в договоре
- Автор контекст: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- новостройки Тюмени, студия под сдачу, проверка ДДУ до эскроу
- buyer risk: назначение объекта, нежилое помещение, ипотека, бронь

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1 («За 2 дня до открытия эскроу…»)
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, дом.рф

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B35",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
