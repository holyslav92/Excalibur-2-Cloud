# Scout inputs — 2026-09-13 (B26)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-13 (YEKT Sunday slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO parking/машино-место/кладовка double-sold (B24 cluster: newbuild_parking_spot_double_sold_tyumen)
- NO DDU finishing vs acceptance mismatch (B25 cluster: acceptance_defects_penalty / newbuild_ddu_finishing_mismatch)
- NO same skeleton as last 3 pubs: B23 apartamenty, B24 parking, B25 finishing (all = DDU appendix vs fact)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-13)
- Live WP recent (last ~12): B25 finishing mismatch, B24 parking double-sold, B23 apartments, transhevaya +480k, installment penalty, escrow zero DDU, subsidized mortgage removed, trade-in, bank appraisal -680k, family mortgage recalc, cottage defects 850k, assignment lost 7 days
- **Rejected:** keys_delay_penalty_unpaid angle — H1 fingerprint duplicate LIVE-V-TYUMENI-ZASTROJSCHIK-P (2026-09-12)
- **Rejected:** KP plot 12 vs 9.7 sotok — valid but weaker engagement vs RVE+tranche; kept as backup cluster newbuild_kp_plot_area_mismatch_tyumen
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: новостройк, ипотек)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B26
- **title_draft:** В Тюмени новостройку сдали без разрешения на ввод — банк не дал второй транш на 520 тысяч
- **slug:** v-tyumeni-novostrojku-sdali-bez-razresheniya-na-vvod-bank-ne-dal-vtoroj-transh
- **cluster_id (new):** newbuild_rve_delay_blocks_mortgage_tranche_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** Дом визуально готов, застройщик зовёт на приёмку/ключи, но **разрешение на ввод в эксплуатацию (РВЭ)** в реестре не появилось 5 месяцев → при **траншевой ипотеке** банк не выдаёт **второй транш** (~520 тыс.) без зарегистрированного права/РВЭ → семья платит аренду + первый транш, не может оформить собственность
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ → сдача корпуса → РВЭ → регистрация дольщика → траншевая ипотека; нет продавца вторички, ЕГРН-вторички, наследников или бабушки
- **story_dup_check:** PASS — distinct from mortgage_rate_hike_before_ddu (ставка накануне ДДУ), LIVE-TRANSHEVAYA (рост суммы 2-го транша на 480к из-за ставки), B12 (перенос сдачи + эскроу), B25/B23/B24 (приложение ДДУ vs факт объекта)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке по ДДУ с траншевой ипотекой; корпус «сдали», пригласили на осмотр
- **risk:** без РВЭ нельзя зарегистрировать право → банк блокирует второй транш; первый транш уже платится, аренда продолжается, срок одобрения ипотеки истекает
- **time:** 5 месяцев после даты «готовности» в уведомлении застройщика; за 11 дней до окончания кредитного договора банк прислал отказ во втором транше
- **finale:** семья отказалась подписывать акт без РВЭ; застройщик сослался на «техническую задержку документов»; банк предложил только рефинансирование под рыночную ставку — ДДУ не расторгли, ключи не получили, спор ушёл в претензию к застройщику и запрос в банк
- **comment_magnet_angle:** «Застройщик зовёт на ключи, а РВЭ в реестре нет уже пятый месяц: вы бы подписали акт „с замечаниями“ ради второго транша или ждали бы разрешение, даже если ипотека „сгорает“?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild RVE+tranche casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-13)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| неустойка застройщика | 55,11176 | 138 (rejected — fingerprint dup keys_delay_penalty live) |
| траншевая ипотека новостройка | 55,11176 | 4 (weak; rate-hike tranche cluster taken LIVE-TRANSHEVAYA) |
| коттеджный поселок тюмень участок | 55,11176 | 34 (backup KP angle) |
| проектная декларация застройщика | 55,11176 | 22 (weak) |
| **разрешение на ввод в эксплуатацию** | **55,11176** | **201** |
| разрешения на ввод в эксплуатацию тюмень | 55,11176 | 31 (local tail) |
| **разрешение на ввод в эксплуатацию** | **225 (compare)** | **16550** |
| новостройки тюмень | 55 | 3640 (context spine) |

**wordstat_rework log:**
- probe «траншевая ипотека новостройка» 55,11176 → 4 (weak; overlaps transh rate cluster)
- probe «неустойка застройщика» 55,11176 → 138 (strong but plot blocked by fingerprint)
- probe «коттеджный поселок тюмень участок» → 34 (weak for P0)
- **rework:** buyer jargon РВЭ + ввод в эксплуатацию + новостройка Тюмень → **final P0 «разрешение на ввод в эксплуатацию» regions 55,11176,compare225 freq 201 (55+11176) / 16550 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ввод объекта, права дольщиков
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B26, title, slug, signal_urls, research angles for Research role.
