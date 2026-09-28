# Assembled research inputs — B33 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. The conductor completed all shell/MCP/Wordstat gates. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below.

**research_date:** 2026-09-28  
**topic_id:** B33  
**title:** За 3 дня до эскроу банк потребовал созаёмщика — в брони семейной ипотеки на новостройку Тюмени обещали одного  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** `newbuild_family_mortgage_coborrower_before_escrow_tyumen`  
**top_energy_mirror:** `clock_ran_out / paper_clean_then_broke`  
**newbuild_mechanism:** семья с двумя детьми покупает **новостройку** Тюмени по **семейной ипотеке**; в брони зафиксировано «одобрение на одного заёмщика, созаёмщик не нужен»; за **3 дня** до открытия эскроу банк требует супругу **созaёмщиком** с подтверждённым доходом, предварительное одобрение «заморожено»; менеджер ОП предлагает подписать ДДU «сначала», семья **отказывается**, эскроу **не открывают**, сделку переносят на другой корпус с пересчётом брони (composite casus — без имён банка/ЖК)

## Scout handoff (2026-09-28)

- **dzen_casus_shape:** PASS  
- **comment_magnet_angle:** «Если банк за три дня до эскроу требует созaёмщика, а в брони обещали одного — вы подписываете ДДU или стопаете сделку?»  
- **why_newbuild_not_secondary:** только бронь ЖК, семейная ипотека на строящееся жильё, эскроу, ДДU с застройщиком  
- **anti_dupe_hard:** PASS; distinct from B29 zero-down, B31 insurance requote, B32 wrong escrow beneficiary, B19 matcap/escrow  
- **fact boundaries:** не называть конкретный банк/ЖК; не утверждать нарушение закона без письма банка

### Locked editorial spine (casus)

1. Предварительное одобрение семейной ипотеки «на одного родителя» — в переписке/брони.  
2. Бронь квартиры в новостройке, назначена дата открытия эскроу-счёта.  
3. За 3 дня: банк меняет состав заёмщиков — нужна супруга созaёмщиком + её доход; одобрение приостановлено/заморожено.  
4. Без финального кредитного решения цепочка ДДU→регистрация→зачисление на эскроу (при ипотеке) не сходится.  
5. ОП: «подпишите ДДU, с банком потом».  
6. Семья **стоп** до подписи, эскроу не открывают, переход на другой корпус + пересчёт брони.

## Wordstat MCP-KV (live 2026-09-28)

| phrase | regions | volume | note |
|--------|---------|-------:|------|
| семейная ипотека тюмень | 55+11176 | **1309** | final P0 |
| семейная ипотека тюмень | 225 (RU) | **1807** | compare |
| семейная ипотека тюмень 2026 | 55+11176 | 422 | support |
| семейная ипотека тюмень условия | 55+11176 | 504 | support |
| купить новостройку в тюмени | 55+11176 | **891** | newbuild spine |
| купить новостройку в тюмени от застройщика | 55+11176 | 421 | support |
| семейная ипотека созaёмщик | 225 | 5476 total; top «супруг созaёмщик» 759 | mechanism demand RU-wide |
| созaёмщик семейная ипотека | 55+11176 | weak &lt;10 | rework probe |

**wordstat_rework:** узкий «созaёмщик семейная ипотека» в Тюмени weak → anchor P0 «семейная ипотека тюмень» 1309 + coborrower в H1/механике.

## Fresh signals (week of 2026-09-28; accessed 2026-09-28)

1. **tyumen-info.ru — 27.09.2026** — тюменский новостной сигнал недели: с 1.10.2026 меняются условия семейной ипотеки (дифференцированные ставки/лимиты, срок до 15 лет). https://tyumen-info.ru/society/2026/09/27/45953.html  
2. **Lenta.ru — 25.09.2026** — обзор изменений программы с 1.10.2026 (Минфин). https://lenta.ru/articles/2026/09/25/izmeneniya-v-programme-semeynoy-ipoteki-s-1-otyabrya-2026-godu/  
3. **Telegram @Tyumen_Rieltor** — канал тенанта, практика сделок. https://t.me/Tyumen_Rieltor  
4. **Дзен tenant** https://dzen.ru/holyslav  
5. SERP community echo (не единственный источник фактов): сюжет «банк / созaёмщик / эскроу / Тюмень» в выдаче — см. research-serp.json query community_experience.

## Official / program (accessed 2026-09-28)

### Минфин РФ (официально)

- С **1 февраля 2026** супруги **обязаны** выступать созaёмщиками по кредитному договору семейной ипотеки; можно привлечь третьих лиц при нехватке дохода; исключение — военная ипотека (117-ФЗ). Принцип «один льготный кредит на семью», договор «в привязке» к детям.  
- URL: https://minfin.gov.ru/ru/press-center/?id_4=40178-izmeneniya_v_programme_semeinaya_ipoteka_v_2026_godu (дата релиза 30.01.2026)

### ДОМ.РФ / программа «Семейная ипотека» (официальная инструкция)

- Ставка до **6%**, ПВ от **20%**, лимит **6 млн ₽** для регионов вне МСК/СПб и их областей; **12 млн** — для столичных регионов.  
- Кредит на **квартиру у застройщика по ДДU** — допустимая цель.  
- «Получить средства может один из родителей **с участием супруга/супруги в качестве созaёмщика**».  
- С **1.02.2026** — «одна семья — одна льготная ипотека»; супруги автоматически созaёмщики (исключения: супруг не гражданин РФ; военная ипотека).  
- Семьи с **двумя несовершеннолетними** без ребёнка до 6 лет / без ребёнка-инвалида — покупка **новостройки у юрлица** только в **35 перечисленных регионах** (Тюменская область **не** в списке на странице инструкции); ограничение **не действует** при строительстве/покупке **дома**.  
- При **недостоверных сведениях о семейном положении** с 01.02.2026 кредитор может **повысить ставку** выше льготной.  
- URL: https://xn--h1alcedd.xn--d1aqf.xn--p1ai/instructions/semeinaya-ipoteka/ (наш.дом.рф)

### Сбербанк — продукт «Семейная ипотека» (person, физлица)

- «Если вы в браке, ваш **супруг должен быть обязательным созaёмщиком**»; исключение — **брачный договор** (по продукту Premium документ не обязателен — отдельная оговорка на странице).  
- СНИЛС нужен от заёмщика **и супруга/супруги**.  
- Лимит продукта на странице: до **12 млн ₽**, ПВ от **20,1%**, срок до **30 лет** (marketing product page — для Тюмени Writer сверяет лимит программы 6 млн vs комбо).  
- URL: https://www.sberbank.ru/ru/person/credits/home/family

### 214-ФЗ — эскроу и ипотека (нормативная рамка, не тариф банка)

- Расчёты по ДДU через эскроу-счета; зачисление средств (в т.ч. ипотечных) — после регистрации ДДU; комиссии за счёт дольщика по закону не взимаются (обзор РБК с отсылкой к 214-ФЗ).  
- Текст закона: https://www.consultant.ru/document/cons_doc_LAW_51038/

## Overlap published-titles-only.md

- **B19** — семейная ипотека + эскроу не открыли (маткапитал), другой финал.  
- **B22** — ставка перед ДДU.  
- **B29** — нулевой ПВ отменили.  
- **B31** — страховка +18k, одобрение сняли.  
- **B32** — чужое юрлицо в реквизитах эскроу за 2 дня.  
- **B33** — **созaёмщик-супруг** vs обещание «один заёмщик» за 3 дня до эскроу.

## Required sections in research-notes.md

Include: research_date, topic_id, cluster_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, voice_angle, surprising_fact, **official_verifications** (table per contract), **source_table** (each row accessed_at 2026-09-28; types: official, news, community), **writer_safe_urls** (t.me/Tyumen_Rieltor, dzen.ru/holyslav, max.ru/id561413315447_biz, plus official URLs above).

**Do NOT** output h2_outline, lead, FAQ, action_outline.

**Do NOT** claim exact bank commissions/tariffs unless verified on person-page.

Output complete research-notes.md now.
