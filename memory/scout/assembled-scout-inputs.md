# Scout inputs — 2026-09-03 (B22)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-03 (YEKT Thursday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks
- Live WP ~20 fetched 2026-09-03 via wordpress_get_posts (newest first)
- **FROZEN plots (30d / recent live — DO NOT reuse):**
  - `newbuild_ddu_area_mismatch_keys_tyumen` — 2026-09-03 «В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте» (slug v-tyumeni-ploschad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry)
  - `newbuild_ddu_cellar_paid_not_handed_tyumen` — B21 кладовка по ДДУ
  - `newbuild_ddu_installment_balance_raised_before_handover_tyumen` — 2026-09-02 рассрочка остаток подняли
  - `newbuild_kp_utilities_not_connected_keys_tyumen` — 2026-09-02 КП без газа/воды
  - `newbuild_assignment_paid_developer_refused_reregister_tyumen` — 2026-09-02 переуступка застройщик отказал
  - `newbuild_developer_legal_entity_change_ddu_escrow_tyumen` — B20
  - `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` — B19
  - `newbuild_booking_price_increase_weekend_tyumen` — 2026-09-01 бронь +380 тыс
  - `newbuild_acceptance_wet_screed_keys_denied` — 2026-09-01 мокрая стяжка
  - `transhevaya_ipoteka_payment_spike` — 2026-08-31 траншевая ипотека
  - `ddu_escrow_handover_delay_tyumen` — B12 перенос сдачи / эскроу заморозили (другой plot: деньги уже на эскроу)
  - all frozen secondary clusters in `memory/scout/used-clusters.json`
- `published-titles-only.md` + `shared/published-articles.md` — B02–B21 ledger

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B22
- **title_draft:** В Тюмени застройщик задержал ключи на 8 месяцев — неустойку предложили сертификатом
- **slug:** v-tyumeni-zastrojschik-zaderzhal-klyuchi-neustojku-predlozhili-sertifikatom
- **cluster_id (new):** newbuild_developer_delay_penalty_certificate_instead_cash_tyumen
- **story_dup_check:** PASS — distinct from B12 (перенос сдачи + заморозка эскроу после внесения), today’s area-at-acceptance plot, wet screed priemka, booking price +380k, B20 legal entity, B19 matkapital; plot = просрочка передачи по ДДУ → начисление неустойки по 214-ФЗ → застройщик предлагает сертификат/бонус на отделку вместо денежной выплаты → семья теряет часть компенсации при двойной нагрузке ипотека+аренда

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени подписала ДДУ на квартиру в новостройке с жёсткой датой передачи в договоре
- **risk:** застройщик перенёс выдачу ключей на 8 месяцев; по договору и 214-ФЗ набежала неустойка; на выдаче ключей менеджер предложил подписать допсоглашение — сертификат на отделку/кладовку вместо денежной выплаты
- **time:** «через 8 месяцев после срока в ДДУ» / «в день выдачи ключей»
- **finale:** семья подписала допсоглашение с сертификатом, денежную неустойку получила частично или в «бумажном» виде; 8 месяцев платили ипотеку и аренду без компенсации — итоговая сумма потерь больше номинала сертификата
- **comment_magnet_angle:** «Просрочили сдачу на полгода — вы бы взяли сертификат на отделку вместо неустойки по ДДУ или пошли бы в суд?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild delay-penalty casus without Klyshin — preferred; avoid priemka/area/wet-screed clusters and B12 escrow-freeze spine)

## Wordstat MCP-KV (live 2026-09-03)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | region 55 | region 11176 | notes |
|-------|-----------|--------------|-------|
| неустойка застройщик дду | 16 | 17 | weak on-plot |
| долгострой тюмень | 82 | — | narrow / news noise |
| неустойка застройщик | 118 | 139 | on-plot cluster |
| неустойка с застройщика (exact) | 44 | 53 | on-plot exact |
| приемка новостройки | 101 | — | rejected — priemka cluster saturated |
| новостройки тюмени от застройщика | 728 | 924 | context only |
| неустойка застройщик | 225 compare | 8500 | RU compare |

**wordstat_rework log:**
- probe «неустойка застройщик дду» 55→16, 11176→17 (weak P0, 33 combined)
- probe «долгострой тюмень» 55→82 (narrow, off-spine for penalty claim)
- probe «приемка новостройки» 55→101 (rejected — live priemka plots 2026-09-01/03 closed)
- probe «неустойка застройщик» 55→118, 11176→139 → **rework accepted as final P0 cluster** (257 combined regional phrase total; on-plot buyer jargon)
- context: «новостройки тюмени от застройщика» 55→728, 11176→924; RU225 «неустойка застройщик»→8500

**Final P0:** «неустойка застройщик» regions 55+11176 freq **257** (55: 118 + 11176: 139); compare RU225 **8500**

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_122165/ — 214-ФЗ о долевом строительстве (неустойка за просрочку)
- https://dzen.ru/holyslav — sibling engagement context, не дубль plot
- https://t.me/klyshin_A — checked, not used this slot
- tenant scout_signal_urls: PUBLIC_SITE_URL/blog/ (env, not hardcoded)
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B22, title, slug, signal_urls, research angles for Research role.
