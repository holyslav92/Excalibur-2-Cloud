# Title inputs — B24 — 2026-09-09

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-izmenili-proektnuyu-deklaraciyu-v-novoj-planirovke-propal-balkon-iz-dd`

## Scout handoff
- cluster_id: newbuild_project_declaration_balcony_removed_tyumen
- klyshin_hook: none (fresh Tyumen newbuild balcony/declaration casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала новостройку с застеклённым балконом/лоджией по приложению к ДДУ; дождалась ключей
  - risk: застройщик обновил проектную декларацию на наш.дом.рф и ссылается на «проект изменился»; на приёмке балкон/лоджия отсутствуют; план в ДДУ не совпадает с фактом
  - time: на приёмке перед подписанием акта; после публикации новой декларации
  - finale: акт не подписан; банк остановил последний ипотечный транш; претензия по 214-ФЗ
- comment_magnet_angle: «В приложении к ДДУ был балкон, на ключах его нет, а застройщик показывает новую декларацию: вы подпишете акт или пойдёте в претензию, даже если транш уже завис?»
- title_draft (rework allowed): В Тюмени изменили проектную декларацию — в новой планировке пропал балкон из ДДУ
- story_dup_check: PASS — distinct plot: исчезновение балкона/лоджии из плана ДДУ vs обновлённая проектная декларация на приёмке; не B21 (кладовка), не B23 (апартаменты в ЕГРН), не B20 (смена юрлица), не B22 (ставка перед ДДУ), не B12 (перенос сдачи)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4642 (55+11176; RU225: 8616)
- support: «проектная декларация застройщика» — 20
- support: «балкон новостройка» — 25 (child: «новостройки с балконами» — 13)
- support: «приемка квартиры в новостройке тюмень» — 30

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ с планом где есть балкон/лоджия, проектная декларация обновлена на наш.дом.рф, приёмка без балкона, ипотека на паузе
- Reader problem: в документах и при выборе был балкон; перед актом застройщик опирается на новую декларацию; ключи и финансирование зависли
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, застройщика)
- Surprising fact: публикация новой проектной декларации ≠ согласие дольщика изменить план в его ДДУ; решает подписанный ДДУ + приложение + факт на приёмке
- Voice angle: «проверил декларацию — а балкон исчез на ключах»; разрыв между декларацией и индивидуальным договором
- Finale: акт не подписан → банк остановил последний транш → претензия по 214-ФЗ
- Distinct from B21 (кладовка по ДДУ), B23 (апартаменты в ЕГРН), B20 (смена юрлица/эскроу), B22 (ставка перед ДДУ), B12 (перенос сдачи на год)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты» (B23 — другой plot)
«В Тюменi застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21), ставка ипотеки перед ДДУ (B22), апартаменты в ЕГРН (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на приёмке», «на ключах», «перед актом»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-izmenili-proektnuyu-deklaraciyu-v-novoj-planirovke-propal-balkon-iz-dd",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
