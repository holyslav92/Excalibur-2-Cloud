# Description inputs — B27 — 2026-09-17

## Task
You are Derouter powerful (gpt-6-astra) executing the Description role. Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return **only** valid JSON per schema below — no markdown, no commentary, no BLOCKER, no refusal. Field `verdict` must be `"PASS"`.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась

**subject:** Другой корпус новостройки вместо забронированного — предложение застройщика перед подписанием ДДУ.

**angle:** Платная бронь не сохранила выбранный лот: перед ДДУ семье предложили другой корпус с худшими параметрами, и она отказалась подписывать договор.

**comment_magnet_angle:** Семья заплатила за бронь конкретной квартиры — достаточно ли застройщику предложить другой корпус или возврат денег через 45 дней, чтобы считать обязательства выполненными?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За 10 дней до подписания ДДУ семье в Тюмени предложили другой корпус — и покупка, к которой готовились полгода, остановилась. За бронь уже заплатили 200 тысяч рублей, семейную ипотеку одобрили, оставалось сверить документы и выйти на сделку. Вместо этого менеджер сообщил: выбранный корпус «заморожен», можно перейти в соседний. На кухне открыли присланный проект договора рядом с бронью — теперь предстояло решать, нужна ли им вообще предложенная квартира. Срок банковского одобрения поджимал, но заканчивать поиски только потому, что пора подписывать, семья не стала.

**Para 2 (early CTA):** В Telegram и MAX разбираю сделки с новостройками изнутри: где ещё можно остановиться, что проверить до подписи и почему готовые документы не всегда означают готовую покупку.

## Case hook (from research / article)
- Тюмень, новостройка, семья, полгода выбора, платная бронь 200 тыс. ₽
- Корпус А, 14-й этаж, вид на парк — забронировали и одобрили семейную ипотеку
- За 10 дней до ДДУ: «корпус заморожен», предлагают корпус Б — 6-й этаж, вид на кран, −1,2 м²
- Бронь ≠ ДДУ: до регистрации это другой объект, не допсоглашение
- Банк готовил эскроу, одобрение тикало — семья отказалась подписывать чужой лот
- Застройщик: возврат брони через 45 дней; до эскроу не дошли
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить новостройку в тюмени» 93; «новостройки тюмень» demand
- buyer risk: бронь, ДДУ, замена корпуса, этаж, вид, семейная ипотека, эскроу

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
