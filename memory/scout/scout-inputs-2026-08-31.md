# Scout inputs — 2026-08-31 slot 3 (15:10 YEKT)

## Date context
- today: 2026-08-31, понедельник
- freshness: prefer sources after 2026-08-01
- tenant: The Риэлтор, Тюмень, dzen_rf_pack=true

## Anti-repeat preflight (DONE)
- live blog ~20 + ledger synced
- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- closed clusters: see memory/scout/used-clusters.json

## Director topic pick (pre-lock, PASS duplicate check)
- cluster_id: `double_sale_two_buyers_one_apartment` (NEW — not in used-clusters)
- title draft: «В Тюмени продали одну квартиру двум покупателям — второй аванс остановили»
- slug draft: v-tyumeni-prodali-odnu-kvartiru-dvum-pokupatelyam-vtoroj-avans-ostanovili
- scout_helper --check-query: PASS (no cannibalization)
- dzen_casus_shape elements:
  - event: продавец принял авансы от двух покупателей на одну квартиру
  - risk: двойная продажа / мошенничество / потеря аванса
  - time: «за день до регистрации» / «на сделке»
  - finale: второй покупатель остановил сделку, первый уже внес деньги — спор
- comment_magnet_angle: «Кто виноват — продавец или риэлтор, который не проверил?»

## Wordstat (MCP-KV live, regions 55+11176)
- wordstat_preflight: wordstat_get_user_info OK
- probe «двойная продажа квартиры» → weak/empty in Tyumen
- rework → probe «продали квартиру двум покупателям» → **135** shows (Tyumen+область)
- top: «продал квартиру двум покупателям» — 135
- final P0: «продал квартиру двум покупателям» — 135 (regions 55,11176)
- compare RU 225: same phrase family strong buyer intent

## Klyshin
- optional, not used this slot (fresh Tyumen casus without Klyshin — preferred)

## Signal URLs (tenant)
- https://t.me/klyshin_A (optional, skipped)
- https://dzen.ru/holyslav
- PUBLIC_SITE_URL/blog/
- https://t.me/holyslav92

## Forbidden / RF
- No Meta/Instagram/Facebook heroes
- No checklist/how-to as main hook

## Task
Write handoff to `.cursor/excalibur-blog-handoff.md` with all required fields:
wordstat_preflight, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework log, final P0, story_dup_check PASS, topic_id B19, title, slug, signal_urls, research angles.
