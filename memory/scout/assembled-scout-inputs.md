# Scout inputs — 2026-08-29 (B14 weekend slot 15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday weekend slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{SITE_BASE}})
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 17 active locks
- **FROZEN today (29 Aug 2026 live plots — DO NOT reuse):**
  - rent_to_buy_owner_sold_while_contract — «В Тюмени три года платили за квартиру — собственник продал её другим»
  - guardianship/incapacity day before advance — «Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд»
  - fssp_arrest_day_before_registration_tyumen — B13 noon slot
- Closed clusters (30d): illegal_renovation (B11), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction, fssp_arrest, B12 ddu_escrow_handover_delay, live double_sale Ялуторовск, etc.
- `scout_helper.py --check-query` + `story_dup.py --text` → PASS for proposed cluster

## Proposed topic (PASS)

- **topic_id:** B14
- **title_draft:** В Тюмени обещали кладовку в подарок — в выписке ЕГРН её не оказалось
- **slug:** v-tyumeni-obeshchali-kladovku-v-podarok-v-vyske-ee-ne-okazalos
- **cluster_id (new):** storage_room_promised_not_in_egrn
- **story_dup_check:** PASS — distinct from egrn_line_blocks_advance (обременение/строка в ЕГРН на саму квартиру), illegal_renovation, matkapital child shares; plot = продавец/агент обещает кладовку/келлер как бонус к сделке, но объект не в собственности продавца / нет кадастрового номера / не в ЕГРН

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала вторичку в доме с подвалом; риелтор продавца назвал «кладовку в подарок» как аргумент цены
- **risk:** в расширенной выписке ЕГРН у продавца только квартира; «кладовка» — чужой подвал без права собственности или общее имущество без выдела
- **time:** за три дня до планируемого аванса, после одобрения ипотеки и согласования даты в МФЦ
- **finale:** сделку остановили до внесения аванса; покупатели нашли другой объект с оформленной кладовкой; продавец не смог быстро выделить/оформить право
- **comment_magnet_angle:** «Кладовку „в подарок“ вы проверяете отдельной выпиской до аванса или верите словам в объявлении?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen casus without Klyshin)

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| кладовка егрн | 55+11176 | 3 (too narrow) |
| купить кладовку | 55+11176 | 373 |
| **купить кладовку в тюмени** | **55+11176** | **108** |
| купить кладовку в тюмени | 225 (compare) | 157 |
| купить кладовку от застройщика в тюмени | 55+11176 | 18 |
| купить квартиру в тюмени | 55+11176 | 22699 (context only) |

**wordstat_rework log:**
- probe «кладовка егрн» 55+11176 → 3 (on-plot but too narrow for P0)
- probe «купить кладовку» 55+11176 → 373 (strong buyer spine)
- **rework:** local Tyumen buyer intent → **final P0 «купить кладовку в тюмени» regions 55,11176 freq 108** (compare RU225 157)

## signal_urls (research)

- {{SITE_BASE}}/blog/ — sibling interlink context
- https://dzen.ru/holyslav
- https://t.me/holyslav92
- https://t.me/klyshin_A — checked, not used
- Rosreestr / ГК РФ on общее имущество МКД + выдел доли в кладовке (research must cite live official sources)

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B14, title, slug, signal_urls, research angles for Research role.
