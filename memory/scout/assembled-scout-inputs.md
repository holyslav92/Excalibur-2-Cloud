# Scout inputs — 2026-09-01 (B19)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-01 (YEKT Monday slot 09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- **FROZEN today (01 Sep 2026 live plots — DO NOT reuse):**
  - `newbuild_acceptance_wet_screed_keys_denied` — daily «На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали» (slug na-priemke-novostrojki-v-tyumeni-nashli-mokruyu-styazhku-klyuchi-ne-vydali)
  - `transhevaya_ipoteka_payment_spike` — «Платёж по новостройке вырос в 8 раз — до брони»
- **Closed clusters (30d):** B12 `ddu_escrow_handover_delay_tyumen` (ключи перенесли на год / эскроу заморозили); matkapital_missing_child_shares (B18 secondary); registered_persons (B17); communal_share (B16); all frozen secondary clusters in used-clusters.json
- Live WP ~20 (EXCALIBUR_RECENT_WP_POSTS 2026-09-01): today's priemka wet screed; transhevaya ipoteka; kapremont secondary; double sale; forged spouse B15; matkapital child shares; propisannye; communal share; closed mortgage cert B14; predvaritelny dogovor; kladovka EGRN; akkreditiv
- `published-titles-only.md` + `shared/published-articles.md` — B02–B15 ledger (B13 never published; B16–B18 assigned to live secondary WP posts in used-clusters, not longform ledger)

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B19
- **title_draft:** Семейную ипотеку на новостройку в Тюмени одобрили — эскроу не открыли из‑за маткапитала
- **slug:** v-tyumeni-semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli
- **cluster_id (new):** newbuild_family_mortgage_matkapital_escrow_blocked_tyumen
- **story_dup_check:** PASS — distinct from B12 (перенос сдачи/заморозка эскроу после внесения), today's priemka wet screed, matkapital_opieka_kids / matkapital_missing_child_shares (вторичка), B09 egrn_line; plot = семейная ипотека на новостройку одобрена, но банк/застройщик не открыли эскроу из‑за незакрытого обязательства по маткапиталу на прошлое жильё

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке под семейную ипотеку, банк одобрил кредит и согласовал схему с маткапиталом в первоначальный взнос
- **risk:** при открытии эскроу-счёта всплыло незакрытое обязательство по прошлому использованию маткапитала (детские доли / справка ПФР / распоряжение) — банк приостановил открытие эскроу, срок брони в офисе продаж истекал
- **time:** за 48 часов до дедлайна брони / подписания ДДУ (после одобрения семейной ипотеки)
- **finale:** бронь сняли, квартиру ушла в свободную продажу; семья потеряла очередь и внесённую плату за бронирование; пришлось заново собирать пакет по маткапиталу и искать другой объект (2–4 недели)
- **comment_magnet_angle:** «Маткапитал уже трогали на прошлую квартиру — вы всё равно бронируете новостройку в семейную ипотеку или сначала закрываете справку в ПФР?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild family-mortgage casus without Klyshin — preferred; avoid today's priemka plot and B12 escrow-delay cluster)

## Wordstat MCP-KV (live 2026-09-01)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка дду | 55+11176 | 25 (rejected — weak volume; close to B12 DDU spine) |
| переуступка новостройка | 55+11176 | 10 (rejected — weak) |
| маткапитал новостройка | 55+11176 | 3 (rejected — weak standalone) |
| семейная ипотека новостройка | 55+11176 | 126 |
| новостройки тюмени семейная ипотека | 55+11176 | 40 |
| новостройки тюмени семейная ипотека | 225 (compare) | 55 |
| семейная ипотека | 55+11176 | 9233 (rejected — too broad, not newbuild-specific) |
| **купить новостройку в тюмени в ипотеку** | **55+11176** | **93** |
| купить новостройку в тюмени в ипотеку | 225 (compare) | 140 |
| купить новостройку тюмень | 55+11176 | 1192 (context only) |

**wordstat_rework log:**
- probe «переуступка дду» 55+11176 → 25 (on-plot but narrow; overlap risk with B12)
- probe «маткапитал новостройка» 55+11176 → 3 (weak P0)
- probe «семейная ипотека новостройка» 55+11176 → 126; local «новостройки тюмени семейная ипотека» → 40
- probe «семейная ипотека» 55+11176 → 9233 (too broad)
- **rework:** buyer jargon mortgage+newbuild Tyumen → **final P0 «купить новостройку в тюмени в ипотеку» regions 55,11176 freq 93** (compare RU225 140); on-plot secondary «новостройки тюмени семейная ипотека» 40

## signal_urls (research)

- https://dzen.ru/holyslav — контекст семейной ипотеки и маткапитала на новостройку; не дубль кластера.
- https://www.gosuslugi.ru/help/faq/maternal_capital/100359 — маткапитал: обязательства по выделению долей
- https://t.me/klyshin_A — checked, not used this slot
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B19, title, slug, signal_urls, research angles for Research role.
