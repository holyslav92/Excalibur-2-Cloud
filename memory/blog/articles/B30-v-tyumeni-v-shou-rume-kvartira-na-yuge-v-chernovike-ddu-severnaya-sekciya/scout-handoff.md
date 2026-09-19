Принял B30 как зафиксированный кластер. Запускаю обязательный Derouter-handoff через utility tier с переданными live Wordstat и anti-dupe результатами.# Scout handoff — B30

topic_id: B30  
run_date: 2026-09-19  
slot: weekend automation, 17:00 YEKT  
tenant: The Риэлтор / Святослав Шакин, Тюмень  
article_dir: `memory/blog/articles/B30-v-tyumeni-v-shou-rume-yuzhnaya-storona-v-chernovike-ddu-severnaya-sektsiya`

## Topic lock

title: «В Тюмени в шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция»

slug: `v-tyumeni-v-shou-rume-yuzhnaya-storona-v-chernovike-ddu-severnaya-sektsiya`

cluster_id: `newbuild_showroom_sun_side_vs_ddu_north_section_tyumen`

top_energy_mirror: `paper_clean_then_broke`

newbuild_mechanism: «Семья смотрит шоу-рум и макет квартиры на южной стороне ЖК в Тюмени. В брони и презентации зафиксированы “солнечная сторона” и вид во двор без тени. За пять дней до подписания ДДУ в черновике обнаруживается та же площадь и этаж, но секция B на северной стороне: окна выходят на соседний корпус и тень. Менеджер объясняет, что это “та же цена, просто другой подъезд”. Семья отказывается от подписания, часть брони удерживают, эскроу не открывали».

why_newbuild_not_secondary: «Сюжет касается только покупки у застройщика: шоу-рум, бронь, презентация, проект ДДУ и эскроу. В нём нет продавца вторичной квартиры, истории ЕГРН, наследства, банкротства или иных вторичных механизмов».

klyshin_hook: optional | none

## Dzen news-casus

dzen_casus_shape: PASS

event: «Квартиру с обещанной южной ориентацией показывают в шоу-руме, но за пять дней до ДДУ покупателю направляют проект с северной секцией».

risk: «Покупатель получает другой объект по ключевому потребительскому параметру: меньше света, окна на соседний корпус, возможное снижение привлекательности для проживания, аренды и перепродажи».

time: «Пять дней до подписания ДДУ; эскроу ещё не открыт».

finale: «Семья отказывается от ДДУ, теряет часть брони и выясняет, какие параметры нужно фиксировать в заявке, бронировке и проекте договора до внесения денег».

comment_magnet_angle: «Если в шоу-руме солнце, а в ДДУ — северная секция за ту же цену, вы бы подписали, чтобы не потерять бронь, или сразу ушли?»

## Wordstat

wordstat_preflight: mcp-kv `wordstat_get_user_info` OK

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» — 4430 | RU «новостройки» — 927399

wordstat_rework: probe «квартиры с отделкой тюмень» — 79 → «тюмень новостройки квартира с отделкой» — 25 → demand spine «новостройки тюмень» — 4430; orientation/section mismatch используется как новостной механизм в H1, а не как отдельный слабый запрос «сторона света»

final P0: «новостройки тюмень» — регионы 55,11176, сравнение с RU 225: 4430 / «новостройки» — 927399

## Anti-repeat

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK

closed_clusters: B27 — land lease vs ownership in declaration; B28 — KP gas 2026 vs declaration 2028; B29 — bank removed zero-down developer promo 6 days before DDU; same-day live topics — 4% discount not in DDU, КП ceilings -25 cm, family mortgage child 7, discount/skidka plots

excluded_recent_mechanisms: `booking_expired` same-day; `assignment_lost` 30d; `paper_clean_then_broke` overload in declaration/utility plots

story_dup_check: PASS | cluster_id: `newbuild_showroom_sun_side_vs_ddu_north_section_tyumen`

h1_fingerprint_check: PASS | fingerprint: `showroom_south_orientation_vs_ddu_north_section_same_area_floor`

formula_spam_check: PASS | last3_mechanisms: declaration land lease/ownership; КП gas commissioning-date mismatch; developer zero-down promotion withdrawn before DDU

anti_dupe_hard: PASS

## Gate results

scout_helper.py --check-query: PASS | 2026-09-19

scout_story_dup.py --text: PASS | 2026-09-19

topic_focus.py: PASS | newbuild-only

owner_lock: PASS | Тюмень; новостройка; покупка у застройщика; квартира; ДДУ/бронь/эскроу

secondary_recycle: PASS | вторичный рынок не используется

## Signal URLs

- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
- `{{SITE_BASE}}/blog/`

## Final lock

final_p0: «новостройки тюмень»

locked_title: «В Тюмени в шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция»

locked_slug: `v-tyumeni-v-shou-rume-yuzhnaya-storona-v-chernovike-ddu-severnaya-sektsiya`

locked_article_dir: `memory/blog/articles/B30-v-tyumeni-v-shou-rume-yuzhnaya-storona-v-chernovike-ddu-severnaya-sektsiya`

handoff_status: PASS
