# Scout inputs — 2026-09-04 (B22)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-04 (YEKT Friday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks (last_sync 2026-09-04)
- **FROZEN today 2026-09-04 (DO NOT reuse plot):**
  - `newbuild_acceptance_defects_act_keys_denied` — «В Тюмени застройщик потребовал акт с дефектами — иначе без ключей» (slug v-tyumeni-na-priemke-naschitali-defekty-zastrojschik-potreboval-podpisat-akt)
- **Recent newbuild live WP Sep 1–3 (distinct cluster required):**
  - bank revoked mortgage approval 72h before DDU — бронь сгорела
  - finish type mismatch чистовая vs предчистовая
  - keys delayed 8 months + certificate instead of penalty
  - DDU area mismatch at keys
  - storage room missing (B21 cluster)
  - installment increase before handover
  - KP without gas/water at keys
  - assignment refusal after payment
  - legal entity change + escrow (B20)
  - price increase after booking
  - family mortgage escrow matkapital (B19)
- **Closed clusters (30d):** B12 ddu_escrow_handover_delay_tyumen; B21 newbuild_ddu_cellar_paid_not_handed_tyumen; B20 newbuild_developer_legal_entity_change_ddu_escrow_tyumen; all frozen secondary in used-clusters.json
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B22
- **title_draft:** В Тюмени накануне ДДУ банк поднял ставку ипотеки — платёж вырос, сделку остановили
- **slug:** v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platyozh-vyros
- **cluster_id (new):** newbuild_mortgage_rate_changed_before_ddu_tyumen
- **story_dup_check:** PASS — distinct from Sep 3 «банк снял одобрение» (revocation, not rate change); distinct from B19 family mortgage escrow; distinct from today's acceptance-defects act; plot = одобрение ипотеки на новостройку было, но за 24–48 часов до подписания ДДУ банк изменил процентную ставку / условия программы, платёж вырос, семья остановила сделку и потеряла бронь

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, банк одобрил ипотеку с фиксированной ставкой в расчёте платежа, застройщик забронировал лот до даты подписания ДДУ
- **risk:** накануне подписания ДДУ банк уведомил об изменении процентной ставки (или отмене льготной программы) — ежемесячный платёж вырос на заметную сумму (например +15–20 тыс. ₽), первоначальный взнос и схема эскроу перестали сходиться
- **time:** за 24–48 часов до подписания ДДУ, после месяцев одобрения и брони
- **finale:** семья отказалась подписывать ДДУ на новых условиях; бронь сгорела, внесённая плата за бронирование не вернулась (или вернулась частично по правилам застройщика); квартира ушла в продажу, пришлось заново искать объект и проходить одобрение
- **comment_magnet_angle:** «Банк поднял ставку накануне ДДУ — вы бы всё равно подписали договор или развернулись бы, даже если бронь сгорит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild mortgage-rate casus without Klyshin — preferred; avoids Sep 3 approval-revocation plot and today's acceptance-defects cluster)

## Wordstat MCP-KV (live 2026-09-04)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55+11176 | 4683 (context only) |
| долгострой тюмени | 55+11176 | 86 (rejected — overlap B12 + Sep 3 keys-delay cluster) |
| ипотека в тюмени на новостройки | 55+11176 | 41 (broader, less rate-specific) |
| ставка ипотеки новостройка | 55+11176 | 54 total |
| **ипотека на новостройку процентная ставка** | **55+11176** | **21** |
| ипотека на новостройку процентная ставка | 225 (compare) | 960 |
| эскроу счет новостройка | 55+11176 | 2 (rejected — B19/B20 escrow cluster) |
| машиноместо новостройка | 55+11176 | 3 (rejected — weak) |
| парковка дду новостройка | 55+11176 | API empty (rejected) |
| площадь балкона дду | 55+11176 | API empty (rejected — Sep 3 area mismatch cluster) |

**wordstat_rework log:**
- probe «долгострой тюмени» 55+11176 → 86 (strong volume but delay/srok cluster closed by B12 + Sep 3)
- probe «ставка ипотеки новостройка» 55+11176 → 54; top child «ипотека на новостройку процентная ставка» → 21
- probe «ипотека в тюмени на новостройки» 55+11176 → 41 (higher volume but loses rate-change spine)
- probe «эскроу счет новостройка» 55+11176 → 2 (weak; escrow plot taken)
- probe «машиноместо новостройка» 55+11176 → 3 (weak parking angle)
- **rework:** localize Tyumen + mortgage-rate buyer jargon on newbuild → **final P0 «ипотека на новостройку процентная ставка» regions 55,11176 freq 21** (compare RU225 960)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст ипотеки на новостройки; не дубль кластера
- https://www.cbr.ru/hkeypress/keypr/ — ключевая ставка ЦБ (контекст изменения ставок банками)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B22, title, slug, signal_urls, research angles for Research role.
