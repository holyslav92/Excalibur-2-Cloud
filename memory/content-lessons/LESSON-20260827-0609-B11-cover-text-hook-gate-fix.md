## LESSON-20260827-0609-B11-cover-text-hook-gate-fix
status: proposed
topic_id: B11
category: structure
confidence: high

### Evidence
- artifact: assembled-cover-text-inputs.md
  finding: cover-text retry after gate BLOCK — (1) hook 5–7 слов по split пробелам, **без em dash (—)**; (2) inline labels ≤28 chars; (3) invalid meme ids forbidden (drake_hotline_bling, suspicious_cat, etc.).
- artifact: cover/cover-text.json + cover-text-gate.json
  finding: PASS hook «Четыре месяца поиска суд оспорил сделку» (6 слов, no em dash); highlight «оспорил»; sticky «ЕГРН не спас»; valid meme_picks from meme-top100 catalog.
- artifact: quality-bar-9.json + opening-meta-gate.json
  finding: all_pass — word_count 2417, h2 8, `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` (4 siblings), inline_figures 7.
- artifact: cover/cover_qa.json (manifest hook with em dash on PNG)
  finding: PNG hook «Четыре месяца искали — суд оспорил сделку» (em dash OK on canvas per cover canon); cover-text gate counts words without em dash — разделение gate JSON vs quad manifest.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_TEXT_GATE_HOOK_WORD_COUNT
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- cover-text.json hook без em dash для word-count gate; quad-manifest/canvas может использовать em dash для OCR readability (canon allows em dash on PNG).
- quality-bar-9 full matrix PASS на Sol — не требовал script patch (в отличие от B06 PIL wordstat sync).
- Comment magnet + prose lead 4–6 — opening-meta PASS.

### Change
- Cover-text role: первый draft hook без em dash (6 слов) — избегать retry BLOCK; примеры в assembled-cover-text-inputs.md как gate checklist.
- Meme picks: copy verbatim ids only — gate BLOCK на invented/Drake ids до Derouter retry.

### Never again
- Hook с em dash в cover-text.json если split даёт >7 «слов» или ломает 5–7 gate.
- Invalid meme catalog ids в cover-text output.

### Proposed apply
- cover-text skill/runbook: default hook template = space-separated 5–7 words; em dash только в quad-manifest `cover_hook` if needed for PNG.
- quality-bar-9: B11 confirms post-B06 PIL fix stable — no new threshold conflict.

### Durable applied
- none (gate fix = editorial retry, не script change)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri
wp_post_id: 9191
