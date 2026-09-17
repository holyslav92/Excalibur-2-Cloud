# Scout inputs — 2026-09-17 (B27, slot ~12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-17 (YEKT weekday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — today's live + 30d locks)

Do NOT reuse these recent live plots (2026-09-15..17):
- bank appraisal below DDU / bank cut credit (bank_appraisal_below_ddu_price)
- parking spot not in declaration (3 days before DDU)
- insurance 186k surfaced before DDU
- keys delayed 9 months + unpaid penalty (keys_delay_penalty_unpaid)
- co-borrower refused family mortgage before escrow
- booking vs DDU section/floor/view mismatch (booking_expired_price_hike / ddu_apartment_vs_apartments_mismatch)
- assignment not approved + 350k advance stuck
- KP house keys without gas on plot
- bank removed ЖК accreditation before DDU
- price hike / price fix failed before DDU
- acceptance for parents failed (acceptance_defects_penalty)
- mortgage approval expired + rate recalc (BLOCKED: overlaps mortgage_rate_hike_before_ddu fingerprint)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-17)
- Live WP ~20 titles fetched via wordpress_get_posts (2026-09-17 newest: bank appraisal; 09-16: parking declaration, insurance, keys delay, co-borrower; 09-15: booking/section, assignment, KP gas, accreditation, price hike, acceptance, price fix; 09-14: matkapital 7y, 3-room→2-room, double booking, area 54→52; 09-13: KP plot 12→9.7, RVE B26, finishing B25, parking double-sold)
- ledger: B26 RVE+tranche, B25 finishing, B23 apartments, B22 rate hike, B21 cellar, B20 legal entity change
- **Rejected:** mortgage approval expired before escrow — SCOUT ANTI-DUPE HARD BLOCKER (story_duplicate mortgage_rate_hike_before_ddu + H1 fingerprint amount:escrow_blocked vs LIVE-V-TYUMENI-ZA-SUTKI-DO-DD insurance post)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: сделк)
- `story_dup.py --text` PASS (fingerprint + formula spam OK)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени за 10 дней до ДДУ перенесли в другой корпус — этаж и вид не совпали, сделку остановили
- **slug:** v-tyumeni-pered-ddu-perenesli-v-drugoj-korpus-etazh-i-vid-ne-sovpali
- **cluster_id (new):** developer_corps_transfer_before_ddu_tyumen
- **top_energy_mirror:** someone_else_took_object (+ paper_clean_then_broke on booking vs DDU object)
- **newbuild_mechanism:** семья держала бронь в корпусе А (этаж 14, вид на парк); за 10 дней до подписания ДДУ застройщик сообщил, что корпус А «заморожен», предлагают только корпус Б — этаж 6, вид на стройплощадку; в проекте ДДУ другой адрес/корпус, площадь −1,2 м²; банк и семья остановили сделку до эскроу
- **why_newbuild_not_secondary:** сюжет целиком в цепочке бронь → выбор лота в ЖК → проект ДДУ → эскроу; нет продавца вторички, ЕГРН, наследников, бабушки или банкротства продавца
- **story_dup_check:** PASS — distinct from booking_expired_price_hike (48h section mismatch, stayed on object), ddu_apartment_vs_apartments_mismatch (apartments vs квартира), trade_in_rejected, price hike/fix, bank appraisal, parking/insurance pre-DDU angles

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени полгода выбирала новостройку, внесла бронь 200 тыс., получила одобрение семейной ипотеки под конкретный корпус и лот
- **risk:** подмена объекта в ДДУ — другой корпус, этаж ниже, вид хуже, площадь меньше; при подписании «как есть» теряют право на первоначальный лот и фиксированную цену
- **time:** за 10 дней до назначенного подписания ДДУ; за 2 дня до открытия эскроу
- **finale:** семья отказалась подписывать ДДУ с новым корпусом; застройщик предложил вернуть бронь «в течение 45 дней» без неустойки; банк снял резерв по ипотеке; сделку остановили — до эскроу не дошли, второй вариант квартиры в том же ЖК уже разобрали
- **comment_magnet_angle:** «Бронь была на 14-й этаж с видом, в ДДУ дали 6-й на стройку: это законная „замена корпуса“ или подмена объекта, за которую надо было уходить сразу?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild corpus-transfer casus without Klyshin; no @klyshin_A signal used)

## Wordstat MCP-KV (live 2026-09-17)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4480 |
| новостройки тюмень | 225 (compare) | 8444 |
| купить новостройку в тюмени | 55,11176 | 928 |
| квартиры в тюмени новостройки | 55,11176 | 1137 |
| приемка квартиры в новостройке тюмень | 55,11176 | 34 (weak; acceptance cluster taken) |
| срок одобрения ипотеки | 55,11176 | 15 (weak; mortgage expiry angle BLOCKED) |
| бронь новостройка тюмень | 55,11176 | 0 (no data) |
| дду новостройка тюмень | 55,11176 | API empty |

**wordstat_rework log:**
- probe «бронь новостройка тюмень» 55,11176 → 0 (no volume; keep casus, rework phrasing)
- probe «срок одобрения ипотеки» 55,11176 → 15 (weak; angle blocked by anti-dupe)
- probe «приемка квартиры в новостройке тюмень» → 34 (weak; B25/acceptance clusters taken)
- **rework:** localize Tyumen newbuild buyer spine → **final P0 «купить новостройку в тюмени» regions 55,11176,compare225 freq 928 (55+11176) / 1973 (RU225 via «купить новостройку в тюмени» on 225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, права дольщиков, замена объекта
- https://www.domrf.ru/ — проектные декларации, реестр застройщиков
- https://t.me/klyshin_A — checked 2026-09-17, not used (no fresh newbuild corpus-transfer hook)
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
