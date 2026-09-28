#!/usr/bin/env bash
set -euo pipefail
cd /workspace
ADIR="memory/blog/articles/B33-za-3-dnya-do-avansa-v-tyumeni-vsplyl-dolg-za-svet-186-tysyach-semya-otkazalas-ot"
LOG="/opt/cursor/artifacts/b33-pipeline.log"
mkdir -p /opt/cursor/artifacts
exec > >(tee -a "$LOG") 2>&1

run() { echo "=== $(date -Is) $* ==="; "$@"; }

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role title \
  --system-file skills/title-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-title-inputs.md" \
  --output title-brief.json \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_writer_chunk.py \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-writer-inputs.md" \
  --output drafts/writer.html \
  --article-dir "$ADIR"

{
  echo "Assembled Sol inputs — B33 — auto after writer"
  echo "ROLE: Sol — перепиши drafts/writer.html в слог SOUL. 1400–1600 слов, 7 inline figures data-slot inline_1..7, interlinks сохранить."
  echo "Comment magnet from title-brief.json"
  echo ""
  echo "WRITER DRAFT:"
  cat "$ADIR/drafts/writer.html"
} > "$ADIR/assembled-sol-inputs.md"

run python3 scripts/excalibur_blog_sol_chunk.py \
  --system-file skills/sol-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-sol-inputs.md" \
  --output article.html \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_stylo.py --article-dir "$ADIR" || true
if [ -f "$ADIR/stylo-report.json" ] && grep -q '"stylo_pass": false' "$ADIR/stylo-report.json" 2>/dev/null; then
  echo "STYLO FAIL — skip repair in this script"
fi

run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" || \
  run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" --repair

{
  echo "Assembled description inputs B33"
  echo "Use title-brief + article lead; Dzen card teaser"
} > "$ADIR/assembled-description-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output description-brief.json \
  --article-dir "$ADIR"

{
  echo "Cover-text B33 vtorichka utility debt before advance; hook 5-7 words Cyrillic"
  cat "$ADIR/title-brief.json" 2>/dev/null || true
} > "$ADIR/assembled-cover-text-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-cover-text-inputs.md" \
  --output cover/cover-text.json \
  --article-dir "$ADIR" &

PID_CT=$!
{
  echo "Schema B33 BlogPosting"
  head -c 8000 "$ADIR/article.html"
} > "$ADIR/assembled-schema-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output schema.jsonld \
  --article-dir "$ADIR"
wait $PID_CT || true

run python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ADIR" || true

export EXCALIBUR_COVER_MAX_ATTEMPTS=2
run python3 scripts/excalibur_blog_grsai_solo_cover.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_image_caption_builder.py --article-dir "$ADIR" --apply

run python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_pipeline_canon.py --article-dir "$ADIR" --stamp
run python3 scripts/excalibur_blog_html_linter.py "$ADIR/article.html" --fix
run python3 scripts/excalibur_blog_opening_meta_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_structure_gate.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_indexer.py --article-dir "$ADIR"

if [ "${EXCALIBUR_BLOG_ALLOW_PUBLISH:-}" = "yes" ]; then
  run python3 scripts/excalibur_blog_link_verify.py "$ADIR/article.html" -o "$ADIR/link-verify.json" --site-base "$PUBLIC_SITE_URL"
  run python3 scripts/excalibur_blog_wp_publish.py --article-dir "$ADIR"
else
  echo "SKIP publish — allow flag not set"
fi

echo "PIPELINE DONE $(date -Is)"
