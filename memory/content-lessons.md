# Excalibur BLOG — content lessons (review-only)

Lessons are proposals until validated. Do not auto-edit Writer prompt or SOUL.

## LESSON-20260820-1105-B03-metrika-credentials
status: proposed
topic_id: B03
category: other
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent; gate SKIP
- metrika_signal: METRIKA CREDENTIALS BLOCKER — no OAuth token / counter id in env

### Named blockers
- METRIKA_FEEDBACK_BLOCKER
- EVIDENCE_SKIPPED

### Keep
- Publish + live-page PASS for B03 (доверенность / СВО hook).
- Kie fallback cover path when Derouter images exhausted.

### Change
- Add `YANDEX_METRIKA_OAUTH_TOKEN` + `YANDEX_METRIKA_COUNTER_ID` to Cloud Secrets so content-learner can ingest 30-day signals after each publish.

### Never again
- Invent `content-evidence-report.json` to bypass SKIP.
- Block publish solely because Metrika credentials missing (Metrika is post-publish feedback).

### Proposed apply
- Human: configure Metrika secrets; re-run `excalibur_blog_metrika_fetch.py --days 30 --ingest` on next cron.
- No durable code change until credentials present.

### Rollback
- N/A (no code applied)
