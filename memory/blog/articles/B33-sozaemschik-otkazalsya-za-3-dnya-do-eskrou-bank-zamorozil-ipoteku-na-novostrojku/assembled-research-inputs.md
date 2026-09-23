# Assembled research inputs — B33 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below.

**research_date:** 2026-09-23  
**topic_id:** B33  
**title (working):** За 3 дня до эскроу созаёмщик отказался подписывать — банк заморозил ипотеку на новостройку в Тюмени  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** `newbuild_co_borrower_refused_three_days_before_escrow_tyumen`  
**top_energy_mirror:** `clock_ran_out` / `stopped_before_money`  
**newbuild_mechanism:** семья покупает **строящуюся новостройку** в Тюмени по **ДДУ**; ипотека оформляется на **двух созаёмщиков**. За **3 дня** до планового **открытия эскроу** один из созаёмщиков **отказывается подписывать** ипотечный комплект (согласие, анкеты, страховка, поручительство/созаёмщик). **Банк приостанавливает** ипотечную сделку / «замораживает» одобрение до согласования состава заёмщиков; **эскроу не открывается**; бронь **~50–90 тыс ₽** под угрозой. **Деньги на эскроу не ушли.**

## Scout / director lock (2026-09-23)

- **NOT:** B32 чужое юрлицо в реквизитах эскроу; B31 страховка за 2 дня до ДДУ; B30 уступка 3 года; B20 смена юрлица застройщика; B19 маткапитал/эскроу не открыли.
- **dzen_casus_shape:** PASS  
- **comment_magnet_angle:** «Если второй созаёмщик перед эскроу «передумал» — банк успеет заменить его или покупку новостройки придётся откладывать?»  
- **why_newbuild_not_secondary:** только ДДУ, эскроу, ипотека на строящийся объект от застройщика  
- **anti_dupe_hard:** PASS — fingerprint `co_borrower_refused_three_days_escrow_frozen`  
- **fact boundaries:** composite editorial casus; не выдавать за подтверждённый репортаж о конкретной семье/банке; без имён ЖК, банка, фамилий

### Locked editorial spine

1. Семья с одобренной ипотекой на квартиру в строящемся ЖК Тюмени; два созаёмщика (супруги/родственники); бронь внесена.  
2. Офис и банк готовят пакет к открытию эскроу; дата «Х» через 3 дня.  
3. Один созаёмщик отказывается подписывать комплект (конфликт, страх долга, развод в процессе, «не хочу быть в кредите» — без конкретики в notes).  
4. Банк: без подписей всех участников сделки **не выдаёт** финальное одобрение / **приостанавливает** выдачу / блокирует открытие эскроу в привязке к ипотеке.  
5. Застройщик напоминает о сроке брони; эскроу **не открыт**.  
6. Финал: покупка **не завершена** до повторного согласования состава заёмщиков и документов банком; деньги на эскроу **не ушли**; agency — что проверить/обсудить до даты эскроу, не «бегите с рынка».

## Wordstat MCP-KV (live 2026-09-23, regions 55, 11176, compare 225)

| phrase | 55 | 11176 | 225 | note |
|--------|---:|---:|---:|------|
| купить новостройку в Тюмени | **679** | **902** | **1914** | P0 spine |
| ипотека Тюмень новостройки от застройщика | **66** | — | — | mechanism support |
| квартира в ипотеку в Тюмени новостройки | **65** | — | — | support |

**wordstat_rework:** final P0 «купить новостройку в Тюмени» — **679 / 902 / 1914**.

## SERP / fresh signals (research-serp.json 2026-09-23; accessed 2026-09-23)

1. **Дзен tenant adjacent** — «В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу» (энергия сюжета, **не** копировать как факт B33). https://dzen.ru/a/aqo1GEjUgT5jhTW5

2. **Дзен** — «В Тюмени банк отказал жене-созаёмщику за 4 дня до открытия эскроу — покупка новостройки остановилась» (типовой механизм недели). https://dzen.ru/a/aqARhcSWjwEswQ2z (snippet context)

3. **RG.ru 15.09.2026** — контекст эскроу и новостроек 2026. https://rg.ru/2026/09/15/a-chto-na-schet.html

4. **novostroikino.ru 2026** — эскроу обязателен с 01.07.2019 для новостроек по 214-ФЗ; отказ в ипотеке — причины (контекст, не единственный источник). https://novostroikino.ru/blog/otkaz-v-ipoteke-na-novostroyku-prichiny-i-chto-delat-2026/

5. **realeo.ru** — эскроу простыми словами 2026. https://realeo.ru/guide/eskrou-schet

6. **kvarnado.ru** — когда раскрывается эскроу; проверки. https://kvarnado.ru/glossarij/guide-kogda-raskryvaetsya-eskrou-schet

7. **Telegram tenant** https://t.me/Tyumen_Rieltor

8. **Дзен tenant** https://dzen.ru/holyslav

## Legal / official anchors (accessed 2026-09-23)

- **214-ФЗ** — ДДУ, счета эскроу (ст. 15.4–15.5), проектная декларация. https://www.consultant.ru/document/cons_doc_LAW_51038/
- Ипотека на двух заёмщиков: оба участника обычно подписывают кредитный договор и связанные документы; банк вправе не продолжать сделку при отказе одного созаёмщика — формулировать как типовая банковская практика без названия конкретного банка и без выдуманных сроков замены.

## Distinction from published (titles only — see published-titles-only.md)

| topic | why different |
|-------|----------------|
| B32 | чужой бенефициар в реквизитах эскроу за 2 дня |
| B31 | страховка / платёж до ДДУ |
| B19 | эскроу не открыли (иной блок) |
| B33 | **созаёмщик отказался подписывать** за 3 дня до эскроу, ипотека приостановлена |

## Practical facts for Writer (no H2 skeleton)

- Созаёмщик ≠ поручитель: в кейсе речь о **созаёмщике** по ипотеке на новостройку; оба несут солидарную ответственность по кредиту — отказ одного блокирует типовой пакет.
- Эскроу открывается в связке с ДДУ и ипотекой; без финального банковского комплекта дата открытия срывается.
- Замена созаёмщика — отдельная процедура (новое одобрение, доходы, согласие супруга и т.д.); **не** обещать «за 3 дня всегда успеют» — зависит от банка и срока одобрения.
- Бронь 50–90 тыс — диапазон кейса; условия возврата — договор бронирования, не федеральная норма.
- Не утверждать, что банк «законно обязан» заменить созаёмщика за N дней.
- Composite casus: механика типовая, конкретная семья не подтверждена публичным репортажем.

## official_verifications (required section in output notes)

| claim | audience | value | official_url | accessed_at | verified |
|-------|----------|-------|--------------|-------------|----------|
| 214-ФЗ: ДДУ, эскроу | все | нормы | https://www.consultant.ru/document/cons_doc_LAW_51038/ | 2026-09-23 | yes |
| Конкретный банк: тарифы, срок замены созаёмщика, комиссии | физлица | не заявлять без person-page банка | — | 2026-09-23 | n/a |

## writer_safe_urls

- https://www.consultant.ru/document/cons_doc_LAW_51038/
- https://novostroikino.ru/blog/otkaz-v-ipoteke-na-novostroyku-prichiny-i-chto-delat-2026/
- https://realeo.ru/guide/eskrou-schet
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav

## voice_angle / surprising_fact (if supported)

- Сделка «почти готова» по календарю эскроу, но один отказ подписи **останавливает** всю цепочку до денег на счёте.
- Многие обсуждают ставку и площадь, но не **оба** подписи до даты эскроу.

Output complete Russian `research-notes.md` per SKILL (no h2_outline, no lead). Include `source_table`, `## official_verifications`, reader_problem/outcome, constraints, case_status composite. Also produce `research-agent-report.json` fields as markdown section `## agent_report` with PASS if fresh signal present.
