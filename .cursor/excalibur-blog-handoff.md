# Scout handoff — B19

date: 2026-08-31
slot: 12:00 YEKT
tenant: The Риэлтор / Тюмень
dzen_rf_pack: true
engagement_goal: Dzen — комментарии, лайки и подписки через локальный news-casus с финалом и спорным правовым углом

wordstat_preflight: mcp-kv wordstat_get_user_info OK

klyshin_hook: optional | original: none (fresh Tyumen casus without Klyshin — preferred)

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
closed_clusters: matkapital_missing_child_shares, registered_persons_block_sale_before_advance, communal_share_preemptive_right_neighbor_blocked, illegal_renovation_rosreestr_blocks_registration, marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction

dzen_casus_shape: PASS
event: «Продавец подписал предварительный договор с первым покупателем, затем принял аванс у второго»
risk: «Двойная продажа, мошенничество и спор о приоритете сделок»
time: «Накануне регистрации — за два дня до сделки в Росреестре»
finale: «Сделку остановили; второй покупатель не внёс деньги в регистрацию, а первый узнал о появлении конкурента»

comment_magnet_angle: «У кого аванс сильнее — у того, кто раньше подписал договор, или у того, кто первым успел передать деньги?»

wordstat_rework: probe «двойная продажа квартиры» 0 → «мошенничество при покупке квартиры» 3 → «предварительный договор купли продажи квартиры» 49 → «купить квартиру в тюмени» 22408 → final P0 «купить квартиру в тюмени вторичка» 4146

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени вторичка» 4146

story_dup_check: PASS
cluster_id: double_sale_two_buyers_same_apartment
legal_plot: «Продавец взял аванс/задаток у двух покупателей на одну квартиру; второй аванс остановили накануне регистрации»
topic_id: B19

title: «В Тюмени продавец взял аванс у двоих покупателей — сделку остановили накануне регистрации»

slug: v-tyumeni-prodavec-vzyal-avans-u-dvoih-pokupatelej-sdelku-ostanovili-nakanune-registracii

signal_urls:
- {{SITE_BASE}}/blog/
- https://dzen.ru/holyslav
- https://t.me/holyslav92
