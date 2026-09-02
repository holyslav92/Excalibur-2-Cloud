# Scout inputs — 2026-09-02 (B21)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-02 (YEKT Wednesday slot 10:05 MSK)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks
- **FROZEN live plots (02 Sep 2026 — DO NOT reuse):**
  - `newbuild_assignment_paid_developer_refused_reregister` — «В Тюмени оплатили переуступку — застройщик не оформил ДДУ» (slug v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat)
  - `newbuild_booking_price_spike_380k` — «Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч»
  - `newbuild_acceptance_wet_screed_keys_denied` — «На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали»
  - `transhevaya_ipoteka_payment_spike` — «Платёж по новостройке вырос в 8 раз — до брони»
- **Closed newbuild clusters (30d):** B12 `ddu_escrow_handover_delay_tyumen` (ключи перенесли на год / эскроу заморозили); B19 `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen`; B20 `newbuild_developer_legal_entity_change_ddu_escrow_tyumen`
- Live WP ~20 (EXCALIBUR_RECENT_WP_POSTS 2026-09-02): today's переуступка; booking 380k; priemka wet screed; transhevaya; B20 legal entity; B19 family mortgage+escrow; kapremont secondary; double sale; forged spouse; matkapital child shares; propisannye; communal share
- `published-titles-only.md` + `shared/published-articles.md` — B02–B15, B19, B20 ledger

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B21
- **title_draft:** В Тюмени в КП обещали газ и воду — на ключах коммуникации не подвели
- **slug:** v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli
- **cluster_id (new):** newbuild_kp_land_boundary_utilities_denied_tyumen
- **story_dup_check:** PASS — distinct from B12 (перенос сдачи квартиры/заморозка эскроу), B20 (смена юрлица/новый ДДУ), B19 (семейная ипотека+эскроу+маткапитал), today's priemka wet screed (квартира в ЖК), переуступка, бронь 380k, transhevaya; plot = покупка **дома в коттеджном посёлке** под Тюменью: в ДДУ и на плане застройщика были границы участка и подведённые коммуникации, на выдаче ключей газ/вода к границе участка не подведены — акт не подписали, ипотека зависла, расторжение ДДУ

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала дом в коттеджном посёлке от застройщика, подписала ДДУ, внесла деньги на эскроу и ипотеку; на презентации показали план с газом и водой у забора участка
- **risk:** в день выдачи ключей коммуникации оказались не подведены к границе участка (или кадастровый план показал иной контур) — застройщик настаивал подписать акт «как есть», банк не разблокировал остаток ипотеки
- **time:** в день выдачи ключей / через три месяца после внесения на эскроу (после обещанного срока сдачи дома)
- **finale:** акт приёма не подписали; через суд расторгли ДДУ, деньги с эскроу вернули через ~4 месяца, но аналогичный дом в том же посёлке подорожал — семья вынуждена искать другой КП или квартиру в ЖК
- **comment_magnet_angle:** «Дом в коттеджном посёлке без газа и воды у забора — вы всё равно подпишете акт приёмки или будете ждать, пока застройщик подведёт коммуникации?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild KP casus without Klyshin — preferred; avoid today's переуступка/priemka/booking clusters)

## Wordstat MCP-KV (live 2026-09-02)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройка | 55+11176 | 10 (rejected — live today) |
| приемка новостройка тюмень | 55+11176 | weak/narrow (rejected — priemka cluster live) |
| коттеджный поселок тюмень | 55+11176 | 1831 (broad context) |
| купить дом в коттеджном поселке тюмень | 55+11176 | 38 |
| **коттеджные поселки тюмень купить дом** | **55+11176** | **59** |
| коттеджные поселки тюмень купить дом | 225 (compare) | 125 |
| расторжение дду | 55+11176 | 123 (context — on-plot legal spine) |
| купить новостройку тюмень | 55+11176 | 1168 (too broad for P0) |

**wordstat_rework log:**
- probe «переуступка новостройка» 55+11176 → 10 (weak; live plot today)
- probe «коттеджный поселок тюмень» 55+11176 → 1831 (strong but broad; not buyer-action)
- probe «купить дом в коттеджном поселке тюмень» 55+11176 → 38
- probe «коттеджные поселки тюмень купить дом» 55+11176 → 59; compare RU225 → 125
- **rework:** buyer jargon KP+house Tyumen → **final P0 «коттеджные поселки тюмень купить дом» regions 55,11176 freq 59** (compare RU225 125)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и КП в Тюмени; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ: обязанности застройщика по коммуникациям и передаче объекта
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B21, title, slug, signal_urls, research angles for Research role.
