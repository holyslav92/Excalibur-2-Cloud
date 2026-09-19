# Assembled title inputs — B27 (Derouter title role)

**topic_id:** B27  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** v-tyumeni-v-proektnoj-deklaracii-zemlya-pod-zhk-v-arende-v-broni-obeschali-sobst  
**research_date:** 2026-09-19

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_land_lease_not_ownership_declaration_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** в офисе продаж говорят «участок наш, в собственности» → вечером перед банком открывают проектную декларацию → в разделе 12 «право аренды» до 2049 → застройщик «подпишите, потом переоформим» → покупатели отказались от ДДУ за 4 дня до подписания
- **comment_magnet_angle (Scout):** «Если под домом не собственность, а аренда до 2049 года — вы бы всё равно подписали ДДУ, если менеджер клянётся, что “переоформят потом”?»

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank)

1. Family + investor, семейная ипотека; бронь 150 000 ₽
2. Менеджер: «участок наш, в собственности»
3. За 4 дня до ДДУ, вечером перед визитом в банк — открыли декларацию на dom.rf/EISZhS
4. Раздел 12: право аренды гос/муниципального участка, срок до **2049**
5. Застройщик: «подпишите как есть, потом переоформим»
6. Отказ от ДДУ; деньги на эскроу не переводили; бронь отменили; 150 000 ₽ вернули через 12 дней

## voice_angle

«Бумажная собственность»: в офисе — «участок наш», в разделе 12 — «право аренды» и другой собственник. Напряжение не в слове «аренда» (214-ФЗ допускает), а в расхождении обещания и официального документа.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4446 |
| купить новостройку в тюмени | 1936 |
| новостройки в тюмени от застройщика | 656 |
| проектная декларация застройщика | 25 |

Spine = новостройки Тюмень; механизм = проектная декларация / раздел 12 / земля под ЖК.

## Anti-dupe (published siblings — другой plot)

B19/B20 эскроу; B12 ключи/срок; B25 отделка; B26 РВЭ; B22 ставка ипотеки. **B27 уникален:** устное обещание собственности на землю vs раздел 12 декларации (аренда + срок) → отказ от ДДУ **до** перевода на эскроу.

## Published titles (anti-repeat only — not style template)

- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали
- B26: В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч
- B22: В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела
- B12: Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась

## Champion energy (formula, not copy)

«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял» — завершённое событие + противоречие + следствие.

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```

Constraints:
- One headline, ~50–70 characters, Klyshin news-casus rhythm
- Clear subject (новостройка / проектная декларация / земля под ЖК)
- Strong verb, active voice; temporal marker if it helps («за 4 дня до ДДУ», «перед ДДУ»)
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific ЖК/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen comments
