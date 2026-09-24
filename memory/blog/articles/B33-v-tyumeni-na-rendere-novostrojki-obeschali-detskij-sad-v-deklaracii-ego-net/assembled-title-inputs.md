# Assembled title inputs — B33 (Derouter title role)

**topic_id:** B33  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** v-tyumeni-na-rendere-novostrojki-obeschali-detskij-sad-v-deklaracii-ego-net  
**research_date:** 2026-09-24

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_render_amenity_missing_declaration_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none (original Tyumen newbuild casus)
- **comment_magnet_angle (Scout):** «Если на рендере ЖК есть детский сад, а в проектной декларации его нет — вы бы всё равно шли в ДДУ ради квартиры или снимали бронь?»

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank)

1. Семья с двумя детьми (3 и 6 лет) выбирает квартиру в новостройке Тюмени; бронь **150 000 ₽**
2. На рендере двора, в шоуруме и в записи менеджера — отдельное здание «детский сад», в брони: «инфраструктура: детсад во дворе»
3. **За пять дней** до визита в банк и подписания ДДУ — открывают проектную декларацию на dom.rf / ЕИСЖС
4. В разделе 22 (социнфраструктура) — только **детская площадка**, детского сада **нет**
5. Менеджер: «город построит позже», рендер — «концепция»
6. Семья **не подписывает ДДУ**, деньги на эскроу не переводит; из 150 000 ₽ возвращают **90 000 ₽** (удержание по тексту брони — не универсальная норма)

## voice_angle

«Сад на картинке»: на рендере — здание с табличкой, в декларации — площадка без сада. Напряжение — логистика семьи с двумя детьми, не абстрактный спор о визуализации.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4294 |
| купить новостройку в тюмени | 897 |
| новостройки в тюмени от застройщика | 628 |
| проектная декларация застройщика | 25 |

Spine = новостройки Тюмень; механизм = рендер/обещание vs проектная декларация раздел 22.

## Anti-dupe (published siblings — другой plot)

- B27: земля в брони «собственность» vs раздел 12 декларации «аренда до 2049»
- B28: газ в брони vs дата в декларации КП
- B25: чистовая в ДДУ vs приёмка
- **B33 уникален:** детский сад на рендере/в брони vs отсутствие в разделе 22 → отказ от ДДУ до эскроу

## Published titles (anti-repeat only — not style template)

- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B25: В Тюмени в ДДУ обещали чистovую — на приёмке 3 расхождения, акт не подписали

## Champion energy (formula, not copy)

«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял» — завершённое событие + противоречие + следствие.

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B33",
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
- Clear subject (новостройка / детский сад на рендере / проектная декларация)
- Strong verb, active voice; temporal marker if it helps («за 5 дней до ДДУ», «перед ДДУ»)
- **H1 MUST name both poles:** обещание на рендере (или в брони) **и** отсутствие в **проектной декларации** (можно «в декларации его нет»)
- Prefer **«В Тюмени»** or **«за 5 дней до ДДU»** when length allows
- Finale hint OK: отказ от ДДU / не подписали ДДU — secondary to render↔declaration contrast
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific ЖК/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen comments (можно опираться на Scout angle, но формулировка живая)

Reference energy (do not copy verbatim): «В Тюмени на рендере новостройки обещали детский сад — в декларации его нет»
