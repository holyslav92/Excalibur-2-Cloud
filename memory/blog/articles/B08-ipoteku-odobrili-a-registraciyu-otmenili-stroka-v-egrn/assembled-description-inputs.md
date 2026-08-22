# Description inputs — B08 — 2026-08-22

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## Runtime note (Derouter)
Return **only** valid JSON matching the schema below — no markdown fences, no commentary, no extra keys.

## topic_id
B08

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию

**subject:** обременение в ЕГРН при покупке квартиры с одобренной ипотекой

**angle:** Одобрение банка создаёт ощущение безопасности, но действующее обременение может остановить регистрацию сделки.

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Ипотеку одобрили. Квартиру нашли. Аванс отдали, договор подписали, документы сдали в МФЦ. Дальше по плану была регистрация — а пришло уведомление о приостановке. В ЕГРН по объекту числится действующая запись об обременении.

**Para 2:** Запись не появилась ночью. Она стояла в выписке ещё до аванса. Её просто не прочитали. Все смотрели в другую сторону: на одобрение банка, на ставку, на дату выхода на сделку.

**Para 3 (context only):** Это не курьёз. Это типовая сцена. Разбираю её так, как она выглядит в тюменской практике: покупатель с одобренной ипотекой, продавец с «чистой квартирой» на словах и одна строка в выписке, которую никто не проверил до денег.

## Case hook (from research / article)
- Банк одобрил заёмщика — не объект; «да» банка ≠ чистая регистрация
- Действующая запись об обременении в ЕГРН стояла до аванса, пролистали раздел ограничений
- Продавец: «старое, уже закрыто» — в реестре запись жива
- Регистратор приостановил; при неустранении — отказ, госпошлина не возвращается
- Формула: сначала проверка, потом аванс
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить квартиру в тюмени» 22880; «егрн» 7543; «выписка из егрн» 2648
- Buyer risk: одобрение ипотеки, обременение, приостановка регистрации, аванс

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler, no how-to blurb
6. Cyrillic; brands OK: ЕГРН, МФЦ, Росреестр
7. News energy — hint at consequence, not «как купить»

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B08",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
