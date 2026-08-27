Scout run B11 — 2026-08-27. Собери handoff-прозу по SKILL (все обязательные строки).

ВАЖНО: верни ТОЛЬКО текст handoff (markdown/plain), без BLOCKER, без bash, без мета-комментариев. Скрипт сам запишет твой ответ в файл. Обязательные поля одной строкой каждое: topic_id, title draft, slug, wordstat_preflight, klyshin_hook, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat, signal_urls, external_signal.

## topic_id
B11

## Title draft (news headline, Klyshin rhythm, Tyumen)
Нотариус 18 лет назад всё проверил — в Тюмени перед авансом всплыла супружеская доля по кооперативу

## slug suggestion
notarius-18-let-nazad-vspylla-supruzheskaya-dolya-pered-avansom

## Klyshin
- hook_id: notary_not_shield_70k
- original hook: «нотариус всё проверил» — нет, не броня
- angle: кооператив + пай в браке + наследство 18 лет назад; нотариус не выделил супружескую долю; при проверке перед сделкой нотариус переоформил долю за 3–4 дня, но отказалась дать справку по наследникам — покупатели остановили аванс
- signal post: https://t.me/klyshin_A — свежий пост 27.08.2026 «Нотариус ошибся 18 лет назад. А проблему нашли только сейчас» (кооператив, обмен, пай, супружеская доля, дети от первого брака)

## Wordstat (MCP-KV live, conductor verified)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes regions 55+11176:
- «нотариус при покупке квартиры» → 25
- «проверка квартиры перед покупкой» → 3
- «квартира наследство продажа» → 181

Rework:
- «юридическая проверка квартиры» → 5 (слабый юридический жаргон)
- buyer spine «купить квартиру в тюмени» → 22722 (RU225 compare 39950)
- niche cluster «квартира наследство продажа» → 181 (RU225 compare 17312) — сохраняет risk/story angle

Final P0: «купить квартиру в тюмени» 22722

## dzen_casus_shape PASS
- event: в Тюмени продают кооперативную квартиру после наследства; покупатели готовы к авансу
- risk: супружеская доля по паю не была выделена 18 лет назад; наследники (в т.ч. от первого брака) не подтверждены документально
- time: «18 лет назад» / «за три дня до аванса»
- finale: нотариус переоформила долю, но отказалась выдать справку по наследникам — сделку остановили до передачи денег

## comment_magnet_angle
«Если нотариус 18 лет назад всё оформил — покупатель уже не вправе задавать вопросы, или вы всё равно копаете цепочку?»

## scout_helper
PASS 2026-08-27 — NO CANNIBALIZATION RISK, TOPIC FOCUS PASS

## signal_urls
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://t.me/holyslav92

## Author / city
Святослав Шакин, Тюмень (локализация, не копипаст Клышина)

## Anti-dup note
Отличается от live WP «нотариус удостоверил — суд отменил через год» (другой plot: суд vs кооператив+пай+супружеская доля). Не B07/B08 (сын первого брака / умершая жена ЗАГС). Не повестка (live avans+повестка). Не маткапитал+опека. Не уставший покупатель 4 мес.
