# Title inputs — B08 — 2026-08-22

## Task
Invent ONE H1/title for topic B08. Output JSON only per skill schema. verdict: PASS.

## topic_id
B08

## Scout handoff
- hook_id: pre_advance_check
- original: «Сначала проверка. Потом аванс.»
- dzen_casus_shape: PASS — ипотека одобрена, регистрация приостановлена/отказ из-за строки обременения в ЕГРН
- title_draft (inspire, not copy): Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка

## Wordstat demand spine (do NOT paste P0 into H1)
- P0: «купить квартиру в тюмени» — 22880
- stickers: «егрн» 7543; «выписка из егрн» 2648; «выписка егрн квартира» 246

## Research — subject & conflict
- Subject: одобрение ипотеки ≠ чистая выписка ЕГРН; действующее обременение
- Reader problem: банк одобрил — кажется безопасно; на регистрации всплывает строка обременения
- Finale: приостановка → отказ в регистрации если не устранено (3 мес по Росреестру)
- fact_boundary: не выдумывать конкретный тюменский адрес; casus как типовая сцена риэлтора

## Voice
- News headline Klyshin rhythm, ~50–70 chars, strong verb
- Forbidden: чеклист, N шагов, стоит ли покупать, полный гайд
- Тюмень / Святослав Шакин — tenant voice

## Anti-dup published
| B01 | В выписке ЕГРН есть строка, после которой аванс вносить нельзя |
| B02–B07 | см. published-titles-only.md |

CRITICAL: B01 = предаванс + строка ЕГРН. B08 = **ипотека одобрена** + **регистрация отменена/приостановлена**. Different hook.

## Runtime (HARD)
Вызываешься из derouter script. Output **only** valid JSON for title-brief.json.
