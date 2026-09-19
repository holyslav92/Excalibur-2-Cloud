# Assembled title inputs — B30 (Derouter title role)

**topic_id:** B30  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** v-tyumeni-v-shou-rume-yuzhnaya-storona-v-chernovike-ddu-severnaya-sektsiya  
**research_date:** 2026-09-19

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_showroom_sun_side_vs_ddu_north_section_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** optional | none — invent own Klyshin-rhythm headline from mechanism below
- **locked_title (Scout direction, may refine for H1 rhythm):** «В Тюмени в шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция»
- **comment_magnet_angle (Scout):** «Если в шоу-руме солнце, а в ДДУ — северная секция за ту же цену, вы бы подписали, чтобы не потерять бронь, или сразу ушли?»

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank)

1. Семья смотрит шоу-рум и макет квартиры на **южной** стороне ЖК в Тюмени; солнце, вид во двор
2. В брони и презентации зафиксирована «солнечная сторона»
3. За **пять дней** до подписания ДДУ — проект договора: та же площадь и этаж, но **секция B**, **северная** сторона; окна на соседний корпус и тень
4. Менеджер: «та же цена, просто другой подъезд»
5. Семья **не подписывает** ДДУ; **часть брони удерживают**; эскроу не открывали

## voice_angle (research)

«Солнце в шоу-руме, тень в черновике»: одинаковые цена, площадь и этаж могут скрывать смену секции и фактически другой объект.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4430 |
| новостройки (RU) | 927399 |
| квартиры с отделкой тюмень | 79 |
| тюмень новостройки квартира с отделкой | 25 |

Spine = новостройки Тюмень; механизм = шоу-рум / южная ориентация vs секция в проекте ДДУ / бронь.

## Anti-dupe (published siblings — другой plot)

B27 земля аренда vs обещание собственности в декларации; B28 газ КП vs декларация; B29 банк снял нулевой взнос за 6 дней до ДДУ; B25 отделка на приёмке; B23 квартира vs апартаменты в ДДУ. **B30 уникален:** шоу-рум юг → черновик ДДУ северная секция, та же площадь/этаж.

## Published titles (anti-repeat only — not style template)

- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B29: Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала
- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали

## Champion energy (formula, not copy)

«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял» — завершённое событие + противоречие + следствие.

## Task

Output **only** valid JSON for `title-brief.json`:

```json
{
  "topic_id": "B30",
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
- Clear subject (новостройка / шоу-рум / ДДУ / секция / бронь)
- Strong verb, active voice; temporal marker if it helps («за 5 дней до ДДУ», «в черновике ДДУ»)
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific ЖК/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen comments (may align with Scout angle above)
