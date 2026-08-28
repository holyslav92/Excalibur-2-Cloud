# Scout handoff — B12

topic_id: B12  
status: LOCKED for Research  
title_draft: В Тюмени раскрыли эскроу — ключи так и не передали  
slug: v-tyumeni-raskryli-eskrou-klyuchi-tak-i-ne-peredali  
cluster_id: escrow_unlocked_keys_not_delivered_ddu  

wordstat_preflight: mcp-kv wordstat_get_user_info OK

klyshin_hook: none | свежий тюменский casus без Klyshin; Klyshin не использовался, чтобы не дублировать закрытые сюжетные линии

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: illegal_renovation_rosreestr_blocks_registration, marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction

dzen_casus_shape: PASS | event: «Семья купила квартиру в тюменской новостройке по ДДУ с эскроу-счётом. После разрешения на ввод банк раскрыл эскроу и перевёл деньги застройщику, но ключи покупательнице вовремя не передали» | risk: «Эскроу защищает деньги до ввода дома, но не удерживает их до фактической передачи квартиры. При просрочке ключей покупатель уже платит за аренду, а деньги у застройщика» | time: «По делу Калининского районного суда Тюмени ключи должны были передать до 31.12.2023, фактически передали 18.03.2024 — почти через три месяца. В августе 2026 года угол снова практический: с 01.01.2026 снят мораторий на взыскание неустойки с застройщиков» | finale: «Суд частично удовлетворил требования: взыскал расходы на аренду, компенсацию морального вреда и судебные расходы — суммарно около 109 тысяч рублей. Покупательница получила ключи, но период ожидания оплачивала съёмным жильём»

comment_magnet_angle: «Эскроу защищает деньги только до разрешения на ввод — вы бы подписали ДДУ, если в нём не понимаете, когда именно получите ключи?»

wordstat_rework: probe «неустойка с застройщика» 50 (регионы 55+11176) → локальный спрос узкий, но юридический конфликт снова актуален после снятия моратория с 01.01.2026 → probe «дду тюмень» 37 → слабый объём → probe «эскроу счет» 811 → сильная механика риска и понятный buyer-жаргон → final P0 «новостройки тюмень» 4717

wordstat: mcp_kv live | regions 55,11176, compare 225 | P0 «новостройки тюмень» 4717 | secondary spine «эскроу счет» 811 | contextual legal demand: «неустойка с застройщика» 50 в регионах 55+11176, 3645 по РФ 225; «неустойка с застройщика в 2026» 502 по РФ 225

story_dup_check: PASS | cluster_id: escrow_unlocked_keys_not_delivered_ddu | новый legal plot: новостройка, ДДУ, раскрытый эскроу и просроченная передача ключей; не повторяет сюжеты о вторичке, ЕГРН, наследстве, доверенности, двойной продаже или незаконной перепланировке

topic: В тюменской новостройке деньги с эскроу уже ушли застройщику после ввода дома, а покупательница ещё почти три месяца ждала ключи и снимала жильё. Суд взыскал с застройщика часть расходов. Материал строится не как инструкция по эскроу, а как законченный местный casus: что именно перестаёт защищать эскроу после разрешения на ввод и почему дата передачи квартиры в ДДУ остаётся критичной.

research_focus:
- Подтвердить реквизиты и обстоятельства дела Калининского районного суда Тюмени по ООО «Клевер Строй».
- Проверить точные даты по ДДУ, дату фактической передачи ключей и разбивку взысканных сумм.
- Отдельно подтвердить правовой режим неустойки после 01.01.2026 и не смешивать его с обстоятельствами дела 2024 года.
- Объяснить разницу между разрешением на ввод, раскрытием эскроу и подписанием акта передачи квартиры.
- Не превращать текст в общий чеклист по покупке новостройки: в центре должна остаться история покупательницы и судебный финал.

signal_urls:
- https://tumentoday.ru/2025/02/03/v_tyumeni_sud_vzyskal_s_zastroyshchika_100_tysyach_rubley_za_zaderzhku_sdachi_doma/
- https://harant.ru/blog/nedvizhimost/eskrou-schyot-raskryt-a-kvartiry-net-pravovaya-kolliziya-o-kotoroj-molchat/
- https://nedvizhimosticeny.ru/moratoreeyi-otmyenyen-dolsheekam-vyernut-dyengee/
- https://dzen.ru/a/aoMNZq3UpQP2T6uq
- https://dzen.ru/holyslav
- https://t.me/holyslav92
- {{SITE_BASE}}/blog/
