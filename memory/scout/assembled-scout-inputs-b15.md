# Scout inputs — 2026-08-29 (B15)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday weekend slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- **FROZEN today (29 Aug 2026 live plots — DO NOT reuse):**
  - rent_to_buy_owner_sold_while_contract — «В Тюмени три года платили за квартиру — собственник продал её другим»
  - fssp_arrest_day_before_registration_tyumen — «В Тюмени приставы арестовали квартиру за два дня до регистрации»
  - storage_room_promised_not_in_egrn — «В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было»
  - akkreditiv_opened_seller_no_money — «Аккредитив открыли, сделку зарегистрировали — продавец без денег»
  - adult_guardianship_over_seller_day_before_advance — «Квартиру остановили за день до аванса — родственники пошли в суд»
  - double_sale_yalutorovsk — «В Ялуторовске квартиру продали двоим»
- Closed clusters (30d): illegal_renovation (B11), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction, B12 ddu_escrow_handover_delay, etc.
- `scout_helper.py --check-query` PASS for this plot
- `story_dup_check` PASS — cluster preliminary_contract_seller_sold_elsewhere_tyumen is NEW

## Proposed topic (PASS)

- **topic_id:** B15
- **title_draft:** В Тюмени подписали предварительный — продавец продал квартиру другим
- **slug:** v-tyumeni-predvaritelnyj-dogovor-prodavec-prodal-kvartiru-drugim
- **cluster_id (new):** preliminary_contract_seller_sold_elsewhere_tyumen
- **story_dup_check:** PASS — distinct from rent_to_buy (найм с правом выкупа), double_sale_yalutorovsk (два покупателя на регистрации), deposit_before_auction (торги), receipt fraud; plot = предварительный ДКП + задаток, продавец параллельно продал другим и подал на регистрацию

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени нашла вторичку, подписала предварительный договор купли-продажи, внесла задаток, банк одобрил ипотеку, назначили дату основного ДКП
- **risk:** продавец заключил основной договор с другими покупателями и подал документы в Росреестр, не предупредив первых — «двойная продажа» через обход предварительного
- **time:** за три дня до плановой сделки / через две недели после предварительного
- **finale:** первые покупатели увидели статус в ЕГРН, остановили внесение аванса по ипотеке; задаток вернули по пункту о штрафе; квартиру получили другие; суд по предварительному — отдельный трек, но объект для первых закрыт
- **comment_magnet_angle:** «Предварительный договор для вас — реальная страховка или просто бумага до аванса?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK

| probe | regions | freq |
|-------|---------|------|
| предварительный договор купли продажи | 55+11176 | 265 |
| **предварительный договор купли продажи квартиры** | **55+11176** | **62** |
| предварительный договор купли продажи квартиры | 225 (compare) | 6612 |
| согласие супруга продажа квартиры | 55+11176 | 74 (rejected — close to marital_share cluster) |
| кадастровая ошибка | 55+11176 | 53 (rejected — weak casus spine) |
| аккредитив при покупке квартиры | 55+11176 | 44 (rejected — today's live plot) |

**wordstat_rework log:**
- probe «предварительный договор купли продажи» 55+11176 → 265
- tighten to apartment buyer jargon → **final P0 «предварительный договор купли продажи квартиры» regions 55,11176 freq 62** (compare RU225 6612)

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_5142/ — ГК РФ ст. 429 предварительный договор
- https://base.garant.ru/ — судебная практика нарушение предварительного договора купли-продажи недвижимости
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B15, title, slug, signal_urls, research angles for Research role.
