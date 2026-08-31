# Description inputs — B16 — 2026-08-31

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B16

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени семья остановила бронь — третий транш раскрыл платёж

**subject:** Траншевая ипотека на новостройке в Тюмени

**angle:** Семья почти забронировала новостройку из-за рекламного платежа «как аренда», но остановилась, увидев полный график и рост платежа после третьего транша.

**comment_magnet_angle:** Сколько месяцев вы готовы платить «как аренду», не видя полного графика траншей?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В офисе продаж это звучало почти как шутка: «Платите как за аренду — только за своё». Семья с ребёнком дошла до брони квартиры в тюменской новостройке, держа в голове одну цифру — около 10 800 ₽ в месяц. Полную лестницу платежей по траншам никто не прятал, но и вслух её не проговорили: график семья запросила сама, за несколько дней до внесения денег. В нём оказался третий транш, после которого «как аренда» заканчивалась. Бронь отменили, ДДУ не подписали. Случай моделируемый — собран из типовых тюменских разговоров этого сезона, без фамилий, названий ЖК, банка и суммы договора: разбираем механику, а не конкретного менеджера.

**Para 2 (early CTA):** Святослав Шакин, The Риэлтор, Тюмень. Разбираю такие схемы до брони, а не после.

## Case hook (from research / article)
- Тюмень, новостройка, траншевая ипотека
- Рекламный платёж «как аренда» ~10 800 ₽ — первые полгода
- Полный график не проговаривали вслух; семья запросила за несколько дней до денег
- Лестница: 10 800 → 21 500 → 86 000 ₽ (рекламное раскрытие 72.ru, готовый дом)
- Третий транш — «как аренда» заканчивается, рост в ~8 раз от старта
- Бронь отменили, ДДУ не подписали — деньги не внесли
- Семья с ребёнком; альтернатива — семейная или рыночная с ровным графиком
- Траншевая и семейная не совмещаются (21,2% vs 6%)
- Автор: Святослав Шакин, The Риэлтор, Тюмень
- Моделируемый кейс, без названий ЖК/банка

## Wordstat demand spine (hint only, no SEO tail in description)
- «траншевая ипотека» 55+11176 Tyumen; «траншевая ипотека новостройка» demand
- buyer risk: транши, график платежей, бронь, ДДУ, первый платёж vs финальный

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler («5 шагов», «полный чеклист»)
6. Cyrillic; brands OK: ДДУ, ЕГРН
7. News energy — hint at consequence/final, not «how to buy»
8. Do NOT start with «В офисе продаж» or «Платите как за аренду»

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B16",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
