# Scout inputs — 2026-09-22 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-22 (YEKT slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO today live WP duplicates: окна во двор vs магистраль; сдвиг сдачи на 2 квартала; кладовая вынесена в отдельный ДДU (2026-09-22)
- NO last-3 formula-only clones without new mechanism (escrow_blocked / days-before-DDU bank cuts) — this plot is **showroom ceiling vs DDU экспликация**, distinct
- NO B30 assignment 3y ban; NO B31 insurance; NO B32 wrong escrow entity; NO terrace-on-visualization (2026-09-21 live); NO BTI -4.2 sqm; NO bank appraisal -900k; NO frozen secondary clusters in used-clusters.json

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK (2026-09-22)
- Live WP recent: declaration shift, storeroom separate DDU, window orientation, down payment hike, terrace visualization, UK 180k, KP -14 sqm, escrow wrong entity, insurance, assignment ban
- `scout_helper.py --check-query` → **ANTI-DUPE HARD PASS** | cluster `newbuild_ceiling_height_showroom_vs_ddu_tyumen`
- `excalibur_blog_topic_focus.py` → PASS (новостройка, ДДU, эскроu, сделка)

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** В шоу-руме новостройки Тюмени обещали потолки три метра — в экспликации ДДU оказалось 2,68, семья остановила сделку до эскроu
- **slug:** v-shou-rume-novostrojki-tyumen-potolki-3-metra-v-ddu-268-semja-ostanovila
- **article_dir:** memory/blog/articles/B33-v-shou-rume-novostrojki-tyumen-potolki-3-metra-v-ddu-268-semja-ostanovila
- **cluster_id:** newbuild_ceiling_height_showroom_vs_ddu_tyumen
- **top_energy_mirror:** paper_clean_then_broke (в шоу-руме «как в рекламе», в проекте ДДU — другая цифра до денег)
- **newbuild_mechanism:** Семья с ребёнком выбирает квартиру в ЖК новостройки Тюмени. Менеджер в шоу-руме называет «потолки три метра», на планировке в брони то же. За несколько дней до эскроu открывают проект ДДU + экспликацию: высота потолков **2,68 м** (или «не менее 2,7» с фактом ниже обещанного). Пересчёт ощущения площади/мебели/детской; банк не блокирует, но семья отказывается подписывать ДДU и не открывает эскроu (composite casus)
- **why_newbuild_not_secondary:** только цепочка покупки от застройщика: шоу-рум, бронь, проект ДДU, экспликация БТИ/проект; нет продавца вторички, наследников, ЕГРН-сюрпризов
- **story_dup_check:** PASS — не терраса (B live), не лоджия/балкон, не площадь BTI -4.2, не секция/вид

## Dzen news-casus shape (PASS)

- **event:** семья в шоу-руме новостройки Тюмени, менеджер показывает «высокие потолки 3 м»
- **risk:** фактическая высота в ДДU ниже → другая планировка мебели/шкафов/детская; ощущение «купили не то»; спор с застройщиком после подписания дороже
- **time:** за 4–5 дней до подписания ДДU / открытия эскроu; вечерняя сверка проекта договора
- **finale:** в эксплikaции 2,68 м; застройщик: «это стандарт по СП, 3 м — маркeting»; семья не подписала ДДU, бронь вернули частично или перенесли на другой лот (composite)
- **comment_magnet_angle:** «Если в шоу-руме говорят «потолки 3 метра», а в ДДU — 2,68, вы бы подписали, чтобы не потерять бронь, или ушли бы сразу?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-22)

| probe | regions | freq |
|-------|---------|------|
| новостройки тюмень | 55,11176 | 4345 |
| купить новостройку в тюмени | 55,11176 | 902 |
| высота потолков новостройка | 55,11176 | ~4 (weak) |
| приемка квартиры в новостройке тюмень | 55,11176 | 28 |

**wordstat_rework:** probe «высота потолков новостройка» weak → anchor P0 «новостройки тюмень» 4345 + mechanism ceiling in H1/body  
**final P0:** «новостройки тюмень» regions 55,11176 compare 225 (4345 local / RU context via «новостройки» national)

## signal_urls

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, проектная декларация, приложения к ДДU
- https://www.domrf.ru/
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used

## Output required

Write complete Scout handoff markdown per SKILL.md with all PASS fields and lock B33 title/slug/article_dir.
