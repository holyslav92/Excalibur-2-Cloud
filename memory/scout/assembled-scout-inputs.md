# Scout inputs — 2026-09-04 (B23 ONLY)

**FORBIDDEN:** topic_id B22 — already published 2026-09-04. Do NOT output B22, mortgage rate change, or cluster `newbuild_mortgage_rate_changed_before_ddu_tyumen`. Output ONLY B23 below.

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body for B23** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-04 (YEKT Friday slot ~15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-04)
- **Published today 2026-09-04 (DO NOT reuse plot):**
  - B22 `newbuild_mortgage_rate_changed_before_ddu_tyumen` — банк поднял ставку ипотеки накануне ДДУ
  - live WP `newbuild_acceptance_defects_act_keys_denied` — застройщик потребовал акт с дефектами
- **Recent newbuild live WP Sep 1–4 (distinct cluster required):**
  - bank revoked mortgage approval 72h before DDU
  - finish type mismatch чистовая vs предчистовая
  - keys delayed 8 months + certificate instead of penalty
  - DDU area mismatch at keys
  - storage room missing (B21)
  - installment increase before handover
  - KP without gas/water at keys
  - assignment refusal after payment
  - legal entity change + escrow (B20)
  - price increase after booking
  - family mortgage escrow matkapital (B19)
- **Closed clusters (30d):** B12 ddu_escrow_handover_delay; B21 cellar; B20 legal entity; all frozen secondary in used-clusters.json
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: аванс, эскроу, новостройка)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B23
- **title_draft:** В Тюмени семья перевела аванс на «эскроу» — счёт оказался чужим
- **slug:** v-tyumeni-semya-perevela-avans-na-eskrou-schet-okazalsya-chuzhim
- **cluster_id (new):** newbuild_wrong_escrow_beneficiary_account_tyumen
- **story_dup_check:** PASS — distinct from B19/B20 «эскроу не открылся / смена юрлица»; distinct from B22 rate change; plot = семья перевела крупный аванс на реквизиты «эскроу-счёта» из письма менеджера, банк перед подписанием ДДУ показал, что бенефициар и номер счёта не совпадают с застройщиком из проектной декларации — деньги зависли, сделку остановили

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, получила от отдела продаж реквизиты для перевода аванса «на эскроу», перевела сумму по QR/платёжке
- **risk:** счёт оказался открыт на другое юрлицо (или с ошибкой в реквизитах) — не тот бенефициар, который указан в проектной декларации и будущем ДДУ; банк отказался открывать ипотеку/эскроу до возврата или перечисления на правильный счёт
- **time:** за 2–5 дней до подписания ДДУ, после брони и одобрения ипотеки
- **finale:** семья остановила сделку; возврат денег затянулся на недели (споры с застройщиком/банком); бронь сгорела, квартира ушла другому покупателю; пришлось заново искать лот и проходить одобрение
- **comment_magnet_angle:** «Если менеджер прислал реквизиты в WhatsApp — вы бы перевели аванс без сверки с проектной декларацией или развернулись бы сразу?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild wrong-escrow-account casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-04)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| дду без эскроу | 55+11176 | 2 (weak; rework) |
| эскроу по дду | 55+11176 | 15 |
| эскроу счет новостройка | 55+11176 | 2 (rejected — B19/B20 cluster) |
| **договор долевого участия** | **55+11176** | **323** |
| договор долевого участия | 225 (compare) | 16196 |
| эскроу по дду | 225 (compare) | 1045 |
| 214 фз об участии в долевом строительстве | 55+11176 | 61 (context) |
| новостройки семейная ипотека тюмень | 55+11176 | 31 (context) |

**wordstat_rework log:**
- probe «дду без эскроу» 55+11176 → 2 (weak spine)
- probe «эскроу по дду» 55+11176 → 15 (escrow jargon ok but low)
- probe «эскроу счет новостройка» 55+11176 → 2 (plot overlap B19/B20)
- **rework:** localize Tyumen newbuild buyer jargon → **final P0 «договор долевого участия» regions 55,11176 freq 323** (compare RU225 16196)

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_51062/ — 214-ФЗ (эскроу, ДДУ)
- https://www.cbr.ru/finmarkets/supervision/sv_e/ — реестр эскроу-агентов ЦБ
- https://dzen.ru/holyslav — контекст новостроек, не дубль кластера
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B23, title, slug, signal_urls, research angles for Research role.
