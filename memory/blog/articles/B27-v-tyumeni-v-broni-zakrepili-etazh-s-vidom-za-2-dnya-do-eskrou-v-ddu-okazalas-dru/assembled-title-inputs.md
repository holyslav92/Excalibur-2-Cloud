# Title inputs — B27 — 2026-09-15

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-broni-etazh-s-vidom-v-ddu-drugaya-sektsiya-sdelku-ostanovili`

## Scout handoff
- cluster_id: ddu_booking_floor_section_mismatch_tyumen
- klyshin_hook: none (fresh Tyumen newbuild casus; https://t.me/klyshin_A checked, not used)
- top_energy_mirror: paper_clean_then_broke — бронь и переписка выглядят чистыми, но в проекте ДДУ другой объект
- newbuild_mechanism: в платной брони зафиксированы этаж, вид на набережную и секция → за 48 ч до подписания ДДУ/эскроу в приложении другая секция, этаж на два ниже, окна во двор → семья не подписала, на эскроу 0 ₽
- why_newbuild_not_secondary: цепочка бронь→ДДУ→эскроу у застройщика; без вторички и ЕГРН
- dzen_casus_shape: PASS
  - event: семья с ребёнком в Тюмени забронировала квартиру в новостройке с видом на набережную; этаж, секцию и вид согласовали в листе бронирования и переписке
  - risk: за 48 часов до сделки в проекте ДДУ — другая секция, этаж на два ниже, окна во двор; подписание откроет ипотеку и эскроу на чужой лот
  - time: 48 часов до подписания ДДУ и открытия счёта эскроу
  - finale: сравнили бронь с приложением к ДДУ, отказались подписывать; «аналогичную» без вида не приняли; сделку остановили, бронь закрыли, на эскроу 0 ₽, ипотечное одобрение не использовали
- comment_magnet_angle: «В брони этаж и вид записаны, а в ДДУ — другая секция: вы бы подписали “с поправкой потом” или сняли бы бронь, даже если менеджер говорит, что квартира ещё есть?»
- title_draft (rework allowed): В Тюмени в брони закрепили этаж с видом — за 2 дня до эскроу в ДДУ оказалась другая секция, сделку остановили
- story_dup_check: PASS — distinct: booking_document_vs_DDU_attachment_object_mismatch (секция+этаж+вид), не приёмка, не смена планировки, не двойная бронь
- distinct_plot: расхождение брони и приложения к ДДУ по секции/этажу/виду до эскроу; не B22 (ставка перед ДДУ), не B23 (апартаменты), не B25 (чистовая на приёмке), не double_booking, не layout_swap

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 3536 (55) / 8388 (RU225)
- support: «новостройки в тюмени от застройщика» — 500; «купить новостройку в тюмени» — 683
- weak tails (do not use as H1 spine): «дду тюмень» 12; «бронь квартира новостройка» 1
- rework: buyer spine = покупка новостройки в Тюмени; конфликт через бронь/ДДУ/эскроу, не юридический хвост «дду тюмень»

## Research — subject & conflict
- Subject: новостройка в Тюмени, платная бронь с этажом и видом, проект ДДУ с приложением, эскроу, предварительное одобрение ипотеки
- Reader problem: покупатель считает бронь гарантией выбранной квартиры; за 48 ч до подписания в ДДУ — другой объект
- Casus: собирательный тюменский сюжет (без имён, ЖК, застройщика, суммы брони)
- Voice angle: бронь и ипотека создают ощущение «сделка почти готова», но до регистрации ДДУ можно остановиться; эскроу защищает деньги, не объект в брони
- Surprising fact: на эскроу 0 ₽ — отказ до регистрации ДДУ; плата за бронь — отдельный вопрос по договору бронирования
- Finale: отказ до подписи и регистрации ДДУ, эскроу не задействован
- Constraints: не обещать автовозврат брони; «вид» не всегда существенное условие ДДУ; не вторичка

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали» (B25 — другой plot)

## Anti-dup published titles
B02–B15, B19–B26 published. Avoid angles: расписка, задаток, доверенность, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), апартаменты (B23), чистовая на приёмке (B25), РВЭ/второй транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, паркинг, машиноместо, кладовка, апартаменты, чистовая отделка, приёмка, РВЭ, транш

## Constraints
- Target ~50–70 chars (scout draft ~95 — tighten while keeping stakes + newbuild marker)
- **HARD:** include «новостройк» or «застройщик» or «ДДУ» or «эскроу» or «бронь» in h1 (topic_focus gate)
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker when it helps («за 48 часов», «за 2 дня до эскроу»)
- One variant only
- Clear subject: бронь / ДДУ / секция / этаж / вид / новостройка / эскроу
- No SEO tail, no colon+keyword, no label head

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-broni-etazh-s-vidom-v-ddu-drugaya-sektsiya-sdelku-ostanovili",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
