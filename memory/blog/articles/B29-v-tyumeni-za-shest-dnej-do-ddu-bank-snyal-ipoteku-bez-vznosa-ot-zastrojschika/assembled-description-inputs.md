# Description inputs — B29 — 2026-09-19

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B29

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала

**subject:** ипотека без первоначального взноса на новостройку

**angle:** Программа с нулевым взносом закончилась перед ДДУ, и семья не успела собрать первоначальный платёж — сделка остановилась до эскроу.

**comment_magnet_angle:** Если банк отменяет нулевой взнос за неделю до ДДУ, вы бы торопились подписать договор или ждали возвращения программы от застройщика?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За 6 дней до ДДУ банк отменил программу с нулевым взносом — семья остановила сделку, платёж вырос примерно на 18 тысяч в месяц. Бронь уже оплатили, квартиру выбрали, будущие расходы разложили по домашнему бюджету. Собственных денег на большой первоначальный взнос не было — именно поэтому предложение застройщика и подошло. Несколько недель подготовки выглядели дорогой к покупке, но не закрепили условия, на которых семья собиралась покупать. Покажу, где заканчивается обещание в офисе продаж и начинается проверка документов, которую стоит провести до передачи денег.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Разбираю покупки не по рекламному платежу, а по условиям, с которыми вы дойдёте до сделки. Смотреть разборы и задать вопрос можно в Telegram и MAX.

## Case hook (from research / article)
- Тюмень, новостройка, семья без накопленного первоначального взноса
- В офисе продаж: «ипотека без взноса от застройщика» / минимальный взнос за счёт акции
- Предварительное одобрение + оплаченная бронь — весь бюджет держался на акции
- За 6 дней до ДДУ: банк закрыл программу, пересчитал условия; нужен ПВ, которого нет
- Платёж +~18 000 ₽/мес; ДДУ не подписан, эскроу не открыт; часть брони удержали (ориентир 50–80 тыс.)
- Отличие от B22: не ставка при сохранённом взносе, а исчезновение нулевого/застройщического входа
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «ипотека от застройщика тюмень» 514; «ипотека без первоначального взноса тюмень от застройщика» 197
- buyer risk: нулевой взнос, акция, бронь vs эскроу, предварительное одобрение, ДДУ

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
  "topic_id": "B29",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
