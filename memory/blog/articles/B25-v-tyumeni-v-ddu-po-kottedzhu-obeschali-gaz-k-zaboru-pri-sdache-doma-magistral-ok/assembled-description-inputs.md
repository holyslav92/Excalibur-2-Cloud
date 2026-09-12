# Description inputs — B25 — 2026-09-07

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B25

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м

**subject:** коттедж по ДДУ и обещанный газ

**angle:** Короткий новостной сюжет показывает главный конфликт: в ДДУ газ обещали у границы участка, но при сдаче магистраль оказалась в 180 метрах, что привело к доплате в 620 тысяч рублей.

**comment_magnet_angle:** Газ в 180 метрах от забора — это выполнение ДДУ или отдельная услуга застройщика?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Под Тюменью семья покупала коттедж с газом «к забору», а перед передачей обнаружила трубу примерно в 180 метрах от участка. Подведение сети до границы было указано не только в презентации, но и в ДДУ — договоре участия в долевом строительстве. В день, когда покупатели стали выяснять, где подключать дом, привычная фраза про коммуникации перестала быть понятной. Вместо конкретного места подключения им предложили отдельно оплатить продолжение сети. Расскажу изнутри: здесь сначала нужно разобраться, что уже входит в цену дома, и только потом обсуждать новые платежи.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. В Telegram и MAX разбираю условия покупки новостроек простым языком: что спросить, какие бумаги открыть и что проверить до брони или аванса.

## Case hook (from research / article)
- Тюмень, коттеджный посёлок, дом по ДДУ, семья
- В презентации и ДДУ — «газ к забору» / подведение к границе участка
- За две недели до акта: труба в ~180 м от забора, не у границы
- Застройщик: «дотянуть до границы» — 620 тыс. ₽, можно в рассрочку
- Семья не подписала передаточный акт — нет понятной точки подключения в документах
- «Газ в посёлке» ≠ «газ у забора» ≠ газ в доме
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить дом в тюмени в коттеджном поселке» 18; «коттеджный поселок тюмень» 12
- buyer risk: ДДУ, газ к границе, доплата, передаточный акт, проектная декларация

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, газ

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B25",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
