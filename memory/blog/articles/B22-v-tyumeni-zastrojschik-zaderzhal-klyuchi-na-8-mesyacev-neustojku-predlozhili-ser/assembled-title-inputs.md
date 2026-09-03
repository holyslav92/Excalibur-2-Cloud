# Title inputs — B22 — 2026-09-03

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B22. verdict: PASS.

## topic_id
B22

## Scout handoff
- cluster_id: newbuild_developer_delay_penalty_certificate_instead_cash_tyumen
- klyshin_hook: none (fresh Tyumen casus without Klyshin — preferred)
- dzen_casus_shape: PASS
  - event: семья в Тюмени подписала ДДУ на квартиру в новостройке с установленной датой передачи ключей
  - risk: застройщик задержал выдачу ключей на 8 месяцев; по 214-ФЗ набежала неустойка; в день выдачи ключей менеджер предлагает сертификат на отделку/кладовку вместо денежной выплаты
  - time: через 8 месяцев после срока передачи в ДДУ, в день фактической выдачи ключей
  - finale: семья подписала допсоглашение с сертификатом; 8 месяцев платили ипотеку и аренду; номинал сертификата ниже законной неустойки; денежная компенсация не покрыла реальные потери
- comment_magnet_angle: «Просрочили сдачу на полгода — вы бы взяли сертификат на отделку вместо неустойки по ДДУ или пошли бы в суд?»
- title_draft (rework allowed): В Тюмени застройщик задержал ключи на 8 месяцев — неустойку предложили сертификатом
- story_dup_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «неустойка застройщик» — 257 (55:118 + 11176:139; RU225:8500)
- on-plot: «неустойка застройщик дду» — 33 (weak)
- context: «приемка квартиры в новостройке» — 92 (saturated cluster — not main hook)
- context: «мораторий на неустойку с застройщика» — 16 (2026 legal context)
- market context only: «новостройки тюмени от застройщика» — 1652 (not P0)

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, просрочка передачи 8 месяцев, неустойка по 214-ФЗ, сертификат вместо денег в день ключей
- Reader problem: 8 месяцев ждали ключи, платили ипотеку и аренду; в день передачи менеджер предлагает сертификат на отделку/кладовку вместо денежной неустойки
- Casus: моделируемый/собирательный тюменский кейс (сентябрь 2026), без выдуманных имён/адресов/сумм
- Voice angle: конфликт не в самой задержке, а в офисе выдачи ключей — «подарок» выглядит быстрым решением, но обменивает денежное требование на ограниченный бонус
- Surprising fact: уведомление о переносе не переписывает ДДУ; текст бумаги в день ключей важнее устных обещаний
- Fresh regional signals (NOT the family case): URA.RU 24.08.2026 переносы сроков; SuperOmsk 19.08.2026 иск к тюменскому застройщику >1 млн неустойки
- Distinct from B12 (перенос сдачи на год + эскроу заморозили), B21 (платная кладовка на ключах), приёмка/мокрая стяжка clusters

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B15, B19–B21 published. Avoid: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ЕГРН ипотека, пожилой по телефону, открытая кухня, перенос сдачи на год/эскроу (B12), маткапитал/эскроу (B19), смена юрлица (B20), платная кладовка (B21).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~70 chars
- News headline energy, Klyshin rhythm, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («8 месяцев», «в день ключей»)
- Clear subject: задержка ключей + сертификат вместо неустойки
- One variant only

## Required JSON output
```json
{
  "topic_id": "B22",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
