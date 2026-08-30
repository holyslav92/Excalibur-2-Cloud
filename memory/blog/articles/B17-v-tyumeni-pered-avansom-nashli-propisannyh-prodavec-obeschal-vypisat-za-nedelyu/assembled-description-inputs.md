# Description inputs — B17 — 2026-08-30

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B17

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Перед авансом в Тюмени нашли прописанных — сделку остановили

**subject:** Прописанные в квартире при покупке вторички в Тюмени

**angle:** Конкретный случай перед авансом показывает, почему обещание продавца выписать родственников не заменяет проверку зарегистрированных лиц.

**comment_magnet_angle:** Продавец клянётся, что прописанные уйдут сами за неделю — вы бы поверили и внесли аванс?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Сделка встала не из-за цены, не из-за банка и не из-за торга. Из-за двух человек, которых в квартире не было, — а в бумагах они были.

**Para 2:** Конец августа, Тюмень, обычная вторичка. Покупатели смотрели квартиру дважды, договорились по сумме, назначили день аванса — всё шло тем спокойным темпом, когда уже мысленно расставляешь мебель. За три дня до передачи денег выяснилось, что в квартире зарегистрированы двое: бывшая жена продавца и его взрослый сын, и ни один из них не собственник. Продавец пожал плечами: формальность, выпишутся за неделю. Покупатели аванс не внесли — деньги не передавались, сделку остановили прямо на переговорах. И это, если по-честному, самый дешёвый способ, каким такая история вообще может закончиться.

## Case hook (from research / article)
- Тюмень, вторичка, за три дня до аванса
- В справке — бывшая жена продавца и взрослый сын, не собственники
- ЕГРН чистый, но «в Росреестре всё чисто» ≠ «никого не прописано»
- Продавец: «выпишутся за неделю, формальность»
- Заявлений на снятие с учёта нет — только слово
- Покупатели остановили сделку до передачи денег — дешёвый финал
- Регистрация не блокирует сделку, но оставляет чужое право пользования
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «прописка при покупке квартиры» 477 RU / 10 Tyumen
- «прописанные в квартире риски» 4; buyer risk: аванс, ЕГРН vs справка о зарегистрированных

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ЕГРН, Росреестр, МФЦ

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B17",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
