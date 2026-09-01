# Scout inputs — 2026-09-01 (B20)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-01 (YEKT Monday slot 12:00 UTC automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- **FROZEN today (01 Sep 2026 live plots — DO NOT reuse):**
  - `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` — B19 longform «Семейную ипотеку на новостройку одобрили — эскроу не открыли» (family mortgage + matkapital escrow)
  - `newbuild_booking_price_increase_48h` — daily «Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч»
  - `newbuild_acceptance_wet_screed_keys_denied` — daily «На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали»
  - `transhevaya_ipoteka_payment_spike` — «Платёж по новостройке вырос в 8 раз — до брони»
- **Closed clusters (30d):** B12 `ddu_escrow_handover_delay_tyumen` (перенос сдачи на год / эскроу заморозили после внесения); all frozen secondary clusters in used-clusters.json
- Live WP ~20 (EXCALIBUR_RECENT_WP_POSTS 2026-09-01): booking +380k; B19 family mortgage escrow; wet screed priemka; transhevaya ipoteka; kapremont secondary; double sale; forged spouse B15; matkapital child shares; propisannye; communal share; closed mortgage cert B14; predvaritelny dogovor
- `published-titles-only.md` + `shared/published-articles.md` — B02–B15, B19 ledger

## Proposed topic (PASS topic_focus + scout_helper --check-query + story_dup PASS)

- **topic_id:** B20
- **title_draft:** В Тюмени застройщик сменил юрлицо — дольщикам прислали новый ДДУ, эскроу не открыли
- **slug:** v-tyumeni-zastrojshchik-smenil-yurlico-dolshchikam-prislali-novyj-ddu-eskrou-ne-otkryli
- **cluster_id (new):** newbuild_developer_legal_entity_change_ddu_escrow_tyumen
- **story_dup_check:** PASS — distinct from B19 (семейная ипотека + маткапитал блокирует эскроу), B12 (перенос сдачи / заморозка после внесения), today's booking price spike, today's wet screed priemka; plot = реорганизация застройщика → смена юрлица в ДДУ → банк не открывает эскроу на нового контрагента → сделка сорвалась до внесения

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, подписала ДДУ с одним юрлицом застройщика и получила одобрение ипотеки под эскроу-схему
- **risk:** через несколько месяцев застройщик прошёл реорганизацию (слияние/преобразование), в офис продаж прислали новый ДДУ уже от другого ООО с иными реквизитами эскроу-счёта — банк отказал открывать эскроу на незнакомого контрагента без переаккредитации
- **time:** через четыре месяца после подписания первого ДДУ / за 72 часа до дедлайна брони
- **finale:** семья отказалась переподписывать «новый» ДДУ вслепую, бронь сгорела, квартиру выставили в свободную продажу; первоначальный взнос за бронь вернули не полностью, очередь на объект потеряли
- **comment_magnet_angle:** «Застройщик сменил юрлицо и прислал новый ДДУ — вы подписываете или выходите из сделки, даже если квартира «та же»?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild developer-reorganization casus without Klyshin — preferred; avoid B19/B12 escrow clusters and today's booking/priemka plots)

## Wordstat MCP-KV (live 2026-09-01)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| застройщик реорганизация | 55+11176 | 3 (rejected — weak standalone) |
| реорганизация застройщика | 55+11176 | 3 (rejected — weak) |
| дду эскроу | 55+11176 | 38 (on-plot secondary; overlap risk B12/B19) |
| новостройки тюмень | 55+11176 | 4667 (context — too broad) |
| **новостройки в тюмени от застройщика** | **55+11176** | **651** |
| новостройки в тюмени от застройщика | 225 (compare) | 1268 |
| купить новостройку в тюмени от застройщика | 55+11176 | 413 (secondary) |
| коттеджные поселки тюмень | 55+11176 | 1843 (alternate angle — not chosen; different plot) |
| приемка квартиры в новостройке | 55+11176 | 109 (rejected — today's wet screed daily) |

**wordstat_rework log:**
- probe «застройщик реорганизация» 55+11176 → 3 (weak P0)
- probe «реорганизация застройщика» 55+11176 → 3 (weak P0)
- probe «дду эскроу» 55+11176 → 38 (on-plot but narrow; escrow spine overlaps B12/B19)
- probe «новостройки тюмень» 55+11176 → 4667 (too broad)
- **rework:** buyer jargon newbuild+developer Tyumen → **final P0 «новостройки в тюмени от застройщика» regions 55,11176 freq 651** (compare RU225 1268)

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_122165/ — 214-ФЗ о долевом участии (смена застройщика / правопреемство)
- https://www.cbr.ru/finmarkets/ — аккредитация застройщика и эскроу-счета (банк)
- https://dzen.ru/holyslav — контекст новостроек Тюмени; не дубль кластера
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B20, title, slug, signal_urls, research angles for Research role.
