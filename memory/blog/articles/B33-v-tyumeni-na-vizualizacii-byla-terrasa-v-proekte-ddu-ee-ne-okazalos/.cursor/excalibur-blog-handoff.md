# Scout handoff — B33

run_date: 2026-09-21  
slot: 12:00 Asia/Yekaterinburg  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_terrace_visualization_missing_ddu_tyumen`

**Title draft / H1 direction:**

> В Тюмени на визуализации была терраса — в проекте ДДУ её не оказалось, сделку остановили

**slug:** v-tyumeni-na-vizualizacii-byla-terrasa-v-proekte-ddu-ee-ne-okazalos-sdelku-ostanovili

**article_dir:** memory/blog/articles/B33-v-tyumeni-na-vizualizacii-byla-terrasa-v-proekte-ddu-ee-ne-okazalos-sdelku-ostanovili

**P0:** «тюмень купить квартиру в новостройке от застройщика» — **258** (Tyumen 55 spine)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: семья покупает квартиру в новостройке Тюмени по ДДУ; на визуализации и в брони зафиксирована терраса (~8–12 м²); за 4 дня до подписания ДДУ в проекте договора и экспликации террасы нет, площадь меньше при той же цене; менеджер предлагает «оформим террасу потом»; семья останавливает сделку до эскроу; бронь ~50–80 тыс ₽ частично удержана (composite casus)
why_newbuild_not_secondary: только бронь, визуализация ЖК, проект ДДУ и эскроу у застройщика — не вторичка/ЕГРН
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; skip UK 180k live, B32 escrow entity, B31 insurance, B30 assignment ban
dzen_casus_shape: PASS | event: выбор «евродвушки с террасой» | risk: в ДДУ нет террасы, ипотека под другую площадь | time: 4 дня до подписания | finale: стоп до эскроу, частичный возврат брони
comment_magnet_angle: «Если терраса есть на картинке, но нет в проекте ДДУ — подписываете с обещанием “дотащим” или стоп до эскроу?»
wordstat_rework: spine «купить квартиру новостройка тюмень» 629 (55) → P0 line «тюмень купить квартиру в новостройке от застройщика» 258 + terrace vs экспликация mechanism
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 258 (55)
story_dup_check: PASS | cluster_id: newbuild_terrace_visualization_missing_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: terrace_visualization_missing_ddu_project
formula_spam_check: PASS | last3_mechanisms: B30 assignment ban; B31 insurance; B32 escrow entity — new skeleton (visualization vs DDU), not «за N дней» only
anti_dupe_hard: PASS
```

## signal_urls

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
