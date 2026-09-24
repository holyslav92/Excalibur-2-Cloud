# Scout inputs — 2026-09-24 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-24 (YEKT slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO repeat live 2026-09-22–23 plots: семейная ипотека ребёнку 7 лет в день ДДУ; КП «лес» vs забор соседа; мебельный пакет партнёра за 4 дня до ДДУ; созаёмщик отказался до эскроу; потолки 2,68 в экспликации; окна во двор vs магистраль; сдвиг сдачи в декларации; кладовая отдельным ДДУ; взнос 15→25%; терраса на визуализации; УК 180 тыс. до ключей
- NO frozen clusters in memory/scout/used-clusters.json (30d): escrow zero mismatch, installment penalty developer, booking expired price hike, trade-in, keys delay penalty, mortgage rate hike, developer entity change, cellar separate DDU, assignment 28d lost buyer, etc.
- NO secondary market plots (бабушка, банкрот, ЕГРН вторичка, опека…)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → active locks synced 2026-09-24
- Live WP recent (~15): family mortgage child 7; KP forest fence; furniture partner 4d; co-borrower escrow 3d; ceiling 2,68; windows courtyard; delivery shift; cellar DDU; down payment hike; terrace render; UK 180k keys; etc.
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug (clean, unique)
- `scout_helper.py --check-story` ANTI-DUPE HARD PASS (cluster newbuild_render_amenity_missing_declaration_tyumen)
- `excalibur_blog_topic_focus.py` PASS (on-focus: новострой)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B33
- **title_draft:** В Тюмени на рендере новостройки обещали детский сад во дворе — в декларации объекта его нет, семья сняла бронь
- **slug:** v-tyumeni-na-renedere-novostrojki-obeschali-detskij-sad-v-deklaracii-ego-net-semya-snyala-bron
- **article_dir:** memory/blog/articles/B33-v-tyumeni-na-renedere-novostrojki-obeschali-detskij-sad-v-deklaracii-ego-net-semya-snyala-bron
- **cluster_id (new):** newbuild_render_amenity_missing_declaration_tyumen
- **top_energy_mirror:** paper_clean_then_broke (красивая картинка → официальный документ без обещания)
- **newbuild_mechanism:** Семья с двумя детьми (3 и 6 лет) выбирает квартиру в новостройке Тюмени. На сайте и в шоу-руме на рендере двора — отдельное здание «детский сад» с подписью. Менеджер в брони пишет «инфраструктура: детсад во дворе». За 5 дней до подписания ДДУ открывают проектную декларацию на dom.rf: в перечне объектов соц. инфраструктуры, которые застройщик обязан построить/передать, **детского сада нет** — только детская площадка. Семья снимает бронь до эскроу, часть аванса удерживают
- **why_newbuild_not_secondary:** Только цепочка покупки у застройщика: бронь, проектная декларация 214-ФЗ, ДДУ, обещания инфраструктуры ЖК. Нет продавца вторички, наследников, ЕГРН-квартиры, опеки, соседской доли
- **story_dup_check:** PASS — не пересекается с КП «лесополоса/забор» (земля/границы), не с «окна во двор», не с «сдвиг сдачи», не с «терраса на картинке» (пристрой к квартире), не с booking price-hike cluster

## Dzen news-casus shape (target PASS)

- **event:** семья с двумя детьми смотрит новостройку в Тюмени; на рендере и в презентации — полноценный детский сад во дворе; бронь 150 тысяч
- **risk:** без сада во дворе — очередь в соседние ДОУ, логистика с двумя малышами; при продаже/ипотеке обещание «сад рядом» на сайте ≠ юридическая обязанность застройщика
- **time:** за 5 дней до визита в банк за одобрением итогового ДДУ; вечером сверили декларацию
- **finale:** в декларации — только детская площадка, сада нет; застройщик: «сад построит город позже, на рендере — концепция»; семья отказалась от ДДУ, вернули 90 тысяч из 150 брони, эскроу не открывали
- **comment_magnet_angle:** «Если на рендере ЖК есть детский сад, а в проектной декларации его нет — вы бы всё равно шли в ДДУ ради квартиры или снимали бронь?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild declaration casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-24)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4294 |
| новостройки | 225 (compare) | (context) |
| детский сад новостройка тюмень | 55,11176 | API empty/<5 (weak) |
| купить новостройку в тюмени | 55,11176 | 897 |
| новостройки в тюмени от застройщика | 55,11176 | 628 |

**wordstat_rework log:**
- probe «детский сад новостройка тюмень» 55,11176 → empty/<5 (too weak for P0 alone)
- rework: anchor buyer spine «новостройки тюмень» + amenity-on-render vs declaration mechanism in H1/body
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4294 (55+11176)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — проектные декларации, перечень объектов соц. инфраструктуры
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, проектная декларация, изменения
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir, signal_urls, research angles for Research role.
