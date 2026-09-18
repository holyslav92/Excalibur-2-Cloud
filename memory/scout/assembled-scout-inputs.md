# Scout inputs — 2026-09-18 (B27, slot ~15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-18 (YEKT Friday slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO переуступка / assignment lost (2026-09-18: assignment 28 days + mortgage day 87)
- NO маткапитал+опека newbuild (2026-09-17)
- NO запрет аренды в ДДУ / investor rental ban (2026-09-17)
- NO другой корпус / section swap (2026-09-17)
- NO оценка банка ниже ДДУ (2026-09-17, cluster bank_appraisal_below_ddu_price)
- NO машино-место / страховка 186к / ключи+9мес неустойка / созаёмщик (2026-09-16)
- NO бронь этаж/вид vs ДДУ / переуступка аванс 350к (2026-09-15)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-18)
- Live WP recent (~12): переуступка 28д, ипотека 87-й день, маткапитал+опека, запрет аренды ДДУ, другой корпус, оценка -900к, машино-место, страховка 186к, ключи+9мес, созаёмщик, бронь vs ДДУ, переуступка 350к
- **Rejected:** keys_delay_penalty_unpaid — cluster locked (2026-09-16)
- **Rejected:** acceptance_defects_penalty / B25 chistovaya — cluster locked, finishing mismatch done
- **Rejected:** KP gas only colodets — valid backup cluster kp_gas_utilities_not_connected_tyumen (P0 «коттеджные поселки тюмень» 1479) — kept as alternate
- **Rejected:** developer double sale — valid but booking_expired fingerprint overlap risk; kept as alternate
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (newbuild: ДДУ, приёмка, БТИ)
- `story_dup.py` — cluster bti_area_smaller_than_ddu_tyumen is NEW (not in used-clusters)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени на ключах площадь по БТИ оказалась на 4,2 кв.м меньше ДДУ — перерасчёт отказали
- **slug:** v-tyumeni-na-klyuchah-ploshchad-po-bti-okazalas-menshe-ddu-pereraschet-otkazali
- **article_dir:** memory/blog/articles/B27-v-tyumeni-na-klyuchah-ploshchad-po-bti-okazalas-menshe-ddu-pereraschet-otkazali
- **cluster_id (new):** bti_area_smaller_than_ddu_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** В ДДУ указана проектная площадь 68,4 кв.м; на выдаче ключей техпаспорт БТИ показывает 64,2 кв.м (−4,2 кв.м). Застройщик ссылается на допустимое отклонение по 214-ФЗ и отказывает в перерасчёте цены; семья уже внесла полную сумму на эскроу по старой площади — спор на приёмке, акт не подписали
- **why_newbuild_not_secondary:** сюжет только в цепочке ДДУ → эскроу → обмеры БТИ при сдаче новостройки застройщиком; нет продавца вторички, ЕГРН-наследников, опеки на вторичке или сделки с физлицом
- **story_dup_check:** PASS — distinct from acceptance_defects_penalty (дефекты/чистовая B25), bank_appraisal_below_ddu_price (оценка банка −900к), booking_expired (бронь vs ДДУ секция), keys_delay_penalty_unpaid (срок ключей+неустойка)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила трёшку в новостройке по ДДУ; застройщик пригласил на выдачу ключей
- **risk:** меньшая площадь по БТИ = переплата за «лишние» квадраты; без подписанного акта — нет регистрации права и риск потери неустойки/ипотечного графика
- **time:** в день выдачи ключей, за 2 часа до подписания акта приёмки-передачи
- **finale:** застройщик отказал в перерасчёте 412 тысяч разницы; семья не подписала акт, ключи не получила; банк напомнил о сроке регистрации по ипотеке — спор ушёл в претензию и независимый обмер
- **comment_magnet_angle:** «В ДДУ 68 квадратов, по БТИ 64 — вы бы подписали акт „с замечаниями“ ради ключей или заблокировали регистрацию, пока застройщик не пересчитает цену?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild BTI-area casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-18)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| площадь по дду | 55,11176 | 5 (weak) |
| изменение площади квартиры | 55,11176 | 5 (weak) |
| приемка квартиры в новостройке | 55,11176 | 128 |
| приемка квартиры в новостройке тюмень | 55,11176 | 29 (local tail) |
| новостройки тюмень | 55,11176 | 4446 |
| купить новостройку в тюмени | 55,11176 | 923 |
| коттеджные поселки тюмень | 55,11176 | 1479 (backup KP angle) |

**wordstat_rework log:**
- probe «площадь по дду» 55,11176 → 5 (weak)
- probe «изменение площади квартиры» 55,11176 → 5 (weak)
- probe «приемка квартиры в новостройке» 55,11176 → 128 (mechanism-adjacent)
- **rework:** buyer jargon новостройки + Тюмень + ДДУ/приёмка → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4446**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, отклонение площади, права дольщика
- https://www.domrf.ru/ — проектные декларации застройщиков
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, article_dir, signal_urls, research angles for Research role.
