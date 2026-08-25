# Scout inputs — 2026-08-25 run

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK

## Signal URLs (today)
- https://t.me/s/klyshin_A — свежий пост «В квартире живет бабушка. Только бабушки в квартире нет» (ПНД, 1/3 доля, старая доверенность, скидка 3 млн, Институт Сербского)
- https://dzen.ru/holyslav — канал tenant
- {{SITE_BASE}}/blog/ — блог tenant
- https://t.me/holyslav92

## Klyshin hook selected
- hook_id: elderly_pnd_serbsky
- original: «В квартире живет бабушка. Только бабушки в квартире нет»
- angle: пожилой собственник 1/3 доли, ПНД, старая доверенность, нет освидетельствования/Сербского, скидка как red flag
- signal: https://t.me/s/klyshin_A (post 2026-08, бабушка-собственник, ПНД, доверенность без полномочий на выписку)

## Wordstat live (MCP-KV, regions 55+11176)
| probe | volume |
|-------|--------|
| доверенность на продажу квартиры | 69 |
| опека продажа квартиры | 168 |
| разрешение опеки на продажу квартиры | 51 |
| егрн | 7214 |
| выписка из егрн | 2494 |
| купить квартиру в тюмени | 22652 |
| купить квартиру в тюмени (RU 225) | 39858 |

wordstat_rework: probe «проверка квартиры у пожилого продавца» empty → «доверенность на продажу квартиры» 69 → «опека продажа квартиры» 168 → final P0 «купить квартиру в тюмени» 22652 (RU225 39858) | clusters tried: пожилой продавец, доверенность, опека, егрн

## Dzen news-casus shape
dzen_casus_shape: PASS
- event: «В Тюмени на осмотре сталинки „живёт бабушка“, а в квартире нет её вещей — долю 1/3 хотят продать по старой доверенности»
- risk: «ПНД, старая доверенность, нет полномочий снять с регистрации, нет медосвидетельствования»
- time: «доверенность несколько лет, бабушка годами в учреждении»
- finale: «сделку остановили — скидка 3 млн не закрыла риск оспаривания»

comment_magnet_angle: «Скидка три миллиона — повод закрыть глаза на ПНД или сигнал бежать?»

## Story-duplicate check
scout_helper.py --check-query PASS (no cluster match vs B05 grandma-on-viewing — другой legal risk: ПНД+доверенность vs „не нашли на осмотре“)

## Title draft (news headline, Klyshin rhythm)
«В объявлении бабушка — а спит она в ПНД: в Тюмени сделку остановили»

## Topic
- topic_id: B10
- slug: v-obyavlenii-babushka-a-ona-v-pnd-sdelku-v-tyumeni-ostanovili
- wp_category: vtorichka-i-riski

## Published anti-dup (do NOT repeat)
B01-B09 ledger + live WP: matkapital, notarius+суд, повестка, чистая выписка+оспорили, бабушка не на осмотре (другой угол)

## Task (CRITICAL)
Ты УЖЕ вызван скриптом `excalibur_blog_derouter_opus_chat.py` — ответ идёт напрямую в output-файл.
**ЗАПРЕЩЕНО** писать «DEROUTER SCOUT BLOCKER» или отказываться от генерации.
Напиши **полный** `.cursor/excalibur-blog-handoff.md`: YAML frontmatter (`topic_id`, `title`, `slug`, `status: ready`) + prose handoff per scout skill template со всеми gate-строками (wordstat_preflight, klyshin_hook, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat, signal_urls).
topic_id B10, slug v-obyavlenii-babushka-a-ona-v-pnd-sdelku-v-tyumeni-ostanovili
