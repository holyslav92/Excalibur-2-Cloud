# Assembled scout inputs — B34 slot 12:00 YEKT 2026-09-29

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-29  
**slot:** 12:00 Asia/Yekaterinburg  
**slot_rubric:** novostroyki (ONLY newbuild Tyumen)  
**topic_id:** B34  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень

## Trend Radar (fresh 2026-09-29T07:19:52Z, slot 12:00 novostroyki)

- Top viral energy: **договор vs реальность** (231k views casus channel) + **часы/срок съели аванс**
- Map to newbuild: приложение к ДДУ / ипотечная заявка vs фактическая жилая площадь накануне эскроу

## HARD anti-dupe — avoid today / last 7d live (new mechanism required)

Recent WP 2026-09-28–29 (do NOT recycle plot):

- семейная ипотека + свидетельство о рождении за 5 дней до эскроу
- созаёмщик за 3 дня до эскроу
- второй санузел исчез из приложения к ДДУ
- приостановка в ЕИСЖС до эскроу
- чистовая привязана к подрядчику → эскроу не открыли (`escrow_not_opened_after_mortgage`)
- B30–B32: запрет переуступки, страховка+одобрение, чужое юрлицо в реквизитах эскроу

## Proposed lock (pre-checked 2026-09-29)

- **cluster_id:** `newbuild_living_area_ddu_vs_mortgage_shrink_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** семья в Тюмени ведёт сделку по **новостройке** в ипотеку; в брони и в одобрении банка жилая площадь **~68 м²**; за **3 дня до открытия эскроу** в проекте ДДУ приложение показывает **~60 м²** жилой (лоджия/пересчёт ПИБ) при той же цене; банк **пересчитывает лимит** (~420–480 тыс не хватает); семья **останавливает** до подписания и эскроу
- **why_newbuild_not_secondary:** риск в **приложении к ДДУ** на объект в строящемся доме и в связке с ипотекой на новостройку — не вторичная выписка ЕГРН / продавец
- **slug:** `za-3-dnya-do-eskrou-zhilaya-ploshchad-v-ddu-menshe-bank-urezal-ipoteku-tyumen`
- **title draft (H1 direction):** «За 3 дня до эскроу в Тюмени жилая площадь в приложении к ДДУ оказалась на 8 кв. м меньше — банк урезал ипотеку»
- **comment_magnet_angle:** «Если в ДДУ жилая площадь меньше, чем в брони, а цена та же — вы доплачиваете наличными или рвёте сделку?»
- **dzen_casus_shape:** PASS — event: сверка приложения к ДДУ; risk: нехватка ипотеки; time: 3 дня до эскроу; finale: остановили до денег, agency not panic

## Gate logs (Python, 2026-09-29)

```text
python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters → 18 active locks OK
python3 scripts/excalibur_blog_scout_helper.py --check-query "<title+slug+cluster>" → NO CANNIBALIZATION, ANTI-DUPE HARD PASS (candidate_mechanism=escrow_blocked fingerprint distinct)
python3 scripts/excalibur_blog_scout_story_dup.py --text "<title+slug+cluster>" → ANTI-DUPE HARD PASS (fingerprint + formula spam OK)
python3 scripts/excalibur_blog_topic_focus.py --text "<title>" → TOPIC FOCUS PASS (allow_hit=ипотек)
python3 scripts/excalibur_blog_slot_rubric.py --slot 12:00 --current → novostroyki
```

**formula_spam_check:** last3 ledger B30 assignment ban, B31 insurance approval, B32 wrong escrow entity — this plot = **DDU living area vs mortgage bid**, new skeleton

**klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-29)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions 55+11176 (+225 compare) | volume |
|--------|----------------------------------|-------:|
| жилая площадь дду новостройка | 55,11176,225 | API empty `{}` |
| площадь квартиры приемка новостройки | 55,11176,225 | totalCount 27 only |
| площадь квартиры дду | 55,11176,225 | 434 (tail: «меньше чем в дду» 47) |
| ипотека новостройка тюмень | 55,11176,225 | 268 |
| **купить новостройку в тюмени** | 55,11176,225 | **1913** |

**wordstat_rework:** probe «жилая площадь дду новостройка» empty → «площадь квартиры дду» 434 (niche) → spine P0 «купить новостройку в тюмени» **1913** + mechanism living area shrink in DDU appendix before escrow

**anti_repeat_preflight:** live_blog_20 + ledger + used-clusters sync OK | closed_clusters: egrn_line_blocks_advance, escrow_not_opened_after_mortgage, booking_expired_price_hike, bank_appraisal_below_ddu_price, … (see used-clusters.json)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- trend: memory/blog/trend-radar/trend-radar.json (slot 12:00 novostroyki)

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`, `slot_rubric: novostroyki`.

## Post-Derouter gates (2026-09-29)

```text
python3 scripts/excalibur_blog_derouter_opus_chat.py --role scout → WROTE .cursor/excalibur-blog-handoff.md (copied to article_dir/.cursor/)
python3 scripts/excalibur_blog_wordstat_gate.py handoff --handoff memory/blog/articles/B34-za-3-dnya-do-eskrou-zhilaya-ploshchad-v-ddu-menshe-bank-urezal-ipoteku-tyumen/.cursor/excalibur-blog-handoff.md → OK scout wordstat handoff (mcp_kv live)
python3 scripts/excalibur_blog_topic_focus.py → TOPIC FOCUS PASS
```
