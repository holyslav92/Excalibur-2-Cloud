# Scout inputs — 2026-09-01 (B20)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-01 (YEKT Monday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- **FROZEN today (01 Sep 2026 live plots — DO NOT reuse):**
  - `newbuild_acceptance_wet_screed_keys_denied` — daily «На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали»
  - `transhevaya_ipoteka_payment_spike` — «Платёж по новостройке вырос в 8 раз — до брони»
  - `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` — B19 longform «Семейную ипотеку на новостройку одобрили — эскроу не открыли»
- **Closed clusters (30d):** B12 ddu_escrow_handover_delay (перенос сдачи/эскроу); all frozen secondary in used-clusters.json
- Live WP ~20: priemka wet screed; transhevaya ipoteka; B19 escrow matkapital; kapremont secondary; double sale; forged spouse B15; etc.
- `scout_helper.py --check-query` PASS + `topic_focus.py` PASS for proposed title

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B20
- **title_draft:** В Тюмени забронировали новостройку — через двое суток цену подняли на 380 тысяч
- **slug:** v-tyumeni-zabronirovali-novostrojku-cherez-dvoe-sutok-cenu-podnyali
- **cluster_id (new):** newbuild_booking_price_increase_after_reservation_tyumen
- **story_dup_check:** PASS — distinct from B12 (срок сдачи/эскроу), B19 (семейная ипотека/маткапитал/эскроу), today's priemka wet screed, transhevaya payment spike; plot = платная бронь новостройки → застройщик внезапно поднял цену квартиры через 48 часов → бронь сгорела / семья не потянула доплату

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени в офисе продаж застройщика забронировала квартиру в новостройке, внесла плату за бронь и получила фиксацию цены «до подписания ДДУ»
- **risk:** через двое суток менеджер сообщил, что «акция закончилась» и цена выросла на 380 тысяч рублей; без доплаты бронь аннулируют, квартиру выставят в свободную продажу
- **time:** 48 часов после оплаты брони, за сутки до дедлайна подписания ДДУ
- **finale:** семья отказалась от доплаты, бронь сгорела, плату за бронирование не вернули (или вернули частично по удержанию); аналогичная планировка ушла на 420 тыс дороже; пришлось искать другой ЖК
- **comment_magnet_angle:** «Бронь с фиксацией цены вам кажется договором — или вы всё равно платите, зная, что застройщик может поднять цену за 48 часов?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild booking-price casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-01)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройка тюмень | 55+11176 | 4667 (context) |
| купить новостройку в тюмени | 55+11176 | 874 |
| ипотека от застройщика тюмень | 55+11176 | 518 |
| ипотека тюмень новостройки от застройщика | 55+11176 | 101 |
| приемка квартиры в новостройке тюмень | 55+11176 | 30 |
| переуступка тюмень | 55+11176 | 17 (weak) |
| долгострой тюмень | 55+11176 | 91 |
| бронь новостройка тюмень | 55+11176 | API empty (weak) |
| **купить новостройку в тюмени** | **55+11176** | **874** |
| купить новостройку в тюмени | 225 (compare) | 1192 |

**wordstat_rework log:**
- probe «переуступка тюмень» 55+11176 → 17 (weak; different plot)
- probe «бронь новостройка тюмень» → empty API (weak standalone)
- probe «долгострой тюмень» → 91 (different plot — delay not price hike)
- probe «ипотека от застройщика тюмень» → 518 (strong buyer intent)
- **rework:** newbuild buyer jargon + Tyumen local → **final P0 «купить новостройку в тюмени» regions 55,11176 freq 874** (compare RU225 1192); on-plot secondary «ипотека от застройщика тюмень» 518

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_122946/ — 214-ФЗ долевое строительство (бронь, ДДУ)
- https://www.gosuslugi.ru/help/faq/housing/100361 — покупка квартиры в строящемся доме
- https://dzen.ru/holyslav — контекст новостроек Тюмени
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B20, title, slug, signal_urls, research angles for Research role.
