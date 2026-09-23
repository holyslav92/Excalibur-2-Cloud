# Scout handoff — B33

**topic_id:** B33  
**run_date:** 2026-09-23  
**slot:** 12:00 Asia/Yekaterinburg  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень  
**status:** LOCKED

## Topic

**cluster_id:** `kp_plot_buffer_forest_promised_cadastre_neighbor_fence_before_ddu_tyumen`

**Title draft / H1 direction:**

> Под Тюменью в КП обещали лесополосу у участка — за 6 дней до ДДУ в кадастровом плане оказался забор соседа

**P0:** «коттеджные поселки тюмень купить дом» — **44**  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison region — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: дом в коттеджном посёлке под Тюменью от застройщика; в буклете и на визуализации — «зелёный буфер / лесополоса» за участком; за 6 дней до ДДУ на дом+землю запросили кадастровый план — граница с соседом с забором, полоса сужена; банк предупредил о риске спора; семья остановила сделку до эскроу, бронь под угрозой
why_newbuild_not_secondary: только КП/ИЖС от застройщика, ДДУ на дом и землю, эскроу и декларация посёлка; нет вторичного участка, наследников, банкротства продавца
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; closed_clusters exclude cellar/parking split, show-room ceiling, terrace viz, gas date, co-borrower escrow
dzen_casus_shape: PASS | event: семья выбрала дом в КП под Тюменью; risk: обещанный «лес» не совпал с кадастром; time: 6 дней до ДДУ; finale: остановили до эскроу, бронь не вернули полностью в composite casus
comment_magnet_angle: «Если на кадастровом плане у участка в КП уже стоит забор соседа, вы бы подписали ДДУ или снимали бронь?»
wordstat_rework: probe «остекление балкона новостройка» — 1 (слабо) → final P0 «коттеджные поселки тюмень купить дом» — 44; RU compare «купить дом в коттеджном поселке» — 4954
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «коттеджные поселки тюмень купить дом» — 44
story_dup_check: PASS | cluster_id: kp_plot_buffer_forest_promised_cadastre_neighbor_fence_before_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: six_days_before_DDU + KP_forest_buffer_vs_neighbor_fence_cadastre
formula_spam_check: PASS | last3_mechanisms: furniture package partner; co-borrower escrow freeze; show-room ceiling — differs (KP land boundary)
anti_dupe_hard: PASS
```

## Demand probes

| phrase | region | shows |
|--------|--------|-------|
| коттеджные поселки тюмень купить дом | 55+11176 | 44 |
| купить дом в коттеджном поселке | 225 | 4954 |
