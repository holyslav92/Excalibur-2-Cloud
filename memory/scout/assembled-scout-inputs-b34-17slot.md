# Scout inputs — 2026-10-03 (B34)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-10-03 (YEKT slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**slot_rubric:** vtorichka (HARD — ONLY вторичка; ignore newbuild-only blocks in scout agent for this slot)
**topic_market_focus:** vtorichka_secondary_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — today + 30d)

- NO «за N дней до аванса банк остановил/снял одобрение» formula (2026-10-03 live: дарственная, перепланировка; 2026-10-02: аренда на Авито; B33 коммунальный долг) — last-3 formula spam risk
- NO задаток/расписка (2026-10-03 live zadatok 180k)
- NO дарственная перед авансом (2026-10-03 live)
- NO неузаконенная перепланировка (2026-10-03 live)
- NO ЕГРН-обременение/ипотека сорвала регистрацию (cluster egrn_line_blocks_advance B09 locked)
- NO frozen clusters in memory/scout/used-clusters.json (30d): inheritance son, deceased spouse, egrn line, bankruptcy finmanager, grandma, opieka matkapital, forged consent, registered persons, communal share, illegal reno rosreestr, etc.
- NO newbuild as main mechanism (ДДУ, бронь, эскроу, застройщик, приёмка новостройки)

## Trend Radar energy (slot vtorichka, 2026-10-03)

- **viral_mechanism:** almost lost перед ключами/деньгами + paper clean then broke (выписка/ДКП «чисто», на сделке вскрывается скрытый договор)
- Mirror energy, NOT plot copy from Dzen sources

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 12 active locks (last_sync 2026-10-03)
- EXCALIBUR_RECENT_WP_POSTS 2026-10-03: zadatok+raspiska, darstvennaya+avans, pereplanirovka+avans, novostroyki slots (family mortgage 7y, DDU отделка, BTI…)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (вторичка marker)
- FSSP/ЕГРН-обременение candidate REJECTED (egrn_line_blocks_advance duplicate)

## Proposed topic (PASS anti-dupe + topic_focus)

> **UPDATE 2026-10-03:** слот закрыт публикацией **B34 ФССП 412k**. Угол ниже перенесён на **B35** — см. `memory/scout/b35-candidate-rent-notarius.md`.

- **topic_id:** B35 *(was B34 in parallel scout run)*
- **title_draft:** В Тюмени на вторичке нотариус на ДКП нашёл договор ренты — регистрацию не открыли
- **short_title:** Нотариус на ДКП нашёл договор ренты — регистрацию не открыли
- **slug:** v-tyumeni-na-vtorichke-notarius-na-dkp-nashol-dogovor-renty-registraciyu-ne-otkryli
- **article_dir:** memory/blog/articles/B34-v-tyumeni-na-vtorichke-notarius-na-dkp-nashol-dogovor-renty-registraciyu-ne-otkryli
- **cluster_id (new):** life_annuity_rent_contract_notary_blocked_secondary_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **vtorichka_mechanism:** Семья покупает двушку на вторичке в Тюмени в ипотеку. Продавец — пожилой собственник, выписка ЕГРН без обременений, согласие супруги, банк одобрил. На подписании ДКП у нотариуса покупатель спросил про папку с договорами — всплыл **договор пожизненной ренты** (пожизненное содержание с иждивением), зарегистрированный ранее: рентополучатель сохраняет право проживания/получения содержания, сделка без его участия оспорима. Нотариус отказался открывать регистрацию, банк заморозил выдачу, семья ушла без ключей (аванс в ячейке не вскрывали / задаток не передавали — только бронь времени и оплаченные услуги)
- **why_vtorichka_not_newbuild:** Сюжет целиком в цепочке ДКП вторички, выписки ЕГРН, нотариального удостоверения/электронной регистрации, ипотеки на вторичное жильё. Нет застройщика, ДДУ, эскроу на новостройку, брони ЖК, приёмки от застройщика

## Dzen news-casus shape (PASS)

- **event:** семья с ребёнком выбрала двушку на вторичке в Тюмени, согласовала ипотеку, пришла к нотариусу подписывать ДКП
- **risk:** договор пожизненной ренты / пожизненного содержания — скрытый обладатель прав на жильё; оспаривание сделки, невозможность вселения, банк снимает финансирование
- **time:** в кабинете нотариуса, в момент подписания ДКП (не «за N дней до аванса»)
- **finale:** нотариус увидел зарегистрированный договор ренты, регистрацию не открыл; банк отложил выдачу кредита; семья отказалась от сделки в тот же день; деньги продавцу не переводили
- **comment_magnet_angle:** «Если выписка ЕГРН чистая, а рента всплыла только у нотариуса — это вина продавца, риэлтора или покупатель сам виноват, что не спросил папку?»

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen secondary rent-contract casus without Klyshin)

## Wordstat MCP-KV (live 2026-10-03)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| вторичное жилье тюмень | 55,11176 | 1093 |
| вторичное жилье тюмень | 225 (compare) | 1828 |
| купить квартиру в тюмени вторичное жилье | 55,11176 | 566 |
| ипотека на вторичное жилье тюмень | 55,11176 | 107 |
| договор пожизненного содержания квартира | 55,11176 | 4 |
| договор ренты квартира | 55,11176 | 19 |
| фссп арест квартиры при продаже | 55,11176 | API empty/<5 (rejected — overlaps egrn_line cluster) |

**wordstat_rework:**
- probe «договор пожизненного содержания квартира» 55,11176 → 4 (too weak for P0 alone)
- probe «договор ренты квартира» 55,11176 → 19 (weak; keep in body/H2)
- probe «фссп…» → empty; plot rejected as duplicate egrn_line_blocks_advance
- **rework:** anchor buyer spine «вторичное жилье тюмень» + mechanism рента/пожизненное содержание в H1
- **final P0 «вторичное жилье тюмень» regions 55,11176,compare225 freq 1093 (55+11176) / 1828 (225)**

## story_dup / fingerprint / formula

- **story_dup_check:** PASS | cluster_id: life_annuity_rent_contract_notary_blocked_secondary_tyumen
- **h1_fingerprint_check:** PASS | fingerprint: notary_dkp_rent_contract_registration_stop (distinct from avans/darstvennaya/pereplanirovka/zadatok)
- **formula_spam_check:** PASS | last3_mechanisms: darstvennaya_before_avans, pereplanirovka_ipoteka_revoke, zadatok_raspiska_bank — candidate = notary_rent_at_dkp (different skeleton)
- **anti_dupe_hard:** PASS

## Handoff required fields (include verbatim block)

slot_rubric: vtorichka
viral_mechanism: almost lost перед ключами/деньгами + paper_clean_then_broke
wordstat_p0: «вторичное жилье тюмень» 1093 (55+11176); compare RU 1828 (225)
comment_magnet_angle: (see above)
dzen_casus_shape: PASS
anti_dupe_hard: PASS
