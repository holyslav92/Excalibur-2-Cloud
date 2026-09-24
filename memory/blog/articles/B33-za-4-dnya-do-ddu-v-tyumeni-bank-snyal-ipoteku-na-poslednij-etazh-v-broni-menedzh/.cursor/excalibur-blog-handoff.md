# Scout handoff — B33

run_date: 2026-09-24  
slot: 17:00 Asia/Yekaterinburg  
topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
status: LOCKED  
topic_market_focus: newbuild_only

## Topic

**cluster_id:** `newbuild_last_floor_bank_mortgage_decline_tyumen`

**Title draft / H1 direction:**

> За 4 дня до ДДУ в Тюмени банк снял ипотеку на последний этаж — в брони менеджер писал «любой этаж»

**slug:** `za-4-dnya-do-ddu-bank-snyal-ipoteku-na-poslednij-etazh-menedzher-obeschal-lyuboj`

**article_dir:** `memory/blog/articles/B33-za-4-dnya-do-ddu-bank-snyal-ipoteku-na-poslednij-etazh-menedzher-obeschal-lyuboj`

**P0:** «новостройки тюмень» — **4294** (55+11176); RU compare **8168** (225)  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: квартира на последнем этаже новостройки Тюмени; в брони и у отдела продаж зафиксировано «ипотека на любой этаж, одобрение есть»; за 4 дня до подписания ДДУ банк аннулирует одобрение — внутренняя политика не кредитует последние этажи (или только с увеличенным взносом); застройщик предлагает этаж ниже с другой планировкой; семья останавливает сделку до эскроу; частичное удержание брони (composite casus, без имён ЖК/банка)
why_newbuild_not_secondary: бронь + ипотека под ДДУ + эскроу на строящийся объект; политика банка по этажности квартиры в новостройке — не сюжет вторички, ЕГРН продавца, наследников или опеки
klyshin_hook: none | original: none | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: matkapital_escrow_sfr; kindergarten_render_declaration; family_mortgage_child_7y; kp_forest_fence; furniture_partner_pack; co_borrower_escrow; showroom_ceiling_explication; building_rotation_magistral; declaration_delivery_shift; cellar_separate_ddu; down_payment_15_25; terrace_visualization (+ 26 locks in used-clusters.json)
dzen_casus_shape: PASS | event: семья выбрала последний этаж, ипотека предварительно одобрена | risk: банк снимает одобрение из‑за политики по последним этажам | time: за 4 дня до подписания ДДУ | finale: отказ от ДДУ до эскроу, частичная потеря брони, поиск объекта с письменным подтверждением этажности в банке
comment_magnet_angle: «Если банк режет последний этаж за несколько дней до ДДУ, вы бы согласились на этаж ниже, чтобы не потерять бронь, или разорвали бы бронь сразу?»
wordstat_rework: probe «ипотека последний этаж» 55,11176 → empty/<5 → probe «ипотека в тюмени на новостройки» 26 (weak) → final P0 «новостройки тюмень» 4294
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4294
story_dup_check: PASS | cluster_id: newbuild_last_floor_bank_mortgage_decline_tyumen
h1_fingerprint_check: PASS | fingerprint: 4_days:last_floor_bank_mortgage_revoked
formula_spam_check: PASS | last3_mechanisms: matkapital SFR escrow 7d; kindergarten render vs PD 5d; child 7y family mortgage on DDU day
anti_dupe_hard: PASS
```

## signal_urls

- {{SITE_BASE}}/blog/
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A (optional — hook not used)
