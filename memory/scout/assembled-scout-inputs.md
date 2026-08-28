# Scout inputs — 2026-08-28 (B12)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-28 (YEKT Friday, slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- Closed clusters (30d): illegal_renovation_rosreestr_blocks_registration (B11), marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction
- Live WP ~20 titles fetched 2026-08-28 (latest: B11 open kitchen / Rosreestr; notarius supruzheskaya; court 2y relatives; matkapital; bankruptcy; elderly phone; etc.)
- `shared/published-titles.md` + `shared/published-articles.md` — B02–B11 ledger

## Proposed topic (PASS scout_helper --check-query)

- **topic_id:** B12
- **title_draft:** В Ялуторовске квартиру продали двум покупателям — первую пытаются выселить
- **slug:** v-yalutorovske-kvartiru-prodali-dvum-pokupatelyam-pervuyu-pytayutsya-vyselit
- **cluster_id (new):** double_sale_two_buyers_rieltor_poa
- **story_dup_check:** PASS (distinct from doverennost_svo_seller — plot = двойная продажа одной квартиры двум покупателям по доверенности риелтора, продавец выбрал более высокую цену; finale = попытка выселения первого покупателя / оспаривание первого договора, NOT СВО-продавец / NOT relatives 2y later)

## Dzen news-casus shape (target PASS)

- **event:** жительница Ялуторовска (Тюменская область) купила квартиру через риелтора по доверенности; деньги перевела, жила в квартире
- **risk:** двойная продажа — риелтор по доверенности заключила сделки с двумя покупателями, продавец получил деньги от обоих
- **time:** спустя год после первой сделки всплыл «второй законный владелец»; попытка выселения первой покупательницы
- **finale:** продавец выбрал покупателя с большей суммой; первую покупательницу пытаются выселить из «своей» квартиры; следствие / проверка; местные юристы отказались — дело взял внешний юрист (URA.RU, юрист Роман Матвеев)
- **comment_magnet_angle:** «Кто прав — тот, кто первым внёс деньги, или тот, кто заплатил больше?»

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen-region casus without Klyshin — preferred; no fresh @klyshin_A post on double-sale plot)
- **signal_urls (tenant):** https://t.me/klyshin_A (monitored, not used) | https://dzen.ru/holyslav | {{SITE_BASE}}/blog/ | https://t.me/holyslav92

## Research signal URLs

- https://ura.news/news/1053102901 — Ялуторовск, двойная продажа, риелтор по доверенности
- https://tumentoday.ru/2025/11/29/babushkina_skhema_kak_moshenniki_lishayut_tyumentsev_kvartir_cherez_pensionerov/ — контекст тюменских мошеннических схем с недвижимостью (9 УД 2024–2025, прокуратура)
- https://megatyumen.ru/realty/tyumencam-obyasnili-kak-minimizirovat-riski-pri-pokupke-kvartiry/ — риски покупки, безопасные расчёты

## Wordstat MCP-KV (live 2026-08-28)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq |
|-------|---------|------|
| двойная продажа | 55+11176 | 13 |
| двойная продажа квартиры | 225 | 281 (top: двойные продажи квартир 281) |
| двойной договор купли продажи квартиры | 225 | 42 |
| аккредитив при покупке квартиры | 55+11176 | 45 |
| проверка егрн | 55+11176 | 28 |
| аванс при покупке квартиры | 55+11176 | 8 |
| эскроу счет квартира | 55+11176 | 40 (top: квартира с эскроу счетом 12) |

**wordstat_rework log:**
- probe «двойная продажа» 55+11176 → **13** (weak local buyer volume)
- probe «двойная продажа квартиры» compare225 → **281** (двойные продажи квартир)
- rework: buyer jargon — безопасные расчёты / проверка перед авансом
- probe «аккредитив при покупке квартиры» 55+11176 → **45**
- probe «проверка егрн» 55+11176 → **28**
- **final P0:** «аккредитив при покупке квартиры» — regions 55,11176 **45** (buyer spine: безопасный расчёт вместо перевода риелтору); compare «двойные продажи квартир» RU225 **281**

## Output required

Write `.cursor/excalibur-blog-handoff.md` with all Scout handoff fields per SKILL.md:
topic_id, title draft, slug suggestion, wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id, signal_urls used.

Then lock topic_id B12, title, slug, signal_urls, research angles for Research role.
