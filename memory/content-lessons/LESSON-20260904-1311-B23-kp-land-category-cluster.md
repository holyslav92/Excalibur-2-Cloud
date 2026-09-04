## LESSON-20260904-1311-B23-kp-land-category-cluster
status: proposed
topic_id: B23
category: geo
confidence: medium

### Evidence
- artifact: .cursor/excalibur-blog-handoff.md
  finding: cluster `newbuild_kp_land_category_wrong_for_housing_tyumen`; story_dup_check PASS; distinct from B21 cellar (`newbuild_ddu_cellar_paid_not_handed_tyumen`), B20 legal-entity, utilities КП plots.
- artifact: .cursor/excalibur-blog-handoff.md#wordstat_rework
  finding: probe «машиноместо тюмень» 213 → rejected (B21 overlap); legal «категории земельных участков» 125 too narrow; final P0 «коттеджные поселки тюмень» **1832** (RU compare 2930); buyer anchor «новостройки тюмень» 4683.
- artifact: research-agent-report.json
  finding: fresh Tyumen signals 72.ru Aug 2026 — ВРИ/зона П-1 vs ИЖС promise; KP buyer-doc casus spine.
- artifact: research-context.json
  finding: `cluster_id: newbuild_kp_land_category_wrong_for_housing_tyumen`, klyshin_hook none.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9653 ingest skipped)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish behavioral — no Metrika)

### Keep
- Scout anti-repeat: reject near-cluster probes (машиноместо → B21) before locking KP land-category casus.
- Wordstat rework: legal-narrow phrase (125) + buyer-volume P0 (коттеджные поселки) — demand spine without secondary-market drift.
- comment_magnet: «ИЖС под ключ» в рекламе vs другая категория в ЕГРН — bipolar act/no-act.

### Change
- Scout ledger: register `newbuild_kp_land_category_wrong_for_housing_tyumen` as distinct from utilities/gas КП and cellar/machine-place clusters.
- Research brief: emphasize ЕГРН category + ВРИ + bank stop **before** act — not generic «проверьте документы».

### Never again
- Retitle B21 cellar/machine-place cluster as land-category story.
- Drop hook on weak legal-only Wordstat without buyer-anchor rework (коттеджные поселки / новостройки тюмень).

### Proposed apply
- `shared/scout-story-clusters.json` — add/confirm cluster entry after human review (not auto-apply).
- B23 live validation: KP newbuild casus without Klyshin; P0 volume 1832 sufficient for Friday slot.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya
wp_post_id: 9653
