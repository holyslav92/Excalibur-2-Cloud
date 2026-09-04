# LESSON-20260904-1000-B23-schema-derouter-preamble

- topic_id: B23
- status: applied
- category: script
- confidence: high

## Evidence refs
- schema-gate FAIL: «schema.jsonld is not valid JSON» — Russian prose + inline JSON from Derouter schema role

## Named blockers
- Derouter utility output for schema role included agent narration before JSON blob

## Keep
- {{SITE_BASE}} placeholder in committed schema.jsonld
- B22 @graph schema shape

## Change (applied)
- `excalibur_blog_schema_gate.py` → `extract_json_payload()` auto-strips preamble and rewrites schema.jsonld

## Never again
- Hand-editing schema without running schema_gate
- Committing schema.jsonld that fails json.loads

## Metrika
- skipped (credentials absent)

## Rollback
- Revert extract_json_payload auto-write in schema_gate.py if it corrupts multi-doc outputs (none seen)
