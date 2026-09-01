# Scout inputs — 2026-09-01 (B16)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-01 (automation slot 05:16 UTC / ~10:16 YEKT)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** newbuild_only (квартиры + дома от застройщика)
**dzen_rf_pack:** true — Meta/Instagram/Facebook heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- Live WP ~20 (wordpress_get_posts 2026-09-01): траншевая ипотека новостройка (9411), B12 escrow delay keys, B15 forged consent, B14 mortgage lien, secondary casus batch — NO prior «приёмка дефекты отказ от акта» plot
- **FROZEN — DO NOT reuse:** B12 `klyuchi-ot-novostrojki` (срок сдачи + эскроу заморожен); live `transhevaya-ipoteka-novostrojka-tyumen` (траншевый платёж ×8); all 19 clusters in used-clusters.json
- `published-titles-only.md` + `shared/published-articles.md` — B02–B15 ledger (B13 skipped)

## Proposed topic (PASS topic_focus + scout_helper + story_dup)

- **topic_id:** B16
- **title_draft:** На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали
- **slug:** v-tyumeni-na-priemke-novostrojki-nashli-mokruyu-styazhku-klyuchi-ne-vydali
- **cluster_id (new):** newbuild_acceptance_defects_refuse_act
- **story_dup_check:** PASS — distinct from B12 (delay/escrow), transhevaya_ipoteka (live), ddu_escrow_wrong_account; plot = дефекты на приёмке-передаче, отказ подписать акт, застройщик откладывает выдачу ключей до устранения

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени пришла на приёмку квартиры в новостройке с ипотекой и отделкой — на осмотре нашли мокрую стяжку, трещину в стене и промерзший подоконник
- **risk:** подписание акта приёмки-передачи без фиксации дефектов = потеря права на бесплатное устранение; застройщик предлагает «подпишите сейчас, исправим потом» — ключи не выдают до подписи
- **time:** в день назначенной приёмки, за две недели до окончания гарантийного срока на устранение по ДДУ
- **finale:** акт не подписали, дефекты зафиксировали в двух экземплярах с фото/видео; застройщик перенёс выдачу ключей на 45 дней; семья осталась платить ипотеку за квартиру без заселения
- **comment_magnet_angle:** «Если застройщик обещает всё исправить после подписи — вы подписываете акт или уходите без ключей?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild acceptance casus without Klyshin — preferred)
- **signal_urls:** see list below

## Wordstat MCP-KV (live 2026-09-01)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| приёмка квартиры в новостройке | 55+11176 | 108 |
| приёмка квартиры в новостройке | 225 (compare) | 6155 |
| приемка квартиры в новостройке тюмень | 55+11176 | 29 |
| акт приемки квартиры в новостройке | 55+11176 | 7 |
| приемка новостроек тюмень | 55+11176 | 29 |
| переуступка новостройка тюмень | 55+11176 | (rejected — different plot) |
| траншевая ипотека новостройка | 55+11176 | (rejected — live WP dup) |

**wordstat_rework log:**
- probe «приёмка квартиры в новостройке» 55+11176 → 108 (broad newbuild buyer intent)
- probe «приемка квартиры в новостройке тюмень» 55+11176 → 29 (localized P0)
- probe «акт приемки квартиры в новостройке» 55+11176 → 7 (too narrow for H1 spine)
- compare RU225 «приёмка квартиры в новостройке» → 6155
- **rework:** localize Tyumen + keep newbuild acceptance jargon → **final P0 «приемка квартиры в новостройке тюмень» regions 55,11176 freq 29** (buyer cluster новостройки; broad cluster 108)

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_5142/ — ГК РФ / ЗоЗПП (приёмка товара с недостатками)
- https://www.gosuslugi.ru/newsearch/приемка%20квартиры%20в%20новостройке — контекст buyer journey
- https://dzen.ru/holyslav — канал holyslav (engagement reference, не дубль кластера)
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B16, title, slug, signal_urls, research angles for Research role.
