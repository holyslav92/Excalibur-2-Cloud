# Description inputs — B19 — 2026-08-31

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B19

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку

**subject:** Долг по взносам на капитальный ремонт при покупке вторичной квартиры

**angle:** Чистая выписка ЕГРН и квитанции без просрочек не выявили долг по капремонту — его нашли отдельной справкой и остановили сделку до аванса.

**comment_magnet_angle:** Достаточно ли чистой выписки ЕГРН, или справку о долгах по капремонту нужно запрашивать всегда?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Сделку в Тюмени остановил не арест, не прописанный ребёнок и не спор о праве. Её остановила строка, которой в выписке ЕГРН не было вовсе.

**Para 2:** Семья выбрала вторичку в панельном доме: цена сошлась, банк одобрил ипотеку под конкретный объект, дату сделки согласовали. Выписка ЕГРН выглядела образцово — право зарегистрировано, обременений и ограничений нет. Продавец выложил на стол квитанции, видимой просрочки в них не читалось. За три дня до аванса — уже после юридической проверки и одобрения банка — покупатели запросили сведения о взносах на капитальный ремонт и увидели накопленный долг в сотни тысяч рублей. Ждать, пока продавец его закроет и принесёт подтверждение, они отказались: аванс не внесли, деньги не передали, сделка встала.

## Case hook (from research / article)
- Тюмень, вторичка в панельном доме, семья с одобренной ипотекой
- ЕГРН «чистая» — право, без обременений; банк одобрил ипотеку
- Продавец показал квитанции без видимой просрочки — но квитанция ≠ выписка по лицевому счёту
- За три дня до аванса запросили сведения по взносам на капремонт (не вода/свет, именно капремонт)
- Справка показала накопленный долг в сотни тысяч — в ЕГРН его не было
- Покупатели отказались ждать погашения — аванс не внесли, сделка встала
- Долг по капремонту переходит к новому собственнику (ст. 158 ч. 3 ЖК) — финансовый риск, не запрет регистрации
- Справка из УК ≠ справка по капремонту; фонд ТО — fkr72.ru
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «купить квартиру в тюмени вторичка» 4146; «долг по капремонту» 29
- buyer risk: ЕГРН, аванс, капремонт, справка по лицевому счёту, вторичка

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler, no «N шагов»
6. Cyrillic; brands OK: ЕГРН
7. Do NOT claim Rosreestr blocks registration — only financial risk / deal stopped before advance
8. Do NOT start with «Сделку в Тюмени остановил» (para 1 opening)

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B19",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
