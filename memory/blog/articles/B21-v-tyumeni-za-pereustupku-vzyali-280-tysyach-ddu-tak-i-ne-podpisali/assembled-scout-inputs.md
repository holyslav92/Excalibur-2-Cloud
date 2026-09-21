# Scout inputs — B21 — 2026-09-01

**MANDATORY:** Derouter utility tier. Output handoff markdown per SKILL.md. Do NOT refuse.

## Preflight
- wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-01)
- setup_complete: true
- live_blog_checked: WP last 15 posts — avoid 9411 (траншевая 8×), 9439 (мокрая стяжка), 9452 (ипотека+эскроу+маткапитал), 9465 (бронь +380k), 9490/B20 (смена юрлица)
- anti_repeat: sync used-clusters OK

## Topic lock
- **topic_id:** B21
- **cluster_id:** `newbuild_assignment_deposit_scam_tyumen`
- **title_draft:** В Тюмени за переуступку взяли 280 тысяч — ДДУ так и не подписали
- **slug:** v-tyumeni-za-pereustupku-vzyali-280-tysyach-ddu-tak-i-ne-podpisali

## klyshin_hook
- optional | energy only: casus+number+punch (280 тысяч, ДДУ не подписали)
- signal: none (original Tyumen newbuild casus, not copying Klyshin plots)

## dzen_casus_shape: PASS
- **event:** пара в Тюмени нашла квартиру в новостройке по переуступке дешевле застройщика на ~400 тыс.; уступающий попросил 280 тыс. «на подготовку цессии» до Росреестра
- **risk:** деньги перевели по СБП на обещание подписать договор цессии за 14 дней; через 3 недели уступающий пропал; в офисе застройщика — квартира всё ещё на первом дольщике, цессия не зарегистрирована
- **time:** август 2026, 21 день после перевода
- **finale:** ДДУ на их имя так и не появился; 280 тыс. под угрозой; пара остановилась до ипотеки и эскроу

## comment_magnet_angle
«Переуступка в новостройке: вы бы перевели 280 тысяч до регистрации цессии в Росреестре, если скидка к застройщику — 400?»

## wordstat_rework
- probe «переуступка новостройка» → 10 (55+11176) — weak
- probe «переуступка новостройки» → 10
- rework: localize Tyumen + buyer jargon
- probe «купить новостройку в тюмени» → **1882** (55+11176)
- probe «новостройки тюмень» → **8771** (55+11176), RU compare **~100k+**
- probe «приемка квартиры в новостройке тюмень» → 30 (context, not plot)
- final P0 «купить новостройку в тюмени» — **1882**

## wordstat
mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 1882 | support «новостройки в тюмени от застройщика» 1268 | niche «переуступка новостройки» 10

## story_dup_check: PASS
- cluster_id: newbuild_assignment_deposit_scam_tyumen
- distinct from B20 (юрлицо/эскроу), B19 (семейная ипотека), 9465 (бронь+цена у застройщика), B12 (перенос сдачи), 9439 (приёмка/стяжка), 9411 (траншевая)

## signal_urls
- https://dzen.ru/a/alm_Hspc2E9VNA0Z (Святослав — переуступка Тюмень, контекст)
- https://www.consultant.ru/document/cons_doc_LAW_51038/ (214-ФЗ ст.11)
- https://t.me/holyslav92
- https://dzen.ru/holyslav

## Output
Write `.cursor/excalibur-blog-handoff.md` with full Scout handoff per SKILL checklist.
