# Scout inputs — 2026-10-05 (B34, slot 15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**OWNER OVERRIDE (binding):** `owner-runtime-lock.json` → `topic_market_focus: rubric_per_slot`. Slot **15:00 = vtorichka**. Do **NOT** reject secondary-market plots. Status must be **PASS** — gates already stamped below.

**run_date:** 2026-10-05 (YEKT Monday slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_market_focus:** rubric_per_slot
**slot_rubric:** vtorichka
**dzen_rf_pack:** true

## Trend Radar (slot vtorichka)

- **viral_mechanism:** almost lost перед ключами/деньгами (trend-radar.json vtorichka top angles)
- **energy mirror:** paper looked right → number in BTI broke the mortgage math before DKP

## Slot constraints

- NO EGRN encumbrance-line recycle (cluster egrn_line_blocks_advance / B09)
- NO utility-debt-before-advance recycle (B33 electricity 186k; FSSP 412k live)
- NO tax-minimum-ownership spam (Oct 4 nalog posts)
- NO darstvennaya / pereplanirovka / bankruptcy seller (recent live WP)
- NO newbuild DDU/escrow/bronь as plot spine — slot is **vtorichka**

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 12 active locks (2026-10-05)
- Live WP + ledger reviewed; closed clusters in `memory/scout/used-clusters.json`
- `scout_helper.py --check-query` PASS (EXIT=0)
- `story_dup.py` PASS for candidate cluster

## Proposed topic

- **topic_id:** B34
- **title_draft:** В Тюмени на вторичке акт БТИ урезал площадь на 6 квадратов — банк пересчитал ипотеку, сделку остановили
- **slug:** v-tyumeni-na-vtorichke-akt-bti-urezal-ploshchad-na-6-kvadratov-bank-pereschital-ipoteku
- **article_dir:** memory/blog/articles/B34-v-tyumeni-na-vtorichke-akt-bti-urezal-ploshchad-na-6-kvadratov-bank-pereschital-ipoteku
- **cluster_id (new):** bti_area_shortfall_secondary_mortgage_tyumen

## Dzen news-casus shape

- **event:** семья с одобренной ипотекой на вторичку в Тюмени дошла до подписания ДКП; продавец показывал план «как в объявлении»
- **risk:** по свежему акту БТИ площадь меньше на 6 м² → банк урезает сумму кредита / требует допвзнос; без денег сделка рвётся
- **time:** накануне подписания ДКП у нотариуса, после заказа акту БТИ
- **finale:** банк пересчитал ипотеку, допвзнос не собрали за сутки — ДКП не подписали, аванс не переводили
- **comment_magnet_angle:** «Если в объявлении 54 м², а БТИ даёт 48 — вы бы доплачивали из кармана или сразу снимали объект с продажи?»

## Klyshin

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-10-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|------|
| купить квартиру в тюмени вторичка | 55 | 2812 |
| купить квартиру в тюмени вторичка | 55,11176 | 3453 |
| купить квартиру в тюмени вторичка | 225 (compare) | 6315 |
| проверка квартиры перед покупкой | 55,11176,225 | 1765 |
| покупка квартиры в аварийном доме | 225 | 221 (rejected — weak + wrong plot) |
| долг за капремонт при покупке квартиры | 225 | 33 (rejected — overlaps utility-debt formula) |

**wordstat_rework:** weak BTI-specific probes (API empty/low) → anchor buyer spine «купить квартиру в тюмени вторичка» + BTI-area casus in H1/body

**final P0:** «купить квартиру в тюмени вторичка» — 3453 (55+11176), compare 225: 6315

## Gates stamped by conductor

- story_dup_check: PASS | cluster_id: bti_area_shortfall_secondary_mortgage_tyumen
- h1_fingerprint_check: PASS
- formula_spam_check: PASS | last3_mechanisms: distinct from nalog/FSSP/darstvennaya/pereplanirovka utility-debt
- anti_dupe_hard: PASS
- dzen_casus_shape: PASS

Write full handoff block per SKILL.md including: wordstat_preflight, slot_rubric, viral_mechanism, comment_magnet_angle, wordstat_rework line, wordstat: mcp_kv live line, topic_id, title_draft, slug, article_dir.
