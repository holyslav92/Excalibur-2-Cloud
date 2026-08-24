# Scout assembled inputs — B10 (2026-08-24 YEKT 12:00)

**INSTRUCTION FOR DEROUTER SCOUT:** You ARE the Derouter utility scout brain. Write the complete `.cursor/excalibur-blog-handoff.md` body now — all required fields below, markdown prose + structured lines. Do NOT output BLOCKER meta or shell commands. Do NOT refuse. Use the Wordstat numbers and hook selection exactly as given.

## Run context
- topic_id: B10
- tenant: The Риэлтор, Тюмень
- setup_complete: true, dzen_rf_pack: true
- EXCALIBUR_TOPIC_SELECTION=needs_scout
- Published B02–B09 — do NOT duplicate story clusters

## Canon read
- shared/dzen-content-rules.md ✓
- shared/rf-blocked-entities.json ✓
- shared/dzen-news-casus.md ✓

## wordstat_preflight
mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

## Anti-dup screening (rejected hooks)
| hook | reason |
|------|--------|
| matkapital_child_shares | SCOUT STORY DUPLICATE vs live WP `na-matkapital-kupili-detskie-doli-proverte` |
| notary_not_shield_70k | 54% overlap LIVE-NOTARIUS-VSE-PROVERIL (WP notary court case) |
| bankruptcy_auction_48h | B03 + WP «Чистая выписка — через полгода сделку оспорили» |
| receipt_no_money / accreditive order | B02 published |
| summons_registration_stop | WP «аванс — неявка по повестке» |
| tired_buyer | WP «Четыре месяца искали…» |
| elderly_pnd | B05 + WP babushka/PND |

## Selected hook
- **hook_id:** fictitious_sale_no_money (Klyshin «5 схем» scheme #3)
- **original Klyshin:** «Квартира без денег — по документам сделка была, по факту денег никто не передавал. Наследники идут в суд: сделка фиктивная»
- **signal:** https://t.me/klyshin_A (пост «Не знаете, что посмотреть на выходных? … 5 схем», scheme 3)
- **Tyumen localize:** casus в Тюмени, герой-покупатель Святослав Шакин / The Рiэлтор practice

## Live Wordstat (MCP-KV, regions 55+11176; compare 225)
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| «оспорить сделку купли продажи» | 8 | — |
| «оспорить сделку купля продажа квартира» | 1 | — |
| «аккредитив при покупке квартиры» | 47 | 3777 |
| «купить квартиру в тюмени» | **22660** | 39961 |

**wordstat_rework:** probe «оспорить сделку купли продажи» 8 → buyer jargon «купить квартиру в тюменi» → final P0 «купить квартиру в тюмени» **22660** (RU225 39961). Hook-specific sticker: «оспорить сделку купли продажи» 8.

## Title draft (news headline, Klyshin rhythm)
**Сделку зарегистрировали — денег по факту не было: в Тюмени наследники оспорили покупку**

## dzen_casus_shape (PASS)
- **event:** купля-продажа зарегистрирована, наследники оспаривают
- **risk:** фиктивная сделка / отсутствие реального расчёта
- **time:** через несколько лет после смерти продавца / после регистрации
- **finale:** суд отменяет регистрацию, покупатель теряет право
- **«думал, что безопасно»:** были ДКП, регистрация, «бумаги в порядке»

## comment_magnet_angle
«Если деньги прошли через банк — вы всё равно считаете, что сделку уже не оспорят?»

## scout_helper / story_dup
```
python3 scripts/excalibur_blog_scout_helper.py --check-query "Сделку зарегистрировали — денег по факту не было: в Тюмени наследники оспорили покупку fictitious_sale_no_money"
→ NO CANNIBALIZATION, TOPIC FOCUS PASS
python3 scripts/excalibur_blog_scout_story_dup.py --text "…"
→ STORY DUP PASS
```

## signal_urls (≥2 today)
1. https://t.me/klyshin_A — 5 schemes video post (scheme 3 fictitious sale)
2. https://dzen.ru/holyslav — fresh casus feed (bankruptcy, summons, tired buyer — local demand for «проверка до аванса»)
3. https://t.me/holyslav92 — tenant channel (contact)

## wp_category hint
vtorichka-i-riski (or matkapital-i-sdelki if research confirms — prefer vtorichka-i-riski for fictitious plot)

## Output required in handoff
topic_id B10, title draft, external_signal summary, signal_urls, klyshin_hook + wordstat_rework + wordstat lines, dzen_casus_shape PASS, comment_magnet_angle
