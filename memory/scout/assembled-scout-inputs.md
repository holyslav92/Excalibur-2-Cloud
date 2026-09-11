# Scout inputs — 2026-09-11 (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-11 (YEKT Friday slot ~15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 25 active locks (sync 2026-09-11)
- **Live WP 2026-09-08..2026-09-11 — DO NOT reuse plot:**
  - застройщик снял субсидию за 3 дня до ДДУ — бронь сгорела
  - рассрочку просрочили на 4 дня — квартира ушла
  - запрет аренды до ключей в ДДУ — инвестор потерял 2 жильцов
  - ДДУ на дом — в выписке не хватило 1,5 сотки
  - трейд-ин занизили на 1,2 млн — сорвался перед ДДУ
  - в ДДУ обещали чистовую — отдали предчистовую
  - бронь сгорела — цена +450 тыс
  - пропал балкон из планировки — банк заморозил транш
  - застройщик год не платил неустойку — семья остановила приёмку
  - ребёнку 7 лет — семейную ипотеку пересчитали перед ДДУ
  - банк остановил транш после приёмки без замечаний
  - ключи без разрешения на ввод — банк заморозил ипотеку
- **Last 3 published formula:** бронь / ДДУ / застройщик — proposed topic uses **переуступка** (different mechanism)
- **Rejected overlap:** расторжение ДДУ / эскроу freeze → близко к B12 (сдвиг сдачи + эскроу) и B19/B20 escrow clusters
- **Rejected overlap:** машино-место по ДДУ → 47% overlap B21 cellar/parking cluster
- **Rejected overlap:** оценка банка ниже ДДУ → covered on live WP 2026-09-05
- **Rejected overlap:** переуступка +280к цена за сутки → другой plot (price hike, not object lost); our plot = **другой покупатель забрал объект**

## Proposed topic (PASS topic_focus + story_dup — pending scout_helper)

- **topic_id:** B24
- **title_draft:** В Тюмени согласовали переуступку — за сутки до аванса квартиру продали другому
- **slug:** v-tyumeni-soglasovali-pereustupku-za-sutki-do-avansa-kvartiru-prodali-drugomu
- **cluster_id (new):** assignment_lost_to_faster_buyer_tyumen
- **story_dup_check:** PASS — distinct plot: покупатель в Тюмени согласовал переуступку по новостройке (договор уступки, согласие застройщика, аванс готовился), за сутки до внесения аванса застройщик сообщил, что квартира уже у другого дольщика — бронь/уступку сняли, объект ушёл более быстрому покупателю

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени нашла переуступку в строящемся ЖК, согласовала с застройщиком и продавцом-уступщиком, готовила аванс и ипотеку
- **risk:** за сутки до перевода аванса застройщик сообщил, что квартира уже закреплена за другим покупателем — переуступка сорвана, аванс не внесли, планировка ушла
- **time:** за 24 часа до запланированного внесения аванса по договору переуступки
- **finale:** уступщик вернул задаток (или спор о удержании), застройщик отказал в повторном закреплении той же квартиры; семья успела взять другую планировку в том же ЖК, но дороже на 280 тысяч — или ушла без объекта (финал: объект потерян, деньги на руках, сроки сорваны)
- **comment_magnet_angle:** «Переуступку согласовали, аванс готовили — а квартиру продали другому за сутки: вы бы винили уступщика, застройщика или себя за паузу?»

## Top-energy + newbuild lock

- **top_energy_mirror:** someone_else_took_object
- **newbuild_mechanism:** переуступка прав по ДДУ — другой покупатель обогнал и забрал квартиру до аванса
- **why_newbuild_not_secondary:** сделка по переуступке в строящемся ЖК (ДДУ, согласие застройщика, этап до ключей) — не вторичка и не ЕГРН-продавец

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild assignment casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-11)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройка | 55+11176 | 16 |
| переуступка квартиры в новостройке риски | 55+11176 | 2 |
| договор переуступки новостройка | 55+11176 | 1 |
| расторжение дду | 55+11176 | 110 (rejected — escrow/B12 overlap risk) |
| приемка квартиры в новостройке тюмень | 55+11176 | 30 (rejected — live bank tranche after acceptance) |
| машиноместо дду | 55+11176 | 1 (rejected — B21 cellar overlap) |
| **новостройки тюмень** | **55+11176** | **4583** |
| **новостройки тюмень** | **225 (compare)** | **8705** (from prior probe pattern) |
| **переуступка новостройка** | **225 (compare)** | use child «переуступка новостройки» from RU if needed |

**wordstat_rework log:**
- probe «переуступка новостройка» 55+11176 → 16 (on-topic newbuild buyer spine)
- probe «договор переуступки новостройка» → 1 (too narrow)
- probe «расторжение дду» → 110 (stronger freq but rejected plot overlap escrow/delay clusters)
- probe «приемка квартиры в новостройке тюмень» → 30 (rejected — acceptance/tranche live plot)
- **rework:** anchor Tyumen newbuild demand spine «новостройки тюмень» 4583 + mechanism phrase «переуступка новостройки» 16 → **final P0 «переуступка новостройки» regions 55,11176,compare225 freq 16 (Tyumen) / compare RU child cluster**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_122165/ — 214-ФЗ, переуступка прав требований по ДДУ
- https://www.domrf.ru/ — справочник застройщиков / ДДУ
- https://t.me/klyshin_A — checked, not used this slot
- {{PUBLIC_SITE_URL}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
