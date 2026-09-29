# Assembled research inputs — B30 (for Derouter research role)

**MANDATORY:** You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research` with utility tier `gpt-5.6-terra`. Output the full `research-notes.md` body only per SKILL.md from the facts below. Do NOT refuse or output BLOCKER.

**research_date:** 2026-09-19  
**topic_id:** B30  
**title:** В Тюмени в макете квартиры был второй санузел — в экспликации ДДУ его не оказалось, сделку заморозили  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**cluster_id:** `newbuild_layout_second_bathroom_missing_ddu_tyumen`  
**top_energy_mirror:** `paper_clean_then_broke`  
**newbuild_mechanism:** новостройка Тюмени; шоу-рум + PDF с **двумя санузлами**; бронь ~40–70 тыс. ₽; ипотека под площадь; за **2 дня** до ДДУ в **экспликации** черновика — **один** санузел; обещание «поправим» не сработало; **стоп до эскроу**; composite casus

## Scout handoff

- **comment_magnet:** «Если в макете два санузла, а в ДДУ один — вы бы подписали “с поправкой потом” или развернулись до эскроу?»  
- **why_newbuild_not_secondary:** только ДДУ/маркетинг застройщика/эскроу, без вторички  
- **anti_dupe_hard:** PASS; отличие от B27–B29 сегодня и от B23 (апартаменты vs квартира)

### Locked editorial spine (composite Tyumen casus)

1. Семья смотрит квартиру в **новостройке** Тюмени; в шоу-руме и буклете — **два санузла** (мастер + гостевой).  
2. Менеджер фиксирует номер квартиры, семья платит **бронь** (~40–70 тыс. ₽), банк одобряет ипотеку под **эту** площадь.  
3. За **2 дня** до подписания ДДУ приходит **проект договора** с **экспликацией помещений** — в тексте **один** совмещённый санузел, площадь меньше, чем в макете.  
4. Менеджер: «это черновик, в финальном поправим» — **второй** проект ДДУ **без** второго санузла.  
5. Семья **не подписывает** ДДУ, **эскроу не открывается**; спор о возврате брони.

## SERP / community (research-serp.json, accessed 2026-09-19)

- Dzen holyslav: «12-й этаж в ДДУ — на ключах 2-й» (другой plot — этаж, не санузел).  
- Dzen: двойная продажа одной квартиры — **другой** cluster.  
- Яндекс.Недвижимость journal: ДДУ в новостройке 2026 — общий контекст.  
- Kadgeo blog: **экспликация помещений** — что это и зачем в сделке.

## Wordstat (regions 55+11176, 2026-09-19)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4430 |
| купить новостройку в тюмени | **920** (P0) |
| новостройки в тюмени от застройщика | 663 |
| планировка квартиры новостройка | 23 |

## Legal / regulatory facts (accessed 2026-09-19)

- **214-ФЗ**: предмет ДДУ должен однозначно описывать объект (в т.ч. через **приложения**: план, экспликация). https://www.consultant.ru/document/cons_doc_LAW_51038/  
- **Экспликация помещений** в ДДУ — перечень помещений с площадями; расхождение с рекламной планировкой = риск спора о предмете договора **до** эскроу.  
- Пока нет регистрации ДДУ и внесения на **эскроу**, покупатель не зафиксировал объект в контуре 214-ФЗ — остановка на черновике **юридически безопаснее**, чем подписать «с поправкой потом».

## official_verifications

| claim | value | official_url | accessed_at |
|-------|-------|--------------|-------------|
| Расчёты по ДДУ на эскроу | 214-ФЗ схема | https://www.consultant.ru/document/cons_doc_LAW_51038/ | 2026-09-19 |

## Constraints for Writer

- Composite casus — без имён ЖК/застройщика/банка.  
- **Не** путать с B23 (апартаменты), B28 (газ КП), сегодняшним кейсом **потолки −25 см** (другой cluster).  
- **Не** обещать автоматический возврат брони.  
- Практика: сверять **экспликацию** и план в **приложении к ДДУ** с макетом **до** подписи и эскроу.

## voice_angle

«На стене красиво два санузла, в договоре — один. Пока не подписали, вы ещё можете развернуться».

## writer_safe_urls

- https://www.consultant.ru/document/cons_doc_LAW_51038/
- https://kadgeoresurs.ru/blog/vsyo-ob-eksplikatsii-pomeshchenij-chto-eto-zachem-nuzhna/
- https://realty.yandex.ru/journal/post/kak-kupit-kvartiru-v-novostroyke-po-ddu/
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- tel:+79220016505

## Output requirements

Write full `research-notes.md` per SKILL: research_date, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, local_context, voice_angle, surprising_fact, official_verifications, source_table (accessed_at 2026-09-19), writer_safe_urls. Include fresh community signal (Dzen holyslav SERP this week). No h2_outline, no lead, no FAQ.
