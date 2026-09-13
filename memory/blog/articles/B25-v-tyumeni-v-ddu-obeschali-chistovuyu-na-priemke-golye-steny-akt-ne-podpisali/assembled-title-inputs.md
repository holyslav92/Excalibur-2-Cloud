# Title inputs — B25 — 2026-09-13

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B25. verdict: PASS.

## topic_id
B25

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-obeschali-chistovuyu-na-priemke-golye-steny-akt-ne-podpisali`

## Scout handoff
- cluster_id: newbuild_ddu_finishing_mismatch_acceptance_tyumen
- klyshin_hook: none (fresh Tyumen newbuild finishing-mismatch casus without Klyshin)
- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: в приложении к ДДУ указана чистовая отделка — на приёмке квартиры фактически whitebox/голые стены; семья отказалась подписывать акт приёма-передачи до сверки спецификации
- dzen_casus_shape: PASS
  - event: семья пришла на приёмку квартиры в новостройке Тюмени
  - risk: в ДДУ и приложении обещана чистовая отделка (ламинат, обои, сантехника), на объекте — предчистовая/white box: нет финишного пола, плитки, обоев, сантехники
  - time: на приёмке, за 48 часов до дедлайна подписания акта (7 рабочих дней по 214-ФЗ)
  - finale: акт приёма-передачи не подписали; составили акт осмотра с перечнем расхождений, фото/видео; ключи не выдали; менеджер предлагал подписать сейчас и «доделать потом»
- comment_magnet_angle: «Вы бы подписали акт с голыми стенами, если в ДДУ написано „чистовая“?»
- title_draft (rework allowed): В Тюмени в ДДУ обещали чистовую — на приёмке голые стены, акт не подписали
- story_dup_check: PASS — distinct plot: несоответствие вида отделки (чистовая в приложении ДДУ vs whitebox на приёмке) → отказ подписать акт
- distinct_plot: расхождение «чистовая» в приложении ДДУ vs фактическая предчистовая/голые стены на приёмке; не B24 (паркинг/машиноместо продали дважды), не B12 (срок сдачи/эскроу), не B21 (кладовка), не B20 (смена юрлица), не B23 (апартаменты vs квартира), не B22 (ставка перед ДДУ)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «приемка квартиры в новостройке тюмень» — 35 (55+11176)
- support: «чистовая отделка новостройка» — 3158 (RU225); «новостройки с чистовой отделкой» — 1620
- support: «предчистовая отделка новостройка» — 3342; «что значит чистовая отделка в новостройке» — 217
- rework: weak local P0 → spine через newbuild jargon: приложение ДДУ, чистовая vs предчистовая, white box, акт осмотра

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ с приложением «чистовая отделка», приёмка квартиры, расхождение с white box/голыми стенами, передаточный акт vs акт осмотра
- Reader problem: покупатель приходит принимать квартиру с обещанной чистовой, видит предчистовую; менеджер предлагает подписать акт сейчас и доделать потом
- Casus: собирательный тюmenский сюжет 2026 (без имён, ЖК, банка, суммы)
- Voice angle: «бумажная чистовая» — в приложении перечень отделки, на объекте белая коробка
- Surprising fact: для ДДУ с 01.01.2025 денежные требования по недостаткам отделки ограничены 3% цены договора — «взять деньги и сделать самому» не всегда покрывает разницу
- Finale: семья не подписала передаточный акт; зафиксировала расхождения актом осмотра; ключи под вопросом
- Distinct from B24 (паркинг продали дважды — published today), B23 (апартаменты в выписке), B21 (кладовка), B12 (перенос сдачи), B20 (смена юрлица), B22 (ставка перед ДДУ)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени в ДДУ написали квартиру — в выписке оказались апартаменты» (B23 — другой plot)
«V tyumeni oplatili kladovku po ddu na klyuchah pomescheniya ne bylo» (B21 — другой plot)

## Anti-dup published titles
B02–B15, B19–B23 published. B24 published today — parking/mashino-mesto double-sold (DO NOT reuse parking angle).
Avoid angles: расписка, задаток, доверенность, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), апартаменты (B23), паркинг/машиноместо (B24).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, паркинг, машиноместо, кладовка

## Constraints
- Max ~50–70 chars
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker when it helps («на приёмке», «в ДДУ», «акт не подписали»)
- One variant only
- Include slug confirmation in angle or separate field if needed
- Clear subject: чистовая отделка / приёмка новостройки / ДДУ

## Required JSON output
```json
{
  "topic_id": "B25",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-ddu-obeschali-chistovuyu-na-priemke-golye-steny-akt-ne-podpisali",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
