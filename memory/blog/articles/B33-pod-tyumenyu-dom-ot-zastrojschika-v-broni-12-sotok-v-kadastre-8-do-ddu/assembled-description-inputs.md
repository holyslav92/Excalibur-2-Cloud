# Description inputs — B33 — 2026-09-25

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B33

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Дом под Тюменью обещали на 12 сотках, но в кадастре 8 — ДДУ остановили

**subject:** Дом от застройщика с земельным участком

**angle:** Документы перед подписанием ДДУ показали, что вместо обещанных 12 соток в кадастре значится 8, поэтому сделку остановили до сверки объекта и цены.

**comment_magnet_angle:** Если в брони 12 соток, а в выписке 8, требовать пересчёт цены или всё равно подписывать ДДУ?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В брони у семьи было 12 соток, а в кадастре — 8: из-за разницы в 400 м² родители двоих детей остановили подписание ДДУ на дом под Тюменью. За четыре дня до сделки они открыли документы на кухне и увидели, что обещанный участок площадью 1200 м² в выписке ЕГРН на конкретный кадастровый номер превратился в 800 м². Бронь уже составила 250 000 ₽, ипотека была в работе, а дом семью устраивал. Но подписывать договор с двумя разными площадями покупатели не стали.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. В Telegram разбираю документы по новостройкам и коттеджным посёлкам. Дополнительная площадка — MAX.

## Case hook (from research / article)
- Под Тюменью, коттеджный посёлок, готовый дом + земля по ДДУ, семья с двумя детьми
- В брони и на плане лота: 12 соток (1200 м²); бронь 250 000 ₽
- За 4 дня до ДДУ открыли выписку ЕГРН: 800 м² (8 соток) — минус 400 м²
- Застройщик: «техническая погрешность межевания», подписывайте без пересчёта цены
- Семья поставила ипотеку на паузу; ДДУ не подписали; эскроу не открывали
- Смысл: план лота ≠ кадастровый номер; проверка площади и приложений до подписи
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «коттеджные поселки тюмень» 1393, «выписка егрн» 4358 (регион)
- дом от застройщика, ДДУ, бронь, кадастр, сотки, ЕГРН
- buyer risk: расхождение площади, цена «дом + земля», ипотека

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЕГРН

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B33",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
