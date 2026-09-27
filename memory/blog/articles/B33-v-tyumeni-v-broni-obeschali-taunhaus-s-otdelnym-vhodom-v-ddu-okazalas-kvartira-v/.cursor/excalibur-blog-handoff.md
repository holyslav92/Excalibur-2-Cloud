# Scout handoff — B33

run_date: 2026-09-27
slot: 15:00 Asia/Yekaterinburg
topic_id: B33
tenant: The Риэлтор / Святослав Шакин, Тюмень
owner_lock: newbuild only
status: READY_FOR_RESEARCH

topic:
  final_p0: «новостройки тюмень»
  final_p0_volume: 4350
  title_draft: «В Тюмени в брони обещали таунхаус с отдельным входом — в ДДУ оказалась квартира в блоке»
  slug: tyumen-newbuild-booking-townhouse-apartment-ddu
  cluster_id: newbuild_townhouse_separate_entry_booking_vs_ddu_block_apartment_tyumen

top_energy_mirror: paper_clean_then_broke

newbuild_mechanism: «Семья с двумя детьми выбирает формат таунхауса / отдельного входа в тюменской новостройке — квартирном low-rise-блоке. В брони и на плане менеджер фиксирует “таунхаус, свой вход, без соседей с лестницы”. За 2–3 дня до открытия эскроу и подписания ДДУ выясняется, что объект оформляется как квартира в многоквартирном блоке: общий подъезд, другой этаж и площадь. Банк видит расхождение с одобрением, поэтому семья останавливает подписание до исправления документов или смены лота.»

why_newbuild_not_secondary: «Сюжет построен только на покупке объекта от застройщика: бронь, проект ДДУ, эскроу, планировка и тип объекта в новостройке. Сделки со вторичным продавцом, ЕГРН вторички и вторичные обременения отсутствуют.»

klyshin_hook: none

anti_repeat_preflight: live_blog_20 + ledger + used_clusters sync OK
closed_clusters_today:
  - «рассрочка разошлась с ценой на 340 тыс до ДДУ»
  - «УК потребовала 180 тыс за 5 дней до ключей»
avoid_clusters:
  - trade-in reject
  - booking expired price hike
  - mortgage rate hike before DDU
  - EGRN encumbrance secondary plot

dzen_casus_shape: PASS
event: «Семья выбрала формат таунхауса в новостройке.»
risk: «Тип объекта в ДДУ оказался не тем, что был обещан и зафиксирован в брони: квартира в блоке вместо ожидаемого формата с отдельным входом.»
time: «За 2–3 дня до открытия эскроу и подписания ДДУ.»
finale: «Семья остановила сделку до получения исправленных документов или смены лота; деньги на эскроу не перечислялись.»
comment_magnet_angle: «Если в брони “таунхаус”, а в ДДУ “квартира в блоке” — вы бы подписали ради сохранения цены или разорвали бронь?»

wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4350

wordstat_probes:
  - phrase: «новостройки тюмень»
    regions: 55,11176
    volume: 4350
    role: final P0 demand spine
  - phrase: «квартиры в тюмени новостройки»
    regions: 55,11176
    volume: 1047
    role: buyer-intent support
  - phrase: «купить новостройку в тюмени»
    regions: 55,11176
    volume: 891
    role: transaction-intent support
  - phrase: «новостройки в тюмени от застройщика»
    regions: 55,11176
    volume: 641
    role: developer/newbuild support
  - phrase: «тюмень новостройки дома»
    regions: 55,11176
    volume: 104
    role: format support
  - phrase: «таунхаус новостройка тюмень»
    regions: 55,11176
    volume: 4
    role: weak probe; not selected as P0

wordstat_rework: «таунхаус новостройка тюмень» 4 → weak; reworked to broader buyer-demand spine «новостройки тюмень» 4350 while retaining the newbuild news mechanism of booking-versus-DDU property-type mismatch.

story_dup_check: PASS
story_dup_basis: «Новый кластер: mismatch between promised townhouse/separate-entry format in booking materials and apartment classification in DDU. Distinct from today’s installment-price discrepancy and management-company fee-before-keys stories.»

h1_fingerprint_check: PASS
fingerprint: «Тюмень + бронь обещала формат жилья/отдельный вход + в ДДУ другой тип объекта/квартира в блоке»

formula_spam_check: PASS
last3_mechanisms:
  - installment versus contract price discrepancy
  - management-company fee before acceptance/keys
  - housing-type mismatch between booking and DDU
assessment: «Механизм и риск отличаются; no repeated booking-price, fee-before-keys, or mortgage-rate skeleton.»

scout_helper_check: PASS
topic_focus: PASS
anti_dupe_hard: PASS

research_constraints:
  - «Проверять только новостройку от застройщика: бронь, план, проект ДДУ, тип объекта, этаж, площадь, вход, эскроу.»
  - «Не превращать материал в спокойный гайд или чеклист.»
  - «Финал должен быть событийным: подписание остановлено до денег, предложено исправление или замена лота.»
  - «Не переименовывать сюжет во вторичку и не использовать вторичные ЕГРН-обременения.»
  - «Развести в тексте маркетинговое описание формата (“таунхаус”, “свой вход”) и юридическую квалификацию объекта в ДДУ.»
  - «Угол комментариев: подписывать ради сохранения цены или разрывать бронь при расхождении формата жилья.»

signal_urls:
  - https://dzen.ru/holyslav
  - https://t.me/Tyumen_Rieltor
  - site blog recent titles (anti-dup)

handoff_gate:
  wordstat_gate: PASS
  newbuild_focus: PASS
  dzen_casus_shape: PASS
  anti_dupe_hard: PASS
  ready_for_research: YES
