# Scout inputs — 2026-09-02 (B21)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-02 (UTC slot 05:00 / YEKT 10:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks
- **FROZEN newbuild plots (DO NOT reuse):**
  - B20 `newbuild_developer_legal_entity_change_ddu_escrow_tyumen` — застройщик сменил юрлицо / эскроу
  - B19 `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` — семейная ипотека / эскроу / маткапитал
  - B12 `ddu_escrow_handover_delay_tyumen` — перенос ключей на год / эскроу заморозили
  - LIVE `newbuild_reservation_price_spike_48h` — бронь +380к за 2 суток (slug v-tyumeni-zabronirovali-novostrojku-cherez-dvoe-sutok-cenu-podnyali-na-380-tysya)
  - LIVE `newbuild_acceptance_wet_screed_keys_denied` — приёмка мокрая стяжка / ключи не выдали
  - LIVE `transhevaya_ipoteka_payment_spike` — платёж вырос в 8 раз до брони
- Live WP ~20 (2026-09-02): B20 legal entity; reservation +380k; B19 family mortgage escrow; wet screed acceptance; tranche mortgage spike; kapremont secondary; double sale; forged spouse; matkapital child shares; propisannye; communal share; closed mortgage cert; predvaritelny dogovor; kladovka; akkreditiv; priostanovili registraciyu; opeka nad prodavcom; najm s pravom vykupa; B12 key delay; Yalutorovsk double sale
- Ledger B02–B20 in `shared/published-articles.md`

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B21
- **title_draft:** В Тюмени оплатили переуступку в новостройке — застройщик отказал переоформлять ДДУ
- **slug:** v-tyumeni-oplatili-pereustupku-zastrojschik-otkazal-pereoformit-ddu
- **cluster_id (new):** newbuild_assignment_developer_refused_dd_reregistration_tyumen
- **story_dup_check:** PASS — distinct from B12/B19/B20 (эскроу/срок сдачи/юрлицо), live reservation price spike, wet screed acceptance, tranche mortgage; plot = покупатель оплатил переуступку прав по ДДУ, застройщик отказал в переоформлении / в реестре остался прежний дольщик, деньги у цедента

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в строящемся ЖК по переуступке — подписали договор с продавцом уступки, внесли аванс и пошли к застройщику за переоформлением ДДУ
- **risk:** застройщик отказал регистрировать нового дольщика (не согласована уступка / в реестре числится другой участник / требования банка-эскроу не выполнены) — деньги ушли цеденту, а право требования так и не закрепилось за покупателем
- **time:** за два дня до визита в банк на открытие эскроу / подписание ДДУ с застройщиком
- **finale:** сделку остановили до эскроу; бронь в офисе продаж сняли; аванс пришлось выбивать через претензию к продавцу уступки; квартиру ушла в свободную продажу, семья вернулась к поиску с потерянным месяцем
- **comment_magnet_angle:** «Переуступку в новостройке оплачиваете до согласия застройщика — или сначала письмо из офиса продаж, что уступку зарегистрируют?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild assignment casus without Klyshin — preferred; avoids B12/B19/B20 and live WP newbuild plots)

## Wordstat MCP-KV (live 2026-09-02)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройка тюмень | 55+11176 | API empty (retry fail) |
| переуступка новостройки | 55+11176 | 10 |
| риски переуступки новостройки | 55+11176 | 2 |
| покупка квартиры в новостройке переуступка | 55+11176 | 4 |
| переуступка новостройки | 225 (compare) | 2422 |
| переуступка новостройка | 225 (compare) | 2422 |
| новостройки тюмень купить | 55+11176 | 1192 (context) |
| **купить новостройку в тюмени** | **55+11176** | **874** |
| купить новостройку в тюмени | 225 (compare) | 1882 |
| купить новостройку в тюмени в ипотеку | 55+11176 | 93 |

**wordstat_rework log:**
- probe «переуступка новостройка тюмень» 55+11176 → API empty
- probe «переуступка новостройки» 55+11176 → 10 (on-plot but weak Tyumen volume)
- probe «риски переуступки новостройки» 55+11176 → 2
- probe «покупка квартиры в новостройке переуступка» 55+11176 → 4
- compare RU225 «переуступка новостройки» → 2422 (national demand confirms plot)
- rework: localize Tyumen + newbuild buyer jargon (ДДУ, новостройка) → probe «купить новостройку в тюмени» 55+11176 → **874** (compare RU225 1882); on-plot secondary «переуступка новостройки» 10 retained for H1 spine

## signal_urls (research)

- sibling B20 slug v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot (interlink DDU/эскроу)
- sibling B19 slug semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli (interlink семейная ипотека)
- https://www.consultant.ru/document/cons_doc_LAW_122902/ — 214-ФЗ: уступка прав требования по ДДУ
- https://dzen.ru/holyslav — канал, newbuild casus energy
- https://t.me/klyshin_A — checked, not used this slot
- tenant blog index via scout_signal_urls in tenant-config

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B21, title, slug, signal_urls, research angles for Research role.
