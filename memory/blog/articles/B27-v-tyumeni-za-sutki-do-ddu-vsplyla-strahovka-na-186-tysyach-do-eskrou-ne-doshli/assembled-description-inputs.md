# Description inputs — B27 — 2026-09-16

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли

**subject:** Страховой пакет на 186 тысяч рублей в допсоглашении к сделке с новостройкой перед подписанием ДДУ

**angle:** Накануне подписания ДДУ семья узнала о новом обязательном платеже, отказалась подписывать допсоглашение и не дошла до открытия эскроу; slug подтверждён.

**comment_magnet_angle:** Вы бы доплатили 186 тысяч ради сохранения брони или остановили сделку, даже если квартира уйдёт?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За сутки до подписания ДДУ в Тюмени у семьи всплыла страховка на 186 тысяч рублей — эскроу не открыли, а бронь квартиры через 48 часов сгорела. Ипотеку банк уже одобрил, объект выбрали, первоначальный взнос и ежемесячный платёж посчитали. Но вечером менеджер прислал допсоглашение, которого не было в исходном расчёте. До визита в банк оставался один день: искать ещё 186 тысяч или остановить сделку.

**Para 2 (early CTA):** Я, Святослав Шакин, разбираю такие истории в The Риэлтор — о новостройках и сделках в Тюмени без лишней паники.

## Case hook (from research / article)
- Тюмень, новостройка, семья с одобренной ипотекой и внесённой бронью
- «Ипотеку одобрили — значит, все расходы известны» — ложный щелчок
- За 24 часа до ДДУ: допсоглашение с пакетом страхования жизни и имущества на 186 000 ₽
- Суммы не было в первоначальном ипотечном расчёте; оформить предлагали у партнёра застройщика
- Обязательность не подтверждена письмом банка — файл от офиса продаж ≠ требование кредитора
- Семья не подписала допсоглашение, эскроу не открыли, бронь сгорела через 48 часов
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить новостройку в тюмени в ипотеку» 93; «ипотека на новостройку тюмень» 40
- buyer risk: допсоглашение, страховой пакет, бронь, эскроу, ДДУ, входной платёж

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
