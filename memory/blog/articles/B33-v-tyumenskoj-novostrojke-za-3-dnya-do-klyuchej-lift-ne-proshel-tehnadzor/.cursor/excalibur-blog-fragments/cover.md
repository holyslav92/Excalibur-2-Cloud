---
status: FAIL
topic_id: B33
pipeline: grsai_solo_cover + quad_canvas_2x
budget_exhausted: true
solo_attempts: 2
cover_qa: FAIL
---

# Cover fragment — B33

## Artifacts

- `cover/cover.png` — solo cover (attempt 2/2, pixel QA FAIL, budget exhausted)
- `cover/inline-01.png` … `cover/inline-07.png` — quad canvas split
- `cover/canvas-quad-01.png` (i2i cover+inline1-3), `cover/canvas-quad-02.png` (t2i inline4-7)
- `cover/cover-budget-result.json` — `reason: cover_budget_exhausted`
- `cover/cover-registry.json` — image_caption_builder PASS

## Cover-QA (2026-09-26)

- `cover/cover_qa.json` → **FAIL** (`gate_status: FAIL`)
- OCR escape: **not applied** (hard host identity + layout, not OCR-only)
- Blocker: **COVER_QA_BLOCKER** — see `cover_qa_blocker` in `cover_qa.json`

## Next

→ **Indexer** (fail-fast after budget exhaust) — **not Publish** until cover PASS / owner regen
