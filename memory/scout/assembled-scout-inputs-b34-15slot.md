# Scout inputs — B34 slot 15:00 YEKT 2026-09-29

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). System file = `memory/scout/scout-system-rubric-per-slot.md` (rubric_per_slot tenant — vtorichka slot 15:00 is **mandatory**, not a violation). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, **no SCOUT BLOCK**, no refusals. Emit PASS handoff. Output the complete handoff text now.

**run_date:** 2026-09-29  
**slot:** 15:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka (вторичка Тюмень) — OWNER OVERRIDE slot 15:00, NOT newbuild  
**tenant:** The Риэлтор — Святослав Шакин, tymenrieltor.ru  
**topic_market_focus:** rubric_per_slot  
**dzen_rf_pack:** true

## Trend Radar (slot vtorichka)

`memory/blog/trend-radar/trend-radar.json` (2026-09-29 15:00):
- **top_energy_mirror:** almost lost перед ключами/деньгами (paper clean → срыв перед деньгами на столе)
- **viral_mechanism (mirror only, NOT plot copy):** almost lost перед авансом/деньгами
- **trend_radar source_url:** https://dzen.ru/a/Zw9N_lUREDllN79D — «Как легально «кидают» при покупке загородного дома…» — **17158** views (mechanism energy only; B34 plot = Tyumen **квартира** вторичка, не загородный дом)
- **strong alternate (Wordstat spine):** https://dzen.ru/a/arnh-zgnvihPFEtB — «Пенсионеры стали переоформлять жильё на родственников…» — **2114** views (viral.sqlite `memory/blog/trend-radar/data/20260929T101800Z/viral.sqlite`)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK (2026-09-29)
- **DO NOT duplicate today live WP:** escrou/DDU newbuild (posts 11235, 11222) — B34 strictly secondary
- **Closed cluster B33:** `secondary_utility_electricity_debt_before_advance_tyumen` — utility/JKU debt before advance — **не повторять**
- Avoid frozen: egrn_line (B09), seller bankruptcy, matkapital/opieka, registered persons (B17), forged consent, grandma POA viewing, gift-to-daughter auction (B03), elderly phone relatives (B10)
- `scout_helper.py --check-query` PASS 2026-09-29
- `excalibur_blog_topic_focus.py` PASS (slot rubric vtorichka, EXCALIBUR_BLOG_SLOT=15:00)
- `story_dup.py` — distinct cluster `secondary_recent_donation_relative_chain_before_advance_tyumen`

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** За неделю до аванса в Тюмени всплыла дарственная — пенсионерка оформила квартиру на сына, семья остановила сделку
- **slug:** za-nedelyu-do-avansa-v-tyumeni-vspyla-darstvennaya-pensionerka-oformila-kvartiru-na-syna
- **article_dir:** memory/blog/articles/B34-za-nedelyu-do-avansa-v-tyumeni-vspyla-darstvennaya-pensionerka-oformila-kvartiru-na-syna
- **cluster_id (new):** secondary_recent_donation_relative_chain_before_advance_tyumen
- **slot_rubric:** vtorichka
- **viral_mechanism:** almost lost перед авансом — «один собственник в ЕГРН», пока не раскрыли цепочку дарения от пенсионерки родственнику и риск оспаривания/соседних наследников
- **vtorichka_mechanism:** Семья покупает двушку на вторичке в Тюмени (ипотека одобрена, торг согласован). Продавец — сын ~40 лет, в выписке один собственник, обременений нет. На осмотре мать продавца (пенсионерка) «просто живёт рядом». За **7 дней** до планового аванса юрист запросил полную цепочку переходов прав — **дарственная от матери сыну 4 месяца назад** (пенсионерка оформила квартиру на родственника, как в тренде Дзена). Всплывает риск: сестра продавца не участвовала в сделке дарения, заявление об оспаривании / сроки оспаривания сделки, налоговый след при быстрой перепродаже. Покупатели **не внесли аванс 420 тыс.**, сделку остановили до договора купли-продажи
- **why_vtorichka_not_newbuild:** вторичная квартира, дарственная между родственниками, аванс на вторичке — без ДДУ, эскроу, застройщика
- **why_not_plot_copy_viral:** не загородный дом, не схема «кидают» с землёй — только **energy** almost-lost + локальный Tyumen casus дарения пенсионерки перед продажей
- **story_dup_check:** PASS — not B33 utility debt, not B09 egrn обременение, not B03 gift daughter auction, not inheritance son first marriage
- **h1_fingerprint_check:** PASS — «7 дней + аванс + дарственная пенсионерка сын» distinct
- **formula_spam_check:** PASS — last published newbuild today escrou slots; B33 was utility; this is donation-chain secondary

## Dzen news-casus shape: PASS

- **event:** семья выбрала вторичку, банк одобрил ипотеку, продавец один в ЕГРН
- **risk:** недавняя дарственная от пенсионерки → оспаривание родственниками / срыв после аванса
- **time:** за 7 дней до внесения аванса на безопасный счёт
- **finale:** аванс не внесли; продавец торопил «дарение между близкими — это нормально» — покупатели ушли проверять другой объект с **полной цепочкой** прав до аванса
- **comment_magnet_angle:** «Если квартиру недавно подарили родственнику, а продавец торопит с авансом — вы бы внесли деньги или сначала проверили всех наследников и дарителей?»

## Klyshin hook

- **klyshin_hook:** none (original Tyumen secondary casus; viral Dzen only for energy)

## Wordstat MCP-KV (live 2026-09-29)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| probe | regions | freq |
|-------|---------|-----:|
| оформление квартиры на родственника | 55,11176 | 21 |
| оформление квартиры на родственника | 225 (compare RU) | 2058 |
| дарение квартиры близкому родственнику | 55,11176 | 164 |
| купить квартиру в тюмени вторичка | 55,11176 | 3413 |
| продажа квартиры после дарения | 55,11176 | 3 |

**wordstat_rework:** probe «продажа квартиры после дарения» 3 (55+11176) → weak buyer spine; «оформление квартиры на родственника» 21 локально но **2058** RU compare → thematic P0 aligned with viral pensioner angle; localize body/H1 на Tyumen вторичка + аванс; supporting buyer demand «купить квартиру в тюмени вторичка» 3413 in rework chain  
**final P0:** «оформление квартиры на родственника» regions 55,11176 freq **21** (compare RU **225** freq **2058**)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- Trend energy: https://dzen.ru/a/Zw9N_lUREDllN79D (17158 views)
- Trend alternate: https://dzen.ru/a/arnh-zgnvihPFEtB (2114 views)

Output full handoff per SKILL with all required fields including: `slot_rubric: vtorichka`, `trend_radar` source_url+views for both viral refs, `anti_dupe_hard: PASS`, `dzen_casus_shape: PASS`, `needs_scout: false`, `wp_category_slugs` suggestion (vtorichka-i-riski, proverka-pered-pokupkoj).
