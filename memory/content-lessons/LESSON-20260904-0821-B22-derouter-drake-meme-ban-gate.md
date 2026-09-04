## LESSON-20260904-0821-B22-derouter-drake-meme-ban-gate
status: applied
topic_id: B22
category: other
confidence: high

### Evidence
- artifact: memory/pipeline-fix-queue.md#INC-20260904-0815-cover-text-banned-meme-drake-b22
  finding: Derouter cover-text returned banned meme id `drake` in `meme_picks`; gate would BLOCK; agent manually replaced picks before commit; fixer applied durable banned-alias detection + gate-retry wrapper.
- artifact: cover/cover-text.json
  finding: final `meme_picks` catalog ids (`disaster_girl`, `keyboard_cat`, `success_kid`, `doge`, `this_is_fine_dog`) — gate PASS.
- artifact: tests/test_meme_canon.py
  finding: `test_rejects_banned_drake_alias` — `drake` → BANNED error with clear message.
- artifact: scripts/excalibur_blog_cover_text_derouter.py
  finding: BANNED ids in system prompt + gate-retry wrapper before manual edit.
- artifact: memory/cover/meme-top100.json
  finding: `drake_no_yes` category `banned`, aliases include `drake`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- DEROUTER_BANNED_MEME_PICK
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Meme canon v1: only `meme-top100.json` catalog ids; people+cats variety; BANNED celebrity/stock templates.
- Derouter cover-text via `excalibur_blog_cover_text_derouter.py` wrapper (gate + retry), not raw Derouter output.

### Change
- **applied (fixer B22):** `resolve_meme_id` + banned alias map (`drake`, `salt bae`); gate-retry with error feedback; cover-text skill documents BANNED ids.

### Never again
- Manual meme_picks edit без gate — wrapper must catch banned/unknown ids first.
- `drake`, `drake_no_yes`, `salt_bae`, `stock_handsome_man` in cover or inline picks.

### Proposed apply
- Director: cover-text role always uses `excalibur_blog_cover_text_derouter.py`; on BANNED error — auto-retry once, then needs-human.

### Durable applied
- scripts/excalibur_blog_meme_canon.py — `resolve_meme_id` + banned alias map; rollback: revert banned map + tests
- scripts/excalibur_blog_cover_text_derouter.py — gate-retry wrapper; rollback: revert wrapper, keep manual gate only
- memory/cover/meme-top100.json — drake_no_yes banned entry; rollback: restore prior catalog row
- skills/cover-text-excalibur-blog/SKILL.md + .cursor mirror — BANNED ids documented; rollback: remove BANNED section
- tests/test_meme_canon.py — drake alias rejection test; rollback: remove test case

### Resolution
status: applied
article_dir: memory/blog/articles/B22-v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi
wp_post_id: 9627
