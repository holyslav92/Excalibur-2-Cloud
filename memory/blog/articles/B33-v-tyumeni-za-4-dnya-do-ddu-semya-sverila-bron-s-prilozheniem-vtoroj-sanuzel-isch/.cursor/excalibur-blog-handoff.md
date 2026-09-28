# Scout handoff — B33 / 12:00 YEKT / 2026-09-28

topic_id: B33  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
slot: 12:00 Asia/Yekaterinburg  
topic_status: LOCKED  
newbuild_only: PASS  
dzen_rf_pack: pre-read required before Writer

## Topic lock

cluster_id: `ddu_second_bathroom_missing_bron_tyumen`

title_draft: «В Тюмени за 4 дня до ДДУ семья сверила бронь с приложением — второй санузел исчез из договора, регистрацию остановили»

slug: `za-4-dnya-do-ddu-vtoroj-sanuzel-ischez-iz-prilozheniya-semya-ostanovila`

P0: «квартиры в тюмени новостройки»

top_energy_mirror: `paper_clean_then_broke`

newbuild_mechanism: «Семья выбирает квартиру в строящемся тюменском ЖК. В офисе продаж и PDF-брони указаны два санузла: мастер-санузел и гостевой. За четыре дня до регистрации ДДУ покупатели сверяют бронь с приложением к договору и видят один санузел вместо двух; цена не изменилась. Регистрацию ДДУ останавливают до внесения денег на эскроу.»

why_newbuild_not_secondary: «Конфликт возникает между бронью/планировкой от застройщика и приложением к ДДУ на строящийся объект. Это не сюжет о ЕГРН, продавце или проверке вторичного жилья.»

casus_status: composite editorial casus; не утверждать в статье конкретные ЖК, банк, застройщика, фамилии или реальную сделку без подтверждаемого источника.

## Dzen news-casus shape

dzen_casus_shape: PASS

event: «За четыре дня до регистрации ДДУ семья сопоставила PDF-брони с приложением к договору.»

risk: «В договоре исчез второй санузел, а стоимость квартиры сохранилась; после регистрации и раскрытия эскроу спорить о другой планировке существенно сложнее.»

time: «4 дня до регистрации ДДУ.»

finale: «Семья остановила регистрацию до эскроу и потребовала привести приложение к ДДУ в соответствие с забронированной планировкой либо зафиксировать новые условия письменно.»

comment_magnet_angle: «Если в брони два санузла, а в ДДУ один — вы бы подписывали “как есть” ради сохранения цены или срывали сделку?»

writer_note: «Не превращать материал в спокойный чеклист. Драматургия: бронь выглядела чисто → перед деньгами обнаружилась разница в приложении → решение остановить регистрацию. Практический вывод — сверять приложение к ДДУ с бронью и планом до регистрации и эскроу.»

## Wordstat

wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework: probe «планировка квартира новостройка» 29 → слабый тюменский спрос для demand spine → probe «новостройки тюмень» 4350, слишком общий → final P0 «квартиры в тюмени новостройки» 1047.

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры в тюмени новостройки» 1047 | RU 225: 2347

wordstat_probes:
- «планировка квартира новостройка» — 29, регионы 55+11176
- «новостройки тюмень» — 4350, регионы 55+11176
- «квартиры в тюмени новостройки» — 1047, регионы 55+11176; 2347, RU 225

## Klyshin

klyshin_hook: optional | none | original: «Клышин не использовался: угол построен на новом DDU-приложении и расхождении брони с планировкой.» | signal: none

## Anti-repeat and focus gates

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: актуальные исключения учтены, включая `eiszhs-priostanovka-do-eskrou-tyumen`, `mortgage_rate_hike_before_ddu` и сегодняшние/недавние кластеры DDU commercial vs studio, таунхаус vs flat, рассрочка 340k, УК 180k keys, lift технадзор, rent ban 2y, parking, КП-бронь sold, холодная лоджия, скидка 380k, планировка 54→49 м².

story_dup_check: PASS | cluster_id: `ddu_second_bathroom_missing_bron_tyumen`

h1_fingerprint_check: PASS | fingerprint: `4days:ddu_layout_bathroom_mismatch`

formula_spam_check: PASS | last3_mechanisms: `pereustupka_ban` / `insurance_payment` / `escrow_wrong_entity`; current mechanism: `booking_vs_ddu_appendix_bathroom_layout_mismatch`

topic_focus_check: PASS | only Tyumen newbuild / DDU / developer booking / escrow-before-registration context

anti_dupe_hard: PASS

## Signal URLs

signal_urls:
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/
- https://t.me/klyshin_A

## Research boundary for Writer

- Не использовать вторичку как аналог, сюжет или «контраст».
- Не называть расхождение в планировке типовой доказанной практикой без источника.
- Если в фактуре появляются конкретные ЖК, застройщик, банк или договор — подтверждать первичным документом либо формулировать как редакционный составной кейс.
- Сохранять P0 в H1/лиде естественно: спросовый запрос — «квартиры в Тюмени новостройки», конфликт — приложение к ДДУ против брони.
