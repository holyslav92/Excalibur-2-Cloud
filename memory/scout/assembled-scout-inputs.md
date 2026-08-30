# Scout inputs — 2026-08-29 (B13, slot 12:05 UTC / ~17:05 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- Live WP blog (~12 titles fetched 2026-08-29):
  1. В Тюмени кладовка «в подarok» остановила сделку — в ЕГРН её не было
  2. Аккредитив открыли, сделку зарегистрировали — продавец без денег
  3. В Тюмени приставы арестовали квартиру за два дня до регистрации
  4. Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд
  5. В Тюмени три года платили за квартиру — собственник продал её другим
  6. Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась
  7. В Ялуторовске квартиру продали двоим — покупательнице грозит выселение
  8. В Тюмени открытая кухня остановила регистрацию квартиры (B11)
  9. Нотариус не выделил супружескую долю — аванс остановили
  10. Купил вторичку в Тюмени — через два года суд забрал квартиру
  11. Четыре месяца искали вторичку — через два года суд оспорил сделку
  12. Маткапитал был, опека промолчала: дети через три года отменили сделку
- **FROZEN today plots — DO NOT reuse:** kladovka/EGRN gift; akkreditiv seller no money; FSSP arrest 2 days before registration; adult guardianship day before advance; rent-to-buy 3 years; Yalutorovsk double sale; B12 escrow novostroyka delay; B11 open kitchen illegal renovation
- Closed clusters (30d): illegal_renovation_rosreestr_blocks_registration, marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction
- Ledger B02–B12 in shared/published-articles.md

## Proposed topic (PASS scout_helper + story_dup)

- **topic_id:** B13
- **title_draft:** Маткапитал потратили, а детям доли не выделили — в Тюмени сделку развернули до денег
- **slug:** v-tyumeni-matkapital-detskie-doli-ne-vydelili-sdelku-razvernu-li
- **cluster_id (new lock):** matkapital_missing_child_shares
- **story_dup_check:** PASS — distinct from matkapital_opieka_kids_cancel_3y (опека молчала + отмена через 3 года); plot = детские доли после маткапитала **никогда не выделили**, в выписке только родители, сделку остановили **до денег** на финальной юрпроверке

## Dzen news-casus shape (PASS)

- **event:** семья в Тюмени выбрала вторичку, ипотеку одобрили, в выписке ЕГРН — только два взрослых собственника
- **risk:** квартира когда‑то покупалась с маткапиталом, но детские доли так и не выделили; сделку можно оспорить, покупатель рискует потерять деньги и квартиру
- **time:** за два дня до задатка, на финальной проверке юриста перед подписанием ДКП
- **finale:** юрист нашёл след маткапитала и отсутствие детских долей — сделку развернули до денег; покупатели ушли к другому объекту; продавцам пришлось бы выделять доли или снимать квартиру с рынка на месяцы
- **comment_magnet_angle:** «Если в выписке только родители, а продавец клянётся, что маткапитала не было — вы верите или уходите?»

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen matkapital casus without Klyshin; avoid today's FSSP/guardianship/rent-to-buy plots)
- **signal_urls:** see below

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| маткапитал доли детей | 55+11176 | 94 |
| доли маткапитала детей | 55+11176 | 94 |
| выделить доли детям в квартире маткапитал | 55+11176 | 23 |
| доли маткапитала детей | 225 (compare) | 7457 |
| несовершеннолетний собственник квартиры | 55+11176 | 96 (alt angle, not chosen) |
| долг капремонт | 55+11176 | 47 (rejected — weaker casus + overlap warning) |
| пристав арест квартира | 55+11176 | 38 (rejected — live WP duplicate today) |
| фссп проверить задолженность | 55+11176 | 232 (rejected — live FSSP plot today) |

**wordstat_rework log:**
- probe «маткапитал доли детей» 55+11176 → 94
- probe «на маткапитал купили детские доли» → API empty
- probe «выделить доли детям маткапитал» 55+11176 → 16 (narrow)
- **rework:** buyer jargon «доли после маткапитала в выписке» → **final P0 «доли маткапитала детей» regions 55,11176 freq 94** (compare RU225 7457)

## scout_helper result

```
python3 scripts/excalibur_blog_scout_helper.py --check-query "Маткапитал потратили, а детям доли не выделили — в Тюмени сделку развернули до денег matkapital_missing_child_shares v-tyumeni-matkapital-detskie-doli-ne-vydelili"
→ ✅ NO CANNIBALIZATION RISK + ✅ TOPIC FOCUS PASS
```

## signal_urls (research)

- https://dzen.ru/holyslav — канал holyslav (контекст маткапитал/детские доли, не дубль кластера opieka_3y)
- https://t.me/holyslav92
- https://t.me/klyshin_A — checked, not used this slot
- https://www.gosuslugi.ru/help/faq/property/100359 — маткапитал: выделение долей детям (справочный контекст)
- https://base.garant.ru/ — нормы о выделении долей при использовании маткапитала (для Research)
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
