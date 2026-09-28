# Scout inputs — B33 slot 17:00 YEKT 2026-09-28

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-28  
**slot:** 17:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka (вторичка Тюмень)  
**tenant:** The Риэлтор — Святослав Шакин, tymenrieltor.ru  
**topic_market_focus:** rubric_per_slot  
**dzen_rf_pack:** true

## Trend Radar (slot vtorichka)

`memory/blog/trend-radar/trend-radar.json` (2026-09-28, vtorichka angles):
- **viral_mechanism:** almost lost перед ключами/деньгами (Окулов PRO загородный дом, 17k views)
- **energy mirror:** paper looked clean → hidden debt before money on table

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK
- Avoid frozen secondary: egrn_line_blocks_advance (B09), seller bankruptcy, matkapital/opieka, registered persons, forged consent, etc. (see used-clusters.json)
- Last published newbuild slots B30–B32 — this slot is **vtorichka only**
- `scout_helper.py --check-query` PASS 2026-09-28
- `excalibur_blog_topic_focus.py` PASS (slot rubric vtorichka, allow_hit=аванс)
- `story_dup.py` — distinct cluster `secondary_utility_electricity_debt_before_advance_tyumen`

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** За 3 дня до аванса в Тюмени всплыл долг за свет 186 тысяч — семья отказалась от сделки
- **slug:** za-3-dnya-do-avansa-v-tyumeni-vspyl-dolg-za-svet-186-tysyach-semya-otkazalas-ot-sdelki
- **article_dir:** memory/blog/articles/B33-za-3-dnya-do-avansa-v-tyumeni-vspyl-dolg-za-svet-186-tysyach-semya-otkazalas-ot-sdelki
- **cluster_id (new):** secondary_utility_electricity_debt_before_advance_tyumen
- **slot_rubric:** vtorichka
- **viral_mechanism:** almost lost перед авансом — «квартира чистая», пока не открыли лицевой счёт и справку ЖКУ
- **vtorichka_mechanism:** Семья покупает двушку на вторичке в Тюмени (ипотека одобрена). Продавец показывает свежую выписку без обременений, на осмотре «всё оплачено». За 3 дня до внесения аванса риэлтор запросил справку об отсутствии задолженности по ЖКУ и сверку лицевого счёта — **долг за электроэнергию 186 400 ₽** (накопленный, счётчик не меняли). УК предупредила: при смене собственника долг может уйти новому владельцу через суд/registrar practice. Семья **не внесла аванс**, сделку остановили до договора
- **why_vtorichka_not_newbuild:** вторичная квартира, продавец-физлицо, ЖКУ/лицевой счёт, аванс на вторичке — без ДДУ, эскроу, застройщика
- **story_dup_check:** PASS — not egrn_line (no обременение plot), not B14 ipoteka spravka, not communal share, not capremont-only retitle
- **h1_fingerprint_check:** PASS — «3 дня + аванс + долг за свет 186» distinct from last-3 formula (DDU/escrow/insurance newbuild)
- **formula_spam_check:** PASS — last3 B31 insurance DDU, B32 escrow requisites, B30 assignment ban — this is secondary utility debt before advance

## Dzen news-casus shape: PASS

- **event:** семья с ребёнком выбрала вторичку, торг согласован, банк одобрил ипотеку
- **risk:** 186k коммунальный долг «прилипает» к покупателю; аванс 350k уже на подходе
- **time:** за 3 дня до планового внесения аванса на безопасный счёт
- **finale:** аванс не внесли; продавец предложил «скину 50 тысяч с цены» — семья отказалась; пошли проверять другой объект с полным пакетом ЖКУ **до** аванса
- **comment_magnet_angle:** «Если перед авансом всплывает долг за свет 186 тысяч, а продавец давит «подпишем сегодня» — вы бы внесли аванс или ушли сразу?»

## Klyshin hook

- **klyshin_hook:** none (original Tyumen secondary casus)

## Wordstat MCP-KV (live 2026-09-28)

| probe | regions | freq |
|-------|---------|-----:|
| купить квартиру в тюмени | 55,11176 | 35654 |
| купить квартиру в тюмени вторичка | 55,11176 | 6415 |
| капремонт при покупке квартиры | 55,11176 | 189 |
| долги за капремонт при покупке квартиры | 55,11176 | 30 |

**wordstat_rework:** utility-debt angle weak on «коммунальные долги» alone → spine P0 **«купить квартиру в тюмени вторичка»** 6415 + electricity debt mechanism in H1/body  
**final P0:** «купить квартиру в тюмени вторичка» regions 55,11176 freq **6415** (compare «купить квартиру в тюмени» 35654 RU-wide context)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- Trend: https://dzen.ru/a/Zw9N_lUREDllN79D (almost lost energy)

Output full handoff per SKILL with: `anti_dupe_hard: PASS`, `dzen_casus_shape: PASS`, `needs_scout: false`, `wp_category_slugs` suggestion for vtorichka (vtorichka-i-riski, proverka-pered-pokupkoj).
