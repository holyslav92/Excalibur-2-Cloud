# Scout handoff — B33

run_date: 2026-09-23  
slot: automation  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_furniture_bundle_partner_before_ddu_tyumen`

**Title draft / H1 direction:**

> За 4 дня до ДДУ застройщик в Тюмени потребовал купить мебельный пакет у партнёра — без него отказался подписывать договор на новостройку

**P0:** «купить новостройку в тюмени» — **898** (Scout MCP-KV, region 55); mechanism «новостройки тюмень дду»  
**Wordstat source:** live MCP-KV Wordstat (Research re-probe 2026-09-23)  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK (doctor)
top_energy_mirror: last_mile_addon_trap / office_pressure_before_signature
newbuild_mechanism: семья покупает квартиру в **новостройке** Тюмени по ДДУ + ипотека; бронь и согласованная цена квартиры в офисе; за **4 дня** до подписания ДДУ менеджер выдаёт **отдельный** договор на «мебельный пакет» у **партнёрской** фирмы (не застройщик) на **~350–480 тыс ₽** и говорит: без оплаты/подписания пакета **не выдадут** проект ДДУ на регистрацию; в черновике ДДУ мебели **нет**, в рекламе — «можно обставить самим»; семья **останавливается**, бронь **~70–100 тыс ₽** под угрозой (composite casus)
why_newbuild_not_secondary: только ДДУ, эскроу, ипотека на строящийся объект от застройщика — не вторичка/ЕГРН
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger; HARD skip clusters B30 assignment, B31 insurance, B32 escrow INN, B29 zero-down, separate-DDU kladovaya (WP 2026-09-22) — другой предмет
dzen_casus_shape: PASS | event: давление мебельным пакетом у партнёра | risk: навязанная допуслуга ломает бюджет/ипотеку | time: 4 дня до ДДУ | finale: стоп до подписи, agency — что отделить в документах
comment_magnet_angle: «Если застройщик за пару дней до ДДУ требует мебель только у “своего” партнёра — вы подписываете пакет или уходите с брони?»
wordstat_rework: live 2026-09-23 «купить новостройку в тюмени» **682** (55) + «от застройщика» 330; узкий «мебельный пакет новостройка» — слабый → spine P0 + jargon ДДУ/допсоглашение/214-ФЗ + ЗоЗПП ст.16 навязывание
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 scout 898 / research 682 | mechanism дду+новостройка в тексте
story_dup_check: PASS | cluster_id: newbuild_furniture_bundle_partner_before_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: furniture_partner_bundle_four_days_before_ddu_refusal
formula_spam_check: PASS | last3: B30 resale ban; B31 insurance; B32 escrow INN
anti_dupe_hard: PASS
signal_urls:
  - https://72.ru/text/realty/2026/09/22/76648597/
  - https://72.ru/text/realty/2026/09/11/76634906/
  - https://harant.ru/blog/zashchita-prav-potrebitelej/navyazyvanie-dopolnitelnyh-uslug-kak-zashhitit-svoi-prava-po-zakonu/
```
