# Scout inputs — 2026-09-21 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-21 (YEKT slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — live ~20 + ledger)

- NO terrasa on visualization vs DDU (2026-09-21 live)
- NO UK 180k before keys / tech connection fee (2026-09-21 live)
- NO KP house -14 sqm on acceptance (2026-09-20 live)
- NO wrong escrow legal entity (B32 / 2026-09-20 live)
- NO insurance payment hike before DDU (B31)
- NO assignment resale ban 3 years (B30)
- NO show-room south vs north section (2026-09-19 live)
- NO second bathroom missing (2026-09-19 live)
- NO zero-down promo removed (B29)
- NO 4% discount missing in DDU (2026-09-19 live)
- NO ceilings 25cm lower KP (2026-09-19 live)
- NO KP gas 2026 vs 2028 declaration (B28)
- NO land lease in declaration (B27)
- NO frozen secondary clusters in used-clusters.json

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (дду)
- `story_dup.py --text` PASS — fingerprint escrow_blocked on generic text only; cluster distinct from B32 wrong entity

## Proposed topic (PASS)

- **topic_id:** B33
- **title_draft:** За 5 дней до ДДУ банк поднял первый взнос с 15% до 25% — лимит по новостройке в Тюмени урезали
- **slug:** za-5-dnej-do-ddu-bank-podnyal-pervyj-vznos-s-15-do-25-limit-po-novostrojke-urezali
- **article_dir:** memory/blog/articles/B33-za-5-dnej-do-ddu-bank-podnyal-pervyj-vznos-s-15-do-25-limit-po-novostrojke-urezali
- **cluster_id:** newbuild_downpayment_ltv_hike_before_ddu_tyumen
- **top_energy_mirror:** clock_ran_out_before_money
- **newbuild_mechanism:** Семья с одобренной ипотекой на квартиру в новостройке Тюмени (ДДУ, эскроу). За 5 дней до подписания банк после внутренней переоценки объекта снизил максимальный LTV: первый взнос с 15% до 25% (~+1,1 млн ₽ наличными). В брони и письме об одобрении было 15%. Семья не успела собрать разницу до даты ДДУ — сделку остановили до эскроу, бронь частично сгорела (composite)
- **why_newbuild_not_secondary:** Только цепочка покупки квартиры в строящемся ЖК: бронь, одобрение на новостройку, проект ДДУ, эскроу. Нет продавца вторички, ЕГРН, наследников, опеки
- **story_dup_check:** PASS — distinct from B29 (zero-down promo removed), B22 (rate hike), B32 (escrow requisites entity), B31 (insurance OSZ)

## Dzen news-casus shape (PASS)

- **event:** пара с ребёнком выбрала двушку в новостройке Тюмени, одобрение ипотеки с 15% взносом
- **risk:** без дополнительного миллиона сделка срывается; бронь и скидка застройщика под угрозой; повторное одобрение — новая ставка/срок
- **time:** за 5 дней до назначенного подписания ДДУ; звонок ипотечного менеджера вечером в четверг
- **finale:** банк зафиксировал 25% взнос; семья за 48 часов не нашла сумму; ДДУ не подписали, эскроу не открывали; застройщик удержал часть брони; одобрение аннулировали через 12 дней (composite)
- **comment_magnet_angle:** «Если за несколько дней до ДДУ банк поднимает взнос с 15% до 25% — вы ищете деньги любой ценой или отпускаете лот?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-21)

| probe | regions | freq |
|-------|---------|------|
| купить новостройку в тюмени | 55,11176 | 898 |
| купить новостройку в тюмени | 225 compare | (context) |
| первоначальный взнос новостройка тюмень | 55,11176 | 94 (spine rework) |
| новостройки в тюмени без первоначального взноса | 55,11176 | 59 |

**wordstat_rework:** probe «первоначальный взнос новостройка тюмень» 94 → anchor P0 «купить новостройку в тюмени» 898 + LTV/downpayment mechanism in H1
**final P0:** «купить новостройку в тюмени» regions 55,11176 freq **898** / compare RU 225

## Handoff flags

```text
wordstat_preflight: mcp-kv OK
top_energy_mirror: clock_ran_out_before_money
newbuild_mechanism: LTV cut 15→25% five days before DDU signing
why_newbuild_not_secondary: newbuild DDU/escrow only
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + sync OK
dzen_casus_shape: PASS
comment_magnet_angle: (see above)
wordstat: mcp_kv live | P0 «купить новостройку в тюмени» 898
story_dup_check: PASS
h1_fingerprint_check: PASS | downpayment_ltv_hike_five_days_before_ddu
formula_spam_check: PASS
anti_dupe_hard: PASS
```
