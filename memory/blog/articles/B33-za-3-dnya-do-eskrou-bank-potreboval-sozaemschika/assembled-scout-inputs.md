# Scout inputs — 2026-09-28 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-28 (YEKT Monday slot ~12:00 UTC+5)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — live WP 2026-09-26..28)

- NO second bathroom / appendix mismatch (2026-09-28 live)
- NO EISJHS construction stop before escrow (2026-09-28 live)
- NO studio vs commercial in DDU (2026-09-27 live)
- NO taunhaus vs apartment block (2026-09-27 live)
- NO installment price mismatch 340k (2026-09-27 live)
- NO UK 180k before keys (2026-09-27 live)
- NO lift tech oversight keys delay (2026-09-26 live)
- NO rental ban 3y in DDU investor (2026-09-26 live)
- NO parking benefit cancelled (2026-09-26 live)
- NO booking removed 1h before DDU KP house (2026-09-26 live)
- NO cold balcony vs glazed loggia (2026-09-26 live)
- NO discount 380k struck from booking (2026-09-26 live)
- NO frozen clusters in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK 2026-09-28
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек)
- `story_dup.py --text` PASS

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** За 3 дня до эскроу банк потребовал созаёмщика — в брони семейной ипотеки на новостройку Тюмени обещали одного
- **slug:** za-3-dnya-do-eskrou-bank-potreboval-sozaemshchika-semejnaya-ipoteka-novostrojka-tyumen
- **article_dir:** memory/blog/articles/B33-za-3-dnya-do-eskrou-bank-potreboval-sozaemshchika-semejnaya-ipoteka-novostrojka-tyumen
- **cluster_id (new):** newbuild_family_mortgage_coborrower_before_escrow_tyumen
- **top_energy_mirror:** clock_ran_out / paper_clean_then_broke
- **newbuild_mechanism:** Семья с двумя детьми берёт квартиру в новостройке Тюмени по семейной ипотеке. Менеджер ОП и брокер в брони зафиксировали: «одобрение на одного заёмщика, созаёмщик не нужен». За 3 дня до открытия эскроу банк прислал условия: без созаёмщика (супруги) кредит не выдадут — одобрение «заморозили». Семья остановила сделку до подписания ДДU и не открывала счёт
- **why_newbuild_not_secondary:** Цепочка только новостройка: бронь в ЖК, семейная ипотека на строящееся жильё, эскроu, ДДU с застройщиком. Нет продавца вторички, ЕГРН, наследников, опеки
- **story_dup_check:** PASS — distinct from B29 zero-down promo, B31 insurance payment hike, B32 wrong escrow entity, live family-mortgage-revoked-at-child-7, installment/rassrochka plots

## Dzen news-casus shape (PASS)

- **event:** семья выбрала двушку в новостройке; получили предварительное одобрение семейной ипотеки на одного родителя
- **risk:** без созаёмщика банк снимает одобрение; без ипотеки нельзя открыть эскроu по 214-ФЗ; бронь сгорает
- **time:** за 3 дня до назначенного открытия эскроu-счёта
- **finale:** банк потребовал подключить супругу созаёмщиком с доходом; менеджер ОП сказал «подпишите ДДU, потом разберёмся»; семья отказалась, эскроu не открыли, сделку перенесли на другой корпус с пересчётом брони (composite casus)
- **comment_magnet_angle:** «Если банк за три дня до эскроu требует созаёмщика, а в бронi обещали одного — вы подписываете ДДU или стопаете сделку?»

## Klyshin hook

- **klyshin_hook:** none | original: none

## Wordstat MCP-KV (live 2026-09-28)

**Preflight:** wordstat_get_user_info OK (MCP-KV)

| probe | regions | freq |
|-------|---------|------|
| семейная ипотека тюмень | 55,11176 | 1309 |
| семейная ипотека тюмень 2026 | 55,11176 | 422 |
| купить новостройку в тюмени | 55,11176 | 891 |
| новостройки тюмень | 55,11176 | 4350 (context) |
| созаёмщик семейная ипотека | 55,11176 | API weak/<10 |

**wordstat_rework log:**
- probe «созаёмщик семейная ипотека» 55,11176 → weak
- **rework:** anchor P0 «семейная ипотека тюмень» + coborrower mechanism in H1/body
- **final P0 «семейная ипотека тюмень» regions 55,11176,compare225 freq 1309 (55+11176)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- Official banks: family mortgage program pages (Sber, VTB, Dom.RF program docs) for coborrower rules 2026

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields listed in B30 handoff example.
