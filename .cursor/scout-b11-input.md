Scout run B11 — 2026-08-27.

**ВАЖНО для модели:** MCP-KV Wordstat и scout_helper УЖЕ выполнены дирижёром (Cursor). Тебе НЕ нужно вызывать инструменты. НЕ пиши BLOCKER. Твоя задача — оформить handoff-прозу из данных ниже в формат SKILL (все обязательные строки: wordstat_preflight, klyshin_hook, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat, topic_id, title draft, signal_urls, external_signal).

## topic_id
B11

## Title draft (news headline, Klyshin rhythm, Tyumen)
В Тюмени четыре месяца искали вторичку — уставший покупатель согласился на риск, через два года суд оспорил сделку

## slug suggestion
chetyre-mesyaca-ishhali-ustavshij-pokupatel-soglasilsya-na-risk

## Klyshin
- hook_id: tired_buyer_bad_flat
- original hook: «уставший покупатель берёт плохую квартиру»
- angle: 3–4 месяца поиска на рынке Тюмени; бюджет тает; покупатель хочет «закончить квест»; приходит с «сделайте безопасно» — в заключении риск (третий наследник / продавец не дал документы); негативные заключения ~10%; «безопасно купить нельзя — только понять риски»
- signal post: https://t.me/klyshin_A — «Клиенты все чаще готовы купить плохую квартиру. Просто потому что нормальных почти нет» (август 2026, ~17.8K views)

## Wordstat (MCP-KV live, conductor verified)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes regions 55+11176:
- «проверка квартиры перед покупкой» → 3
- «риски при покупке квартиры» → 17
- «вторичка в тюмени» → 6068
- «купить квартиру в тюмени» → 22833

Compare RU225:
- «купить квартиру в тюмени» → 40089

Rework (weak hook probes → buyer spine):
- hook probes 3–17 → локализация Тюмень + buyer spine «купить квартиру в тюмени» 22833 (RU225 40089)
- sticker cluster: «купить квартиру в тюмени вторичка» 4071; «вторичка в тюмени» 6068

Final P0: «купить квартиру в тюмени» 22833

## dzen_casus_shape PASS
- event: семья в Тюмени четыре месяца искала вторичку, бюджет тает, согласилась на квартиру с «жёлтым» заключением
- risk: третий наследник; продавец не дал документы, без которых риск не снимается
- time: через два года после регистрации
- finale: суд оспорил сделку — покупатель думал, что «закончил поиск», но риск не стоил квартиры

## comment_magnet_angle
«Если заключение желтое, а поиск уже четвертый месяц — вы всё равно внесли бы аванс, чтобы закончить?»

## scout_helper
PASS 2026-08-27 — NO CANNIBALIZATION RISK, TOPIC FOCUS PASS
story_dup PASS — no published plot cluster

## signal_urls
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://t.me/holyslav92

## Author / city
Святослав Шакин, Тюмень (локализация, не копипаст Клышина)

## Anti-dup note
Не пересекается с B01–B10 clusters и WP slugs to avoid (маткапитал/опека, банкротство продавца, нотариус+год+суд, повестка+регистрация, выписка чистая+3 мес, скидка+ПНД). Отклонены для B11: notary_not_shield_70k (LIVE pool overlap 39%), summons_registration_stop (WP povestka), matkapital_child_shares (WP matkapital-byl-opeka), five_court_schemes (overlap B03/B04).

## WP slugs explicitly avoided (story-duplicate window)
matkapital-byl-opeka-molchala, kupili-kvartiru-prodavec-bankrotstvo, v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil, avans-vnesli-registraciyu-priostanovili-po-povestke, v-vypiske-vse-chisto-prodavec-vladel-tri-mesyaca, skidka-skryla-pnd-sdelku
