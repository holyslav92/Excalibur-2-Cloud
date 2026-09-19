# Scout inputs — 2026-09-19 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-19 (YEKT Saturday slot 09:00 — weekend automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO cottage KP kadastr boundary 1.8m (2026-09-18 live)
- NO BTI area 4.2 sqm less than DDU (2026-09-18 live)
- NO assignment 28 days lost to another buyer (2026-09-18 live)
- NO mortgage approval expired day 87 (2026-09-18 live)
- NO matkapital child shares day 47 (2026-09-17 live)
- NO DDU appendix rental ban investor (2026-09-17 live)
- NO different building/corpus 10 days before DDU (2026-09-17 live)
- NO bank appraisal 900k lower (cluster bank_appraisal_below_ddu_price locked)
- NO parking spot missing in declaration (2026-09-16 live)
- NO insurance 186k before DDU (2026-09-16 live)
- NO keys 9 months late penalty unpaid (cluster keys_delay_penalty_unpaid locked)
- NO co-borrower refused family mortgage (2026-09-16 live)
- NO B26 RVE delay blocks tranche (published 2026-09-13)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots
- NO heavy «эскроу не открыл» phrasing — fingerprint overlaps ddu_amount_vs_escrow_zero cluster

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-19)
- Live WP recent (~12): cottage kadastr 1.8m, BTI -4.2 sqm, assignment 28d, ipoteka day 87, matkapital day 47, rental ban appendix, other corpus 10d, bank appraisal -900k, parking declaration, insurance 186k, keys 9mo penalty, co-borrower family mortgage
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug (fingerprint booking_expired — distinct from booking_expired_price_hike price-hike plot)
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени в проектной декларации земля под ЖК в аренде — в брони обещали собственность, за 4 дня до ДДУ отказались
- **slug:** v-tyumeni-v-deklaracii-zemlya-v-arende-semja-otkazalas-do-ddu
- **cluster_id (new):** newbuild_land_lease_not_ownership_declaration_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** В офисе продаж и брони зафиксировали «земля в собственности застройщика»; на dom.rf в проектной декларации участок под корпусом — **государственная аренда до 2049**, не собственность. Семья с детьми + инвестор под семейную ипотеку сверили декларацию за 4 дня до подписания ДДУ → отказались, бронь сняли, деньги на счёт не переводили
- **why_newbuild_not_secondary:** Риск только в цепочке долевого строительства: проектная декларация застройщика по 214-ФЗ, ДДУ, бронь в ЖК. Нет продавца вторички, ЕГРН-квартиры, наследников, бабушки или опеки
- **story_dup_check:** PASS — distinct from parking/машино-место in declaration (2026-09-16), developer legal entity change (B20), escrow zero (B12 cluster), different corpus (2026-09-17), cottage kadastr (KP other plot)

## Dzen news-casus shape (target PASS)

- **event:** семья с двумя детьми и инвестор смотрели двушку в новостройке Тюмени; менеджер в офисе продаж показал план благоустройства и сказал, что «участок наш, в собственности»
- **risk:** аренда земли у города/региона — при смене арендатора/расторжении аренды статус дома и ипотека под вопросом; банк при проверке декларации может отказать в семейной ипотеке или потребовать допсоглашение
- **time:** за 4 дня до назначенного подписания ДДУ; вечером перед визитом в банк открыли dom.rf
- **finale:** в декларации — «право аренды земельного участка», срок до 2049; семья отказалась от ДДУ, застройщик предложил «подписать как есть — потом переоформят», отказали; бронь 150 тысяч вернули за 12 дней, на сделку не вышли
- **comment_magnet_angle:** «Если под домом не собственность, а аренда до 2049 — вы бы всё равно подписали ДДУ, если менеджер клянётся, что „переоформят потом“?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild declaration land-tenure casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-19)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4446 |
| купить новостройку в тюмени | 55,11176 | 923 |
| купить новостройку в тюмени | 225 (compare) | 1936 |
| новостройки в тюмени от застройщика | 55,11176 | 656 |
| проектная декларация застройщика | 55,11176 | 25 |
| проектная декларация застройщика | 225 (compare) | 1176 |
| дду эскроу | 55,11176 | 44 (weak; avoided in H1 — escrow cluster overlap) |
| земельный участок аренда застройщик | 55,11176 | 3 (too weak alone) |
| семейная ипотека новостройка | 55,11176 | 90 (context) |
| приемка новостройки тюмень | 55,11176 | 32 (blocked acceptance cluster) |

**wordstat_rework log:**
- probe «земельный участок аренда застройщик» 55,11176 → 3 (too weak for P0 alone)
- probe «проектная декларация застройщика» 55,11176 → 25 (mechanism-specific, weak)
- probe «дду эскроу» 55,11176 → 44 (weak + plot overlap risk)
- **rework:** anchor buyer spine «новостройки тюмень» + mechanism in H1/body, not weak tail alone
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4446 (55+11176) / context RU buyer «купить новостройку в тюмени» 1936 (225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации (право на земельный участок)
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, проектная декларация
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
