# Scout inputs — 2026-09-12 slot 15:00 YEKT (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-12 (YEKT Saturday slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{SITE_BASE}})
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → last_sync 2026-09-12
- **Live TODAY 2026-09-12 — DO NOT reuse mechanism/H1:**
  - slot 09: extra meters / доплата 420 тыс / keys withheld (WP 10109)
  - slot 12: acceptance_defects cottage / мотивированный отказ 850 тыс (WP 10137)
  - also live today: escrow shortfall 4,2 млн vs zero on escrow; family mortgage recalc 19 days before Oct 1
- **Rejected overlap:** bank appraisal below DDU → 42% overlap with today's family mortgage recalc slot
- **Rejected overlap:** booking expired registration delay → cluster booking_expired_price_hike locked
- **Rejected overlap:** assignment markup → 50% overlap with 2026-09-11 pereustupka slot
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS
- `excalibur_blog_scout_story_dup.py` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени застройщик забрал скидку за досрочный платёж по рассрочке — семья переплатила 320 тысяч
- **slug:** v-tyumeni-zastrojschik-zabral-skidku-za-dosrochnyj-platezh-semya-pereplatila-320
- **cluster_id (new):** installment_early_pay_discount_clawback_tyumen
- **top_energy_mirror:** number_in_claim_vs_zero_paid
- **newbuild_mechanism:** рассрочка от застройщика на новостройку — в договоре скидка за досрочное погашение транша; семья внесла платёж раньше срока, застройщик пересчитал график и **забрал скидку** (clawback), итоговая сумма в ДДУ выросла на 320 тыс — остановили перед финальным траншем
- **why_newbuild_not_secondary:** сюжет только про рассрочку/ДДУ с застройщиком на квартиру в ЖК, не про продавца вторички; деньги и спор — в цепочке новостройка→застройщик→банк
- **story_dup_check:** PASS — distinct from installment_penalty_developer (4-day late payment, apartment lost) and from today's escrow/extra-meters/acceptance/family-mortgage plots

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени взяла квартиру в новостройке в рассрочку от застройщика со скидкой 320 тыс при досрочном внесении очередного платежа
- **risk:** после досрочного платежа застройщик ссылается на пункт договора о пересчёте скидки — «скидка действует только при соблюдении графика», досрочный платёж трактуется как нарушение условий акции; сумма к доплате 320 тыс перед подписанием финального акта/транша
- **time:** за 5–7 дней до очередного транша / перед выходом на регистрацию ДДУ в банке
- **finale:** семья остановила подписание, запросила переписку и актуальный график; застройщик предложил вернуть скидку только при отказе от досрочного платежа (возврат денег 2–3 недели) — семья выбрала форк: не подписывать допсоглашение, уйти к другому корпусу/застройщику с проверкой пункта о скидке **до** брони
- **comment_magnet_angle:** «Если в рассрочке скидка за досрочный платёж, а застройщик потом её забирает — вы бы доплатили 320 тысяч или рвали договор, даже если квартира уже «ваша на бумаге»?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild installment clawback without Klyshin)

## Wordstat MCP-KV (live 2026-09-12)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| оценка банка новостройка | 55 | 3 (weak) |
| ипотека новостройка тюмень | 55 | 208 |
| квартиры в тюмени новостройка ипотека | 55 | 102 |
| **рассрочка от застройщика тюмень** | **55,11176** | **127** |
| рассрочка на квартиру от застройщика тюмень | 55 | 21 |
| ипотека новостройка | 225 (compare) | 36667 |
| новостройки тюмень | 55 | (context buyer spine) |

**wordstat_rework log:**
- probe «оценка банка новостройка» 55 → 3 (weak; overlap risk with today's family mortgage slot)
- probe «бронь новостройка тюмень» → MCP empty (retry skipped; booking cluster frozen)
- **rework:** localize Tyumen + newbuild buyer jargon (рассрочка, застройщик, ДДУ, новостройка) → **final P0 «рассрочка от застройщика тюмень» regions 55,11176,compare225 freq 127 (55)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ / ДДУ контекст
- https://www.domrf.ru/
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
