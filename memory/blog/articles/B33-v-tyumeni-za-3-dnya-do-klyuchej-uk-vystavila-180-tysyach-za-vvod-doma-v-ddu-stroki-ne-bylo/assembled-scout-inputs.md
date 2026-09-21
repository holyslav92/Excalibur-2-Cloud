# Scout inputs — 2026-09-21 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-21 (YEKT slot 05:00 UTC automation — weekday Monday)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO B30–B32 plots (assignment ban 3y / insurance +18k / escrow wrong INN) — published 2026-09-20
- NO B27–B29 (land lease / family mortgage child 7 / zero down payment removed)
- NO keys_delay_penalty / acceptance_defects_penalty live clusters (LIVE keys / acceptance)
- NO developer legal entity / escrow requisites swap (B32 + LIVE escrow)
- NO frozen secondary clusters in used-clusters.json
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → synced 2026-09-21
- Live WP recent: escrow INN, insurance, assignment, KP -14 sqm, shou-room, maket sanuzel, discount 4%, etc.
- `scout_helper.py --check-query` PASS for proposed title
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS — fingerprint + formula spam OK (distinct from last-3 bank-stop formula)

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** В Тюмени за 3 дня до ключей УК выставила 180 тысяч за ввод дома — в ДДУ этой строки не было
- **slug:** v-tyumeni-za-3-dnya-do-klyuchej-uk-vystavila-180-tysyach-za-vvod-doma-v-ddu-stroki-ne-bylo
- **article_dir:** memory/blog/articles/B33-v-tyumeni-za-3-dnya-do-klyuchej-uk-vystavila-180-tysyach-za-vvod-doma-v-ddu-stroki-ne-bylo
- **cluster_id (new):** newbuild_uk_handover_fee_not_in_ddu_tyumen
- **top_energy_mirror:** number_in_claim_vs_zero_paid
- **newbuild_mechanism:** Семья с ипотекой на квартиру в сданном ЖК в Тюмени получает приглашение на ключи. За **3 дня** до выдачи ключей управляющая организация (назначена застройщиком) выставляет счёт **~180 000 ₽** за «ввод дома в эксплуатацию / подключение к сетям / формирование УК» — в подписанном ДДУ и приложениях **нет** такой строки и суммы. Банк требует акт приёмки для последнего транша; без оплаты УК не допускает к подписанию актов. Семья останавливает перевод, запрашивает основание у застройщика и УК, ключи переносят
- **why_newbuild_not_secondary:** Цепочка только дольщик–застройщик–УК при сдаче новостройки: ДДУ, акт ввода, приёмка, траншевая/эскроу-ипотека. Нет продавца вторички, ЕГРН-сделки с физлицом, наследников, опеки
- **story_dup_check:** PASS — distinct from B25 finishing mismatch, B26 vvod permission, B32 escrow INN, KP gas/area plots

## Dzen news-casus shape (PASS)

- **event:** семья с двумя детьми, ипотека на квартиру в сданном ЖК (Тюмень), дата ключей назначена
- **risk:** без оплаты счёта УК не пускают на приёмку → банк не отдаёт последний транш; 180 тыс. «сверху» к ДДУ
- **time:** за 3 дня до выдачи ключей, вечером в личном кабинете УК/почтой счёт
- **finale:** в ДДУ и приложениях нет услуги «ввод дома» на 180 тыс.; застройщик ссылается на «типовой договор с УК»; семья **не платит** без письменного основания, перенос ключей на 2 недели, акт не подписан, транш не выдан
- **comment_magnet_angle:** «Если УК присылает счёт на 180 тысяч, которого нет в ДДУ, вы платите, чтобы не сорвать ключи, или стопорите сделку?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-21)

| probe | regions | freq |
|-------|---------|------|
| новостройки тюмень | 55,11176 | 4395 |
| управляющая компания новостройка | 55,11176 | 4 |
| акт приемки передачи квартиры | 55,11176 | 9 |

**wordstat_rework:** weak on УК-specific probes → anchor P0 «новостройки тюмень» + UK-fee mechanism in H1/body
**final P0:** «новостройки тюмень» regions 55,11176 freq 4395

## signal_urls

- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, передача объекта, УК
- https://www.domrf.ru/
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Full Scout handoff per SKILL with anti_dupe_hard: PASS, dzen_casus_shape: PASS, comment_magnet_angle, wordstat P0, cluster_id newbuild_uk_handover_fee_not_in_ddu_tyumen.
