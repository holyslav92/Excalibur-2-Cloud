# Title inputs — B26 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE Klyshin-style screaming clickbait H1 for topic B26: **casus + digit + punch**. Truth from article facts. Ban calm guides. verdict: PASS.

## topic_id
B26

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-ne-podpisali-akt-s-brakom-zastrojschik-vystavil-shtraf-190-tysyach`

## Scout handoff
- cluster_id: newbuild_acceptance_defect_penalty_clause_tyumen
- klyshin_hook: none (fresh Tyumen newbuild acceptance/defect casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья с детьми в Тюмени дождалась сдачи корпуса в новостройке, пришла на приёмку с чек-листом
  - risk: кривые стены, щели в окнах, неработающая вентиляция; акт не подписан; застройщик сослался на штрафную оговорку ДДУ за «необоснованное уклонение от приёмки» без оговорки о браке
  - time: 14 календарных дней после уведомления о готовности к передаче
  - finale: застройщик выставил претензию ~190 000 ₽; банк заморозил финальный транш ипотеки; семья направила встречную претензию с актом осмотра и фото; ключи не получены; спор в досудебной стадии
- comment_magnet_angle: «Если на приёмке нашли брак, а застройщик шлёт штраф за „затягивание“ — вы подпишете акт „без претензий“ ради ключей или будете спорить, даже если ипотека висит?»
- title_draft (rework allowed): В Тюмени не подписали акт с браком — застройщик выставил штраф 190 тысяч
- story_dup_check: PASS — distinct from B12 (handover delay/escrow freeze), B19 (matkapital/escrow), B21 (kladovka), B22 (rate change before DDU), B23 (apartments in EGRN)
- distinct_plot: приёмка новостройки с дефектами → отказ от акта → договорный штраф дольщику ~190k + банк держит финальный транш

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 3640 (55) / 8705 (225); live MCP-KV 4660 (55+11176)
- support: «приемка новостройки» RU225 — 7098
- support: «приемка квартиры в новостройке» — 6211
- weak local: «приемка квартиры в новостройке тюмень» — 33
- probes «штраф за просрочку приемки», «дефекты приемка новостройка» — no reliable volume

## Research — subject & conflict
- Subject: приёмка квартиры в тюменской новостройке по ДДУ; семья с детьми, семейная ипотека, эскроу
- Reader problem: нашли брак на приёмке, не подписали акт — через 14 дней штраф ~190 000 ₽; банк не выдал финальный транш без акта; аренда и платежи продолжаются
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм договора)
- Defects: кривые стены, щели в окнах, неработающая вентиляция; акт осмотра с фото
- Legal spine: отказ при дефектах по ст. 8 ч. 5 214-ФЗ ≠ «уклонение» по пункту ДДУ; штраф 190k — договорная неустойка (~0,1%/день × 14 дней, иллюстрация)
- Surprising fact: законный отказ подписать акт при браке — не автоматическое уклонение; договорный штраф и односторонний акт — разные механизмы
- Voice angle: застройщик переводит спор о браке в денежный счёт «за затягивание», банк ждёт акт — семья платит за аренду и по траншу без ключей
- Finale: встречная претензия; ключи не получены; досудебная стадия; семья не подписала акт «без претензий» под давлением штрафа

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени не подписали акт с браком — застройщик выставил штраф 190 тысяч» (draft energy — sharpen with digit + punch)
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), апартаменты в выписке (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, calm how-to guides

## Constraints
- Klyshin rhythm: завершённое событие + противоречие + следствие; **digit 190** in H1 when factual
- Max ~50–70 chars
- Strong verb, active voice, temporal marker («через 14 дней», «на приёмке»)
- Tyumen when relevant
- One variant only
- News-casus, not checklist

## Required JSON output
```json
{
  "topic_id": "B26",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-ne-podpisali-akt-s-brakom-zastrojschik-vystavil-shtraf-190-tysyach",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
