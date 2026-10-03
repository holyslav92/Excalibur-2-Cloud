# Scout handoff — B34

topic_id: B34  
run_date: 2026-10-03  
slot: 09:00 Asia/Yekaterinburg  
slot_rubric: novostroyki  
tenant: The Риэлтор — Святослав Шакин  
topic_market_focus: newbuild_focus_lock  
article_dir: memory/blog/articles/B34-v-tyumeni-v-novostrojke-na-priemke-bti-4-kv-m-doplata-380-tysyach-do-klyuchej  
slug: v-tyumeni-v-novostrojke-na-priemke-bti-4-kv-m-doplata-380-tysyach-do-klyuchej  
title_draft: В Тюмени на приёмке БТИ добавила 4 кв.м — застройщик потребовал доплату 380 тысяч, семья отложила ключи  
cluster_id: newbuild_bti_area_surcharge_before_keys_tyumen  
wp_category_slugs: proverka-pered-pokupkoj, novostroyki  

wordstat_preflight: mcp-kv wordstat_get_user_info OK  
top_energy_mirror: paper_clean_then_broke  
newbuild_mechanism: Семья с двумя детьми покупает трёшку в новостройке Тюмени по ДДУ: в договоре и брони указано 78,2 кв.м, а на приёмке замер БТИ показывает 82,0 кв.м. Застройщик требует доплату 380 000 ₽ по цене квадратного метра из ДДУ и не передаёт ключи без оплаты либо подписания акта с новой площадью. Банк предупреждает о зависшем ипотечном графике, пока акт не подписан, а сроковые риски по ключам продолжают тикать.  
why_newbuild_not_secondary: Объект куплен по ДДУ в строящемся/сданном ЖК Тюмени; событие происходит на приёмке у застройщика, с замером БТИ и актом ввода. Это не вторичный ДКП, не спор с продавцом по ЕГРН и не вторичная перепродажа.  
klyshin_hook: optional | original: none  
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; closed_clusters: booking_expired, acceptance_defects_penalty, cellar_paid B21/Oct2 190k, escrow rent listing Oct1, school declaration, deposit 35/89 mismatch, bank appraisal, keys delay penalty и другие 13 активных locks  
dzen_casus_shape: PASS | event: семья приехала на приёмку с ипотекой и детьми, ожидая ключи | risk: доплата 380 000 ₽ и двойной дедлайн банка/неустойки застройщика | time: день приёмки, до подписания акта | finale: семья не подписала акт в тот день, зафиксировала расхождение площади и отложила ключи для повторной сверки с проектной документацией и ДДУ  
comment_magnet_angle: Если на приёмке площадь выросла на 4 кв.м и застройщик просит доплату 380 тысяч — вы подписываете акт в тот же день или останавливаете сделку до сверки с ДДУ?  
wordstat_rework: probe «бти новостройка» 1 и «дду новостройка» 17 → probe «приемка квартиры в новостройке тюмень» 10 → demand spine «новостройки тюмень» 4394; final P0 «новостройки тюмень» 4394  
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4394 | compare «купить новостройку в тюмени»: 908 local / 1900 RU  
story_dup_check: PASS | cluster_id: newbuild_bti_area_surcharge_before_keys_tyumen  
h1_fingerprint_check: PASS | fingerprint: приёмка + БТИ +4 кв.м + доплата 380  
formula_spam_check: PASS | last3_mechanisms: paid cellar option 190k; presentation deposit 35 vs DDU 89; school year declaration vs ad  
anti_dupe_hard: PASS  
dzen_rf_pack: true  
signal_urls: https://dzen.ru/holyslav; https://t.me/Tyumen_Rieltor; https://dzen.ru/a/YA7B343-ezstBMCs  

## Editorial angle

The emotional engine is “paper looked clean, then the number changed at the threshold.” The family has already secured ипотека and эскроу, arrives expecting keys, and faces a 380,000 ₽ demand before the act can be signed. The article should preserve the completed casus and its unresolved-but-active decision point: pause, document the discrepancy, and verify the DДУ/project documentation before accepting the revised area.

The central conflict for comments is speed versus verification: sign and pay to avoid schedule and financing complications, or stop at the act and challenge the discrepancy before taking the keys. The plot remains strictly about a Tyumen newbuild purchase and must not drift into secondary-market analogies or a calm checklist format.
