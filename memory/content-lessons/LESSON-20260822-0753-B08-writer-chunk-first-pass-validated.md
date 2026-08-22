## LESSON-20260822-0753-B08-writer-chunk-first-pass-validated
status: validated
topic_id: B08
category: other
confidence: high

### Evidence
- artifact: derouter-opus-stamp-writer-part{1,2,3}.json
  finding: Writer longform B-mode (2491 слов, 7 inline) запущен сразу в 3-part chunk — все части Derouter REST PASS, без HTTP 524; drafts/writer.html собран до Sol.
- artifact: derouter-opus-stamp-sol.json
  finding: Sol single-shot PASS (10683 tokens) после chunked Writer — финальный article.html без retry.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID absent)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Longform Writer: **chunk-only на первом проходе** (подтверждение B06 после 524 recovery).
- Sol может оставаться single-shot, если Writer уже chunked и input умещается в context.

### Change
- Директор: для B-mode 7-inline не пробовать Writer single-shot — сразу chunk scripts.
- Cross-validate: B06 (524→chunk recovery) + B08 (chunk-first clean) = durable pattern.

### Never again
- Не ждать 524 на Writer longform, чтобы «узнать», что нужен chunk.

### Proposed apply
- Поднять LESSON-20260821-0615-B06-derouter-524-chunk-fallback до `validated`.
- Director checklist: longform preflight → chunk-only (без single-shot trial).

### Durable applied
- none (skills/writer-excalibur-blog уже документирует; второй run подтверждает)

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-ipoteku-odobrili-a-registraciyu-otmenili-stroka-v-egrn
wp_post_id: 9063
validates: LESSON-20260821-0615-B06-derouter-524-chunk-fallback
