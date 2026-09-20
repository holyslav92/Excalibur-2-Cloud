# Assembled scout inputs — B30 slot 09 YEKT 2026-09-20 (weekend owner request)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-20  
**slot:** 09:00 Asia/Yekaterinburg (Sunday weekend)  
**topic_id:** B30  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (avoid recent live)

Recent 2026-09-19: B27 land lease, B28 KP gas dates, B29 zero-down bank promo, plus live posts on sanuzel/maket/discount/semejnaya ipoteka 7 years.  
Do NOT reuse booking_expired cluster, declaration-only mismatch without new mechanism, or assignment 28-day wait plot (live 2026-09-18).

## Proposed lock (pre-checked 2026-09-20)

- **cluster_id:** `newbuild_assignment_resale_ban_ddu_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** investor/family buys **переуступка** on Tyumen newbuild (DDU assignment path); sales office + assignment agreement looked clean; **3 days before signing** the draft DDU appendix shows **clause banning resale/assignment for 3 years** (or similar lock-in) not shown in booking chat / assignment offer summary; buyer planned flip or exit before keys; **stopped before escrow**; partial assignment fee at risk (~80–120k composite)
- **why_newbuild_not_secondary:** переуступка прав по ДДУ на объект в строящемся доме — not secondary EGRN seller casus
- **title draft (H1 direction):** «За 3 дня до ДДU в проекте переуступки всплыл запрет перепродажи на 3 года — сделку в Тюмени остановили до эскроу»
- **comment_magnet_angle:** «Если в переуступке всплывает запрет продажи на 3 года — вы подписываете или ищете другой лот?»
- **scout_helper.py --check-query:** PASS 2026-09-20 (anti_dupe_hard PASS, topic focus PASS; fingerprint assignment_lost distinct from 28-day wait live)
- **formula_spam_check:** last3 B27 declaration land, B28 KP gas, B29 bank zero-down — this is assignment contract clause / investor exit, new skeleton

## Wordstat MCP-KV (live 2026-09-20)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| купить новостройку в тюмени | 55,11176 (RU compare) | 1917 |
| новостройки тюмень купить от застройщика | 55,11176 | 985 |
| переуступка новостройка тюмень | 55,11176 | MCP empty once |
| купить новостройку в тюмени в ипотеку | 55,11176 | 129 |

**wordstat_rework:** probe «переуступка новостройка тюmenь» empty → spine P0 «купить новостройку в тюмени» 1917 + mechanism assignment resale ban in DDU draft

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: buyer on assignment track for Tyumen newbuild
- risk: hidden resale/assignment restriction in DDU draft
- time: 3 days before signing / escrow
- finale: stopped before escrow; agency landing on what to read in assignment + DDU project before fee

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
