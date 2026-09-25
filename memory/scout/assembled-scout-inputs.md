# Scout inputs — 2026-09-25 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-25 (YEKT slot ~09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true
**topic_id:** B33

## Slot constraints (HARD FORBIDDEN)

- NO frozen secondary clusters (memory/scout/used-clusters.json 30d)
- NO repeat last-3 formula skeleton without new mechanism: B30 assignment resale ban 3y, B31 insurance +18k before DDU, B32 wrong escrow legal entity
- NO «за N дней до ДДУ» clone without distinct mechanism (recent WP flood)
- NO escrow_not_opened / co-borrower refused (cluster locked LIVE-SOZAEMSCHIK)
- NO B30 plot (3-year resale ban in assignment) — this is developer pulling lot to direct sale
- NO bank appraisal -900k vs DDU (locked)
- NO booking_expired_price_hike / apartment vs apartments mismatch clusters

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 25 active locks (last_sync 2026-09-25)
- Live WP recent: last floor mortgage 4d, matkapital SFR 7d, detsad render, child 7 family mortgage, KP forest fence, furniture package, co-borrower escrow, ceiling 2.68m, courtyard vs magistral, delivery shift, cellar separate DDU
- Published ledger last: B32 escrow wrong entity, B31 insurance, B30 assignment ban
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug below
- `excalibur_blog_topic_focus.py` PASS (on-focus: переуступка, новостройка, застройщик)

## Proposed topic (PASS topic_focus + scout_helper)

- **title_draft:** В Тюмени инвестор согласовал переуступку — застройщик снял лот и продал по прямому ДДУ на 400 тысяч дороже
- **slug:** v-tyumeni-zastrojschik-snyal-pereustupku-i-prodal-pryamym-ddu-dorozhe
- **article_dir:** memory/blog/articles/B33-v-tyumeni-zastrojschik-snyal-pereustupku-i-prodal-pryamym-ddu-dorozhe
- **cluster_id (new):** newbuild_developer_pulled_assignment_sold_direct_tyumen
- **top_energy_mirror:** someone_else_took_object
- **newbuild_mechanism:** Инвестор (или семья) согласовывает переуступку прав по ДДУ в новостройке Тюмени: бронь/депозит уступающего, согласование с застройщиком, ипотека в работе. Застройщик снимает квартиру с «переуступок» и продаёт тот же лот по прямому ДДУ другому покупателю дороже (~400 тыс.). Первый покупатель теряет объект и часть внесённых сумм / время одобрения
- **why_newbuild_not_secondary:** Цепочка только первички: переуступка прав по ДДУ, офис продаж застройщика, прямая продажа лота, эскроу/бронь в ЖК. Нет продавца-физлица на вторичке, ЕГРН-сделки, наследников, опеки

## Dzen news-casus shape (PASS)

- **event:** инвестор в Тюмени выбрал переуступку в строящемся ЖК — менеджер застройщика письменно подтвердил «лот в переуступке, можно выходить на ДДУ»
- **risk:** пока банк дорабатывает ипотеку под переуступку, застройщик может вывести квартиру в прямую продажу; уступающий и покупатель теряют объект, бронь/аванс частично не возвращают
- **time:** через 11 дней после согласования переуступки, за 2 дня до планового подписания ДДУ с уступающим
- **finale:** лот исчез из реестра переуступок, в прямой продаже та же квартира +400 тыс.; инвестор не успел подписать; удержали 150 тыс. «за согласование», остальное вернули через 3 недели
- **comment_magnet_angle:** «Если застройщик снял переуступку и продал квартиру дороже, вы бы судились за удержанные 150 тысяч или сразу искали другой лот?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-25)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|------|
| переуступка тюмень | 55,11176 | 8 |
| переуступка новостройка тюмень | 55,11176 | API empty (<5) |
| новостройка переуступка купить | 55,11176 | API empty (<5) |
| переуступка новостройка | 225 compare | 2561 |
| купить новostройку в тюмени | 55,11176 | 897 |
| купить новостройку в тюмени | 225 compare | 1921 |
| новостройки тюмень | 55,11176 | 4294 (context spine) |

**wordstat_rework:** probe «переуступка тюмень» 8 → weak; anchor buyer P0 «купить новostройку в тюменi» (newbuild + инвестор/семья) + переуступка mechanism in H1
**final P0:** «купить новостройку в тюмени» regions 55,11176 freq **897** | compare 225 freq **1921**

## signal_urls (tenant scout)

- {{SITE_BASE}}/blog/
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- dom.rf / 214-ФЗ project declarations (research)
- regional Tyumen newbuild news (research only)

## Required handoff fields (include verbatim blocks)

Write full handoff with: topic_id B33, slug, title_draft, article_dir, cluster_id, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat line, story_dup_check PASS, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS, signal_urls list.
