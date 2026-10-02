# Scout inputs — B34 slot 17:00 YEKT 2026-10-02

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no refusals.

**SLOT RUBRIC OVERRIDE (mandatory):** This run is slot **17:00 YEKT = `vtorichka` ONLY** per `shared/slot-rubric-lock.md` and pipeline `rubric_per_slot`. The legacy «newbuild-only» paragraphs in the scout skill are **inactive** for this invocation. **Do NOT BLOCK** a vtorichka topic. **needs_scout: false** on PASS.

Output the complete handoff text now.

**run_date:** 2026-10-02  
**slot:** 17:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka (вторичка Тюмень ONLY — NOT novostroyki)  
**tenant:** The Риэлтор — Святослав Шакин  
**topic_market_focus:** rubric_per_slot  
**dzen_rf_pack:** true (dzen-content-rules + rf-blocked-entities read by conductor)

## Trend Radar (slot vtorichka)

`memory/blog/trend-radar/trend-radar.json` (2026-10-02T12:21Z, slot 17:00):
- **viral_mechanism:** almost lost перед ключами/деньгами (Klyshin channel energy — mechanics only, do NOT copy «7 грехов» plot)
- **energy mirror:** думали, что объект «свободен», пока не увидели чужое объявление перед авансом

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 14 active locks
- **Avoid today / 30d secondary clusters:** competing buyer+avans (WP 2026-10-02), family mortgage recalc before avans, seller bankruptcy, bailiff ban, registered lease 3y in EGRN, gift deed pensioner, B33 utility electricity debt 186k, B09 egrn encumbrance, frozen secondary list in used-clusters.json
- Last-3 WP secondary mechanisms ≠ «активная сдача на площадке» (distinct from EGRN 3y lease casus)
- `scout_helper.py --check-query` **PASS** 2026-10-02 (clean unique)
- `excalibur_blog_topic_focus.py` PASS (slot rubric vtorichka, EXCALIBUR_BLOG_SLOT=17:00)
- `story_dup.py` — new cluster `secondary_active_rent_listing_discovered_before_advance`

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** В Тюмени на вторичке за 2 дня до аванса нашли квартиру в аренде на Авито — покупатель ушёл
- **slug:** za-2-dnya-do-avansa-na-vtorichke-nashli-kvartiru-v-arende-na-avito-pokupatel-ushel
- **article_dir:** memory/blog/articles/B34-za-2-dnya-do-avansa-na-vtorichke-nashli-kvartiru-v-arende-na-avito-pokupatel-ushel
- **cluster_id (new):** secondary_active_rent_listing_discovered_before_advance
- **slot_rubric:** vtorichka
- **viral_mechanism:** almost lost перед авансом — «продавали честно», пока не нашли параллельное «сдам» с тем же адресом/фото
- **vtorichka_mechanism:** Семья с ипотекой на вторичке в Тюмени согласовала цену, осмотр прошёл, выписка ЕГРН без долгосрочной аренды. За **2 дня** до внесения аванса покупатель (или риэлтор) по совету знакомых пробил объект на Авито — **активное объявление «сдам»** с теми же комнатами/планировкой и свежими фото. Продавец: «это старое, сниму завтра». Арендатор на связи подтвердил, что живёт по договору ещё 8 месяцев. Семья **не внесла аванс**, сделку остановили до договора купли-продажи
- **why_vtorichka_not_newbuild:** вторичка, физлицо-продавец, аванс, проверка перед сделкой — без ДДУ/эскроу/застройщика (отличие от LIVE «сдам» в новостройке перед эскроу)
- **story_dup_check:** PASS — not registered_lease_3y_egrn, not competing_buyer_avans, not bankruptcy/bailiff/gift deed
- **h1_fingerprint_check:** PASS — «2 дня + аванс + Авито аренда» distinct fingerprint
- **formula_spam_check:** PASS — last3 secondary: competing buyer, family mortgage recalc, seller bankruptcy — new mechanism = parallel rent listing discovery

## Dzen news-casus shape: PASS

- **event:** покупатели выбрали вторичку, банк одобрил ипотеку, аванс назначен на конкретную дату
- **risk:** квартиру одновременно сдают; выселение/расторжение не гарантировано до аванса
- **time:** за 2 дня до планового аванса
- **finale:** аванс не внесли; продавец обещал «снять объявление» — покупатель ушёл проверять другой объект с проверкой площадок **до** аванса
- **comment_magnet_angle:** «Если за два дня до аванса находите «сдам» на ту же квартиру, а продавец клянётся, что объявление старое — вы бы всё равно внесли аванс?»

## Klyshin hook

- **klyshin_hook:** none (trend-radar energy only; no plot copy)

## Wordstat MCP-KV (live 2026-10-02)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| probe | regions | freq |
|-------|---------|-----:|
| аванс при покупке квартиры | 55,11176 | 13 |
| тюмень ипотека вторичное жилье | 55,11176 | 131 |
| купить квартиру в тюмени вторичка | 55,11176 | 3348 |
| купить квартиру в тюмени вторичка | 225 (compare) | 6220 |
| проверка квартиры перед покупкой | 55,11176 | 4 |

**wordstat_rework:** «проверка квартиры перед покупкой» 4 → weak; «аванс при покупке квартиры» 13 → narrow; spine buyer P0 **«купить квартиру в тюмени вторичка»** 3348 (55+11176) with ипотека angle in body  
**final P0 / primary_query:** «купить квартиру в тюмени вторичка» regions 55,11176 freq **3348** (compare RU 225: **6220**)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- Trend energy (mechanics only): https://dzen.ru/a/XLmtcugWMwCyk9aL

Output full handoff per SKILL with all required fields including: `slot_rubric=vtorichka`, `anti_dupe_hard: PASS`, `dzen_casus_shape: PASS`, `needs_scout: false`, suggested `wp_category_slugs`: vtorichka-i-riski, proverka-pered-pokupkoj.
