# Title inputs — B24 — 2026-09-07

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-byl-12-j-etazh-na-klyuchah-otdali-kvartiru-na-2-m`

## Scout handoff
- cluster_id: ddu_floor_changed_at_keys_tyumen
- topic_market_focus: newbuild_only
- klyshin_hook: none (fresh Tyumen newbuild floor-mismatch casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру на 12-м этаже новостройки (вид, тишина, ценность), оплатила бронь, подписала ДДУ с этажом в приложении
  - risk: на выдаче ключей застройщик ведёт на 2-й этаж; ссылается на перераспределение в секции / техкоррекцию проекта; без акта стопорятся ипотека, регистрация и переезд; вид, шум, приватность и рыночная ценность другие
  - time: день выдачи ключей и приёмки, через 2–3 года после подписания ДДУ
  - finale: акт не подписан; «компенсация» скидкой на паркинг отклонена; претензия; давление ипотечными платежами; спор о замене объекта или расторжении ДДУ
- comment_magnet_angle: «В ДДУ чётко написан 12-й этаж, а на ключах дают 2-й: вы бы подписали акт ради мебели и ипотеки — или пошли бы в суд, даже если застройщик предложит скидку на паркинг?»
- title_draft (rework allowed): В Тюмени в ДДУ был 12-й этаж — на ключах отдали квартиру на 2-м
- story_dup_check: PASS — distinct: этаж/объект зафиксирован в брони и ДДУ vs другой физический этаж на ключах; не B12 (перенос сдачи), не B21 (кладовка), не B23 (апартаменты vs квартира), не B22 (ставка перед ДДУ)
- distinct_plot: подмена этажа при выдаче ключей после ДДУ; не площадь, не статус жилое/нежилое, не срок сдачи

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4663 (55+11176; RU225: 8691)
- support: «приемка новостроек тюмень» — 36
- support: «приемка квартиры в новостройке тюмень» — 33
- support: «купить новостройку в тюмени» — 865
- narrow tail «этаж новостройка дду» — empty; casus stays in headline, spine = новостройки тюмень

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ с 12-м этажом в приложении, выдача ключей с квартирой на 2-м этаже, отказ от акта приёмки, ипотека/регистрация на паузе
- Reader problem: купили «высокий» этаж по ДДУ; на ключах ведут на другой этаж; застройщик говорит про изменение проекта; без акта стоп ключи, регистрация, финальная стадия ипотеки
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка)
- Surprising fact: этаж — обязательная идентифицирующая характеристика объекта в ДДУ (ст. 4 214-ФЗ); правка проектной декларации ≠ согласие на другой лот
- Voice angle: не «царапина на приёмке», а подмена объекта, когда этаж прямо записан в договоре
- Finale: акт не подписан → скидка на паркинг отклонена → претензия и спор о замене/расторжении
- Distinct from B12 (сдвиг сдачи/эскроу), B21 (кладовка), B23 (апартаменты в выписке), B22 (ставка перед ДДУ), B09 (ЕГРН обременение)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени в ДДУ написали квартиру — в выписке оказались апартаменты» (B23 — другой plot)
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21), ставка ипотеки перед ДДУ (B22), апартаменты vs квартира в выписке (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на ключах», «в ДДУ», «на приёмке»)
- One variant only
- Include slug confirmation in angle or separate field if needed
- newbuild_only: headline must read as новостройка/ДДУ/ключи, not secondary market

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-ddu-byl-12-j-etazh-na-klyuchah-otdali-kvartiru-na-2-m",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
