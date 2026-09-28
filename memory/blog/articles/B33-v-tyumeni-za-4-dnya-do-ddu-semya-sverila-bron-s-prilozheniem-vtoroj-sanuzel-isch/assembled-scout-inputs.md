# Assembled scout inputs — B33 slot 12 YEKT 2026-09-28

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-28  
**slot:** 12:00 Asia/Yekaterinburg (weekday morning longform)  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only  
**dzen_rf_pack:** true (dzen-content-rules + rf-blocked-entities pre-read)

## HARD anti-dupe (today live ~20 — DO NOT reuse)

Morning 09 slot today: EISJHS construction pause before escrow (`eiszhs-priostanovka-do-eskrou-tyumen`). Recent WP also: DDU commercial vs studio, taunhaus vs flat, rassrochka 340k, UK 180k keys, lift tehnadzor, rent ban 2y, parking, KP bron sold, lodzhiya cold, skidka 380k, planirovka 54→49 m².

**Rejected candidate:** family mortgage removed before DDU → SCOUT ANTI-DUPE HARD BLOCKER vs `mortgage_rate_hike_before_ddu` (payment/rate spike fingerprint).

## Proposed lock (pre-checked 2026-09-28)

- **cluster_id:** `ddu_second_bathroom_missing_bron_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** Tyumen newbuild flat; sales office + booking PDF / plan show **two bathrooms** (master + guest); family mortgage track; **4 days before DDU registration** buyer compares booking annex to DDU appendix — **second bathroom gone** (single WC only); price unchanged; family **stops registration** before escrow; composite casus (no real JK/bank/surnames as asserted facts in handoff)
- **why_newbuild_not_secondary:** DDU appendix vs developer booking on **строящийся объект** — not secondary EGRN / seller inspection plot
- **title draft (H1 direction):** «В Тюмени за 4 дня до ДДУ семья сверила бронь с приложением — второй санузел исчез из договора, регистрацию остановили»
- **slug:** `za-4-dnya-do-ddu-vtoroj-sanuzel-ischez-iz-prilozheniya-semya-ostanovila`
- **comment_magnet_angle:** «Если в брони два санузла, а в ДДУ один — вы бы подписывали “как есть” ради сохранения цены или срывали сделку?»
- **scout_helper.py --check-query:** PASS 2026-09-28 (anti_dupe_hard PASS, topic focus PASS)
- **h1_fingerprint:** `4days:ddu_layout_bathroom_mismatch` (mechanism layout/bathroom, NOT sqm-only like 54→49 post)
- **formula_spam:** last3 published B30/B31/B32 = pereustupka ban / insurance payment / escrow wrong entity — this is **layout appendix vs booking**, distinct skeleton

## Wordstat MCP-KV (live 2026-09-28)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 | RU 225 compare |
|--------|------------------|----------------|
| планировка квартира новостройка (probe) | 29 | — |
| новостройки тюмень (probe) | 4350 | — |
| **квартиры в тюмени новостройки (final P0)** | **1047** | **2347** |

**wordstat_rework:** probe «планировка квартира новостройка» 29 → weak for Tyumen spine → probe «новостройки тюмень» 4350 (generic) → **final P0 «квартиры в тюмени новостройки» 1047** (buyer demand + layout casus)

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: family compares booking plan to DDU appendix before signing
- risk: layout downgrade (second bathroom removed) with same price
- time: 4 days before DDU registration
- finale: registration stopped; agency landing — verify annex matches booking before escrow

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/
- https://t.me/klyshin_A (optional signal only; hook not from Klyshin)

Output handoff with ALL required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`, `signal_urls`, `wordstat:` line with live volumes only.
