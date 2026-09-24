# Scout inputs — 2026-09-24 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-24 (YEKT weekday slot ~09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — conductor read shared/dzen-content-rules.md + shared/rf-blocked-entities.json

## Slot constraints (HARD FORBIDDEN)

- NO frozen/locked clusters in memory/scout/used-clusters.json (30d) — see sync 2026-09-24 (26 locks)
- NO recent WP Sep 21–23 plots: family mortgage child 7, KP forest fence, furniture package, co-borrower escrow freeze, ceiling 2.68m, windows to road, delivery shift declaration, cellar separate DDU, down payment 15→25%, terrace missing, UK 180k, house -14sqm, etc.
- NO formula spam skeleton clone of last 3 ledger (B30 переуступка запрет, B31 страховка+одобрение, B32 чужое юрлицо эскроу) without new mechanism
- NO secondary retitle (бабушка, банкрот продавца, прописанные, ЕГРН-вторичка, опека…)
- NO acceptance-defects / «акт приёмки не подписали» cluster (acceptance_defects_penalty locked — school-shift-at-keys rejected for dup)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 26 active locks (last_sync 2026-09-24)
- Live blog fetch attempted (PUBLIC_SITE_URL/blog/) — footer-only h2 in HTML scrape; rely on EXCALIBUR_RECENT_WP_POSTS + published-titles.md (~20)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир/новострой)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B33
- **title_draft:** В Тюмени в брони новостройки продали квартиру на 14-м этаже — в проектной декларации лифт только до 12-го, семья остановила ДДУ
- **slug:** v-broni-novostrojki-14-etazh-lift-tolko-do-12-semya-ostanovila-ddu-tyumen
- **article_dir:** memory/blog/articles/B33-v-broni-novostrojki-14-etazh-lift-tolko-do-12-semya-ostanovila-ddu-tyumen
- **cluster_id (new):** newbuild_elevator_serves_fewer_floors_than_unit_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья с двумя детьми и одобренной ипотекой бронирует квартиру на 14-м этаже ЖК в Тюмени («вид», тишина). Перед подписанием ДДУ сверяют проектную декларацию на dom.rf и поэтажные планы: **пассажирский лифт обслуживает этажи 1–12**, технический — без доступа жильцам. Квартира на 14-м в ДДУ числится, но ежедневный сценарий — пешком с коляской и сумками с 12-го. Менеджер ссылается на «премиум высоту» в брони; в декларации этажность корпуса и лифтовая группа не совпадают с обещанием. Семья останавливает ДДУ до эскроу
- **why_newbuild_not_secondary:** Риск только в цепочке первички: бронь застройщика, проектная декларация 214-ФЗ, ДДУ на квартиру в строящемся ЖК, ипотека/эскроу. Нет продавца вторички, осмотра с бабушкой, долей, наследников, прописанных или «чистой ЕГРН» вторичного рынка
- **story_dup_check:** PASS — distinct from booking_expired_price_hike (секция/цена 48ч), ddu_apartment_vs_apartments, show-room ceiling 2.68m (экспликация площади, не лифт), windows-to-road (ориентация фасада), acceptance_defects_penalty (дефекты на приёмке), B26 РВЭ/транш

## Dzen news-casus shape (target PASS)

- **event:** семья бронирует «высокий» лот на 14-м в новостройке Тюмени; в шоу-руме показывают панораму с высоты
- **risk:** ежедневная жизнь с детьми без лифта до 14-го; при ипотеке банк может оспорить соответствие объекта заявленным характеристикам; переплата за «высоту» без сервиса лифта
- **time:** за несколько дней до визита в банк на подписание ДДУ и открытие эскроу; вечером сверили декларацию и планы
- **finale:** в декларации лифт до 12-го; застройщик предлагает «подпишите, лифт достроят» или «ходите по лестнице»; семья отказывается от ДДУ, бронь частично удержана, на эскроу не вышли
- **comment_magnet_angle:** «Купили бы квартиру на 14-м, если лифт официально только до 12-го, а в брони писали “вид с высоты”?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild elevator/declaration casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-24)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4339 |
| новостройки тюмень | 225 (compare) | 8207 |
| купить новостройку в тюмени | 55,11176 | 898 |
| новостройки в тюмени от застройщика | 55,11176 | 631 |
| дду тюмень | 55,11176 | 22 |
| проектная декларация застройщика | 55,11176 | 24 |
| приемка квартиры в новостройке тюмень | 55,11176 | 27 |
| жк новостройки тюмень | 55,11176 | 169 |
| эскроу новостройка тюмень | 55,11176 | API empty (treat as weak) |
| школа при новостройке | 55,11176 | API empty (alternate angle rejected) |

**wordstat_rework log:**
- probe «школа при новостройке» 55,11176 → empty (rejected school-at-keys angle — also dup risk with acceptance cluster)
- probe «эскроу новостройка тюмень» 55,11176 → empty/<5 (too weak for P0)
- probe «проектная декларация застройщика» 55,11176 → 24 (mechanism jargon, weak vs spine)
- probe «приемка квартиры в новостройке тюмень» 55,11176 → 27 (weak; overlaps acceptance cluster tone)
- **rework:** anchor buyer demand spine «новостройки тюмень» + H1 localizes ЖК/ДДУ/14 этаж/лифт/декларация
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4339 (55+11176) / 8207 (225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — проектные декларации, лифтовое оборудование, этажность
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, проектная декларация
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Gates already PASS (conductor)

- h1_fingerprint_check: PASS | fingerprint: elevator_12_floors_unit_14
- formula_spam_check: PASS | last3_mechanisms: B30 assignment_resale_ban_3y, B31 insurance_payment_approval_revoked, B32 escrow_wrong_legal_entity (all «за N дней до ДДУ» — this plot is бронь+декларация+лифт, stopped before escrow)
- anti_dupe_hard: PASS

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir, signal_urls, research angles for Research role.
