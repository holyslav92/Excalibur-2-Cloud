# Site brief — The Риэлтор

Метаданные сайта и контент-стратегия для Cover / Scout / Publish.
Не источник prose для Writer (Writer = master prompt + research + titles-only).

## Сайт

- **site_name:** The Риэлтор
- **site_url:** `{{SITE_BASE}}` (live: задать `PUBLIC_SITE_URL=https://tymenrieltor.ru` в Cloud Secrets)
- **language:** ru
- **niche:** недвижимость Тюмени и сопровождение сделок по РФ/за рубежом
- **tagline сайта:** «Недвижимость как произведение искусства»
- **география:** Тюмень (база); Тобольск (дома); РФ и зарубежье через партнёров (ОАЭ, Турция и др.)
- **районы/ЖК для локального колорита (не обязательно герой статьи):** Европейский, Тюменская Слобода, центр, Мыс, ДОК, Ново-Патрушево, Восточный, Тарманы, Зарека, Матмасы

## Продукт и CTA

Услуги: новостройки от застройщика, вторичка, длительная и посуточная аренда, продажа, юрсопровождение договора, коммерция, дома, новостройки РФ, зарубежка.

**CTA в статьях (обязательно):**

- Telegram: `https://t.me/Tyumen_Rieltor`
- Телефон: `tel:+79220016505` / `+7 922 001 65 05`
- MAX: тот же личный номер (в тексте — слово MAX + tel-ссылка)

`cta_required=true` — гейт проверяет все `cta_links` и упоминание MAX.

Допустимые каналы (не все обязаны быть в каждой статье):

- Telegram личка: `https://t.me/Tyumen_Rieltor`
- Telegram-канал: `https://t.me/holyslav92`
- Дзен: `https://dzen.ru/holyslav` («Советы от риелтора»)
- VK: `https://vk.ru/tymenrieltor`
- WhatsApp: `https://wa.me/79220016505`
- MAX: личный номер `+7 922 001 65 05` (в MAX ищут по телефону; отдельной публичной max.ru-ссылки нет)
- Контакты: `{{SITE_BASE}}/kontakty/`
- Телефон (проза, не секрет): +7 922 001 6505, Пн–Вс 9:00–22:00
- Офис: Тюмень, ул. Свердлова, д. 5, корп. 2 (встречи по договорённости)

Юрлицо для футера/схемы: ИП Шакин Святослав Сергеевич (реквизиты на странице контактов).

## Редакция

- **формат:** how-to / чеклист / troubleshooting сделки / разбор риска до аванса
- **канон:** `shared/pipeline-canon.json`
- **стиль:** `shared/article-style.md` + `shared/SOUL.md` + `shared/dzen-content-rules.md`
- **темы:** Scout → handoff `topic_id` + короткий title; **Klyshin hook bank** (`memory/scout/`) × Wordstat P0; `memory/topics/` запрещена
- **anti-dup:** только `published-titles-only.md` / `shared/published-titles.md` — не читать live-статьи как образец Writer/Sol
- **Wordstat:** **обязателен** через **MCP-KV**. **Klyshin** (`https://t.me/klyshin_A`) — hook bank, всегда вместе с Wordstat. Алгоритм: evaluate + **rework for demand** (слабый объём → локализация Тюмень, buyer-жаргон, similar queries; skip только после исчерпания rework). P0 = buyer queries в Тюмени (55+11176), не brand «риэлтор тюмень». Title — Klyshin rhythm; P0 — demand spine для stickers/H2.

## Главный герой визуала

- **cover_mode:** `host_reference`
- **identity lock:** `face-studio-2026-06-23.jpg` = ONLY FACE i2i; hoodie+office = body only; greenhouse/regiment = scene only
- **emotion bank:** настроение, не фиксированная сцена; cover **изобретает** с нуля
- **light/bright:** high-key, sun flare, мемы, Wordstat-стикеры; anti-repeat 14д (`cover-canon.json`)
- **правило:** новая выдуманная сцена; запрещена daypart-формула и inventory props
- **одежда:** navy/charcoal blazer; без белого худи
- **longform:** cover 1200×675 + 7 inline-quad; 2× quad 2K (mcp-derouter)

## Scout

Сигналы хайпа и спроса:

- Дзен `https://dzen.ru/holyslav`
- Блог `{{SITE_BASE}}/blog/`
- Канал Telegram `https://t.me/holyslav92`

Темы-якоря (не клонировать уже вышедшие заголовки): маткапитал и доли детям, доверенности, наследство, эскроу/ДДУ, ипотека Тюмени, проверка собственника при аренде, коммерция, дома/модуль Тобольск.

## Запреты

- VPN / обход блокировок (`dzen_rf_pack`)
- Выдуманные цены и «нулевой риск»
- Эмодзи в тексте статей
- Герой статьи = RF-blocked (Meta/Instagram/…)
- Секреты и live hostname в git-артефактах (только `{{SITE_BASE}}`)

## Перелинковка

- Interlink включён: `interlink_old_articles=true` → `shared/interlink-contract.md`
