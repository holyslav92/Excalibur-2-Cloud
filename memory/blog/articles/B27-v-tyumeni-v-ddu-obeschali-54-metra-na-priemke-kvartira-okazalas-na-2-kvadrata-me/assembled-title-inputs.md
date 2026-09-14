# Title inputs — B27 — 2026-09-14

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Confirm title_draft as H1/title for topic B27 (verbatim). Write angle + comment_magnet only. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-obeschali-54-metra-na-priemke-kvartira-okazalas-na-2-kvadrata-me`

## Scout handoff
- cluster_id: newbuild_ddu_area_mismatch_acceptance_tyumen
- klyshin_hook: none
- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: в ДДУ и проектной декларации 54,2 м²; на приёмке замер БТИ/итоговый обмер 52,1 м² (−2,1 м²). Застройщик: «проектные отклонения в пределах нормы», цена не пересчитывается, акт подписать «как есть»
- dzen_casus_shape: PASS
  - event: семья пришла на приёмку двушки в новостройке Тюмени
  - risk: в ДДУ 54,2 м², итоговый обмер БТИ 52,1 м² (−2,1 м² ≈ 3,9%); менеджер ссылается на «допуск», перерасчёта нет
  - time: на приёмке; уведомление о готовности 11 дней назад; 48 часов до сгорания брони соседней планировки
  - finale: семья не подписала акт; направила претензию на перерасчёт; застройщик предложил скидку 90 тыс. вместо ~210 тыс. перерасчёта
- comment_magnet_angle: на приёмке площадь меньше на 2 квадрата, застройщик зовёт подписать акт «как есть» — скидка 90 тыс. или претензия с риском по ипотеке?
- title_draft (**MUST use verbatim** as h1 and title): В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше
- story_dup_check: PASS — distinct plot: несоответствие площади (ДДУ/проект vs факт/BТИ на приёмке)
- distinct_plot: площадь в ДДУ vs итоговый обмер; не B25 (отделка чистовая vs whitebox), не B23 (апартаменты), не B12 (срок сдачи), не B26 (РВЭ)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «приемка квартиры в новостройке тюмень» — 35 (55+11176)
- support: «площадь квартиры меньше чем в дду» — 61 (RU225); parent «площадь квартиры меньше дду» — 80
- rework: weak local P0 → spine через newbuild jargon: ДДУ, площадь, приёмка, перерасчёт, допуск, БТИ

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ с площадью 54,2 м², приёмка квартиры, итоговый обмер 52,1 м², спор о перерасчёте и «допустимом отклонении»
- Reader problem: покупатель видит площадь меньше ДДУ; менеджер предлагает подписать акт без перерасчёта
- Casus: собирательный тюменский сюжет 2026 (без имён, ЖК, банка)
- Voice angle: не «лишние сантиметры на рулетке», а квартира меньше на площадь, сопоставимую с частью кухни или гардеробной
- Surprising fact: универсального федерального допуска «до X м² без перерасчёта» в 214-ФЗ нет — решает пункт ДДУ; подпись акта не всегда лишает права на перерасчёт
- Finale: семья не подписала акт, направила претензию
- Distinct from B25 (чистовая vs голые стены), B23 (апартаменты), B12 (перенос сдачи), B26 (РВЭ)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали» (B25 — другой plot: отделка)

## Anti-dup published titles
B02–B15, B19–B26 published. B25 sibling — чистовая на приёмке, другой cluster.
Avoid angles: расписка, задаток, отделка/whitebox (B25), апартаменты (B23), срок сдачи (B12), РВЭ (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker when it helps («на приёмке», «в ДДУ»)
- One variant only
- Clear subject: площадь / ДДУ / приёмка новостройки

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше",
  "title": "В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-ddu-obeschali-54-metra-na-priemke-kvartira-okazalas-na-2-kvadrata-me",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
