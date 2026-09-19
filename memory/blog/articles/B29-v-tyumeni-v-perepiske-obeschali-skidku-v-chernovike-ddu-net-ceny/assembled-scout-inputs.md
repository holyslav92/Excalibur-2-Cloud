# Scout assembled inputs — B29 (slot ~15:00 YEKT, 2026-09-19)

tenant: The Риэлтор / Святослав Шакин, Тюмень
topic_id: B29
topic_market_focus: newbuild_only
slot: 2026-09-19 ~15:00 YEKT (weekday slot 3 of 4)

## Anti-repeat preflight (done)
- sync-used-clusters: OK (30 locks)
- live EXCALIBUR_RECENT_WP_POSTS 2026-09-19: B27 земля аренда ЖК; B28 газ КП; потолки КП −25 см; семейная ипотека 7 лет ребёнку; avoid retelling
- closed newbuild clusters include: booking_expired_price_hike, trade_in, installment, assignment (live 28d), declaration-heavy KP plots today

## Pick (LOCK for handoff)
- cluster_id: newbuild_crm_promo_discount_not_in_ddu_draft
- working_title: В Тюмени в переписке обещали скидку 4% — в черновике ДДУ полной цены не было
- slug_suggestion: v-tyumeni-v-perepiske-obeschali-skidku-v-chernovike-ddu-net-ceny
- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: акция/скидка в CRM и переписке с менеджером не попала в проект ДДУ; семья остановилась за 3 дня до открытия эскроу
- why_newbuild_not_secondary: покупка квартиры в строящемся ЖК по ДДУ 214-ФЗ, эскроу и ипотека — не сделка с продавцом вторички
- klyshin_hook: none
- dzen_casus_shape: event — получили черновик ДДУ без скидки; risk — переплата ~580–620 тыс и потеря брони; time — «за 3 дня до эскроу»; finale — сделку остановили, эскроу не открывали
- comment_magnet_angle: «Скрин переписки со скидкой — это обещание застройщика или просто реклама?»
- signal_urls: PUBLIC_SITE_URL/blog/ (anti-dup titles only); no Klyshin

## Wordstat (MCP-KV live — do not invent)
wordstat_preflight: wordstat_get_user_info OK (Yandex Cloud API)
probes:
- «скидка застройщик новостройка» regions 55+11176 → 3 (weak)
- «новостройки тюмень» → 3502 (55), 4430 (11176), 8321 (225 compare)
- «купить новостройку в тюмени» → 920 (55+11176), 1917 (225 compare)
wordstat_rework: weak promo phrase → anchor buyer P0 «купить новостройку в тюмени»
final P0: «купить новостройку в тюмени» 920 (regions 55+11176); compare RU 225: 1917

## Gates already run (Cursor)
- scout_helper --check-query: ANTI-DUPE HARD PASS, TOPIC FOCUS PASS
- scout_story_dup --text: PASS fingerprint + formula
- topic_focus: PASS

## Output
Produce full `.cursor/excalibur-blog-handoff.md` per SKILL with all mandatory handoff fields including anti_dupe_hard: PASS.
