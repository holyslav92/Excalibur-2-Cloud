# Assembled scout inputs — B29 slot 15 YEKT 2026-09-19 (weekend owner request)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-19  
**slot:** 15:00 Asia/Yekaterinburg (weekend)  
**topic_id:** B29  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (today already live — DO NOT reuse)

1. B27 09:00 — land lease vs ownership in declaration | `newbuild_land_lease_not_ownership_declaration_tyumen` | energy `paper_clean_then_broke`
2. B28 12:00 — KP gas 2026 vs declaration 2028 | `newbuild_kp_gas_declaration_date_mismatch_tyumen` | energy `paper_clean_then_broke`

Also avoid: family mortgage «child turned 7 / 19 days to Oct 1» rewrite (live today). Prefer **different** top_energy_mirror than `paper_clean_then_broke`.

## Proposed lock (pre-checked)

- **cluster_id:** `newbuild_developer_zero_down_program_expired_before_ddu_tyumen`
- **top_energy_mirror:** `clock_ran_out`
- **newbuild_mechanism:** apartment in Tyumen newbuild; sales office + booking promise «ипотека без первоначального взноса от застройщика» / subsidized bank program tied to developer promo; mortgage approved on that terms; **6 days before DDU** bank notifies program ended / subsidy window closed; payment jumps (~18k/month in casus); family cannot assemble down payment in time; **stop before escrow**; booking partial loss (e.g. 50–80k withheld) — composite Tyumen casus, no real surnames/JK/bank names in handoff body as “fact”
- **why_newbuild_not_secondary:** DDU + developer promo + escrow path + newbuild only — no secondary EGRN seller plot
- **title draft (H1 direction):** «В Тюмени за шесть дней до ДДУ банк снял ипотеку без взноса от застройщика — семья не успела собрать первоначальный платёж»
- **comment_magnet_angle:** «Если банк снимает “нулевой взнос” за неделю до ДДУ, вы бы торопились подписать или ждали, пока застройщик вернёт программу?»
- **scout_helper.py --check-query:** PASS 2026-09-19 (anti_dupe_hard PASS, topic focus PASS)
- **formula_spam:** last3 must differ from declaration-mismatch skeleton (B27+B28); this is bank promo clock, not PD vs booking text

## Wordstat MCP-KV (live 2026-09-19)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| ипотека от застройщика | 55,11176 | 715 |
| ипотека от застройщика тюмень | 55,11176 | 514 |
| ипотека без первоначального взноса тюмень от застройщика | 55,11176 | 197 |
| ипотека от застройщика без взноса | 55,11176 | 210 |
| новостройки тюмень | (probe if needed) | — |

**wordstat_rework:** probe «бронь новостройка тюмень» (MCP empty once) → spine P0 «ипотека от застройщика тюмень» 514 + mechanism zero-down promo expiry

**klyshin_hook:** none (optional not used)

## dzen_casus_shape: PASS

- event: family on newbuild track with developer zero-down promo
- risk: clock on bank/developer subsidy program
- time: 6 days before DDU
- finale: stopped before escrow; partial booking loss; agency landing (what to verify in writing before booking)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
