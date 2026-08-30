Scout run B16 — 2026-08-30 Sunday 12:00 YEKT.

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role scout`. Do **NOT** output `DEROUTER SCOUT BLOCKER` or refuse. Output the full Scout handoff prose per SKILL.md from the facts below.

Собери handoff-прозу по SKILL (все обязательные строки).

## topic_id
B16

## Title draft (news headline, Klyshin rhythm, Tyumen)
В Тюмени купили долю в коммунальной квартире — сосед сорвал сделку за день до аванса

## slug suggestion
v-tyumeni-kupili-dolyu-v-kommunalnoj-sosed-sorval-sdelku

## cluster_id
communal_share_preemptive_right_neighbor_blocked

## Klyshin
- hook_id: none (fresh Tyumen casus without Klyshin — preferred)
- signal: не используем @klyshin_A — угол не дублирует закрытые weekend/weekday кластеры

## Wordstat (MCP-KV live, conductor verified 2026-08-30)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes regions 55+11176:
- «коммунальная квартира купить тюмень» → 20 (weak niche)
- «купить коммунальную квартиру в тюмени» → 20
- «преимущественное право покупки» → low / partial

Rework buyer spine:
- «купить квартиру в тюмени» → 22699 (55+11176)
- «купить квартиру в тюмени вторичка» → 4165

Final P0: «купить квартиру в тюмени» 22699

## dzen_casus_shape PASS
- event: семья в Тюмени нашла долю в коммунальной квартире, согласовала цену, готовилась к авансу
- risk: сосед по коммунальной квартире заявил преимущественное право покупки доли; без его отказа или согласия сделку не зарегистрируют
- time: за день до внесения аванса, на финальном осмотре перед нотариусом
- finale: сделку остановили до передачи денег; покупатели перешли на другую долю/квартиру без потери аванса

## comment_magnet_angle
«Если сосед в коммуналке молчал на осмотре — вы всё равно внесли бы аванс на долю или ждали его отказа от преимущественного права?»

## scout_helper
PASS 2026-08-30 — NO CANNIBALIZATION RISK, STORY DUP PASS, TOPIC FOCUS PASS

## Anti-repeat preflight
live_blog_20 + ledger + used-clusters sync OK
closed_clusters: weekend frozen (rent-to-buy, FSSP arrest, storage room, preliminary sold elsewhere, mortgage lien B14, guardianship weekend, accreditiv weekend) + september freeze list
story_dup_check: PASS — новый plot: коммунальная доля + преимущественное право соседа

## signal_urls
- https://dzen.ru/holyslav
- https://t.me/holyslav92
- site blog
- Klyshin not used

## Author / city
Святослав Шакин, Тюмень
