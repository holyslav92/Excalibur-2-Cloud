# Scout inputs — 2026-08-28 (B12)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-28 (YEKT Friday, slot ~15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- Closed clusters (30d): illegal_renovation_rosreestr_blocks_registration (B11 today), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction
- Live WP ~20 titles (2026-08-28): includes **double sale Ялуторовск** (NOT in used-clusters yet — avoid double_sale cluster this slot), B11 open kitchen, notarius supruzheskaya, court 2y, matkapital, bankruptcy, elderly phone, etc.
- `published-titles-only.md` + `shared/published-articles.md` — B02–B11 ledger

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B12
- **title_draft:** Ключи от новостройки в Тюмени перенесли на год — деньги на эскроу заморозили
- **slug:** v-tyumeni-perenesli-sdachu-novostroyki-eskrou-zamorozili-dengi
- **cluster_id (new):** ddu_escrow_handover_delay_tyumen
- **story_dup_check:** PASS — distinct from B02 (расписка/аккредитив вторичка), B09 (строка ЕГРН), B11 (перепланировка); NOT double_sale (live WP Ялуторовск today); finale = перенос сдачи + эскроу/ДДУ, NOT отказ Росреестра на вторичке

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени подписала ДДУ в ЖК, внесла полную стоимость на эскроу-счёт, ждала ключи по графику застройщика
- **risk:** односторонний перенос срока передачи квартиры на 12 месяцев — деньги на эскроу нельзя вернуть без расторжения/суда по 214-ФЗ; ипотека «висит»
- **time:** за три недели до обещанной выдачи ключей (квартал сдачи в рекламе ЖК)
- **finale:** дольщик подал претензию и расторжение — банк вернул деньги с эскроу / застройщик выплатил неустойку по решению суда; альтернатива финала для Research: частичная компенсация + новая дата с актом приёмки
- **comment_magnet_angle:** «Если застройщик переносит сдачу на год — вы ждёте или сразу требуете возврат с эскроу?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen novostroyka casus without Klyshin — preferred; avoid closed plots and today's double-sale live post)
- **signal_urls (tenant):** https://t.me/klyshin_A (checked, not used) | https://dzen.ru/holyslav | {{SITE_BASE}}/blog/ | https://t.me/holyslav92

## Wordstat MCP-KV (live 2026-08-28)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| эскроу счет новостройка | 225 | 344 |
| купить квартиру по дду | 225 | 2053 (top: купить квартиру по дду 1845) |
| купить квартиру по дду | 55+11176 | 23 |
| новостройки тюмень | 55+11176 | **4717** |
| новостройки тюмень | 225 (compare) | 8980 |
| купить новостройку в тюмени | 55+11176 | 830 |
| ипотека новостройка тюмень | 55+11176 | 214 |

**wordstat_rework log:**
- probe «эскроу счет новостройка» RU225 → 344 (buyer spine ok but narrow)
- probe «купить квартиру по дду» RU225 → 1845; same phrase 55+11176 → 23 (weak local on exact DDU phrase)
- probe «аренда с выкупом квартиры тюмень» 55+11176 → 26 (weak)
- probe «машиноместо егрн» 55+11176 → 3 (too weak for P0)
- **rework:** localize Tyumen + novostroyka buyer jargon → **final P0 «новостройки тюмень» regions 55,11176 freq 4717** (compare RU225 8980); secondary spine «купить новостройку в тюмень» 830

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B12, title, slug, signal_urls, research angles for Research role.
