# Scout inputs — 2026-08-28 (B11)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-28 (YEKT Friday, slot ~09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 15 active locks
- Closed clusters (30d): marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction
- Live WP ~20 titles fetched via doctor/today (2026-08-27 posts on notarius/supruzheskaya, rodstvenniki 2y, 4 months search, matkapital, bankruptcy, etc.)
- `published-titles-only.md` + `shared/published-articles.md` — B02–B10 ledger

## Proposed topic (PASS scout_helper --check-query)

- **topic_id:** B11
- **title_draft:** В Тюмени купили квартиру с открытой кухней — Росреестр отказал в регистрации
- **slug:** v-tyumeni-kupili-kvartiru-s-otkrytoy-kuhney-rosreestr-otkazal-v-registracii
- **cluster_id (new):** illegal_renovation_rosreestr_blocks_registration
- **story_dup_check:** PASS (no match to closed clusters; avoid «суд забрал» phrasing — finale = отказ Росреестра / приостановка / предписание жилинспекции, NOT relatives contest 2y later)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила вторичку с «красивой» открытой кухней; аванс внесли, документы подали
- **risk:** неузаконенная перепланировка (снесена несущая/межкомнатная стена) не отражена в ЕГРН/техпаспорте
- **time:** через 9–14 дней после подачи на регистрацию, накануне планируемой выдачи ключей
- **finale:** Росреестр приостановил регистрацию / отказ; покупатели не стали собственниками; продавец не согласен «вернуть как было» до сделки
- **comment_magnet_angle:** «Скидку за открытую кухню вы бы взяли — или это всегда красный флаг?»

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen casus without Klyshin — preferred to avoid closed plots)
- **signal_urls (tenant):** https://dzen.ru/holyslav | https://t.me/holyslav92 | site blog | klyshin_A optional — not used this slot

## Wordstat MCP-KV (live 2026-08-28)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|------|
| перепланировка квартира | 55 | 369 (top: перепланировка квартиры тюмень 86) |
| квартира с неузаконенной перепланировкой | 55+11176 | 17 |
| покупка квартиры с неузаконенной перепланировкой | 225 | 192 |
| риски покупки квартиры с неузаконенной перепланировкой | 225 | 72 |
| неузаконенная перепланировка | 225 | 2234 |
| согласование перепланировки тюмень | 55 | 14 |

**wordstat_rework log:**
- probe «двойная продажа квартиры» 55+11176 → empty/weak locally
- probe «мошенничество при покупке квартиры» 55 → 3
- probe «аренда с выкупом квартиры тюмень» 55+11176 → 26
- **final P0:** «покупка квартиры с неузаконенной перепланировкой» — RU225 **192**; localized spine «квартира с неузаконенной перепланировкой» 55+11176 **17**; buyer spine «перепланировка квартиры тюмень» **86**

## Output required

Write `.cursor/excalibur-blog-handoff.md` with all Scout handoff fields per SKILL.md:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id.

Then lock topic_id B11, title, slug, signal_urls, research angles for Research role.
