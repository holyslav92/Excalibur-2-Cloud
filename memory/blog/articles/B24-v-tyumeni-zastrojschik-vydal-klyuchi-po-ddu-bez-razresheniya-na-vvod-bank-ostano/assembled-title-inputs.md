# Title inputs — B24 — 2026-09-08

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## Scout handoff
- cluster_id: newbuild_keys_without_commissioning_mortgage_hold_tyumen
- klyshin_hook: none (fresh Tyumen casus without Klyshin — preferred)
- dzen_casus_shape: PASS
  - event: семья в Тюмени получила ключи по ДДУ, подписала акт приёма-передачи, начала ремонт
  - risk: разрешения на ввод (РНВ) в реестре ещё нет — банк не переводит остаток ипотеки на эскроу; семья платит из своих
  - time: 5–10 дней после подписания акта, при запросе остатка кредита
  - finale: банк заморозил выдачу до РНВ; застройщик ссылается на подписанный акт; семья остановила приёмку, подала претензию — спор
- comment_magnet_angle: «Ключи на руках, а ипотека не дошла: подписали бы акт без РНВ или ждали разрешение на ввод?»
- title_draft (rework allowed): В Тюмени застройщик выдал ключи по ДДУ без разрешения на ввод — банк остановил остаток ипотеки
- story_dup_check: PASS — distinct from B12 (перенос сдачи / эскроу после внесения), B19, B22, B23

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить квартиру в тюмени новостройка ипотека» — 85 (55+11176); 123 (RU225)
- secondary: «ввод жк в эксплуатацию» — 21
- secondary: «разрешение на ввод в эксплуатацию жк» — 9
- rework: demand spine через Tyumen newbuild jargon (новостройка, ДДУ, ипотека, застройщик) — не вставлять сырую фразу в H1

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, ключи и акт до РНВ, остаток ипотеки на эскроу
- Reader problem: ключи на руках, ремонт начат — банк остановил остаток ипотеки, потому что в реестре нет разрешения на ввод
- Casus: собирательный тюменский кейс (сентябрь 2026), без имён/адресов/сумм
- Surprising fact: 214-ФЗ привязывает эскроу к вводу, а не к подписи акта — ключи могут быть, а остаток ипотеки нет
- Fresh signal: реестровая модель РНВ с 01.09.2026 (svoedom.ru 31.08.2026)
- Distinct from B12: там деньги на эскроу, ключей нет (перенос сдачи); B24 — ключи есть, остаток не дошёл
- voice_angle: «бумага чистая — пока не проверил реестр»

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B15, B19–B23 published. Avoid: перенос сдачи на год (B12), маткапитал/эскроу (B19), ставка перед ДДУ (B22), апартаменты (B23), смена юрлица (B20).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tail

## Constraints
- Max ~70 chars (~50–70 preferred)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps
- One variant only
- Klyshin rhythm: завершённое событие + противоречие + следствие
- Clear subject (новостройка/ДДУ/ипотека/застройщик)

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
