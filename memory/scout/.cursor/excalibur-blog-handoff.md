# Scout handoff — B33

**run_date:** 2026-09-26  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**topic_market_focus:** newbuild_only  
**dzen_rf_pack:** true  

## Topic lock

- **topic_id:** B33
- **title:** В Тюмени за 5 дней до ДДУ в новостройке поменяли планировку — в брони 54 квадрата, в проекте 49
- **slug:** `v-tyumeni-za-5-dnej-do-ddu-v-novostrojke-smenili-planirovku-bron-54-v-proekte-49`
- **article_dir:** `memory/blog/articles/B33-v-tyumeni-za-5-dnej-do-ddu-v-novostrojke-smenili-planirovku-bron-54-v-proekte-49`
- **cluster_id:** `newbuild_layout_area_mismatch_before_ddu_tyumen`

## Mandatory handoff fields

```text
wordstat_preflight: mcp-kv wordstat_get_top_requests OK 2026-09-26

top_energy_mirror: paper_clean_then_broke

newbuild_mechanism: Семья с ребёнком бронирует двухкомнатную в ЖК в Тюмени: в брони и на визуализации — 54,2 м², евродвушка с лоджией. За 5 дней до подписания ДДУ менеджер присылает новый лист планировки из проектной декларации: 49,1 м², другая конфигурация комнат, цена в ДДУ не снижается. Банк пересчитывает одобрение; семья останавливает сделку до эскроу.

why_newbuild_not_secondary: Только первичка: бронь застройщика, приложение к ДДУ, площадь из проектной декларации 214-ФЗ, ипотека на новостройку. Нет вторички, наследников, опеки.

klyshin_hook: none | original: none

anti_repeat_preflight: sync-used-clusters 2026-09-26; live WP excludes BTI area, KP sotok, parking DDU, assignment, matkapital SFR, kindergarten render, etc.

dzen_casus_shape: PASS | event: бронь 54 м² двушка в тюменском ЖК | risk: ипотека и ожидания семьи | time: за 5 дней до ДДУ и эскроу | finale: в ДДУ 49,1 м², банк сузил лимит, ДДУ не подписали, эскроу не открывали

comment_magnet_angle: Если в брони 54 м², а в ДДУ 49 — подписали бы ДДУ при обещании «пересчёт по БТИ» или сняли бронь?

wordstat_rework: «планировка квартира новостройка» 27 в 55+11176 слабо → P0 «новостройки тюмень» 4326

wordstat: mcp_kv live | regions 55,11176 | P0 «новостройки тюмень» — 4326

story_dup_check: PASS | cluster_id: newbuild_layout_area_mismatch_before_ddu_tyumen

h1_fingerprint_check: PASS

formula_spam_check: PASS

anti_dupe_hard: PASS
```

## signal_urls

- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_51040/
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
