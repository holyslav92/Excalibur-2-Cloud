# Scout handoff — B24

**run_date:** 2026-09-06, Sunday 15:00 YEKT (owner weekend slot)  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**topic_market_focus:** newbuild_only  
**topic_id:** B24  
**status:** LOCKED FOR RESEARCH

## Locked topic

**Title draft / H1:** В Тюмени в ДДУ обещали участок 12 соток — в кадастре оказалось 8

**Slug:** `v-tyumeni-v-ddu-obeshchali-uchastok-12-sotok-v-kadastre-okazalos-8`

**Cluster ID:** `newbuild_kp_plot_size_mismatch_ddu_cadastre_tyumen`

**P0 demand spine:** `новостройки тюмень`

## Core news-casus

Семья в Тюмени выбрала дом в коттеджном посёлке от застройщика: в рекламе, на визуализации и в проекте ДДУ участок указан как 12 соток. Покупатели внесли бронь, получили одобрение ипотеки и заказали выписку ЕГРН с кадастровым планом перед подписанием ДДУ. За 5 дней до сделки кадастр показал 8 соток — часть площади ушла под сервисную зону и подъездную дорогу, которых не было в презентации. Банк остановил открытие эскроу на полную сумму, застройщик предложил «доплатить за 4 сотки отдельным договором». Семья разорвала бронь и вернула часть аванса; спор ушёл в досудебку.

Сюжет только о **новом доме от застройщика** в КП (ДДУ, эскроу, ипотека на ИЖС/КП), не о вторичном участке.

## Required handoff fields

**wordstat_preflight:** mcp-kv `wordstat_get_user_info` OK; Yandex Cloud API.

**top_energy_mirror:** `paper_clean_then_broke` — в ДДУ и рекламе «12 соток», кадастровая выписка перед деньгами показывает 8.

**newbuild_mechanism:** дом в коттеджном посёлке от застройщика — площадь участка в ДДУ/презентации vs фактическое межевание и ЕГРН; банк не открывает эскроу на полную цену.

**why_newbuild_not_secondary:** покупка нового дома у застройщика по ДДУ с эскроу и ипотекой; не сделка с физлицом на вторичном рынке земли.

**klyshin_hook:** optional | none | original: none | signal: none

**anti_repeat_preflight:** live_blog_20 + ledger + used-clusters sync OK 2026-09-06 | closed: double DDU sale, доплата отделки, delay keys, DDU m² mismatch (квартира), apartaments B23, trade-in, переуступка, оценка банка, категория земли (другой механизм)

**dzen_casus_shape:** PASS  
- **event:** семья берёт дом в КП, бронь + ипотека под 12 соток  
- **risk:** кадастр 8 соток, эскроу не открывают, цена не пересчитана  
- **time:** за 5 дней до подписания ДДУ  
- **finale:** бронь разорвана, досудебка; ключи не получили

**comment_magnet_angle:** «Если в ДДУ 12 соток, а на межевании 8 — подписали бы ДДУ „как есть“ или разорвали бронь, даже если дом почти готов?»

## Wordstat demand

**wordstat_rework:**  
- probe `дом в коттеджном поселке тюмень` 55 → **42**  
- probe `купить дом в коттеджном поселке тюмень` 55 → **20**  
- rework → P0 `новостройки тюмень` **4663** (55) / **8691** (RU225)

**wordstat:** mcp_kv live | regions 55, 11176, compare 225 | P0 `новостройки тюмень` — **4663** (55); **8691** (compare 225)

## Anti-duplicate results

**story_dup_check:** PASS | cluster_id: `newbuild_kp_plot_size_mismatch_ddu_cadastre_tyumen`

**h1_fingerprint_check:** PASS | fingerprint: `12_соток_8_кадастр_дду_кп`

**formula_spam_check:** PASS | last3_mechanisms: double_sale_ddu, доплата_отделки_ключи, delay_keys_penalty — новая механика: площадь участка ДДУ vs кадастр в КП

**anti_dupe_hard:** PASS

## Signal URLs

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51057/
- https://www.domrf.ru/
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Research brief

1. ДДУ на дом с земельным участком в КП: где фиксируется площадь, границы, кадастровый номер.
2. Межевание, ЕГРН, проектная декларация — как сверять до подписания.
3. Ипотека + эскроу на дом/участок: когда банк останавливает сделку при расхождении площади.
4. Права дольщика при уменьшении площади vs реклама/ДДУ.
5. Отличие от «категории земли» (уже опубликован другой casus).
