# Scout inputs — 2026-09-30 slot 12:00 YEKT (B34)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-30  
**slot:** 12:00 Asia/Yekaterinburg  
**slot_rubric:** novostroyki  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)  
**topic_market_focus:** newbuild_only  
**dzen_rf_pack:** true  

## Trend Radar (fresh)

- `memory/blog/trend-radar/trend-radar.json` generated_at 2026-09-30T07:11:46Z, slot_local 12:00, slot_rubric novostroyki  
- novostroyki energy: «договор vs реальность» (declaration/booking vs fact)  
- vtorichka top energy mirror (not plot): almost_lost перед ключами/деньгами → translate to newbuild ONLY  

## Slot constraints (HARD FORBIDDEN)

- NO today live WP: приёмка промёрзшая стена / ключи через 40 дней (acceptance frozen wall — do not retitle)  
- NO last-3 published skeleton «за N дней до эскроу/ДДУ» countdown formulas (area cut, birth cert, co-borrower, finishing contractor, second bathroom, EISZHS stop, etc.)  
- NO keys_delay / acceptance_defects / booking_expired_price_hike / escrow_not_opened / ddu_apartment mismatch clusters (see used-clusters.json)  
- NO frozen secondary retitles  
- NO Meta/Instagram heroes (rf-blocked)  

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 15 active locks (2026-09-30)  
- Live WP ~20 reviewed via excalibur_blog_today.py + EXCALIBUR_RECENT_WP_POSTS  
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug  
- `excalibur_blog_topic_focus.py` PASS (новостройке, брони, ДДУ, застройщик context)  
- `story_dup.py --text` PASS  

## Proposed topic (PASS)

- **topic_id:** B34  
- **title_draft:** В новостройке Тюмени в брони обещали двор без машин — в проекте появился проезд, семья остановила ДДУ  
- **slug:** v-tyumeni-v-novostrojke-v-broni-obeschali-dvor-bez-mashin-v-proekte-poyavilsya-proezd  
- **article_dir:** memory/blog/articles/B34-v-tyumeni-v-novostrojke-v-broni-obeschali-dvor-bez-mashin-v-proekte-poyavilsya-proezd  
- **cluster_id (new):** newbuild_master_plan_driveway_added_tyumen  
- **top_energy_mirror:** paper_clean_then_broke  
- **viral_mechanism (trend):** договор vs реальность — маркетинг брони vs актуальный проект/генплан  
- **newbuild_mechanism:** Семья с детьми выбирает квартиру в жилом комплексе в Тюмени: в брони и на стенде менеджер зафиксировал «двор без машин / детская площадка во дворе». За 5 дней до подписания ДДУ открыли обновлённый раздел проекта на сайте застройщика и в проектной декларации — во дворе появился **проезд для пожарных и сервисных машин** (ширина 6 м), парковочные места у подъезда. Семья отказалась подписывать ДДУ, бронь частично удержали, на эскроу не вышли  
- **why_newbuild_not_secondary:** Цепочка только новостройки: бронь застройщика, проектная декларация 214-ФЗ, ДДУ, эскроу. Нет продавца вторички, ЕГРН-сделки, дарственной, опеки, бабушки, банкротства продавца  
- **story_dup_check:** PASS — не приёмка/дефекты (сегодняшняя промёрзшая стена), не перенос срока ключей (keys_delay), не смена секции/цены в брони (booking_expired_price_hike), не земля в аренде (B27)  

## Dzen news-casus shape (PASS)

- **event:** семья с двумя детьми выбрала квартиру во дворе «без машин»; в брони менеджер отметил «тихий двор, детская зона»  
- **risk:** шум, безопасность детей, просадка цены при перепродаже; ипотека одобрена под «семейную» квартиру с двором  
- **time:** за 5 дней до назначенного подписания ДДУ; вечером перед визитом в офис застройщика увидели обновление генплана  
- **finale:** в проекте появился проезд и парковка у подъезда; застройщик сказал «подпишите ДДУ, это служебный проезд»; семья отказалась; из брони 150 тыс. вернули 90 тыс., ДДУ не подписали  
- **comment_magnet_angle:** «Если во дворе внезапно появляется проезд, а бронь уже оплачена — вы бы подписали ДДУ, чтобы не потерять квартиру, или разорвали бы бронь?»  

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen newbuild casus without Klyshin)  

## Wordstat MCP-KV (live 2026-09-30)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|-----:|
| бронь новостройка тюмень | 55,11176 | empty/<5 |
| дду новостройка | 55,11176 | 17 |
| материнский капитал новостройка | 55,11176 | 8 |
| купить новостройку в тюмени | 55,11176 | 900 |
| новостройки тюмень | 55,11176 | 4325 |
| новостройки тюмень | 55,11176,225 compare | 8295 (RU context) |

**wordstat_rework:** probe «бронь новостройка тюмень» empty → «дду новостройка» 17 (weak) → «материнский капитал новостройка» 8 (weak, wrong mechanism) → rework buyer spine **«купить новостройку в тюмени»** 900 + H1 keeps бронь/ДДУ/двор mechanism  

**final P0:** «новостройки тюмень» regions 55,11176 freq **4325** (compare RU «новостройки тюмень» 8295 with 225)  

## signal_urls (research)

- https://dzen.ru/holyslav  
- https://www.domrf.ru/ — проектные декларации, изменения проекта  
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ  
- https://t.me/Tyumen_Rieltor  
- Site blog listing (anti-dup only)  

## Output required

Write complete Scout handoff markdown per SKILL.md with: slot_rubric novostroyki, viral_mechanism, wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS, comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id newbuild_master_plan_driveway_added_tyumen, h1_fingerprint_check PASS, formula_spam_check PASS (last3 not escrow-countdown), anti_dupe_hard: PASS.

Lock topic_id B34, title, slug, article_dir.
