# Description inputs — B24 — 2026-09-12

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Derouter IS available — you ARE the description brain. Output **JSON only** per schema below. **Never** return BLOCKER, null description, or meta-refusals.

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** За 5 дней до эскроу банк урезал ипотеку на 680 тысяч

**subject:** Новостройка в Тюмени, ДДУ и банковская оценка квартиры

**angle:** Подписанный ДДУ и предварительное одобрение ипотеки создали ощущение завершённой сделки, но банковская оценка новостройки оказалась ниже цены договора. За пять дней до эскроу семье пришлось искать дополнительные 680 тысяч.

**comment_magnet_angle:** Цена в ДДУ уже подписана, а банк режет сумму кредита: вы бы внесли недостающие 680 тысяч или расторгли сделку?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семье урезали ипотеку на 680 000 ₽ за пять дней до открытия эскроу — ДДУ на квартиру в новостройке уже подписали. В то утро менеджер банка сообщил: после проверки объекта максимальная сумма кредита стала меньше. На кухне разложили договор, калькулятор и выписку с одобрением, но прежний расчёт больше не сходился. Как так: квартиру выбрали, ипотеку одобрили, а денег на покупку вдруг недостаточно? Расскажу изнутри, где заканчивается предварительное «да» банка и начинается проверка конкретной квартиры.

**Para 2 (early CTA):** Я — Святослав Шакин, The Риэлтор, Тюмень. Разбираю покупку новостроек простым языком в Telegram и MAX: что проверить до подписи и какие вопросы задать до перевода денег.

## Case hook (from research / article)
- Тюмень, новостройка на севере города, семья с предварительным одобрением ипотеки
- «Ипотеку одобрили» ≠ окончательный лимит по конкретному лоту
- ДДУ подписан, цена в договоре зафиксирована — банк заказал оценку строящейся квартиры
- Оценочная стоимость на 680 000 ₽ ниже цены в ДДУ
- Банк пересчитал кредитный лимит; за 5 дней до эскроу не хватило собственных денег
- Семья не смогла собрать доплату; бронь сгорела, квартира вернулась в продажу, плату за бронь не вернули полностью
- Автор: Святослав Шакин, The Риэлтор, Тюмень
- Distinct from B22 (ставка перед ДДУ), B19 (эскроу/маткапитал), B06 (автооценка вторички)

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 3593 (55); «купить новостройку в тюмени» 688; «ипотека новостройка» 398
- buyer risk: предварительное одобрение, оценка ниже ДДУ, эскроу, первоначальный взнос, бронь

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
