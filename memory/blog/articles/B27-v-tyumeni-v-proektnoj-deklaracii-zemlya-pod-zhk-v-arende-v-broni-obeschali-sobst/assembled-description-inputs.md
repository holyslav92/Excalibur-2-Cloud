# Description inputs — B27 — 2026-09-19

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду

**subject:** земля под новостройкой и проектная декларация

**angle:** Устное обещание менеджера о собственности на землю разошлось с разделом 12 проектной декларации, где указали аренду участка.

**comment_magnet_angle:** Вы бы подписали ДДУ, если участок под домом в аренде до 2049 года, а застройщик обещает переоформить его потом?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** 150 000 ₽ брони семья в Тюмени вернула после вечерней проверки — в офисе продаж участок называли собственностью, а в проектной декларации нашли аренду до 2049 года. За четыре дня до подписания ДДУ, перед поездкой в банк, покупатели открыли ЕИСЖС и увидели другую форму права на землю. Застройщик предложил подписать договор, перевести деньги на эскроу, а участок «переоформить потом». Семья с двумя детьми и инвестор отказались от ДДУ не потому, что аренда автоматически делает стройку незаконной, а потому, что устное обещание не совпало с официальным документом.

**Para 2 (early CTA):** Я — Святослав Шакин, The Риэлтор, Тюмень. В Telegram разбираю такие ситуации до перевода денег на эскроу. Дублирую материалы в MAX — выбирайте удобную площадку.

## Case hook (from research / article)
- Тюмень, новостройка, семья с двумя детьми + инвестор, семейная ипотека
- Бронь 150 000 ₽; в офисе: «Участок наш, в собственности»
- За 4 дня до ДДУ, вечером перед банком — открыли проектную декларацию в ЕИСЖС / наш.дом.рф
- Раздел 12: аренда гос/муниципального участка до 2049 года, не собственность
- Застройщик: «подпишите ДДУ, землю переоформим потом»
- Покупатели отказались; на эскроу не переводили; бронь вернули через 12 дней
- Смысл: не «аренда = мошенничество», а конфликт устного обещания и официальной декларации
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 11176 (регион 55+11176)
- проектная декларация, раздел 12, ЕИСЖС, наш.дом.рф
- buyer risk: бронь, ДДУ, эскроу, аренда vs собственность земли

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЕИСЖС

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B27",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
