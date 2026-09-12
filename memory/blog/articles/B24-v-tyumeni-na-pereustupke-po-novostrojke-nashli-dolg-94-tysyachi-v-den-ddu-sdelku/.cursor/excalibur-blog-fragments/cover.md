---
status: PASS
topic_id: B24
pipeline: quad_canvas_2x_grsai_standard + solo_cover_regen
budget_exhausted: true
grsai_canvas_attempts: 1
solo_cover_attempts: 2
cover_qa_gate: FAIL
---

# Cover fragment — B24

## Artifacts

- `cover/cover.png` — 1200×675 solo regen (attempt 2 best_candidate)
- `cover/inline-01.png` … `cover/inline-07.png` — quad canvas split (7 inlines)
- `cover/canvas-quad-01.png` (i2i), `cover/canvas-quad-02.png` (t2i retry)
- `cover/quad-manifest.json`, `cover/scene-draft.json`, `cover/cover-budget-result.json`
- `cover/cover_qa.json` — FAIL (budget exhausted → Indexer per fail-fast)

## Canon

- hook: «Долг сорвал сделку с квартирой»
- phone: +7 922 001 65 05
- meme_picks: this_is_fine_dog, nihilist_penguin (cover); disappointed_black_guy, expanding_brain, yelling_at_clouds (inlines)
- glass sales pavilion, sage linen shirt, anti-repeat motifs recorded

## Next

→ Cover-QA OCR escape or Indexer (fail-fast, no regen loop)
