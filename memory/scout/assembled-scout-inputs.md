# Scout inputs — 2026-09-15 (B27, slot 15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-15 (YEKT slot 15:00 — 4-й пост дня, нужен СВЕЖИЙ кластер)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — same day 2026-09-15)

- NO КП без газа на ключах (utilities KP gas)
- NO банк снял ЖК с аккредитации за 24ч до ДДУ
- NO подорожал прайс ЖК за 9 дней до ДДУ
- NO приёмка для родителей — лифт/акт (acceptance_defects_penalty)
- NO сорвалась фиксация цены за 5 дней до ДДУ
- NO parking/кладовка double-sold (B24 cluster)
- NO DDU finishing mismatch (B25)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-15)
- Live WP today (5 posts): KP gas, bank deaccreditation, price hike, parents acceptance, price fixation failed
- Recent 2026-09-14: matkapital 7 years, DDU layout 3→2, double booking, 54 sqm mismatch, KP plot 12 vs 9.7
- **Rejected:** bank appraisal below DDU — fingerprint dup LIVE-V-TYUMENI-BANK-OCENIL-NO + ddu_amount_vs_escrow_zero lock
- **Rejected:** keys_delay_penalty_unpaid — fingerprint dup LIVE-V-TYUMENI-ZASTROJSCHIK-P
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени застройщик не согласовал переуступку — аванс 350 тысяч завис за 3 дня до ДДУ
- **slug:** v-tyumeni-zastrojschik-ne-soglasoval-pereustupku-avanse-ne-vernuli
- **article_dir:** memory/blog/articles/B27-v-tyumeni-zastrojschik-ne-soglasoval-pereustupku-avanse-ne-vernuli
- **cluster_id (new):** assignment_developer_consent_denied_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** Покупатель нашёл **переуступку** по ДДУ в новостройке, перевёл **аванс 350 тыс.** первому дольщику по договору уступки; за **3 дня до подписания нового ДДУ** застройщик прислал отказ в **согласии на переуступку** (долг по взносам у первого дольщика / «не прошли внутреннюю проверку») → аванс у assignor, сделка остановлена **до** эскроу и банковских денег
- **why_newbuild_not_secondary:** сюжет = цепочка ДДУ → согласие застройщика на уступку → новый договор с застройщиком; нет продавца вторички, ЕГРН-вторички, наследников, бабушки или «чистой выписки»
- **story_dup_check:** PASS — distinct from assignment_lost_to_faster_buyer (другой забрал бронь), trade_in_rejected, booking/price fixation today, escrow zero, bank deaccreditation

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени решила купить квартиру в строящемся ЖК **по переуступке** — цена ниже прайса застройщика
- **risk:** без письменного **согласия застройщика** новый ДДУ не подписать; аванс у первого дольщика — возврат только по договору уступки, не по 214-ФЗ
- **time:** за **3 дня** до назначенного подписания ДДУ в офисе застройщика пришёл отказ; аванс перевели **19 дней** назад
- **finale:** застройщик предложил купить «с нуля» по текущему прайсу (+420 тыс. к сумме уступки); первый дольщик вернул только **120 тыс.** из 350 — остальное «комиссия и удержание»; семья отказалась от нового ДДУ, квартиру забрал другой покупатель с согласованной уступкой
- **comment_magnet_angle:** «350 тысяч аванса переуступки — это ещё не эскроу: вы бы перевели деньги первому дольщику до письменного согласия застройщика или ждали бы официальный ответ из офиса продаж?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild assignment casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-15)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройки | 55,11176 | 18 (weak — assignment jargon) |
| договор переуступки новостройки | 55,11176 | 5 (weak) |
| новостройки тюмень | 55,11176 | 4475 (context spine) |
| **купить новостройку в тюмени** | **55,11176** | **902** |
| купить новостройку в тюмени | 225 (compare) | 1916 |

**wordstat_rework log:**
- probe «переуступка новостройки» 55,11176 → 18 (weak; keep casus angle assignment)
- probe «договор переуступки новостройки» → 5 (weak)
- **rework:** buyer demand spine newbuild Тюмень → **final P0 «купить новостройку в тюмени» regions 55,11176,compare225 freq 902 (55+11176) / 1916 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, права дольщиков, переуступка
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
