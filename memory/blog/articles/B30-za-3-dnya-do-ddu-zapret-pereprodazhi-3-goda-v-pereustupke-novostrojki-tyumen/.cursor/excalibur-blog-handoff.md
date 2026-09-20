# Scout handoff — B30

run_date: 2026-09-20  
slot: 09:00 Asia/Yekaterinburg  
topic_id: B30  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_assignment_resale_ban_ddu_tyumen`

**Title draft / H1 direction:**

> За 3 дня до ДДU в проекте переуступки всплыл запрет перепродажи на 3 года — сделку в Тюмени остановили до эскроу

**P0:** «купить новостройку в тюмени» — **1917**  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: переуступка на новостройку Тюмени; за 3 дня до подписания в проекте ДДU пункт запрета перепродажи/новой уступки 3 года — не было в переписке о переуступке; покупатель планировал выход до ключей; остановка до эскроu; риск комиссии переуступки ~80–120 тыс ₽ (composite)
why_newbuild_not_secondary: переуступка прав по ДДU на строящийся объект, не вторичка/ЕГРН продавца
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
dzen_casus_shape: PASS | event: переуступка новостройки | risk: скрытый lock-in 3 года | time: 3 дня до подписания | finale: стоп до эскроu
comment_magnet_angle: «Если в переуступке всплывает запрет продажи на 3 года — вы подписываете или ищете другой лот?»
wordstat_rework: probe «переуступка новостройка тюмень» empty → P0 «купить новостройку в тюмени» 1917
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 1917
story_dup_check: PASS | cluster_id: newbuild_assignment_resale_ban_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: assignment_resale_ban_three_years_before_escrow
formula_spam_check: PASS | last3_mechanisms: B27 land lease; B28 KP gas; B29 zero-down promo
anti_dupe_hard: PASS
```
