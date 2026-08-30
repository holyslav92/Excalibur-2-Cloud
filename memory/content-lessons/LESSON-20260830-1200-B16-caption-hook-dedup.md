# LESSON-20260830-1200-B16-caption-hook-dedup

- topic_id: B16
- status: applied
- category: script
- confidence: high (repeatable publish blocker)

## Evidence

- `excalibur_blog_image_caption_builder.py --apply` appended `cover_hook` to cover alt on every run.
- Publish calls `apply_article_captions` internally → hook duplicated 4× → `alt too long` FAIL.
- quality-bar-9 `image_alt_human` false positive PASS until publish preflight.

## Keep

- Visual segment + single stakes sentence pattern for cover alt.

## Change

- `build_cover_alt`: skip hook append when hook text already in visual segment (applied in script).

## Never again

- Re-run `--apply` on cover alt that already contains full hook without dedup guard.

## Proposed apply

- applied: `scripts/excalibur_blog_image_caption_builder.py` hook-in-visual guard.

## Metrika

- BLOCKER: credentials absent (INC-20260821-0615); lessons without behavioral signals.
