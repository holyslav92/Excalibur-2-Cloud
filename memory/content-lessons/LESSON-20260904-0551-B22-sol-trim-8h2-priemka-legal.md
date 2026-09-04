## LESSON-20260904-0551-B22-sol-trim-8h2-priemka-legal
status: proposed
topic_id: B22
category: structure
confidence: medium

### Evidence
- artifact: drafts/writer.html
  finding: Writer draft ~2788 words; 8 H2 + 7-item numbered practice checklist + comparison table + legal refs (ПП 2226, 3%, 60 дней, НОСТРОЙ, 214-ФЗ).
- artifact: derouter-opus-stamp-sol-trim.json
  finding: Sol TRIM AGGRESSIVE 2498→2310 words (−188); brief `assembled-sol-trim-inputs.md` target 2000–2150 — **still above cap** after automated trim.
- artifact: drafts/variant-a.html vs article.html
  finding: Director manual word trim post-Sol: variant-a ~2207 → final ~2104–2134 (`quality-bar-9.json` word_count: 2134); ~100–175 words cut without losing 8 H2 / 7 inline / table / comment magnet.
- artifact: quality-bar-9.json
  finding: final PASS — `word_count_1800_2200: true`, `spine_once_no_recap: true`, 8 H2, 7 inline, 4 sibling interlinks.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260828-1310-B12-sol-tighten-writer-over-2600 (writer ~2904, sol −346w); LESSON-20260901-1338-B20-sol-trim-spine-once (sol TRIM ~130w). B22 = heaviest legal checklist + 8 H2 → needs **two-pass** trim (Sol TRIM + director).

### Named blockers
- WRITER_OVER_WORDCOUNT_CAP
- SOL_TRIM_INSUFFICIENT_FOR_8H2_LEGAL
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Sol TRIM AGGRESSIVE brief с явным списком «не трогать» (8 H2, 7 figure, CTA blocks, comment magnet, 4 interlink href, table).
- Practice checklist как numbered H2-block — engagement + utility для priemka casus; не заменять bullet-dump в лиде.

### Change
- Director runbook: при 8 H2 + legal checklist + writer >2700 — планировать Sol TRIM **и** director micro-trim gate до quality-bar (не полагаться на один Sol TRIM pass).
- Writer brief: target 2000–2150 на priemka/legal casus с 7+ H2 (снижает двойной trim spend).
- `assembled-sol-trim-inputs.md`: добавить post-trim word-count checkpoint (если >2150 после Sol TRIM → flag director trim).

### Never again
- Публиковать после Sol TRIM если word_count >2200 на 8-H2 legal casus без director length pass.
- Сжимать practice checklist ниже 7 пунктов ради word cap — сначала H2 body repeats и spine-once dupes.

### Proposed apply
- Human review: Sol TRIM template + writer target для priemka/defect clusters (не auto-apply Writer prompt).
- Третий cross-run (B12/B20/B22) sol-trim pattern — кандидат на runbook entry, не skill bloat.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-na-priemke-naschitali-defekty-zastrojschik-potreboval-podpisat-akt
wp_post_id: 9614
