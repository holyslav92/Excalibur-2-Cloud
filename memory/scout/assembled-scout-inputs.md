# Scout inputs — 2026-09-21 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-21  
**slot:** 12:00 Asia/Yekaterinburg (cron automation)  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)  
**topic_market_focus:** newbuild_only  
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO UK 180k before keys (live WP 2026-09-21)
- NO parking mandatory separate contract (overlap booking cluster)
- NO «за N дней до ДДU» skeleton spam — last3 B30/B31/B32 used that formula; pick different time beat
- NO escrow wrong legal entity (B32), insurance requote (B31), assignment resale ban (B30)
- NO frozen clusters in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` OK
- Live WP recent: UK 180k, KP -14 sqm, escrow wrong entity, insurance, assignment ban, show-room section mismatch, sanuzel, zero-down, discount 4%, KP ceilings, gas dates, family mortgage 7 years
- `scout_helper.py --check-query` PASS for terrace title (fingerprint ddu_vs_escrow_amount — distinct plot: terrace on visualization missing in DDU project)
- `excalibur_blog_topic_focus.py` PASS (дду, новостройка)

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** В Тюмени на визуализации была терраса — в проекте ДДУ её не оказалось, сделку остановили
- **slug:** v-tyumeni-na-vizualizacii-byla-terrasa-v-proekte-ddu-ee-ne-okazalos-sdelku-ostanovili
- **article_dir:** memory/blog/articles/B33-v-tyumeni-na-vizualizacii-byla-terrasa-v-proekte-ddu-ee-ne-okazalos-sdelku-ostanovili
- **cluster_id (new):** newbuild_terrace_visualization_missing_ddu_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья выбирает квартиру в новостройке Тюмени по ДДУ; на сайте/визуализации и в брони зафиксирована **терраса** (~8–12 м²) как часть лота; за **4 дня** до подписания ДДУ открывают проект договора и экспликацию — террасы нет, площадь меньше, цена та же; менеджер говорит «терраса общая / оформим потом»; семья **останавливает сделку до эскроу**, бронь ~50–80 тыс ₽ под удержанием (composite casus)
- **why_newbuild_not_secondary:** только цепочка покупки у застройщика: бронь, визуализация ЖК, проект ДДУ, эскроу; нет продавца вторички и ЕГРН-сюжетов
- **story_dup_check:** PASS — distinct from show-room section mismatch (B live sanuzel/maket), BTI sqm KP, chistovaya acceptance

## Dzen news-casus shape (target PASS)

- **event:** семья с ребёнком выбрала «евродвушку с террасой» в новостройке Тюмени; визуализация и бронь с планом с террасой
- **risk:** без террасы лот другой (свет/площадь/цена); ипотека одобрена под заявленную площадь; подписание ДДУ закрепляет меньшую площадь
- **time:** за 4 дня до визита в банк на подписание ДДУ; вечером сверили PDF проекта
- **finale:** в экспликации террасы нет; застройщик предложил подписать «как есть» и оформить террасу актом позже; семья отказалась, эскроу не открывали, договорились о возврате части брони
- **comment_magnet_angle:** «Если терраса есть на картинке, но нет в проекте ДДУ — вы подписываете с обещанием “дотащим” или стопаете до эскроу?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-21)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|-----:|
| купить квартиру новостройка тюмень | 55 | 629 (phrase total) |
| тюмень купить квартиру в новостройке от застройщика | 55 (top line) | 258 |
| приемка квартиры в новостройке тюмень | 55,11176 | 29 |
| семейная ипотека новостройка тюмень | 55,11176 | 23 |
| эскроу счет новостройка | 225 compare | 388 |

**wordstat_rework:** probe «терраса новостройка тюмень» not run (API flake) → anchor P0 «тюмень купить квартиру в новостройке от застройщика» 258 (55) + mechanism terrace/visual vs DDU экспликация in H1

**final P0:** «тюмень купить квартиру в новостройке от застройщика» — regions 55,11176, compare 225 — freq **258** (Tyumen 55 spine line)

## signal_urls

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, проект ДДУ, описание объекта
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check (note break from last3 «за N дней»), anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir.
