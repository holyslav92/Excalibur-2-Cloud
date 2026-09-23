# Scout assembled inputs — 2026-09-23 slot ~12:00 YEKT

## Preflight done
- doctor OK, setup complete
- used-clusters sync OK (27 locks)
- live WP recent titles read via excalibur_blog_today.py
- dzen_rf_pack: dzen-content-rules + rf-blocked read (no blocked heroes)
- newbuild focus lock + dzen-top-angle-newbuild-lock read

## Candidate LOCK (passed gates)

**Title draft:**
Под Тюменью в КП обещали лесополосу у участка — за 6 дней до ДДУ в кадастровом плане оказался забор соседа

**cluster_id:** `kp_plot_buffer_forest_promised_cadastre_neighbor_fence_before_ddu_tyumen`

**Mechanism:** семья покупает дом в коттеджном посёлке под Тюменью от застройщика; на визуализации и в буклете — «зелёный буфер / лесополоса» за задним двором; за 6 дней до подписания ДДУ на дом+землю запросили кадастровый план участка — граница с соседом уже с забором и сужением полосы; банк/нотариус предупредили о споре; семья остановила сделку до эскроу, бронь под угрозой.

**top_energy_mirror:** paper_clean_then_broke (на картинке «лес», в документе — чужой забор)

**why_newbuild_not_secondary:** только КП/ИЖС от застройщика, ДДУ на дом и землю, эскроу, проектная декларация посёлка — не вторичный участок с бабушкой/ЕГРН.

**comment_magnet_angle:** «Если у участка в КП на кадастре уже стоит забор соседа, вы бы подписали ДДУ “как есть” или снимали бронь?»

**klyshin_hook:** none

## Wordstat MCP-KV (live)
- wordstat_get_user_info: OK
- P0 probe final: «коттеджные поселки тюмень купить дом» — **44** (regions 55+11176)
- RU compare «купить дом в коттеджном поселке» — 4954 (region 225)
- rework: weak «остекление балкона новостройка» rejected; localized KP buyer spine retained

## Anti-dupe checks (PASS)
```
python3 scripts/excalibur_blog_scout_helper.py --check-query "..." → ANTI-DUPE HARD PASS
python3 scripts/excalibur_blog_scout_story_dup.py --text "..." → PASS
python3 scripts/excalibur_blog_topic_focus.py --text "..." → PASS
```

## Signal URLs (tenant)
- site blog, dzen holyslav — titles only anti-dup

Write full handoff per skill template to `.cursor/excalibur-blog-handoff.md` in article dir B33.
