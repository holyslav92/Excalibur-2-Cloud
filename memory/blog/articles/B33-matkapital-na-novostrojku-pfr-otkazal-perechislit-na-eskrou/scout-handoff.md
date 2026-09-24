# Scout handoff — B33

run_date: 2026-09-24  
slot: 10:00 UTC (~15:00 Asia/Yekaterinburg)  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_matkapital_pfr_escrow_ddu_wording_tyumen`

**Title draft / H1 direction:**

> Материнский капитал на новостройку в Тюмени — ПФР отказал перечислить на эскроу из-за одной строки в ДДУ

**P0:** «купить новостройку в тюмени» — **897** (Tyumen 55+11176 spine) + «материнский капитал» — **7044** (Tyumen 55, mechanism)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225 («купить новостройку в тюмени» **1921**)

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: семья с двумя детьми берёт квартиру в новостройке Тюмени по ДДУ с ипотекой; планирует направить материнский (и при необходимости региональный) капитал на эскроу-счёт; за **неделю** до подписания ДДУ ПФР/СФР отклоняет заявление на перечисление — в проекте договора неверно указаны доли детей / целевое назначение / реквизиты эскроу; без маткапитала не хватает собственных средств; сделку останавливают до исправления проекта ДДУ (composite casus)
why_newbuild_not_secondary: только ДДУ, эскроу, маткапитал на покупку у застройщика — не вторичка/ЕГРН/опека на вторичном рынке
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; skip frozen secondary matkapital_opieka clusters
dzen_casus_shape: PASS | event: отказ ПФР на маткапитал | risk: не откроют эскроу в срок | time: неделя до ДДУ | finale: стоп, правят договор, agency
comment_magnet_angle: «Если ПФР завернул маткапитал на новостройку из-за одной строки в ДДУ — вы бы успели переписать договор до брони или отказались бы от объекта?»
wordstat_rework: probe «материнский капитал новостройка тюмень» (low volume API) → spine «купить новостройку в тюмени» 897 + mechanism «материнский капитал» 7044 (region 55)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 897 | mechanism «материнский капитал» 7044
story_dup_check: PASS | cluster_id: newbuild_matkapital_pfr_escrow_ddu_wording_tyumen
h1_fingerprint_check: PASS | fingerprint: matkapital_pfr_reject_ddu_wording_week_before
formula_spam_check: PASS | last3_mechanisms: detsad render; child 7 family mortgage; KP forest fence — distinct matkapital/PFR
anti_dupe_hard: PASS
```
