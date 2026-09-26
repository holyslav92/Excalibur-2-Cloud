# Description inputs — B33 — 2026-09-26

You ARE inside `excalibur_blog_derouter_opus_chat.py --role description`. Output **only** valid JSON for `description-brief.json`. Never return verdict BLOCKED — write the teaser.

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B33

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** За 3 дня до ключей в тюменской новостройке лифт не прошёл осмотр — заселение перенесли

**subject:** лифт в тюменской новостройке, не прошедший техническое освидетельствование

**angle:** За три дня до выдачи ключей выяснилось, что лифт не допущен к эксплуатации. Из-за этого заселение перенесли, а семьи остались одновременно с ипотекой и арендой.

**comment_magnet_angle:** Согласны ли вы заходить в новостройку, если лифт формально не сдан?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За 3 дня до получения ключей семья из Тюмени узнала: лифтом в их новостройке пользоваться нельзя — ключи могли не выдать в назначенный срок. Ещё через 3 дня должна была состояться передача квартиры — вместо переезда семья получила новую дату и двойную кассу. Кабина не прошла полное техническое освидетельствование и не была введена в эксплуатацию. Квартира находилась на высоком этаже, поэтому вариант «поднимем всё по лестнице» отпал — мебель, техника и детские вещи так не переезжают. Ипотека уже списывалась, аренду прежнего жилья отменять было рано.

**Para 2 (early CTA):** Готовитесь к приёмке новостройки в Тюмени? В моих Telegram и MAX разбираю документы, переносы ключей и проблемы, которые лучше заметить до подписи акта.

## Case hook (from research / article)
- Тюмень, новостройка, семейная ипотека, квартира на высоком этаже
- За ~3 дня до ключей: лифт без акта полного технического освидетельствования / не введён в эксплуатацию
- Ключи перенесли; ипотека уже идёт, аренда не отменилась — двойная касса
- Передаточный акт не подписали до документов на лифт и проверки работы
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 11176 (регион 55+11176)
- лифт, техосвидетельствование, ключи, перенос сдачи, приёмка

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, 214-ФЗ

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»

## Required JSON output
```json
{
  "topic_id": "B33",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
