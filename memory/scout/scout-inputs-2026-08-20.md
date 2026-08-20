# Scout inputs — 2026-08-20 (The Риэлтор)

## Run context
- date: 2026-08-20 (YEKT slot 12:00)
- tenant: The Риэлтор / Святослав Шакин / Тюмень
- published anti-dup (titles only): B01 ЕГРН/аванс, B02 расписка/денег нет, plus recent WP: нотариус +70к, наследники 3 года, повестка Росреестр, Сербский/бабушка, маткапитал доли, торги/дарение дочери

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API)

## Selected Klyshin hook (NOT yet used in articles)
- hook_id: power_of_attorney_svo
- original: «доверенность не броня — особенно старая и после СВО»
- angle: доверенности на продажу, в т.ч. старые; риск отзыва; межрегиональная сделка «один прилетит, остальные по доверенности»; СВО-цепочка
- klyshin_signal: 5 схем видео — новая схема с доверенностями участников СВО; «доверенность не броня»

## Live Wordstat probes (regions 55+11176; compare 225)

### Probe 1: «доверенность на продажу квартиры»
- Tyumen 55+11176: 99 (head)
- Russia 225: 7647
- Top Tyumen similar: нотариус доверенность 27, генеральная 18, доля 20, проверка доверенности нотариуса 1

### Probe 2: «проверка квартиры перед покупкой»
- Tyumen: 9 (weak alone)
- Similar buyer cluster weak — needs rework spine

### Probe 3: «егрн выписка на квартиру» (rework buyer jargon)
- Tyumen: 172 cluster (выписка из егрн 130, госуслуги 31)
- Related: егрн 7477, выписка из росреестра 225

### Probe 4: «купить квартиру в тюмени» (P0 spine)
- Tyumen: 23066
- Clusters: вторичка 3943, однокомнатная 1579, от застройщика 862

## Wordstat rework log
probe «проверка квартиры перед покупкой» 9 (weak) →
probe «доверенность на продажу квартиры» 99 (buyer-intent, hook-aligned) →
probe «егрн выписка на квартиру» 172 (checklist spine for due diligence) →
final P0 «купить квартиру в тюмени» 23066 | sticker/H2 clusters: доверенность на продажу 99, выписка егрн 130, вторичка 3943

## Signal URLs (fetch context)
- https://t.me/klyshin_A — доверенности, 5 схем, СВО
- https://dzen.ru/holyslav — блог риэлтора
- {{SITE_BASE}}/blog/ — sibling articles
- https://t.me/holyslav92 — личный канал

## Task for Scout
Pick topic_id B03. Invent catchy Klyshin-rhythm title (clear subject, no SEO tail). Slug from title.
Output handoff markdown per skill: topic_id, title draft, external_signal, signal_urls, klyshin_hook line, wordstat_rework line, wordstat line.
Facts city = Тюмень / Святослав Шакин. Do NOT duplicate B01-B02 angles.
