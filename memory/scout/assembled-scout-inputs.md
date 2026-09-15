# Scout inputs — 2026-09-15 (B27, slot 17 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-15 (YEKT weekday slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — already published 2026-09-15)

- NO assignment + advance hang (переуступка 350k)
- NO KP without gas on keys
- NO bank de-accreditation ЖК before DDU
- NO price list hike before DDU (прайс ЖК)
- NO acceptance for parents / elevator defects
- NO price fixation failure before DDU
- NO matkapital child 7 years before escrow
- NO treшka→dvushka swap in DDU before escrow
- NO double booking same apartment (two bрони)
- NO DDU area -2 sqm on acceptance
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-15)
- Live WP recent (~12): assignment advance 350k, KP no gas, accreditation removed, price hike, parents acceptance, price fixation, matkapital 7y, treшka→dvushka, double booking, area -2 sqm, cottage 12 vs 9.7 sotok, RVE no tranche
- **Rejected backup:** ddu_hidden_mandatory_club_fee_tyumen — valid but floor/section mismatch stronger paper_clean_then_broke mirror vs today's DDU-object swaps
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: брони, эскроу, ДДУ, сделку)
- `story_dup.py --text` PASS — fingerprint booking_expired mechanism distinct from area/layout swaps

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени в брони закрепили этаж с видом — за 2 дня до эскроу в ДДУ оказалась другая секция, сделку остановили
- **slug:** v-tyumeni-v-broni-etazh-s-vidom-v-ddu-drugaya-sektsiya-sdelku-ostanovili
- **cluster_id (new):** ddu_booking_floor_section_mismatch_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** в платной брони и в переписке с менеджером зафиксированы **этаж, вид из окна и секция** (лист бронирования / приложение); за **2 дня до открытия эскроу** прислали проект ДДУ — в приложении **другая секция корпуса, этаж на два ниже, окна во двор вместо набережной**; семья отказалась подписывать, бронь сняли, деньги на эскроу не ушли
- **why_newbuild_not_secondary:** цепочка бронь → ДДУ → эскроу → застройщик/ЖК; нет продавца вторички, ЕГРН, наследников, бабушки или маткапитала на вторичке
- **story_dup_check:** PASS — distinct from ddu_area_mismatch (-2 кв.м на приёмке), ddu_layout_swap (трёшка→двушка), double_booking_same_unit, price_fixation_fail, booking_expired_price_hike (subsidy removed)

## Dzen news-casus shape (target PASS)

- **event:** семья с ребёнком в Тюмени забронировала квартиру в новостройке на набережной — этаж и вид согласовали письменно в брони
- **risk:** в ДДУ другой объект (секция/этаж/вид) → ипотека и эскроу открываются уже на «не тот» лот; после подписания сменить сложно
- **time:** за **48 часов** до даты подписания ДДУ и открытия счёта эскроу
- **finale:** родители сравнили лист брони с приложением к ДДУ, отказались подписывать; застройщик предложил «аналогичную» квартиру без того вида — семья остановила сделку, бронь закрыли, на эскроу **0**, ипотечное одобрение не тратили
- **comment_magnet_angle:** «В брони этаж и вид записаны, а в ДДУ — другая секция: вы бы подписали „с поправкой потом“ или сняли бы бронь, даже если квартира „ещё есть“?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild booking-vs-DDU floor/section casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-15)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| дду новостройка тюмень | 55,11176 | MCP empty (rework) |
| дду тюмень | 55 | 12 (weak) |
| бронь квартира новостройка | 55 | totalCount 1 (weak) |
| договор дду тюмень | 55 | totalCount 1 (weak) |
| новостройки тюмень от застройщика | 55,11176 | 864 |
| купить новостройку в тюмени | 55 | 683 |
| приемка квартиры в новостройке тюмень | 55 | 24–36 (topic tail, weak P0) |
| **новостройки тюмень** | **55** | **3536** |
| **новостройки тюмень** | **225 (compare)** | **8388** |

**wordstat_rework log:**
- probe «дду новостройка тюмень» 55,11176 → empty/error (weak local DDU tail)
- probe «дду тюмень» 55 → 12 (weak)
- probe «бронь квартира новостройка» 55 → 1 (weak)
- probe «приемка квартиры в новостройке тюmenь» 55 → 24–36 (plot-adjacent but weak; acceptance cluster taken today)
- **rework:** newbuild buyer spine — бронь/ДДУ/эскроу + локализация Тюмень → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 3536 (55) / 8388 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, предмет ДДУ, характеристики объекта в приложении
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
