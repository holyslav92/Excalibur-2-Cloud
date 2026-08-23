# Scout assembled inputs — B11 — 2026-08-23

## Assignment
- topic_id: B11
- tenant: The Риэлтор / tymenrieltor.ru / Святослав Шакин / Тюмень
- Date: 2026-08-23 (Sunday YEKT)
- Slot: after B10 published today (grandma absent PND)

## Selected hook
- hook_id: tired_buyer_bad_flat (bank #12)
- original Klyshin: «Клиенты все чаще готовы купить плохую квартиру. Просто потому что нормальных почти нет»
- klyshin_signal_url: https://t.me/klyshin_A (post ~2026-08: 3–4 месяца поиска, усталость, «сделайте так, чтобы мы безопасно купили эту квартиру», негативные заключения ~10%, «покупаете жильё или будущий суд?»)
- angle for B11: **уставший покупатель после 3–4 месяцев поиска настаивает на рискованной квартире** — поведенческий риск + отказ до аванса по отрицательному заключению. НЕ наследство/сын, НЕ маткапитал, НЕ доверенность СВО, НЕ торги/задаток, НЕ скидка −2 млн, НЕ умершая жена, НЕ ипотека+ЕГРН, НЕ бабушка/ПНД.

## Anti-dupe constraints (HARD)
Published ledger: B02–B10. Do NOT duplicate clusters: inheritance son, matkapital child shares, doverennost SVO, deposit auction, -2M discount, deceased wife, mortgage EGRN, grandma PND absent.
Live WP note: есть «tri-mesyaca-iskali-kvartiru» — B11 angle = усталость + отрицательное заключение + отказ до аванса, не пересказ «3 месяца искали» без casus-финала.
scout_helper PASS on title draft below.

## Dzen news-casus (must PASS)
- event: в Тюмени семья 4 месяца ищет квартиру; на объекте с красными флагами в заключении просят «обезопасить покупку»
- risk: усталость покупателя → согласие на незакрытые юридические риски (документы не дали / отрицательное заключение)
- time: «после четырёх месяцев поиска» / «перед авансом»
- finale: сделку остановили; клиенту помогли не купить «судебный процесс вместо квартиры»
- buyer thought safe: «мы уже устали, сделайте так, чтобы можно было купить»

## Wordstat live probes (MCP-KV, regions 55+11176; compare 225)
- wordstat_get_user_info: OK (2026-08-23)
- probe «уставший покупатель квартира» — 7
- probe «вторичка в тюмени» — 5875
- probe «новостройки тюмень» — 4689
- probe «проверка квартиры перед покупкой» — 9
- probe «купить квартиру в тюмени» — 22753 (RU225 40097)
- rework path: hook weak 7 → вторичка 5875 / новостройки 4689 → buyer spine «купить квартиру в тюмени» 22753

## Title draft (news headline, Klyshin rhythm)
Четыре месяца искали в Тюмени — и чуть не купили квартиру, от которой юристы отказали

## article_dir slug
B11-pyat-mesyacev-iskali-v-tyumeni-ustavshij-pokupatel-chut-ne-kupil-riskovannuyu

## signal_urls (required)
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

## Output format
Write `.cursor/excalibur-blog-handoff.md` with all mandatory gate lines per scout skill:
wordstat_preflight, topic_id B11, title draft, article_dir, klyshin_hook, dzen_casus_shape, wordstat_rework, wordstat, signal_urls, external_signal summary.
