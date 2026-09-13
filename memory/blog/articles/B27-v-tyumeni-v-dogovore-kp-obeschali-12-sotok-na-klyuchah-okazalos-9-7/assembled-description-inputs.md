# Description inputs — B27 — 2026-09-13

## Runtime (Derouter gpt-6-astra)
You are the Derouter powerful description writer invoked by excalibur_blog_derouter_opus_chat.py. Write the teaser JSON now. Return only the JSON object — never BLOCKED, never meta-refusal.

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В КП Тюмени купили 12 соток — намерили 9,7 и остались без ключей

**subject:** Площадь участка при покупке дома у застройщика в коттеджном посёлке Тюмени: договорные 12 соток против фактических 9,7.

**angle:** Договорная площадь столкнулась с результатом межевания, а отказ принять меньший участок оставил семью без ключей.

**comment_magnet_angle:** Подписали бы акт с оговоркой ради переезда, получив 9,7 сотки вместо договорных 12, или отказались бы от приёмки до разрешения спора, продолжая платить за аренду?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья купила дом с участком 12 соток, а за три дня до передачи получила межевой план на 9,7 — и осталась без ключей. Дом был готов, уведомление о передаче пришло, но вместо обычной приёмки на стол легли два документа с разными цифрами: в договоре — 12 соток, в межевом плане — меньше 10. Застройщик предложил принять уменьшенный участок без пересчёта цены или доплатить за соседний фрагмент. Семье пришлось выяснять, какую землю она покупала и какую теперь ей предлагают принять.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Разбираю документы и спорные моменты покупки новостроек простым языком — в Telegram и MAX. Чтобы такие вопросы появлялись до передачи денег, а не за несколько дней до ключей.

## Case hook (from research / article)
- Тюмень, коттеджный посёлок, семья, дом по ДДУ со эскроу
- В договоре и на схеме — 12 соток; за 3 дня до акта — межевой план с «уточнённой площадью» 9,7 сотки
- Разница 2,3 сотки = 19,2%, почти пятая часть участка
- Застройщик: доплатить за соседний фрагмент ИЛИ принять 9,7 без пересчёта цены
- Семья отказалась подписывать передаточный акт, направила претензию, заказала независимое межевание
- Ключи не выдали; деньги на эскроу; аренда и платежи не останавливаются
- «Уточнённая» звучит безобидно, но межевой план не переписывает ДДУ
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «коттеджные поселки тюмень» 1566 (регион 55+11176)
- «участок в коттеджном поселке» 52
- buyer risk: ДДУ, межевой план, площадь участка, передаточный акт, эскроу, КП

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, КП, эскроу

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Доделаем потом», — услышала семья на приёмке в Тюмени. Но в приложении к ДДУ были пол, двери и сантехника, а перед ними — white box.»

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
