# Scout inputs — 2026-08-29 (B13)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday slot ~12:00 UTC+5 automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- Closed clusters (30d): illegal_renovation (B11), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction
- B12 published 2026-08-28: ddu_escrow_handover_delay (новостройка эскроу) — avoid repeat
- Live WP 2026-08-29: opeka nad prodavcom, rent-with-buyout 3y — avoid (fresh daily posts)
- Live WP 2026-08-28: double sale Ялуторовск — avoid double_sale cluster
- `published-titles-only.md` + `shared/published-articles.md` — B02–B12 ledger

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B13
- **title_draft:** В Тюмени обещали машино-место к квартире — в Росреестре прав на него не нашли
- **slug:** v-tyumeni-obeshchali-mashino-mesto-k-kvartire-prav-v-rosreestre-ne-nashli
- **cluster_id (new):** parking_promise_not_in_registry_tyumen
- **story_dup_check:** PASS — distinct from B11 (перепланировка/открытая кухня), B09/B01 (строка ЕГРН вторичка), B12 (эскроу новостройка), matkapital_opieka (дети 3 года), live double-sale/rent-buyout/opeka today; plot = обещанное машино-место/паркинг «в подарок» к сделке, права не зарегистрированы / чужой собственник

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в ЖК с «бонусом» — машино-место в подземном паркинге; продавец/застройщик включил место в договор купли-продажи или отдельным приложением
- **risk:** перед авансом выяснилось, что машино-место не принадлежит продавцу, не выделено в ЕГРН как отдельный объект, или зарегистрировано на третьих лиц — покупатель рискует заплатить за «воздух»
- **time:** за два дня до внесения аванса на квартиру, на финальном согласовании комплекта «квартира + парковка»
- **finale:** сделку по квартире разделили — аванс остановили до проверки реестра; машино-место вычеркнули из пакета / пересчитали цену; альтернатива для Research: покупатель отказался от «подарка», купил только квартиру, парковку оформили отдельным ДКП после проверки
- **comment_magnet_angle:** «Машино-место „в подарок“ — вы верите на слово или требуете выписку до аванса?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen casus without Klyshin — preferred; avoid closed clusters and today's live WP plots)
- **signal_urls (tenant):** https://t.me/klyshin_A (checked, not used) | https://dzen.ru/holyslav | {{SITE_BASE}}/blog/ | https://t.me/holyslav92

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| купить машиноместо в тюмени | 55 | **53** |
| купить машиноместо | 55 | 153 |
| купить машиноместо | 225 (compare) | 29560 |
| машиноместо егрн | 55+11176 | 3 (too weak) |
| переуступка дду | 55 | 23 |
| аккредитив при покупке квартиры | 55 | 23 |

**wordstat_rework log:**
- probe «машиноместо егрн» 55+11176 → 3 (too weak for P0)
- probe «переуступка дду» 55 → 23 (ok but weaker local story fit)
- **rework:** localize Tyumen buyer jargon → **final P0 «купить машиноместо в тюмени» regions 55,11176 freq 53** (compare RU225 «купить машиноместо» 29560); secondary spine «купить машиноместо» 153 region 55

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
