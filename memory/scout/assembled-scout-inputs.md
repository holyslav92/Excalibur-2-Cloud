# Scout inputs — 2026-09-14 (B27, slot ~15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-14 (YEKT weekday slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO double booking same unit (published 2026-09-14: две брони на одну квартиру, 180 тыс.)
- NO DDU area/sqm mismatch at приёмке (published 2026-09-14: 54 м² в ДДУ → −2 м² на приёмке)
- NO keys_delay_penalty_unpaid / неустойка за просрочку сдачи — H1 fingerprint duplicate LIVE-V-TYUMENI-ZASTROJSCHIK-P (2026-09-12)
- NO parking/машино-место/кладовка double-sold, NO RVE+tranche (B26), NO clean finish mismatch (B25), NO KP plot 12→9.7 соток
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-14)
- Live WP recent (~12): double booking 180k, area −2 sqm, KP 12→9.7 соток, RVE+tranche 520k, parking P-42, B25 finishing, assignment 7d, transh +480k, escrow zero DDU, subsidized mortgage 3d, trade-in, bank appraisal −680k, family mortgage recalc Oct 1
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду, эскроу, застройщик)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени в ДДУ зафиксировали трёшку — перед эскроу застройщик предложил двушку, семья остановила сделку
- **slug:** v-tyumeni-v-ddu-treshku-pered-eskrou-zastrojschik-predlozhil-dvushku
- **article_dir:** memory/blog/articles/B27-v-tyumeni-v-ddu-treshku-pered-eskrou-zastrojschik-predlozhil-dvushku
- **cluster_id (new):** newbuild_layout_changed_before_escrow_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** В ДДУ и приложении зафиксирована конкретная планировка (3-комнатная, этаж, площадь). За день до подписания заявления на **эскроу** менеджер застройщика предлагает **другую** квартиру (2-комнатная, меньше метраж) «по той же цене» — семья отказывается, **бронь снимают**, на эскроу деньги не уходят, но сгорает окно одобрения ипотеки
- **why_newbuild_not_secondary:** сюжет целиком в цепочке бронь → ДДУ → эскроу → застройщик; нет продавца вторички, ЕГРН-вторички, наследников, бабушки или опеки
- **story_dup_check:** PASS — distinct from area mismatch at приёмке (today), double booking (today), B23 apartamenty, B25 finishing, escrow zero, subsidized 3d (booking_expired overlap if «3 дня» in title — avoid)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала трёшку в новостройке, подписала ДДУ с приложением-планировкой
- **risk:** перед эскроу застройщик меняет объект на меньшую планировку без снижения цены в договоре
- **time:** накануне подписания заявления на открытие эскроу-счёта (после одобрения ипотеки)
- **finale:** семья отказалась подписывать эскроу на «двушку»; застройщик снял бронь; лот ушёл другому покупателю; деньги на эскроу не поступили, но одобрение ипотеки истекло через 19 дней
- **comment_magnet_angle:** «В ДДУ уже записана „трёшка“, а перед эскроу вам подсовывают „двушку“ за ту же цену: вы бы подписали эскроу или сняли бронь, даже если одобрение ипотеки сгорит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild layout-swap casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-14)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| неустойка застройщик просрочка сдачи | 55,11176,225 | 295 (rejected — fingerprint dup keys_delay_penalty live) |
| планировка квартира новостройка | 55,11176,225 | 1825 |
| планировки квартир новостройка | 55,11176,225 | 1825 |
| планировки квартир новостройка | 225 (compare) | 1825 |
| новостройки тюмень купить | 55,11176,225 | 2410 (context spine) |
| купить новостройку в тюмени | 55,11176,225 | 1918 |
| дду новостройка тюмень | 55,11176,225 | weak/empty |
| эскроу новостройка тюмень | 55,11176,225 | weak/empty |

**wordstat_rework log:**
- probe «неустойка застройщик просрочка сдачи» 55,11176 → 295 (strong but plot blocked by fingerprint dup)
- probe «дду новостройка тюмень» / «эскроу новостройка тюмень» → weak/empty
- rework: buyer jargon планировка + новостройка + ДДУ/эскроу angle → **final P0 «планировки квартир новостройка» regions 55,11176,compare225 freq 1825**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, права дольщиков
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
topic_id, title_draft, slug, article_dir, wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
