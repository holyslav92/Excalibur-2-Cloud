# Scout inputs — 2026-09-16 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-16 (YEKT weekday slot)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO keys_delay_penalty_unpaid / неустойка за просрочку ключей (LIVE 2026-09-16)
- NO acceptance_defects_penalty / «акт не подписали» на приёмке квартиры (LIVE-V-TYUMENI-NOVOSTROJKU-VY, B25)
- NO KP plot 12 vs 9 sotok with act refusal — fingerprint overlap with acceptance cluster (tested BLOCKER)
- NO assignment_lost / переуступка зависла (LIVE-V-TYUMENI-ZASTROJSCHIK-N)
- NO DDU layout shrink treshka→dvushka (LIVE-V-TYUMENI-V-DDU-ZAFIKSIR)
- NO frozen clusters in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 29 active locks (last_sync 2026-09-16)
- Live WP recent (~20): keys+penalty unpaid, bank refused co-borrower family mortgage, bron vs DDU section, assignment 350k stuck, KP gas no act, bank removed accreditation, price hike before DDU, parents acceptance defects, price fixation failed, matkapital child 7y, treshka→dvushka, double booking same apt
- `shared/published-titles.md` + ledger read — B26 RVE+tranche published; B25 finishing; B23 apartamenty
- **Rejected:** newbuild_kp_plot_area_mismatch_tyumen with «акт не подписали» — SCOUT ANTI-DUPE HARD (acceptance_defects_penalty)
- **Rejected:** investor_assignment_vs_rent — H1 fingerprint assignment_lost dup LIVE-V-TYUMENI-ZASTROJSCHIK-N
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли
- **slug:** v-tyumeni-za-sutki-do-ddu-vsplyla-strahovka-186-tysyach-do-eskrou-ne-doshli
- **cluster_id (new):** hidden_insurance_rider_before_ddu_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** Семья готовилась к подписанию ДДУ на квартиру в новостройке; за **24 часа** до визита в банк менеджер выложил **допсоглашение** с обязательным пакетом страхования жизни/имущества на **186 000 ₽**, которого не было в расчёте ипотеки и брони → платёж и первый взнос «раздулись» → семья **остановила сделку до открытия эскроу**, бронь сгорела
- **why_newbuild_not_secondary:** цепочка бронь → одобрение ипотеки → ДДУ → эскроу у застройщика; нет продавца-физлица, ЕГРН-вторички, наследников или опеки
- **story_dup_check:** PASS — distinct from mortgage_rate_hike_before_ddu (ставка), ddu_amount_vs_escrow_zero (сумма на эскроу), installment_penalty_developer (рассрочка), trade_in, accreditation removal, co-borrower refusal

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в ЖК, банк одобрил ипотеку, назначили дату подписания ДДУ и открытия эскроу
- **risk:** скрытый обязательный страховой пакет в допсоглашении увеличивает входной платёж; отказ = срыв срока брони / повторная заявка
- **time:** за **сутки** до подписания ДДУ, вечером в чате с менеджером офиса продаж
- **finale:** допсоглашение не подписали, на эскроу деньги не ушли, бронь аннулировали через 48 часов; застройщик предложил «оформить страховку у партнёра» — семья отказалась и пересчитала бюджет с риэлтором
- **comment_magnet_angle:** «Страховку на 186 тысяч вынесли в допсоглашение накануне ДДУ — вы бы доплатили ради квартиры или развернулись, даже если бронь сгорит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-16)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

**Note:** `wordstat_get_top_requests` returned transient API 499 on this run; frequencies below are live **`wordstat_get_dynamics`** monthly shows (PERIOD_MONTHLY, Aug 2026) — not invented.

| probe | regions | freq (Aug 2026 monthly shows) |
|-------|---------|-------------------------------|
| страхование ипотеки тюмень | 55,11176 | 29 (weak) |
| дду тюмень | 55,11176 | 19 (weak) |
| дду новостройка тюмень | 55,11176 | N/A |
| купить квартиру в новостройке тюмень | 55,11176 | 676 (Jul; Aug combined w/225: 1453) |
| **новостройки тюмень** | **55,11176** | **4802** |
| **новостройки тюмень** | **225 (compare)** | **8947** |

**wordstat_rework log:**
- probe «страхование ипотеки тюмень» 55,11176 → 29 (weak; insurance tail only)
- probe «дду тюмень» 55,11176 → 19 (weak)
- rework: localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, эскроу, ипотека) keeping hidden-rider casus shape
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4802 (55+11176) / 8947 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, права дольщиков
- https://www.cbr.ru/finmarkets/supervision/svps/ — требования банков к страхованию ипотеки (контекст)
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Required handoff fields (emit all)

wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat, story_dup_check, h1_fingerprint_check, formula_spam_check, anti_dupe_hard, topic_id, title_draft, slug, cluster_id, signal_urls
