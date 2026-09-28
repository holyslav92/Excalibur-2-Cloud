# Scout inputs — weekend slot 17 YEKT 2026-09-26

run_date: 2026-09-26
slot: 17:00 Asia/Yekaterinburg (owner weekend request)

## Same-day angle check (avoid collision with 09/12/15 today)
Already published 2026-09-26: parking lgoty before keys; KP house 1h booking cancel; loggia→balcony; discount 380k; layout 54→49 m²; act area vs DDU.
This pick: **lift technical inspection blocks keys** — NOT used today.

## Handoff

wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: clock_ran_out
newbuild_mechanism: «За 3 дня до выдачи ключей в тюменской новостройке лифт не прошёл технадзор — заселение остановили, семья одновременно платит ипотеку и аренду»
why_newbuild_not_secondary: «Сюжет только про ввод дома и приёмку лифта в ЖК от застройщика по ДДУ/214-ФЗ, не про осмотр вторички»
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
dzen_casus_shape: PASS | event: «вызвали на ключи» | risk: «лифт не допущен к эксплуатации» | time: «за 3 дня до даты в уведомлении» | finale: «договорились о переносе + проверка документов на лифт»
comment_magnet_angle: «Согласны ли вы заходить в новостройку, если лифт формально не сдан?»
wordstat_rework: probe «купить квартиру в новостройке тюмень» 625 → probe «квартиры с ремонтом от застройщика тюмень» 319 → final P0 «квартира в тюмени купить новостройки» 625
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартира в тюмени купить новостройки» 625
story_dup_check: PASS | cluster_id: newbuild_elevator_technical_inspection_blocked_keys_tyumen
h1_fingerprint_check: PASS | fingerprint: keys_delay_penalty:elevator_technical_inspection
formula_spam_check: PASS | last3_mechanisms: booking_expired (today) — candidate keys_delay_penalty/elevator, distinct
anti_dupe_hard: PASS

title_draft: В тюменской новостройке за 3 дня до ключей лифт не прошёл технадзор — семья платит ипотеку и аренду
topic_id: B33
