# LESSON-20260905-1214-B24-ddu-area-declaration-cluster

topic_id: B24
run_date: 2026-09-05
status: proposed
category: geo
confidence: low (Metrika credentials absent)

## Evidence refs
- none (content-evidence-report.json skipped)
- publish: wp_post_id=9775, live-page PASS
- cluster: `newbuild_ddu_area_vs_project_declaration_mismatch_tyumen`

## Named findings
- Wordstat P0 «новостройки тюмень» 4660 — strong newbuild demand hook.
- Sol trim ×3 needed after inline inject (2386→2140 words).
- Quad canvas split overwrote solo cover.png → required solo regen before quality-bar cover_qa_pass.
- Derouter utility roles (research, schema) returned FS blocker — conductor fallback used.

## Keep
- News-casus arc: ДДУ 45 vs декларация 41, agency ending before подпись.
- Interlink siblings B19/B20/B23 (newbuild DDU family).

## Change (proposed)
- After `quad_apply` canvas 1, auto-restore `cover-solo-pass.png` if present OR skip cover slot overwrite when `cover_qa.json` already PASS.

## Never again
- Publish without re-running solo cover QA after quad split overwrites cover.png.

## Metrika
- METRIKA CREDENTIALS BLOCKER — behavioral baseline skipped (INC-20260821-0615).
