# Scout inputs — 2026-09-05 (B26, YEKT 17:00 slot)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT Saturday slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-05)
- **Live WP 2026-09-05 — DO NOT reuse plot:**
  - B23: квартира в ДДУ → апартаменты в ЕГРН
  - B24 LIVE: переуступка +280к за сутки до ДДУ
  - B25 LIVE: рассрочка застройщика — досрочное закрытие сожгло скидку
  - оценка банка ниже цены ДДУ на 400к
  - трейд-ин сорвался за день до ДДУ
  - инвестор: аренда запрещена до ключей
  - застройщик потребовал подписать акт с дефектами (инверсный угол — другой casus)
  - на приёмке не хватило метров
  - чистовая vs предчистовая в ДДУ
  - аванс на чужой эскроу-счёт
  - категория земли / дом в КП
  - банк снял одобрение за 72ч до ДДУ (B22 ставка перед ДДУ)
  - ключи задержали 8 месяцев — неустойка сертификатом
  - trade-in, spouse consent, sold twice, EGRN caprepair, 8-tranche — frozen, не брать
- **Rejected overlap:** wet screed only plot (frozen cluster); forced defect act (live inverted); B12 delay keys; B21 cellar/parking
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду, новостройк)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B26
- **title_draft:** В Тюмени не подписали акт с браком — застройщик выставил штраф 190 тысяч
- **slug:** v-tyumeni-ne-podpisali-akt-s-brakom-zastrojschik-vystavil-shtraf-190-tysyach
- **cluster_id (new):** newbuild_acceptance_defect_penalty_clause_tyumen
- **story_dup_check:** PASS — distinct legal plot: семья пришла на приёмку новостройки, нашла существенные дефекты (кривые стены, щели в оконных блоках, неработающая вентиляция), **отказалась подписывать акт**; застройщик сослался на пункт ДДУ о «необоснованном уклонении от приёмки» и выставил **неустойку ~190 000 ₽** (0,1% в день от цены договора × 14 дней) + угроза расторжения с удержанием; банк не выдал остаток ипотеки без акта; семья застряла между арендой и платежами

## Dzen news-casus shape (target PASS)

- **event:** семья с детьми в Тюмени дождалась сдачи корпуса в новостройке, пришла на приёмку с чек-листом
- **risk:** обнаружены дефекты, акт не подписан; в ДДУ есть штрафная оговорка за «затягивание приёмки» без оговорки про брак
- **time:** в течение **14 календарных дней** после уведомления о готовности к передаче (типичный срок по 214-ФЗ / ДДУ)
- **finale:** застройщик выставил претензию на **190 000 ₽** неустойки; банк заморозил финальный транш ипотеки; семья направила встречную претензию с актом осмотра и фото, спор ушёл в досудебку — ключи не получили, но позицию не сдали под давлением штрафа
- **comment_magnet_angle:** «Если на приёмке нашли брак, а застройщик шлёт штраф за „затягивание“ — вы подпишете акт „без претензий“ ради ключей или будете спорить, даже если ипотека висит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild acceptance-penalty casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| приемка новостройки | 55 | 110 |
| приемка квартиры в новостройке тюмень | 55 | 20 |
| приемка квартиры в новостройке | 55 | 100 |
| семейная ипотека новостройка | 55 | 75 |
| новостройки семейная ипотека тюмень | 55 | 16 |
| траншевая ипотека новостройка | 55 | 4 (weak — not P0) |
| **новостройки тюмень** | **55** | **3640** |
| **новостройки тюмень** | **11176** | (Tyumen oblast included in metro) |
| **новостройки тюмень** | **225 (compare)** | **8705** |
| купить новостройку в тюмени | 55 | 639 (context) |

**wordstat_rework log:**
- probe «траншевая ипотека новостройка» 55 → 4 (weak; tranche cluster frozen on live)
- probe «штраф за просрочку приемки» 55 → no reliable volume (API empty)
- probe «дефекты приемка новостройка» 55 → no reliable volume
- probe «приемка квартиры в новостройке тюмень» 55 → 20 (local buyer intent — supports casus)
- probe «приемка новостройки» 55 → 110 (acceptance spine)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, акт приёмки, дефекты) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 3640 (55) / 8705 (RU225)**

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_122947/ — 214-ФЗ о долевом строительстве (приёмка, неустойка)
- https://www.domrf.ru/ — контекст застройщиков / ДДУ
- https://dzen.ru/holyslav — контекст новостроек (не дубль кластера)
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B26, title, slug, signal_urls, research angles for Research role.
