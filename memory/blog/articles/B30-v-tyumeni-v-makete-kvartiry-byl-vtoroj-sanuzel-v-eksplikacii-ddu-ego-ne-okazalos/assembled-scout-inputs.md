# Assembled scout inputs — B30 slot 17 YEKT 2026-09-19 (weekend owner request)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-19  
**slot:** 17:00 Asia/Yekaterinburg (weekend)  
**topic_id:** B30  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (today already live — DO NOT reuse)

1. B27 — land lease vs ownership in declaration | `paper_clean_then_broke`
2. B28 — KP gas 2026 vs declaration 2028 | `paper_clean_then_broke`
3. B29 — bank removed zero-down developer promo 6 days before DDU | `clock_ran_out`
Also live today (WP): 4% discount missing in DDU draft; KP ceilings 25 cm lower; child turned 7 family mortgage removed.

**Proposed lock (pre-checked 2026-09-19):**
- **cluster_id:** `newbuild_layout_second_bathroom_missing_ddu_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** Tyumen newbuild apartment; sales gallery + PDF booklet show **two bathrooms** (master + guest WC); booking paid (~40–70k); mortgage approved on that layout; **2 days before DDU signing** family compares **экспликация помещений** in draft DDU — only **one** combined bathroom; manager says «это черновик, поправим» but revised draft still one WC; family **freezes deal before escrow**; partial booking loss risk — composite casus
- **why_newbuild_not_secondary:** only DDU + newbuild sales materials + escrow path; no secondary EGRN seller
- **title draft:** «В Тюмени в макете квартиры был второй санузел — в экспликации ДДУ его не оказалось, сделку заморозили»
- **comment_magnet_angle:** «Если в макете два санузла, а в ДДУ один — вы бы подписали “с поправкой потом” или развернулись до эскроу?»
- **scout_helper --check-query:** PASS 2026-09-19 (anti_dupe_hard PASS, topic focus PASS)

## Wordstat MCP-KV (live 2026-09-19)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| новостройки тюмень | 55,11176 | 4430 |
| купить новостройку в тюмени | 55,11176 | 920 |
| новостройки в тюмени от застройщика | 55,11176 | 663 |
| планировка квартиры новостройка | 55,11176 | probe partial |

**wordstat_rework:** spine P0 «купить новостройку в тюмени» 920 + mechanism layout/explication mismatch

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: family chose layout with 2 bathrooms in showroom
- risk: DDU explication does not match marketing layout
- time: 2 days before DDU
- finale: stopped before escrow; agency on comparing explication before money

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
