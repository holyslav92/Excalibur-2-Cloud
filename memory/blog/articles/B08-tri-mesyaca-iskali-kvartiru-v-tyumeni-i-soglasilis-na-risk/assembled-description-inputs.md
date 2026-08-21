# Description inputs — B08 — 2026-08-21

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B08

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Квартиру в Тюмени ищут четвёртый месяц. Уже согласны на риск

**subject:** покупка вторички в Тюмени: усталость покупателя после месяцев поиска и осознанное согласие на юридический риск по документам

**angle:** Klyshin-ритм: четвёртый месяц поиска — узнаваемая боль; усталость превращается в согласие на риск. НЕ B05 (скидка+задаток), НЕ B06 (автооценка+очередь), НЕ B07 (наследство+сын).

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** «Святослав, мы четвёртый месяц смотрим. Устали. Согласны на риск — только помогите сделать безопасно».

**Para 2:** Звучит спокойно. По смыслу — сдача позиций. Дальше идёт описание квартиры, и в описании уже видно, где будет больно: право перешло к продавцу пару месяцев назад, продают «по доверенности», история собственников читается с трудом.

**Para 3 (context only):** В одной фразе — два взаимоисключающих запроса. «Согласны на риск» значит: мы готовы принять вероятность потерь. «Сделайте безопасно» значит: уберите вероятность потерь.

## Case hook (from research / article)
- Семья 3–4 месяца смотрит вторичку в Тюмени, «ну ладно, хотя бы эту»
- Согласны на риск по документам, но просят «сделать безопасно» — взаимоисключающие запросы
- Проверка не обнуляет риск, а делает его видимым до аванса
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить квартиру в тюмени» 22990; «вторичка в тюмени» 5813
- «купить квартиру в тюмени вторичка» 3965
- Buyer risk: усталость, аванс, ЕГРН, доверенность

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЕГРН, ЦИАН

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
