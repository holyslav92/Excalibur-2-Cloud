## LESSON-20260822-0753-B08-inbound-interlink-ledger-post-id-gap
status: proposed
topic_id: B08
category: structure
confidence: medium

### Evidence
- artifact: interlink-plan.json — `inbound_targets` 3 siblings (B06, B04, B07), `inbound_updates: []`
- artifact: memory/blog/wp-publish-log.md#B08 — «interlink: no inbound targets with post_id in ledger»
- artifact: interlink-plan.json outbound — sibling `post_id: null` в ledger entries
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- MISSING_UI_BRIDGE (inbound «Читайте также» не применён к старым постам)
- LEDGER_POST_ID_NULL
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Outbound interlink 4× PASS — buyer path не блокирован.
- interlink-plan корректно идентифицирует inbound_targets.

### Change
- После publish: backfill `post_id` в shared/published-articles.md / ledger для B02–B07, затем retry auto_interlink_after_publish.
- Publish script: stamp post_id в ledger atomically при OK post=.

### Never again
- Не считать interlink «закрытым» только по outbound-gate, если inbound_updates пуст и ledger без post_id.

### Proposed apply
- Fixer: ledger post_id backfill + inbound interlink retry для B08 targets (B06, B04, B07).

### Durable applied
- none (повторяется с B06 — нужен pipeline fix)

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-ipoteku-odobrili-a-registraciyu-otmenili-stroka-v-egrn
wp_post_id: 9063
