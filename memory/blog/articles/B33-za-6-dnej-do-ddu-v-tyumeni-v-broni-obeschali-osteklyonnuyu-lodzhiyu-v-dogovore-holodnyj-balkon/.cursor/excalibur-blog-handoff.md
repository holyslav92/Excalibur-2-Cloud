# Scout handoff — B33

run_date: 2026-09-26  
slot: 09:00 Asia/Yekaterinburg  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED

## Topic

**cluster_id:** `newbuild_glazed_loggia_promised_cold_balcony_ddu_tyumen`

**Title draft / H1 direction:**

> За 6 дней до ДДУ в Тюмени в брони обещали остеклённую лоджию — в договоре холодный балкон, банк урезал ипотеку

**slug:** `za-6-dnej-do-ddu-v-tyumeni-v-broni-obeschali-osteklyonnuyu-lodzhiyu-v-dogovore-holodnyj-balkon`

**article_dir:** `memory/blog/articles/B33-za-6-dnej-do-ddu-v-tyumeni-v-broni-obeschali-osteklyonnuyu-lodzhiyu-v-dogovore-holodnyj-balkon`

**P0:** «новостройки тюмень» — **4326** (регионы 55+11176); compare RU «купить новостройку в тюмени» — **1928** (225)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: трёшка в строящемся ЖК Тюмени в ипотеку; в брони и на планировке «лоджия с остеклением, тёплый контур»; за 6 дней до ДДУ в приложении — неостеклённый балкон, остекление отдельным договором ~280–320 тыс ₽; банк урезал лимит ~450 тыс ₽; стоп до эскроу; бронь 150 тыс частично удержали (composite)
why_newbuild_not_secondary: бронь + приложение к ДДУ на квартиру в новостройке, спецификация балкона/лоджии и пересчёт ипотеки; нет продавца вторички, ЕГРН, наследников или опеки
klyshin_hook: optional | none | original: none | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: 21 locks (last_sync 2026-09-26); избегали live: планировка 54→49, акт −1.8 м², 12→8 соток, частичный ввод, паркинг отдельный ДДУ, сорванная переуступка, последний этаж, маткапитал СФР, детсад на рендере, 7 лет семейная ипотека, лесополоса КП, мебельный пакет
dzen_casus_shape: PASS | event: семья выбрала квартиру с «остеклённой лоджией» на стенде; в брони галочка «остекление включено» | risk: холодный балкон режет полезные метры и лимит ипотеки; остекление вне кредита +300 тыс | time: 6 дней до подписания ДДУ и эскроу | finale: в проекте ДДУ холодный балкон; банк снизил лимит; отказ от ДДУ, эскроу не открывали
comment_magnet_angle: «Если в брони лоджия “с остеклением”, а в ДДУ — холодный балкон: доплачиваете из своих или рвёте сделку?»
wordstat_rework: probe «остекление лоджии новостройка» 55,11176 → 2 → weak; probe «дду новостройка тюмень» 55,11176 → empty; probe «управляющая компания новостройка» 55,11176 → 3 → rejected; rework → P0 spine «новостройки тюмень» 4326 + mechanism в H1
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4326
story_dup_check: PASS | cluster_id: newbuild_glazed_loggia_promised_cold_balcony_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: glazed_loggia_vs_cold_balcony_six_days_before_ddu
formula_spam_check: PASS | last3_mechanisms: DDU planning sqm change; acceptance act sqm vs DDU; KP kadastr sotok — B33 mechanism loggia glazing spec vs DDU
anti_dupe_hard: PASS
```

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_51040/
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used
