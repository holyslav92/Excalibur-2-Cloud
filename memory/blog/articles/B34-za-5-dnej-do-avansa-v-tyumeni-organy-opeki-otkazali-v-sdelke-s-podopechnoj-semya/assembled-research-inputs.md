# Assembled research inputs — B34 (Derouter research role)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed Wordstat + scout gates. **Your job is ONLY to write `research-notes.md` and valid `research-agent-report.json` body in markdown** — no tool calls, no BLOCKER, no refusal. Use ONLY facts below + cited URLs; do not invent news beyond composite casus parameters.

**research_date:** 2026-10-01  
**topic_id:** B34  
**slot_rubric:** vtorichka  

## Composite casus (Writer source of truth)

- Семья с **двумя детьми**, двушка на вторичке в Тюмени, ипотека одобрена, цена согласована.  
- Продавец — женщина **~72 года**, признана **недееспособной**, сделку ведёт **сын-опекун**.  
- На словах: «согласие органов опеки уже есть».  
- Выписка ЕГРН без обременений.  
- За **5 дней** до планового аванса **~380 000 ₽** риэлтор запрашивает **письменное** согласие органов опеки.  
- Приходит **отказ**: цена/условия не обеспечивают интересы подопечной (нет подтверждения альтернативного пригодного жилья).  
- Опекун давит срочностью («подпишем предварительный без опеки»).  
- Семья **не внесла аванс**; сделка остановлена до ДКП.  
- **comment_magnet:** «Если опекун говорит «разрешение есть», а письма из опеки нет — вы бы внесли аванс или ушли сразу?»

## Wordstat (live 2026-10-01, MCP-KV)

| phrase | regions | volume |
|--------|---------|-------:|
| купить квартиру в тюмени вторичка | 55+11176 | 3305 |
| вторичное жилье в тюмени | 55+11176 | 910 |
| опека при продаже квартиры | 55+11176 | 41 |
| опека при продаже квартиры | 225 | 2678 |

## Fresh signals (accessed 2026-10-01)

1. **sudact.ru** — раздел «Опека и попечительство» (судебная практика). https://sudact.ru/practice/opeka-i-popechitelstvo2/  
2. **pravo-pro.ru** — материал о прекращении/отказе опеки (контекст органов опеки). https://pravo-pro.ru/blog/posts/prekrashchenie-opeki/  
3. **72.ru** — чеклисты рисков вторички (коммуналка/документы до аванса), 04.09.2026. https://72.ru/text/realty/2026/09/04/76622643/  
4. **Telegram** https://t.me/Tyumen_Rieltor — community signal accessed 2026-10-01  
5. **Дзен** https://dzen.ru/holyslav — community accessed 2026-10-01  

## Legal (official type in source_table)

- **ГК РФ ст. 26, 28, 30** — сделки недееспособных и подопечных, согласие органов опеки (consultant.ru / garant.ru canonical).  
- **Семейный кодекс ст. 64** — права и обязанности опекунов (контекст представительства подопечного).

## official_verifications

Не применимо (нет банковского тарифа в casus) — note PASS N/A.

Output full research-notes.md per SKILL (sections: research_date, topic_id, cluster_id, reader_problem, reader_outcome, casus_boundary, practical_facts, source_table, wordstat_table, official_verifications) AND end with fenced JSON block for research-agent-report.json status PASS.
