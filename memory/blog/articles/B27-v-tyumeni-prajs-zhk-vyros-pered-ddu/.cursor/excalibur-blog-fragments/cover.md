---
status: FIX_ATTEMPTED
topic_id: B27
pipeline: solo_cover_grsai_standard_fix
budget_exhausted: true
grsai_canvas_attempts: 2
solo_cover_attempts: 1
cover_qa: FAIL
---

# Cover fragment — B27 (fix attempt)

## Fix action

Solo i2i regen (`excalibur_blog_grsai_solo_cover.py --max-attempts 1`) with HOST CROP + STICKY top-left + TEXT LAYOUT suffix.

## Target issues (user request)

| Issue | Before | After regen |
|-------|--------|-------------|
| `pixel_host_close_up` | face_h_frac=0.12 FAIL | face_h_frac=0.28 PASS |
| sticky on chest | `pixel_wordstat_not_on_host_chest` FAIL | PASS (top-left pin) |
| hook + phone | OCR flakes | hook present; phone readable PASS |

## Remaining Cover-QA FAIL

- `pixel_meme_zone_clear` — gold bar bands overlap meme zone (blocks OCR escape)
- OCR flakes: `pixel_hook_title_not_truncated`, `pixel_identity_matches_studio` (skin blob)
- False positives: `+480 тыс` price tags → `pixel_no_wordstat_query_strips` / `pixel_wordstat_not_opaque_bars`

## Artifacts

- `cover/cover.png` — solo regen 1200×675 (md5 4ad5ef49…)
- `cover/cover_qa.json` — status FAIL
- `cover/cover-budget-result.json` — budget exhausted (1 fix attempt)

## Next

Cover-QA still FAIL → Indexer only if owner accepts OCR escape / manual override; else new topic budget.
