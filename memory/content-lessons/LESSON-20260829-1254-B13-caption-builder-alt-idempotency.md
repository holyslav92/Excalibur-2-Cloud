## LESSON-20260829-1254-B13-caption-builder-alt-idempotency
status: active
topic_id: B13
category: structure
confidence: high

### Evidence
- artifact: quality-bar-9.json
  finding: `image_alt_human: false` — `cover: alt too long (355 chars)`; registry cover alt 315 chars duplicated hook.
- artifact: image-alt-gate.json
  finding: before fixer — cover alt repeated hook «Маткапитал остановил сделку до задатка» 5–6×; after `--apply` PASS with single hook sentence (118 chars).
- artifact: cover/cover-budget-result.json
  finding: cover pixel FAIL unrelated to alt length but blocked `quality-bar-9` publish gate together with `cover_qa_pass`.
- artifact: memory/pipeline-fix-queue.md#INC-20260829-1252-cover-pixel-budget-b13
  finding: root cause — `excalibur_blog_image_caption_builder.py --apply` re-appended `cover_hook` on each run.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- CAPTION_BUILDER_NON_IDEMPOTENT
- IMAGE_ALT_TOO_LONG
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Human alt pattern: host + emotion + sticker + hook once — no scene_hint / prompt tokens in alt.
- `image_alt_human` gate in quality-bar-9 — catches alt length and production tokens.

### Change
- Caption builder must be idempotent: strip trailing hook repeats; skip append if hook already in visual line; rebuild from motifs when manifest alt contaminated.
- Run `--apply` once after cover finalization, not in a loop without idempotency guard.

### Never again
- Re-run `excalibur_blog_image_caption_builder.py --apply` on same article without idempotency — duplicates hook and fails alt length gate.
- Treat `image-alt-gate.json` PASS as sufficient when `quality-bar-9` still reads stale long alt from registry.

### Proposed apply
- none (fixer already shipped); monitor next run double `--apply` does not grow alt.

### Durable applied
- `scripts/excalibur_blog_image_caption_builder.py` — `strip_trailing_hook_repeats`, `hook_already_in_visual`, contaminated-alt rebuild (INC-20260829-1252, commit 350c6b3).
- `tests/test_image_caption_builder.py` — idempotency regression.
- Rollback: revert caption builder hook-dedup helpers; re-run tests.

### Resolution
status: applied
article_dir: memory/blog/articles/B13-matkapital-potratili-a-detyam-doli-ne-vydelili-v-tyumeni-sdelku-razvernuli-do-de
wp_post_id: none
