# Scout inputs — 2026-08-31 slot 12:00 YEKT

## Run context
- date: 2026-08-31 (понедельник)
- slot: 12:00 YEKT (automation cron 07:02 UTC)
- tenant: The Риэлтор / Тюмень / dzen_rf_pack=true
- needs_scout: true

## Anti-repeat preflight (DONE)
- live_blog_20 + ledger + `--sync-used-clusters` OK (2026-08-31)
- closed_clusters (30d): matkapital_missing_child_shares, registered_persons_block_sale_before_advance, communal_share_preemptive_right_neighbor_blocked, illegal_renovation_rosreestr_blocks_registration, marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction

## Recent live WP titles (avoid duplicate plots)
- В Тюмени не подтвердили согласие супруги — аванс остановили (2026-08-31)
- Квартиру с маткапиталом не купили: детских долей не было в ЕГРН
- Перед авансом в Тюмени нашли прописанных — сделку остановили
- В Тюмени сосед остановил покупку доли перед авансом
- Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени (B14)
- В Тюмени подписали предварительный — квартиру продали другим
- В Тюмени кладовка «в подарок» остановила сделку
- Аккредитив открыли, сделку зарегистрировали — продавец без денег
- В Тюмени приставы арестовали квартиру за два дня до регистрации
- Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд (опека)
- В Тюмени три года платили за квартиру — собственник продал её другим

## Proposed NEW cluster (not in closed list)
- cluster_id: `double_sale_two_buyers_same_apartment`
- legal plot: продавец взял аванс/задаток у двух покупателей на одну квартиру; второй аванс остановили накануне регистрации
- story_dup_check: PASS (scout_helper.py --check-query OK)

## Dzen news-casus shape
- event: продавец подписал предварительный с первым покупателем, затем принял аванс от второго
- risk: двойная продажа / мошенничество / спор о приоритете сделок
- time: «накануне регистрации» / «за два дня до сделки в Росреестре»
- finale: сделку остановили, второй покупатель не внёс деньги в сделку / первый покупатель узнал о конкуренте
- comment_magnet_angle: «У кого аванс сильнее — у кого договор раньше?»

## Wordstat (MCP-KV live, regions 55+11176)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework:
- probe «двойная продажа квартиры» → API empty/0 → rework
- probe «мошенничество при покупке квартиры» → 3 (слабо)
- probe «предварительный договор купли продажи квартиры» → 49 (слабо, angle уже на live)
- probe «проверка квартиры перед покупкой» → 2 (слабо)
- probe «купить квартиру в тюмени» → 22408 → localize news to вторичка
- final P0 «купить квартиру в тюмени вторичка» → **4146** (Tyumen 55+11176)

## Title draft (news headline)
**В Тюмени продавец взял аванс у двоих покупателей — сделку остановили накануне регистрации**

## topic_id
B19

## slug
v-tyumeni-prodavec-vzyal-avans-u-dvoih-pokupatelej-sdelku-ostanovili-nakanune-registracii

## klyshin_hook
none (fresh Tyumen casus without Klyshin — preferred)

## Task for Scout handoff
Write complete `.cursor/excalibur-blog-handoff.md` with all required fields per skill:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape: PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id, topic_id B19, title, slug, signal_urls (tenant), engagement goal Dzen.
