# Assembled scout inputs — B34 slot 15:00 YEKT 2026-10-01

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only. No BLOCKER.

**run_date:** 2026-10-01  
**slot:** 15:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka  
**topic_market_focus:** rubric_per_slot  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)  
**dzen_rf_pack:** true  

## Trend Radar (memory/blog/trend-radar/trend-radar.json, 2026-10-01)

- **viral_mechanism (vtorichka):** almost lost перед ключами/деньгами  
- **energy mirror:** «С 1 октября вырастет спрос на вторичную недвижимость…» (Life, score 8.53) — calendar hook **не** клеить как сюжет; механика = почти потеряли сделку на финишной прямой  
- **klyshin_hook:** none  

## Anti-repeat preflight (DONE 2026-10-01)

- `excalibur_blog_scout_story_dup.py --sync-used-clusters`  
- Live WP recent: банкрот продавца, пристав, долг за свет B33, дарственная, аренда в ЕГРН, новостройки эскроу/ДДУ сегодня — **не** повторять  
- **NO** egrn_line_blocks_advance / renta / ипотечное обременение (B09 lock)  
- **NO** matkapital kids shares cancel (frozen cluster) — сюжет **подопечная-продавец**, не детские доли  

## Proposed topic (PASS)

- **topic_id:** B34  
- **title_draft:** За 5 дней до аванса в Тюмени органы опеки отказали в сделке с подопечной — семья не внесла аванс  
- **slug:** za-5-dnej-do-avansa-v-tyumeni-organy-opeki-otkazali-v-sdelke-s-podopechnoj-semya-ne-vnesla-avanс  
- **article_dir:** memory/blog/articles/B34-za-5-dnej-do-avansa-v-tyumeni-organy-opeki-otkazali-v-sdelke-s-podopechnoj-semya-ne-vnesla-avanс  
- **cluster_id:** secondary_guardianship_ward_seller_refusal_tyumen  
- **vtorichka_mechanism:** покупка вторички у продавца-подопечной (опекун на сделке); на словах «разрешение опеки уже есть»; за **5 дней** до аванса запрос официального согласия органов опеки → **отказ** (цена ниже оценки / не обеспечено альтернативное жильё подопечной); семья **не внесла аванс**, сделку остановили до ДКП  
- **why_vtorichka_not_novostroyki:** ДКП, аванс, ЕГРН, органы опеки при отчуждении жилья подопечного — не ДДУ/эскроу/застройщик  
- **scout_helper --check-query:** PASS 2026-10-01 (warnings only on formula skeleton)  
- **story_dup / anti_dupe_hard:** PASS  
- **topic_focus:** PASS (vtorichka slot)  

## Dzen news-casus shape: PASS

- **event:** семья с детьми выбирает двушку на вторичке в Тюмени, торг согласован, ипотека одобрена  
- **risk:** без согласия опеки сделка недействительна; аванс на счёт риэлтора/продавца = деньги в воздухе  
- **time:** 5 дней до планового аванса (~400 тыс ₽ composite)  
- **finale:** отказ опеки зафиксирован письмом; продавец/опекун давил «подпишем без бумаги» — семья **не внесла аванс**, agency: что запросить до аванса  
- **comment_magnet_angle:** «Если опекун говорит «разрешение есть», а письма из опеки нет — вы бы внесли аванс или ушли сразу?»  

## Wordstat MCP-KV (live 2026-10-01)

| phrase | regions | volume |
|--------|---------|-------:|
| опека при продаже квартиры | 55,11176 | 41 |
| купить квартиру в тюмени вторичка | 55,11176 | 3305 |
| вторичное жилье в тюмени | 55,11176 | 910 |
| опека при продаже квартиры | 225 compare | 2678 |

**wordstat_rework:** P0 spine «купить квартиру в тюмени вторичка» 3305 + механика отказа опеки в H1/теле  
**final P0:** купить квартиру в тюмени вторичка — regions 55+11176, freq 3305 (compare RU «опека при продаже квартиры» 2678)  

## Handoff flags

- slot_rubric: vtorichka  
- viral_mechanism: almost_lost_before_money  
- dzen_casus_shape: PASS  
- comment_magnet_angle: (см. выше)  
- anti_dupe_hard: PASS  
- klyshin_hook: none  

Output handoff with all Scout fields per SKILL.
