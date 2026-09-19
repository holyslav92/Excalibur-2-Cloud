# Assembled research inputs — B27 (for Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER` or refuse synthesis. Output the full `research-notes.md` body only per SKILL.md from the facts below.

**research_date:** 2026-09-19  
**topic_id:** B27  
**title:** В Тюмени в проектной декларации земля под ЖК в аренде — в брони обещали собственность, за 4 дня до ДДУ отказались  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**author_city:** Тюмень  
**cluster_id:** `newbuild_land_lease_not_ownership_declaration_tyumen`  
**top_energy_mirror:** `paper_clean_then_broke`  
**newbuild_mechanism:** sales office says land in developer ownership; project declaration section 12 shows state/municipal lease with end date; family + investor check before DDU and bank visit; refuse to sign; booking returned in 12 days; money never transferred to escrow

## Scout handoff (2026-09-19)

- **dzen_casus_shape:** PASS
- **comment_magnet_angle:** «Если под домом не собственность, а аренда до 2049 года — вы бы всё равно подписали ДДУ, если менеджер клянётся, что “переоформят потом”?»
- **locked editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank, address):**
  1. Sales office + booking: manager shows landscaping plan, says «участок наш, в собственности»
  2. Family with two children + investor under family mortgage track; booking 150 000 ₽; DDU signing scheduled
  3. Evening before bank visit, 4 days before DDU: open project declaration on dom.rf/EISZhS
  4. Section 12: «Право аренды», municipal/state land, lease end **2049** (editorial lock from Scout — not tied to one verified named Tyumen ЖК)
  5. Developer offers «подпишите как есть, потом переоформим»
  6. Buyers refuse DDU; money not sent to escrow; booking cancelled; 150 000 ₽ returned in **12 days**
- **why_newbuild_not_secondary:** only DDU/214-FZ/declaration/booking chain; no secondary seller, EGRN secondary, inheritance, matkapital on secondary
- **anti_dupe:** cluster `newbuild_land_lease_not_ownership_declaration_tyumen` — distinct from escrow, parking, wrong corpus, keys delay, co-borrower, RVE, finishing mismatch clusters

## Overlap (published-titles-only.md)

Published B02–B15, B19–B26. **B27 — другой plot:** расхождение **устного обещания о собственности на землю** vs **раздел 12 проектной декларации (аренда + срок)** → отказ от ДДУ **до перевода денег**. Не B19/B20 (эскроу), не B12 (ключи/срок), не B25 (отделка).

## Wordstat MCP-KV (2026-09-19)

| phrase | region | volume | note |
|--------|--------|-------:|------|
| новостройки тюмень | 55+11176 | **4446** | P0 spine |
| купить новостройку в тюмени | 225 | **1936** | compare225 |
| новостройки в тюмени от застройщика | 55+11176 | **656** | supporting |
| проектная декларация застройщика | 55+11176 | **25** | weak mechanism tail; «дом рф проектная декларация» 11 |
| семейная ипотека новостройка | 55+11176 | **90** | «новостройки тюмени семейная ипотека» 24 |

**rework_from:** «земельный участок аренда застройщик» (3) too weak → spine «новостройки тюмень» + mechanism in text.

## Fresh signals (accessed 2026-09-19)

1. **Tyumen EISZhS PDF — declaration № 72-001426 от 02.09.2026** (МЖД, г. Тюмень, ул. Циолковского; СЗ «ЛЮДИ ЦЕНТР»): section **12.1.1 — Право собственности**; lease end field empty (ownership). URL: https://io.cdnstroy.ru/ot98ht7c2ijcf_1eb35mz.pdf
2. **Tyumen EISZhS PDF — declaration № 72-000935 от 04.07.2025** (МЖК ул. Малышева–Бирюзова, СЗ «СОЗДАТЕЛИ. ВТОРОЙ»): **12.1.1 — Право аренды**; **12.1.6 — окончание права: 17.11.2026**; кадастр **72:23:0106001:4795**; площадь **20 321 м²**; собственник участка — **ИП Петерс А.Ю.** (застройщик арендует у частного собственника, не «своя земля»). URL: https://i2.cdnstroy.ru/2v74hehqr4c5c_1e5cesz.pdf
3. **Tyumen EISZhS PDF — «Архитектурный ансамбль Вознесенский», declaration with lease until 20.07.2032**; **12.1.1 — Право аренды**; собственник — **ООО «Тюменская овчинно-меховая фабрика»**; кадастр **72:23:0109002:3067**. URL: https://io.cdnstroy.ru/o8uu0ktt4qv65_11ew2po.pdf
4. **Tenant Telegram @Tyumen_Rieltor** (live fetch 2026-09-19): ongoing newbuild lead posts; contextual post with promo **«до 15 сентября»** — week-of-research community signal. URL: https://t.me/Tyumen_Rieltor
5. **Dzen channel tenant** https://dzen.ru/holyslav — material «Эскроу в Тюмени защищает деньги, а не срок — ДДУ читают до брони» (newbuild: read contract before booking, not just escrow slogan).

## Legal framework — verified (214-ФЗ, consultant.ru, accessed 2026-09-19)

### Ст. 3 ч. 1 — право привлекать деньги дольщиков
Застройщик вправе привлекать средства **только после** разрешения на строительство, размещения проектной декларации и госрегистрации **права собственности на ЗУ** **либо договора аренды/субаренды** (или безвозмездного пользования в случаях закона).  
→ **Аренда земли сама по себе не делает проект «незаконным»**, если аренда зарегистрирована и отражена в декларации.  
URL: https://www.consultant.ru/document/cons_doc_LAW_51038/24a7b7f2b0571ac53f7b789c337316109c23d1a7/

### Ст. 13 ч. 1 — залог в пользу дольщиков
С момента регистрации ДДУ у дольщиков в залоге: ЗУ в собственности застройщика **или право аренды/субаренды** + строящийся дом.  
URL: https://www.consultant.ru/document/cons_doc_LAW_51038/8cd5c59176348e82c463bf71be71c5d897762b67/

### Ст. 19 — проектная декларация
- Официальный документ; определяет объём прав застройщика на привлечение средств.
- **Ч. 4:** изменения вносятся **ежемесячно не позднее 10-го числа** следующего месяца через ЕИСЖС.
- **Ч. 7:** при нарушении требований к декларации дольщик может оспорить сделку как совершённую под заблуждением.
- **Ч. 8:** ответственность за неполную/недостоверную информацию в декларации.
URL: https://www.consultant.ru/document/cons_doc_LAW_51038/a9d2c9fd3a6b153a7b2094a93824ee93f1ed2881/

### Ст. 21 п. 3, 5 — информация о проекте
Декларация содержит сведения о **правах застройщика на ЗУ** (вид права, реквизиты документа, собственник если застройщик не собственник, кадастр, площадь) и **документы, подтверждающие права**. По требованию дольщика застройщик обязан предоставить их для ознакомления.  
URL: https://www.consultant.ru/document/cons_doc_LAW_51038/aa003239194cdccc51aac0d1eae29e47362cac58/

### Форма декларации — Приказ Минстроя № 239/пр от 04.04.2022
**Раздел 12:** права на ЗУ — пункты 12.1.1 (вид права: собственность / аренда / субаренда), 12.1.6 (дата окончания права), 12.2 (собственник ЗУ если застройщик не собственник), 12.3 (кадастровый номер, площадь).  
URL: https://www.consultant.ru/document/cons_doc_LAW_417299/

## Practical facts for Writer (no invented ЖК names)

### Где смотреть
- Единственный обязательный актуальный источник декларации — **ЕИСЖС / наш.дом.рф** (не PDF из мессенджера, не буклет).
- В карточке выбрать **конкретный корпус/этап** — у соседних корпусов одного бренда земля и право могут различаться.
- Сверять: раздел **12** декларации ↔ проект ДДУ ↔ разрешение на строительство (номер, срок, адрес, кадастр).

### Что значит «аренда» для покупателя (осторожные формулировки)
- **Не утверждать автоматически:** «дом незаконен», «ДДУ недействителен», «банк откажет в семейной ипотеке» — зависит от срока аренды vs срока строительства, условий договора аренды, политики банка, эскроу.
- **Проверять:** 12.1.6 — срок окончания аренды **перекрывает** срок ввода/передачи по декларации и ДДУ с запасом; 12.2 — кто собственник (город/регион/частное лицо); совпадение кадастра с корпусом.
- **Устное «переоформим в собственность потом»** без отражения в декларации, приложениях к ДДУ или письменного обязательства застройщика **не заменяет** раздел 12.
- На практике менеджеры могут называть аренду «наш участок» — kvarnado.ru, novostroikino.ru (2026 guides): сверять декларацию с рекламой **до** брони/аванса.

### Tyumen localization (verified public declarations, not the unnamed casus ЖК)
- В тюменских декларациях **и собственность, и аренда** — оба легальные формата (примеры выше).
- Реальные сроки аренды в публичных тюменских PDF: **17.11.2026**, **20.07.2032** — не 2049; редакционная цифра **2049** в casus = Scout lock, иллюстрирует **длинную муниципальную/государственную аренду**, но **не подтверждена** для конкретного названного объекта.
- Департамент земельных отношений и градостроительства Администрации города Тюмени фигурирует как орган, выдавший разрешение на строительство в декларациях по арендованным участкам.

### Бронь и отказ до ДДУ (editorial anchors only)
- Бронь **150 000 ₽** — locked Scout figure for composite casus; типовой порядок возврата зависит от **условий бронирования** (срок, основания удержания); в casus — возврат через **12 дней**, деньги на эскроу **не переводились** (риск ниже, чем при открытом эскроу).
- Семейная ипотека: банк может запросить пакет по объекту и застройщику; расхождение устных обещаний с декларацией — повод **остановиться и уточнить письменно**, не автоматический отказ.

### Что сравнивать в разделе 12 (checklist facts, not H2)
- 12.1.1 вид права (собственность / аренда / субаренда)
- 12.1.3–12.1.5 номер, дата, регистрация договора
- 12.1.6 дата окончания права
- 12.2 собственник земли (если не застройщик)
- 12.3 кадастровый номер и площадь ↔ корпус в ДДУ
- История изменений декларации на dom.rf (ежемесячные обновления)

## Constraints / typical mistakes (Writer)
- Не называть конкретный ЖК, застройщика, банк, адрес, фамилии — composite casus.
- Не писать «аренда = мошенничество / нельзя строить / банк точно откажет».
- Не подменять casus общим гайдом «как проверить новостройку».
- Не уходить во вторичку, бабушку, ЕГРН вторички, эскроу-кластеры B19/B20.
- Не утверждать, что в Тюмени «всегда 2049» — только editorial casus number.
- Устное обещание «собственность» vs декларация «аренда» — **конфликт документов**, не «мелочь».
- Подписывать ДДУ «как есть» надеясь на «переоформят» — типичная ошибка; без письменной фиксации в договоре/декларации риск на покупателе.
- Бронь ≠ проверка декларации; проверку делать **до** перевода денег на эскроу и подписания ДДУ.

## voice_angle
«Бумажная собственность»: в офисе — «участок наш», в разделе 12 — «право аренды» и чужой собственник или город. Конфликт не про «страшную аренду», а про то, что **официальный документ не совпал с обещанием** за четыре дня до ДДУ.

## surprising_fact
По ч. 1 ст. 3 214-ФЗ застройщик **имеет право** привлекать деньги при зарегистрированной **аренде** земли — проблема casus не в самом слове «аренда», а в том, что менеджер обещал **другое**, а покупатель узнал об этом из декларации, а не из договора.

## writer_safe_urls
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- tel:+79220016505
- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_51038/

## Output requirements
Write full `research-notes.md` per SKILL: reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, local_context, voice_angle, surprising_fact, official_verifications (legal norms only — no bank tariffs), source_table (all accessed_at 2026-09-19), writer_safe_urls. No h2_outline, no lead, no FAQ.
