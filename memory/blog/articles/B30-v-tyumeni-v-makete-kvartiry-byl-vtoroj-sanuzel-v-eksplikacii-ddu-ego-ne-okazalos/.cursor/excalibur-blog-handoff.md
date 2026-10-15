# Scout handoff — B30

**topic_id:** B30  
**run_date:** 2026-09-19  
**slot:** 17:00 Asia/Yekaterinburg  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень  
**status:** LOCKED

## Topic

**cluster_id:** `newbuild_layout_second_bathroom_missing_ddu_tyumen`

**Title draft / H1 direction:**

> В Тюмени в макете квартиры был второй санузел — в экспликации ДДУ его не оказалось, сделку заморозили

**P0:** «купить новостройку в тюмени» — **920**  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison region — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: квартира в новостройке Тюмени; в шоу-руме и PDF-буклете планировка с двумя санузлами (мастер + гостевой); оплачена бронь ~40–70 тыс. ₽; ипотека одобрена под эту площадь; за 2 дня до подписания ДДУ в экспликации помещений черновика — один совмещённый санузел; менеджер обещает «поправим в финальном ДДУ», но повторный проект без второго санузла; семья замораживает сделку до эскроу; риск удержания части брони — composite casus
why_newbuild_not_secondary: только маркетинг застройщика, экспликация ДДУ и эскроу-путь в новостройке; нет продавца вторички, ЕГРН, опеки, банкротства
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; B27–B29 today excluded
dzen_casus_shape: PASS; event: семья выбрала планировку с двумя санузлами; risk: экспликация ДДУ не совпадает с макетом; time: 2 дня до ДДУ; finale: остановились до эскроу, agency — сверять экспликацию до денег
comment_magnet_angle: «Если в макете два санузла, а в ДДУ один — вы бы подписали “с поправкой потом” или развернулись до эскроу?»
wordstat_rework: probe «планировка квартиры новостройка» 23 → spine P0 «купить новостройку в тюмени» 920
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» — 920
story_dup_check: PASS | cluster_id: newbuild_layout_second_bathroom_missing_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: two_bathrooms_showroom_vs_ddu_explication
formula_spam_check: PASS | last3_mechanisms: declaration/land (B27), KP gas dates (B28), zero-down promo clock (B29) — layout explication mismatch is new
anti_dupe_hard: PASS
```

## Demand probes

| Запрос | Результат |
|---|---:|
| новостройки тюмень | 4430 |
| купить новостройку в тюмени | 920 |
| новостройки в тюмени от застройщика | 663 |
| планировка квартиры новостройка | 23 |

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
