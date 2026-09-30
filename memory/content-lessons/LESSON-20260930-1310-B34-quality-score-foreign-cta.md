# LESSON-20260930-1310-B34-quality-score-foreign-cta

- **topic_id:** B34
- **slot:** 17:00 YEKT, vtorichka
- **status:** proposed
- **confidence:** medium (evidence SKIP; Metrika ingest blocked)

## Evidence refs

- none (content-evidence-report.json absent; gate SKIP)
- Run artifacts: `article-quality-score.json` first FAIL → one repair pass; `quality-score-notes.md`

## Named blockers / friction

- Quality score FAIL: H1/lead/finale retell + CTA wording «бронь» tripped `no_foreign_slot_rubric_mechanism` on vtorichka slot.
- Cover-text Derouter occasionally returned prose instead of JSON → manual `cover-text.json` + gate.
- Git secret scan blocked commit until `interlink-plan.json` used `{{SITE_BASE}}` and quad-mcp `model` redacted.

## keep / change / never_again

- **keep:** one quality-score `--repair` Sol only; targeted HTML/title fixes when repair still borderline.
- **change:** Sol assembled inputs should remind: vtorichka slot — no newbuild CTA hooks (бронь/ДДУ) in end CTAs.
- **never_again:** commit full site URL in interlink-plan or raw `DEROUTER_IMAGE_MODEL` in quad-mcp-result JSON.

## Metrika

- METRIKA FEEDBACK BLOCKER (credentials absent); no behavioral signal for B34 post 11346.

## Proposed apply

- Review-only: add one line to quality-score repair checklist in `shared/article-quality-score-lock.md` (slot-rubric CTA lexicon) — **human gate**, not auto-applied.
