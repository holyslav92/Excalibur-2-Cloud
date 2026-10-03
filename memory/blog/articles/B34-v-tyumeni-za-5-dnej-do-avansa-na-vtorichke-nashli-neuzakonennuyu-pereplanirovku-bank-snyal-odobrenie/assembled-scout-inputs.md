# Scout inputs — 2026-10-03 slot 15:00 YEKT (vtorichka)

**CRITICAL:** You run inside `excalibur_blog_derouter_opus_chat.py` (utility gpt-5.6-terra). Write the full Scout handoff markdown body only — no tool calls, no BLOCKER refusals.

**run_date:** 2026-10-03  
**slot_local:** 15:00  
**slot_rubric:** vtorichka  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)  
**dzen_rf_pack:** true  
**topic_market_focus:** rubric_per_slot (vtorichka ONLY — no newbuild mechanisms)

## Trend Radar (memory/blog/trend-radar/trend-radar.json)

- **viral_mechanism (vtorichka):** almost lost перед ключами/деньгами  
- **energy mirror:** paper_clean_then_broke — «на осмотре всё красиво», на техпаспорте/сверке с БТИ другое  
- Do NOT glue unrelated calendar «семейная ипотека 1 октября» unless it is the H1 mechanism (it is NOT).

## Anti-repeat preflight (DONE)

- `excalibur_blog_scout_story_dup.py --sync-used-clusters` OK  
- Live WP recent vtorichka: B33 utility electricity debt; rental on Avito; agreed price stolen; family mortgage Oct 1; bankruptcy seller; bailiff ban  
- **FORBIDDEN:** repeat B33 utility/JKU debt cluster; frozen clusters in memory/scout/used-clusters.json  
- `excalibur_blog_topic_focus.py` PASS (аванс, вторичка)  
- `excalibur_blog_scout_story_dup.py --text` PASS fingerprint+formula  
- `scout_helper.py --check-query` warnings only (no hard cluster duplicate)

## Proposed topic (LOCK)

- **topic_id:** B34  
- **title_draft:** В Тюмени за 5 дней до аванса на вторичке нашли неузаконенную перепланировку — банк снял одобрение  
- **slug:** v-tyumeni-za-5-dnej-do-avansa-na-vtorichke-nashli-neuzakonennuyu-pereplanirovku-bank-snyal-odobrenie  
- **article_dir:** memory/blog/articles/B34-v-tyumeni-za-5-dnej-do-avansa-na-vtorichke-nashli-neuzakonennuyu-pereplanirovku-bank-snyal-odobrenie  
- **cluster_id (new):** secondary_illegal_redevelopment_bti_mismatch_tyumen  
- **vtorichka_mechanism:** Покупатели согласовали цену на трёшку на вторичке в Тюмени, ипотека одобрена. На повторном осмотре с замерщиком/риэлтором заметили: кухня и гостиная слились в одно помещение, дверной проём в несущей стене зашит. В техпаспорте БТИ план **другой**. Продавец: «так живут все, узаконим после». За **5 дней** до аванса банк после запроса техпаспорта **снял одобрение** — риск отказа регистрации и требования привести в соответствие. Семья **не внесла аванс**.  
- **why_not_other_clusters:** не долг ЖКУ/свет (B33), не аренда на Авито, не банкрот, не пристав, не семейная ипотека-пересчёт — механика **перепланировка/БТИ vs факт**.

## Dzen news-casus shape (PASS)

- **event:** семья с ипотекой выбирает трёшку; на первом показе ремонт «евро», стены снесены визуально  
- **risk:** неузаконенная перепланировка → отказ Росреестра, штрафы, принудительный демонтаж; банк не выдаст/не зарегистрирует залог  
- **time:** за 5 дней до планового аванса; вечером после повторного замера  
- **finale:** банк снял одобрение; продавец предлагал «скинем 200 тысяч, узаконим сами» — покупатели отказались; аванс не вносили  
- **comment_magnet_angle:** «Если на вторичке ремонт красивый, а в БТИ план старый — вы бы внесли аванс под обещание «узаконим потом» или остановили сделку?»

## Klyshin

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-10-03)

**Preflight:** wordstat_get_user_info OK

| probe | regions | freq |
|-------|---------|-----:|
| вторичка в тюмени | 55,11176 | 5459 |
| купить квартиру в тюмени вторичка | 55,11176 | 3348 |
| неузаконенная перепланировка квартиры | 55,11176 | 13 |
| покупка квартиры с неузаконенной перепланировкой | 55,11176 | 2 |
| вторичка в тюмени | 225 compare | 9750 |

**wordstat_rework:** weak niche probes on перепланировка → anchor P0 buyer spine «вторичка в тюмени» + mechanism in H1/body  
**final P0:** «вторичка в тюмени» regions 55,11176,compare225 freq 5459 / RU 9750

## Handoff footer (include verbatim fields)

wordstat_preflight: mcp-kv wordstat_get_user_info OK  
slot_rubric: vtorichka  
viral_mechanism: almost lost перед ключами/деньгами  
dzen_casus_shape: PASS  
comment_magnet_angle: (see above)  
anti_dupe_hard: PASS  
story_dup_check: PASS | cluster_id: secondary_illegal_redevelopment_bti_mismatch_tyumen  
h1_fingerprint_check: PASS  
formula_spam_check: PASS  
wordstat: mcp_kv live | P0 «вторичка в тюмени» 5459 (55+11176)
