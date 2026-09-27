# Assembled scout inputs — B33 slot 15 YEKT 2026-09-27 (weekend owner request)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-27  
**slot:** 15:00 Asia/Yekaterinburg (Sunday weekend)  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (today 2026-09-27 — DO NOT reuse)

1. Slot 09 — рассрочка разошлась с ценой на 340 тыс до ДДУ | mechanism: installment vs contract price
2. Slot 12 — УК потребовала 180 тыс за 5 дней до ключей | mechanism: management company fee before acceptance

Also avoid: trade-in reject, booking expired price hike, mortgage rate hike before DDU, EGRN encumbrance secondary plot.

## Proposed lock (pre-checked)

- **cluster_id:** `newbuild_townhouse_separate_entry_booking_vs_ddu_block_apartment_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** семья с двумя детьми смотрит формат «таунхаус / отдельный вход» в тюменской новостройке (квартирный блок low-rise); в брони и на плане менеджер фиксирует «таунхаус, свой вход, без соседей с лестницы»; за 2–3 дня до открытия эскроу в проекте ДДУ — объект как **квартира** в многоквартирном блоке, общий подъезд, этаж/площадь не те, что в брони; банк видит расхождение с одобрением; семья **останавливает** подписание до правки или смены лота (agency, не паника)
- **why_newbuild_not_secondary:** только ДДУ/бронь/эскроу от застройщика, выбор форма жилья в новостройке — не сделка с продавцом вторички
- **title draft (H1 direction):** «В Тюмени в брони обещали таунхаус с отдельным входом — в ДДУ оказалась квартира в блоке»
- **comment_magnet_angle:** «Если в брони “таунхаус”, а в ДДУ “квартира в блоке” — вы бы подписали ради сохранения цены или разорвали бронь?»
- **scout_helper.py --check-query:** PASS 2026-09-27 (anti_dupe_hard PASS, topic focus PASS)
- **formula_spam_check:** PASS — last3 today/weekend mix (рассрочка/УК/лифт…) ≠ booking-vs-DDU housing type mismatch

## Wordstat MCP-KV (live 2026-09-27)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| новостройки тюмень | 55,11176 | 4350 |
| квартиры в тюмени новостройки | 55,11176 | 1047 |
| купить новостройку в тюмени | 55,11176 | 891 |
| новостройки в тюмени от застройщика | 55,11176 | 641 |
| тюмень новостройки дома | 55,11176 | 104 |
| таунхаус новостройка тюмень | 55,11176 | 4 (weak — rework) |

**wordstat_rework:** слабый «таунхаус» → spine P0 **«новостройки тюмень» 4350** + механика сверки брони/типа объекта в ДДУ (семьи + инвесторы, формат жилья)

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: семья выбрала формат таунхауса в новостройке
- risk: тип объекта в ДДУ ≠ обещание в брони
- time: за 2–3 дня до эскроу/ДДУ
- finale: остановили до денег; что сверить в брони и приложениях к ДДУ

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- site blog recent titles (anti-dup)

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
