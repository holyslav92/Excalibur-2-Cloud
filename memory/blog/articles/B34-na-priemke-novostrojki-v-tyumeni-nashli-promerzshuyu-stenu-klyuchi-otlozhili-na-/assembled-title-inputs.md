# Title inputs — B34 — 2026-09-30

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier for title). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B34. verdict: PASS.

## topic_id
B34

## slug (confirm — article dir already fixed)
`na-priemke-novostrojki-v-tyumeni-nashli-promerzshuyu-stenu-klyuchi-otlozhili-na-`

## Scout handoff
- slot_rubric: novostroyki ONLY — no secondary/arenda mechanism in H1
- cluster_id: newbuild_acceptance_frost_damaged_wall_keys_delayed_tyumen
- klyshin_hook: none
- top_energy_mirror: almost_lost_before_keys + clock_ran_out_before_money
- newbuild_mechanism: приёмка квартиры у застройщика по ДДУ — существенный дефект стены до подписания акта; ключи и регистрация сдвигаются
- dzen_casus_shape: PASS
  - event: семья с детьми на финальной приёмке тюменской новостройки; ипотека и эскроу уже в сделке
  - risk: на стене признаки промерзания/намокания — не сводить к «косметике»
  - time: решение в день приёмки; застройщик озвучил ~40 дней на устранение
  - finale: передаточный акт не подписан до фиксации дефекта; ключи отложены; семья платит ипотеку и аренду параллельно
- comment_magnet_angle: Подписали бы акт с замечанием без независимой экспертизы ради ключей — или ждали бы 40 дней?
- title_draft (rework allowed): На приёмке новостройки в Тюмени нашли промёрзшую стену — ключи отложили на 40 дней
- story_dup_check: PASS — distinct: frost/wet wall at acceptance vs B25 (чистовая vs white box), B12 (перенос сдачи), B26 (РВЭ)
- distinct_plot: промёрзшая/влажная стена + отказ подписать акт + таймер 40 дней до ключей

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «приемка квартиры в новостройке тюмень» — 28 (55+11176); RU compare — 59
- support: «приемка квартиры в новостройке» — 122
- broad: «новостройки тюмень» — 3547
- support: «ипотека новостройка тюмень» — 153
- rework: probe новостройки → spine приёмка новостройки тюмень

## Research — subject & conflict
- Subject: приёмка новостройки Тюмень, ДДУ, холодная влажная стена, передаточный акт vs фиксация дефекта, ~40 дней ожидания, ипотека+аренда
- Reader problem: подписать акт ради ключей или ждать с доказательствами
- Voice angle: два риска — зафиксировать до передачи или подписать и доказывать потом
- Surprising fact: просрочка передачи и просрочка устранения дефекта — разные основания; не одна «неустойка за 40 дней»
- Finale: акт не подписан; фиксация наблюдений; обсуждение независимой проверки — не автоматическая неустойка
- Distinct from B25 (отделка чистовая/white box), B12 (срок сдачи/эскроу год), B26 (РВЭ/транш), B21/B20/B19 as main plot

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени в ДДУ обещали чистovую — на приёмке голые стены, акт не подписали» (B25 — другой plot)

## Anti-dup published titles
Avoid repeating angles from B25 (чистовая на приёмке), B12 (перенос сдачи), B26 (РВЭ), B33 (долг за свет вторичка), parking, кладовка, апартаменты, ставка перед ДДУ as main hook.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, вторичка, ЕГРН, бронь без newbuild acceptance context

## Constraints
- Max ~50–70 chars (можно чуть длиннее если casus ясен)
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild acceptance
- Strong verb, active voice; temporal marker: «на приёмке», «40 дней», «акт не подписали»
- One variant only
- Clear subject: приёмка новостройки / промёрзшая или влажная стена / ключи отложены

## Required JSON output
```json
{
  "topic_id": "B34",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "na-priemke-novostrojki-v-tyumeni-nashli-promerzshuyu-stenu-klyuchi-otlozhili-na-",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
