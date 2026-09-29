# Scout handoff — B34

topic_id: B34  
run_date: 2026-09-29  
slot: 12:00 Asia/Yekaterinburg  
slot_rubric: novostroyki  
tenant: The Риэлтор / Святослав Шакин, Тюмень

wordstat_preflight: mcp-kv `wordstat_get_user_info` OK

top_energy_mirror: `paper_clean_then_broke`

newbuild_mechanism: семья в Тюмени оформляет покупку квартиры в строящемся доме в ипотеку. В брони и ипотечном одобрении указана жилая площадь около 68 м². За 3 дня до открытия эскроу в приложении к ДДУ обнаруживается около 60 м² жилой площади — из-за пересчёта площади/лоджии. Цена не меняется, но банк пересчитывает лимит: не хватает ориентировочно 420–480 тыс. рублей. Семья останавливает сделку до подписания ДДУ и открытия эскроу.

why_newbuild_not_secondary: риск возникает в приложении к ДДУ на объект в строящемся доме и в связке с ипотечным лимитом на новостройку. Это не вторичная квартира, не выписка ЕГРН и не спор с продавцом готового жилья.

klyshin_hook: optional | none

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK  
closed_clusters: `egrn_line_blocks_advance`, `escrow_not_opened_after_mortgage`, `booking_expired_price_hike`, `bank_appraisal_below_ddu_price`, а также активные кластеры из `memory/scout/used-clusters.json`

dzen_casus_shape: PASS  
event: семья сверяет приложение к ДДУ перед подписанием и открытием эскроу  
risk: фактическая жилая площадь меньше заявленной в брони и ипотечном одобрении, банк снижает лимит  
time: 3 дня до открытия эскроу  
finale: семья останавливает сделку до перечисления денег; агентство не доводит покупателя до панической доплаты

comment_magnet_angle: «Если в ДДУ жилая площадь меньше, чем в брони, а цена та же — вы доплачиваете наличными или рвёте сделку?»

wordstat_rework: probe «жилая площадь дду новостройка» 0 → «площадь квартиры приемка новостройки» 27 → «площадь квартиры дду» 434 / «меньше чем в дду» 47 → final P0 «купить новостройку в тюмени» 1913

wordstat: mcp_kv live | regions 55, 11176, compare 225 | P0 «купить новостройку в тюмени» 1913 | buyer spine новостройки

title_draft: «За 3 дня до эскроу в Тюмени жилая площадь в приложении к ДДУ оказалась на 8 кв. м меньше — банк урезал ипотеку»

slug: `za-3-dnya-do-eskrou-zhilaya-ploshchad-v-ddu-menshe-bank-urezal-ipoteku-tyumen`

story_dup_check: PASS | cluster_id: `newbuild_living_area_ddu_vs_mortgage_shrink_tyumen`

h1_fingerprint_check: PASS | fingerprint: `3 дня до эскроу + жилая площадь в приложении к ДДУ меньше на 8 м² + банк урезал ипотеку`

formula_spam_check: PASS | last3_mechanisms: B30 — запрет переуступки; B31 — страховка и одобрение; B32 — чужое юрлицо в реквизитах эскроу

anti_dupe_hard: PASS

top_energy_to_plot: PASS — эмоциональная конструкция «документы выглядели нормально, но перед деньгами обнаружилось расхождение» перенесена только на покупку новостройки в Тюмени.

newbuild_focus: PASS — квартира в строящемся доме, приложение к ДДУ, ипотека, эскроу.

slot_rubric_check: PASS | `novostroyki`

scout_signal_urls:
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- trend radar: `memory/blog/trend-radar/trend-radar.json`

final_p0: «купить новостройку в тюмени» — 1913  
final_topic: «За 3 дня до эскроу в Тюмени жилая площадь в приложении к ДДУ оказалась на 8 кв. м меньше — банк урезал ипотеку»
