# Description inputs — B34 — 2026-09-29

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B34

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени аренда на 3 года в ЕГРН остановила сделку

**subject:** зарегистрированная аренда квартиры на вторичном рынке

**angle:** На финальном осмотре перед авансом покупатели увидели в ЕГРН договор найма на три года. Обещание продавца выселить арендатора к ключам не заменило юридическое последствие: после покупки новый собственник стал бы наймодателем на прежних условиях.

**comment_magnet_angle:** Если арендатор живёт в квартире, а договор на три года зарегистрирован в ЕГРН, ждать обещанного выезда к ключам или сразу снимать сделку с повестки?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья остановила покупку вторички за 7 дней до аванса: на повторном осмотре в квартире обнаружился жилец с зарегистрированным в ЕГРН договором найма на 3 года. Ипотеку уже одобрили, первый осмотр прошёл спокойно, а продавец уверял, что к передаче ключей наниматель съедет. Но обещанный выезд — не то же самое, что оформленное прекращение найма. Покупатели не стали передавать деньги и остановили подготовку сделки до подписания договора купли-продажи. Документ, который вовремя показали в квартире, изменил всю картину покупки.

**Para 2:** Я Святослав Шакин, The Риэлтор, Тюмень. Разбираю, что проверять в квартире и документах до аванса, — в Telegram и MAX.

## Case hook (from research / article)
- Тюмень, вторичка, ипотека одобрена, до аванса семь дней
- Первый осмотр — пустая квартира, выписка без обременений
- Повторный осмотр — жилец, письменный договор найма на 3 года + регистрация в ЕГРН
- Продавец обещал выезд к ключам; семья не внесла аванс
- Ст. 675 ГК: новый собственник = наймодатель на прежних условиях
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- вторичка, договор найма, ЕГРН, аванс, осмотр квартиры
- buyer risk: зарегистрированное обременение найма, обещание vs документ

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакin context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЕГРН, ГК РФ

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
