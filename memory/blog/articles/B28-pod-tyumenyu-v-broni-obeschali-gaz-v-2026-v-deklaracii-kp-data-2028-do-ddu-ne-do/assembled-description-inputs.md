# Description inputs — B28 — 2026-09-19

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B28

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч

**subject:** Газ в коттеджном посёлке и проектная декларация

**angle:** Обещанный срок подключения газа расходится с проектной декларацией: семья отказалась подписывать ДДУ и потеряла часть брони.

**comment_magnet_angle:** Если в брони обещают газ, а декларация указывает более поздний срок, вы бы подписали ДДУ ради сохранения брони или ушли?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Семья с двумя детьми внесла 200 000 ₽ за бронирование готового дома в строящемся коттеджном посёлке под Тюменью, но до покупки не дошла и потеряла 60 000 ₽. Газ, на который рассчитывали при переезде, в документах оказался совсем не на том горизонте, что в обещаниях офиса продаж. Дом готов — казалось бы, остаётся оформить сделку и планировать жизнь за городом. Только готовый дом и готовое отопление от газа — не одно и то же. Расскажу изнутри этой развилки: что проверить, пока за вами ещё выбор, а не подписанный ДДУ.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Выбираете дом или новостройку — напишите в Telegram или MAX. Подключусь до аванса: сначала разберём документы, потом будем решать, за что платить.

## Case hook (from research / article)
- Под Тюменью, коттеджный посёлок, готовый дом по ДДУ, семья с двумя детьми
- Бронь 200 000 ₽; в бронировании и офисе: «газ к 2026»
- За 6 дней до ДДУ вечером открыли проектную декларацию в ЕИСЖС (dom.rf)
- В разделе о сетях: ввод газопровода IV квартал 2028, не 2026
- Застройщик: «подпишите ДДУ, по внутреннему графику сделаем раньше»
- Семья отказалась от ДДУ; эскроу не открывали; из брони вернули 140 000 ₽, удержали 60 000 ₽ за резервирование лота
- Смысл: готовый дом ≠ готовый газ; слова менеджера vs декларация 214-ФЗ; проверка до подписи
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 4430, «коттеджные поселки тюмень» 1455 (регион)
- проектная декларация, ЕИСЖС, газоснабжение, ТУ, ДДУ, бронь, КП
- buyer risk: обещание газа, срок сетей, удержание брони

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЕИСЖС, КП

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B28",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
