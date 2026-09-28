# Scout inputs — 2026-09-28 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-28 (YEKT slot 09:00 weekday)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO B32 wrong escrow beneficiary / wrong legal entity in requisites (cluster escrow_wrong_beneficiary)
- NO partial commissioning / bank revoked mortgage (LIVE-NOVOSTROJKA-TYUMEN-CHAST)
- NO UK 180k before keys, lift tech inspection, parking benefit, rental ban appendix, studio commercial, townhouse-as-apartment, installment +340k, discount 380k, area 54→49, acceptance -1.8m², flooding neighbor without distinct mechanism
- NO frozen secondary clusters in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 17 active locks (2026-09-28)
- Live WP recent (~20): investor studio commercial DDU; townhouse vs apartment; installment 340k; UK 180k; lift tech; rental ban; parking; KP house reservation lost; cold balcony; discount 380k; planning area drop; acceptance area; KP kadastr 12→8; partial commissioning; separate parking DDU; assignment 150k; last floor mortgage; matkapital SFR; kindergarten on render; family mortgage child 7
- `scout_helper.py --check-query` PASS for proposed title (cluster newbuild_eiszhs_construction_suspended_before_escrow_tyumen; fingerprint escrow_blocked distinct from B32 wrong beneficiary)
- `excalibur_blog_topic_focus.py` PASS (эскроу / новостройка)
- `scout_helper.py --check-slug` PASS

## Proposed topic (PASS topic_focus + scout_helper)

- **topic_id:** B33
- **title_draft:** За 2 дня до эскроу в ЕИСЖС у ЖК статус «строительство приостановлено» — семья не открыла счёт
- **slug:** za-2-dnya-do-eskrou-eisjs-stroitelstvo-priostanovleno-tyumen
- **article_dir:** memory/blog/articles/B33-za-2-dnya-do-eskrou-eisjs-stroitelstvo-priostanovleno-tyumen
- **cluster_id (new):** newbuild_eiszhs_construction_suspended_before_escrow_tyumen
- **top_energy_mirror:** paper_clean_then_broke / stopped_before_money
- **newbuild_mechanism:** Семья с одобренной ипотекой на квартиру в строящемся ЖК Тюмени. В брони и на презентации — «сдача в срок», объект в ЕИСЖС в статусе «строится». За **2 дня** до назначенного открытия эскроу-счёта ипотечный менеджер просит «финальную сверку» — семья сама заходит в **ЕИСЖС (наш.дом.рф)** и видит у **своего корпуса** статус **«строительство приостановлено»** (или эквивалентная отметка о приостановке) с датой, которой **не было** на встрече в офисе неделей ранее. Банк-эскроу-агент **не подтверждает** открытие счёта / блокирует перевод до прояснения причины приостановки и соответствия проектной декларации. Офис продаж давит сроком брони. Семья **не открывает эскроу и не переводит деньги**; бронь под угрозой, но аванс на эскроу не ушёл.
- **why_newbuild_not_secondary:** Только цепочка ДДУ + ипотека + эскроу + ЕИСЖС по строящемуся объекту. Нет продавца вторички, ЕГРН-квартиры, наследников, опеки.
- **story_dup_check:** PASS — distinct from B32 (wrong beneficiary requisites), B26 (no commissioning permit), partial commissioning plot (другой статус в декларации), keys/UK/lift clusters

## Dzen news-casus shape (target PASS)

- **event:** семья с детьми выбрала квартиру в строящемся ЖК Тюмени; бронь; ипотека одобрена; назначено открытие эскроу
- **risk:** приостановка строительства в ЕИСЖС = сдвиг сроков, риск для банка и для маткапитала/семейной ипотеки; перевод на эскроу при «красном» статусе может сорвать одобрение
- **time:** за 48 часов до открытия эскроу; вечером перед визитом в банк
- **finale:** статус «приостановлено» в реестре; застройщик ссылается на «техническую паузу»; банк не открывает счёт; семья откладывает подписание ДДУ, деньги на эскроу не переводит, бронь спорная но без потери эскроу-аванса
- **comment_magnet_angle:** «Если бы в ЕИСЖС перед эскроу увидели “строительство приостановлено”, вы бы всё равно открыли счёт ради срока брони или остановились до письменного объяснения?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen EISJS-status casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-28)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4350 |
| купить новостройку в тюмени | 55,11176 | 891 |
| долгострой тюмень | 55,11176 | 42 |
| эскроу счет новостройка | 55,11176 | weak (<10 typical) |

**wordstat_rework log:**
- probe «эскроу счет новостройка» Tyumen weak alone
- rework: spine «новостройки тюмень» 4350 + mechanism «ЕИСЖС / приостановка строительства / эскроу»
- **final P0 «новостройки тюмень» regions 55,11176 freq 4350**

## Gates stamped

- dzen_casus_shape: PASS
- comment_magnet_angle: (see above)
- anti_dupe_hard: PASS
- newbuild_mechanism: (see above)
- top_energy_mirror: paper_clean_then_broke
- why_newbuild_not_secondary: (see above)
- final P0 phrase+volume: новостройки тюмень — 4350 (55+11176)

## signal_urls (for Research)

- {{SITE_BASE}}/blog/ (recent titles context only)
- https://наш.дом.рф/ (ЕИСЖС public registry — mechanism)
- Scout optional: fresh 72.ru / tymen news week of 2026-09-22+ on newbuild market Tyumen

Write full `.cursor/excalibur-blog-handoff.md` per scout skill format with all fields above for Director.
