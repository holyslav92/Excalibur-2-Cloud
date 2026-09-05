# Scout inputs — 2026-09-05 (B25)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT weekend slot 15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-05)
- **FROZEN today 2026-09-05 (DO NOT reuse plot):**
  - B23: bank appraisal below DDU / bron burned (`v-tyumeni-odobrili-ipoteku-na-novostrojku-ocenka-banka-nizhe-ceny-ddu`)
  - B24: assignment price raised before DDU (`v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela`)
  - trade-in failed before DDU (`v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela`)
  - investor rental ban until keys (`v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch`)
- **Recent newbuild live WP Sep 3–5 (distinct cluster required):**
  - wet screed acceptance defects / act with defects
  - escrow wrong account
  - area mismatch on keys
  - predchistovka vs chistovaya shown
  - bank withdrew approval 72h before DDU
  - keys delayed certificate instead of penalty
  - rate raised before DDU (B22)
  - tranche mortgage 8x payment
  - cottage land category wrong (2026-09-04)
  - cellar paid not handed (B21)
  - legal entity swap escrow (B20)
- **Closed clusters (30d):** all in `memory/scout/used-clusters.json` — 21 locks
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир)
- `scout_story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B25
- **title_draft:** В Тюмени взяли квартиру в рассрочку от застройщика — на досрочном закрытии всплыла комиссия
- **slug:** v-tyumeni-rassrochka-zastrojschika-dosrochnoe-zakrytie-komissiya
- **cluster_id (new):** newbuild_developer_installment_early_payoff_penalty_tyumen
- **story_dup_check:** PASS — distinct from B22 rate-change before DDU; distinct from B23 bank appraisal; distinct from B24 assignment price hike; distinct from trade-in / rental-ban / escrow / acceptance / area / finish clusters; plot = семья оформила рассрочку от застройщика на новостройку (без ипотеки), через несколько месяцев нашла деньги на досрочное закрытие или переход на ипотеку, в договоре всплыла скрытая комиссия/штраф за досрочное погашение или пересчёт цены без скидки — бронь сгорела или переплата съела выгоду

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке и оформила беспроцентную рассрочку от застройщика вместо ипотеки — менеджер обещал «можно закрыть досрочно без штрафов»
- **risk:** при попытке досрочного погашения (или перехода на ипотеку перед ДДУ) в договоре всплывает пункт о комиссии за досрочное закрытие / пересчёте цены без скидки / штрафе 8–15% от остатка — скидка «сгорает», итоговая цена выше рыночной
- **time:** через 3–6 месяцев после брони, за 2–4 недели до подписания ДДУ, когда семья собрала сумму на закрытие
- **finale:** семья отказалась подписывать ДДУ на пересчитанных условиях; бронь сгорела, внесённые платежи по рассрочке частично удержаны как «неустойка» или зачтены без возврата; квартира ушла в продажу по новой цене
- **comment_magnet_angle:** «Рассрочка без процентов — вы бы поверили менеджеру на слово или сразу искали бы пункт про досрочное закрытие в договоре?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild installment casus without Klyshin — preferred; avoids mortgage/DDU/escrow/assignment clusters from Sep 3–5)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| рассрочка от застройщика | 55+11176 | 226 |
| **рассрочка от застройщика тюмень** | **55+11176** | **143** |
| квартира в рассрочку от застройщика тюмень | 55+11176 | 82 |
| квартира в рассрочку от застройщика | 55+11176 | 103 |
| новостройка в рассрочку от застройщика | 55+11176 | 7 |
| машиноместо в новостройке | 55+11176 | 2 (rejected — weak volume) |
| досрочное погашение рассрочка застройщик | 55+11176 | API empty (rejected) |
| рассрочка от застройщика | 225 (compare) | 21301 |

**wordstat_rework log:**
- probe «рассрочка от застройщика» 55+11176 → 226 (strong base)
- probe «машиноместо в новостройке» 55+11176 → 2 (rejected — weak; parking/declaration angle parked)
- probe «досрочное погашение рассрочка застройщик» 55+11176 → API empty (too narrow)
- probe «квартира в рассрочку от застройщика тюмень» 55+11176 → 82 (good but narrower than localized P0)
- **rework:** localize Tyumen + developer-installment buyer jargon → **final P0 «рассрочка от застройщика тюмень» regions 55,11176 freq 143** (compare RU225 parent phrase 21301)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек/рассрочек; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ долевое строительство (контекст ДДУ vs рассрочка до ДДУ)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B25, title, slug, signal_urls, research angles for Research role.
