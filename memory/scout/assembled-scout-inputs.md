# Scout inputs — 2026-09-03 (B22)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-03 (YEKT Wednesday slot 09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks
- **Closed newbuild plots (30d — DO NOT reuse):**
  - `newbuild_ddu_cellar_paid_not_handed_tyumen` — B21 кладовка по ДДУ
  - `newbuild_developer_legal_entity_change_ddu_escrow_tyumen` — B20 смена юрлица
  - `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` — B19 семейная ипотека/эскроу
  - `ddu_escrow_handover_delay_tyumen` — B12 перенос сдачи / эскроу заморозили
- **Live WP 2026-09-02 (avoid same plot):** рассрочка ДДУ остаток подняли; КП газ/вода; переуступка отказ; приёмка мокрая стяжка; бронь +380 тыс; траншевая ипотека ×8
- `scout_helper.py --check-query` PASS for proposed title + cluster `newbuild_ddu_area_mismatch_overpay_tyumen`
- `excalibur_blog_topic_focus.py` PASS (ДДУ/newbuild)

## Proposed topic (PASS all gates)

- **topic_id:** B22
- **title_draft:** В Тюмени площадь в ДДУ не сошлась с ключами — переплатили за метры
- **slug:** v-tyumeni-ploshchad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry
- **cluster_id (new):** newbuild_ddu_area_mismatch_overpay_tyumen
- **story_dup_check:** PASS — distinct from B21 (другое помещение/кладовка), B12 (срок сдачи), приёмка wet screed (дефекты стяжки), B20 (юрлицо); plot = в ДДУ указана одна площадь, по обмерам БТИ/акту приёмки меньше — переплата за «воздух», застройщик отказывает в перерасчёте

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке по ДДУ, цена привязана к площади в договоре
- **risk:** при приёмке обмеры показали меньшую площадь, чем в ДДУ (лоджия/общие зоны/округление) — переплата сотни тысяч рублей
- **time:** на приёмке квартиры / за 2 недели до подписания акта передачи
- **finale:** застройщик отказал в перерасчёте или предложил символическую скидку; семья не подписала акт / подписала под давлением срока ипотеки — потеряли деньги или отложили регистрацию
- **comment_magnet_angle:** «Площадь в ДДУ совпала с ключами — вы вообще сверяете метры до акта или верите цифрам в договоре?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild DDU area casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-03)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| площадь квартиры дду | 55+11176 | 11 (weak standalone) |
| площадь квартиры новостройка | 55+11176 | 7 (weak) |
| приемка квартиры в новостройке тюмень | 55+11176 | 35 |
| приемка новостроек тюмень | 55+11176 | 35 |
| **купить новостройку в тюмени** | **55+11176** | **857** |
| купить новостройку в тюмени | 225 (compare) | 1884 |
| новостройки тюмень купить от застройщика | 55+11176 | 528 |

**wordstat_rework log:**
- probe «площадь квартиры дду» 55+11176 → 11 (on-plot but weak P0)
- probe «площадь квартиры новостройка» 55+11176 → 7 (weak)
- probe «приемка квартиры в новостройке тюмень» 55+11176 → 35 (secondary local)
- **rework:** buyer jargon newbuild Tyumen → **final P0 «купить новостройку в тюмени» regions 55,11176 freq 857** (compare RU225 1884); on-plot secondary «приемка квартиры в новостройке тюмень» 35

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_116964/ — ГрК РФ / требования к площади в проектной документации
- https://www.gosuslugi.ru/help/faq/dom/100361 — приёмка квартиры в новостройке
- https://dzen.ru/holyslav — контекст новостроек Тюмени
- {{SITE_BASE}}/blog/
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B22, title, slug, signal_urls, research angles for Research role.
