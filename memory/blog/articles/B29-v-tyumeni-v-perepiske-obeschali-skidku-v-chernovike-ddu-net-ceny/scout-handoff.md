```markdown
# Excalibur Blog Scout Handoff — B29

topic_id: B29
tenant: The Риэлтор / Святослав Шакин, Тюмень
slot: 2026-09-19 ~15:00 YEKT
topic_market_focus: newbuild_only

## Topic lock

title_draft: В Тюмени в переписке обещали скидку 4% — в черновике ДДУ полной цены не было
slug: v-tyumeni-v-perepiske-obeschali-skidku-v-chernovike-ddu-net-ceny
cluster_id: newbuild_crm_promo_discount_not_in_ddu_draft

top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: акция/скидка в CRM и переписке с менеджером не попала в проект ДДУ; семья остановилась за 3 дня до открытия эскроу
why_newbuild_not_secondary: покупка квартиры в строящемся ЖК по ДДУ 214-ФЗ, эскроу и ипотека — не сделка с продавцом вторички

klyshin_hook: none | original: none (Klyshin not used)
signal_urls:
  - PUBLIC_SITE_URL/blog/ — anti-dup titles only
  - Klyshin: none

## News-casus shape

dzen_casus_shape: PASS
event: семья получила проект ДДУ, в котором обещанная в переписке скидка 4% не была отражена; цена в документе оказалась полной
risk: переплата ориентировочно 580–620 тыс. рублей и возможная потеря брони
time: до открытия эскроу оставалось 3 дня
finale: покупатели остановили сделку и не открывали эскроу

comment_magnet_angle: «Скрин переписки со скидкой — это обещание застройщика или просто реклама?»

## Wordstat

wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework: probe «скидка застройщик новостройка» 3 → слабый промо-запрос → buyer-demand anchor «купить новостройку в тюмени» 920

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4430 (11176); «купить новостройку в тюмени» 920; compare225 «новостройки тюмень» 8321

wordstat_probes:
  - query: «скидка застройщик новостройка»
    regions: 55 + 11176
    frequency: 3
    result: weak; not used as final P0
  - query: «новостройки тюмень»
    region_55: 3502
    region_11176: 4430
    region_225: 8321
  - query: «купить новостройку в тюмени»
    regions: 55 + 11176
    frequency: 920
    region_225: 1917
    result: final buyer-demand P0

final_p0: «купить новостройку в тюмени»
final_p0_frequency: 920
final_p0_regions: Тюмень 55 + Тюменская область 11176
final_p0_ru_compare: 1917, RU 225

## Anti-repeat and gates

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
closed_clusters:
  - booking_expired_price_hike
  - trade_in
  - installment
  - assignment
  - declaration-heavy KP plots today
  - B27: земля аренда ЖК
  - B28: газ КП
  - потолки КП −25 см
  - семейная ипотека 7 лет ребёнку

story_dup_check: PASS
story_dup_basis: cluster is not present in the closed 30-day list; no same-story retitle detected
story_dup_cluster_id: newbuild_crm_promo_discount_not_in_ddu_draft

h1_fingerprint_check: PASS
fingerprint: скидка-в-переписке-не-в-проекте-ДДУ

formula_spam_check: PASS
last3_mechanisms: не повторяются; текущий механизм — несоответствие CRM/переписки и проекта ДДУ

anti_dupe_hard: PASS

scout_helper_check: ANTI-DUPE HARD PASS, TOPIC FOCUS PASS
topic_focus_check: PASS
scout_story_dup_check: PASS fingerprint + formula

## Editorial lock

market_lock: ONLY newbuild
property_type: квартира в строящемся ЖК
transaction_mechanism: ДДУ по 214-ФЗ, ипотека, эскроу
audience:
  - семьи с детьми
  - покупатели первой квартиры
  - инвесторы, оценивающие скидки и финальную цену входа

forbidden_reframe:
  - не переводить сюжет во вторичку
  - не делать спокойный чек-лист или универсальный гайд
  - не заменять казус историей о чистой ЕГРН, банкротстве продавца, опеке или маткапитале во вторичке
  - не утверждать, что переписка автоматически доказывает наличие скидки
  - не выдавать ориентировочную сумму переплаты за установленный юридический ущерб без подтверждающих документов

editorial_angle: покупатель остановил сделку в последний момент, потому что рекламная скидка из переписки не совпала с ценой в проекте ДДУ; спор — достаточно ли цифрового обещания менеджера, если в договоре стоит другая сумма

conversion_intent: консультация перед покупкой новостройки в Тюмени; проверка цены, скидки, проекта ДДУ и условий открытия эскроу

## Required handoff summary

wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: «акция/скидка в CRM и переписке с менеджером не попала в проект ДДУ; семья остановилась за 3 дня до открытия эскроу»
why_newbuild_not_secondary: «покупка квартиры в строящемся ЖК по ДДУ 214-ФЗ, эскроу и ипотека — не сделка с продавцом вторички»
klyshin_hook: none | original: none (Klyshin not used)
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: booking_expired_price_hike, trade_in, installment, assignment, declaration-heavy KP plots today, B27 земля аренда ЖК, B28 газ КП, потолки КП −25 см, семейная ипотека 7 лет ребёнку
dzen_casus_shape: PASS | event: «получили черновик ДДУ без скидки» | risk: «переплата около 580–620 тыс. рублей и потеря брони» | time: «за 3 дня до открытия эскроу» | finale: «сделку остановили, эскроу не открывали»
comment_magnet_angle: «Скрин переписки со скидкой — это обещание застройщика или просто реклама?»
wordstat_rework: probe «скидка застройщик новостройка» 3 → buyer-demand anchor → final P0 «купить новостройку в тюмени» 920
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 920
story_dup_check: PASS | cluster_id: newbuild_crm_promo_discount_not_in_ddu_draft
h1_fingerprint_check: PASS | fingerprint: скидка-в-переписке-не-в-проекте-ДДУ
formula_spam_check: PASS | last3_mechanisms: current mechanism is distinct from the last three
anti_dupe_hard: PASS
```
