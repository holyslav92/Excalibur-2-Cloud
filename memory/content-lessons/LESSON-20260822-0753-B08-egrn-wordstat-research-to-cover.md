## LESSON-20260822-0753-B08-egrn-wordstat-research-to-cover
status: proposed
topic_id: B08
category: utility
confidence: medium

### Evidence
- artifact: research-agent-report.json#wordstat
  finding: P0 `купить квартиру в тюмени` vol=22880; stickers `егрн` 7543, `выписка из егрн` 2648; hook `выписка егрн квартира` vol=246
- artifact: cover/quad-manifest.json#wordstat_stickers
  finding: `["выписка егрн квартира", "егрн", "купить квартиру в тюмени"]` — прямой carry-over из research
- artifact: cover/cover_qa.json — PASS, pixel_wordstat_only_top_left, 2 paper-gold regions
- artifact: quality-bar-9.json — `wordstat_stickers_not_title_overlap: true`, cover_qa_pass: true
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Research Wordstat stickers → quad-manifest `wordstat_stickers` без ручного переписывания.
- Cover hook «Проверь выписку до аванса» + sticky в cover-text согласованы с Klyshin «сначала проверка, потом аванс» (research fresh_signal).

### Change
- Cover-text agent: `cover-text.json` может иметь `wordstat_stickers: []` при PIL overlay — source of truth = quad-manifest, не cover-text empty array.

### Never again
- Не считать пустой `wordstat_stickers` в cover-text.json признаком отсутствия Wordstat на обложке — сверять quad-manifest + cover_qa pixel evidence.

### Proposed apply
- Document в cover skill: при quad pipeline stickers живут в quad-manifest; cover-text optional echo.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-ipoteku-odobrili-a-registraciyu-otmenili-stroka-v-egrn
wp_post_id: 9063
