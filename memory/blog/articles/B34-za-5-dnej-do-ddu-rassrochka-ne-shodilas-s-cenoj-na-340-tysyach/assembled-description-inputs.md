# Description inputs — B34 — 2026-09-27

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B34

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** За 5 дней до ДДУ в Тюмени рассрочка разошлась с ценой на 340 тысяч — семья остановила регистрацию

**subject:** Рассрочка от застройщика и её график в договоре на новостройку

**angle:** Финальная сверка перед регистрацией показала разрыв примерно в 340 000 ₽ между ценой ДДУ и графиком рассрочки, поэтому сделку пришлось остановить до исправления документов.

**comment_magnet_angle:** Если график рассрочки не сходится с суммой в ДДУ на сотни тысяч рублей, подписывать документы или ждать новый пакет?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За пять дней до подписания ДДУ семья в тюменской новостройке нашла разницу в 340 000 ₽ — и остановила сделку до подачи документов на регистрацию. В офисе продаж обсуждали удобный ежемесячный платёж, но не всю сумму, которая должна была сойтись в договоре и графике рассрочки. Бронь и аванс уже были оплачены, дата подписания приближалась, ипотечные расчёты могли начаться в любой момент. Когда ДДУ, приложение и платежи разложили рядом, стало ясно: в таком виде пакет отправлять нельзя.

**Para 2 (early CTA):** Новости и разборы новостроек в Тюмени — в Telegram и MAX.

## Case hook (from research / article)
- Тюмень, новостройка, семья, рассрочка от застройщика по ДДУ
- «Платёж в месяц устроит» — продавали рассрочку, но не всю арифметику цены
- Цена в ДДУ vs сумма первоначального взноса + график платежей — не сходится на ~340 000 ₽
- Бронь и аванс уже оплачены; ипотека может начать расчёт в любой момент
- За 5 дней до подписания/регистрации сверка — регистрацию остановили, пакет не ушёл в Росреестр
- Причина расхождения неочевидна: скидка, бонус, Excel, версия приложения, финальный платёж
- Автор контекст: Святослав Шакин, The Рiэлтор, Тюмень (не label head)

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить новостройку в тюмени» 676; «график платежей дду» 19; рассрочка от застройщика — узкий спрос
- buyer risk: цена ДДУ, график рассрочки, бронь, аванс, регистрация, ипотека

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, Росреестр

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B34",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
