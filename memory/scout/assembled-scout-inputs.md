# Scout inputs — 2026-09-06 (B28)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-06 (YEKT weekend automation slot 09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## topic_id confirmation

- **Next free topic_id:** B28 (B23–B27 used; repo article dirs end at B23; live WP published B24–B27 on 2026-09-05)
- **article_dir:** `memory/blog/articles/B28-v-tyumeni-zastrojschik-potreboval-doplatu-za-uluchshennuyu-otdelku-pered-klyuchami`

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 29 active locks (last_sync 2026-09-06)
- **Live WP ~12 titles (2026-09-05) — DO NOT reuse plot:**
  - B23 / LIVE: банк оценка ниже ДДУ + апартаменты вместо квартиры в ЕГРН
  - B24 / LIVE: переуступка +280к за сутки до ДДУ — бронь сгорела
  - B25 / LIVE: рассрочка застройщика — досрочное погашение сжегло скидку
  - B26 / LIVE: приёмка брак → штраф застройщика ~190к
  - B27 / LIVE: ключи задержали 7 месяцев — неустойка 340к не выплачена
  - trade-in сорвался за день до ДДУ
  - инвестор: аренда запрещена до ключей
  - категория земли сорвала ипотеку на дом в КП
  - аванс на чужой эскроу-счёт
  - ДДУ 45 м² vs декларация 41 м²
  - банк снял одобрение за 72ч до ДДУ
  - ключи 8 мес — неустойка сертификатом
- **Frozen clusters (user list + used-clusters.json):** trade-in, wet screed приёмка, юрлицо/escrow swap, tranche 8×, spouse consent, sold twice, EGRN caprepair, parking/cellar B21, legal entity B20, bank rate B22, escrow B19, investor rental ban, bank withdrew 72h, keys 8mo certificate, DDU m² mismatch, wrong escrow, land category KP — all CLOSED
- **Rejected overlap:** «чистовая vs предчистовая в ДДУ» (live) — наш угол = **доплата за улучшенную отделку не из ДДУ перед ключами**, другая механика (stopped_before_money, не классификация отделки)
- **Rejected overlap:** bank appraisal below DDU (B23 cluster) — не оценка банка, а требование доплаты застройщиком
- **Rejected overlap:** acceptance defects penalty B26 — не брак при приёмке, а навязанная доплата за пакет отделки
- `scout_helper.py --check-query` PASS
- `excalibur_blog_scout_story_dup.py --text` PASS
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B28
- **title_draft:** В Тюмени застройщик потребовал доплату за улучшенную отделку перед ключами — в ДДУ её не было
- **slug:** v-tyumeni-zastrojschik-potreboval-doplatu-za-uluchshennuyu-otdelku-pered-klyuchami
- **cluster_id (new):** newbuild_extra_finish_payment_not_in_ddu_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** застройщик на выдаче ключей требует доплату ~280–320 тыс. за пакет «улучшенной отделки», которого нет в ДДУ и приложениях — менеджер обещал устно на показе; без доплаты ключи не отдают
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ → сдача дома → приёмка/ключи у застройщика новостройки; нет продавца вторички, ЕГРН-вторички или сделки с физлицом
- **story_dup_check:** PASS — новый cluster_id; механика «доплата за отделку не из договора» не пересекается с B26 (штраф за брак), B27 (неустойка за срок), B25 (рассрочка/скидка), B23 (апартаменты/оценка)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке по ДДУ с предчистовой отделкой, внесла деньги на эскроу, дом сдали, пригласили на ключи
- **risk:** в офисе застройщика выставили доплату ~300 тыс. за «улучшенную отделку» (ламинат, натяжные потолки, сантехника) — в ДДУ и спецификации только предчистовая; без оплаты отказали выдавать ключи и акт
- **time:** в день выдачи ключей / за 48 часов до подписания акта приёмки-передачи (после 2,5 года ожидания сдачи)
- **finale:** семья отказалась платить «с потолка», зафиксировала отказ письменно, подала претензию; застройщик частично отступил или спор ушёл в досудебку — ключи получили только после проверки приложений к ДДУ (или суд/Роспотребнадзор)
- **comment_magnet_angle:** «Менеджер на показе обещал „улучшенную отделку“, в ДДУ — предчистовая: вы бы доплатили 300 тысяч за ключи или пошли в суд, даже если ребёнок уже ждёт переезд?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild finish-payment casus without Klyshin — preferred; avoids B23–B27 live plots)

## Wordstat MCP-KV (live 2026-09-06)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| улучшенная отделка новостройка | 55+11176 | 3 (totalCount only — weak) |
| отделка новостройка дду | 55+11176 | 1 (totalCount only — weak) |
| отделка новостройка | 55+11176 | 269 |
| отделка новостроек тюмень (child) | 55+11176 | 42 |
| новостройки с отделкой от застройщика (child) | 55+11176 | 59 |
| **новостройки тюмень** | **55+11176** | **4660** |
| **новостройки тюмень** | **225 (compare)** | **8705** |
| купить новостройку в тюмени (context) | 55+11176 | 856 |

**wordstat_rework log:**
- probe «улучшенная отделка новостройка» 55+11176 → 3 (weak angle-specific)
- probe «отделка новостройка дду» 55+11176 → 1 (weak)
- probe «отделка новостройка» 55+11176 → 269; child «отделка новостроек тюмень» → 42 (localized but below spine)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, отделка застройщика) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4660 (55+11176) / 8705 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_122478/ — 214-ФЗ ДДУ, состав работ/отделка в договоре
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Gate results (conductor verified)

- story_dup_check: PASS | cluster_id: newbuild_extra_finish_payment_not_in_ddu_tyumen
- h1_fingerprint_check: PASS | fingerprint: extra_finish_payment:ddu_not_listed (distinct from keys_delay_penalty / 190k / 340k)
- formula_spam_check: PASS | last3_mechanisms: apartments_egistr_mismatch, assignment_price_hike, developer_installment_discount_burn (B23–B25 live — different skeleton)
- anti_dupe_hard: PASS
- topic_focus: PASS

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard.

Lock topic_id B28, title, slug, signal_urls, article_dir, research angles for Research role.
