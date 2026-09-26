# Assembled scout inputs — B33 slot 12 YEKT 2026-09-26 (Saturday owner/cron run)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-26  
**slot:** 12:00 Asia/Yekaterinburg  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (avoid recent live 2026-09-25–26)

Do NOT reuse: бронь сгорела/скидка/площадь в акте/лоджия/паркинг/КП сотки/переуступка запрет resale 3y (B30)/эскроу чужое юрлицо (B32)/страховка ипотека (B31)/маткапитал эскроу.

## Proposed lock (pre-checked 2026-09-26)

- **cluster_id:** `newbuild_ddu_rental_ban_investor_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** инвестор/семья берёт квартиру в тюменской новостройке под сдачу; бронь и ипотека согласованы; за **3 дня до эскроу** в проекте ДДУ всплывает пункт: **запрет сдачи в аренду 24 месяца** / только «личное проживание» / штраф за «коммерческое использование» — в переписке с ОП этого не было; покупатель останавливается **до подписания и до эскроу**; на кону бронь ~50–80 тыс + время одобрения
- **why_newbuild_not_secondary:** ограничения в **ДДУ застройщика** на объект в строящемся доме, не вторичка/ЕГРН-продавец
- **title draft (H1 direction):** «В проекте ДДУ в тюменской новостройке всплыл запрет сдавать квартиру 2 года — инвестор остановился за 3 дня до эскроу»
- **comment_magnet_angle:** «Если в ДДУ пишут «нельзя сдавать 2 года» — вы всё равно подписываете ради ставки или ищете другой ЖК?»
- **scout_helper.py --check-query:** PASS 2026-09-26 (anti_dupe_hard PASS, topic focus PASS)
- **formula_spam_check:** last live posts heavy on booking/bron changes — this is **DDU rental restriction / investor exit**, distinct skeleton

## Wordstat MCP-KV (live 2026-09-26)

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| купить новостройку в тюмени | 55,11176 | 892 |
| купить новостройку в тюмени от застройщика | 55,11176 | 422 |
| новостройки тюмень | 55,11176 | (probe via spine) |
| рассрочка от застройщика тюмень | 55,11176 | 128 |

**wordstat_rework:** spine P0 «купить новостройку в тюмени» 892 + mechanism DDU rental ban for investors

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: investor/family on Tyumen newbuild purchase for rental income
- risk: hidden rental ban clause in DDU draft
- time: 3 days before escrow signing
- finale: stopped before escrow; agency on what to read in DDU project + booking chat before fee

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
