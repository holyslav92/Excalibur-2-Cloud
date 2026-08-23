# Scout assembled inputs — B10 — 2026-08-23

## Assignment
- topic_id: B10
- tenant: The Риэлтор / tymenrieltor.ru / Святослав Шакин / Тюмень
- Article A of 2 today (Director run)
- Date: 2026-08-23 (Sunday YEKT)

## Selected hook
- hook_id: elderly_pnd_serbsky (bank #3)
- original Klyshin: «В квартире живет бабушка. Только бабушки нет»
- klyshin_signal_url: https://t.me/klyshin_A (post ~line 65: сталинка, бабушка-собственник 1/3, ПНД, старая доверенность, «где спит бабушка»)
- angle for B10: **физическое отсутствие пожилого собственника + ПНД + доверенность без полномочий на выписку** — НЕ скидка 2–3 млн (B05), НЕ «очередь в Сербского» (live WP 8740)

## Anti-dupe constraints (HARD)
Published ledger: B02–B09. Live WP recent: povестка, nasledstvo-ne-proshlo-tri-goda, v-vypiske-egrn-est-stroka, tri-mesyaca-iskali-kvartiru.
Do NOT duplicate clusters: inheritance son first marriage, matkapital child shares, doverennost SVO, deposit before auction, -2M discount.
B05 used elderly_pnd_serbsky with discount angle — B10 must differ: no «уценили на два миллиона», no urgent deposit hook.

## Dzen news-casus (must PASS)
- event: осмотр сталинки в Тюмени; в объявлении «живёт бабушка-собственник 1/3», в квартире нет её вещей/спального места
- risk: ПНД, дееспособность, старая доверенность без снятия с регистрации, продажа доли без бабушки на сделке
- time: «на осмотре» / «перед авансом»
- finale: сделку остановили; риск оспаривания и суда если бы внесли аванс
- buyer thought safe: «риелтор сказал бабушка в санатории, доверенность есть»

## Wordstat live probes (MCP-KV, regions 55+11176; compare 225)
- probe «бабушка в объявлении пнд» — weak/none
- probe «проверка квартиры у пожилого продавца» — API empty
- probe «опека при продаже квартиры» — 28
- probe «доверенность на продажу квартиры» — 72
- probe «выписка егрн на квартиру» — 124 (similar cluster «егрн» 7509)
- probe «купить квартиру в тюмени» — 22753 (RU225 40097)
- rework path: hook weak → доверенность 72 + опека 28 → buyer spine «купить квартиру в тюмени» 22753

## Title draft (news headline, Klyshin rhythm)
В объявлении жила бабушка-собственник — в квартире её следов не нашли, сделку в Тюмени остановили до аванса

## signal_urls (required)
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

## Output format
Write `.cursor/excalibur-blog-handoff.md` with all mandatory gate lines per scout skill:
wordstat_preflight, topic_id B10, title draft, klyshin_hook, dzen_casus_shape, wordstat_rework, wordstat, signal_urls, external_signal summary.
