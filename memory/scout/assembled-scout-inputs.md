# Scout inputs — 2026-09-07 (B24, slot ~17:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-07 (YEKT weekday slot 4 ~17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 29 active locks (last_sync 2026-09-07)
- **Live WP ~20 (2026-09-07) — DO NOT reuse plot:**
  - 2026-09-07: ДДУ расторгли из-за 5 дней просрочки рассрочки — удержали 180 тыс (slot ~15)
  - 2026-09-07: ДДУ на коттедж — газ у забора обещали, магистраль в 180 м (slot ~12)
  - 2026-09-07: в ДДУ 12-й этаж — на ключах дали 2-й (slot ~09)
  - эскроу не хватило 400 тыс до ДДУ (ddu_amount_vs_escrow_zero LOCKED)
  - 12 vs 8 соток в КП; 1 квартира 2 семьям; 300 тыс перед ключами; ключи +7 мес без неустойки; 45 vs 41 м²; приёмка 190 тыс штраф; апартаменты в ЕГРН; рассрочка потеряли скидку; инвестор аренда запрещена; переуступка +280к; трейд-ин; оценка ниже ДДУ; категория земли КП; чужой счёт аванса; ставка перед ДДУ; акт с дефектами
- **Rejected:** title with «на эскроу не хватило N тысяч» → ddu_amount_vs_escrow_zero cluster LOCK
- **Rejected:** «накануне ДДУ — банк остановил подписание» → 40% overlap B22 / LIVE-V-TYUMENI-NAKANUNE-DDU-B
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек, семейн)
- `excalibur_blog_scout_story_dup.py --text` PASS

## Proposed topic (PASS all gates)

- **topic_id:** B24
- **title_draft:** В Тюмени семейную ипотеку одобрили на двоих — перед ДДУ созаёмщика исключили, лимит упал
- **slug:** v-tyumeni-semejnuyu-ipoteku-odobrili-na-dvoih-pered-ddu-sozaemshchika-isklyuchili
- **article_dir:** B24-v-tyumeni-semejnuyu-ipoteku-odobrili-na-dvoih-pered-ddu-sozaemshchika-isklyuchili
- **cluster_id (new):** newbuild_coborrower_dropped_before_ddu_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** банк одобрил семейную ипотеку на двоих под ДДU на новостройку; за сутки до подписания убрал созаёмщика из кредита — лимит упал, на эскроu не хватило суммы по договору, подписание остановили **до** перевода денег
- **why_newbuild_not_secondary:** только ДДU/эскроu/застройщик и семейная ипотека на новостройку; нет вторичного продавца, ЕГРН-наследников и «чистой выписки» как в top-10 вторичке

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, получила одобрение семейной ипотеки на двоих, забронировала объект и пришла подписывать ДДU
- **risk:** банк исключил созаёмщика из одобрения — сумма кредита и первоначального взноса перестала сходиться с ценой в ДДU и графиком эскроu
- **time:** за сутки / в день подписания ДДU в офисе застройщика
- **finale:** подписание остановили до перевода на эскроu; бронь сгорела или застройщик поднял цену; семья не внесла деньги — сделку сорвали на месте (agency: остановились до аванса)
- **comment_magnet_angle:** «Банк неделю держал одобрение „на двоих", а перед ДДU созаёмщика выкинули. Вы бы подписали договор на оставшийся лимит или забрали бы бронь?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild casus; Klyshin not used — avoids duplicate with live ~20)

## Wordstat MCP-KV (live 2026-09-07)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| созаемщик ипотека | 55+11176 | 573 |
| созаемщик ипотека | 225 (compare) | 35922 |
| ипотека на новостройку тюмень | 55+11176 | 55 (weak local) |
| семейная ипотека тюмень | 55+11176 | 1158 (top: «семейная ипотека в тюмени» 730) |
| **семейная ипотека в тюмени** | **55+11176** | **730** |
| семейная ипотека в тюмени | 225 (compare) | 1063 |
| новостройки тюмень | 55+11176 | 4670 (context spine) |

**wordstat_rework log:**
- probe «созаемщик ипотека» 55+11176 → 573; compare RU225 → 35922 (buyer intent есть, но без Tyumen/newbuild spine)
- probe «ипотека на новостройку тюмень» 55+11176 → 55 (слабо)
- rework: localize Tyumen + семейная ипотека + newbuild buyer jargon (ДДU, эскроu, созаёмщик)
- probe «семейная ипотека в тюмени» 55+11176 → **730**; compare RU225 → **1063**
- **final P0 «семейная ипотека в тюмени» 730 (regions 55,11176) / 1063 (compare 225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ / ДДU
- https://www.domrf.ru/
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with ALL fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat (mcp_kv live | regions 55,11176,compare225 | P0 phrase+freq), story_dup_check PASS + cluster_id, h1_fingerprint_check PASS + fingerprint, formula_spam_check PASS + last3_mechanisms, anti_dupe_hard PASS, topic_id B24, title, slug, article_dir, signal_urls.
