# Scout inputs — 2026-08-29 (B13)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday weekend slot 09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- Closed clusters (30d): illegal_renovation (B11), ddu_escrow_handover (B12 live), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction
- Live WP ~20 titles (2026-08-29): includes double sale Ялуторовск (28.08) — NOT same cluster (rent-to-buy ≠ двойная продажа двоим); B11 open kitchen, B12 novostroyka escrow, notarius, court 2y, matkapital, bankruptcy, elderly phone, повестка, etc.
- `scout_helper.py --check-query` PASS for proposed cluster

## Proposed topic (PASS scout_helper + story_dup PASS)

- **topic_id:** B13
- **title_draft:** Три года платили по найму с правом выкупа — в Тюмени собственник продал квартиру другим
- **slug:** v-tyumeni-tri-goda-platili-po-naimu-s-pravom-vykupa-sobstvennik-prodal-kvartiru
- **cluster_id (new):** rent_to_buy_owner_sold_while_contract
- **story_dup_check:** PASS — distinct from double_sale_two_buyers (Ялуторовск), court_took_apartment, deposit_before_auction, doverennost; plot = договор найма с правом выкупа + скрытая продажа во время выплат, NOT двойная регистрация двоим покупателям

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени жила в квартире по договору найма с правом выкупа, три года платили «как свои» — аренду плюс выкупные платежи по графику
- **risk:** собственник параллельно продал квартиру другому покупателю; новый владелец предъявил права; семья узнала за неделю до финального выкупного платежа, когда собрались внести остаток
- **time:** накануне последнего выкупного платежа (третий год контракта)
- **finale:** сделку остановили до аванса на «другую» квартиру; проверка ЕГРН и реестра переходов прав показала продажу; семья через суд взыскала выплаты и не потеряла право на возврат (agency landing — проверили реестр до финального платежа, не «вторичка мина»)
- **comment_magnet_angle:** «Если платите по найму с правом выкупа — раз в квартал смотрите ЕГРН или только на слово собственника?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen rent-to-buy casus without Klyshin — preferred; avoid closed plots and live double-sale Ялуторовск angle)
- **signal_urls (tenant):** https://t.me/klyshin_A (checked, not used) | https://dzen.ru/holyslav | {{SITE_BASE}}/blog/ | https://t.me/holyslav92

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| аренда с выкупом квартиры | 55+11176 | 38 |
| если в тюмени аренда с выкупом квартиры | 55+11176 | 15 (sub-query) |
| договор найма с правом выкупа | 55+11176 | 21 |
| купить вторичку в тюмени | 55+11176 | **4882** |
| купить вторичку в тюмени | 225 (compare) | ~6347 |
| риски покупки квартиры | 55+11176 | 63 |
| машиноместо егрн | 55+11176 | 3 |

**wordstat_rework log:**
- probe «аренда с выкупом квартиры» 55+11176 → 38 (exact legal phrase weak locally)
- probe «договор найма с правом выкупа» 55+11176 → 21 (still weak for P0)
- probe «машиноместо егрн» 55+11176 → 3 (too weak — rejected parking cluster)
- **rework:** localize Tyumen + secondary buyer jargon → **final P0 «купить вторичку в тюмени» regions 55,11176 freq 4882** (compare RU225 ~6347); secondary spine «аренда с выкупом квартиры» 38 for cover-text context

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
