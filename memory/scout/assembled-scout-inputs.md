# Scout inputs — 2026-09-18 (B27, slot 17:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-18 (YEKT Friday slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO repeat of today's 2026-09-18 publications: BTI -4.2 sqm DDU; assignment 28 days lost; mortgage approval expired day 87; matkapital child shares; DDU rental ban appendix; other corpus 10 days before DDU; bank appraisal -900k; parking spot in declaration; insurance 186k before escrow; keys +9 months penalty unpaid; co-borrower refused
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots
- NO B25 finishing-at-acceptance retitle (acceptance_defects_penalty cluster locked)
- NO BTI area mismatch retitle (today's LIVE BTI -4.2 sqm is apartment sqm, not land boundary)

## Angle selection (two owner proposals — PICK KP boundary)

**Rejected:** застройщик потребовал доплату за «улучшенный пакет отделки» за 48 часов до ДДУ — overlaps B25 отделка cluster + weak Wordstat (отделка новостройки тюмень 32) + formula spam risk (last 3 = DDU appendix vs fact in apartments)

**SELECTED:** дом в КП — граница участка не совпала с кадастром на ключах — unique newbuild house/KP plot, top_energy paper_clean_then_broke, strong Wordstat spine

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-18)
- Live WP recent (~12): BTI -4.2 sqm; assignment 28d; mortgage day 87; matkapital shares; rental ban DDU; other corpus; appraisal -900k; parking declaration; insurance 186k; keys +9mo; co-borrower; booking section mismatch 48h
- `scout_helper.py --check-query` — run after title lock
- `excalibur_blog_topic_focus.py` — run after title lock

## Proposed topic (PASS topic_focus + scout_helper + story_dup expected PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени на ключах дом в коттеджном посёлке — граница участка съехала на 1,8 метра, акт не подписали
- **slug:** v-tyumeni-na-klyuchah-dom-v-kp-granica-uchastka-ne-sovpala-s-kadastrom
- **cluster_id (new):** newbuild_kp_plot_boundary_cadastre_mismatch_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья купила дом в коттеджном посёлке под Тюменью по ДДУ с земельным участком; на приёмке/ключах вызвали кадастрового инженера — **забор и межа сдвинуты** относительно **кадастрового плана** (съезд ~1,8 м), площадь в ЕГРН меньше, чем в презентации застройщика; акт приёма не подписали, регистрацию права остановили
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ с застройщиком КП → сдача дома → приёмка участка → регистрация; нет продавца вторички, наследников, бабушки или «чистой ЕГРН» вторичного рынка
- **story_dup_check:** PASS — distinct from BTI sqm mismatch (apartment interior), acceptance_defects_penalty/B25 (finishing), parking declaration, corpus swap, all frozen secondary

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени подписала ДДУ на дом в коттеджном посёлке; застройщик пригласил на ключи через 14 месяцев
- **risk:** граница участка в натуре не совпадает с кадастром → меньше площадь, соседний забор «съедает» метры, банк может не принять залог по ипотеке на землю
- **time:** на приёмке, за 2 часа до подписания акта; инженер на месте показал расхождение 1,8 м по одной стороне
- **finale:** акт не подписали; застройщик предложил «межевание за свой счёт через полгода»; семья отказалась от ключей, направила претензию, банк приостановил выдачу последнего транша ипотеки до урегулирования границ
- **comment_magnet_angle:** «На ключах забор стоит не по кадастру, а застройщик обещает „поправить межу“ через полгода: вы бы взяли дом сейчас или вернули бы ключи, даже если ипотека уже платится?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP boundary casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-18)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| улучшенная отделка дду | 55,11176 | empty/weak (rejected angle) |
| отделка новостройки тюмень | 55,11176 | 32 (weak; B25 cluster overlap) |
| коттеджный поселок тюмень участок | 55,11176 | 34 (weak tail) |
| границы земельного участка | 55,11176 | 927 (strong but generic) |
| кадастровые границы земельных участков | 55,11176 | 116 |
| дома в тюмени от застройщика | 55,11176 | 255 |
| **коттеджные поселки тюмень** | **55,11176** | **1479** |
| **коттеджные поселки тюмень** | **225 (compare)** | **2418** |
| новостройки тюмень | 55 | 3640 (context spine) |

**wordstat_rework log:**
- probe «улучшенная отделка дду» 55,11176 → empty (rejected finish-upsell angle — B25 + formula spam)
- probe «отделка новостройки тюмень» → 32 weak
- probe «коттеджный поселок тюмень участок» → 34 weak tail
- probe «границы земельного участка» → 927 strong but not buyer-local KP spine
- **rework:** buyer jargon КП + дом от застройщика Тюмень → **final P0 «коттеджные поселки тюмень» regions 55,11176,compare225 freq 1479 (55+11176) / 2418 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, земельный участок дольщика
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации КП
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
