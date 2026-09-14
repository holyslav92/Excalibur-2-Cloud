# Scout inputs — 2026-09-14 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-14 (YEKT Monday slot 10:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO parking/машино-место double-sold (B24 cluster)
- NO DDU finishing vs acceptance mismatch (B25 cluster: acceptance_defects_penalty)
- NO RVE delay + mortgage tranche (B26 cluster: newbuild_rve_delay_blocks_mortgage_tranche_tyumen)
- NO keys_delay_penalty_unpaid (H1 fingerprint duplicate LIVE-V-TYUMENI-ZASTROJSCHIK-P)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-14)
- Live WP recent: B26 RVE+tranche, B25 finishing, B24 parking, B23 apartamenty, transhevaya +480k, installment penalty, escrow zero, subsidized mortgage removed, trade-in, bank appraisal -680k, family mortgage recalc, cottage defects 850k, assignment lost 7 days, KP plot 12 vs 9.7 sotok
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: новостройк, дду, приёмк)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше
- **slug:** v-tyumeni-v-ddu-obeschali-54-metra-na-priemke-kvartira-okazalas-menshe
- **cluster_id (new):** newbuild_ddu_area_mismatch_acceptance_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** В ДДУ и проектной декларации указана площадь 54,2 м²; на приёмке замер БТИ показал 52,1 м² (−2,1 м²). Застройщик ссылается на «проектные отклонения в пределах нормы», но цена в ДДУ не пересчитана, акт приёма-передачи требуют подписать без скидки. Семья остановила подписание за 48 часов до истечения срока брони на переуступку соседней квартиры.
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ → проектная декларация → приёмка новостройки → акт; нет продавца вторички, ЕГРН-обременений, наследников или бабушки на осмотре
- **story_dup_check:** PASS — distinct from B25 (отделка чистовая vs голые стены), B23 (квартира vs апартаменты), B24 (парковка), B26 (РВЭ+транш), extra meters penalty (420k за лишние метры — обратный кейс: метры пропали)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала двушку в новостройке; в ДДУ и буклете — 54,2 м², платёж по ипотеке рассчитан на эту площадь
- **risk:** меньшая площадь = меньше ликвидность и переплата ~180–220 тыс. за «воздух»; застройщик не согласен на уменьшение цены; без акта — нет регистрации и второй транш ипотеки
- **time:** приёмка через 11 дней после уведомления; 48 часов до сгорания брони на соседнюю планировку; 6 дней до дедлайна банка на регистрацию
- **finale:** семья не подписала акт, зафиксировала расхождение в претензии, запросила перерасчёт цены ДДУ; застройщик предложил скидку 90 тыс. вместо 210 тыс. по формуле; банк ждёт решения — ключи не получили, но сделку не сорвали окончательно
- **comment_magnet_angle:** «На приёмке площадь меньше на 2 квадрата, а застройщик зовёт подписать акт „как есть“: вы бы взяли скидку 90 тысяч или ушли бы в претензию и рискнули сроком ипотеки?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild area-mismatch casus without Klyshin)

## Wordstat (MCP-KV live — conductor verified)

- **wordstat_preflight:** mcp-kv wordstat_get_user_info OK
- **wordstat_rework:**
  - probe «площадь квартиры дду новостройка» → API empty → rework
  - probe «приемка квартиры новостройка тюмень» → 35 (Tyumen 55+11176)
  - probe «переуступка новостройка» → 18 (55+11176)
  - probe «семейная ипотека новостройка тюмень» → 23 (55+11176)
  - → final P0 «приемка квартиры в новостройке тюмень» **35**
- **wordstat:** mcp_kv live | regions 55,11176,compare225 | P0 «приемка квартиры в новостройке тюмень» 35

## Anti-dupe hard (DONE)

- **h1_fingerprint_check:** PASS | fingerprint: ddu_area_mismatch_acceptance
- **formula_spam_check:** PASS | last3_mechanisms: rve_tranche_block, finishing_mismatch, parking_double_sold (all different)
- **anti_dupe_hard:** PASS

## Output format

Write complete handoff markdown with all required fields from skills/scout-excalibur-blog/SKILL.md handoff section. End with clear topic_id B27, title_draft, slug, cluster_id for research_start.
