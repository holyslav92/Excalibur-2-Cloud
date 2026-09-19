# Scout inputs — 2026-09-19 (B28)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-19 (YEKT Saturday slot 12:00 — weekend automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO B27 today: land lease not ownership in declaration (cluster newbuild_land_lease_not_ownership_declaration_tyumen)
- NO family mortgage revoked at child 7 years (2026-09-19 live)
- NO cottage kadastr boundary 1.8m (2026-09-18 live)
- NO BTI ate 4.2 sqm DDU (2026-09-18 live)
- NO 28 days assignment lost to another buyer (2026-09-18 live)
- NO mortgage approval expired day 87 (2026-09-18 live)
- NO matkapital/opieka kids shares (2026-09-17 live)
- NO DDU appendix rental ban investor +240k (2026-09-17 live)
- NO different building 10 days before DDU (2026-09-17 live)
- NO bank appraisal -900k vs DDU (cluster bank_appraisal_below_ddu_price locked)
- NO parking not in declaration (2026-09-16 live)
- NO insurance 186k day before DDU/escrow (2026-09-16 live)
- NO frozen clusters in memory/scout/used-clusters.json (30d): escrow zero, booking expired price hike, trade-in, installment penalty, keys delay penalty, mortgage rate hike, developer entity change, cellar, acceptance defects, etc.
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-19)
- Live WP recent (~12): B27 land lease declaration, family mortgage child 7, cottage kadastr 1.8m, BTI -4.2 sqm, assignment 28d, ipoteka day 87, matkapital day 47, rental ban appendix, other corpus 10d, bank appraisal -900k, parking declaration, insurance 186k
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug (fingerprint booking_expired — distinct from booking_expired_price_hike price-hike plot and B27 land-lease plot)
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B28
- **title_draft:** Под Тюменью в брони обещали газ в 2026 — в декларации КП дата 2028, до ДДУ не дошли
- **slug:** v-tyumeni-v-broni-obeschali-gaz-v-2026-v-deklaracii-kp-data-2028-do-ddu-ne-doshli
- **article_dir:** memory/blog/articles/B28-v-tyumeni-v-broni-obeschali-gaz-v-2026-v-deklaracii-kp-data-2028-do-ddu-ne-doshli
- **cluster_id (new):** newbuild_kp_gas_declaration_date_mismatch_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья покупает готовый дом в коттеджном посёлке под Тюменью по ДДУ. В брони и презентации менеджер зафиксировал «газ подключён / подключение в 2026». Перед подписанием ДДУ открыли проектную декларацию на dom.rf — в графе инженерных сетей **срок ввода газопровода в эксплуатацию: IV квартал 2028**, не 2026. Семья с детьми (отопление, котёл, бюджет) отказалась от ДДУ, бронь 200 тысяч вернули частично, на эскроу не вышли
- **why_newbuild_not_secondary:** Сюжет только в цепочке покупки дома от застройщика в КП: бронь, проектная декларация 214-ФЗ, ДДУ на дом, сроки коммуникаций застройщика. Нет продавца вторички, ЕГРН-квартиры, наследников, бабушки, опеки или соседской доли
- **story_dup_check:** PASS — distinct from B27 land lease (different mechanism: gas infrastructure date vs land tenure), cottage kadastr boundary 1.8m (acceptance/plot boundary, not utilities), B25 chistovaya on acceptance (finishing, not gas), booking_expired_price_hike (section/price, not utilities timeline)

## Dzen news-casus shape (target PASS)

- **event:** семья с двумя детьми выбрала готовый дом в коттеджном посёлке под Тюменью; менеджер показал участок с табличкой «газ» и в брони написал «коммуникации — газ, подключение 2026»
- **risk:** без газа дом зимой неэксплуатируем или потребует дорогой альтернативы (электрокотёл/газгольдер); банк при ипотеке на ИЖС/дом может отказать или урезать сумму, если в декларации срок сетей сдвинут на 2+ года
- **time:** за 6 дней до назначенного подписания ДДУ; вечером перед визитом в банк сверили декларацию на dom.rf
- **finale:** в декларации — ввод газопровода IV кв. 2028; застройщик предложил «подпишите ДДУ, газ дотащим раньше по внутреннему графику»; семья отказалась; бронь 200 тыс. вернули 140 тыс. (удержали 60 за «бронирование лота»), ДДУ не подписали, эскроу не открывали
- **comment_magnet_angle:** «Если в брони газ в 2026, а в декларации КП — 2028, вы бы подписали ДДУ, чтобы не потерять бронь, или ушли бы сразу?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP gas-declaration casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-19)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| коттеджные поселки тюмень | 55,11176 | 1455 |
| коттеджные поселки | 225 (compare) | 274847 |
| дома в коттеджных поселках тюмени | 55,11176 | 55 |
| тюмень купить дом в коттеджном поселке | 55,11176 | 23 |
| газ коттеджный посёлок | 55,11176 | 3 |
| подключение газа коттеджный посёлок | 55,11176 | API empty (treat as <5) |
| новостройки тюмень | 55,11176 | 4430 (context spine) |
| новостройки тюмени от застройщика с отделкой | 55,11176 | 23 (not used — B25/B27 overlap risk) |

**wordstat_rework log:**
- probe «газ коттеджный посёлок» 55,11176 → 3 (too weak for P0 alone)
- probe «подключение газа коттеджный посёлок» 55,11176 → empty/<5 (too weak)
- probe «высота потолков новостройка» 55,11176 → 3 (alternate angle rejected — weak + apartment not KP)
- **rework:** anchor buyer spine «коттеджные поселки тюмень» (KP/house demand) + gas-date mechanism in H1/body
- **final P0 «коттеджные поселки тюмень» regions 55,11176,compare225 freq 1455 (55+11176) / RU context «коттеджные поселки» 274847 (225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации (сроки инженерных сетей, газ)
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, проектная декларация
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B28, title, slug, article_dir, signal_urls, research angles for Research role.
