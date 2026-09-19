# Title inputs — B28 — 2026-09-19

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B28. verdict: PASS.

## topic_id
B28

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-dome-kp-potolki-nizhe-ddu-na-25-santimetrov-zamer-na-sdache-pokazal-`

## Scout handoff
- cluster_id: newbuild_ceiling_height_below_ddu_kp_tyumen
- klyshin_hook: none (fresh Tyumen KP ceiling-height casus without Klyshin)
- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: ДДУ на индивидуальный дом в коттеджном посёлке под Тюменью; в приложении к ДДУ высота потолков **2,7 м**; на сдаче лазерный замер — **2,45 м** (−25 см); застройщик: «конструктивный допуск», скидка **80 000 ₽** вместо перерасчёта; семья не подписала акт, ключи не взяла, финальный транш на эскроу не переводился; через **9 дней** вернули задаток **250 000 ₽**, на регистрацию не вышли
- why_newbuild_not_secondary: только ДДУ на новый дом от застройщика в КП, не вторичка/ЕГРН/бабушка
- dzen_casus_shape: PASS
  - event: семья с детьми и инвестор выбрали дом в КП под Тюменью; в офисе — макет с «высокими потолками 2,7»
  - risk: фактическая высота ниже приложения к ДДУ; давление подписать акт «как есть» под скидку
  - time: день сдачи дома, замер перед актом приёма-передачи
  - finale: 2,45 м вместо 2,7 м; скидка 80 тыс. вместо перерасчёта; акт не подписали; задаток 250 тыс. вернули через 9 дней
- comment_magnet_angle (Scout): «Если потолки на 25 см ниже, чем в ДДУ, — вы подпишете акт за обещанную скидку или остановитесь до ключей?»
- title_draft (rework allowed — MUST shorten to ~50–70 chars): В Тюмени в доме КП потолки ниже ДДУ на 25 сантиметров — замер на сдаче показал 2,45 вместо 2,7 метра, перерасчёт отказали
- story_dup_check: PASS — distinct from B25 (чистовая отделка), B26 (РВЭ/транш), B27 (земля аренда), BTI площадь, acceptance_defects
- distinct_plot: количественное расхождение высоты потолков в приложении ДДУ vs замер на сдаче в **доме КП** (ИЖД), не квартира ЖК

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — **4430** (55+11176)
- support: «коттеджные поселки тюмень» — **1455**; «дома в тюмени от застройщика» — **253**
- weak: «приемка дома от застройщика» — 2; «высота потолков дду» — 0
- rework: spine новостройки/КП + механизм ДДУ/приложение/замер на сдаче в теле, не в H1

## Research — subject & conflict (research-notes.md)
- Subject: новый дом от застройщика в коттеджном посёлке под Тюменью, ДДУ с приложением 2,7 м потолки, сдача, лазерный замер 2,45 м, передаточный акт, скидка vs перерасчёт
- Reader problem: на передаче потолки ниже договора; менеджер давит скидкой вместо объяснения последствий
- Casus: modeled composite — без имён КП, застройщика, банка
- Voice angle: красивая цифра в офисе vs формулировка приложения к ДДУ и способ замера
- Surprising fact: 25 см — не «допуск отделки» (миллиметры), а расхождение с договорной высотой
- Finale: акт не подписан, ключи не выданы, задаток возвращён, регистрации нет

## Champion energy (formula, do NOT copy verbatim)
«В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали» (B25 — другой plot)
«За 4 дня до ДДУ в Тюмени обещали землю в собственности — декларация показала аренду» (B27)

## Anti-dup published titles
B02–B15, B19–B27 published. **Не** B25 (отделка), **не** B26 (РВЭ), **не** B27 (земля), **не** BTI площадь, **не** коттедж кадастр забор.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, приёмка дома (weak cluster tail as main hook)

## HARD GATE (topic_focus.py — MUST PASS)
H1 **must** contain an explicit newbuild marker: **ДДУ**, **КП**, **новостройк**, **застройщик**, **эскроу**, or **ЖК** (see shared/newbuild-focus-lock.md).  
Previous draft FAIL: «Под Тюменью замер выявил потолки ниже на 25 см — новый дом не приняли» → `NEWBUILD FOCUS BLOCKER` (only «дом»).

## Constraints
- Max ~50–70 chars (scout draft is TOO LONG — compress)
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild/KP house
- **Include «ДДУ» or «КП» in H1** (demand spine stays новостройки тюмень in body)
- Strong verb, active voice; temporal marker when it helps («на сдаче», «замер показал», «акт не подписали»)
- Clear subject: потолки / ДДУ / дом КП / замер
- One variant only

## Required JSON output
```json
{
  "topic_id": "B28",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-dome-kp-potolki-nizhe-ddu-na-25-santimetrov-zamer-na-sdache-pokazal-",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
