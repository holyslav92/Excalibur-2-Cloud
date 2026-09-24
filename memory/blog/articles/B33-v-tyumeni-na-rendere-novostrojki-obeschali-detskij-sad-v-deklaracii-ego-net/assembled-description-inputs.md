# Description inputs — B33 — 2026-09-24

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B33

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени на рендере новостройки обещали детсад — в декларации его нет

**subject:** Детский сад на рендере новостройки и проектная декларация

**angle:** Семья увидела детский сад на рендере и в материалах брони, но за пять дней до ДДУ обнаружила, что в проектной декларации его нет, и отказалась подписывать договор.

**comment_magnet_angle:** Если детский сад показали на рендере и пообещали в офисе, но в проектной декларации его нет, вы бы всё равно подписали ДДУ ради квартиры?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За пять дней до ДДУ семья с двумя детьми внесла бронь 150 000 ₽ за квартиру, а потом выяснила: обещанного детского сада в проектной декларации нет — и до эскроу родители остановили сделку. На рендере всё выглядело убедительно: зелёный двор, дорожка и отдельное светлое здание с табличкой «детский сад». В офисе менеджер подтвердил, что сад будет рядом с домом. Для детей трёх и шести лет это означало короткий путь из подъезда вместо ежедневных поездок через весь город.

**Para 2 (early CTA):** Если вы выбираете квартиру в Тюмени и хотите заранее проверить документы и обещания застройщика, напишите Святославу Шакину, The Риэлтор.

## Case hook (from research / article)
- Тюмень, новостройка, семья с детьми 3 и 6 лет
- Рендер: отдельное здание «детский сад»; менеджер: сад рядом с домом
- Бронь 150 000 ₽; в договоре брони: «инфраструктура: детсад во дворе»
- За 5 дней до ДДУ вечером открыли проектную декларацию на dom.rf / ЕИСЖС
- В разделе социнфраструктуры — детская площадка, отдельного детсада нет
- Ответ офиса: «город построит позже», рендер — концепция
- Раздел 22: площадка ≠ муниципальный детский сад с местами
- Семья отказалась от ДДУ до эскроу; из брони вернули 90 000 ₽ (удержание 60 000 по условиям брони)
- Смысл: картинка и строка в брони не заменяют декларацию 214-ФЗ
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 4294, «купить новостройку в тюмени» 897 (регион 55+11176)
- проектная декларация, ЕИСЖС, dom.rf, ДДУ, бронь, детский сад, раздел 22
- buyer risk: рендер vs декларация, инфраструктура во дворе, эскроу

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЕИСЖС

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

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
