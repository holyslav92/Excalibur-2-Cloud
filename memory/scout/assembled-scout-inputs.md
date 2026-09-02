# Scout inputs — 2026-09-02 (B21)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-02 (YEKT Wednesday slot 17:00 — 4th weekday longform)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks
- **FROZEN today (02 Sep 2026 live plots — DO NOT reuse):**
  - `newbuild_installment_ddu_balance_raised_before_handover` — «В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли»
  - `newbuild_assignment_paid_developer_refused_reregister` — «В Тюмени оплатили переуступку — застройщик не оформил ДДУ»
  - `newbuild_kp_utilities_missing_at_keys` — «В Тюмени дом сдали без газа и воды — семья не взяла ключи»
  - `newbuild_acceptance_wet_screed_keys_denied` — «На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали»
  - `newbuild_booking_price_spike_48h` — «Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч»
  - `transhevaya_ipoteka_payment_spike` — «Платёж по новостройке вырос в 8 раз — до брони»
- **Closed clusters (30d):** B20 `newbuild_developer_legal_entity_change_ddu_escrow_tyumen`; B19 `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen`; B12 `ddu_escrow_handover_delay_tyumen`; all frozen secondary clusters in used-clusters.json
- Live WP ~20 (EXCALIBUR_RECENT_WP_POSTS 2026-09-02): рассрочка ДДУ остаток; переуступка отказ; КП без газа/воды; мокрая стяжка; бронь +380к; B20 юрлицо; B19 семейная ипотека эскроу; transhevaya ipoteka; kapremont secondary; double sale; forged spouse; matkapital child shares
- `published-titles-only.md` + `shared/published-articles.md` — B02–B20 ledger
- `scout_helper --check-query` → PASS; `topic_focus.py` → PASS; `story_dup.py --text` → PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup)

- **topic_id:** B21
- **title_draft:** В Тюмени оплатили кладовку по ДДУ — на ключах помещения не было
- **slug:** v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomeshcheniya-ne-bylo
- **cluster_id (new):** newbuild_ddu_cellar_paid_not_handed_tyumen
- **story_dup_check:** PASS — distinct from today's priemka wet screed (construction defect), КП utilities missing, B12 handover delay, B20 entity change, B19 escrow/matkapital; plot = accessory object (кладовка) named in ДДУ and paid in price, but not handed over at keys / wrong number / not in acceptance act

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке; в ДДУ отдельной строкой указана кладовка с номером и площадью, сумма включена в цену договора и оплачена на эскроу
- **risk:** на выдаче ключей кладовку не передали — «ещё не построили», «номер изменился», «это опция, не объект ДДУ»; в акте приёма-передачи кладовки нет
- **time:** в день выдачи ключей / на приёмке квартиры через 14 месяцев после подписания ДДУ
- **finale:** семья подписала акт только на квартиру под давлением срока ипотеки; кладовку обещали «допишут потом» — через два месяца застройщик предложил другое помещение меньшей площади или доплату 180 тыс.; спор ушёл в претензию, ключи от квартиры уже получены — вернуть всё назад дороже
- **comment_magnet_angle:** «Кладовку прописали в ДДУ с номером — вы подписываете акт приёмки квартиры, если кладовку не передали?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild DDU accessory casus without Klyshin — preferred; no overlap with today's live plots)

## Wordstat MCP-KV (live 2026-09-02)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| паркинг новостройка тюмень | 55+11176 | 2 (rejected — weak volume) |
| кладовка дду новостройка | 55+11176 | 0 (rejected — no data) |
| паркинг в дду | 55+11176 | 0 (rejected — no data) |
| кладовка новостройка | 55+11176 | 25 |
| купить кладовку в новостройке | 55+11176 | 19 |
| **купить кладовку в новостройке тюмень** | **55+11176** | **18** |
| купить кладовку в новостройке тюмень | 225 (compare) | 19 |
| отделка под ключ новостройка | 55+11176 | 22 (rejected — overlap risk with today's priemka acceptance cluster) |
| приемка новостройки тюмень | 55+11176 | 35 (rejected — today's wet screed plot) |
| новостройки тюмень | 55+11176 | 4649 (context only — too broad) |

**wordstat_rework log:**
- probe «паркинг новостройка тюмень» 55+11176 → 2 (weak P0)
- probe «кладовка дду новостройка» 55+11176 → 0 (weak)
- probe «кладовка новостройка» 55+11176 → 25; local «купить кладовку в новостройке» → 19
- **rework:** newbuild buyer jargon accessory object Tyumen → **final P0 «купить кладовку в новостройке тюмень» regions 55,11176 freq 18** (compare RU225 19)

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ: предмет ДДУ, нежилые помещения в составе объекта
- https://dom.gosuslugi.ru — приёмка долевого строительства, акт приёма-передачи
- https://dzen.ru/holyslav — контекст новостроек и ДДУ; не дубль кластера
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B21, title, slug, signal_urls, research angles for Research role.
