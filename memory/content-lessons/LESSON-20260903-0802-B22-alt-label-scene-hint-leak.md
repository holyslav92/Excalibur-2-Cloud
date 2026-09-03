## LESSON-20260903-0802-B22-alt-label-scene-hint-leak
status: proposed
topic_id: B22
category: structure
confidence: medium

### Evidence
- artifact: image-alt-gate.json (pre-publish FAIL → publish PASS)
  finding: `inline_2` и `inline_7` FAIL `scene_hint overlap in alt` — builder взял путь `panel_labels` для `comparison_table` / `structure_diagram` («Уведомление одностороннее…», «Мораторий с 2026 отменён…»), что совпало с `scene_hint` в gate.
- artifact: cover/quad-manifest.json (publish diff)
  finding: после fix — `labels: []`, alt переключён на h2_anchor: «к разделу «День ключей…»» / «Мораторий сняли…»»; gate PASS.
- artifact: quality-bar-9.json
  finding: `image_alt_human: true` после `excalibur_blog_image_caption_builder.py --apply`.
- artifact: wp-publish-result.json
  finding: publish PASS post **9575**, все `inline_alt` OK.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- ALT_LABEL_SCENE_HINT_OVERLAP
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Gate `scene_hint overlap in alt` — ловит prompt-leak до WP.
- h2_anchor-based alt для infographic slots после FAIL — human-readable, без дубля scene_hint.

### Change
- `build_inline_alt`: при наличии `h2_anchor` **предпочитать** h2-путь над `panel_labels` для `comparison_table`, `structure_diagram`, `timeline`, `chart` — или pre-validate labels path против `scene_hint` и fallback на h2.
- Director: после quad-split запускать `image_caption_builder --apply` **до** quality-bar-9, не только на publish.

### Never again
- Публиковать inline alt со списком panel_labels, если gate уже FAIL на scene_hint overlap.
- Копировать cover-text `inline_labels` дословно в alt.

### Proposed apply
- `scripts/excalibur_blog_image_caption_builder.py` → `build_inline_alt` h2-first when `h2_anchor` present (review-only; needs 2nd run confirm).
- CLOUD-AUTOMATION runbook: caption builder сразу после Cover-QA.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-zastrojschik-zaderzhal-klyuchi-na-8-mesyacev-neustojku-predlozhili-ser
wp_post_id: 9575
