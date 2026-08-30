# Scout inputs — B17 — 2026-08-30 15:00 YEKT slot

## Run context
- topic_id: B17 (next after B16 shipped 12:00 today)
- tenant: The Риэлтор / tymenrieltor.ru / Святослав Шакин
- slot: Sunday weekend Grok routine the-4
- klyshin_hook: none (fresh Tyumen casus without Klyshin)

## Anti-repeat preflight
- synced used-clusters: 17 active locks (see memory/scout/used-clusters.json)
- weekend LIVE clusters to avoid (already published): rent_to_buy, relatives_court_incapacity, fssp_arrest, akkreditiv_seller_no_money, storage_room_not_in_egrn, preliminary_contract_sold_elsewhere, seller_mortgage_lien, communal_share_neighbor (B16)
- frozen through September: ЕГРН/банкротство, маткапитал+опека, 4 месяца поиска, повестка, бабушка+доверенность, ПНД 3млн, супружеская доля/наследники, суд 2 года, пожилой по телефону

## Proposed cluster (conductor pre-lock)
- cluster_id: registered_persons_block_sale_before_advance
- plot: покупатели в Тюмени проверили ЕГРН — чисто, ипотеку одобрили. Перед авансом запросили справку о зарегистрированных: в квартире числятся бывшая жена продавца и взрослый сын. Продавец обещал «сами выпишутся за неделю, уже делали». Юрист: добровольная выписка может затянуться на месяцы, зарегистрированные имеют права на жильё. Сделку остановили до аванса — задаток не вносили.
- dzen_casus_shape: PASS
  - event: срыв сделки накануне аванса из-за прописанных
  - risk: зарегистрированные лица / невозможность выселить до сделки
  - time: за 3 дня до планируемого аванса
  - finale: отказ от сделки, деньги не потеряны
- comment_magnet_angle: «Продавец клянётся, что прописанные уйдут сами — вы бы поверили и внесли аванс?»
- title draft: В Тюмени перед авансом всплыли прописанные — продавец обещал выписать за неделю

## Wordstat MCP-KV (live 2026-08-30)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework log:
- probe «выписка из квартиры прописанные» → 6 (55+11176)
- probe «прописанные в квартире риски» → 4 (55+11176)
- probe «снять с регистрации квартира тюмень» → 13 (55+11176)
- rework → final P0 «прописка при покупке квартиры» → 10 (55+11176); compare RU 225 → 477

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «прописка при покупке квартиры» 10 (Tyumen+oblast), RU 477

## Live blog recent (from today.py / WP)
- B16 communal share neighbor blocked
- B14 seller mortgage lien
- preliminary contract sold elsewhere
- storage room not in EGRN
- akkreditiv seller no money
- FSSP arrest 2 days before registration
- relatives court incapacity day before advance
- rent to buy owner sold elsewhere

## Task for Scout (Derouter)
Confirm or refine cluster_id, title draft, P0 phrase, comment_magnet_angle.
Output handoff per skill format with story_dup_check: PASS and all required fields.
If duplicate cluster detected — pick different NEW Tyumen casus from open angles in next-cluster-guidance.md.
