# Scout inputs — 2026-09-25 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-25 (YEKT slot ~15:00 automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — live ~20 + today 2026-09-25)

- NO parking separate DDU / mashinomesto (2026-09-25 live)
- NO investor assignment / застройщик сорвал переуступку (2026-09-25 live)
- NO last floor mortgage / «любой этаж» (2026-09-24 live)
- NO matkapital SFR escrow (2026-09-24 live)
- NO kindergarten on render (2026-09-24 live)
- NO family mortgage child 7 years (2026-09-23 live)
- NO cottage forest / KP gas (B28), land lease (B27), furniture pack, co-borrower freeze, showroom ceiling, window courtyard, delivery shift, insurance requote (B31), escrow wrong entity (B32), assignment resale ban (B30), etc.
- NO acceptance/handover defects cluster (acceptance_defects_penalty locked)
- NO frozen secondary clusters in memory/scout/used-clusters.json

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK
- Live WP recent: parking DDU, assignment investor, last floor, matkapital SFR, detsad render, …
- `scout_helper.py --check-story` PASS for proposed title (partial commissioning vs declaration)
- `excalibur_blog_topic_focus.py` PASS (новостройка)
- `story_dup` PASS — mechanism distinct from B26 permission-to-commission (that was **no permit at all**); here **partial** commissioning of multi-section building before DDU

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** За 4 дня до ДДУ в Тюмени в декларации всплыло частичное введение дома — банк снял ипотеку на новостройку
- **slug:** za-4-dnya-do-ddu-v-tyumeni-v-deklaracii-vsplylo-chastichnoe-vvedenie-doma-bank-snyal-ipoteku
- **article_dir:** memory/blog/articles/B33-za-4-dnya-do-ddu-v-tyumeni-v-deklaracii-vsplylo-chastichnoe-vvedenie-doma-bank-snyal-ipoteku
- **cluster_id (new):** newbuild_partial_commissioning_declaration_before_ddu_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья покупает квартиру в многосекционной новостройке Тюмени по ДДУ с ипотекой. В брони и на визуализации — «дом сдан, ключи скоро». За **4 дня** до подписания ДДУ юрист сверил проектную декларацию на dom.rf: в реестре стоит **частичное введение в эксплуатацию** — в эксплуатацию введён только один корпус/секция, а квартира в другой секции ещё **не введена**. Банк при проверке объекта залога пересчитал риск срока и **снял одобрение ипотеки**; эскроу не открыли; бронь под удержанием (composite casus)
- **why_newbuild_not_secondary:** только цепочка ДДУ/декларация 214-ФЗ/эскроу/ипотека на строящийся или частично введённый объект от застройщика; нет продавца-физлица и вторичной ЕГРН-сделки
- **story_dup_check:** PASS — distinct from B26 (no permit at handover for whole building), B22 delivery shift, B27 land tenure, acceptance defects cluster

## Dzen news-casus shape (PASS)

- **event:** семья с ипотекой выбрала квартиру в ЖК Тюмени; менеджер говорил «дом уже сдаём»
- **risk:** частичный ввод = квартира формально в не введённой секции; банк не принимает в залог / снимает одобрение; деньги на эскроу не уходят вовремя
- **time:** 4 дня до назначенного подписания ДДУ; вечером перед визитом в банк открыли декларацию
- **finale:** в декларации — частичный ввод; застройщик предложил «подпишите ДДУ, остальное доведём»; семья отказалась; бронь частично удержали; ипотеку пересобирали на другой лот
- **comment_magnet_angle:** «Если в декларации частичный ввод, а вам обещали «уже сдано» — вы подписываете ДДУ ради брони или ждёте полный ввод?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-25)

**Preflight:** wordstat_get_user_info OK

| probe | regions | freq |
|-------|---------|------|
| купить новостройку в тюмени | 55,11176 | 892 |
| новостройки тюмень | 55 | 3504 (context) |
| ввод в эксплуатацию новостройки | 55,11176 | API low / sparse (mechanism in H1) |
| разрешение на ввод новостройки | 55,11176 | treat as weak — rework to spine |

**wordstat_rework:** weak «ввод в эксплуатацию» alone → anchor P0 «купить новостройку в тюмени» + partial commissioning mechanism in title/body

**final P0:** «купить новостройку в тюмени» — **892** (55+11176); compare context «новостройки тюмень» 3504 (55)

## signal_urls (research)

- https://www.domrf.ru/ — проектные декларации, статус ввода
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir, signal_urls, research angles for Research role.
