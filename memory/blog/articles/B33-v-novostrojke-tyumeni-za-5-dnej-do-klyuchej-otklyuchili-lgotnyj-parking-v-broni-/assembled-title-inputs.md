# Assembled title inputs — B33 (Derouter title role)

**topic_id:** B33  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**slug:** v-novostrojke-tyumeni-za-5-dnej-do-klyuchej-otklyuchili-lgotnyj-parking-v-broni-  
**research_date:** 2026-09-26

## Scout handoff / klyshin_hook

- **cluster_id:** `newbuild_parking_promo_revoked_before_keys_tyumen`
- **top_energy_mirror:** number_claimed_vs_unpaid (обещали «0 ₽ полгода» — перед ключами тариф включили)
- **dzen_casus_shape:** PASS
- **klyshin_hook:** none
- **comment_magnet_angle (Scout):** «Если паркинг «бесплатно полгода» пропадает за неделю до ключей — вы всё равно подписываете акт или торгуетесь?»
- **anti_dupe_hard:** PASS — distinct from LIVE separate DDU parking (2026-09-25); here **льготный тариф в брони отозван** за 5 дней до ключей

## Editorial spine (composite Tyumen newbuild casus — do NOT name ЖК, developer, bank, УК)

1. Семья покупает квартиру в новостройке Тюмени
2. В брони/КП: льготный паркинг — **6 месяцев бесплатно** или 0 ₽
3. Семья закладывает отсутствие платежа в бюджет
4. За **5 дней** до выдачи ключей УК/застройщик включает платный тариф **~8–12 тыс. ₽/мес**
5. Льгота «как в брони» в личном кабинете УК не видна
6. Семья **останавливает** подписание акта по квартире или ведёт переговоры о **письменном** продлении акции (agency, not panic)

**Not this plot:** отдельный ДДУ только на машино-место (соседний опубликованный угол 2026-09-25).

## voice_angle (from research)

Спокойный, процедурный: квартира по ДДУ ≠ паркинг по другому договору/УК; сверить бронь с подписанным пакетом; запросить перенос льготы **до** давления «подпишите акт сегодня».

## surprising_fact (for angle, not necessarily in H1)

Сила позиции — не слоган «в подарок», а попала ли льгота в **договор на машино-место** или договор с УК.

## Wordstat demand spine (P0 — не вставлять в H1 дословно)

| phrase | volume (55 / notes) |
|--------|---------------------:|
| новостройки тюмень | 3504 (research) / 4326 (scout handoff) |
| купить новостройку в тюмени | 892 |
| паркинг тюмень | 736 |

Spine = новостройки Тюмень + покупка новостройки; механизм = паркинг/льгота в брони vs платный тариф перед ключами.

## Anti-dupe (published siblings — другой plot)

- B21: кладовка по ДДУ на ключах — помещения не было
- B25: чистовая в ДДУ — акт не подписали
- B27/B28: бронь/КП vs декларация (земля, газ) — отказ до ДДУ
- B12: срок сдачи / эскроу
- **B33 уникален:** льготный **паркинг в брони** отозван за **5 дней до ключей**, не отдельный ДДU-only parking plot

## Published titles (anti-repeat only — not style template)

- B28: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- B27: За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду
- B25: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали
- B12: Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась

## Champion energy (formula, not copy)

«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял» — завершённое событие + противоречие + следствие.

## Scout title draft (too long — compress to ~50–70 chars)

> В новостройке Тюмени за 5 дней до ключей отключили льготный паркинг — в брони обещали полгода бесплатно

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
- Clear subject (новостройка / паркинг / льгота в брони)
- Strong verb, active voice; temporal marker («за 5 дней до ключей»)
- No SEO tail, no «чеклист», no «2026», no colon+keyword spam
- No naming specific ЖК/developer/bank/УК
- `comment_magnet_angle` = sharp debate question for Dzen comments (can refine Scout angle)
- `h1` and `title` same string
