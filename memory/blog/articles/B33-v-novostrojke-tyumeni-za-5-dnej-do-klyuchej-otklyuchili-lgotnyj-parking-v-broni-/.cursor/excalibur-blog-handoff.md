# Scout handoff — B33

run_date: 2026-09-26  
slot: 15:00 Asia/Yekaterinburg (Saturday automation run)  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_parking_promo_revoked_before_keys_tyumen`

**Title draft / H1 direction:**

> В новостройке Тюмени за 5 дней до ключей отключили льготный паркинг — в брони обещали полгода бесплатно

**P0:** «новостройки тюмень» — **4326** (55) / **8242** (225 compare) + «купить новостройку в тюмени» — **892** (mechanism spine)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_top_requests OK (partial empty on niche parking phrase)
top_energy_mirror: number_claimed_vs_unpaid (обещали «0 ₽ полгода» — перед ключами тариф включили)
newbuild_mechanism: семья покупает квартиру в новостройке Тюмени; в брони/КП зафиксирован льготный паркинг (6 мес бесплатно или фикс 0 ₽); за **5 дней** до выдачи ключей УК/застройщик меняет условия — льгота исчезает, ежемесячный платёж за машино-место ~8–12 тыс ₽; семья пересчитывает бюджет, откладывает подписание акта/регистрацию или торгуется за письменное продление (composite casus)
why_newbuild_not_secondary: паркинг/машино-место в ЖК от застройщика, ДДU/акт приёмки, не вторичный гараж
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; distinct from LIVE separate DDU parking (2026-09-25) — там отдельный ДДU, здесь **льготный тариф в брони отозван**
dzen_casus_shape: PASS | event: обещанный бесплатный паркинг | risk: ежемесячный платёж +4000–12000 к бюджету | time: 5 дней до ключей | finale: стоп/переговоры, agency — что фиксировать до брони
comment_magnet_angle: «Если паркинг «бесплатно полгода» пропадает за неделю до ключей — вы всё равно подписываете акт или торгуетесь?»
wordstat_rework: niche «паркинг новостройка тюmenь» weak → spine «новостройки тюмень» 4326 + «купить новостройку в тюмени» 892
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4326 | mechanism «купить новostройку в тюmenи» 892
story_dup_check: PASS | cluster_id: newbuild_parking_promo_revoked_before_keys_tyumen
h1_fingerprint_check: PASS | fingerprint: parking_promo_six_months_revoked_five_days_before_keys
formula_spam_check: PASS | last3_mechanisms: separate DDU parking; area act mismatch; booking discount erased — new angle promo revoke
anti_dupe_hard: PASS
```
