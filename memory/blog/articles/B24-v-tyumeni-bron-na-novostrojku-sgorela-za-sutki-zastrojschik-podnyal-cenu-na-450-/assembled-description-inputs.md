# Description inputs — B24 — 2026-09-10

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч

**subject:** платная бронь новостройки в Тюмени

**angle:** Бронь на 48 часов не защитила семью от резкого повышения цены: застройщик пересчитал квартиру накануне ДДУ, а бронь сняли.

**comment_magnet_angle:** Вы бы доплатили 450 тысяч, чтобы не потерять выбранную планировку, или отказались бы от квартиры после такого пересчёта?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Семья в Тюмени внесла 50 000 ₽ за бронь новостройки — и через сутки узнала, что выбранная квартира подорожала ещё на 450 000 ₽. Ипотеку банк предварительно одобрил, первоначальный взнос и платёж считались под прежнюю цену. Но ДДУ ещё не подписали, эскроу не открыли, а срок брони продолжал идти. Когда доплатить разницу не получилось, бронь сняли, лот вернули в продажу, а 50 000 ₽ удержали как оплату услуги бронирования.

**Para 2 (early CTA):** Я — Святослав Шакин, The Риэлтор, Тюмень. В Telegram разбираю такие ситуации без рекламного глянца: подписывайтесь на Telegram. Короткие заметки и связь есть также в MAX.

## Case hook (from research / article)
- Тюмень, новостройка, семья с предварительно одобренной ипотекой
- «Ипотеку одобрили — значит, цена закреплена» — ложный щелчок
- Платная бронь 50 000 ₽, фиксация лота и цены на 48 часов
- За сутки до конца брони застройщик поднял цену на 450 000 ₽
- Бронь ≠ ДДУ ≠ эскроу; одобрение банка не фиксирует прайс застройщика
- Доплаты не хватило — бронь сняли, лот ушёл другим, 50 000 ₽ удержали как услугу
- ДДУ не подписан, эскроу не открыт
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить новостройку в тюмени в ипотеку» 93; «ипотека на новостройку тюмень» 40
- buyer risk: платная бронь, фиксация цены, ДДУ, эскроу, пересчёт прайса

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
