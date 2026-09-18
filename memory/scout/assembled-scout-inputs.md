# Scout inputs — 2026-09-18 (B27, slot 12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-18 (YEKT weekday slot **12:00**)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO repeat of **09:00 slot today** (LIVE-V-TYUMENI-ODOBRENIE-IPOT): ипотека «сгорела» на 87-й день одобрения — cluster mortgage approval expired
- NO acceptance_defects_penalty / KP act refusal plots (B25, LIVE acceptance, LIVE KP gas)
- NO formula spam skeleton ddu_vs_escrow_amount (last 3 live: insurance 186k, corpus change, matkapital opieka — all escrow/DDU-adjacent)
- NO frozen secondary clusters in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-18)
- Live WP recent (~20): ипотека сгорела 87-й день (2026-09-18 09:00), matkapital+опека новостройка, запрет аренды в приложении к ДДУ, перенос в другой корпус, оценка -900k, машино-место в декларации, страховка 186k, ключи +9 мес без неустойки, созаёмщик отказ, бронь vs секция ДДУ, переуступка аванс 350k, КП без газа…
- **Rejected:** KP участок -2 сotki — BLOCKED as acceptance_defects_penalty cluster
- **Rejected:** DDU 65 vs 58 sqm — FORMULA SPAM (ddu_vs_escrow_amount skeleton in last 3)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: эскроu, новостройк)
- `story_dup.py --text` PASS → cluster `assignment_lost_to_faster_buyer`

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени 28 дней ждали регистрацию переуступки — за сутки до эскроу лот забрал другой
- **slug:** v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj
- **article_dir:** memory/blog/articles/B27-v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj
- **cluster_id (new):** assignment_lost_to_faster_buyer
- **top_energy_mirror:** someone_else_took_object
- **newbuild_mechanism:** покупатель держит **переуступку** по новостройке (договор уступки + согласие застройщика); застройщик **не регистрирует уступку в реестре 28 дней**; накануне открытия эскроу лот **снимают с брони** и продают другому — первый покупатель теряет объект, аванс/бронь под угрозой
- **why_newbuild_not_secondary:** цепочка ДДU первоначального дольщика → согласование переуступки → регистрация уступки → эскроu нового покупателя; нет продавца вторички, ЕГРН-сделки между физлицами, наследников или «чистой выписки»
- **story_dup_check:** PASS — отличается от LIVE переуступка 350k (аванс **завис**, не «лот ушёл другому»), от booking_expired_price_hike (бронь vs секция ДДU), от mortgage approval expired (87-й день ипотеки)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени нашла переуступку в строящемся ЖК, подписала договор уступки, внесла бронь; застройщик обещал зарегистрировать уступку «на этой неделе»
- **risk:** без регистрации уступки эскроu не открывают на нового дольщика; пока тянут — лот могут продать повторно
- **time:** 28 дней ожидания регистрации; за **сутки** до даты открытия эскроu менеджер сообщает, что квартира «уже в брони» у другого покупателя
- **finale:** семья не успела на эскроu; бронь/аванс застройщик предложил вернуть только частично; договор уступки оспорили через претензию — лот потерян, пришлось искать другую планировку дороже
- **comment_magnet_angle:** «28 дней регистрацию тянули, а лот сняли за сутки до эскроu: вы бы ждали согласие застройщика или сразу искали другую переуступку, даже если цена уже поднялась?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild assignment casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-18)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройка | 55,11176 | 19 (weak P0 alone) |
| переуступка квартиры | 55,11176 | 63 (mixed secondary/newbuild) |
| переуступка новостройки | 55,11176 | 19 |
| **купить новостройку в тюмени** | **55,11176** | **923** |
| купить новостройку в тюмени | 225 (compare) | (buyer spine RU compare) |
| новостройки тюмень | 55,11176 | 4446 (context) |

**wordstat_rework log:**
- probe «переуступка новостройка» 55,11176 → 19 (weak; не drop casus)
- probe «переуступка квартиры» 55,11176 → 63 (смешанный спрос, не чистый newbuild P0)
- **rework:** buyer jargon **купить новостройку в тюмени** + hook переуступка/эскроu/застройщик → **final P0 «купить новостройку в тюмени» regions 55,11176,compare225 freq 923 (55+11176)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, переуступка прав требования по ДДU
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, article_dir, signal_urls, research angles for Research role.
