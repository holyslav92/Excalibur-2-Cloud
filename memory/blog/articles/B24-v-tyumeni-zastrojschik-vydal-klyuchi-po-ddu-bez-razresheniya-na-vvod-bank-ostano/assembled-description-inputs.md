# Description inputs — B24 — 2026-09-08

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку

**subject:** новостройка в Тюмени, ДДУ и остаток ипотечного кредита

**angle:** Семья получила ключи и начала ремонт, но банк остановил перевод остатка ипотеки: разрешения на ввод дома ещё не было в реестре.

**comment_magnet_angle:** Ключи на руках, а ипотека не дошла: подписали бы акт без разрешения на ввод или ждали?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Через 2 дня после ключей банк остановил основной транш ипотеки: в реестре ещё не было разрешения на ввод дома. В субботу семья получила квартиру в тюменской новостройке. Первый небольшой платёж по ДДУ уже прошёл, поэтому покупатели считали вопрос с кредитом решённым. Менеджер показал акт, сослался на заселившихся соседей и поторопил с подписью. Семья подписала документ, начала ремонт — а разницу временно пришлось закрывать за свой счёт.

**Para 2 (early CTA):** Я разбираю такие ситуации в Telegram и MAX: какие документы проверить до подписи, что запросить у застройщика и когда подключать банк.

## Case hook (from research / article)
- Тюмень, новостройка, ДДУ, траншевая ипотека, эскроу
- Ключи в субботу, акт подписан, ремонт начат — в реестре нет РНВ
- Первый транш прошёл → ложное ощущение «кредит решён»
- Через 2 дня банк остановил основной транш: нет разрешения на ввод
- Акт приёма-передачи ≠ разрешение на ввод; заселившиеся соседи не заменяют реестр
- Семья закрывает разницу своими деньгами, пока эскроу не раскрыт
- Застройщик: «квартира передана» — банк: «нет документа для остатка»
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 312; «дду новостройка» 89; «эскроу счет» 312
- buyer risk: ключи, акт, РНВ, траншевая ипотека, остаток на эскроу

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, РНВ, банк

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
