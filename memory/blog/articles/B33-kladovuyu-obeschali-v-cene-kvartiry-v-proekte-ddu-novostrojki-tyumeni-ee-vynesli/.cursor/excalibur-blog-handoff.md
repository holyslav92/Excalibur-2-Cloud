```markdown
# Scout handoff — B33

status: LOCKED  
run_date: 2026-09-22  
slot: 05:00 UTC / 10:00 YEKT  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
topic_market_focus: newbuild_only

## Locked topic

cluster_id: newbuild_storage_room_booking_vs_ddu_separate_contract_tyumen  
h1_fingerprint: storage_room_separate_contract_four_days_before_escrow

title_draft:  
> Кладовую обещали в цене квартиры — в проекте ДДУ новостройки Тюмени её вынесли отдельным договором за 4 дня до эскроу

slug_draft: `kladovaya-v-novostroyke-otdelnyy-dogovor-pered-eskrou-tyumen`

## Demand spine

wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework:  
- probe `купить кладовую в новостройке от застройщика` — 199, RU total; механизм подтверждён, но не используется как основной спросовый spine  
- probe `купить новостройку в тюмени` — 1890  
- final P0 `новостройки тюмень` — 8251

wordstat: mcp_kv live | regions 55, 11176, compare 225 | P0 `новостройки тюмень` 8251

rejected_alternate: `семейная ипотека + доля ребёнка` — overlap with LIVE-V-TYUMENI-REBENKU-ISPOLN: 43%

## Newbuild and Dzen casus

top_energy_mirror: paper_clean_then_broke

newbuild_mechanism:  
Семья выбирает квартиру в тюменском ЖК. В брони или КП менеджер фиксирует формулировку «кладовая в комплекте», однако за четыре дня до оформления эскроу семья получает проект ДДУ: кладовое помещение вынесено в отдельный договор, а за него требуется доплата. Решение принимают до подписания документов и перевода денег.

why_newbuild_not_secondary:  
Сюжет построен только на бронировании у застройщика, проекте ДДУ, отдельном договоре на кладовую и эскроу. Вторичная недвижимость, ЕГРН и сделка с частным продавцом не используются.

dzen_casus_shape: PASS  
event: «кладовую в брони или КП обещали включённой в цену квартиры»  
risk: «в проекте ДДУ кладовая оформлена отдельным договором и требует доплаты»  
time: «за 4 дня до эскроу»  
finale: «стоп до подписания: агентство сверяет проект ДДУ, номер и площадь кладовой ещё до брони»

comment_magnet_angle:  
«Кладовую в брони “в подарок” — вы сверяете номер и площадь в проекте ДДУ или верите менеджеру?»

klyshin_hook: optional | none

## Anti-repeat and gates

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK

closed_clusters_checked:  
- booking_expired_price_hike  
- ddu_apartment_vs_apartments_mismatch  
- mortgage_rate_hike_before_ddu  
- ddu_amount_vs_escrow_zero  
- newbuild_mortgage_insurance_requote_before_ddu_tyumen (B31)  
- escrow_wrong_legal_entity (B32)  
- assignment_resale_ban (B30)  
- LIVE kladovka paid at keys not delivered — different delivery/non-transfer cluster

story_dup_check: PASS | cluster_id: newbuild_storage_room_booking_vs_ddu_separate_contract_tyumen

h1_fingerprint_check: PASS | fingerprint: storage_room_separate_contract_four_days_before_escrow

formula_spam_check: PASS | last3_mechanisms:
- B30: assignment_resale_ban_3y in переуступке
- B31: mortgage_insurance_requote_before_ddu
- B32: escrow_account_wrong_legal_entity

scout_helper_check: PASS  
candidate_fingerprint: escrow_blocked  
candidate_mechanism: escrow_blocked  
cannibalization_risk: none  
topic_focus: PASS

topic_focus_gate: PASS  
anti_dupe_hard: PASS

## Source and compliance notes

live_blog_review: EXCALIBUR_RECENT_WP_POSTS + published-articles.md reviewed  
dzen_rf_pack: shared/dzen-content-rules.md + rf-blocked-entities.json reviewed; topic clean  
klyshin_source: none  
story_type: composite Tyumen newbuild casus; do not present the scenario as a documented claim about a named ЖК or developer without primary evidence in research

## Writer direction

Основной конфликт — не «как купить кладовую», а момент, когда обещание из брони не совпадает с проектом ДДУ до денег на эскроу. Материал должен держать семейную ставку: покупатели рассчитывали на место для коляски, шин, сезонных вещей или хранения в новой квартире, а отдельный договор меняет итоговый бюджет. Финал — действие до подписи, без вторичного рынка и без спокойного чеклистового формата.
```
