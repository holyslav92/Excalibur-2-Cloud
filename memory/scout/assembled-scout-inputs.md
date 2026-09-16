# Scout inputs — 2026-09-16 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-16 (YEKT weekday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO co-borrower / family mortgage refusal (live 2026-09-16: bank refused co-borrower 4 days before escrow)
- NO booking floor/view mismatch, assignment 350k, KP no gas, accreditation removed, price hike, acceptance for parents, price fixation (all live 2026-09-15)
- NO matkapital 7 years, 3-room→2-room, double booking, 54→52 meters (live 2026-09-14)
- NO B26 RVE/no commissioning permit + second tranche; NO B25 finishing mismatch; NO B23 apartments; NO B22 rate hike; NO B20 legal entity change; NO B19 escrow not opened
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 28 active locks (last_sync 2026-09-16)
- Live WP recent (~12): co-borrower family mortgage 4d before escrow; booking/DDU section; assignment 350k; KP no gas; accreditation removed; price hike; parents acceptance; price fixation; matkapital 7y; 3-room→2-room; double booking; 54→52 m²
- **Rejected:** bank_appraisal_below_ddu_price — CLUSTER LOCK ddu_amount_vs_escrow_zero + H1 fingerprint dup LIVE-V-TYUMENI-BANK-OCENIL-NO
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: новострой)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени ключи от новостройки выдали с опозданием на 9 месяцев — неустойку на счёт так и не перевели
- **slug:** v-tyumeni-klyuchi-novostrojka-opozdanie-neustojka-ne-vyplatili
- **cluster_id:** keys_delay_penalty_unpaid
- **top_energy_mirror:** clock_ran_out
- **newbuild_mechanism:** срок передачи по ДДУ прошёл на 9 месяцев; ключи выдали с опозданием; застройщик в переписке признал просрочку и обещал неустойку по 214-ФЗ; семья подписала акт приёмки с оговоркой о взыскании; расчёт неустойки (~380 тыс.) направили претензией; застройщик сослался на «отсрочку исполнения» и мораторий 2026; на счёт дольщиков деньги не поступили — спор ушёл в суд
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ → срок сдачи → акт приёмки → неустойка застройщика по 214-ФЗ; нет продавца вторички, ЕГРН-сделки, наследников или бабушки на осмотре
- **story_dup_check:** PASS — distinct from B12 (перенос сдачи + эскроу/ипотека до ключей), B26 (РВЭ + второй транш), installment_penalty_developer (рассрочка 4 дня), LIVE morning co-borrower

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в ЖК по ДДУ с ипотекой; дата передачи в договоре прошла, ключи молчали
- **risk:** каждый месяц просрочки — аренда + ипотека; после выдачи ключей — неустойка как единственный «возврат» за год ожидания; застройщик тянет выплату
- **time:** 9 месяцев после договорной даты; ключи вручили на 271-й день просрочки; через 4 месяца после акта — ноль на счёте по претензии
- **finale:** акт подписан с оговоркой; претензия с расчётом ~380 тыс. — ответ «отсрочка до конца 2026»; семья подала в суд, ДДУ не расторгали, квартиру не сдают в аренду из-за отделки
- **comment_magnet_angle:** «Ключи уже в руках, а неустойку за год ждут четвёртый месяц: вы бы подписали акт без оговорки ради заселения или тормозили до перевода денег на счёт?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild keys-delay + unpaid penalty without Klyshin)

## Wordstat MCP-KV (live 2026-09-16)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| неустойка застройщика за просрочку сдачи | 55,11176 | 3 |
| **неустойка застройщика** | **55,11176** | **134** |
| неустойка застройщика | 225 (compare) | 8156 |
| оценка новостройки для банка | 55,11176 | 1 (rejected — dup cluster bank appraisal live) |
| новостройки тюмень | 55,11176 | 4475 (context spine) |

**wordstat_rework log:**
- probe «неустойка застройщика за просрочку сдачи» 55,11176 → 3 (weak tail)
- rework → buyer jargon «неустойка застройщика» + ДДУ/ключи → **final P0 «неустойка застройщика» regions 55,11176,compare225 freq 134 (55+11176) / 8156 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, срок передачи, неустойка
- https://www.domrf.ru/ — проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{PUBLIC_SITE_URL}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
