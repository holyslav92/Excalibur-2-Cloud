# Scout handoff — B31

run_date: 2026-09-20  
slot: 12:00 Asia/Yekaterinburg (Sunday weekend Grok routine)  
topic_id: B31  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_mortgage_insurance_requote_before_ddu_tyumen`

**Title draft / H1 direction:**

> За 2 дня до ДДU страховка подняла платёж на 18 тысяч — банк снял одобрение новостройки в Тюмени

**P0:** «купить новостройку в тюмени» — **1917** (spine) + «страхование ипотеки» — **913** (Tyumen 55, mechanism)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: number_claimed_vs_unpaid
newbuild_mechanism: семья покупает квартиру в новостройке Тюмени по ДДU; банк одобрил ипотеку с расчётным платежом при **ориентировочной** стоимости страховки; за **2 дня** до подписания ДДU страховщик выставил финальный полис — премия выросла (~18 000 ₽/мес к полному платежу); банк пересчитал ПДН/лимит и **снял одобрение**; эскроу не открыли; бронь ~60–90 тыс ₽ под удержанием (composite casus)
why_newbuild_not_secondary: только ДДU, эскроu, ипотека на строящийся объект от застройщика — не вторичка/ЕГРН
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; HARD skip B30 cluster assignment_resale_ban
dzen_casus_shape: PASS | event: одобренная ипотека на новостройку | risk: финальная страховка ломает платёж | time: 2 дня до ДДU | finale: стоп до эскроu, agency что сверять до брони
comment_magnet_angle: «Если страховка в последний день добавляет 18 тысяч к платежу — вы успеваете пересобрать одобрение или откладываете покупку?»
wordstat_rework: probe «страхование ипотеки новостройка тюмень» → spine «купить новостройку в тюмени» 1917 + mechanism «страхование ипотеки» 913 (region 55)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новostройку в тюмени» 1917 | mechanism «страхование ипотеки» 913
story_dup_check: PASS | cluster_id: newbuild_mortgage_insurance_requote_before_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: insurance_requote_two_days_before_ddu_approval_revoked
formula_spam_check: PASS | last3_mechanisms: B28 KP gas; B29 zero-down promo; B30 assignment resale ban
anti_dupe_hard: PASS
```
