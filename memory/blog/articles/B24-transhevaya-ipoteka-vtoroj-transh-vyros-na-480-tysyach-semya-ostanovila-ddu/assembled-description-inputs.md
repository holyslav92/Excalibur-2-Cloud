# Description inputs — B24 — 2026-09-12

## PRODUCTION (mandatory)
You are Derouter powerful tier (gpt-6-astra) in live Excalibur BLOG pipeline. Derouter REST is connected and running. The conductor will run `excalibur_blog_description_gate.py` after your output. Return ONLY valid JSON with a non-empty `description` string. Do NOT return BLOCKED, null description, or meta-refusal.

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени второй транш ипотеки вырос на 480 тысяч — ДДУ остановили

**subject:** траншевая ипотека на новостройку и второй транш

**angle:** Цифра и срок показывают момент риска: семья обнаружила рост нагрузки за день до ДДУ и остановила сделку до открытия эскроу.

**comment_magnet_angle:** Кто должен был заметить рост платежа — банк, застройщик или сама семья до брони квартиры?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За день до подписания ДДУ семья в Тюмени увидела в полном графике банка прибавку примерно 40 тысяч рублей в месяц — около 480 тысяч рублей в год к ипотечной нагрузке. До этого квартира казалась посильной: бронь оформлена, ипотека одобрена, а «платёж на период стройки» укладывался в домашний бюджет. Но после второго транша, то есть выдачи оставшейся части кредита, действовал бы уже другой график. Доходы и текущие обязательства с ним не сходились, поэтому семья остановила сделку до подписания ДДУ и перевода денег на эскроу.

**Para 2 (early CTA):** Я разбираю такие покупки через документы и семейный бюджет, а не только через красивую цифру в объявлении. Если на руках расчёт траншевой ипотеки и проект ДДУ — пришлите, посмотрим до подписания. Святослав Шакин, The Риэлтор, Тюмень.

## Case hook (from research / article)
- Тюмень, новостройка, траншевая ипотека, семья с одобрением на полную сумму
- «Платёж на период стройки» ≠ постоянная нагрузка — временный низкий платёж по первому траншу
- За день до ДДУ: полный график показал +40 тыс./мес (~480 тыс./год) к нагрузке — не рост ставки, а второй транш
- Ставка не менялась; проценты на большую выданную сумму
- Семья остановила сделку: ДДУ не подписали, эскроу не открыли
- Бронь — отдельный вопрос по договору; одобрение ≠ завершённая сделка
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» P0 4560; «траншевая ипотека» 4
- buyer risk: транш, второй транш, график платежей, ДДУ, эскроу, бронь, семейный бюджет

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
