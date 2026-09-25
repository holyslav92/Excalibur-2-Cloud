# Scout handoff — B33

run_date: 2026-09-25  
slot: 10:14 Asia/Yekaterinburg (cron automation)  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_parking_separate_ddu_mortgage_tyumen`

**Title draft / H1 direction:**

> За 4 дня до эскроу в новостройке Тюмени машиноместо из акции вынесли в отдельный ДДУ — банк не заложил паркинг, семья остановила сделку

**P0:** «купить квартиру тюмень от застройщика в новостройке» — **310** (Tyumen 55+11176); anchor «квартира в тюмени купить новостройки» — **625**  
**Wordstat source:** live MCP-KV Wordstat 2026-09-25  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: number_in_claim_vs_zero_paid
newbuild_mechanism: новостройка Тюмени; в брони/КП «паркинг в подарок» или «в цене»; за 4 дня до эскроу — отдельный ДДУ на машиноместо (850–950 тыс ₽ composite); банк залогирует только квартиру; семья без второго кредита/наличных — стоп до эскроu
why_newbuild_not_secondary: машиноместо и квартира по ДДU застройщика на строящийся объект, не вторичный гараж/ЕГРН продавца
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
dzen_casus_shape: PASS | event: скрытый отдельный ДДУ на паркинг | risk: +900 тыс вне ипотеки | time: 4 дня до эскроu | finale: стоп, пересбор пакета или отказ от места
comment_magnet_angle: «Если паркинг вынесли в отдельный договор накануне эскроu — вы доплачиваете наличными или отказываетесь от машиноместа?»
wordstat_rework: probe «машиноместо дду» partial → P0 «купить квартиру тюмень от застройщика в новостройке» 310 + «квартира в тюмени купить новостройки» 625
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру тюмень от застройщика в новостройке» 310
story_dup_check: PASS | cluster_id: newbuild_parking_separate_ddu_mortgage_tyumen
h1_fingerprint_check: PASS | fingerprint: parking_separate_ddu_four_days_before_escrow
formula_spam_check: PASS | last3_mechanisms: pereustupka lot; last floor mortgage; matkapital escrow
anti_dupe_hard: PASS
```
