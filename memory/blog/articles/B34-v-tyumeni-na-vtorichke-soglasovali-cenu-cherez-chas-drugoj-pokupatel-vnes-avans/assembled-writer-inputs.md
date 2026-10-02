Assembled Writer inputs — B34 — 2026-10-02

ROLE: Writer (смысл). Derouter writer_chunk — HTML fragments only, no fences, no h1.

H1 context (не в HTML): В Тюмени согласовали цену на двушку — через час её забрали авансом

slot_rubric: vtorichka (только вторичка — без ДДУ, эскроу, брони новостройки, дарения как механизма сюжета)

HARD: ~1400–1600 слов total, hard max 1750. News-casus vtorichka Tyumen. **7 H2** once each. **7 inline placeholders** — после открытия каждого H2 (или сразу под заголовком H2) вставить ровно один:
`<figure class="inline-quad" data-slot="inline_N"><img src="cover/inline-0N.png" alt="" loading="lazy"></figure>` для N=1..7 (src: inline-01.png … inline-07.png).

Interlink **2–4** published siblings (контекстно в теле, не спам):
- /blog/vtorichka-i-riski/za-3-dnya-do-avansa-v-tyumeni-vsplyl-dolg-za-svet-186-tysyach-semya-otkazalas-ot/ (B33 — стоп до аванса на вторичке)
- /blog/vtorichka-i-riski/v-tyumeni-poddelnoe-soglasie-suprugi-ostanovilo-sdelku-pered-avansom/ (B15 — проверка до аванса)
- /blog/vtorichka-i-riski/pochti-vnesli-zadatok-za-48-chasov-do-torgov-kvartiru-podarili-docheri/ (B03 — задаток vs уход объекта)
- /blog/vtorichka-i-riski/raspisku-na-kvartiru-napisali-deneg-na-schete-net/ (B02 — деньги без договора)

Comment magnet (once, immediately after casus finale H2 block, before practical H2):
«Вы бы внесли аванс в тот же день без расширенной выписки или сначала до конца проверили квартиру — даже если её могут забрать?»

CTA zones per quality-bar: after lead 4–6 sentences — `<p class="excalibur-cta excalibur-cta-early">` TG+MAX only (https://t.me/Tyumen_Rieltor, https://max.ru/id561413315447_biz); mid — `excalibur-cta-mid` TG+MAX; end — `excalibur-cta-end` full channel set + phone **once** tel:+79220016505. Use {{SITE_BASE}} for site links in end CTA.

Scout handoff (research-context.json):
- cluster: secondary_rival_buyer_snatched_advance_tyumen
- P0: «купить квартиру в тюмени вторичка» — 3348 (regions 55+11176)
- mechanism: конкуренция на горячем объекте; «договорились» ≠ зафиксировали обязательства

Casus spine (one pass — no triple recap):
- Семья в Тюмени, двушка на вторичке; с продавцом согласовали цену устно и в мессенджере; риэлтор предупредил о других просмотрах.
- Примерно через час другой покупатель передал продавцу аванс; объявление сняли до встречи первой семьи.
- Финал casus: у семьи остаётся одобренная ипотека, выбранная квартира ушла; снова конкурентный поиск.
- Не утверждать, что продавец нарушил закон; переписка ≠ бронь; не писать meta «собирательный случай».

Market context (кратко, не glue в casus): 72.ru — в августе 2026 ~65,6% покупателей квартир в Тюмени выбрали вторичку; средняя цена ~5,1 млн; ипотека на вторичке 24%→32%. Семейная ипотека с 1 октября — только фон спроса, не причина сюжета героев.

Legal/practical (plain Russian, из research): переписка/устная цена ≠ ДКП; предварительный договор (ст. 429 ГК) фиксирует обязанность заключить основной, не право собственности; задаток (ст. 380) vs аванс; Пленум ВС №49 п.23 — риск иной квалификации при большой предоплате; на конкурентном объекте аванс часто слабее задатка для покупателя.

H2: «Двушка на вторичке в Тюмени: цену согласовали, а объявление ещё висело»
H2: «Переписка о цене и очередь из просмотров»
H2: «Через час: другой покупатель внёс аванс — квартиру сняли с продажи»
H2: «Финал для семьи: ипотека на руках, объекта уже нет»
H2: «Почему «договорились» и «зафиксировали деньгами» — разные вещи»
H2: «Что успеть проверить, если объект горячий, а время давит»
H2: «Таблица: переписка, аванс, задаток, предварительный договор»

Ending: agency — письменные условия до денег, не panic «никогда не покупать вторичку»; ручка до аванса.

FACTS: research-notes.md + title-brief.json in same directory.
