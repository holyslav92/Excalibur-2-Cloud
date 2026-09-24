Assembled Title inputs — B33 — 2026-09-24

You ARE inside `excalibur_blog_derouter_opus_chat.py --role title`. Output **only** valid JSON for `title-brief.json` per SKILL.

topic_id: B33
research_date: 2026-09-24
slug: v-tyumeni-v-broni-novostrojki-prodali-kvartiru-na-14-m-etazhe-v-proektnoj-deklar
P0 Wordstat: «новостройки тюмень» — 4339 (regions 55+11176); «купить новостройку в тюмени» — 898
cluster: newbuild_elevator_serves_fewer_floors_than_unit_tyumen
top_energy: paper_clean_then_broke
mechanism: семья с двумя детьми, ипотека одобрена; бронь квартиры на **14-м** этаже новостройки Тюмени («вид», «премиальная высота» в брони); перед ДДУ сверили проектную декларацию и поэтажные планы — **пассажирский лифт 1–12**, квартира на 14-м; ежедневный сценарий — лестница с коляской; семья **остановила ДДУ** до эскроу; бронь частично удержана (суммы не называть в H1)
klyshin_hook: none (fresh Tyumen newbuild elevator/declaration casus)
comment_magnet_angle (Scout): «Купили бы квартиру на 14-м, если лифт официально только до 12-го, а в брони писали “вид с высоты”?»

Refine scout title_draft to ~55–68 Cyrillic chars. **Em dash (—) only in h1 — NO colon.** Keep words: бронь/новостройка, 14-й этаж, проектная декларация, лифт до 12-го, семья остановила ДДУ. Klyshin rhythm: event + contradiction in documents + consequence.

Scout title_draft (base — shorten, do not copy length):
«В Тюмени в брони новостройки продали квартиру на 14-м этаже — в проектной декларации лифт только до 12-го, семья остановила ДДУ»

Avoid duplicating: B27 земля аренда/собственность в декларации; B28 газ в брони vs декларация; B32 чужое юрлицо эскроу; B31 страховка — this is **лифт до 12 / квартира 14 / декларация / бронь**.

H1 must: news-casus, Tyumen newbuild, 14-й этаж vs лифт до 12-го, проектная декларация or бронь, семья stopped ДДУ (not escrow plot), proper Cyrillic, no «2026», no checklist head, no SEO tail, no naming ЖК/застройщик. **Hard max 70 Cyrillic characters in h1** (count spaces and punctuation).

published-titles-only.md is in article dir.

Gates after JSON: topic_focus.py + scout_story_dup.py on final h1.
