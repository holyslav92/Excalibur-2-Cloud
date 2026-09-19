# Scout assembled inputs — B27 — 2026-09-19 (YEKT ~10:00)

## Run context
- tenant: The Риэлтор / tymenrieltor.ru
- topic_id: B27
- topic_market_focus: newbuild_only
- slot: Saturday 2026-09-19 (~10:00 YEKT)

## Canon read
- shared/dzen-news-casus.md ✓
- shared/newbuild-focus-lock.md ✓
- shared/dzen-top-angle-newbuild-lock.md ✓
- shared/dzen-content-rules.md ✓
- shared/rf-blocked-entities.json ✓

## Anti-repeat preflight
- sync: python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters → 30 active locks
- live blog ~20 (WP MCP 2026-09-19): заголовки включая земля/аренда декларация, коттедж кадастр, БТИ площадь, переуступка 28 дней, ипотека 87 день, маткапитал доли, запрет аренды ДДУ, другой корпус, оценка ниже ДДУ, машино-место, страховка 186к, ключи 9 мес, созаёмщик, аккредитация ЖК, прайс +480к, газ на ключах КП, и др.
- ledger last published topic_id: B26
- closed clusters: memory/scout/used-clusters.json (30 entries)

## Picked topic (LOCK)

**title_draft:** В Тюмени ребёнку исполнилось 7 лет за 5 дней до ДДУ — семейную ипотеку сняли

**slug_suggestion:** v-tyumeni-rebenku-7-let-semejnuyu-ipoteku-snyali-pered-ddu

**cluster_id:** family_mortgage_child_age_limit_before_ddu

**top_energy_mirror:** clock_ran_out

**newbuild_mechanism:** Семейная ипотека на квартиру в ЖК по ДДУ: банк одобрил льготу при ребёнке до 7 лет. За 5 дней до подписания ДДУ и открытия эскроу ребёнку исполнилось 7 лет — банк пересчитал заявку и снял семейную ставку; платёж вырос, до внесения на эскроу семья не дошла.

**why_newbuild_not_secondary:** Покупка квартиры от застройщика в новостройке: бронь, проект ДДУ, эскроу-счёт, аккредитация ЖК. Не вторичка, не ЕГРН-продавец.

**klyshin_hook:** none

**dzen_casus_shape:** PASS
- event: семья в Тюмени выбрала лот в ЖК, получила одобрение семейной ипотеки, назначила подписание ДДУ
- risk: условие программы — ребёнок младше 7 лет на дату сделки; льгота сгорает
- time: «за 5 дней до ДДУ», в день рождения ребёнка
- finale: банк снял семейную ипотеку / поднял ставку, сделку остановили до эскроу

**comment_magnet_angle:** «Ребёнку исполнилось 7 лет в пятницу, ДДУ в среду — кто должен был предупредить семью: банк, застройщик или риелтор?»

## Wordstat (MCP-KV live — НЕ выдумывать)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework:
- probe «семейная ипотека новостройка тюмень» → 35 (слабо)
- probe «семейная ипотека тюмень» → 1716 (лучше)
- probe «купить новостройку в тюмени» → 1936 (сильный newbuild spine)
- final P0 «семейная ипотека в тюмени» → 1060 (buyer-intent семьи + локализация Тюмень)

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «семейная ипотека в тюмени» 1060

## Gate checks (already run)

scout_helper --check-query → PASS (exit 0)
scout_story_dup --text → PASS
topic_focus → PASS
cluster_id family_mortgage_child_age_limit_before_ddu — NOT in used-clusters 30d

story_dup_check: PASS | cluster_id: family_mortgage_child_age_limit_before_ddu
h1_fingerprint_check: PASS | fingerprint: ddu_vs_escrow_amount (mechanism distinct from 87-day approval / co-borrower refusal)
formula_spam_check: PASS | last3_mechanisms: commissioning_permit_tranche (B26), finish_acceptance (B25), apartment_vs_apartments (B23)
anti_dupe_hard: PASS

## signal_urls (scout)
- PUBLIC_SITE_URL/blog/
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

## Instruction
Write Scout handoff prose for research_start: topic B27, title, slug, cluster, all mandatory handoff fields, news-casus angle for Writer, no checklist shape, Russian.
