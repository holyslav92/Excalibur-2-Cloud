# Assembled Scout input — B07 — 2026-08-21 (slot 07:01 UTC)

## Run context
- topic_id: B07
- scout_date: 2026-08-21
- tenant: The Риэлтор, Тюмень, автор Святослав Шакин
- dzen_rf_pack: true — без Meta/Facebook/Instagram как героя; СВО только как факт кейса (не политический how-to)
- used_hooks anti-dup: pre_advance_check(B01), receipt_no_money(B02), bankruptcy_auction_48h(B03), power_of_attorney_svo(B04), urgent_discount_risk+elderly_pnd_serbsky(B05), cian_autoprice_minus_million(B06)
- selected hook: heirs_first_marriage_3y (NOT used; matkapital_child_shares and summons_registration_stop weaker clusters)

## Published titles only (anti-dup)
| topic_id | title |
|----------|-------|
| B02 | В Тюмени расписку за квартиру написали — денег на счёте нет |
| B03 | Почти внесли задаток на торгах — квартиру подарили дочери |
| B04 | Квартиру продавали по доверенности. Хозяин был на СВО |
| B05 | Квартиру уценили на два миллиона и просят задаток сегодня |
| B06 | Автооценка занизила цену — и квартира подорожала за сутки |

Overlap check: B07 = наследники/отказы/3 года — не дублирует B04 (доверенность), B05 (скидка), B06 (автооценка). B01 pre_advance adjacent but другий hook (егрн/аванс generic).

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

## Signal URLs (live fetch 2026-08-21)

### https://t.me/s/klyshin_A — PRIMARY Klyshin signal (heirs hook)
Пост «Один отчет за 2 900 рублей — и стало понятно, что в квартиру лучше не заходить» (август 2026):
- Предавансовая проверка: приватизация мама/папа/ребёнок; папа умер, доля по наследству.
- Отчёт красным: документы-основания и история владения — риск; **после наследства не прошло 3 года**.
- Наследники первой очереди = супруг, дети, родители — **все**, включая **дети от первого брака**, не только «семья в квартире».
- Риелтор не знает «первый ли брак» → задача: дети от первого брака, отказы, общение.
- Вскрылось: **сын от первого брака есть, отказа нет, документов нет**, где он — неизвестно.
- Ответ продавцов: «Ну отказа не будет. **Покупайте так**».
- Кейс СВО: отец умер 2 года назад, сын на СВО — мог не заявить права; юридическая возможность оспорить → суд.
- Клиент **не купил** — лучше потерять объект на выборе, чем суд.
- Реакции: 👍132 🔥68 ❤58
- CTA канала: «Сначала проверка. Потом аванс.» Предавансовый отчёт 2900 ₽.

Связанный пост «Продавец сказал: В браке не был. А потом нашлась умершая жена и наследники» — цепочки наследников, супружеская доля, дети от разных браков (усиливает угол, но B07 фокус = 3 года + отказ + первый брак).

### https://dzen.ru/holyslav — tenant mirror
Святослав Шакин «Советы от риелтора», август 2026:
- 50 мин назад: B06 «Автооценка занизила цену…» (published)
- 18 ч: B05 «Квартиру уценили на два миллиона…»
- Подборка «2026 юридически важные» — контекст проверки до аванса в Тюмени

### {{SITE_BASE}}/blog/ — site blog (WP live)
Recent published (MCP wordpress_get_posts):
- B06 автооценка / B05 скидка / B04 доверенность / B03 торги / B01-adjacent нотариус +70k
- Нет опубликованного поста про наследников первого брака / 3 года / отказы — зелёное поле для B07

### https://t.me/holyslav92
Канал Святослава Шакина — риэлтор Тюмень; CTA hub (сигнал tenant voice, не дубль Klyshin).

## Klyshin hook bank entry
- id: heirs_first_marriage_3y
- hook_ru: «дети от первого брака и отказы — три года не прошло»
- angle: наследники, отказы, срок 3 года после наследства; предавансовый отчёт с красными рисками
- tyumen_localize: true

## Wordstat MCP-KV live — regions 55 + 11176 — 2026-08-21

Rework cycle (hook probes → buyer clusters):
| step | phrase | volume (55+11176) | note |
|------|--------|-------------------|------|
| probe | проверка квартиры при наследстве | API empty | rework |
| probe | проверка квартиры перед покупкой | 9 | weak |
| probe | наследники квартира | 215 → «наследник квартиры» | hook cluster |
| probe | наследство квартира продажа | 176 → «квартира наследство продажа» | sale cluster |
| probe | вступление в наследство | 1266 | buyer intent |
| probe | наследство квартиры | **968** | **final P0** (seed phrase match) |
| buyer spine | купить квартиру в тюмени | 23066 | sticker/H2 (not final — overlap B01/B06) |

Compare RU225:
- наследство квартиры: 105131
- вступление в наследство: 143484
- купить квартиру в тюмени: 40585

Stickers/H2 from live queries:
- продажа квартиры после наследства (34)
- продажа квартиры в наследство менее 3 лет (15)
- наследство квартира наследники (53)
- после вступления в наследство квартиры (96)

## Task for Scout handoff
OUTPUT ONLY the handoff markdown body (no code blocks with bash, no meta). Write:
- topic_id: B07
- title draft: Klyshin rhythm, case hook про «покупайте так» / сын от первого брака / 3 года / Тюмень; НЕ SEO-хвосты
- external_signal prose (Klyshin case + Tyumen buyer framing for Святослав Шакин)
- signal_urls list (all four)
- wordstat_preflight line
- klyshin_hook line with id, original, angle, signal URL
- wordstat_rework line with full probe→final log and frequencies
- wordstat line: mcp_kv live | regions 55,11176,compare225 | P0 «наследство квартиры» 968 | compare RU225 105131 | include купить квартиру в тюмени 23066 as sticker cluster

Facts: Святослав Шакин / Тюмень. Do not copy Moscow/Dubai posts as P0.
