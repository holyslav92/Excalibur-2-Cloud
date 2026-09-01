# Description inputs — B20 — 2026-09-01

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B20

## cluster
newbuild booking price increase

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч

**subject:** бронь новостройки в Тюмени

**angle:** Завершённый конфликт с понятными ставками: покупатель забронировал квартиру, но за 48 часов столкнулся с повышением цены на 380 тысяч.

**comment_magnet_angle:** Бронь с фиксацией цены — договор или обещание на 48 часов?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В четверг вечером в офисе продаж пара выбрала двушку на девятом этаже, подписала бронь на двое суток — бесплатно, «до понедельника, чтобы вы спокойно собрали документы». В субботу менеджер перезвонил сам: квартира на месте, никто её не забрал, всё в силе, только с ночи обновился прайс — та же квартира, тот же этаж, тот же стояк, плюс 380 тысяч.

**Para 2 (CTA block follows):** Меня зовут Святослав Шакин, The Риэлтор, Тюмень…

## Case hook (from research / article)
- Тюмень, новостройка, бесплатная бронь на двое суток
- Менеджер: «бронь держит квартиру, а не цену»
- В бумаге не было слова «цена» — только срок резерва квартиры
- Прайс обновился за 48 часов: +380 000 ₽ на ту же двушку
- Пара добрала деньги из бюджета на кухню, взяли квартиру по новой цене
- Суда не было — формально застройщик прав по тексту брони
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить новостройку в Тюмени» 874; «ипотека от застройщика Тюмень» 518
- buyer risk: бронь ≠ фиксация цены, прайс-лист, ДДУ

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B20",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
