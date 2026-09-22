# Scout inputs — 2026-09-22 slot 05:00 UTC / 10:00 YEKT

run_date: 2026-09-22
topic_id: B33
tenant: The Риэлтор / Святослав Шакин, Тюмень, topic_market_focus: newbuild_only

## Preflight
- python3 scripts/excalibur_blog_doctor.py — OK
- python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters — OK (last_sync updated)
- wordstat_get_user_info — OK (MCP-KV 2026-09-22)
- dzen_rf_pack: shared/dzen-content-rules.md + rf-blocked-entities.json reviewed — topic clean
- live blog ~20 titles from EXCALIBUR_RECENT_WP_POSTS + published-articles.md

## Wordstat MCP-KV (regions: Тюмень 55, область 11176, compare RU 225)
| phrase | volume | note |
|--------|--------|------|
| новостройки тюмень | 8251 | P0 spine (region 55 in API response) |
| купить кладовую в новостройке от застройщика | 199 | mechanism probe (RU total, localized casus) |
| купить новостройку в тюмени | 1890 | secondary spine |

Rejected alternate: семейная ипотека + доля ребёнка — overlap LIVE-V-TYUMENI-REBENKU-ISPOLN 43%

## scout_helper formal check (2026-09-22)
Command:
python3 scripts/excalibur_blog_scout_helper.py --check-query "Кладовую обещали в цене квартиры в новостройке — в проекте ДДU Тюмени её вынесли отдельным договором за 4 дня до эскроu застройщик эскроu"

Output:
- candidate_fingerprint=escrow_blocked
- candidate_mechanism=escrow_blocked
- NO CANNIBALIZATION RISK
- ANTI-DUPE HARD PASS
- TOPIC FOCUS PASS
- exit 0

python3 scripts/excalibur_blog_topic_focus.py — PASS

## closed_clusters (excerpt — do NOT reuse until locked_until)
booking_expired_price_hike, ddu_apartment_vs_apartments_mismatch, mortgage_rate_hike_before_ddu, ddu_amount_vs_escrow_zero, newbuild_mortgage_insurance_requote_before_ddu_tyumen (B31), escrow_wrong_legal_entity (B32), assignment_resale_ban (B30), LIVE kladovka paid at keys not delivered (different cluster: delivery not separate contract)

## formula_spam last3 published mechanisms
- B30: assignment_resale_ban_3y in переуступке
- B31: mortgage_insurance_requote_before_ddu
- B32: escrow_account_wrong_legal_entity

## Proposed LOCK
cluster_id: newbuild_storage_room_booking_vs_ddu_separate_contract_tyumen
h1_fingerprint: storage_room_separate_contract_four_days_before_escrow
Title draft / H1:
> Кладовую обещали в цене квартиры — в проекте ДДU новостройки Тюмени её вынесли отдельным договором за 4 дня до эскроu

top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: семья берёт квартиру в ЖК Тюмени; в брони/КП менеджер фиксирует «кладовая в комплекте»; за 4 дня до эскроu проект ДДU — кладовое помещение отдельным договором и доплата; стоп до подписания (composite casus)
why_newbuild_not_secondary: только ДДU/эскроu/застройщик, не вторичка и не ЕГРН-сделка
klyshin_hook: none
dzen_casus_shape: PASS | event: обещание в брони | risk: отдельный договор на кладовую | time: 4 дня до эскроu | finale: agency — сверка проекта ДДU до брони
comment_magnet_angle: «Кладовую в брони “в подарок” — вы сверяете номер и площадь в проекте ДДU или верите менеджеру?»
anti_dupe_hard: PASS
story_dup_check: PASS

Produce final scout handoff markdown file per SKILL format with status: LOCKED and all required fields.
