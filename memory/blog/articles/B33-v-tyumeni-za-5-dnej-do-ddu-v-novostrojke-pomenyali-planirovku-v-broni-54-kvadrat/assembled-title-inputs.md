# Assembled title inputs — B33 (Derouter title role)

**topic_id:** B33  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** v-tyumeni-za-5-dnej-do-ddu-v-novostrojke-pomenyali-planirovku-v-broni-54-kvadrat  
**research_date:** 2026-09-26

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_layout_area_mismatch_before_ddu_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none | original: none (use champion news-casus energy, not Klyshin copy)
- **comment_magnet_angle (Scout):** Если в брони 54 м², а в ДДУ 49 — подписали бы ДДУ при обещании «пересчёт по БТИ» или сняли бронь?

## Editorial spine (composite Tyumen casus — do NOT name ЖК, developer, bank)

1. Семья с ребёнком, семейная ипотека; бронь оплачена (~80–150 тыс ₽ ориентир)
2. В офисе и на визуализации — ~54,2 м², евродвушка с лоджией
3. За **5 дней** до подписания ДДУ менеджер присылает лист из декларации/приложения: **49,1 м²**, другая конфигурация, **цена не снижается**
4. Ответ: «та же квартира», «пересчитаем по БТИ» (БТИ — только готовый объект; до ДДУ сравнивают бронь, рекламу, декларацию, графический план в проекте ДДУ)
5. Банк пересматривает предварительное одобрение (взнос/лимит/пауза)
6. ДДУ не подписан, эскроу не открыт; сделку остановили, бронь отменили (возврат по условиям соглашения)

## voice_angle (research-notes)

Момент, когда лот из брони превращается в другой объект в проекте ДДУ. Напряжение: 5 дней до подписания, деньги в брони, ипотека на кону.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume |
|--------|-------:|
| новостройки тюмень | 4326 |
| купить новостройку в тюмени | 892 |
| новостройки в тюмени от застройщика | 630 |
| планировка квартира новостройка | 27 |
| проектная декларация застройщика | 25 |

Spine = новостройки Тюмень; механизм = планировка/площадь бронь vs проект ДДУ до подписания.

## Anti-dupe (published siblings — другой plot)

B27 земля аренда vs обещание собственности; B22 ставка; B29 нулевой взнос; B31 страховка; B32 чужое юрлицо в реквизитах; B25 чистовая на приёмке; B23 апартаменты в ДДУ. **B33 уникален:** смена площади и планировки **внутри одного лота** между бронью и проектом ДДУ за 5 дней до подписания.

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
- Clear subject (новостройка / планировка / площадь / ДДУ / бронь)
- Strong verb, active voice; temporal marker «за 5 дней до ДДУ» if it fits length
- Stakes: 54 vs 49 м² (можно «пять квадратов» или цифры — не дублировать fingerprint B27 «4 дня»)
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific ЖК/developer/bank
- `comment_magnet_angle` = sharp debate question for Dzen comments (can refine Scout angle)

published-titles-only.md is in article dir.
