## LESSON-20260828-0819-B12-wordstat-eggrp-accreditiv-buyer-spine
status: proposed
topic_id: B12
category: utility
confidence: medium

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md#wordstat
  finding: Hook «двойная продажа» 55+11176 → **13** (weak local); rework → compare «двойные продажи квартир» RU225 **281**; buyer spine probes «аккредитив при покупке квартиры» **45**, «проверка егрн» **28**.
- artifact: research-agent-report.json#wordstat
  finding: Final P0 phrase «проверка егрн» volume 28 (Tyumen+region); angle «аккредитив при покупке квартиры» 45; rework_from documented.
- artifact: cover/cover-text.json#inline_6
  finding: Sticker «Аккредитив 3400 ₽» + article H2 «Аккредитив и банковский расчёт» — buyer utility spine, не title-dump «двойная продажа».
- artifact: quality-bar-9.json
  finding: `wordstat_stickers_not_title_overlap: true` — stickers отделены от hook «Квартиру продали двоим — кто останется?».
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- WEAK_LOCAL_HOOK_VOLUME (двойная продажа 13 — не drop, а rework)
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Wordstat = evaluate + rework for demand, не binary skip при слабом local hook.
- Buyer jargon spine: ЕГРН проверка + безопасный расчёт (аккредитив) когда plot-hook слабый локально, но compare RU показывает спрос на «двойные продажи».
- Официальный факт в тексте: Сбер аккредитив 3 400 ₽ физлица (research official_source_audit PASS) — не путать с юрлиц 0,3%/min 15 000.

### Change
- Scout P0 lock: при plot «двойная продажа» weak local — финальный P0 на buyer action («проверка егрн», «аккредитив»), compare phrase на RU225 для SEO spine в H2, не на обложке strip.
- Cover-text: держать Wordstat stickers в inline labels (inline_6 аккредитив), hook остаётся casus («двоим — кто останется?»).

### Never again
- Drop hot casus из-за Wordstat local 13 без rework log.
- Wordstat query strips на cover PNG (canon: stickers only, no strips).

### Proposed apply
- Scout skill: document B12 as rework template — weak local plot phrase → buyer spine P0 + RU225 compare for editorial angle.
- Writer proposals only in content-lessons (не writer-master-prompt): при double-sale cluster всегда блок «ЕГРН не отвечает на главный вопрос» + «аккредитив/расчёт» (B12 structure worked, quality-bar PASS).

### Durable applied
- none (B06 had quality-bar PIL sync; B12 — editorial pattern only)

### Resolution
status: recorded
article_dir: memory/blog/articles/B12-v-yalutorovske-kvartiru-prodali-dvum-pokupatelyam-pervuyu-pytayutsya-vyselit
wp_post_id: 9240
