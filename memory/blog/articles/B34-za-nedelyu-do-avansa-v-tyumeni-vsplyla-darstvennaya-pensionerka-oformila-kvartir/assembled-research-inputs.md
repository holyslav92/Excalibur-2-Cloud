# Assembled research inputs — B34 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `research-notes.md` only per SKILL.md from facts below. Do NOT output BLOCKER.

**research_date:** 2026-09-29  
**topic_id:** B34  
**title:** За неделю до аванса в Тюмени всплыла дарственная — пенсионерка оформила квартиру на сына  
**slot_rubric:** vtorichka  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** secondary_recent_donation_relative_chain_before_advance_tyumen  

## Scout handoff (source of casus mechanics — modeled composite, not court report)

- **dzen_casus_shape:** PASS  
- **comment_magnet:** «Если квартиру недавно подарили родственнику, а продавец торопит с авансом — вы бы внесли деньги или сначала проверили всех наследников и дарителей?»  
- **viral_mechanism:** almost lost перед авансом — «чистая» выписка ЕГРН (один собственник, без обременений) не раскрывает недавнюю дарственную в цепочке.  
- **finale:** аванс **420 000 ₽** не внесён; сделку остановили **до** договора купли-продажи; продавец торопил («дарение между близкими — нормально»).  
- **timeline:** за **7 дней** до планового аванса на безопасный счёт; дарственная от **пенсионерки-матери** продавцу-сыну **~4 месяца** назад.  
- **buyer setup:** двушка на вторичке в Тюмени, ипотека одобрена, торг согласован; на осмотре мать продавца «просто живёт рядом».  
- **risk line:** недавний переход по дарению → риск оспаривания (давление на пожилого дарителя, дееспособность, интересы других родственников/наследников), быстрая перепродажа после дарения.  
- **why_not_newbuild:** без ДДУ, эскроу, застройщика.  
- **anti-dupe:** distinct from B33 (ЖКУ/свет), B03 (дарение дочери на торгах банкротства), B10 (телефон/родственники).  
- **signal_urls:** https://dzen.ru/holyslav , https://t.me/Tyumen_Rieltor , https://dzen.ru/a/Zw9N_lUREDllN79D (energy only), https://dzen.ru/a/arnh-zgnvihPFEtB (тема: пенсионеры переоформляют жильё на родственников — mechanics/energy, не копировать сюжет).

## Wordstat (live 2026-09-29, MCP-KV)

| phrase | regions | volume |
|--------|---------|-------:|
| оформление квартиры на родственника | 55+11176 | 21 |
| оформление квартиры на родственника | 225 (RU compare) | 2058 |
| купить квартиру в тюмени вторичка | 55+11176 | 3413 |
| дарение квартиры близкому родственнику | 55+11176 | 164 |
| продажа квартиры после дарения | 55+11176 | 3 (weak — не P0) |

**P0:** оформление квартиры на родственника (21 local / 2058 RU). Buyer spine: купить квартиру в тюмени вторичка 3413.

## Fresh signals (accessed 2026-09-29)

1. **72.ru — 29.09.2026** — рынок Тюмени: с 1 октября меняются условия семейной ипотеки; покупатели торопятся закрыть сделки до дедлайна → контекст давления «успеть до аванса». https://72.ru/text/realty/2026/09/29/76665356/

2. **72.ru — 04.09.2026** — юрист: свежая выписка ЕГРН **не даёт абсолютной гарантии**; нужно основание прошлого перехода (дарение, наследство, КП), тревожные сигналы — недавние перепродажи, сделки между родственниками, продажа сразу после приобретения. https://72.ru/text/realty/2026/09/04/76622643/

3. **newstyumen.ru — 24.09.2026** — региональная лента: новые правила семейной ипотеки с 1 октября (контекст срочности покупателей). https://newstyumen.ru/society/2026/09/24/98780.html

4. **Telegram канал тенанта** https://t.me/Tyumen_Rieltor

5. **Дзен автора** https://dzen.ru/holyslav

## Legal / official (for Writer — cite only these for hard law claims)

| claim | source | accessed |
|-------|--------|----------|
| С 13.01.2025 договор дарения **недвижимости** между гражданами — **обязательное нотариальное удостоверение** (459-ФЗ, ст. 574 ГК РФ) | http://publication.pravo.gov.ru/document/0001202412130012 + https://www.consultant.ru/document/cons_doc_LAW_461829/f7434c3f82e03bdb4533ba4e2cab29aa1026553d/ | 2026-09-29 |
| Закон направлен в т.ч. на защиту социально уязвимых дарителей; в финальной редакции **нет** исключения для близких родственников | consultant overview 459-ФЗ | 2026-09-29 |
| Основания **отмены дарения** (покушение на жизнь/вред здоровью дарителя, угроза утраты вещи с неимущественной ценностью, банкротство дарителя-ИП/юрлица и др.) — ст. **578** ГК РФ | https://www.consultant.ru/law/podborki/otmena_dareniya_v_sudebnom_poryadke/ | 2026-09-29 |
| Недействительность сделки при недееспособности/ограниченной дееспособности, обмане, насилии — общие нормы ГК (ст. **177**, **179** и след.) — для оспаривания дарения родственниками/наследниками | https://www.consultant.ru/document/cons_doc_LAW_5142/ | 2026-09-29 |

**Do NOT** state exact notary tariff %/₽ unless added to official_verifications from notariat.ru / НК РФ person pages — optional context only as «уточнять у нотариуса».

## Practical checks (from 72.ru 04.09.2026 + scout)

- Запросить **выписку о переходе прав** (история) + правоустанавливающие документы на **каждый** недавний переход.  
- Отдельно: кто **даритель**, возраст/дееспособность, были ли другие наследники/дети/супруг, нотариальная форма (после 13.01.2025).  
- «Один собственник в ЕГРН» ≠ отсутствие споров по прошлой дарственной.  
- Быстрая перепродажа после дарения — фактор повышенного внимания (в т.ч. в разборах Росреестра для вторички — через обзоры СМИ, не как единственный источник).  
- До аванса: стоп и полная цепочка; не смешивать с новостройкой/эскроу.

## official_verifications required in output

- 459-ФЗ / ст. 574 ГК — notarial gift of real estate between individuals (official pravo.gov + consultant).  
- ст. 578 ГК — cancellation grounds (consultant podborka / GK).  
- No bank commission claims.

## writer_safe_urls

https://t.me/Tyumen_Rieltor , https://dzen.ru/holyslav , https://max.ru/id561413315447_biz , https://72.ru/text/realty/2026/09/04/76622643/ , https://72.ru/text/realty/2026/09/29/76665356/

Output complete `research-notes.md` with sections: research_date, topic_id, cluster_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, voice_angle, surprising_fact, official_verifications (table), source_table (accessed_at 2026-09-29), writer_safe_urls. No h2_outline, no lead prose.
