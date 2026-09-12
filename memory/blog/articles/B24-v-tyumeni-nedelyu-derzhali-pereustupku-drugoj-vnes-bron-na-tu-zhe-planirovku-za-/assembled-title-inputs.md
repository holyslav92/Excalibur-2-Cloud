# Title inputs — B24 — 2026-09-12

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-nedelyu-derzhali-pereustupku-drugoj-vnes-bron-na-tu-zhe-planirovku-za-`

## Scout handoff
- cluster_id: assignment_lost_to_faster_buyer
- top_energy_mirror: someone_else_took_object
- newbuild_mechanism: переуступка прав по ДДУ — семья согласовала цену с цессионарием, ждала документы неделю; застройщик принял бронь от другого покупателя на ту же планировку/лот
- why_newbuild_not_secondary: сделка через договор цессии к ДДУ застройщика, бронь в офисе продаж ЖК — не вторичный договор купли-продажи
- klyshin_hook: none (no fresh TG; avoid dupe risk)
- dzen_casus_shape: PASS
  - event: семья договорилась о переуступке, отложила бронь «до готовности пакета документов»
  - risk: застройщик не держит устную бронь — лот уходит тому, кто внёс деньги первым
  - time: «неделю ждали» → «за сутки до их визита бронь сняли»
  - finale: объект ушёл другому покупателю; аванс по цессии не вносили — потеряли планировку и цену, не деньги на эскроу
- comment_magnet_angle: «Переуступку можно „держать“ без брони у застройщика — или это самообман?»
- title_draft (rework allowed): В Тюмени неделю держали переуступку — другой внёс бронь на ту же планировку за сутки
- story_dup_check: PASS — distinct from booking_expired_price_hike (+280k), B22 mortgage rate before DDU, trade_in_rejected, B19 escrow/matkapital

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 909 (55+11176)
- support: «новостройки тюмень» — 4560
- weak local: «переуступка тюмень» — 8; «переуступка новостройки» — 14 (55+11176)
- national spine: «переуступка новостройка» — 2475 (RU225)
- rework: anchor buyer-intent на новостройку + casus hook переуступка/бронь (не вставлять сырую фразу в H1)

## Research — subject & conflict
- Subject: переуступка в тюменской новостройке, устная «бронь» без денег у застройщика, конкуренция за планировку
- Reader problem: покупатель думает, что договорённость с цессионарием = объект «их»; застройщик продаёт лот первому с оплаченной бронью
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка)
- Surprising fact: неделя согласований с продавцом по переуступке не мешает застройщику принять бронь от третьего лица на тот же лот
- Voice angle: разрыв между «мы уже договорились» и офисом продаж, где действует правило «кто первый внёс бронь»
- Finale: планировка и цена ушли; деньги на эскроу не зависли — потеряли шанс, не депозит
- Distinct from published Dzen angles: +280 тыс. к переуступке за сутки (price hike plot); B22 bank rate; trade-in срыв

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: ставка, не переуступка)
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22), квартира vs апартаменты в ДДУ (B23). Не дублировать «переуступку подняли на 280 тысяч» — другой механизм (цена vs очередь брони).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO-хвосты, двоеточие+ключ

## Constraints
- Max ~50–70 chars (Cyrillic)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («неделю», «за сутки»)
- Clear subject: переуступка / бронь / новостройка
- One variant only

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-nedelyu-derzhali-pereustupku-drugoj-vnes-bron-na-tu-zhe-planirovku-za-",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
