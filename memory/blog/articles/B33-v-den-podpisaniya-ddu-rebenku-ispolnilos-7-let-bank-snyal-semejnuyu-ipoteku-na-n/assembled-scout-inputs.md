# Assembled scout inputs — B33 slot 12 YEKT 2026-09-23

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-23  
**slot:** 12:00 Asia/Yekaterinburg  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (avoid recent live)

Recent 2026-09-23 live: KP лесополоса/забор соседа; мебельный пакет партнёра за 4 дня до ДДУ; созаёмщик отказался за 3 дня до эскроу.  
Recent skeleton «за N дней до ДДУ/эскроу» — **не повторять**.  
Closed clusters: escrow_not_opened_after_mortgage, mortgage_rate_hike_before_ddu, matkapital_* secondary, assignment B30, insurance B31, etc. — see used-clusters.json.

## Proposed lock (pre-checked 2026-09-23)

- **cluster_id:** `family_mortgage_child_age_7_ddu_day_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** семья берёт **новостройку** в Тюмени по **семейной ипотеке** (ребёнок был в лимите возраста при одобрении); в **день подписания ДДУ** ребёнку исполняется **7 лет** — банк пересчитывает программу, **снимает льготную ставку** / требует допвзнос или отказывает в выдаче; семья **останавливает сделку до эскроу**; на кону бронь/аванс застройщику (~150–250k composite)
- **why_newbuild_not_secondary:** семейная ипотека + ДДУ на объект в строящемся доме от застройщика, не вторичка/ЕГРН-продавец
- **title draft (H1 direction):** «В день подписания ДДУ ребёнку исполнилось 7 лет — банк снял семейную ипотеку на новостройку в Тюмени, семья отказалась от сделки»
- **comment_magnet_angle:** «Если день рождения ребёнка совпадает с подписанием ДДУ — вы переносите дату или рискуете ставкой?»
- **scout_helper.py --check-query:** PASS 2026-09-23 (anti_dupe_hard PASS, topic focus PASS)
- **formula_spam_check:** last3 live = KP forest / furniture partner / co-borrower escrow — this is **family mortgage age rule on signing day**, new skeleton (not «за N дней до»)

## Wordstat MCP-KV (live 2026-09-23)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| семейная ипотека тюмень | 55,11176 | 1243 |
| семейная ипотека тюмень 2026 | 55,11176 | 374 |
| купить новостройку в тюмени | 55,11176 | 898 |
| новостройки в тюмени купить в ипотеку | 55,11176 | 75 |

**wordstat_rework:** probe «семейная ипотека новостройка тюмень» weak → spine P0 «семейная ипотека тюмень» 1243 + mechanism child age 7 on DDU signing day

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: семья на финале ДДУ по новостройке с одобренной семейной ипотекой
- risk: потеря льготной программы в день подписания из‑за возраста ребёнка
- time: день подписания ДДУ (не «за N дней»)
- finale: отказ от подписания до эскроу; agency — как сверить дату рождения и график подписания с банком/застройщиком

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
