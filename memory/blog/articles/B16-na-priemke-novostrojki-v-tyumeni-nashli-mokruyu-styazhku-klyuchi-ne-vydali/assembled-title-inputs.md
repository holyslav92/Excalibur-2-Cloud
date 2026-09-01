# Title inputs — B16 — 2026-09-01

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B16. verdict: PASS.

## topic_id
B16

## Scout handoff
- cluster_id: newbuild_acceptance_defects_refuse_act
- klyshin_hook: none (fresh Tyumen newbuild acceptance casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени пришла на приёмку квартиры в новостройке с ипотекой и отделкой; во время осмотра обнаружили мокрую стяжку, трещину в стене и промерзший подоконник
  - risk: подписание акта приёмки-передачи без полной фиксации недостатков может осложнить требование о бесплатном устранении дефектов; застройщик предлагает подписать акт с обещанием исправить всё позже, но ключи не выдаёт до подписи
  - time: в день назначенной приёмки, за две недели до окончания гарантийного срока на устранение по ДДУ
  - finale: семья не подписала акт; дефекты зафиксировали в двух экземплярах с фото и видео; застройщик перенёс выдачу ключей на 45 дней — семья продолжает платить ипотеку без заселения
- comment_magnet_angle: «Если застройщик обещает всё исправить после подписи — вы подписываете акт или уходите без ключей?»
- title_draft (rework allowed): На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали
- story_dup_check: PASS
- Distinct from B12: здесь дефекты при приёмке и отказ от акта, НЕ перенос сдачи/эскроу

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «приемка квартиры в новостройке тюмень» — 29 (55+11176)
- broad: «приёмка квартиры в новостройке» — 108 (Tyumen)
- secondary: «приёмка квартиры в новостройке на что обратить» — 17
- context: «подписание акта приемки квартиры в новостройке» — 58 (RU225)
- context: «существенные недостатки при приемке новостройки» — 22 (RU225)
- low: «акт приемки квартиры в новостройке» — 7 (Tyumen)

## Research — subject & conflict
- Subject: приёмка квартиры в новостройке Тюмень, мокрая стяжка и другие дефекты, отказ подписать акт, ключи не выдали
- Reader problem: на приёмке видны дефекты, застройщик говорит «подпишите — исправим потом», ключи не отдают до подписи; страх потерять требования и остаться без квартиры при ипотеке
- Casus: моделируемый/собирательный тюменский кейс (сентябрь 2026), без выдуманных имён/адресов/сумм
- Surprising fact: с 01.01.2026 специалист СРО нужен при любых разногласиях по перечню недостатков
- Fresh regional signal (NOT the family case): MegaTyumen 02.08.2026 — жалобы на протечки/сырость в ЖК «Дом на Мысу»; tyumen-info 27.08.2026 — СК по нарушениям застройщика
- Finale: отказ от акта → фиксация дефектов → перенос ключей на 45 дней → ипотека без заселения
- Distinct from B12 (сдача/эскроу), B09 (ЕГРН), B11 (перепланировка)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B15 published. Avoid repeating angles: расписка, задаток/торги, доверенность, автооценка, наследство, ЗАГС, ЕГРН обременение (B09), пожилой по телефону, открытая кухня (B11), перенос сдачи/эскроу (B12), поддельное согласие (B15). B16 = дефекты на приёмке + отказ от акта + ключи.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps
- One variant only

## Required JSON output
```json
{
  "topic_id": "B16",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
