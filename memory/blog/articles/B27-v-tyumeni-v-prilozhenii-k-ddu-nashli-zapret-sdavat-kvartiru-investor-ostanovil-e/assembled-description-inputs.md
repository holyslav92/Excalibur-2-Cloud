# Description inputs — B27 — 2026-09-17

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** with non-null `description` string. verdict: PASS. No BLOCKER refusals.

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч

**subject:** Приложение к ДДУ в новостройке с запретом сдавать квартиру

**angle:** Инвестор рассчитывал сдавать студию, но за два дня до визита в банк нашёл запрет аренды в приложении к ДДУ и отказался от сделки и от альтернативного лота на 240 тысяч дороже.

**comment_magnet_angle:** Менеджер обещал, что квартиру можно сдавать, но в приложении оказался запрет: стоило ли терять бронь или доплачивать 240 тысяч за другой лот?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени инвестор нашёл в приложении к ДДУ запрет на аренду, а вариант без него стоил на 240 тысяч рублей дороже — покупка студии оказалась под вопросом. Бронь уже оформили, ипотеку предварительно одобрили, доход от будущих жильцов заложили в расчёт платежа.

**Para 2 (early CTA):** Я — Святослав Шакин, The Риэлтор в Тюмени. В новостройке смотрю не только на планировку и платёж: важно, что покупателю предлагают подписать.

## Case hook (from research / article)
- Тюмень, новостройка, студия под аренду, ДДУ + приложение №3
- Менеджер: «свободное использование»; на стр. 14 приложения — запрет сдачи до регистрации дома
- 2 дня до визита в банк; эскроу не открывали
- Альтернативный лот +240 тыс. ₽ — отказ; бронь сгорела
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only)
- «купить новостройку в тюмени» 928
- «договор долевого участия эскроу» 439 (RU)
- аренда / приложение к ДДУ / инвестор

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs
3. Klyshin rhythm: case hook, intrigue
4. Geo: Тюмень OK
5. No checklist spoiler

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
