# Scout assembled inputs — slot 2026-10-01 09:00 YEKT

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals, no «запустите Derouter». Output the complete handoff text now per SKILL checklist.

**topic_id (director):** B34  
**slot_rubric:** novostroyki (новостройки Тюмень)  
**trend_radar:** `memory/blog/trend-radar/trend-radar.json` (slot_rubric=novostroyki, MECHANICS_AND_ENERGY_ONLY)

## Preflight read

- `shared/dzen-content-rules.md` + `shared/rf-blocked-entities.json` — OK (no Meta/DENY heroes in topic)
- `shared/dzen-news-casus.md`, `shared/newbuild-focus-lock.md`, `shared/dzen-top-angle-newbuild-lock.md`
- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` — OK (director, 2026-10-01)

## Live blog ~20 (WP titles, newest first)

1. За 6 дней до аванса в Тюмени на вторичке всплыло банкротство продавца — семья не перевела деньги
2. Во вторичке Тюмени — запрет пристава сорвал аванс за 4 дня
3. В Тюмени за 5 дней двор без машин стал проездом — бронь урезали
4. На приёмке в Тюмени нашли промёрзшую стену — ключи через 40 дней
5. В Тюмени аренда на 3 года в ЕГРН остановила сделку
6. В Тюмени дарственная остановила сделку за 7 дней до аванса
7. За 3 дня до эскроу в новостройке Тюмени площадь в ДДУ урезали — ипотека не сошлась
8. За 5 дней до эскроu банк остановил семейную ипотеку без свидетельства
9. За 3 дня до аванса в Тюмени всплыл долг за свет 186 тысяч — семья отказалась от сделки
10. В Тюмени за 4 дня до ДДУ застройщик привязал чистовую к подрядчику — без допсоглашения эскроу не открыли
11. В Тюмени банк потребовал созаёмщика за 3 дня до эскроу — в брони был один
12. В новостройке Тюмени за 4 дня до ДДУ исчез второй санузел — семья остановила регистрацию
13. (ledger) B32 — чужое юрлицо в реквизитах эскроу
14. B31 — страховка подняла платёж перед ДДУ
15. B30 — запрет переуступки 3 года
16. B29 — нулевой взнос сняли за 6 дней до ДДУ
17. B28 — газ в КП 2026 vs 2028 в декларации
18. B27 — земля в аренде vs обещание собственности
19. B26 — РВЭ нет — второй транш
20. B25 — чистовая в ДДУ vs голые стены

**Formula spam guard:** last live/published mix heavy on «за N дней банк/эскроу остановил» и secondary casus — candidate avoids бронь+сутки+ДДУ skeleton and secondary plots.

## Trend Radar energy (novostroyki slot — mechanics ONLY, NOT rent plot)

Mirror from rubrics.novostroyki angles:
- **mechanism:** `договор vs реальность` (реклама/устное vs проектная декларация)
- **NOT used as plot:** аренда, сдача внаём, диван под сдачу (top viral in feed — forbidden as story)

Mirror from vtorichka top energy (plot stays newbuild):
- **top_energy_mirror:** `paper_clean_then_broke` — «на бумаге/в рекламе обещали одно, в документе застройщика — другое»

## Candidate topic (news-casus)

**cluster_id:** `newbuild_pd_school_deadline_vs_ads_tyumen`  
**newbuild_mechanism:** инфраструктура ЖК — школа в рекламе/на стенде vs срок в проектной декларации; семья остановила подписание ДДУ до эскроу  
**why_newbuild_not_secondary:** сюжет только про покупку квартиры в ЖК от застройщика (ДДУ, проектная декларация 214-ФЗ), не про вторичку/аванс/ЕГРН продавца  

**short title (research_start):** Школа в рекламе ЖК vs проектная декларация — ДДУ не подписали  

**H1 draft:** В Тюмени за две недели до ДДУ семья сверила школу из рекламы — в проектной декларации срок 2030, подписание остановили  

**dzen_casus_shape:** PASS  
- event: семья готовилась к ДДУ после одобрения ипотеки, сверила обещание «школа рядом/скоро» с актуальной проектной декларацией  
- risk: покупка «под детей» без инфраструктуры в горизонте семьи; нельзя «дописать» школу в ДДУ  
- time: за две недели до подписания ДДУ  
- finale: подписание остановили, бронь/условия под вопросом (agency: проверять PD до аванса застройщику, не только рендер)  

**comment_magnet_angle:** «Если в декларации школа через пять лет — вы всё равно берёте квартиру под ребёнка или нет?»  

**klyshin_hook:** none  

## Wordstat preflight (MCP-KV live)

```
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat_rework:
  probe «парковочное место новостройка» 2 (reg 55) →
  probe «машиноместо новостройка» 5 (reg 55) →
  probe «семейная ипотека новостройка тюмень» 15 (reg 55) →
  rework: усилить buyer spine «новостройки тюмень» + casus PD/инфраструктура (не drop news-casus) →
  final P0 «новостройки тюмень» 3553 (reg 55); compare «купить новостройку в тюмени» 686 (55) / 900 (11176) / 1907 (225)
top_energy_mirror: paper_clean_then_broke (+ trend mechanic договор vs реальность, NOT rent plot)
newbuild_mechanism: «реклама школы vs срок в проектной декларации — стоп ДДУ»
why_newbuild_not_secondary: «214-ФЗ PD и ДДУ застройщика, не сделка с физлицом на вторичке»
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: (all in memory/scout/used-clusters.json — candidate matches NO frozen cluster regex)
dzen_casus_shape: PASS (see above)
comment_magnet_angle: «…школа через пять лет — всё равно берёте под ребёнка?»
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 3553
story_dup_check: PASS | cluster_id: newbuild_pd_school_deadline_vs_ads_tyumen
h1_fingerprint_check: PASS | fingerprint: (no number bucket collision with 48h/500k published)
formula_spam_check: PASS | last3_mechanisms: (secondary bailiff/bankruptcy + newbuild courtyard — distinct from PD/school)
anti_dupe_hard: PASS
slot_rubric: novostroyki
viral_mechanism: договор vs реальность (energy from trend-radar, newbuild plot)
```

## Director handoff fields

- topic_id: B34
- wp_category expectation: novostroyki / proverka-pered-pokupkoj or ipoteka per topic_defaults
- engagement: Dzen comment magnet on school timeline vs family choice
