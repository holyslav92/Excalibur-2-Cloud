# Scout inputs — 2026-09-02 (B21)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals, no meta-commentary about files or shell. Output the complete handoff text now as plain markdown.

**run_date:** 2026-09-02 (YEKT Wednesday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks
- **FROZEN today (02 Sep 2026 live — DO NOT reuse):**
  - `newbuild_kp_utilities_missing_at_handover_tyumen` — «В Тюмени дом сдали без газа и воды — семья не взяла ключи»
  - `newbuild_assignment_ddu_registration_refused_tyumen` — «В Тюмени оплатили переуступку — застройщик не оформил ДДУ»
- **Recent newbuild closed (30d):** B20 `newbuild_developer_legal_entity_change_ddu_escrow_tyumen`; бронь+цена +380к; B19 семейная ипотека+эскроу+маткапитал; мокрая стяжка приёмка; траншевая ипотека; B12 `ddu_escrow_handover_delay_tyumen`
- Live blog ~20 synced via EXCALIBUR_RECENT_WP_POSTS + tymenrieltor.ru/blog/

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B21
- **title_draft:** В Тюмени платили рассрочку по ДДУ — перед сдачей застройщик поднял остаток
- **slug:** v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok
- **cluster_id (new):** newbuild_developer_installment_balance_increased_before_handover_tyumen
- **story_dup_check:** PASS — distinct from B12 (перенос сдачи/заморозка эскроу), B20 (смена юрлица), бронь+380к (цена при брони, не рассрочка), B19 (ипотека+маткапитал), wet screed priemka, KP comms today, переуступка today; plot = график рассрочки в ДДУ, 14 месяцев платежей, допсоглашение с ростом остатка за месяц до ключей

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке с рассрочкой от застройщика по графику в ДДУ
- **risk:** за месяц до сдачи корпуса застройщик прислал допсоглашение — остаток вырос примерно на 400 тыс., сроки сжаты; угроза расторжения ДДУ и потери внесённых платежей
- **time:** «14 месяцев платили по графику» → «за месяц до сдачи»
- **finale:** семья отказалась подписывать допсоглашение; застройщик пригрозил расторжением; деньги и очередь на квартиру под угрозой; обратились за разбором до подписи
- **comment_magnet_angle:** «Если в ДДУ прописан график рассрочки — застройщик вообще имеет право поднять остаток за месяц до ключей?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild installment casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-02)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| рассрочка от застройщика тюмень | 55+11176 | 142 |
| рассрочка от застройщика | 55+11176 | 213 |
| рассрочка от застройщика | 225 (compare) | 21115 |
| квартира в рассрочку от застройщика тюмень | 55+11176 | 88 |
| долгострой тюмень | 55+11176 | 91 (rejected — overlap B12) |
| штраф застройщику | 55+11176 | 42 (rejected — weak) |
| отделка новостроек тюмень | 55+11176 | 44 |
| **новостройки тюмень** | **55+11176** | **4649** |
| новостройки тюмень | 225 (compare) | 8792 |

**wordstat_rework log:**
- probe «рассрочка от застройщика тюмень» 55+11176 → 142 (strong local hook)
- probe «рассрочка от застройщика» 55+11176 → 213; compare RU225 → 21115
- probe «долгострой тюмень» 55+11176 → 91 (rejected — B12 cluster overlap)
- probe «штраф застройщику» 55+11176 → 42 (weak)
- **rework:** buyer demand spine newbuild Tyumen → **final P0 «новостройки тюмень» regions 55,11176 freq 4649** (compare RU225 8792); on-plot hook «рассрочка от застройщика тюмень» 142

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ долевое строительство (ДДУ, права дольщика)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/[REDACTED]

## Output required

Write complete Scout handoff markdown. **GATE FORMAT (HARD):** include these exact flat single-line fields (no markdown bold on keys, each on its own line near the top after topic_id):

```
topic_id: B21
title_draft: ...
slug: ...
cluster_id: ...
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: optional | none | original: none | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: ...
dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «…» | finale: «…»
comment_magnet_angle: «…?»
wordstat_rework: probe «…» <freq> → … → final P0 «…» <freq>
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4649
story_dup_check: PASS | cluster_id: newbuild_developer_installment_balance_increased_before_handover_tyumen
```

Then add Research direction, signal_urls, article_dir as sections below.

Lock topic_id B21, title, slug for Research role.
