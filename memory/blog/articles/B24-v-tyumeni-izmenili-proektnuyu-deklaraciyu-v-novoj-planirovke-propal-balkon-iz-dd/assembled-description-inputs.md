# Description inputs — B24 — 2026-09-09

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B24

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени пропал балкон на ключах — банк заморозил транш

**subject:** Балкон в квартире новостройки по ДДУ

**angle:** На приёмке балкона из приложения к ДДУ не оказалось: застройщик сослался на обновлённую проектную декларацию, акт не подписали, а банк остановил последний ипотечный транш.

**comment_magnet_angle:** Если балкон указан в приложении к ДДУ, но застройщик показывает новую декларацию, подписывать акт или требовать устранения нарушения по 214-ФЗ?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья приехала на приёмку и увидела вместо застеклённого балкона глухую стену — через два дня банк заморозил последний ипотечный транш. В приложении к ДДУ балкон был на плане: контур, площадь, место на этаже. Застройщик показал свежую проектную декларацию и объяснил, что проект изменили. Для семьи главным остался подписанный план из договора, а не новый файл на наш.дом.рф — ключи в этот день не выдали.

**Para 2 (early CTA):** Я, Святослав Шакин, The Риэлтор из Тюмени, разбираю такие ситуации в Telegram и MAX. Там можно следить за новостройками Тюмени, приёмкой квартир и изменениями в ипотечных сделках.

## Case hook (from research / article)
- Тюмень, новостройка, семья с ипотекой и эскроу
- В приложении к ДДУ — застеклённый балкон (контур, площадь, место на этаже)
- Застройщик обновил проектную декларацию на наш.дом.рф, ссылается на «сняли по проекту»
- На приёмке вместо балкона — глухая стена
- Акт не подписали, претензия по 214-ФЗ (устранение или уменьшение цены)
- Через два дня банк остановил последний ипотечный транш; ключи не выдали
- Проектная декларация ≠ допсоглашение к ДДУ
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- новостройки Тюмень, ДДУ, приёмка квартиры, проектная декларация
- buyer risk: балкон в плане, акт приёмки, ипотечный транш, эскроу

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, 214-ФЗ, банк

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
