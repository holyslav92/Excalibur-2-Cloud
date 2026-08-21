## LESSON-20260821-1109-B07-derouter-524-validates-b06-chunk
status: skipped_duplicate
topic_id: B07
category: other
confidence: high

### Evidence
- artifact: derouter-opus-stamp-sol.json — merge 3-part chunk (524 recovery)
  finding: Single-shot Sol HTTP 524; recovery sol-part1..3 → article.html PASS (same pattern as B06).
- artifact: derouter-opus-stamp-writer-part{1,2,3}.json + derouter-opus-stamp-sol-part{1,2,3}.json
- cross_ref: LESSON-20260821-0615-B06-derouter-524-chunk-fallback (status validated after B07)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- DEROUTER_HTTP_524
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Longform B-mode (7 inline): Writer/Sol 3-part chunk на первом проходе — validated B06+B07.

### Change
- Director preflight: B-mode article_mode → chunk scripts, не single-shot Derouter.

### Never again
- Single-shot Writer/Sol на longform B-mode.

### Proposed apply
- См. validated LESSON-20260821-0615-B06-derouter-524-chunk-fallback

### Durable applied
- `.cursor/skills/writer-excalibur-blog/SKILL.md` (existing)
- `.cursor/skills/director-excalibur-blog/SKILL.md` — preflight chunk-only note (this run)

### Resolution
status: skipped_duplicate
article_dir: memory/blog/articles/B07-nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
wp_post_id: 8994
supersedes: none
duplicate_of: LESSON-20260821-0615-B06-derouter-524-chunk-fallback
