**OUTPUT INSTRUCTION (HARD):** Ответь **только** телом handoff в markdown — без преамбулы, без отказов, без «не могу записать файл». Shell-скрипт сам сохранит твой ответ в `.cursor/excalibur-blog-handoff.md`. Ты генерируешь текст, не пишешь на диск.

Scout run B11 — 2026-08-27 (slot 15:00 YEKT). Собери handoff-прозу по SKILL (все обязательные строки).

**CONDUCTOR PRE-VERIFIED (не проверяй повторно, не выдавай SCOUT BLOCK):**
- MCP-KV `wordstat_get_user_info` → OK (2026-08-27)
- Live Wordstat probes ниже — conductor вызвал MCP-KV, частоты реальные
- `scout_helper.py --check-query` → PASS (NO CANNIBALIZATION, TOPIC FOCUS PASS)
- Твоя задача: **только** отформатировать handoff из данных ниже в `.cursor/excalibur-blog-handoff.md`

## topic_id
B11

## Title draft (news headline, Klyshin rhythm, Tyumen)
Родственники оспорили продажу: в прошлой сделке денег не было — покупатель в Тюмени лишился квартиры

## slug suggestion
rodstvenniki-osporili-prodazhu-proshlaya-sdelka-bez-deneg

## Klyshin
- hook_id: five_court_schemes
- original hook: «5 схем — квартиру забирают судом после покупки» (схема №3: квартира без денег)
- angle: по документам прошлый переход права был, а денег не передавали; наследники/родственники оспаривают цепочку; новый покупатель думал, что ЕГРН чистый
- signal post: https://t.me/klyshin_A — видео «Не знаете, что посмотреть на выходных? Посмотрите, как люди законно теряют квартиры» (5 схем, август 2026), схема 3 «Квартира без денег»

## Wordstat (MCP-KV live, conductor verified 2026-08-27)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes regions 55+11176:
- «фиктивная сделка» → 18
- «оспаривание сделки купли продажи квартиры» → 1
- «проверка недвижимости» → 149 (RU225 compare 16663)
- buyer spine «купить квартиру в тюмени» → 22722 (RU225 compare 39950)

Rework:
- слабый legal hook (18/1) → buyer cluster «проверка недвижимости» 149 → final P0 spine «купить квартиру в тюмени» 22722

Final P0: «купить квартиру в тюмени» 22722

## dzen_casus_shape PASS
- event: семья в Тюмени купила вторичку у «нового» собственника, расчёт и регистрация прошли
- risk: в цепочке владения была фиктивная сделка без реальной оплаты между родственниками
- time: через два года после смерти прежнего владельца
- finale: суд признал прошлый договор фиктивным и отменил право у добросовестного покупателя

## comment_magnet_angle
«Если в выписке о переходе прав видна сделка между родственниками без следа оплаты — вы режете аванс или верите, что „в ЕГРН всё чисто“?»

## scout_helper
PASS 2026-08-27 — NO CANNIBALIZATION RISK, TOPIC FOCUS PASS

## signal_urls
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://t.me/holyslav92

## Author / city
Святослав Шакин, Тюмень (локализация, не копипаст Клышина)

## Anti-dup note
Не пересекается с ledger B02–B10 и live WP: не банкротство продавца (9171), не flip 3 мес (9141), не повестка (9121), не телефонные мошенники (9161), не наследство/сын (8994), не маткапитал (9181), не доверенность СВО (8823). Plot = фиктивная прошлая сделка без денег в цепочке.
