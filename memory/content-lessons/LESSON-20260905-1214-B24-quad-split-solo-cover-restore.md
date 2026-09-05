# LESSON-20260905-1214-B24-quad-split-solo-cover-restore

topic_id: B24
run_date: 2026-09-05
status: proposed
category: structure
confidence: medium (run evidence)

## Evidence refs
- `excalibur_blog_quad_apply.py --canvas-index 1` overwrote `cover/cover.png` from quad panel
- `cover_qa.json` stamped md5 mismatch → quality-bar `cover_qa_pass` FAIL
- Recovery: `excalibur_blog_grsai_solo_cover.py` regen → PASS

## Proposed apply
- In `excalibur_blog_cover_quad_split.py`: if `cover_qa.json` gate_status=PASS before split, copy existing `cover.png` → `cover-solo-pass.png` and write quad panel to `cover-quad-panel.png` instead of overwriting `cover.png`.

## Never again
- Run quality-bar-9 after quad apply without verifying cover.png md5 vs cover_qa stamp.
