# Assembled research inputs — B34 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `research-notes.md` only per `.cursor/skills/excalibur-research/SKILL.md` from facts below. Language: Russian. Do NOT output BLOCKER text instead of notes.

**research_date:** 2026-10-02  
**topic_id:** B34  
**title (working):** В Тюмени в презентации ЖК обещали взнос 35 — в ДДУ 89, ипотеку урезали  
**slot_rubric:** novostroyki  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** newbuild_management_fee_ddu_appendix_vs_sales_tyumen  
**viral_mechanism:** договор vs реальность (paper_clean_then_broke)

## Scout handoff (2026-10-02)

- **dzen_casus_shape:** PASS  
- **comment_magnet:** «Если в презентации 35 ₽, а в приложении к ДДУ уже 89 ₽ за квадрат — вы подписали бы, чтобы не потерять бронь, или развернулись бы сразу?»  
- **newbuild_mechanism:** семья с ребёнком, трёшка в строящемся ЖК Тюмень. PDF/презентация отдела продаж: «плата за содержание с ключей — от 35 ₽/м²». На предподписании ДДУ приложение №3: **89 ₽/м²**, ежегодная индексация, отдельная строка на капремонт. Банк пересчитал полную нагрузку (ипотека + содержание) и **урезал одобренную сумму ~620 тыс. ₽**. Семья **не подписала** ДДУ, эскроу не открывали, **бронь 150 тыс. ₽** вернули после претензии. В другой корпус не переходили.  
- **why_newbuild_not_secondary:** только цепочка первички (бронь застройщика, презентация, приложение к ДДU, ипотека, эскроу). Без вторичного продавца, ДКП, ЕГРН вторички.  
- **anti_dupe_hard / story_dup / h1_fingerprint:** PASS (см. `.cursor/excalibur-blog-handoff.md`)  
- **Klyshin:** none — свежий Tyumen casus  
- **Editorial:** не чек-лист; конфликт «красивая презентация vs приложение к ДДУ»; без countdown «за N дней до эскроу» в H1  

### Casus boundary (internal)

Редакционный композитный кейс для Дзен news-casus. **Не** подавать как репортаж с фамилиями, названием ЖК, банка или застройщика. Суммы **35 / 89 ₽/м²**, **~620 тыс.**, **150 тыс. бронь** — параметры сюжета, не рыночная норма по Тюмени.

## Wordstat (live MCP-KV, 2026-10-02, regions 55+11176 unless noted)

| phrase | volume | note |
|--------|-------:|------|
| новостройки тюмень | 4360 | **P0 spine** (Scout final) |
| купить новостройку в тюмени | 905 | support |
| договор долевого участия | 392 | support (RF-wide in probe) |
| плата за содержание жилья | 6 | weak — mechanism in H1/body |
| управляющая компания новостройка | 2 | weak |
| дду новостройка тюмень | empty API | partial |
| эскроу счет новостройка | empty API | partial |

**rework_log:** Scout kept casus + P0 «новостройки тюмень» 4360; tariff 35→89 mechanics in story not in Wordstat P0.

## Fresh signals this week (required — accessed 2026-10-02)

1. **Tyumen-info.ru — 29.09.2026** — проект повышения минимального взноса на капремонт с **14,62** до **15,20 ₽/м²**, план с **1 октября 2026**, документ на согласовании. https://tyumen-info.ru/society/2026/09/29/46542.html  

2. **Tumentoday.ru — 25.09.2026** — комментарий директора департамента ЖКХ С. Тегенцева: текущий взнос **14,62 ₽/м²**, проект индексации **+4%** → **15,20 ₽/м²** с **1 октября**, проект на согласовании. https://tumentoday.ru/2026/09/25/vznos_na_kapremont_v_tyumenskoy_oblasti_mozhet_vyrasti_na_4/  

3. **Vse42.ru / Nash Gorod line — late Sept 2026** — цитата проекта постановления: минимальный взнос **15,2 ₽/м²**, вступление с **01.10.2026** (проект). https://vse42.ru/news/33643495  

4. **Pravda.ru — 22.09.2026** — обзор: рост капремонта в Тюменской области, среднероссийский минимум **16,76 ₽/м²** (лето 2026) vs региональный контекст. https://www.pravda.ru/news/districts/2413526-tyumen-kapremont-tarify/  

5. **Tenant channels (ongoing casus context):** https://t.me/Tyumen_Rieltor , https://dzen.ru/holyslav  

6. **SERP cluster (same week):** серия casus автора на Дзен про расхождения перед ДДУ/эскроу в Тюмени (площадь, скидка, срок сдачи) — энергия рубрики «договор vs реальность», не подтверждение цифр 35/89.

## Legal / regulatory facts (for Writer — not lead copy)

### 214-ФЗ (ДДУ, эскроу, декларация)

- **214-ФЗ** регулирует ДДU, проектную декларацию (ст. 19), обязательные условия договора (ст. 4–6), эскроу (ст. 15.4–15.5).  
- Canonical: https://www.consultant.ru/document/cons_doc_LAW_51038/  
- **Презентация отдела продаж / PDF** — не замена ДДU и не документ для регистрации; обязательства по квартире и цене фиксируются в **тексте ДДU + приложениях**, которые покупатель подписывает.  
- **Эскроу** открывается в цепочке после согласования ДДU; до подписания ДДU и регистрации нет финальной фиксации сделки (см. ст. 15.4–15.5 214-ФЗ).  
- **Бронь 150 тыс.** в кейсе — **не** эскроу; отдельное соглашение о бронировании; возврат после отказа от ДДU — исход кейса после претензии, не универсальная гарантия без текста договора брони.

### ЖК РФ — содержание vs капремонт

- **Ст. 156 ЖК РФ:** плата за **содержание** жилого помещения должна обеспечивать содержание общего имущества; в типовой модели после заселения размер для дома без ТСЖ часто определяется **общим собранием собственников** с учётом предложений УК, **не менее чем на год** (ч. 7).  
- **Ст. 156 ч. 8.1:** **минимальный взнос на капитальный ремонт** устанавливает **субъект РФ** (отдельная строка от «содержания»).  
- Canonical art. 156: https://www.consultant.ru/document/cons_doc_LAW_51057/4b915eab001a797267f9e18ef420f11e94aeaf2c/  
- **Writer constraint:** «35 ₽ содержание» в презентации и «89 ₽ + индексация + капремонт» в приложении к ДДU могут включать **разные корзины расходов**; нельзя автоматически приравнивать строки без расшифровки приложения.

### Официальный региональный капремонт (Tyumen) — для контекста, не для цифр 35/89 в кейсе

- **Фонд капремонта ТО (fkr72.ru):** с **01.07.2025** минимальный взнос **14,62 ₽/м²** (ссылка на постановление Правительства ТО № 395-п от 26.06.2025). https://www.fkr72.ru/owners/detail/regionalnaya-programma-kapitalnogo-remonta/  
- **Планируемое** повышение до **15,20 ₽/м²** с **01.10.2026** — по проектам СМИ **на 02.10.2026 ещё на согласовании**; в notes пометить «проект, не финальный акт на дату research».

### Ипотека, ПДN, урезание лимита

- **Предварительное одобрение** не гарантирует финальную сумму кредита; банк может пересчитать **ПДN / допустимый платёж** при изменении полной ежемесячной нагрузки (ипотека + иные обязательные платежи, в т.ч. **ожидаемое содержание** — по внутренней методике банка).  
- **~620 тыс. ₽** урезания лимита — **параметр кейса**, не норма ЦБ.  
- **Ключевая ставка ЦБ 14,00%** с **24.07.2026** — фон для ипотеки, не индивидуальный тариф. https://www.cbr.ru/press/pr/?file=24072026_133000key.htm  
- **Не называть** конкретный банк и **не** приписывать ему точный % ПДN без official person-page.

## Reader framing (internal)

- **reader_problem:** семья уже «вложилась» эмоционально и финансово (бронь, одобрение, презентация с низкой «коммуналкой с ключей»), а на предподписании ДДU видит другую ежемесячную нагрузку; боится потерять бронь, но ипотека перестаёт сходиться.  
- **reader_outcome:** поймёт, что презентация ≠ приложение к ДДU; содержание и капремонт — разные корзины; рост «коммуналки» в приложении может **пересчитать ипотечный лимит**; до подписания ДДU и эскроу можно остановиться и требовать расшифровку строк **и** условий брони письменно.  
- **voice_angle:** спокойно, без «все застройщики мошенники»; agency — сверить приложения до подписи, запросить смету, переспросить банк о полной нагрузке.  
- **surprising_fact (sourced):** региональный минимум **капремонта** в ТО (**14,62 ₽/м²** с июля 2025) на порядок ниже сюжетных **89 ₽/м² «содержания»** в приложении кейса — значит в 89 ₽ likely bundled services/indexation, not only state minimum kapremont.

## official_verifications table (must appear in notes)

| claim | audience | value | official_url | accessed_at | verified |
|-------|----------|-------|--------------|-------------|----------|
| Минимальный взнос на капремонт ТО | собственники МКД | 14,62 ₽/м² с 01.07.2025 | https://www.fkr72.ru/owners/detail/regionalnaya-programma-kapitalnogo-remonta/ | 2026-10-02 | yes |
| Ключевая ставка ЦБ | макро / ипотека | 14,00% с 24.07.2026 | https://www.cbr.ru/press/pr/?file=24072026_133000key.htm | 2026-10-02 | yes |
| Плата за содержание / капремонт — разные механизмы | физлица-собственники | ст. 156 ЖК РФ (ч. 7, 8.1) | https://www.consultant.ru/document/cons_doc_LAW_51057/4b915eab001a797267f9e18ef420f11e94aeaf2c/ | 2026-10-02 | yes |
| ДДU / эскроу контекст | участники долевого строительства | 214-ФЗ | https://www.consultant.ru/document/cons_doc_LAW_51038/ | 2026-10-02 | yes |
| План 15,20 ₽/м² с 01.10.2026 | собственники | **проект**, не финальный акт на дату research | https://tyumen-info.ru/society/2026/09/29/46542.html | 2026-10-02 | yes (media, project status) |

**No bank tariff rows.** Casus numbers 35, 89, 620k, 150k — **not** official_verifications.

## Overlap

Only `published-titles-only.md` — cluster distinct from B25/B27/B31/B32 (приёмка, земля, страховка, эскроу-реквизиты).

## writer_safe_urls

- https://www.consultant.ru/document/cons_doc_LAW_51038/
- https://www.consultant.ru/document/cons_doc_LAW_51057/4b915eab001a797267f9e18ef420f11e94aeaf2c/
- https://www.fkr72.ru/owners/detail/regionalnaya-programma-kapitalnogo-remonta/
- https://www.cbr.ru/press/pr/?file=24072026_133000key.htm
- https://t.me/Tyumen_Rieltor
- https://dzen.ru/holyslav
- https://max.ru/id561413315447_biz
- tel:+79220016505

## Forbidden in notes output

- h2_outline, action_outline, FAQ skeleton, ready lead paragraph  
- «случай собирательный» / «не репортаж» meta in writer-facing prose blocks (casus_boundary section is OK internal)  
- Copying neighbor research-notes prose style verbatim

Produce complete `research-notes.md` with sections: research_date, topic_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, local_context, voice_angle, surprising_fact, official_verifications, source_table, writer_safe_urls.
