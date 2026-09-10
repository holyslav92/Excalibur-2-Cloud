# Description inputs — B24 — 2026-09-10

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки

**subject:** Дом в коттеджном посёлке Тюмени по ДДУ и участок при нём

**angle:** Новостройка выглядит определённой в ДДУ, но перед приёмкой семья обнаруживает в выписке ЕГРН на 1,5 сотки меньше и другую границу участка. Заголовок подтверждает slug: дом купили в посёлке, а расхождение нашли в выписке.

**comment_magnet_angle:** Подписывать ли акт приёмки дома, если застройщик обещает позже уточнить межевание, или требовать устранения расхождения до получения ключей?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья подписала ДДУ на дом с 12 сотками, а перед приёмкой в выписке ЕГРН увидела 10,5 — не хватило 1,5 сотки, и выбор стал жёстким: брать ключи или добиваться обещанной земли. В день приёмки на столе оказались два документа с разными параметрами участка. Приложение к договору обещало одну территорию, реестр показывал другую. На спорной линии уже стоял соседский забор, а застройщик предлагал подписать акт и разобраться с межеванием потом. Можно ли принимать дом, если с землёй под ним и вокруг него ещё нет ясности?

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, личный риэлтор в Тюмени. Расскажу изнутри, где в покупке дома заканчивается «всё готово» и начинается проверка документов. Такие разборы публикую в Telegram и MAX.

## Case hook (from research / article)
- Тюмень, коттеджный посёлок, дом по ДДУ, ипотека ИЖС, эскроу
- В приложении к ДДУ — 12 соток и линия границы
- Выписка ЕГРН — 10,5 соток (недостача 1,5 сотки, 12,5%)
- Граница в ЕГРН смещена относительно договорной схемы
- На спорной линии — забор соседа
- Застройщик: «Подпишите акт, домежуем потом»
- Семья не взяла ключи, не подписала акт, отправила претензию
- Забор не устанавливает юридическую границу, но сигнализирует о споре
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- newbuild cottage / ИЖС / ДДУ / участок / ЕГРН / межевание
- buyer risk: граница участка, площадь, акт приёмки, застройщик

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЕГРН, ИЖС

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
