# Scout inputs — 2026-09-15 (B27, YEKT 12:00 slot)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-15 (YEKT weekday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{SITE_BASE}})
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO today clusters (2026-09-15): bank accreditation revoked, price hike +480k before DDU, acceptance for parents, price fixation/indexation failed
- NO yesterday clusters: matkapital 7yr before escrow, 3-room→2-room DDU swap, double booking same unit, 54→52 sqm area mismatch
- NO keys_delay_penalty_unpaid (H1 fingerprint dup LIVE-V-TYUMENI-ZASTROJSCHIK-P)
- NO bank_appraisal_below_ddu (fingerprint dup LIVE-TRANSHEVAYA)
- NO KP plot area only (B26-adjacent live: 12 vs 9.7 sotok) — this slot = **utilities/gas**, not cadastral area
- NO frozen secondary clusters in used-clusters.json (30d)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-15)
- Live WP today (4): аккредитация банка снята; прайс +480k; приёмка для родителей; фиксация цены сорвалась
- Live WP yesterday: маткапитал 7 лет; трёшка→двушка; две брони; 54→52 метра
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS
- `story_dup` anti-dupe HARD PASS

## Proposed topic (PASS all gates)

- **topic_id:** B27
- **title_draft:** В КП Тюмени вручили ключи от дома — газа на участке не оказалось, акт не подписали
- **slug:** v-tyumeni-v-kp-vydali-klyuchi-uchastok-bez-gaza
- **cluster_id (new):** newbuild_kp_utilities_not_ready_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Коттеджный посёлок / дом от застройщика — торжественная выдача ключей, в договоре и презентации «коммуникации по графику», но **газопровод к участку не подведён**, техусловия Газпрома отсутствуют, электрическая мощность ниже заявленной в договоре → семья **не подписала акт приёма**, ключи формально вручили, проживание невозможно
- **why_newbuild_not_secondary:** сюжет = покупка **дома в КП от застройщика** (договор долевого участия / договор с застройщиком КП), не вторичка, не бабушка/ЕГРН/банкрот продавца; риск в обещанных **инженерных сетях до ввода**, не в сделке с физлицом

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила дом в коттеджном посёлке по договору с застройщиком, дождалась «сдачи», приехала на вручение ключей
- **risk:** без газа и достаточной электромощности дом непригоден для зимнего проживания; подписанный акт ослабляет претензии по коммуникациям
- **time:** за 3 дня до вручения застройщик прислал акт «сети будут в течение квартала»; на участке — только котлован под ввод, шурф пустой
- **finale:** акт не подписали, ключи взяли «на хранение» под расписку; застройщик предложил подписать с оговоркой — отказ; семья осталась в съёме, платит ипотеку; претензия с фото и ссылкой на пункт договора о сроках газификации
- **comment_magnet_angle:** «Ключи в руках, газа нет: вы бы подписали акт с формулировкой „сети подключат позже“, если застройщик давит „все уже приняли“?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP utilities casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-15)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| подключение газа участок тюмень | 55,11176 | 0 (empty API) |
| дом в коттеджном поселке тюмень | 55,11176 | 66 |
| коттеджный поселок тюмень | 55,11176 | 1519 |
| **коттеджные поселки тюмень** | **55,11176** | **1519** |
| коттеджный поселок купить | 225 (compare) | 16557 |
| новостройки тюмень | 55,11176 | 4475 (context spine) |

**wordstat_rework log:**
- probe «подключение газа участок тюмень» 55,11176 → 0 (weak/empty) → rework to KP buyer jargon
- probe «дом в коттеджном поселке тюмень» → 66 (local tail)
- probe «коттеджный поселок тюмень» → 1519
- **final P0 «коттеджные поселки тюмень» regions 55,11176,compare225 freq 1519 (55+11176) / 16557 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, передача объекта
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Required handoff fields (emit ALL)

Emit standard Scout handoff with: topic_id, title_draft, slug, cluster_id, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat, story_dup_check, h1_fingerprint_check, formula_spam_check, anti_dupe_hard, signal_urls.

**formula_spam_check context:** last 3 published today = bank accreditation / price indexation / acceptance defects — KP utilities = distinct mechanism (коммуникации КП, not DDU price/bank/приёмка дефекты).
