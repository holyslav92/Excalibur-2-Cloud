# Scout inputs — 2026-09-14 (B27, slot 17:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-14 (YEKT weekday slot ~17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO double booking / две брони на одну квартиру (today 09:00 slot)
- NO DDU area mismatch −2 м² / площадь меньше на приёмке (today 12:00 slot)
- NO layout downgrade трёшка→двушка перед эскроу (today 15:00 slot)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots
- NO retitle: бабушка, банкрот, ЕГРН-вторичка, опека-вторичка, паркинг double-sold (B24), чистовая приёмка (B25), РВЭ+транш (B26)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-14)
- Live WP today (2026-09-14): две брони на одну квартиру; DDU 54 м² → −2 м² на приёмке; трёшка в ДДУ → двушка за 19 дней до эскроу
- **Rejected angles:** страховой отказ+эскроу (fingerprint dup LIVE-V-TYUMENI-BANK-OCENIL-NO); неустойка+мораторий (fingerprint dup LIVE-V-TYUMENI-ZASTROJSCHIK-P); скидка за досрочный платёж (fingerprint dup LIVE-TRANSHEVAYA)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек, новостройк)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени одобрили маткапитал на новостройку — за 9 дней до эскроу ребёнку исполнилось 7 лет, банк остановил ДДУ
- **slug:** v-tyumeni-matkapital-na-novostrojku-rebenku-ispolnilsya-7-let-bank-ostanovil-ddu
- **article_dir:** memory/blog/articles/B27-v-tyumeni-matkapital-na-novostrojku-rebenku-ispolnilsya-7-let-bank-ostanovil-ddu
- **cluster_id (new):** newbuild_matkapital_child_age_limit_before_escrow_tyumen
- **top_energy_mirror:** clock_ran_out
- **newbuild_mechanism:** семья взяла семейную ипотеку + маткапитал на квартиру в новостройке по ДДУ; СФР одобрил направление средств на эскроу при условии возраста ребёнка; за 9 дней до подписания ДДУ и открытия эскроу ребёнку исполнилось 7 лет → СФР приостановил распоряжение → банк не принял неполный пакет и остановил сделку, бронь под угрозой
- **why_newbuild_not_secondary:** маткапитал и семейная ипотека направляются на эскроу-счёт по ДДУ с застройщиком; нет продавца вторички, наследников, ЕГРН-вторички; отличие от B18 (детские доли на вторичке) и B19 (эскроу не открыли по техпричинам банка)
- **story_dup_check:** PASS — distinct from matkapital_missing_child_shares (B18 secondary), escrow_not_opened_after_mortgage (B19), today’s booking/area/layout clusters

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала двушку в новостройке, одобрили семейную ипотеку и подали маткапитал на эскроу
- **risk:** без распоряжения СФР банк не открывает эскроу и не подписывает ДДУ; при «перешагивании» возраста ребёнка сертификат блокируется до пересмотра
- **time:** за 9 дней до даты подписания ДДУ; день рождения ребёнка совпал с окном брони
- **finale:** банк прислал отказ в выдаче кредита без полного маткапитала; застройщик дал 5 дней на замену программы — семья остановила ДДУ, пересчитала без маткапитала (платёж +18 тыс./мес), бронь сняли через 3 дня; деньги на эскроу не ушли
- **comment_magnet_angle:** «Ребёнку исполнилось 7 лет за неделю до эскроу, а менеджер говорил „маткапитал успеем“: вы бы подписали ДДУ без сертификата, если банк уже прислал предупреждение, или снимали бронь и пересчитывали ипотеку?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild matkapital+age casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-14)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| материнский капитал новостройка | 55,11176 | 11 (weak) |
| материнский капитал на покупку жилья | 55,11176 | 72 |
| маткапитал новостройка тюмень | 55,11176 | 3 (weak) |
| семейная ипотека | 55,11176 | 9962 (broad) |
| **семейная ипотека тюмень** | **55,11176** | **1227** |
| семейная ипотека тюмень | 225 (compare) | 1740 |
| новостройки тюмень | 55,11176 | 8390 (context spine) |

**wordstat_rework log:**
- probe «материнский капитал новостройка» 55,11176 → 11 (weak, plot-specific)
- probe «материнский капитал на покупку жилья» → 72 (ok but narrow)
- rework: buyer jargon семейная ипотека + локализация Тюмень + newbuild casus → **final P0 «семейная ипотека тюмень» regions 55,11176,compare225 freq 1227 (55+11176) / 1740 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_256370/ — ФЗ о маткапитале, направление на жильё
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, эскроу, ДДУ
- https://sfr.gov.ru/ — СФР, распоряжение маткапиталом
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, article_dir, signal_urls, research angles for Research role.
