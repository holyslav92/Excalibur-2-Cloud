# Scout inputs — 2026-08-30 (B13)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-30 (YEKT Sunday weekend slot 09:00 — Grok routine the-4)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- **FROZEN (owner + Saturday 29.08.2026 live — DO NOT reuse plots):**
  - rent_to_buy_owner_sold — «три года платили по найму с правом выкупа»
  - guardianship_adult_day_before_advance — «родственники оформили опеку за день до аванса»
  - fssp_arrest_two_days_before_registration — «приставы арестовали за два дня до регистрации»
  - accreditive_seller_no_money — «аккредитив открыли, продавцу деньги не дошли»
  - storage_room_gift_not_in_egrn — «кладовка в подарок, в ЕГРН её не было»
  - preliminary_contract_sold_to_others — «предварительный договор — продали другим»
  - Plus 30d locks: egrn_line, bankruptcy, matkapital, marital_share, court_2y, elderly_phone, pnd, military, grandma_poa, inheritance_son, illegal_renovation B11, escrow B12, etc.
- Live WP ~20 from excalibur_blog_today RECENT_WP_POSTS (2026-08-29 batch above + B11/B12)
- `published-titles-only.md` + `shared/published-articles.md` — B02–B12 ledger

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B13
- **title_draft:** В Тюмени продавец показал справку о закрытии ипотеки — банк всё ещё держал залог
- **slug:** v-tyumeni-prodavec-pokazal-spravku-o-zakrytii-ipoteki-bank-derzhal-zalog
- **cluster_id (new):** seller_mortgage_not_discharged_bank_lien_blocks_deal
- **story_dup_check:** PASS — distinct from B09 (ипотека покупателя одобрена, строка в ЕГРН); Saturday accreditive (деньги не дошли продавцу после регистрации); seller_bankruptcy; egrn_line generic; plot = продавец представил «справку о погашении», но обременение ипотеки в ЕГРН/банке не снято → регистрация невозможна до аванса

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала вторичку с ипотекой у продавца; продавец показал справку банка «кредит погашен» и обещал снять залог «в день сделки»
- **risk:** ипотечное обременение в ЕГРН не снято — банк не выдал согласие на сделку; справка о закрытии не равна снятию залога в Росреестре
- **time:** за 24–48 часов до планируемого внесения аванса, при финальной проверке выписки ЕГРН и запроса в банк
- **finale:** сделку остановили до аванса; покупатели ушли на другой объект; продавец должен дождаться снятия обременения (2–4 недели) — покупатели не ждали
- **comment_magnet_angle:** «Справку банка о закрытии кредита вы бы приняли за достаточную — или только свежую выписку ЕГРН без обременения?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen seller-mortgage casus without Klyshin)
- **signal_urls:** see list below

## Wordstat MCP-KV (live 2026-08-30)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| продажа квартиры при ипотеке | 55 | 25 |
| как продать ипотечную квартиру | 55 | 22 |
| купить квартиру в тюмени вторичка | 55 | 3225 |
| купить квартиру в тюмени | 55+11176 | 22699 |
| выписка из егрн на квартиру | 55 | 190 |
| купить квартиру вторичка | 55 | 5298 |
| продажа квартиры при ипотеке | 225 (compare) | — |

**wordstat_rework log:**
- probe «продажа квартиры при ипотеке» 55 → 25 (on-plot, narrow)
- probe «как продать ипотечную квартиру» 55 → 22 (seller-side)
- **rework:** buyer spine + Tyumen localize → **final P0 «купить квартиру в тюмени вторичка» regions 55,11176 freq 3225** (compare context: «купить квартиру в тюмени» 22699); casus hook ties to seller mortgage discharge check before advance

## signal_urls (research)

- https://dzen.ru/holyslav — holyslav channel (FSSP/mortgage context, not duplicate)
- https://t.me/holyslav92
- {{SITE_BASE}}/blog/
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
