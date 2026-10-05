# Assembled research inputs — B34 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Live fetch already done by conductor — all URLs and facts are verified below. Do **NOT** refuse, do **NOT** ask for MCP, do **NOT** meta-narrate. Output **only** the markdown body for `research-notes.md` (max ~1200 words) per SKILL.md sections from the facts below.

**research_date:** 2026-10-05  
**topic_id:** B34  
**title:** В Тюмени на вторичке оценка на 900 тысяч ниже ДКП — банк снял одобрение  
**slot_rubric:** vtorichka (17:00 YEKT)  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** `secondary_bank_appraisal_below_dkp_price_tyumen`  
**viral_mechanism / trend energy:** `paper_clean_then_broke` — «на бумаге чисто», одобрение и документы создают ощущение финиша, **остановка до денег** (до аванса/ДКП), **NOT** календарный spine «с 1 октября семейная ипотека» (это только фон рынка, не главный сюжет).

## Scout / director handoff

- **P0 Wordstat:** «купить вторичное жилье в тюмени» — **749** (regions 55+11176).
- **dzen_casus_shape:** PASS — вторичка, ДКП, оценка vs цена, банк снял одобрение.
- **comment_magnet_angle:** «Если оценка на 900 тысяч ниже цены в ДКП — вы успеете договориться с продавцом или банк заберёт одобрение?»
- **anti_dupe:** отличие от опубликованной **новостройки** «900 тыс ниже ДДУ» (другой cluster); от **B06** (автооценка ЦИАН/Домклик, не банковский отчёт); от **B33** (долг ЖКУ).
- **fact boundaries:** composite casus; без имён банка/оценщика/адреса; **900 000 ₽** — параметр разрыва цена ДКП vs отчёт; «снял одобрение» = банк отозвал/приостановил предварительное одобрение после отчёта, аванс **не внесён**.

### Locked editorial spine (paper clean → broke before money)

1. Семья на вторичке в Тюмени: торг согласован, **предварительное одобрение** ипотеки по доходу, выписка ЕГРН «чистая», продавец готов к ДКП по согласованной цене — **на бумаге всё сходится**.
2. Банк запускает **обязательную для вторички** оценку аккредитованным оценщиком **до** аванса и подписания ДКП (не путать с отложенной оценкой по ДДУ).
3. Отчёт: **рыночная/залоговая** стоимость на **900 000 ₽ ниже**, чем цена в проекте ДКП (пример: ДКП 6,0 млн vs оценка 5,1 млн — иллюстрация масштаба, не утверждение рыночной цены Тюмени).
4. Банк считает кредит от **меньшей** из двух величин (цена договора vs оценка); не хватает первоначального взноса **или** внутренний лимит/ПДН → **одобрение снято** / требуется новый пакет; семья **не дошла до аванса**.
5. Продавец давит «другие смотрят»; покупатель понимает, что одобрение по **личности** ≠ одобрение **объекта**.
6. Agency: заказать оценку/сверку **до** аванса, торг после отчёта, письменный ответ банка, условие возврата задатка, второй банк параллельно.

## Wordstat MCP-KV (live 2026-10-05, regions 55 + 11176)

| phrase | volume | note |
|--------|-------:|------|
| купить вторичное жилье в тюмени | **749** | P0 |
| купить квартиру в тюмени вторичное жилье | 605 | synonym |
| продажа квартир в тюмени вторичка | 724 | sibling demand |
| ипотека тюмень вторичка | 111 | mechanism |
| оценка квартиры для ипотеки | 28 | narrow; Tyumen slice weak |
| оценка квартиры для ипотеки втб | 9 | bank+jargon |

**wordstat_rework:** узкий «оценка для ипотеки» → spine P0 749 + sibling «продажа… вторичка» 724 + «ипотека вторичка» 111.

## Fresh signals (week of 2026-10-05; accessed 2026-10-05)

1. **72.ru — 02.10.2026** — рост интереса к вторичке (+21% ДКП г/г за 8 мес 2026 по данным Авито/Роскадастр в материале). https://72.ru/text/realty/2026/10/02/76673072/
2. **72.ru — 05.10.2026** — экспертный разбор новых правил семейной ипотеки (фон спроса на вторичку, **не** главный casus). https://72.ru/text/economics/2026/10/05/76678646/
3. **IRN.ru — 02.10.2026** — рекорд спроса на вторичку и выдач семейной ипотеки 30.09.2026 (контекст ажиотажа и спешки). https://www.irn.ru/news/160752-spros-na-vtorichku-vyros-do-rekordnogo-urovnya-kak.html
4. **Дзен tenant — alc8GjRgISluH81l** (свежий пост канала): порядок «одобрение → ЕГРН → **сверка цены с оценкой банка** → аванс»; кредит от **меньшей** из цены договора и оценки; зазор **10–15%** как ориентир риска. https://dzen.ru/a/alc8GjRgISluH81l
5. **SERP sibling (не копировать сюжет новостройки):** dzen apud4MSWjwEsm5rC — «оценка ниже на 400 тыс — бронь сгорела» (механика близкая, другие цифры/контекст).
6. **Российская газета — обзор 2026** — банк выдаёт кредит от меньшей из цены договора и оценочной стоимости (механика, не тариф банка). https://rg.ru/post/kak-kupit-kvartiru-v-ipoteku-na-vtorichnom-rynke-poshagovaia-instrukciia.html
7. **UnistroyRF explainer** — на вторичке оценка **до** сделки, без отчёта банк не выходит на сделку. https://unistroyrf.ru/blog/ocenka_kvartiri_dlya_ipoteki/
8. **Telegram @Tyumen_Rieltor**, **Дзен holyslav** — tenant CTA channels.

## Law / official (no invented bank %)

- **102-ФЗ «Об ипотеке»** — залоговая/оценочная стоимость определяется по соглашению залогодателя и банка; банк вправе заложить **залоговую** стоимость ниже рыночной отчёта (контекст 9111.ru → ст. 14 ч. 1 п. 9). Consultant: https://www.consultant.ru/document/cons_doc_LAW_19396/ (102-ФЗ).
- **Domclick (экосистема Сбера, физлица)** — explainer: ипотека на вторичке требует оценки; личное/имущественное страхование и порядок — не подменяют индивидуальный тариф. https://blog.domclick.ru/ipoteka/post/strahovanie-pri-ipoteke (использовать для рамки «оценка обязательна на вторичке», не для % LTV без строки на person-странице).
- **Не утверждать** конкретный % LTV (80/90) от имени Сбера/ВТБ без person-страницы; в обзорах RG — «например 80%» как иллюстрация механики с пометкой «уточнять в своём банке письменно».
- **Отчёт об оценке:** в отраслевых разборах срок актуальности **6 месяцев** для сделки (Vladis blog) — если сделка тянется, нужен новый отчёт.

## Overlap published (titles only)

- B06 — автооценка сервисов, не банковский отчёт перед ДКП.
- B31 — страховка + новостройка + ДДU.
- Опубликованный cluster «900 тыс ниже **ДДU**» — **новостройка**; B34 — **900 тыс ниже ДКP**, вторичка.

## Output

Complete `research-notes.md` with: research_date, topic_id, cluster_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, voice_angle, surprising_fact, official_verifications table, source_table (accessed_at 2026-10-05), writer_safe_urls (TG, MAX, dzen holyslav). No h2_outline, no lead prose, no FAQ skeleton.
