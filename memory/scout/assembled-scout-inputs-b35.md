# Assembled Scout inputs — weekend slot 17:00 YEKT 2026-09-27

## Context
- run_date: 2026-09-27, slot 17:00 Asia/Yekaterinburg (owner weekend exception)
- topic_id: B35 (new)
- Avoid today clusters: B111 keys/UK fees 180k; B34 installment vs price 340k; B33 townhouse vs apartment in block
- topic_market_focus: newbuild_only

## Live blog today (headlines only, anti-dupe)
1. За 5 дней до ключей УК потребовала 180 тысяч — приёмку остановили
2. За 5 дней до ДДУ рассрочка разошлась с ценой на 340 тысяч
3. За 2 дня до ДДУ — таунхаус оказался квартирой в блоке

## Wordstat (MCP-KV live)
- P0 «новостройки тюмень» — 8246 (regions 55+11176); RU 225 compare «новостройки тюмень» 8246
- «приемка квартиры в новостройке тюмень» — 28
- «семейная ипотека новостройка тюмень» — 12 (weak; P0 spine used)

## Candidate LOCK
**Angle:** paper_clean_then_broke — в брони/витрине «студия под сдачу», в проекте ДДУ назначение «нежилое/коммерческое», нельзя прописка, ипотека под угрозой.
**cluster_id:** `newbuild_ddu_commercial_vs_residential_studio_tyumen`
**scout_helper --check-query:** ANTI-DUPE HARD PASS (2026-09-27)
**topic_focus:** PASS

## Title draft (news headline)
В Тюмени за 2 дня до эскроу инвестор сверил ДДУ — «студия» оказалась коммерческим помещением

## comment_magnet_angle
«Если в ДДУ вместо квартиры всплывает коммерция — вы торгуетесь за замену лота или уходите?»

## dzen_casus_shape
PASS | event: сверка ДДУ перед эскроу | risk: коммерция вместо жилья | time: 2 дня до эскроу | finale: стоп до денег

Produce full handoff per scout skill with all required fields.
