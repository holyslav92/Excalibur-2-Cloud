# Scout inputs — B33 run 2026-09-25 slot ~15:09 YEKT

## Director preflight
- doctor: OK
- today: needs_scout → B33
- dzen_rf_pack: read shared/dzen-content-rules.md + rf-blocked-entities — no RF-blocked heroes

## Live blog / anti-dupe (sync used-clusters done)
Recent WP slugs to NOT reuse (ledger drift): partial vвод, parking DDU, pereustupka cancelled, last floor, matkapital escrou, detsad render, family mortgage age 7, KP forest fence, furniture pack, co-borrower escrow, ceiling height, windows yard.

## Candidate LOCK
**cluster_id:** `newbuild_kp_land_area_mismatch_cadastre_before_ddu_tyumen`

**Title draft:**
Под Тюменью в брони обещали 12 соток — в кадастре оказалось 8 до подписания ДДУ

**Casus (composite, Tyumen newbuild house/KP):**
Семья выбирает дом от застройщика под Тюменью (КП/ИЖС). В брони и презентации — участок 12 соток. За несколько дней до ДДУ менеджер присылает выписку ЕГРН/межевой план: в кадастре 8 соток. Разница бьёт по ипотеке (залоговая стоимость), по коммуникациям и по цене. Семья останавливает подписание до сверки границ и приложений к ДДУ.

**scout_helper --check-query:** ANTI-DUPE HARD PASS, TOPIC FOCUS PASS
**candidate_mechanism:** ddu_vs_escrow_amount (land cadastre mismatch — distinct from escrow amount cluster)

## Wordstat MCP-KV live
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes:
- «новостройки тюмень купить» total 1157 → P0 «купить новостройку в тюмени» **892** (55+11176)
- «дом от застройщика тюмень» total 344 → mechanism «дома с участком от застройщика тюмень» **24**; spine «купить дом в тюмени от застройщика» **118**

wordstat_rework: probe «участок коттеджный поселок тюмень» weak → rework to «дом от застройщика тюмень» + «дома с участком от застройщика тюмень» + spine «купить новостройку в тюмени» for demand bridge (квартиры+дома канон)

final P0: «купить новостройку в тюмени» 892 | mechanism «купить дом в тюмени от застройщика» 118 | local «дома с участком от застройщика тюмень» 24

## Locks
top_energy_mirror: paper_clean_then_broke (в брони «12 соток», в кадастре меньше)
newbuild_mechanism: КП/дом от застройщика — площадь земельного участка в ДДУ vs кадастр до подписания
why_newbuild_not_secondary: только договор с застройщиком на дом+землю, не покупка готового участка на вторичке
klyshin_hook: none
comment_magnet_angle: «Если в брони 12 соток, а в выписке 8 — вы требуете пересчёт цены или всё равно подписываете ДДУ?»
dzen_casus_shape: PASS
anti_dupe_hard: PASS
formula_spam_check: last3 live ≠ land-area (partial vвод / parking DDU / pereustupka) — PASS

topic_id: B33
slug hint: kp-uchastok-12-sotok-v-kadastre-8-do-ddu
