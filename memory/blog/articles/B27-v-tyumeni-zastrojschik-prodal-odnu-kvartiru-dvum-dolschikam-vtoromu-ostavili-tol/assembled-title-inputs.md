# Title inputs — B27 — 2026-09-14

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-dolschikam-vtoromu-ostavili-tol`

## Scout handoff
- cluster_id: double_sale_same_unit_newbuild
- klyshin_hook: none (fresh Tyumen newbuild double-sale casus without Klyshin)
- top_energy_mirror: lost_lot_before_escrow
- newbuild_mechanism: офис продаж оформил две брони на один условный номер квартиры в тюменской новостройке; первая семья подписала ДДУ и открыла эскроу на 11 дней раньше; вторая за 4 дня до своего эскроу узнала, что лот «уже у другого дольщика»; вернули 180 тыс. брони и предложили «похожую» квартиру с доплатой +390 тыс.; вторая подала претензию
- dzen_casus_shape: PASS
  - event: две семьи в тюменской новостройке выбрали один номер квартиры; менеджер оформил две брони на один лот в одну неделю
  - risk: бронь не блокирует повторную продажу лота; без регистрации ДДУ «окно» для второго покупателя; эскроу не спасает от потери выбранного лота
  - time: первая семья на 11 дней раньше с ДДУ и эскроу; вторая — за 4 дня до открытия эскроу
  - finale: второй семье вернули бронь, предложили другую секцию с доплатой; отказ от доплаты, претензия; первая продолжает сделку; спор не закрыт
- comment_magnet: один номер — два договора брони: доплатить 390 тыс. за «такую же» в соседней секции или требовать ту же цену?
- title_draft (rework allowed): В Тюмени застройщик продал одну квартиру двум дольщикам — второму оставили только бронь
- story_dup_check: PASS — distinct plot: двойная продажа одного лота (две брони/ДДУ), не переуступка, не сгоревшая бронь с ростом цены, не смена юрлица, не ставка перед ДДУ
- distinct_plot: один номер — две брони → вторая семья потеряла лот до эскроу; не B20 (юрлицо), не B22 (ставка), not B19 (маткапитал/эскроу), not assignment, not booking_expired_price_hike

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4502 (55+11176)
- support: «купить новостройку в тюмени» — 909; «договор долевого участия» — 373; «регистрация ДДУ» — 65
- rework: legal spine через ДДУ/регистрацию/бронь новостройки — не вставлять сырые фразы в H1

## Research — subject & conflict
- Subject: новостройка в Тюмени, двойная бронь/продажа одного номера квартиры, ДДУ vs бронь, эскроу, вторая семья потеряла лот
- Reader problem: семья внесла бронь, считает квартиру своей — офис сообщает, что лот оформляют другому
- Casus: редакционный тюменский сюжет 2026 (без имён, ЖК, банка)
- Voice angle: конфликт не «деньги с эскроу исчезли», а «один номер в двух договорах брони»; юридически решает регистрация ДДУ, не обещание менеджера
- Surprising fact: вторая семья не потеряла цену квартиры на эскроу — до него не дошла; болезненнее потеря выбранного лота и доплата за «аналог»
- Finale: возврат 180 тыс. брони, предложение другой секции +390 тыс., претензия, спор открыт

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)

## Anti-dup published titles
B02–B15, B19–B26 published. Avoid angles: расписка, задаток, доверенность, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня, перенос сдачи (B12), маткапитал/эскроу (B19), смена юрлица (B20), ставка перед ДДУ (B22), апартаменты (B23), чистовая (B25), РВЭ/транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tails, label heads

## Constraints
- Max ~50–70 chars (scout draft ~79 — tighten if possible while keeping stakes + newbuild marker)
- **HARD:** include «новостройк» or «застройщик» or «ДДУ» or «бронь» in h1 (topic_focus gate)
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker when it helps («за 4 дня до эскроу», «один номер — две брони»)
- One variant only
- Clear subject: двойная продажа / две брони / один номер / дольщики / новостройка
- No SEO tail, no «полный гайд», no checklist hook

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-dolschikam-vtoromu-ostavili-tol",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
