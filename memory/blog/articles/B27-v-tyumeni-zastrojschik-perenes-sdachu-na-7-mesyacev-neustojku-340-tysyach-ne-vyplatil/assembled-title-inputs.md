# Title inputs — B27 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## Scout handoff
- cluster_id: newbuild_delivery_delay_penalty_not_paid
- klyshin_hook: none (fresh Tyumen newbuild casus — Klyshin rhythm without copy-paste)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в новостройке по ДДУ; за три недели до обещанной передачи ключей застройщик уведомил о переносе срока сдачи на семь месяцев
  - risk: после фактической просрочки дольщики рассчитали неустойку примерно в 340 тысяч рублей по 214-ФЗ; застройщик признал перенос, но деньги не выплатил и предложил подписать дополнительное соглашение без условия о неустойке
  - time: спустя семь месяцев после первоначальной даты передачи по ДДУ; претензия с расчётом направлена в течение двух недель после наступления фактической просрочки
  - finale: ключи семья получила с задержкой, деньги с эскроу после ввода уже ушли застройщику, но 340 тысяч рублей не перечислены; семья не подписала допсоглашение; конфликт перешёл в досудебную претензию и возможный суд
- comment_magnet_angle: «Вы бы подписали допсоглашение о переносе срока, если в нём нет ни слова о неустойке — ради надежды быстрее получить ключи?»
- title_draft (rework allowed): В Тюмени застройщик перенёс сдачу на 7 месяцев — неустойку 340 тысяч не выплатил
- story_dup_check: PASS — distinct from B12 (escrow freeze + termination after year delay), certificate compensation cluster, acceptance-with-defects cluster

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «неустойка застройщик дду» — 18 (55+11176)
- secondary: «взыскать неустойку с застройщика» — 13 (55+11176)
- context: «неустойка с застройщика» — 3701 (RU225)
- context: «новостройки тюмень» — 4660 (55+11176)

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, перенос сдачи на 7 месяцев, неустойка ~340 тыс. руб., допсоглашение без неустойки
- Reader problem: за три недели до ключей — письмо о переносе на 7 месяцев; ипотека капает; после просрочки претензия с расчётом неустойки; застройщик признаёт перенос, но деньги не платит и тянет на «чистое» допсоглашение
- Casus: моделируемый/собирательный тюменский кейс (сентябрь 2026), без выдуманных имён/адресов ЖК/застройщика/банка
- Surprising fact: письмо о переносе само по себе не меняет договорную дату в зарегистрированном ДДУ; раскрытие эскроу после ввода не означает, что спор о неустойке исчерпан
- Fresh regional signal (NOT the family case): ЖК «Сикрет Плэйс» — перенос сроков, 24.08.2026 (ЕИСЖС); доля задержек в Тюмени выросла до 53,1% (РБК УрФО, 28.05.2026)
- Finale: ключи получены с задержкой; эскроу у застройщика; 340 тыс. не выплачены; досудебная претензия / возможный суд
- Distinct from B12: там расторжение и заморозка эскроу до ввода; здесь — ключи получены, эскроу раскрыт, но неустойку не платят и давят допсоглашением

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

Klyshin rhythm target: casus + number + punch — завершённое событие, конкретная цифра (7 месяцев / 340 тысяч), ударный финал.

## Anti-dup published titles
B02–B15, B19–B23 published. Avoid angles: расписка, задаток/торги, доверенность, автооценка, наследство, ЗАГС, ЕГРН обременение (B09), пожилой по телефону (B10), открытая кухня (B11), **B12 перенос на год + эскроу заморозили + ипотека**, смена юрлица/эскроу (B20), ипотека перед ДДУ (B22), апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tails, label heads

## Constraints
- Max ~70 chars (~50–70 ideal)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps
- One variant only
- Clear subject (новостройка / застройщик / неустойка / ДДУ)

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
