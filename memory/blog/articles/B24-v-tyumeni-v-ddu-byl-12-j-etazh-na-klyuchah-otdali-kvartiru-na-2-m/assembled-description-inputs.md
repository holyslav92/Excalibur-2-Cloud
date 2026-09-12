# Description inputs — B24 — 2026-09-07

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й

**subject:** Новостройка в Тюмени с этажом, указанным в ДДУ

**angle:** Завершённая выдача ключей обернулась спором: покупателю предложили не тот этаж, который прямо указан в ДДУ. Угол соответствует slug.

**comment_magnet_angle:** Вы бы подписали акт ради мебели и ипотеки или отказались бы от квартиры и пошли в суд, если в ДДУ указан 12-й этаж, а на ключах дают 2-й?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В день выдачи ключей семья из Тюмени приехала за своей квартирой в новостройке, а открыла дверь на другом этаже. В ДДУ, приложении с поэтажным планом и всей истории покупки стоял 12-й этаж. На месте оказался второй: ниже окна, другой вид, больше шума и совсем другое чувство приватности. Представитель застройщика объяснил это «перераспределением в секции» и технической корректировкой проекта. Готового согласия семьи на замену квартиры при этом не было.

**Para 2:** Я Святослав Шакин, The Риэлтор в Тюмени. В Telegram разбираю такие ситуации с новостройками, а в MAX можно задать вопрос и следить за разбором.

## Case hook (from research / article)
- Тюмень, новостройка, ДДУ, выдача ключей, передаточный акт
- В ДДУ и поэтажном плане — 12-й этаж; на ключах открыли дверь на 2-м
- Застройщик: «перераспределение в секции», «техническая корректировка проекта»
- Семья не давала согласия на другой этаж; акт не подписали
- Давление: «подписывайте, иначе ипотека затянется»
- Сняли видео, потребовали акт о несоответствии, направили претензию — досудебная стадия
- Этаж — идентифицирующая характеристика объекта по 214-ФЗ, не «мелочь при приёмке»
- Проектная декларация ≠ согласие на другой лот
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- новостройки Тюмени (55+11176); приёмка квартиры, ДДУ, этаж, акт приёма-передачи
- buyer risk: несоответствие ДДУ, подмена этажа, ипотека на финише

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЕГРН

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
