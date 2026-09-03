# Scout inputs — 2026-09-03 (B22)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-03 (YEKT Thursday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks
- **FROZEN today (03 Sep 2026 live plots — DO NOT reuse):**
  - `newbuild_keys_delayed_penalty_certificate` — «В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом»
  - `newbuild_acceptance_area_mismatch` — «В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте»
  - `newbuild_installment_balance_increase` — «В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли»
  - `newbuild_cottage_utilities_missing` — «В Тюмени дом сдали без газа и воды — семья не взяла ключи»
  - `newbuild_assignment_refused` — «В Тюмени оплатили переуступку — застройщик не оформил ДДУ»
- **Closed clusters (30d):** B21 `newbuild_ddu_cellar_paid_not_handed_tyumen`; B20 `newbuild_developer_legal_entity_change_ddu_escrow_tyumen`; B19 family mortgage escrow; B12 escrow delay; all frozen secondary in used-clusters.json
- Live WP ~20 (EXCALIBUR_RECENT_WP_POSTS 2026-09-03): today's keys delay, area mismatch, installment increase, cottage utilities, assignment refusal; B21 kladovka; B20 юрлицо; booking price +380k; wet screed priemka; transhevaya ipoteka
- `published-titles-only.md` + `shared/published-articles.md` — B02–B21 ledger

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B22
- **title_draft:** В Тюмени на показе была чистовая — в ДДУ оказалась предчистовая
- **slug:** v-tyumeni-na-pokaze-chistovaya-v-ddu-predchistovaya
- **cluster_id (new):** newbuild_showroom_finish_ddu_mismatch_tyumen
- **story_dup_check:** PASS — distinct from area mismatch priemka (метры), wet screed, installment increase, keys delay, kladovka B21, юрлицо B20; plot = на шоу-руме/показе застройщик демонстрировал квартиру с чистовой отделкой, в тексте ДДУ и приложении — предчистовая/без отделки; семья остановилась перед авансом после сверки приложения

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке после осмотра шоу-рума с чистовой отделкой (ламинат, обои, сантехника); менеджер устно подтвердил «так и сдадим»
- **risk:** в проекте ДДУ и приложении к договору указан иной вид отделки — предчистовая/white box; стоимость «доделки» до уровня показа не входит в цену; при отказе подписывать — сгорает бронь
- **time:** в день подписания ДДУ в офисе продаж, за сутки до истечения брони
- **finale:** семья отказалась от аванса, бронь сняли; через неделю аналогичную планировку продали другому покупателю; доплата за чистовую по прайсу застройщика оказалась на 420–480 тыс. выше ожиданий
- **comment_magnet_angle:** «Шоу-рум с чистовой — вы всё равно подписываете ДДУ, если в приложении написано „предчистовая“?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild finish/DDU casus without Klyshin — preferred; avoid today's priemka area/wet-screed plots)

## Wordstat MCP-KV (live 2026-09-03)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| отделка новостройки | 55+11176 | 274 |
| новостройки отделкой тюмень | 55+11176 | 44 |
| приемка квартиры в новостройке тюмень | 55+11176 | 32 |
| дду новостройка | 55+11176 | 20 (weak standalone) |
| новостройки тюмень | 55+11176 | 4683 |
| купить новостройку в тюмени | 55+11176 | 866 |
| купить новостройку в тюмени | 225 (compare) | 1872 |
| новостройки с отделкой | 55+11176 | 127 |

**wordstat_rework log:**
- probe «дду новостройка» 55+11176 → 20 (weak P0)
- probe «приемка квартиры в новостройке тюмень» 55+11176 → 32 (on-plot but narrow)
- probe «новостройки отделкой тюмень» 55+11176 → 44 (on-plot secondary)
- probe «отделка новостройки» 55+11176 → 274 (broad)
- probe «новостройки тюмень» 55+11176 → 4683 (too broad for P0 spine)
- **rework:** buyer jargon newbuild+purchase Tyumen → **final P0 «купить новостройку в тюмени» regions 55,11176 freq 866** (compare RU225 1872); on-plot secondary «новостройки отделкой тюмень» 44

## signal_urls (research)

- https://dzen.ru/holyslav — контекст приёмки и отделки в новостройках; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ долевое строительство, приложение к ДДУ
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/[REDACTED]

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B22, title, slug, signal_urls, research angles for Research role.
