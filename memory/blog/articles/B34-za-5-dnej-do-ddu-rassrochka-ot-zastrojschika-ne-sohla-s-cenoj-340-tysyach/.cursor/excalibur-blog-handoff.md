# Scout handoff — B34

run_date: 2026-09-27  
slot: 12:00 Asia/Yekaterinburg (Sunday weekend Grok Bot)  
topic_id: B34  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_installment_schedule_total_mismatch_ddu_tyumen`

**Title draft / H1 direction:**

> За 5 дней до ДДУ рассрочка от застройщика не сходилась с ценой на 340 тысяч — семья остановила регистрацию в Тюмени

**P0:** «купить новостройку в тюмени» — **892** (spine) + «новостройки в рассрочку от застройщика» — **11** (Tyumen 55, mechanism)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: number_in_claim_vs_zero_paid
newbuild_mechanism: семья берёт квартиру в новостройке Тюмени по ДДУ с рассрочкой от застройщика; в договоре одна итоговая цена, в приложении — график платежей; за **5 дней** до подписания и регистрации сверка показала **разрыв ~340 000 ₽** (сумма графика ≠ цена ДДУ + взнос); банк/юрист советуют не регистрировать до выравнивания; бронь и аванс под риском (composite casus)
why_newbuild_not_secondary: только ДДУ, эскроу/рассрочка застройщика на строящийся объект — не вторичка и не ЕГРН-сюжет
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; skip B33 UK fee; skip weekend bron/площадь/лифт/паркинг clusters
dzen_casus_shape: PASS | event: финальный пакет ДДУ с рассрочкой | risk: цифры в договоре и графике расходятся | time: 5 дней до регистрации | finale: стоп до правки, agency — сверка до аванса
comment_magnet_angle: «Если в графике рассрочки не хватает сотен тысяч до суммы в ДДУ — вы подписываете или ждёте новый пакет?»
wordstat_rework: probe «рассрочка от застройщика новостройка» 11 → spine «купить новостройку в тюмени» 892 (region 55)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 892 | mechanism «новостройки в рассрочку от застройщика» 11
story_dup_check: PASS | cluster_id: newbuild_installment_schedule_total_mismatch_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: installment_schedule_340k_mismatch_five_days_before_ddu
formula_spam_check: PASS | last3_mechanisms: B33 UK fee before keys; lift tech inspection; rental ban in DDU
anti_dupe_hard: PASS
```
