#!/usr/bin/env bash
set -euo pipefail
cd /workspace
ADIR="memory/blog/articles/B34-v-tyumeni-za-4-dnya-do-eskrou-vsplyl-zalog-zastrojschika-na-kvartiru-v-novostroj"
LOG="/opt/cursor/artifacts/b34-pipeline.log"
mkdir -p /opt/cursor/artifacts
exec > >(tee -a "$LOG") 2>&1
export EXCALIBUR_BLOG_SLOT=12:00

run() { echo "=== $(date -Is) $* ==="; "$@"; }

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role research \
  --system-file skills/excalibur-research/SKILL.md \
  --user-file "$ADIR/assembled-research-inputs.md" \
  --output "$ADIR/research-notes.md" \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_research_official_gate.py --article-dir "$ADIR" || true

python3 -c "
from pathlib import Path
adir = Path('$ADIR')
notes = (adir / 'research-notes.md').read_text(encoding='utf-8')
chunk = notes[:5500].rsplit('\n', 1)[0] + '\n' if len(notes) > 5500 else notes
(adir / 'assembled-title-inputs.md').write_text(
    'Assembled title inputs B34 newbuild pledge before escrow\n\n' + chunk,
    encoding='utf-8',
)
"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role title \
  --system-file skills/title-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-title-inputs.md" \
  --output "$ADIR/title-brief.json" \
  --article-dir "$ADIR"

{
  echo "Assembled Writer inputs — B34 — 2026-09-29"
  echo "ROLE: Writer (смысл). Derouter writer_chunk — HTML fragments only."
  echo ""
  cat "$ADIR/title-brief.json" 2>/dev/null || true
  echo ""
  echo "Research:"
  head -c 12000 "$ADIR/research-notes.md"
} > "$ADIR/assembled-writer-inputs.md"

run python3 scripts/excalibur_blog_writer_chunk.py \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-writer-inputs.md" \
  --output drafts/writer.html \
  --article-dir "$ADIR"

{
  echo "Assembled Sol inputs — B34"
  echo "ROLE: Sol — drafts/writer.html → SOUL article.html, 1400–1600 слов, 7 inline data-slot inline_1..7, interlinks 2–4 newbuild siblings."
  cat "$ADIR/drafts/writer.html"
} > "$ADIR/assembled-sol-inputs.md"

run python3 scripts/excalibur_blog_sol_chunk.py \
  --system-file skills/sol-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-sol-inputs.md" \
  --output article.html \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_stylo.py --article-dir "$ADIR" || true
if [ -f "$ADIR/stylo-report.json" ] && grep -q '"stylo_pass": false' "$ADIR/stylo-report.json" 2>/dev/null; then
  if [ -f "$ADIR/stylo-notes.md" ]; then
    run python3 scripts/excalibur_blog_sol_chunk.py \
      --system-file skills/sol-excalibur-blog/SKILL.md \
      --user-file "$ADIR/assembled-sol-inputs.md" \
      --output article.html \
      --article-dir "$ADIR" \
      --extra-user-file "$ADIR/stylo-notes.md" || true
    run python3 scripts/excalibur_blog_stylo.py --article-dir "$ADIR" || true
  fi
fi

run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" || \
  run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" --repair

{
  echo "Assembled description inputs B34"
  head -c 4000 "$ADIR/article.html"
} > "$ADIR/assembled-description-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output "$ADIR/description-brief.json" \
  --article-dir "$ADIR"

{
  echo "Cover-text B34 newbuild pledge; hook 5-7 Cyrillic words"
  cat "$ADIR/title-brief.json" 2>/dev/null || true
} > "$ADIR/assembled-cover-text-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-cover-text-inputs.md" \
  --output "$ADIR/cover/cover-text.json" \
  --article-dir "$ADIR" &

PID_CT=$!
{
  echo "Schema B34 BlogPosting"
  head -c 8000 "$ADIR/article.html"
} > "$ADIR/assembled-schema-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output "$ADIR/schema.jsonld" \
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
run python3 scripts/excalibur_blog_description_gate.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_indexer.py --article-dir "$ADIR"

if [ "${EXCALIBUR_BLOG_ALLOW_PUBLISH:-}" = "yes" ]; then
  run python3 scripts/excalibur_blog_link_verify.py "$ADIR/article.html" -o "$ADIR/link-verify.json" --site-base "${PUBLIC_SITE_URL}"
  run python3 scripts/excalibur_blog_wp_publish.py --article-dir "$ADIR"
else
  echo "SKIP publish — allow flag not set"
fi

echo "PIPELINE DONE $(date -Is)"
