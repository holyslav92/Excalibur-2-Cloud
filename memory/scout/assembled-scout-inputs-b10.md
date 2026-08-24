# Scout inputs — B10 (2026-08-24)

## INSTRUCTION FOR DEROUTER (READ FIRST)
You are invoked **via** `excalibur_blog_derouter_opus_chat.py`. The Cursor conductor **already ran**:
- wordstat_get_user_info OK
- live Wordstat probes (MCP-KV)
- scout_helper --check-query PASS
- signal fetch klyshin_A + dzen holyslav

**Your ONLY task:** write the final Scout handoff markdown (Russian prose + mandatory gate lines). Do NOT refuse for missing shell/MCP. Do NOT ask to run scripts. Output the handoff body now.

## Assignment
topic_id: B10
publish_format: longform
tenant: The Риэлтор / Святослав Шакин / Тюмень
run_date: 2026-08-24 MSK

## Triple gate decision
Selected hook: **five_court_schemes** → sub-angle **быстрый переход права / flip** (схема №2 из видео Klyshin «5 схем»).

Rejected hooks (with reason):
- matkapital_child_shares — SCOUT STORY DUPLICATE vs live WP «на маткапитал купили детские доли»
- summons_registration_stop — overlap 38% with live WP avans+povestka (2026-08-24)
- phone_scammers_notary / notary court cancel — overlap 54–61% with live WP/Dzen «нотarius udostoveril, sud otmenil» (phone scammers casus already published today)
- notary_not_shield_70k — overlap 54% with in_pool LIVE-NOTARIUS +70k
- elderly_pnd_serbsky — duplicate WP babushka osmotr (2026-08-23)
- pre_advance_check — B01 ledger hook; Klyshin fresh post overlaps B07 inheritance cluster

## Title draft (news headline, Klyshin rhythm)
**H1:** В выписке всё чисто — а продавец владел квартирой три месяца: через полгода финуправляющий оспорил сделку

**slug:** prodavets-vladel-tri-mesyaca-sdelku-osporili

**article_dir (research_start):** memory/blog/articles/B10-prodavets-vladel-tri-mesyaca-sdelku-osporili

## Klyshin hook
klyshin_hook_id: five_court_schemes
original: «5 схем — квартиру забирают судом после покупки» → angle: **быстрый переход права / флип**
signal_post: https://t.me/klyshin_A — видео-разбор 5 схем (август 2026): «Квартиру купили недавно и уже снова продают. Иногда флиппер. А иногда человек понял, что купил проблему и пытается быстро перекинуть дальше.»
secondary_signal: пост про горячую вторичку + «Сначала проверка. Потом аванс.» (контекст спешки покупателей)

## External signals (today)
1. https://t.me/klyshin_A — 5 схем + горячая вторичка
2. https://dzen.ru/holyslav — канал holyslav (Tyumen casus champion formula)
3. https://t.me/holyslav92

## Published siblings — DO NOT duplicate plot
B02 receipt_no_money, B03 deposit_before_auction, B04 doverennost_svo, B05 discount_2m+grandma, B06 auto appraisal, B07 inheritance son first marriage, B08 dead wife share, B09 mortgage EGRN cancelled registration

Live WP 2026-08-24: notarius+sud otmenil (phone scammers), avans+povestka stop

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

## Wordstat rework log (live MCP-KV, regions 55+11176, compare 225)
wordstat_rework:
- probe «проверка квартиры перед покупкой» **8** (55+11176)
- probe «банкротство продавца квартиры» **28** (55+11176)
- rework «купить квартиру в тюмени вторичка» **3996** (55+11176)
- final P0 «купить квартиру в тюмени» **22660** (55+11176) | RU225 **39961**
- sticker cluster: «банкротство продавца квартиры» 28; «купить квартиру в тюмени вторичка» 3996

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 22660 | RU225 39961 | secondary «купить квартиру в тюмени вторичка» 3996 | risk «банкротство продавца квартиры» 28

## Dzen news-casus shape
dzen_casus_shape: PASS
- event: покупатель в Тюмени купил вторичку, выписка ЕГРН без запретов, расчёт прошёл
- risk: продавец владел объектом ~3 месяца (быстрый переход права / возможный флип / предбанкрот)
- time: «через полгода после регистрации»
- finale: финансовый управляющий оспорил сделку как подозрительную/фиктивную цепочку
- hero thought safe: «выписка чистая — значит можно»

comment_magnet_angle: «Три месяца владения продавца — для вас стоп-сигнал или „на рынке так принято“?»

## scout_helper result
python3 scripts/excalibur_blog_scout_helper.py --check-query "В выписке всё чисто — продавец владел квартирой три месяца: через полгода финуправляющий оспорил сделку five_court_schemes flip prodavets-vladel-tri-mesyaca-sdelku-osporili"
→ NO CANNIBALIZATION RISK, TOPIC FOCUS PASS

## RF/Dzen
dzen_rf_pack: read shared/dzen-content-rules.md + rf-blocked-entities.json — PASS (no DENY heroes)

## Writer notes
Facts/city: Святослав Шакин / Тюмень (не копипаст Klyshin Москва).
Champion arc: прозаический лид 4–6 предложений → early TG+MAX → хронология → финал суда → практика после → comment magnet.
Interlink: 2–4 sibling from shared/published-articles.md.
