# Scout inputs — 2026-09-04 (B23, 12:00 YEKT slot)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-04 (YEKT Friday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-04)
- **Recent newbuild live WP Sep 1–4 (DO NOT reuse plot):**
  - wrong escrow account transfer (2026-09-04)
  - bank raised mortgage rate before DDU (B22 published 2026-09-04)
  - developer demanded sign act with defects (2026-09-04)
  - bank withdrew mortgage approval 72h before DDU (2026-09-03)
  - clean finish shown but DDU had pre-finish (2026-09-03)
  - keys delayed 8 months — penalty as certificate (2026-09-03)
  - area mismatch DDU vs keys (2026-09-03)
  - installment DDU balance raised before delivery (2026-09-02)
  - KP without gas/water on keys (2026-09-02) — **distinct:** utilities, not land category
  - assignment paid but developer refused re-registration (2026-09-02)
  - cellar paid not in DDU keys (B21)
  - developer legal entity change escrow (B20)
  - family mortgage approved escrow not opened (B19)
- **Rejected angles this slot:**
  - parking/mashinomesto in DDU → scout_helper overlap 40% with B21 cellar cluster
  - double sale same apartment → overlap with LIVE-V-TYUMENI-KVARTIRU-PRODA (sold twice)
  - mortgage rate before DDU → B22 published today
- **Closed clusters (30d):** B21 newbuild_ddu_cellar_paid_not_handed_tyumen; B20 newbuild_developer_legal_entity_change_ddu_escrow_tyumen; B19 family mortgage escrow; all frozen secondary in used-clusters.json
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дом)
- `excalibur_blog_scout_story_dup.py --text` PASS (30d)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B23
- **title_draft:** В Тюмени купили дом в коттеджном посёлке — категория земли не для жилья
- **slug:** v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya
- **cluster_id (new):** newbuild_kp_land_category_wrong_for_housing_tyumen
- **story_dup_check:** PASS — distinct from Sep 2 KP gas/water (utilities plot); distinct from B21 cellar; plot = семья купила дом по ДДУ в КП под ИЖС/жильё, на этапе регистрации/ключей выписка ЕГРН показала категорию земли не «земли населённых пунктов» (например с/х или промышленность) — банк остановил ипотеку, регистрацию права собственности отказали, ключи не передали

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала готовый/строящийся дом в коттеджном посёлке, подписала ДДУ, внесла деньги на эскроу, банк одобрил ипотеку под ИЖС
- **risk:** в выписке ЕГРН на участок категория земли не подходит для постоянного проживания / ИЖС — застройщик обещал «жилой посёлок», а в документах другая категория или ВРИ не совпадает с домом
- **time:** за 2–4 недели до выдачи ключей, когда юрист запросил свежую выписку на участок перед регистрацией
- **finale:** банк приостановил выдачу ипотеки, Росреестр отказал в регистрации; семья отказалась подписывать акт приёма-передачи дома; деньги на эскроу заморожены, застройщик ссылается на «перевод категории в процессе» без сроков
- **comment_magnet_angle:** «В рекламе КП писали „ИЖС под ключ“, а в выписке — другая категория земли. Вы бы всё равно подписали акт, если дом уже построен?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP land-category casus without Klyshin — preferred; avoids B21 cellar pattern and Sep 2 utilities KP plot)

## Wordstat MCP-KV (live 2026-09-04)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55+11176 | 4683 (context only) |
| машиноместо тюмень | 55+11176 | 213 (rejected — scout_helper overlap B21 cellar) |
| парковочное место новостройка | 55+11176 | 4 (rejected — weak + B21 overlap) |
| умный дом квартира | 55+11176 | 40 (rejected — weak volume) |
| субсидия на ипотеку | 55+11176 | 62 (rejected — subsidy revocation = different plot, weaker KP tie) |
| категории земельных участков | 55+11176 | 125 (legal spine, lower than KP demand) |
| **коттеджные поселки тюмень** | **55+11176** | **1832** |
| коттеджные поселки тюмень | 225 (compare) | 2930 |
| купить дом в тюмени | 55+11176 | 11544 (too broad, loses KP land-risk spine) |

**wordstat_rework log:**
- probe «машиноместо тюмень» 55+11176 → 213 (strong but parking/cellar cluster overlap B21 — FAIL scout_helper)
- probe «категории земельных участков» 55+11176 → 125 (legal angle OK but weaker buyer demand)
- probe «умный дом квартира» 55+11176 → 40 (weak; smart-home plot unused but low volume)
- probe «субсидия на ипотеку» 55+11176 → 62 (mortgage subsidy plot distinct but weaker KP localization)
- probe «коттеджный поселок тюмень» 55+11176 → 1832; compare RU225 → 2930
- **rework:** localize Tyumen KP buyer jargon (коттеджный посёлок, ИЖС, категория земли) → **final P0 «коттеджные поселки тюмень» regions 55,11176 freq 1832** (compare RU225 2930)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст покупки домов/КП в Тюмени; не дубль кластера
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B23, title, slug, signal_urls, research angles for Research role.
