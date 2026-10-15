# Scout handoff — B34

- **run_date:** 2026-09-29
- **slot:** 15:00 Asia/Yekaterinburg
- **tenant:** The Риэлтор — Святослав Шакин
- **site:** tymenrieltor.ru
- **topic_market_focus:** rubric_per_slot
- **slot_rubric:** vtorichka
- **market:** вторичка, Тюмень
- **dzen_rf_pack:** true
- **needs_scout:** false

## Topic

- **topic_id:** B34
- **title_draft:** За неделю до аванса в Тюмени всплыла дарственная — пенсионерка оформила квартиру на сына, семья остановила сделку
- **slug:** `za-nedelyu-do-avansa-v-tyumeni-vspyla-darstvennaya-pensionerka-oformila-kvartiru-na-syna`
- **article_dir:** `memory/blog/articles/B34-za-nedelyu-do-avansa-v-tyumeni-vsplyla-darstvennaya-pensionerka-oformila-kvartir`
- **cluster_id:** `secondary_recent_donation_relative_chain_before_advance_tyumen`
- **wp_category_slugs:** `vtorichka-i-riski`, `proverka-pered-pokupkoj`

## Mechanism and angle

- **viral_mechanism:** almost lost перед авансом/деньгами — чистые документы и один собственник в ЕГРН создают ощущение безопасности, но риск раскрывается непосредственно перед внесением денег.
- **top_energy_mirror:** almost lost перед ключами/деньгами: paper clean → срыв перед деньгами на столе.
- **vtorichka_mechanism:** Семья покупает двушку на вторичке в Тюмени: ипотека одобрена, торг согласован, в ЕГРН один собственник, обременений нет. За 7 дней до планового аванса юрист запрашивает полную цепочку переходов прав и обнаруживает дарственную от пенсионерки матери продавцу-сыну, оформленную 4 месяца назад. Возникает риск оспаривания родственниками и вопросов к быстрой перепродаже. Аванс 420 тыс. рублей не внесён, сделку остановили до подписания договора купли-продажи.
- **why_vtorichka_not_newbuild:** вторичная квартира, дарственная между родственниками и аванс на вторичном рынке; отсутствуют ДДУ, эскроу и застройщик.
- **why_not_plot_copy_viral:** используется только механика и энергия «почти сорвалось перед деньгами». Сюжет — локальный казус с квартирой в Тюмени и недавней дарственной пенсионерки сыну, а не загородный дом и не копирование сюжета о мошенничестве с землёй.
- **klyshin_hook:** none

## Dzen trend radar

1. **Основной viral reference**
   - **source_url:** https://dzen.ru/a/Zw9N_lUREDllN79D
   - **title:** «Как легально „кидают“ при покупке загородного дома…»
   - **views:** 17158
   - **use:** mirror mechanics/energy only — almost lost перед авансом/деньгами.
   - **plot restriction:** не переносить сюжет загородного дома; материал B34 — квартира на вторичке в Тюмени.

2. **Альтернативный Wordstat spine**
   - **source_url:** https://dzen.ru/a/arnh-zgnvihPFEtB
   - **title:** «Пенсионеры стали переоформлять жильё на родственников…»
   - **views:** 2114
   - **use:** тематическая опора для линии переоформления жилья пенсионеркой на родственника.

## Dzen casus shape

- **dzen_casus_shape:** PASS
- **event:** семья выбрала квартиру на вторичке, банк одобрил ипотеку, в ЕГРН указан один собственник.
- **risk:** недавняя дарственная от пенсионерки сыну создаёт риск оспаривания родственниками и срыва сделки после внесения аванса.
- **time:** за 7 дней до внесения аванса на безопасный счёт.
- **finale:** аванс 420 тыс. рублей не внесли. Продавец торопил покупателей, уверяя, что «дарение между близкими — это нормально». Семья остановила сделку и ушла проверять другой объект с полной цепочкой переходов прав до аванса.

## Search and Wordstat

- **wordstat_preflight:** `mcp-kv wordstat_get_user_info OK`
- **final P0 phrase:** `оформление квартиры на родственника`
- **P0 local regions:** 55,11176
- **P0 local frequency:** 21
- **P0 RU compare regions:** 225
- **P0 RU compare frequency:** 2058
- **supporting buyer-demand phrase:** `купить квартиру в тюмени вторичка`
- **supporting phrase frequency:** 3413, regions 55,11176
- **additional phrase:** `дарение квартиры близкому родственнику`
- **additional phrase frequency:** 164, regions 55,11176
- **weak phrase:** `продажа квартиры после дарения`
- **weak phrase frequency:** 3, regions 55,11176
- **wordstat_rework:** локальный запрос о продаже после дарения слабый; основной P0 — «оформление квартиры на родственника» с локализацией в тексте и H1 на Тюмень, вторичку и аванс. Поддерживающая buyer-спина — «купить квартиру в тюмени вторичка».

## Reader engagement

- **comment_magnet_angle:** «Если квартиру недавно подарили родственнику, а продавец торопит с авансом — вы бы внесли деньги или сначала проверили всех наследников и дарителей?»
- **recommended practical takeaway:** до аванса запрашивать полную цепочку переходов прав, проверять основания недавнего перехода, участников дарения и возможные семейные или наследственные риски; не считать отсутствие обременений и одного собственника в ЕГРН достаточной проверкой.

## Duplication and compliance gates

- **anti_dupe_hard:** PASS
- **story_dup_check:** PASS — distinct from B33 utility/ЖКУ debt before advance; B09 EGRN encumbrance; B03 gift-to-daughter auction; B10 elderly phone relatives; and other frozen clusters.
- **h1_fingerprint_check:** PASS — distinct combination: 7 дней + аванс + дарственная пенсионерки сыну.
- **formula_spam_check:** PASS — previous live topics were newbuild escrow/DDU and B33 concerned utility debt; B34 is a distinct secondary-market donation-chain story.
- **newbuild exclusion:** PASS — do not use DDU, escrow, developer or newbuild framing.
- **dzen_casus_shape:** PASS

## Signal URLs

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- https://dzen.ru/a/Zw9N_lUREDllN79D
- https://dzen.ru/a/arnh-zgnvihPFEtB

## Gate stamp (machine-readable)

klyshin_hook: none | original: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: secondary_utility_electricity_debt_before_advance_tyumen (B33), escrow_not_opened_after_mortgage, egrn_line_blocks_advance
wordstat_rework: probe «продажа квартиры после дарения» 3 (55,11176) → «оформление квартиры на родственника» 21 (55,11176) / 2058 (225) → supporting «купить квартиру в тюмени вторичка» 3413 → final P0 «оформление квартиры на родственника» 21 Tyumen + RU compare 2058
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «оформление квартиры на родственника» 21 (55,11176) compare «оформление квартиры на родственника» 2058 (225) | buyer spine «купить квартиру в тюмени вторичка» 3413
story_dup_check: PASS | cluster_id: secondary_recent_donation_relative_chain_before_advance_tyumen
h1_fingerprint_check: PASS | fingerprint: 7d+avanс+darstvennaya+pensionerka+syn
formula_spam_check: PASS | last3_mechanisms: utility_debt_before_advance, escrow_ddu_newbuild_live, family_mortgage_escrow
anti_dupe_hard: PASS
