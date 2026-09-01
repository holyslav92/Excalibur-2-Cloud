## LESSON-20260901-0625-B16-newbuild-acceptance-defects-cluster
status: proposed
topic_id: B16
category: geo
confidence: low

### Evidence
- artifact: research-notes.md, research-agent-report.json
  finding: Scout cluster `newbuild_acceptance_defects_refuse_act` — приёмка новостройки, дефекты (мокрая стяжка), отказ от акта, ключи не выдали; distinct from B12 (`ddu_escrow` / перенос сдачи).
- artifact: assembled-title-inputs.md, memory/scout/assembled-scout-inputs.md
  finding: P0 Wordstat «приемка квартиры в новостройке тюмень» — 29 (Tyumen 55+11176); broad «приёмка квартиры в новостройке» — 108; RU «акт приемки квартиры в новостройке» — 247.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, word_count 2164 (soft target 1800–2200, hard max 2400 PASS), dzen_reading_minutes_est 11, 4 sibling interlinks.
- artifact: cover/cover-text.json
  finding: sticky «Подписывать или ждать?» mirrors comment-magnet angle for Dzen engagement.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9439 ingest skipped; no behavioral baseline for acceptance cluster)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0; no Metrika cohort)

### Keep
- Newbuild-only casus: мокрая стяжка + неподписанный акт + ключи — hot Tyumen stakes без вторички.
- Ending landing agency: «Подписывать или ждать?» как comment magnet, не how-to checklist финалом.
- Regional фон (Дом на Мысу, СК) отделён от casus B16 в research — no cross-contamination.

### Change
- Scout 30d lock: после publish синхронизировать `newbuild_acceptance_defects_refuse_act` в `memory/scout/used-clusters.json` (ledger sync script).
- Sol/Writer: word_count 2164 чуть выше soft target — при следующем acceptance-cluster посте держать ≤2200 без spine repeat.

### Never again
- Смешивать B16 (дефекты при приёмке) с B12 (перенос сдачи/эскроу) в Scout anti-dup.
- Переносить жалобы других ЖК на casus B16.

### Proposed apply
- Scout story-cluster registry: `newbuild_acceptance_defects_refuse_act` locked 30d after B16 publish (review-only).
- Metrika cohort tag `newbuild_acceptance` после credentials fix — сравнить с B12 `ddu_escrow` retention (needs Metrika).

### Durable applied
- none — first run of cluster; behavioral validation pending Metrika

### Resolution
status: recorded
article_dir: memory/blog/articles/B16-na-priemke-novostrojki-v-tyumeni-nashli-mokruyu-styazhku-klyuchi-ne-vydali
wp_post_id: 9439
