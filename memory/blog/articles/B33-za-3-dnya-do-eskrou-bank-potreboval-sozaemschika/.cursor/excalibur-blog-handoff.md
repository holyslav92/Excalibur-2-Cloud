# Scout handoff — B33

- **run_date:** 2026-09-28
- **slot:** Monday, ~12:00 YEKT
- **tenant:** The Риэлтор — Святослав Шакин, Тюмень
- **topic_market_focus:** `newbuild_only`
- **topic_id:** `B33`
- **article_dir:** `memory/blog/articles/B33-za-3-dnya-do-eskrou-bank-potreboval-sozaemshchika-semejnaya-ipoteka-novostrojka-tyumen`
- **slug:** `za-3-dnya-do-eskrou-bank-potreboval-sozaemshchika-semejnaya-ipoteka-novostrojka-tyumen`
- **title_draft:** За 3 дня до эскроу банк потребовал созаёмщика — в брони семейной ипотеки на новостройку Тюмени обещали одного
- **cluster_id:** `newbuild_family_mortgage_coborrower_before_escrow_tyumen`

## Mandatory focus

- **top_energy_mirror:** `clock_ran_out / paper_clean_then_broke`
- **newbuild_mechanism:** Семья с двумя детьми выбирает квартиру в новостройке Тюмени по семейной ипотеке. Менеджер отдела продаж и брокер фиксируют в брони: «одобрение на одного заёмщика, созаёмщик не нужен». За три дня до открытия эскроу банк присылает другие условия: без супруги в качестве созаёмщика кредит не выдадут, предварительное одобрение «заморожено». Семья останавливает сделку до подписания ДДУ и не открывает счёт.
- **why_newbuild_not_secondary:** Сюжет полностью связан с новостройкой: бронь в ЖК, семейная ипотека на строящееся жильё, эскроу и ДДУ с застройщиком. В истории нет продавца вторичного жилья, ЕГРН, наследников, опеки или иных вторичных механизмов.
- **audience:** семьи с детьми, покупающие квартиру в новостройке Тюмени; инвесторы и покупатели, оценивающие риски ипотечного одобрения до ДДУ.

## Dzen news-casus shape

- **dzen_casus_shape:** `PASS`
- **event:** Семья выбрала двушку в новостройке и получила предварительное одобрение семейной ипотеки на одного родителя.
- **risk:** Банк снимает или приостанавливает одобрение без созаёмщика; без подтверждённого кредита семья не может перейти к открытию эскроу по сделке, а бронь объекта оказывается под угрозой.
- **time:** За три дня до назначенного открытия эскроу-счёта.
- **finale:** Банк потребовал подключить супругу созаёмщиком с подтверждённым доходом. Менеджер отдела продаж предложил подписать ДДУ, а вопрос с банком решить позже. Семья отказалась подписывать документы и не открыла эскроу; сделку перенесли на другой корпус с пересчётом условий брони.
- **comment_magnet_angle:** «Если банк за три дня до эскроу требует созаёмщика, а в брони обещали одного, вы подписываете ДДУ или стопаете сделку?»

## Klyshin

- **klyshin_hook:** `none`
- **original:** none
- **signal:** none
- **reason:** Свежий внешний hook не используется; самостоятельный локальный казус по новостройке Тюмени предпочтительнее дублирования закрытых сюжетов.

## Wordstat

- **wordstat_preflight:** mcp-kv `wordstat_get_user_info` OK
- **wordstat:** `mcp_kv live`
- **regions:** Тюмень `55`, Тюменская область `11176`
- **comparison_region:** РФ `225`
- **P0:** «семейная ипотека тюмень»
- **P0 frequency:** `1309` в регионах 55 + 11176
- **buyer-demand context:**
  - «семейная ипотека тюмень» — `1309`
  - «семейная ипотека тюмень 2026» — `422`
  - «купить новостройку в тюмени» — `891`
  - «новостройки тюмень» — `4350` context
  - «созаёмщик семейная ипотека» — API weak, `<10`

### Wordstat rework

- **probe:** «созаёмщик семейная ипотека» — regions 55, 11176 — API weak, `<10`
- **rework:** Слабый узкий запрос не используется как основной P0. Demand spine перенесён на «семейная ипотека тюмень», а механизм с созаёмщиком сохранён в H1, лиде и теле материала.
- **final P0:** «семейная ипотека тюмень» — regions 55, 11176, compare 225 — `1309`

## Anti-repeat

- **anti_repeat_preflight:** live blog ~20 + ledger + used-clusters sync OK
- **sync status:** `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` — OK, 2026-09-28
- **closed-cluster check:** PASS
- **story_dup_check:** `PASS`
- **scout_helper_check:** `PASS`
- **topic_focus_check:** `PASS` — on-focus: ипотека
- **frozen secondary check:** PASS
- **slot exclusions:** PASS — тема не использует second bathroom, EISJHS construction stop, studio/commercial DDU, taunhaus/apartment block, installment price mismatch, UK payment before keys, lift oversight, rental ban, parking benefit, booking removal, balcony/loggia, discount or иные перечисленные live-кластеры.
- **distinct from:** B29 zero-down promotion, B31 insurance payment increase, B32 wrong escrow entity, family-mortgage-revoked-at-child-7, installment/rassrochka plots.

## Required hard gates

- **story_dup_check:** `PASS` — cluster `newbuild_family_mortgage_coborrower_before_escrow_tyumen`
- **h1_fingerprint_check:** `PASS` — fingerprint: `3-days-before-escrow + family-mortgage + coborrower-demand + Tyumen-newbuild`
- **formula_spam_check:** `PASS` — distinct mechanism: mortgage co-borrower requirement before escrow; not zero-down promotion, insurance repricing, wrong escrow entity, installment terms or booking cancellation.
- **anti_dupe_hard:** `PASS`
- **secondary_market_check:** `PASS` — no secondary-market plot or retitle.
- **newbuild_focus_check:** `PASS`
- **dzen_news_casus_check:** `PASS` — completed event, concrete risk, deadline, finale and comment magnet present.

## Editorial angle

The article should frame the conflict as a deadline failure between a preliminary mortgage promise and the bank’s final borrower requirements. The key question is not a general guide to co-borrowers, but whether a family should sign a DДУ when the bank changes the borrower configuration three days before escrow. The narrative must keep the object, booking, DДУ and escrow within the newbuild purchase chain and end with the family’s decision to stop rather than sign documents on an unresolved financing condition.

## Final handoff

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: clock_ran_out / paper_clean_then_broke
newbuild_mechanism: Семья с двумя детьми покупает квартиру в новостройке Тюмени по семейной ипотеке; за 3 дня до открытия эскроу банк требует супругу созаёмщиком, хотя в брони было указано одобрение на одного заёмщика.
why_newbuild_not_secondary: Только бронь в ЖК, семейная ипотека на строящееся жильё, эскроу и ДДУ с застройщиком; вторичный рынок, ЕГРН и продавец вторички отсутствуют.
klyshin_hook: optional | none | original: none | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: checked; proposed cluster is new
dzen_casus_shape: PASS | event: семья выбрала двушку и получила предварительное одобрение на одного родителя | risk: банк потребовал созаёмщика, бронь и сделка оказались под угрозой | time: за 3 дня до открытия эскроу | finale: семья отказалась подписывать ДДУ и не открыла эскроу; сделку перенесли на другой корпус с пересчётом брони
comment_magnet_angle: «Если банк за три дня до эскроу требует созаёмщика, а в брони обещали одного — вы подписываете ДДУ или стопаете сделку?»
wordstat_rework: probe «созаёмщик семейная ипотека» 55,11176 → API weak/<10 → anchor P0 «семейная ипотека тюмень» → final P0 «семейная ипотека тюмень» 1309
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «семейная ипотека тюмень» 1309
story_dup_check: PASS | cluster_id: newbuild_family_mortgage_coborrower_before_escrow_tyumen
h1_fingerprint_check: PASS | fingerprint: 3-days-before-escrow + family-mortgage + coborrower-demand + Tyumen-newbuild
formula_spam_check: PASS | last3_mechanisms: zero-down promotion; insurance payment increase; wrong escrow entity
anti_dupe_hard: PASS
```
