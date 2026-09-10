# Scout inputs — 2026-09-10 (B24, slot ~12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-10 (YEKT weekday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 24 active locks (last_sync 2026-09-10)
- **Today 2026-09-10 already published (~09 slot):** «В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч» (cluster booking_expired_price_hike) — DO NOT reuse
- **Recent WP ~12 titles — DO NOT reuse plot/mechanism:**
  - балкон / проектная декларация vs ДДУ
  - неустойка за просрочку ключей + остановка приёмки
  - семейная ипотека: ребёнку 7 лет перед ДДУ
  - банк остановил транш после приёмки без замечаний
  - ключи без разрешения на ввод
  - переуступка: долг 94 тыс в день ДДУ
  - маткапитал + детские доли перед ключами
  - созаёмщика исключили за 7 дней до ДДУ
  - рассрочка застройщика: 5 дней просрочки → расторжение
  - коттедж: газ в ДДУ vs факт 180 м
  - этаж 12 в ДДУ → 2-й на ключах
- **Rejected candidates (BLOCKER or overlap):**
  - bank appraisal ниже ДДУ → H1 fingerprint duplicate
  - trade-in + «бронь» в hook → booking_expired cluster
  - acceptance defects + amount → fingerprint duplicate
  - mortgage revoked 72ч → слишком близко к B19/B20 escrow-сюжетам (helper PASS, но finish — чище для 12:00 слота)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду, новостройка)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени в ДДУ обещали чистовую — на ключах отдали предчистовую
- **slug:** v-tyumeni-v-ddu-obeschali-chistovuyu-na-klyuchah-otdali-predchistovuyu
- **article_dir:** memory/blog/articles/B24-v-tyumeni-v-ddu-obeschali-chistovuyu-na-klyuchah-otdali-predchistovuyu
- **cluster_id (new):** finish_package_mismatch_ddu_tyumen
- **story_dup_check:** PASS — distinct legal plot: в ДДУ и приложении к договору указан стандарт **чистовой** отделки от застройщика (обои, ламинат, сантехника в комплекте); на приёмке квартира сдана в **предчистовой/whitebox** (штукатурка, стяжка без финиша) → расхождение условий ДДУ, доплата за доработку или отказ подписать акт, спор о неустойке/компенсации

## Top-energy + newbuild lock

- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** расхождение стандарта отделки в ДДУ (чистовая) vs факт на ключах (предчистовая/whitebox)
- **why_newbuild_not_secondary:** только договор с застройщиком и приёмка новостройки; не ремонт на вторичке и не «косметика от продавца»

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке с чистовой отделкой по ДДУ, дождалась ключей
- **risk:** на приёмке стены без обоев, пол без финишного покрытия, санузел без комплекта — фактически предчистовая; застройщик ссылается на приложение/изменение проекта; доплата на доработку или угроза неустойки за затягивание подписания акта
- **time:** на приёмке / в первые 48 часов после уведомления о сдаче дома
- **finale:** семья отказалась подписывать акт без фиксации расхождения; застройщик насчитал «просрочку приёмки» или предложил допсоглашение с доплатой; спор ушёл в претензию (или суд по требованию привести отделку к ДДУ / снизить цену)
- **comment_magnet_angle:** «В акте написали „без замечаний“, а отделка не та, что в ДДУ — вы бы всё равно подписали ключи или шли в претензию, даже если застройщик грозит неустойкой за затягивание?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen finish-mismatch casus without Klyshin; avoids today's booking cluster and recent priemka/bank/defect plots)

## Wordstat MCP-KV (live 2026-09-10)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| чистовая отделка новостройка | 55+11176 | 34 |
| отделка новостройка | 55+11176 | 260 |
| **отделка квартир в новостройках** | **55+11176** | **173** |
| новостройки отделкой тюмень | 55+11176 | 44 |
| новостройки тюмень | 55+11176 | 4642 |
| **отделка квартир в новостройках** | **225 (compare)** | **21063** |
| купить новостройку в тюмени | 55+11176 | 885 |

**wordstat_rework log:**
- probe «чистовая отделка новостройка» 55+11176 → 34 (on-topic but weak)
- probe «отделка новостройка» 55+11176 → 260; top child «отделка квартир в новостройках» → **173**
- probe «новостройки тюмень» 55+11176 → 4642 (broad spine, kept as context)
- **rework:** localize Tyumen + finish jargon (чистовая, предчистовая, ДДУ, приёмка) → **final P0 «отделка квартир в новостройках» regions 55,11176,compare225 freq 173 (55+11176) / 21063 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ, приёмка объекта долевого строительства
- https://www.domrf.ru/ — справочник застройщиков / стандарты отделки
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, article_dir, signal_urls, research angles for Research role.
