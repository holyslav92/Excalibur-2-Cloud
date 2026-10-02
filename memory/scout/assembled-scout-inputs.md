# Scout inputs — 2026-10-02 (B34)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**SLOT RUBRIC OVERRIDE (2026-09-28 owner, HARD for this run):** `shared/slot-rubric-lock.md` + `shared/pipeline-canon.json` → `slot_rubric_mix` replace legacy «только новостройки» **per slot**. This run: **15:00 YEKT → `vtorichka` ONLY** (`python3 scripts/excalibur_blog_slot_rubric.py --current` → vtorichka). `shared/newbuild-focus-lock.md` applies to **`novostroyki` slots only**. Secondary market casus is **REQUIRED**, not forbidden. Do **not** reject for «secondary plot» — reject only if anti-dupe/Wordstat/slot mechanism fails (already PASS below).

**run_date:** 2026-10-02  
**slot:** 15:00 YEKT  
**slot_rubric:** vtorichka (вторичка) — NOT newbuild-only for this slot (`shared/slot-rubric-lock.md`)  
**topic_id:** B34  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**dzen_rf_pack:** true  

## Slot constraints (HARD FORBIDDEN — owner + live WP)

Do NOT recycle these recent plots (even with new title):
- банкрот продавца на вторичке (2026-09-30 live)
- дарственная пенсионерка / остановила сделку (2026-09-29)
- долг за свет 186 тыс. перед авансом (B33, 2026-09-28)
- семейная ипотека на вторичке с 1 октября / лимит не сошёлся (2026-10-01 live)
- запрет пристава сорвал аванс (2026-09-30 live)
- аренда 3 года в ЕГРН остановила покупку (2026-09-29)
- NO retitle newbuild (ДДУ/эскроу/бронь) into this vtorichka slot

## Trend Radar (slot 15:00, rubric vtorichka)

Source: `memory/blog/trend-radar/trend-radar.json` (generated 2026-10-02T10:22:30Z)

- **viral_mechanism (SAME energy only):** `almost lost перед ключами/деньгами` — top angle Life «С 1 октября вырастет спрос на вторичную недвижимость…» (views 38614, viral_score 8.52)
- **Mirror for this topic:** `someone_else_took_object` + `clock_ran_out` — семья «успела» по цене, но не по авансу; другой покупатель забрал объект на фоне октябрьского спроса на вторичку (без сюжета семейной ипотеки 1 октября)

## Anti-repeat preflight (DONE)

```bash
python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters
# → 14 active locks (last_sync 2026-10-02)
```

Live WP / ledger recent (~12): кладовая из брони 190k (newbuild), презентация 35 vs ДДУ 89 (newbuild), семейная ипотека вторичка 1 окт, эскроу+«сдам» newbuild, школа в рекламе ЖК, банкрот продавца, запрет пристава, двор без машин, промёрзшая стена, аренда в ЕГРН, дарственная, долг за свет B33.

**Proposed cluster (NEW):** `secondary_rival_buyer_snatched_advance_tyumen`

**title_draft:** В Тюмени на вторичке согласовали цену — через час другой покупатель внёс аванс

**slug hint:** v-tyumeni-na-vtorichke-soglasovali-tsenu-cherez-chas-drugoj-pokupatel-vnes-avanс

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "В Тюмени на вторичке согласовали цену — через час другой покупатель внёс аванс secondary_rival_buyer_snatched_advance_tyumen clock_ran_out"
# → ANTI-DUPE HARD PASS, NO CANNIBALIZATION RISK

python3 scripts/excalibur_blog_topic_focus.py --text "В Тюмени на вторичке согласовали цену — через час другой покупатель внёс аванс"
# → TOPIC FOCUS PASS (allow_hit=аванс, vtorichka slot)

python3 scripts/excalibur_blog_slot_rubric.py --current
# → vtorichka
```

Rejected candidates (for rework log):
- bank appraisal −620k before advance → 42% overlap with bankruptcy «семья не перевела деньги» skeleton (BLOCK)
- kapremont / MFO pledge in EGRN → cluster lock `egrn_line_blocks_advance` B09 (BLOCK)
- seller price hike after mortgage → `mortgage_rate_hike_before_ddu` lock (BLOCK)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени нашла двушку на вторичке, торг согласовали с продавцом устно и в переписке; риэлтор предупредил про очередь покупателей после всплеска спроса с 1 октября
- **risk:** без задатка/аванса продавец legally free — другой покупатель вносит аванс первым; у семьи остаются одобренная ипотека и потерянный объект
- **time:** «через час» после согласования цены, накануне планируемого аванса
- **finale:** продавец принял аванс от другого, объявление сняли; семья не успела перевести деньги, вернулись в поиск на перегретом рынке
- **comment_magnet_angle:** «Вы бы внесли аванс в тот же день без расширенной выписки или до конца проверили — даже если квартиру могут забрать?»

## Wordstat MCP-KV (live, regions 55+11176, compare 225)

**wordstat_preflight:** `wordstat_get_user_info` → OK (Yandex Cloud API)

| probe | freq (55+11176) | note |
|-------|-----------------|------|
| покупка квартиры на вторичке тюмень | API empty | rework |
| вторичное жилье тюмень | 1113 | spine candidate |
| купить квартиру вторичка тюмень | **3348** | **final P0** |
| аванс при покупке квартиры | 13 | casus lexicon |
| обременение при покупке квартиры | 30 | not this plot |
| ипотека на вторичку тюмень | 48 | secondary |
| семейная ипотека на вторичку в тюмени | 18 | **avoid plot** (live WP) |

**compare 225:** «купить квартиру в тюmeni вторichka» → **6220**

**wordstat_rework:** probe «вторичное жилье тюmenь» 1113 → probe «купить квартиру вторichka tюmenь» **3348** → final P0 «купить квартиру в тюmeni вторichka» **3348** (55+11176)

**klyshin_hook:** none (optional not used; fresh Tyumen casus without Klyshin)

## Handoff fields to emit (complete)

- slot_rubric: vtorichka
- viral_mechanism: almost_lost_before_keys_money → someone_else_took_object
- top_energy_mirror: someone_else_took_object / clock_ran_out
- vtorichka_mechanism: конкуренция покупателей + аванс на вторичке (не ДДУ/эскроу)
- dzen_casus_shape: PASS
- comment_magnet_angle: (see above)
- wordstat + story_dup + anti_dupe_hard: PASS
- research_start command with --topic-id B34
