# Scout assembled inputs — B25 slot ~12:00 YEKT 2026-09-07

## Tenant
- brand: The Риэлтор / Святослав Шакин
- topic_market_focus: newbuild_only
- slot: 12:00 Asia/Yekaterinburg (weekday)
- topic_id candidate: B25

## Live blog ~20 (anti-repeat preflight)
1. В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й (2026-09-07)
2. В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание
3. В Тюмени в ДДУ обещали 12 соток — кадастр показал 8
4. В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили
5. В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ
6. Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил
7. В Тюмени ДДУ на 45 м² остановили: декларация показала 41
8. На приёмке в Тюмени нашли брак — застройщик потребовал 190 тысяч
9. В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты
10. В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку
11. В Тюмени инвестор не подписал ДДУ: аренду запретили до ключей
12. В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела
13. В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела (B22)
14. В Тюмени застройщик сменил юрлицо — банк не открыл эскроу (B20)
15. В Тюмени оплатили кладовку по ДДУ — на ключах её не оказалось (B21)

## Closed clusters (30d) — DO NOT reuse
ddu_amount_vs_escrow_zero, ddu_apartment_vs_apartments_mismatch, booking_expired_price_hike, assignment_lost_to_faster_buyer, trade_in_rejected_developer, bank_appraisal_below_ddu_price, mortgage_rate_hike_before_ddu, acceptance_defects_penalty, newbuild_ddu_cellar_paid_not_handed_tyumen, newbuild_developer_legal_entity_change_ddu_escrow_tyumen, keys_delay_penalty_unpaid, escrow_not_opened_after_mortgage, installment_penalty_developer, storage_room_missing_on_keys + frozen secondary clusters

## Scout pick (pre-validated gates)
- title_draft: В Тюмени в ДДУ по коттеджу обещали газ к забору — при сдаче дома магистраль оказалась в 180 метрах
- slug: v-tyumeni-v-ddu-po-kottedzhu-obeschali-gaz-k-zaboru-pri-sdache-magistral-v-180-metrah
- cluster_id: kp_gas_boundary_mismatch_on_keys_tyumen
- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: дом в коттеджном посёлке / ИЖС от застройщика — в ДДУ и проектной декларации газ «к границе участка», при сдаче магистраль в 180 м от забора, подключение 600+ тыс., семья остановила акт / не подписала приёмку
- why_newbuild_not_secondary: сюжет = ДДУ с застройщиком КП/дом, коммуникации по проектной декларации, не вторичный дом с сюрпризами в ЕГРН
- klyshin_hook: none (свежий hot Tyumen casus без Klyshin)
- dzen_casus_shape: event=сдача дома в КП под Тюменью; risk=газ не у границы участка, доплата на подключение; time=«за две недели до подписания акта»; finale=акт не подписали, застройщик предложил доплату 620 тыс. или рассрочку на коммуникации
- comment_magnet_angle: «Газ в двухстах метрах — это вообще выполнение ДДУ или уже отдельная услуга?»
- anti_dupe_hard: PASS (scout_helper + story_dup pre-checked)

## Wordstat live MCP-KV (regions 55, 11176, compare 225)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat_rework:
- probe «коттеджные поселки тюмень купить» 172 (55+11176)
- probe «купить дом в тюмени от застройщика» 155 (55+11176)
- probe «купить новостройку в тюмени» 650 (55) — broader newbuild spine
- final P0 «купить дом в тюмени от застройщика» 155 (on-topic for КП/дом casus)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить дом в тюмени от застройщика» 155

## Gate pre-checks (already PASS)
- scout_helper --check-query: PASS
- story_dup: PASS
- topic_focus: PASS

Write full handoff per SKILL.md format with signal_urls, article_dir, topic_id B25.
