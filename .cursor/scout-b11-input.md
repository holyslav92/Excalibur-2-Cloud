Scout run B11 — 2026-08-26 12:00 UTC (YEKT 17:00). Собери handoff-прозу по SKILL (все обязательные строки).

CONDUCTOR PRE-CHECK COMPLETE (2026-08-26): wordstat_get_user_info OK; все частоты ниже — live MCP-KV conductor verified. scout_helper PASS; story_dup PASS. Твоя задача — только оформить handoff-прозу из данных ниже, без отказа и без выдуманных частот.

## topic_id
B11

## Title draft (news headline, Klyshin rhythm, Tyumen)
Маткапитал был, опека молчала: через три года дети оспорили сделку в Тюмени

## slug suggestion
matkapital-opieka-det-i-osporili-sdelku-tyumen

## Klyshin
- hook_id: matkapital_child_shares
- original hook: «маткапитал и детские доли»
- angle: родители использовали маткапитал, детям доли формально не выделили; опека не зафиксировала нарушение; покупатель думал, что «всё давно закрыто»; через три года выросшие дети оспорили сделку — суд отменил регистрацию
- signal post: https://t.me/klyshin_A — видео «5 схем, из-за которых забирают квартиру» (п.4 Маткапитал: «родители использовали маткапитал, но детей долями не наделили; дети выросли и начали сами оспаривать сделки») + пост про проверку перед покупкой (маткапитал в списке 10 рисков)

## Wordstat (MCP-KV live, conductor verified)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes regions 55+11176:
- «маткапитал при покупке квартиры» → 19 (RU225 compare 1927)
- «детская доля в квартире» → 35
- «продажа детских долей в квартире» → 10
- «выделение детских долей в квартире» → 5

Rework (news phrasing, NOT checklist):
- hook weak locally → buyer jargon «детские доли» + «маткапитал»
- «вторичка в тюмени» → 6068 (RU225 compare 10044)
- buyer spine «купить квартиру в тюмени» → 22833 (RU225 40089)

Final P0: «вторичка в тюмени» 6068

## dzen_casus_shape PASS
- event: покупка квартиры в Тюмени, продавцы использовали маткапитал годы назад
- risk: детские доли не выделены; опека не зафиксировала; в выписке «тишина»
- time: «через три года» после регистрации
- finale: дети оспорили сделку — суд отменил регистрацию права

## comment_magnet_angle
«Если маткапитал был, а в выписке долей детей нет — вы останавливаете сделку или верите словам продавца „уже всё оформили“?»

## scout_helper
PASS 2026-08-26 — NO CANNIBALIZATION RISK, TOPIC FOCUS PASS, STORY DUP PASS
Rejected matkapital angle «доли не видели в выписке» — overlap LIVE-NA-MATKAPITAL-KUPILI-DET (live WP). Chosen distinct plot: опека молчала + дети оспорили через 3 года.

## Rejected candidates (note)
- summons_registration_stop — dup live WP «аванс внесли — повестка остановила»
- tired_buyer_bad_flat — dup live WP «4 месяца искали / согласились на риск»
- matkapital «доли в выписке не было» — STORY DUPLICATE live WP cluster

## signal_urls
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://t.me/holyslav92

## Author / city
Святослав Шакин, Тюмень (локализация, не копипаст Клышина)

## Anti-dup note
Не пересекается с B02–B10 ledger clusters. Отличие от live WP matkapital: не «доли не видели в выписке при покупке», а «опека молчала → дети оспорили через 3 года».
