# Assembled research inputs — B34 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below.

**research_date:** 2026-09-29  
**topic_id:** B34  
**title (working):** За 3 дня до эскроу в Тюмени жилая площадь в приложении к ДДУ оказалась на 8 кв. м меньше — банк урезал ипотеку  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slot_rubric:** novostroyki  
**cluster_id:** `newbuild_living_area_ddu_vs_mortgage_shrink_tyumen`  
**top_energy_mirror:** `paper_clean_then_broke` / `stopped_before_money`  

## Scout handoff (2026-09-29)

- **newbuild_mechanism:** семья в Тюмени покупает квартиру в строящемся доме в ипотеку. В брони и ипотечном одобрении — жилая площадь **~68 м²**. За **3 дня** до открытия эскроу в **приложении к ДДУ** — **~60 м²** жилой (пересчёт площади/лоджии). Цена в договоре **не меняется**, банк пересчитывает лимит: не хватает **~420–480 тыс. ₽** собственных. Семья **останавливает сделку до подписания ДДУ и открытия эскроу**.
- **why_newbuild_not_secondary:** приложение к ДДУ на объект в строящемся доме + ипотечный лимит на новостройку; не ЕГРН вторички, не спор с продавцом готового жилья.
- **dzen_casus_shape:** PASS  
- **comment_magnet_angle:** «Если в ДДУ жилая площадь меньше, чем в брони, а цена та же — вы доплачиваете наличными или рвёте сделку?»  
- **anti_dupe_hard:** PASS  
- **fact boundaries:** composite editorial casus; без имён ЖК, банка, фамилий; 68→60 м² жилой — параметры кейса; 420–480 тыс. — диапазон нехватки ПВ/собственных в модели, не тариф банка.

### Distinction from published (titles only)

| topic | why different |
|-------|----------------|
| B25 | отделка/приёмка, не площадь в приложении до эскроу |
| B22 | банк поднял **ставку**, не урезал лимит из‑за площади |
| B31 | страховка/одобрение, не жилая площадь в ДДУ |
| B32 | чужое юрлицо в реквизитах эскроу |
| B29 | исчезла схема ПВ от застройщика |
| B34 | **жилая площадь в приложении к ДДУ меньше брони/одобрения** → банк режет лимит **до** эскроу |

### Locked editorial spine (for facts, not H2)

1. Семья с одобренной ипотекой на новостройку Тюмени; в брони и в ЛК банка — **68 м²** жилой.  
2. Менеджер показывает «ту же» квартиру; цена договора фиксирована.  
3. За 72 часа до открытия эскроу: черновик ДДУ + **приложение с планом** — жилая **60 м²** (лоджия/пересчёт по ПИБ/БТИ-логике в тексте объяснить простым языком).  
4. Ипотечный менеджер: пересчёт залога/лимита — одобрено меньше на **~450 тыс.** (вилка 420–480).  
5. Офис: «доплатите наличными, площадь же общая та же» — семья **не подписывает** ДДУ.  
6. Финал: деньги на эскроу **не ушли**; бронь под вопросом; agency — сверка приложения до подписи.

## Wordstat MCP-KV (live 2026-09-29)

| phrase | volume | regions | note |
|--------|-------:|---------|------|
| купить новостройку в тюмени | **891** | 55+11176 | P0 spine (scout rework 1913 on wider compare — use live 891 for notes) |
| купить новостройку в тюмени от застройщика | 421 | 55+11176 | support |
| новостройки тюмень купить в ипотеку | 71 | 55+11176 | support |
| площадь квартиры дду | **434** | 225 RF | demand on area+DDU (scout) |
| площадь квартиры меньше чем в дду | **47** | 225 | mechanism jargon |
| площадь квартиры приемка новостройки | 27 | 55+11176 | weak local — spine P0 |

**wordstat_rework:** узкий «жилая площадь дду новостройка» 0 → spine «купить новостройку в тюмени» + «площадь квартиры дду» RF.

## Fresh signals (week of 2026-09-29; accessed 2026-09-29)

1. **Российская газета — 18.09.2026** — УрФО: в Тюменской области **самые высокие** показатели раскрытия эскроу; за месяц дольщики оплатили **4,6 тыс.** квартир на **22 млрд ₽**; контекст активных сделок с ДДУ/эскроу в регионе. https://rg.ru/2026/09/18/reg-urfo/bolshe-vsego-eskrou-schetov-raskryli-v-tiumenskoj-oblasti-v-autsajderah-iamal.html

2. **72.ru — 15.09.2026** — тюменский рынок новостроек, покупатели смотрят объекты «вживую» на финальной стадии (контекст недели). https://72.ru/text/realty/2026/09/15/76640741/

3. **Право ПРО — 28.06.2026** — эскроу по 214-ФЗ: деньги блокируются до ввода; этапы ДДУ → регистрация → открытие счёта → внесение средств; просрочка внесения >3 мес. — банк может отказаться от договора счёта (п. 11 ст. 15.5). https://pravo-pro.ru/blog/posts/scheta-eskrou-v-dolevom-stroitelstve/

4. **novostroyker.ru — чек-лист ДДУ 2026** — приложение к ДДУ должно содержать **план и площадь**; сверка с бронью до подписи (обзор, не единственный источник цифр). https://novostroyker.ru/blog/sovety/dolevoe-uchastie-12-punktov-yurista

5. **pravo-pro / domino72 (SERP)** — если фактическая площадь меньше проектной: претензия застройщику, суд (контекст **после** сдачи; в кейсе риск **до** подписи). https://domino72.ru/stati/eskrou-schet-pri-pokupke-novostroyki

6. **Telegram tenant** https://t.me/Tyumen_Rieltor — community channel (scout signal)

7. **Дзен tenant** https://dzen.ru/holyslav — editorial channel (scout signal)

8. **trend radar** memory/blog/trend-radar/trend-radar.json — energy `paper_clean_then_broke`

## Legal / official anchors (accessed 2026-09-29)

- **214-ФЗ** — ДДУ, обязательные условия договора, в т.ч. **характеристики объекта** (включая площадь) в договоре и приложениях; счета эскроу ст. **15.4–15.5** (внесение после регистрации ДДУ). https://www.consultant.ru/document/cons_doc_LAW_51038/
- **214-ФЗ** — изменение цены при расхождении площади при передаче (нормы о допустимом отклонении и перерасчёте — для **после** сдачи; в notes разделить «до подписи» vs «на ключах»).
- **ГК РФ** ст. **860.7–860.10** — договор счёта эскроу (трёхсторонняя схема). https://www.consultant.ru/document/cons_doc_LAW_5142/
- **Жилищный кодекс / постановления** — определения **жилой** vs **общей** площади, правила учёта лоджий/балконов в документации (для объяснения «почему цифры пляшут» без юрпростыни).

## Practical facts for Writer (no H2 skeleton)

- В маркетинговой брони часто фигурирует «жилая 68» с учётом лоджии по одной методике; в **приложении к ДДУ** (план БТИ/ПИБ) лоджия может входить в **общую**, но не в **жилую** — отсюда −8 м² без изменения цены за м² в договоре.
- **Цена договора** может оставаться прежней, пока общая площадь в пределах допуска — но **банк** оценивает объект для ипотеки по своим правилам: меньше жилая/иная конфигурация → ниже оценка → **меньше одобренный лимит** при том же ПВ%.
- Предварительное одобрение привязано к параметрам лота; смена площади в финальном ДДУ — типичный повод для **пересмотра** до выдачи (не утверждать, что любой банк обязан сохранить старый лимит).
- Сверка до подписи: бронь → одобрение банка (площадь) → **приложение к ДДУ** (таблица площадей построчно) → проектная декларация/описание в ЕИСЖС при споре.
- Доплата **420–480 тыс.** в кейсе — модельный разрыв между старым и новым лимитом + собственные; не рыночная статистика Тюмени.
- До открытия эскроу и регистрации ДДУ семья может **остановиться** без перевода на эскроу; бронь — отдельный договор (возврат по условиям брони).
- Не путать с B25 (отделка на приёмке) и с пост-сдачным перерасчётом площади (компенсация застройщику/дольщику по 214-ФЗ).

## official_verifications (required section in output notes)

| claim | audience | value | official_url | accessed_at | verified |
|-------|----------|-------|--------------|-------------|----------|
| 214-ФЗ: ДДУ, эскроу 15.4–15.5, характеристики объекта | все | нормы, без тарифов ₽ | https://www.consultant.ru/document/cons_doc_LAW_51038/ | 2026-09-29 | yes |
| ГК РФ: договор счёта эскроу | все | ст. 860.7–860.10 | https://www.consultant.ru/document/cons_doc_LAW_5142/ | 2026-09-29 | yes |
| Банк России / УрФО статистика эскроу (контекст) | макро | Тюмень лидер по раскрытию эскроу в УрФО (цитата РГ) | https://rg.ru/2026/09/18/reg-urfo/bolshe-vsego-eskrou-schetov-raskryli-v-tiumenskoj-oblasti-v-autsajderah-iamal.html | 2026-09-29 | yes (медиа+ЦБ в материале) |

**Do not** invent bank mortgage recalculation %, LTV tables, or escrow opening fees without bank person-page verification. Gap 420–480 тыс. — **editorial case parameter only**.

## writer_safe_urls

- https://www.consultant.ru/document/cons_doc_LAW_51038/
- https://www.consultant.ru/document/cons_doc_LAW_5142/
- https://rg.ru/2026/09/18/reg-urfo/bolshe-vsego-eskrou-schetov-raskryli-v-tiumenskoj-oblasti-v-autsajderah-iamal.html
- https://72.ru/text/realty/2026/09/15/76640741/
- https://pravo-pro.ru/blog/posts/scheta-eskrou-v-dolevom-stroitelstve/
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav

## voice_angle / surprising_fact

- «Цена та же» в ДДУ не значит «ипотека та же»: банк смотрит на **жилую** в приложении, а не на красивую цифру в брони.
- Многие сверяют цену и этаж, но не **таблицу площадей** в приложении построчно с одобрением.

Output complete Russian `research-notes.md` per SKILL (no h2_outline, no lead). Include `source_table`, `## official_verifications`, reader_problem/outcome, constraints, case_status composite.
