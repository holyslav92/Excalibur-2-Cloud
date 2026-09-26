# Description inputs — B33 — 2026-09-26

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B33

## pipeline_canon
human-first-v2 (Sol complete — article.html final)

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** За 5 дней до ДДУ в новостройке площадь упала с 54 до 49 м²

**subject:** площадь и планировка квартиры в новостройке между бронью и ДДУ

**angle:** Бронь показывала 54 м², но за пять дней до подписания ДДУ в документах появилась квартира площадью 49 м² без снижения цены.

**comment_magnet_angle:** Подписали бы ДДУ с обещанием пересчитать площадь по БТИ или сразу сняли бы бронь?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За пять дней до подписания ДДУ семья в Тюмени увидела: вместо обещанных 54,2 м² в документах стоит 49,1 м², а цена квартиры не изменилась. Бронь уже оплачена, в планах — семейная ипотека и переезд с ребёнком. Ещё недавно в офисе показывали лоджию, две комнаты и понятную планировку. Теперь на столе лежал лист с другой конфигурацией, а менеджер говорил: «Это та же квартира, площадь пересчитаем по БТИ». Покажу, на каком месте в такой ситуации лучше остановиться, пока ДДУ не подписан и эскроу не открыт.

**Para 2 (early CTA):** Разбираю такие ситуации с новостройками Тюмени в Telegram и MAX: что проверить до подписи и где остановиться, пока деньги ещё можно вернуть по условиям сделки.

## Case hook (from research / article)
- Тюмень, новостройка, семья с ребёнком, семейная ипотека
- Бронь ~80–150 тыс. ₽; в офисе показывали ~54,2 м² с лоджией и двумя комнатами
- За 5 дней до ДДУ: в декларации/экспликации 49,1 м², другая схема, цена прежняя
- Менеджер: «та же квартира, пересчитаем по БТИ»
- Банк пересмотрел одобрение; ДДУ не подписали, эскроу не открыли, бронь отменили
- Смысл: бронь ≠ гарантия планировки; проект ДДУ — опора до подписи; БТИ не отменяет расхождение до договора
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- новостройки тюмень, ДДУ, бронь, площадь квартиры, проектная декларация, семейная ипотека, эскроу

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, БТИ

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B33",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
