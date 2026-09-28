# Scout handoff — B33

run_date: 2026-09-27  
slot: 09:00 Asia/Yekaterinburg (weekend owner path)  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_uk_membership_fee_before_keys_not_in_ddu_tyumen`

**Title draft / H1 direction:**

> За 5 дней до ключей в тюменской новостройке потребовали 180 тысяч в УК — в ДДУ этой строки не было

**P0:** «новостройки тюмень» — **8242** (Tyumen 55); «купить новостройку в тюмени» — **1928**  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_top_requests OK (новостройки тюмень 8242)
top_energy_mirror: stopped_before_money
newbuild_mechanism: семья на финале новостройки Тюмени; за 5 дней до ключей застройщик/ОП требует «взнос в УК» / членский взнос ~180 тыс ₽ до подписания акта; в ДДУ и брони строки нет; банк не открывает финальный транш / семья не вносит наличные — стоп до акта приёмки
why_newbuild_not_secondary: объект по ДДУ на этапе ввода/ключей, не сделка с продавцом вторички; риск — навязанные платежи до регистрации права
klyshin_hook: none (energy only: «остановили до денег»)
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK (2026-09-27)
dzen_casus_shape: PASS | event: ключи новостройки | risk: внезапный взнос УК | time: 5 дней до ключей | finale: стоп, проверка ДДУ/214-ФЗ, agency до акта
comment_magnet_angle: «Вам когда-нибудь требовали оплатить УК или «членский взнос» до ключей — а в ДДУ этого не было? Что сделали?»
wordstat_rework: probe «передача ключей новостройка» 3 → spine «новостройки тюмень» 8242 + «купить новостройку в тюмени» 1928
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 8242
story_dup_check: PASS | cluster_id: newbuild_uk_membership_fee_before_keys_not_in_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: amount:uk_fee_before_keys_not_in_ddu
formula_spam_check: PASS | last3_mechanisms: live lift techadzor; rent ban DDU; parking benefit cancel (distinct from UK fee)
anti_dupe_hard: PASS
```
