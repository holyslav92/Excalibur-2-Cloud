# Scout assembled input — B06 — 2026-08-21

## Задача
Выбрать P0 тему B06 через Klyshin×Wordstat dual gate. Уже использованы B01–B05. Anti-dup на сайте: наследство 3 года, Сербский/бабушка, нотarius +70k, маткапитал детские доли, повестка продавцу.

## Кандидаты (оценка Wordstat Tyumen 55+11176, compare RU 225)

### 1. cian_autoprice_minus_million — ВЫБРАН
- Klyshin hook: «автооценка ЦИАН/Домклик минус миллион к рынку»
- Live signal (2026-08, top @klyshin_A): сервис 18 млн vs живой рынок ~20 млн; собственник занижает → очередь на показ → снимает объявление → поднимает цену выше рынка
- Wordstat probes (MCP-KV live):
  - «оценка квартиры тюмень» → 73 (слабый hook-probe)
  - rework «купить квартиру в тюмени вторичка» → 3943
  - rework «вторичка в тюмени» → 5798
  - final P0 «купить квартиру в тюмени» → 23066 (Tyumen 55+11176)
  - compare RU 225 «купить квартиру в тюмени» → 40585
- Anti-dup: не пересекается с B01–B05; отличен от B05 (скидка/срочность vs алгоритмическая заниженная цена)
- Buyer angle для Тюмени: покупатель на вторичке не ориентируется на «рекомендованную цену» ЦИАН/Домклик; заниженная автооценка = ложный «дешёвый» объект или срыв сделки после поднятия цены

### 2. tired_buyer_bad_flat — отклонён
- «купить квартиру в тюмени» 23066 — тот же P0, но угол слабее дифференцируется от общих «проверяйте до аванса»; hook «уставший покупатель» не даёт отдельного Wordstat-кластера

### 3. five_court_schemes — отклонён
- «проверка квартиры перед покупкой» 9; «банкротство продавца квартиры» 30 — слабые кластеры; anti-dup с B03 (торги/банкротство), B04 (доверенность), маткапитал на сайте

### 4. phone_scammers_notary — отклонён
- «мошенники при покупке квартиры» 1; rework «юридическая проверка квартиры при покупке» 5 — нет честного high-frequency buyer cluster с тем же story без overlap с нотариус +70k

### 5. notary_not_shield_70k — отклонён (anti-dup)
- Прямой смысловой дубль опубликованного поста «нотarius +70k» на сайте

## Wordstat preflight
wordstat_get_user_info OK (MCP-KV Yandex Cloud API, 2026-08-21)

## Signal URLs (≥2 помимо klyshin_A)
- https://t.me/klyshin_A — пост про автооценку минус 1–2 млн (август 2026)
- https://dzen.ru/holyslav — канал «Советы от риэлтора», свежие материалы про риски вторички
- {{SITE_BASE}}/blog/ — блог The Риэлтор
- https://t.me/holyslav92 — личный канал Святослава Шакина

## Published titles (anti-dup only)
B01 ЕГРН/аванс ready; B02 расписка published; B03 48ч/дарение published; B04 доверенность СВО published; B05 скидка 2 млн published

## Выход handoff
topic_id: B06
hook_id: cian_autoprice_minus_million
article_dir slug suggestion: B06-avtoocenka-minus-dva-milliona-k-rinku
title draft: Klyshin rhythm — case hook про автооценку и «минус два миллиона» (не SEO-хвост)
final P0: «купить квартиру в tюmeni» 23066
stickers/H2 из rework: «вторичка в тюmeni» 5799, «купить квартиру в tюmeni вторичka» 3943

Напиши handoff в формате skill: topic_id, title draft, external_signal, signal_urls, wordstat_preflight, klyshin_hook, wordstat_rework, wordstat lines, article_dir, priority P0.
