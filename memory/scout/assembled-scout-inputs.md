# Scout inputs — 2026-09-10 (B24, slot 09 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-10 (YEKT weekday slot 1 — 09:00 / 05 UTC)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 23 active locks (last_sync 2026-09-10)
- **Live WP ~12 titles (2026-09-06..09) — DO NOT reuse plot:**
  - пропал балкон на ключах — банк заморозил транш
  - застройщик год не платил неустойку — семья остановила приёмку
  - перед ДДУ ребёнку 7 лет — семейную ипотеку пересчитали
  - банк остановил транш после приёмки без замечаний
  - ключи без разрешения на ввод — банк заморозил ипотеку
  - на переуступке долг 94 тысячи
  - маткапитал за 3 недели до ключей
  - созаёмщика убрали за 7 дней до ДДУ
  - ДДУ расторгли из-за 5 дней просрочки рассрочки
  - газ в ДДУ на коттедж — 180м до магистрали
  - этаж в ДДУ 12-й — на ключах 2-й
  - на эскроу не хватило 400 тысяч
- **Rejected overlap:** bank appraisal below DDU → H1 fingerprint duplicate with installment/escrow amount cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: новостройк)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени бронь на новостройку сгорела за сутки — застройщик поднял цену на 450 тысяч
- **slug:** v-tyumeni-bron-na-novostrojku-sgorala-zastrojschik-podnyal-cenu
- **cluster_id (new):** booking_expired_price_hike_tyumen
- **top_energy_mirror:** almost_lost_home
- **newbuild_mechanism:** платная бронь с фиксацией цены на 48 часов сгорела — застройщик поднял стоимость квартиры на 450 тысяч накануне подписания ДДУ; семья не успела доплатить разницу
- **why_newbuild_not_secondary:** бронь и цена у застройщика в ЖК, ДДУ с эскроу ещё не подписан — не сделка с продавцом вторички и не проверка ЕГРН
- **story_dup_check:** PASS — distinct legal plot: бронь/оферта застройщика + срок 48 ч + внезапное повышение цены; не пересекается с эскроу-400k, ставкой банка (B22), апартаментами (B23), переуступкой-долгом, trade-in live plots

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, внесла бронь 50 тысяч, получила фиксацию цены и планировки на 48 часов
- **risk:** за сутки до дедлайна брони застройщик поднял цену на 450 тысяч — без доплаты бронь сгорает, объект уходит другому покупателю
- **time:** за 24 часа до окончания брони / накануне подписания ДДУ и открытия эскроу
- **finale:** семья не успела внести доплату — бронь сняли, квартиру забронировали другие; 50 тысяч брони удержали по оферте как штраф, ДДУ не подписали
- **comment_magnet_angle:** «Бронь на двое суток и внезапные +450 тысяч: вы бы доплатили, чтобы не потерять планировку, или искали бы другой ЖК — даже если ипотека уже одобрена?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild booking/price-hike casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-10)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| бронь новостройка | 55,11176 | 3 |
| бронь новостройки | 55,11176 | 3 |
| новостройки тюмень | 55,11176 | 4642 |
| **купить новостройку в тюмени** | **55,11176** | **885** |
| купить новостройку в тюмени | 225 (compare) | 1903 |

**wordstat_rework log:**
- probe «бронь новостройка» 55+11176 → 3 (weak direct match)
- probe «бронь новостройки» 55+11176 → 3 (weak)
- rework: localize Tyumen + newbuild buyer jargon (купить новостройку, бронь, застройщик, ДДU) → **final P0 «купить новостройку в тюмени» regions 55,11176,compare225 freq 885 (55+11176) / 1903 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и ипотеки; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ / ДДU (контекст брони и цены)
- https://www.domrf.ru/ — справочник застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS, topic_id, title_draft, slug, signal_urls.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
