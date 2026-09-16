# Title inputs — B27 — 2026-09-16

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-klyuchi-ot-novostrojki-vydali-s-opozdaniem-na-9-mesyacev-neustojku-na-`

## Scout handoff
- cluster_id: keys_delay_penalty_unpaid
- klyshin_hook: none (fresh Tyumen newbuild keys-delay + unpaid penalty without Klyshin)
- top_energy_mirror: clock_ran_out
- newbuild_mechanism: срок передачи по ДДУ прошёл на 9 месяцев; ключи выдали с опозданием; застройщик признал просрочку и обещал неустойку по 214-ФЗ; семья подписала акт с оговоркой о взыскании; претензия с расчётом ~380 тыс.; застройщик сослался на «отсрочку исполнения» 2026; на счёт деньги не поступили — спор ушёл в суд
- why_newbuild_not_secondary: только ДДУ → срок передачи → акт → неустойка 214-ФЗ; без вторички/ЕГРН-сделки
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в ЖК по ДДУ с ипотекой; дата передачи в договоре прошла, ключи молчали
  - risk: каждый месяц просрочки — аренда + ипотека; после выдачи ключей неустойка как единственный «возврат» за год ожидания; застройщик тянет выплату
  - time: 9 месяцев после договорной даты; ключи на 271-й день просрочки; через 4 месяца после акта — ноль на счёте по претензии
  - finale: акт подписан с оговоркой; претензия с расчётом ~380 тыс. — ответ «отсрочка до конца 2026»; семья подала в суд, ДДУ не расторгали
- comment_magnet_angle: «Ключи уже в руках, а неустойку за год ждут четвёртый месяц: вы бы подписали акт без оговорки ради заселения или тормозили до перевода денег на счёт?»
- title_draft (rework allowed): В Тюмени ключи от новостройки выдали с опозданием на 9 месяцев — неустойку на счёт так и не перевели
- story_dup_check: PASS — distinct from B12 (перенос сдачи до ключей + эскроу), B26 (РВЭ + второй транш), B25 (отделка на приёмке)
- h1_fingerprint: keys_after_9_month_delay_penalty_not_paid

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «неустойка застройщика» — 134 (55+11176) / 8156 (RU225)
- support: «неустойка с застройщика» — 56; «неустойка за просрочку застройщика» — 23
- support: «претензия застройщику неустойка» — 15
- context: «новостройки тюмень» — 4475 (buyer spine)
- rework: weak tail «неустойка застройщика за просрочку сдачи» (3) → spine через newbuild jargon: ключи, ДДУ, акт, неустойка, претензия

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, задержка передачи ~9 месяцев, передаточный акт с оговоркой, неустойка застройщика по 214-ФЗ, претензия без выплаты
- Reader problem: ключи уже получены, но застройщик не перечисляет рассчитанную неустойку и ссылается на отсрочку; непонятно, можно ли было подписывать акт и как не потерять денежное требование
- Casus: modeled composite Tyumen 2026 (без имён, ЖК, банка, номера иска)
- Voice angle: контраст «ключи есть / отделка идёт» vs «деньги за просрочку не пришли»
- Surprising fact: подписанный акт останавливает начисление новых дней неустойки, но не превращает уже рассчитанное требование в деньги на счёте
- Finale: иск подан, деньги не пришли, ДДУ действует
- Distinct from B12 (перенос срока ДО ключей, эскроу заморожен), B26 (РВЭ/второй транш), B25 (чистовая vs голые стены на приёмке)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot: до ключей)

## Anti-dup published titles
B02–B15, B19–B23, B25, B26 published. Avoid: расписка, задаток, доверенность, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня, перенос сдачи до ключей (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), апартаменты (B23), чистовая на приёмке (B25), РВЭ/второй транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker when it helps («через 9 месяцев», «после акта», «на 271-й день»)
- One variant only
- Clear subject: ключи/новостройка/неустойка застройщика/ДДУ
- Angle must differ from B12 (перенос ДО ключей) — here keys ARE received, penalty NOT paid
- **HARD:** H1 MUST contain at least one newbuild marker: «новостройк*», «ДДУ», «застройщик*», «ЖК» — otherwise topic_focus gate BLOCKER
- Prefer «новостройк*» or «застройщик*» in H1 (demand spine «неустойка застройщика» without pasting P0 verbatim)

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-klyuchi-ot-novostrojki-vydali-s-opozdaniem-na-9-mesyacev-neustojku-na-",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
