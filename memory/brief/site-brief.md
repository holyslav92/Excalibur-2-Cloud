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

**CTA в статьях:** `https://t.me/Tyumen_Rieltor` (`tenant-config.cta_links`).  
`cta_required=false`, но если ссылка в списке — гейт ждёт её в HTML.

Допустимые каналы (не все обязаны быть в каждой статье):

- Telegram личка: `https://t.me/Tyumen_Rieltor`
- Telegram-канал: `https://t.me/holyslav92`
- Дзен: `https://dzen.ru/holyslav` («Советы от риелтора»)
- VK: `https://vk.ru/tymenrieltor`
- WhatsApp: `https://wa.me/79220016505`
- MAX: упоминается на сайте как канал срочных вопросов
- Контакты: `{{SITE_BASE}}/kontakty/`
- Телефон (проза, не секрет): +7 922 001 6505, Пн–Вс 9:00–22:00
- Офис: Тюмень, ул. Свердлова, д. 5, корп. 2 (встречи по договорённости)

Юрлицо для футера/схемы: ИП Шакин Святослав Сергеевич (реквизиты на странице контактов).

## Редакция

- **формат:** how-to / чеклист / troubleshooting сделки / разбор риска до аванса
- **канон:** `shared/pipeline-canon.json`
- **стиль:** `shared/article-style.md` + `shared/SOUL.md` + `shared/dzen-content-rules.md`
- **темы:** Scout → handoff `topic_id` + короткий title; `memory/topics/` запрещена
- **anti-dup:** только `published-titles-only.md` / `shared/published-titles.md` — не читать live-статьи как образец Writer/Sol
- **Wordstat:** желателен для Scout (MCP), не обязателен для старта

## Главный герой визуала

- **cover_mode:** `host_reference`
- **герой:** Святослав Шакин (лицо только с `portrait.jpg` / landing; не дефолт пайплайна)
- **одежда lock:** slim navy blazer, чёрный crew, navy брюки, чёрные туфли; **без** белого худи и наушников
- **reference / lock:** `memory/cover/blog-hero.json` + `memory/cover/assets/portrait.jpg`
- **URL эталона:** `{{SITE_BASE}}/wp-content/themes/tymenrieltor-light/assets/images/portrait.jpg`
- **style preset:** `memory/cover/quad-style-the-rieltor.json` (`the_rieltor_twilight_gold`)
- **палитра:** панели `#FFFFFF`; ink `#141821` / `#1a1508`; золото `#dcc5a1` `#ecd9b6` `#f3e6c9`; twilight `#05070f` `#0e1322` — mood сайта, не фон quad
- **мотивы:** мелкий золотой ключ-дом (не лого-watermark), папка/ключи/дверь как метафора сделки
- **запреты cover:** pink-cat, EXCALIBUR stamp, beige gradient, Instagram, чужое лицо
- **inline:** без людей; 3–6 RU labels; не выдавать UI за скрин ЦИАН/Авито
- **meme_caption_ru:** пусто

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
- Interlink на старые статьи (`interlink_old_articles=false`)
