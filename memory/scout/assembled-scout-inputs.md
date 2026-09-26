# Scout inputs — 2026-09-26 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-26 (YEKT Saturday automation slot 10:00 UTC cron)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — live WP ~20)

- NO area minus 1.8m BTI vs DDU (2026-09-26 live)
- NO KP 12 vs 8 sotok kadastr (2026-09-25)
- NO partial commissioning section (2026-09-25)
- NO parking separate DDU (2026-09-25)
- NO assignment torn + 150k (2026-09-25)
- NO last floor mortgage 4d (2026-09-24)
- NO matkapital SFR escrow line (2026-09-24)
- NO kindergarten on render (2026-09-24)
- NO child 7 family mortgage day of DDU (2026-09-23)
- NO forest fence neighbor KP (2026-09-23)
- NO furniture package partner (2026-09-23)
- NO co-borrower refused escrow (2026-09-23)
- NO frozen secondary clusters in used-clusters.json

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 2026-09-26
- `scout_helper.py --check-query` PASS (fingerprint booking_expired; mechanism layout swap distinct from BTI area / booking price hikes)
- `excalibur_blog_topic_focus.py` PASS (дду)
- `story_dup.py --text` PASS fingerprint + formula spam OK

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** В Тюмени за 5 дней до ДДУ в новостройке поменяли планировку — в брони 54 квадрата, в проекте 49
- **slug:** v-tyumeni-za-5-dnej-do-ddu-v-novostrojke-smenili-planirovku-bron-54-v-proekte-49
- **article_dir:** memory/blog/articles/B33-v-tyumeni-za-5-dnej-do-ddu-v-novostrojke-smenili-planirovku-bron-54-v-proekte-49
- **cluster_id (new):** newbuild_layout_area_mismatch_before_ddu_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья с ребёнком бронирует двухкомнатную в ЖК в Тюмени: в брони и на визуализации — 54,2 м², евродвушка с лоджией. За 5 дней до подписания ДДУ менеджер присылает новый лист планировки из проектной декларации: 49,1 м², другая конфигурация комнат, цена в ДДУ не снижается. Банк пересчитывает одобрение; семья останавливает сделку до эскроу
- **why_newbuild_not_secondary:** Только цепочка первички: бронь застройщика, приложение к ДДУ, площадь и план из проектной декларации 214-ФЗ, ипотека на новостройку. Нет продавца вторички, ЕГРН-вторички, наследников, опеки
- **story_dup_check:** PASS — distinct from BTI -1.8m acceptance (приёмка/BTI), land lease B27, chistovaya B25, assignment B30, parking separate DDU

## Dzen news-casus shape (PASS)

- **event:** семья выбрала двушку в тюменском ЖК; в брони зафиксировали площадь 54 м² и планировку с лоджией
- **risk:** меньшая площадь и другая планировка бьют по ипотечному одобрению и по ожиданиям «что покупаем»; доплата за «улучшенную» планировку не прописана
- **time:** за 5 дней до визита в банк на подписание ДДУ и открытие эскроу
- **finale:** в приложении к ДДУ — 49,1 м² и иная схема комнат; застройщик предложил «это та же квартира, пересчитали по БТИ»; банк сузил лимит; семья отказалась от ДДУ, бронь вернули частично, на эскроу не вышли
- **comment_magnet_angle:** «Если в брони 54 м², а в ДДУ 49 — вы бы подписали, если застройщик обещает “пересчёт по БТИ”, или сразу снимали бронь?»

## Klyshin hook

- **klyshin_hook:** none | original: none

## Wordstat MCP-KV (live 2026-09-26)

| probe | regions | freq |
|-------|---------|------|
| новостройки тюмень | 55,11176 | 4326 |
| планировка квартира новостройка | 55,11176 | 27 |
| купить новостройку в тюмени | 55,11176 | 892 |
| новостройки тюмень | 225 compare | (context) |

**wordstat_rework:** probe «планировка квартира новостройка» weak alone → anchor P0 «новостройки тюмень» + layout mechanism in H1/body
**final P0:** «новостройки тюмень» regions 55,11176 freq 4326

## signal_urls

- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_51040/
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Complete Scout handoff per SKILL with: wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS, cluster_id, anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir, signal_urls.
