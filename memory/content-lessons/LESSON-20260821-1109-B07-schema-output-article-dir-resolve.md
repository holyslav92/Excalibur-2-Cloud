## LESSON-20260821-1109-B07-schema-output-article-dir-resolve
status: applied
topic_id: B07
category: other
confidence: high

### Evidence
- artifact: INC-20260821-1040-schema-output-root (memory/pipeline-fix-queue.md)
  finding: `excalibur_blog_derouter_opus_chat.py --output schema.jsonld --article-dir memory/blog/articles/B07-…` записал JSON-LD в `/workspace/schema.jsonld` (корень репо), не в article dir; schema_gate BLOCK до ручного mv.
- artifact: derouter-opus-stamp-schema.json + schema-gate.json — PASS после mv в article dir
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- SCHEMA_OUTPUT_PATH_ROOT
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Schema role: `--output schema.jsonld` + `--article-dir` — basename output в каталоге статьи.
- Gate order: Write schema.jsonld → затем `excalibur_blog_schema_gate.py` (не parallel с Write).

### Change
- `resolve_output_path()` в derouter script: bare filename + `--article-dir` → article_dir/filename; `memory/...` paths — от repo root.

### Never again
- Не вызывать schema gate до записи schema.jsonld в `<article_dir>/`.
- Не полагаться на cwd для basename `--output` без `--article-dir`.

### Proposed apply
- Skill schema: явно `--output schema.jsonld` (basename OK после fix).

### Durable applied
- `scripts/excalibur_blog_derouter_opus_chat.py` — `resolve_output_path()` (rollback: revert function + restore root-relative basename behavior)
- incident INC-20260821-1040-schema-output-root → fixed

### Resolution
status: applied
article_dir: memory/blog/articles/B07-nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
wp_post_id: 8994
