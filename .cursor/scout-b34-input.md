Scout run B34 — 2026-09-29, слот 17:00 YEKT, рубрика **vtorichka** (НЕ новостройки). Собери handoff-прозу по SKILL + slot-rubric-lock. Все обязательные строки handoff.

## topic_id
B34

## slot_rubric
vtorichka (EXCALIBUR_SLOT_RUBRIC=vtorichka)

## Trend Radar (memory/blog/trend-radar/trend-radar.json, slot 17:00)
- top_energy: almost lost перед ключами/деньгами
- viral mechanism from vtorichka angles: casus+число, «7 смертных грехов покупателя» energy — mirror stakes, NOT copy plot
- policy: MECHANICS_AND_ENERGY_ONLY

## Title draft (news headline, Tyumen, вторичка — NOT ДДУ/эскроу/застройщик)
В Тюмени зарегистрированная аренда на три года остановила покупку вторички за неделю до аванса

## slug suggestion
za-nedelyu-do-avansa-v-tyumeni-arendator-pokazal-zaregistrirovannyj-dogovor-semya-ostanovila-vtorichku

## cluster_id (new, unique)
registered_lease_rosreestr_blocks_secondary_before_advance

## Plot (vtorichka casus — distinct from closed clusters)
- Семья выбрала вторичку в Тюмени, ипотека одобрена, аванс через неделю.
- На повторном осмотре арендатор предъявил договор аренды, зарегистрированный в Росреестре на 3 года; продавец говорил «съедет к ключам».
- Риск: зарегистрированная аренда / право пользования — покупатель не получает свободное владение; выселение не за один день.
- Финал: семья остановила сделку до аванса, потеряли время и часть расходов на проверки, но не внесли деньги.
- NOT: дарственная (сегодня WP), долг за свет B33, ЕГРН обременение B09, прописанные B17, newbuild/эскроу.

## Klyshin
optional | none — свежий casus без Klyshin (Trend Radar channel energy only)

## Wordstat (MCP-KV live, conductor verified 2026-09-29)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes regions 55+11176 (+ compare RU 225 where noted):
- «вторичка в тюмени» → 5501
- «купить квартиру в тюмени» → 20303
- «купить квартиру в тюмени вторичка» → 3413 (RU225 → 6415)
- «аренда квартиры при продаже» → 2 (weak — rework)
- «регистрация договора аренды в росреестре» → 37
- «обременение в егрн» → 56 (plot NOT egrn mortgage — do not use as story spine)

wordstat_rework:
- probe «аренда квартиры при продаже» 2 → buyer spine «купить квартиру в тюмени вторичка»
- final P0 demand spine for H1/SEO: «купить квартиру в тюмени вторичка» 3413

## dzen_casus_shape PASS
- event: покупка вторички в Тюмени, аванс назначен
- risk: зарегистрированный в Росреестре договор аренды на 3 года, арендатор на месте
- time: за неделю до аванса, на финальном осмотре
- finale: семья отказалась от сделки до передачи денег

## comment_magnet_angle
«Если арендатор живёт в квартире, а договор в Росреестре — вы ждёте «съедет к ключам» или сразу снимаете сделку с повестки?»

## anti_repeat_preflight
live_blog_20 + ledger + used-clusters sync OK (2026-09-29)
closed_clusters avoided: egrn_line_blocks_advance, registered_persons_block_sale_before_advance, дарственная live today, B33 utilities debt, all newbuild escrow clusters

## scout_helper + story_dup (pre-derouter)
PASS 2026-09-29 — NO CANNIBALIZATION, ANTI-DUPE HARD PASS, TOPIC FOCUS PASS (vtorichka)

## viral_mechanism / top_energy_mirror
almost_lost_before_money — деньги ещё не ушли, но объект «почти их» сорвал зарегистрированный арендатор

## slot rubric note
vtorichka ONLY — why NOT newbuild: слот 17:00 YEKT rubric lock; сюжет про вторичную сделку и аренду при продаже

## signal_urls
- https://dzen.ru/holyslav
- tenant scout_signal_urls from config

## Author / city
Святослав Шакин, Тюмень

## REQUIRED gate lines (exact field names — wordstat_gate.py)
klyshin_hook: optional | none | original: «нет — Tyumen casus без Klyshin»
wordstat_rework: probe «аренда квартиры при продаже» 2 → «регистрация договора аренды в росреестре» 37 → final P0 «купить квартиру в тюмени вторичка» 3413
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени вторичка» 3413
