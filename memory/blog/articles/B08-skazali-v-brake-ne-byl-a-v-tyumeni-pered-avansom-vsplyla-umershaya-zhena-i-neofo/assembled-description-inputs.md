# Description inputs — B08 — 2026-08-22

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B08

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Справка ЗАГС была чистой — банк отказал из-за доли умершей жены

**subject:** Справка ЗАГС и супружеская доля умершей жены при продаже вторичной квартиры

**angle:** Формально действующая справка не отражала брак на дату покупки квартиры; невыделенная доля умершей супруги привела к отказу банка и срыву сделки.

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Справка ЗАГС была на руках. Настоящая, с печатью.

**Para 2:** Выписка из ЕГРН — чистая: ни арестов, ни обременений, ни запретов на регистрацию. Двое собственников, брат и сестра, отвечали спокойно и без пауз. Цена согласована. Документы собраны. Покупатель ждал одобрения по ипотеке и уже мысленно расставлял мебель.

**Para 3 (context only):** Сделка развалилась до аванса. Банк отказал, продавцы приводить документы в порядок не захотели.

## Case hook (from research / article)
- Брат и сестра продавали квартиру, купленную в 1998 году
- На вопрос о браке: «в браке не состояли» + справка ЗАГС
- Справка охватывала период только с 2004 года — про 1998-й молчит
- Один продавец на дату покупки был в браке; супруга умерла
- Супружескую долю не выделяли; наследники фактически приняли, права не оформили
- Один наследник тоже умер — цепочка длиннее
- ЕГРН чистая, но наследников в реестре нет
- Банк отказал в ипотеке; покупатель вышел до аванса
- Автор: Святослав Шакин, риэлтор в Тюмени

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить квартиру в тюмени» 22880; «вторичка» 4023
- «наследство квартира продажа» 157; «согласие супруга на продажу квартиры» 49
- Buyer risk: аванс, ипотека, справка ЗАГС не на дату покупки, невыделенная доля

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. News card energy: завершённое событие, финал (банк отказал / до аванса)
5. Geo/facts: Тюмень / Шакин context OK
6. No label head («Риэлтор Тюмень» alone), no checklist spoiler, no how-to blurb
7. Cyrillic; brands OK: ЕГРН, ЗАГС

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
