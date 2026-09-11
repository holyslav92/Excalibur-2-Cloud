# Scout inputs — 2026-09-11 (B35)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-11 (YEKT weekday slot)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 24 active locks
- **Live WP last ~20 (2026-09-11) — DO NOT reuse plot:**
  - дом посёлок границы участка / 1,5 сотки (2026-09-10)
  - трейд-ин занизили оценку (2026-09-10)
  - чистовая → предчистовая в ДДУ (2026-09-10)
  - бронь сгорела +450к (2026-09-10)
  - пропал балкон / банк заморозил транш (2026-09-09)
  - неустойка год не платили / приёмку остановили (2026-09-09)
  - ребёнку 7 лет — семейную ипотеку пересчитали (2026-09-09)
  - банк после приёмки без замечаний — 10 дефектов (2026-09-09)
  - ключи без разрешения на ввод (2026-09-08)
  - переуступка долг 94к (2026-09-08)
  - маткапитал за 3 недели до ключей (2026-09-08)
  - созаёмщика убрали за 7 дней до ДДУ (2026-09-07)
  - **рассрочка просрочка — ДДУ расторгли, удержали 180к (2026-09-07) — CLOSED, не retitle**
  - газ у забора 180м / этаж 12→2 / эскроу -400к / 12→8 соток / двойная продажа / доплата отделка 300к (2026-09-05–07)
- **Rejected:** installment penalty — live 2026-09-07 «ДДУ расторгли из-за пяти дней просрочки»
- **Rejected:** bank appraisal below DDU — formula_spam / fingerprint vs live escrow shortfall cluster
- **Rejected:** area shortage on acceptance — overlaps acceptance cluster density this week (B31 clean act)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир, дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B35
- **title_draft:** В Тюмени в ДДУ запретили аренду до ключей — инвестор потерял двух арендаторов
- **slug:** v-tyumeni-v-ddu-zapretili-arendu-do-klyuchei-investor-poteryal-arendatorov
- **cluster_id (new):** newbuild_rental_banned_until_keys_ddu_tyumen
- **story_dup_check:** PASS — distinct plot: инвестор покупает новостройку под сдачу, в приложении к ДДУ пункт «не сдавать до регистрации права/получения ключей»; два арендатора уже согласовали заезд и аванс — застройщик предупреждает о расторжении при нарушении; инвестор останавливает подписание / ищет выход через расторжение брони

## Dzen news-casus shape (target PASS)

- **event:** инвестор в Тюмени выбрал студию в новостройке под сдачу, внёс бронь, согласовал двух арендаторов на дату после сдачи дома
- **risk:** в приложении к ДДУ запрет передачи в аренду до регистрации права — нарушение = штраф + расторжение; арендаторы уходят к конкурентам, окупаемость срывается
- **time:** за 5–7 дней до подписания ДДУ, когда юрист прочитал приложение целиком
- **finale:** инвестор отказался подписывать ДДУ в текущей редакции; застройщик не согласился вычеркнуть пункт — бронь сгорела, один арендатор уже внёс задаток на другую квартиру
- **comment_magnet_angle:** «В ДДУ мелким шрифтом „аренда запрещена до ключей“ — вы бы всё равно подписали под сдачу или считаете, что „все так делают неофициально“?»

## Klyshin hook

- **klyshin_hook:** none | fresh Tyumen newbuild investor casus without Klyshin

## Wordstat MCP-KV (live 2026-09-11)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| аренда новостройка тюмень | 55,11176 | ~5 (weak/noisy API tail) |
| купить новостройку для сдачи | 55,11176 | 0 (empty) |
| **новостройки тюмень** | **55,11176** | **4670** |
| **новостройки тюмень** | **225 (compare RU)** | **8607** |
| купить новостройку в тюмени | 55,11176 | 899 (investor/buyer context) |
| рассрочка от застройщика тюмень | 55,11176 | 135 (rejected — live installment 2026-09-07) |

**wordstat_rework log:**
- probe «аренда новостройка тюмень» 55,11176 → ~5 (weak niche; not drop casus)
- probe «купить новостройку для сдачи» 55,11176 → empty
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, инвестор, ключи) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4670 (55) / 8607 (RU225)**

## Handoff fields (must include verbatim structure)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: «запрет сдачи в аренду до ключей/регистрации права в приложении к ДДУ новостройки»
why_newbuild_not_secondary: «ограничение только в договоре долевого участия с застройщиком; на вторичке такого пункта в ДДУ не бывает — это чисто newbuild-механика для инвестора»
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: booking_expired_price_hike, trade_in_rejected_developer, installment_penalty_developer (live 2026-09-07), matkapital_newbuild_3w_keys, assignment_debt_94k, keys_without_permit, acceptance_bank_stop, …
dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «…» | finale: «…»
comment_magnet_angle: «…?»
wordstat_rework: probe «аренда новостройка тюмень» ~5 → «купить новостройку для сдачи» 0 → final P0 «новостройки тюмень» 4670
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4670
story_dup_check: PASS | cluster_id: newbuild_rental_banned_until_keys_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: keys_delay_penalty
formula_spam_check: PASS | last3_mechanisms: trade_in, finish_package, booking_expired (distinct from candidate)
anti_dupe_hard: PASS
```

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_122907/ — 214-ФЗ / ДДУ контекст
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with topic_id B35, title, slug, signal_urls, research angles for Research role. Russian language.
