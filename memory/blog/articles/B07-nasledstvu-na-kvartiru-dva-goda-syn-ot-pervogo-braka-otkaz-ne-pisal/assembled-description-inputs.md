# Description inputs — B07 — 2026-08-21

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B07

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Квартиру унаследовал один. Сын от первого брака отказ не писал

**subject:** наследство на квартиру: скрытый наследник первой очереди (сын от первого брака) без нотариального отказа — риск при покупке до аванса

**angle:** Klyshin-ритм через контраст «унаследовал один» / «сын не писал». В ЕГРН и в свидетельстве один собственник — а второй наследник первой очереди отказ не оформлял. НЕ B02–B06: не расписка, не доверенность, не задаток, не автооценка; крючок — ненаписанный отказ и мнимая чистота документов.

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Квартира хорошая. Цена адекватная. Продавец один — и в выписке ЕГРН он тоже один. Основание права: свидетельство о праве на наследство. Отец умер около двух лет назад, наследство оформлено, всё «чисто».

**Para 2:** А потом, между делом, в разговоре всплывает: «Ну там ещё сын есть, от первого брака. Он далеко, служит, связи нет. Отказ не писал, но мы потом разберёмся».

**Para 3 (context only):** Вот на этом месте сделка перестаёт быть простой.

## Case hook (from research / article)
- Отец умер ~2 года назад, квартира оформлена на одного собственника
- Сын от первого брака: отказ от наследства не писал, «разберёмся потом»
- Один в ЕГРН ≠ все наследники учтены; свидетельство — документ одного наследника
- Покупатель рискует авансом при незакрытом круге наследников первой очереди
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «наследство квартира» 942 (55+11176); «отказ от наследства» 285; «наследственное дело» 1647
- Buyer risk: аванс, реестр наследственных дел, нотариальный отказ, непроявленный наследник

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЕГРН, ФНП

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B07",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
