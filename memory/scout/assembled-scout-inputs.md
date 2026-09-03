# Scout inputs — 2026-09-03 (B22)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-03 (YEKT slot ~12:00 UTC 12:04)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks
- **FROZEN today (03 Sep 2026 live plots — DO NOT reuse):**
  - finishing mismatch — «В тюменской новостройке показали чистовую — в ДДУ была предчистовая»
  - delay + certificate penalty — «В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом»
  - area mismatch at acceptance — «В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте»
- **Closed newbuild clusters (30d):** newbuild_ddu_cellar_paid_not_handed_tyumen (B21); newbuild_developer_legal_entity_change_ddu_escrow_tyumen (B20); semejnaya ipoteka escrow (B19); installment raised before delivery (live 2026-09-02); assignment refused (live 2026-09-02); KP utilities missing (live 2026-09-02); B12 ddu_escrow_handover_delay
- `topic_focus.py` PASS; `scout_helper.py --check-query` PASS — NO CANNIBALIZATION RISK

## Proposed topic (PASS all gates)

- **topic_id:** B22
- **title_draft:** В Тюмени банк снял одобрение ипотеки на новостройку — бронь сгорела за три дня до ДДУ
- **slug:** v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela
- **cluster_id (new):** newbuild_mortgage_approval_withdrawn_booking_lost_tyumen
- **story_dup_check:** PASS — distinct from B19 (эскроу/маткапитал), B20 (смена юрлица), B21 (кладовка), today's priemka/отделка/задержка plots; plot = банк отозвал одобрение ипотеки на новостройку за 3 дня до подписания ДДУ, бронь сгорела, квартиру продали другому

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, внесла плату за бронь, банк выдал одобрение ипотеки и согласовал схему с застройщиком
- **risk:** за три дня до подписания ДДУ банк повторно проверил доход/кредитную историю и **снял одобрение** — без нового банка ДДУ подписать нельзя, срок брони истекает
- **time:** за 72 часа до дедлайна брони / подписания ДДУ (после первичного одобрения ипотеки)
- **finale:** бронь сгорела, квартиру ушла другому покупателю; плату за бронирование вернули частично или не вернули (штраф по условиям офиса продаж); семья заново искала объект и банк 2–3 недели
- **comment_magnet_angle:** «Банк снял одобрение за три дня до ДДУ — вы успели бы найти другой банк или отказались бы от этой квартиры?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild mortgage casus without Klyshin — preferred; no duplicate of closed clusters)

## Wordstat MCP-KV (live 2026-09-03)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| бронь новостройка | 55+11176 | 3 (rejected — weak) |
| ипотека на новостройку тюмень | 55+11176 | 58 → child «ипотека в тюмени на новостройки» 41 |
| одобрение ипотеки новостройка | 55+11176 | empty (rejected) |
| машино-место новостройка | 55+11176 | empty (rejected) |
| приемка квартиры новостройка | 55+11176 | 126 (rejected — today's priemka plot closed) |
| новостройки тюмень | 55+11176 | 4683 (context spine) |
| новостройки тюмень | 225 compare | 8767 |
| **купить новостройку в тюмени в ипотеку** | **55+11176** | **86** |
| купить новостройку в тюмени в ипотеку | 225 compare | 130 |

**wordstat_rework log:**
- probe «бронь новостройка» 55+11176 → 3 (weak P0)
- probe «ипотека в тюмени на новостройки» 55+11176 → 41 (on-plot but narrow)
- probe «новостройки тюмень» 55+11176 → 4683 (strong spine, less mortgage-specific)
- **rework:** buyer jargon mortgage+newbuild Tyumen → **final P0 «купить новостройку в тюмени в ипотеку» regions 55,11176 freq 86** (compare RU225 130)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст ипотеки на новостройку в Тюмени; не дубль кластера B19/B20
- https://www.cbr.ru/finmarkets/files/supervision/sv_letters/2024/in_16-6-1_2024-03-15.pdf — ЦБ: требования к ипотечному кредитованию (контекст повторной проверки заёмщика)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B22, title, slug, signal_urls, research angles for Research role.
