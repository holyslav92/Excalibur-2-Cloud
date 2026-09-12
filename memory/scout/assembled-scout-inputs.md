# Scout inputs — 2026-09-10 (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-10 (YEKT Thursday slot ~12:00, 4-й cron run сегодня)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 24 active locks (last_sync 2026-09-10)
- **Live WP 2026-09-10 (~12 titles) — DO NOT reuse plot:**
  - trade-in сорвался перед ДДУ (занизили оценку 1,2 млн) — cluster trade_in_rejected_developer
  - в ДДУ обещали чистовую — отдали предчистовую
  - бронь сгорела, цена +450 тыс — cluster booking_expired_price_hike
  - пропал балкон в планировке — банк заморозил транш (2026-09-09)
  - застройщик год не платил неустойку — приёмку остановили (2026-09-09)
  - ребёнку 7 лет — семейную ипотеку пересчитали перед ДДУ (2026-09-09)
  - банк остановил транш после приёмки без замечаний (2026-09-09)
  - ключи без разрешения на ввод — банк заморозил ипотеку (2026-09-08)
  - переуступка долг 94к — сделку остановили (2026-09-08)
  - маткапитал за 3 недели до ключей — детские доли (2026-09-08)
  - созаёмщика убрали перед ДДУ (2026-09-07)
  - ДДУ расторгли из-за просрочки рассрочки — удержали 180 тыс (2026-09-07)
- **Rejected overlap:** parking «машиноместо по ДДУ» → 44% overlap with B21 cellar cluster (scout_helper FAIL)
- **Rejected overlap:** trade-in, finishing, booking, balcony, penalty, matkapital, co-borrower, tranche, keys without permit, assignment debt
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)
- `excalibur_blog_scout_story_dup.py --text` PASS (fingerprint + formula spam OK)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени купили дом в посёлке — границы участка в выписке не совпали с ДДУ
- **slug:** v-tyumeni-kupili-dom-v-poselke-granicy-uchastka-ne-sovpali-s-ddu
- **article_dir:** memory/blog/articles/B24-v-tyumeni-kupili-dom-v-poselke-granicy-uchastka-ne-sovpali-s-ddu
- **cluster_id (new):** newbuild_cottage_plot_boundary_ddu_mismatch_tyumen
- **story_dup_check:** PASS — distinct plot: семья купила **дом в коттеджном посёлке** от застройщика по ДДУ; в приложении к договору — план границ участка 12 соток с забором по линии; при получении выписки ЕГРН и выезде на участок кадастровая граница **на 1,5 сотки меньше**, забор соседа стоит на «их» земле по плану в ДДУ → ипотека на ИЖС под угрозой, застройщик ссылается на «уточнение межевания», семья остановила приёмку дома

## Top-energy mirror

- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** ДДУ на дом в КП + кадастровая граница участка vs план в приложении к договору; расхождение площади/границ при регистрации права
- **why_newbuild_not_secondary:** покупка **дома от застройщика** в коттеджном посёлке по ДДУ (214-ФЗ), не сделка с физлицом на вторичном рынке; риск в проектной/кадастровой документации застройщика до приёмки

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала дом в коттеджном посёлке, подписала ДДУ, внесла аванс и открыла ипотеку на ИЖС
- **risk:** при регистрации права на землю и дом выписка ЕГРН показывает **меньшую площадь участка** и другую линию границы, чем в приложении к ДДУ; забор соседа фактически на «их» метрах; банк приостанавливает выдачу транша
- **time:** на этапе регистрации права / перед финальной приёмкой дома (через 3–4 недели после подачи документов в Росреестр)
- **finale:** застройщик предложил «подождать уточнения межевания» и всё равно подписать акт; семья отказалась от приёмки, подала претензию с требованием привести границы в соответствие с ДДУ или расторгнуть договор — ключи не получили, спор ушёл в досудебку
- **comment_magnet_angle:** «В ДДУ нарисовали 12 соток, а в выписке — 10,5, и забор соседа уже стоит на вашей линии: вы бы подписали акт приёмки дома „как есть“ или сразу в суд, даже если застройщик обещает „домежить потом“?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild KP plot-boundary casus without Klyshin — preferred; avoids today's 3 live plots and B21 parking/cellar overlap)

## Wordstat MCP-KV (live 2026-09-10)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| машиноместо новостройка | 55 | 2 (rejected — 44% overlap B21 cellar) |
| паркинг новостройка тюмень | 55 | 1 (rejected — overlap + weak) |
| **коттеджный поселок тюмень** | **55** | **1341** |
| дом в коттеджном поселке тюмень | 55 | 43 (on-topic buyer) |
| ижс тюмень | 55 | 522 (land/house buyer spine) |
| купить участок ижс тюмень | 55 | 166 (context) |
| **новостройки тюмень** | **55+11176** | **4670** |
| новостройки тюмень | 225 (compare) | 8607 |

**wordstat_rework log:**
- probe «машиноместо новостройка» 55 → 2 (rejected — scout_helper 44% overlap B21)
- probe «паркинг новостройка тюмень» 55 → 1 (weak; parking cluster overlap)
- probe «коттеджный поселок тюмень» 55 → 1341 (strong KP buyer intent — on-topic for plot story)
- probe «ижс тюмень» 55 → 522 (strong land/house buyer spine)
- probe «дом в коттеджном поселке тюмень» 55 → 43 (narrow but on-plot)
- **rework:** localize Tyumen + newbuild buyer jargon (коттеджный посёлок, ДДУ, ИЖС, застройщик) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4670 (55+11176) / 8607 (RU225)** with contextual spine «коттеджный поселок тюмень» 1341

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и ипотеки; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ / земельные участки (контекст межевания)
- https://www.domrf.ru/ — справочник застройщиков / ДДУ (контекст КП)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Include: topic_id B24, title_draft, slug, article_dir, signal_urls, research angles for Research role.
