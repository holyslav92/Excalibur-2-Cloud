# Pipeline fix queue

## INC-20260819-1733-cover-derouter-image-discontinued
status: open
run_date: 2026-08-19
role: excalibur-blog-cover
topic_id: B01
article_dir: memory/blog/articles/B01-povestka-prodavcu-sdelka-vstanet
symptom: Derouter api-direct HTTP 400 — platform discontinued REST image gen; Kie fallback required for both canvases.
root_cause: Derouter image model no longer serves /images/generations or /images/edits; only text models remain in /v1/models list.
fix_applied: Canvas 1 Kie i2i with prefer_local_reference + identity-real upload; canvas 2 Kie i2i from white-canvas-2k-16x9 plate; split longform patched for inline_4..7.
keep: Kie File Stream Upload path when WP reference_url unavailable; local identity-real rotation via excalibur_blog_identity_real.py.
change: Document Derouter image discontinuation in doctor/setup; auto prefer_local_reference on canvas 1 batch; white plate for canvas-2 Kie when Derouter t2i unavailable.
never_again: Do not block 8-panel cover on Derouter-only when model returns discontinued; do not run canvas-2 split with cover slot map (overwrites cover.png).

## INC-20260819-1730-cover-longform-split-modules
status: open
run_date: 2026-08-19
role: excalibur-blog-cover
topic_id: B01
symptom: quad_manifest and cover_quad_prompt failed — ModuleNotFoundError excalibur_blog_quad_slots; quad_apply passed unsupported --canvas-index to split script.
root_cause: scripts/excalibur_blog_quad_slots.py and excalibur_blog_identity_real.py missing from repo; cover_quad_split hardcoded 4-panel map only.
fix_applied: Added quad_slots + identity_real modules; quad_apply passes --canvas path; split resolves slot keys per canvas from manifest (inline_4..7 on canvas-quad-02).
keep: Run manifest/prompt scripts from scripts/ cwd or PYTHONPATH=scripts.
change: Ship quad_slots + identity_real in repo; longform split/inject for 7 inline in cover_quad_split.py.
never_again: Second canvas split must not remap quadrants to cover/inline_1..3.
