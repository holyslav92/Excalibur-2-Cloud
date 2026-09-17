# Scout inputs — 2026-09-17 (B27, slot ~12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-17 (YEKT Thursday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO corp/building swap before DDU (published today LIVE)
- NO bank appraisal below DDU / escrow amount mismatch (published today)
- NO parking spot in declaration (published 2026-09-16)
- NO insurance surprise before DDU (published 2026-09-16)
- NO keys delay / penalty unpaid (cluster keys_delay_penalty locked)
- NO acceptance finishing mismatch (B25 cluster acceptance_defects_penalty)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks
- Live WP recent (~12): corp swap, bank appraisal -900k, parking declaration, insurance 186k, keys +9mo penalty, co-borrower refused, booking section mismatch, assignment 350k, KP no gas, accreditation removed, price hike, parents acceptance lift
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени в приложении к ДДУ нашли запрет сдавать квартиру — инвестор остановил эскроу
- **slug:** v-tyumeni-v-prilozhenii-k-ddu-nashli-zapret-sdavat-investor-ostanovil-eskrou
- **cluster_id (new):** newbuild_ddu_rental_ban_investor_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Инвестор покупает квартиру в новостройке под сдачу; в брошюре и прайсе — «свободное использование», но в **приложении №3 к ДДУ** (правила дома / ограничения) мелким шрифтом — **запрет сдавать жильё в аренду** до регистрации дома и без согласия УК. Без аренды экономика сделки не сходится → инвестор **останавливает открытие эскроу** за 2 дня до подписания
- **why_newbuild_not_secondary:** сюжет только в цепочке ДДУ новостройки + приложения к договору долевого участия + эскроу до регистрации; нет продавца вторички, ЕГРН, наследников, бабушки, банкротства продавца
- **story_dup_check:** PASS — distinct from booking_expired, trade_in, subsidy removed, appraisal below DDU, assignment (переуступка), parents acceptance

## Dzen news-casus shape (target PASS)

- **event:** инвестор из Тюмени выбрал студию в сдающемся ЖК под аренду, бронь и ипотека одобрены
- **risk:** пункт приложения к ДДУ запрещает сдачу; нарушение = штраф + расторжение; доходность падает ниже платежа по ипотеке
- **time:** за 2 дня до визита в банк на открытие эскроу юрист нашёл запрет в приложении на стр. 14
- **finale:** инвестор не подписал ДДУ, бронь сгорела, застройщик предложил «другую квартиру без ограничений» — но с доплатой 240 тыс.; инвестор отказался, эскроу не открыли, аванс не вносили
- **comment_magnet_angle:** «Вам менеджер говорил „можно сдавать“, а в приложении к ДДУ — запрет: вы бы доплатили за „чистый“ лот или ушли бы к другому застройщику, даже если бронь сгорит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild investor rental-ban casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-17)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| сдать квартиру в новостройке | 55,11176 | 7 (weak) |
| квартиры в сданных новостройках | 55,11176 | 7 (weak) |
| **купить новостройку в тюмени** | **55,11176** | **928** |
| купить новостройку в тюмени от застройщика | 55,11176 | 465 |
| новостройки тюмень | 55,11176 | 4480 (context) |
| **купить новостройку в тюмени** | **225 (compare)** | probe via «новостройки тюмень» RU context |

**wordstat_rework log:**
- probe «сдать квартиру в новостройке» 55,11176 → 7 (weak investor tail)
- rework: buyer jargon **купить новостройку в тюмени** + инвесторский casus (аренда в приложении ДДУ) → **final P0 «купить новостройку в тюмени» regions 55,11176 freq 928**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, права дольщиков
- https://www.domrf.ru/ — проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Handoff footer (include verbatim in output)

wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: «запрет сдачи в приложении к ДДУ новостройки — инвестор остановил эскроу»
why_newbuild_not_secondary: «сюжет в ДДУ/приложении/эскроу новостройки, не вторичка»
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: bank_appraisal, keys_delay, acceptance_defects, booking_expired, …
dzen_casus_shape: PASS
comment_magnet_angle: «менеджер обещал сдачу, в приложении запрет — доплатите или уйдёте?»
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 928
story_dup_check: PASS | cluster_id: newbuild_ddu_rental_ban_investor_tyumen
h1_fingerprint_check: PASS | fingerprint: escrow_blocked
formula_spam_check: PASS
anti_dupe_hard: PASS
