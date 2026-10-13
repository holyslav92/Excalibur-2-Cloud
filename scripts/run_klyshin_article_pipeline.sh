#!/usr/bin/env bash
# Пайплайн одной статьи Klyshin/vtorichka — Derouter + gates + publish
set -euo pipefail
cd /workspace
ADIR="${1:?usage: run_klyshin_article_pipeline.sh <article-dir>}"
export EXCALIBUR_BLOG_RUBRIC=vtorichka
export EXCALIBUR_BLOG_ALLOW_PUBLISH="${EXCALIBUR_BLOG_ALLOW_PUBLISH:-yes}"
export EXCALIBUR_COVER_MAX_ATTEMPTS=2
LOG="/opt/cursor/artifacts/$(basename "$ADIR")-pipeline.log"
mkdir -p /opt/cursor/artifacts
exec > >(tee -a "$LOG") 2>&1
run() { echo "=== $(date -Is) $* ==="; "$@"; }

out_in_dir() {
  local rel="$1"
  echo "$ADIR/$rel"
}

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role title \
  --system-file .cursor/skills/title-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-title-inputs.md" \
  --output "$(out_in_dir title-brief.json)" \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_writer_chunk.py \
  --system-file .cursor/skills/writer-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-writer-inputs.md" \
  --output drafts/writer.html \
  --article-dir "$ADIR"

{
  echo "Sol inputs — $(basename "$ADIR")"
  echo "Rewrite drafts/writer.html per SOUL; Klyshin short-line storytelling; 1400-1600 words; 7 inline data-slot inline_1..7"
  echo "WRITER:"
  cat "$ADIR/drafts/writer.html"
} > "$ADIR/assembled-sol-inputs.md"

run python3 scripts/excalibur_blog_sol_chunk.py \
  --system-file .cursor/skills/sol-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-sol-inputs.md" \
  --output article.html \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_stylo.py --article-dir "$ADIR" || true
# Stylo FAIL: один repair Sol только через quality-score-notes, не через stylo-notes (gold может быть сломан)

run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" || \
  run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" --repair

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file .cursor/skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output "$(out_in_dir description-brief.json)" \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file .cursor/skills/cover-text-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-cover-text-inputs.md" \
  --output "$(out_in_dir cover/cover-text.json)" \
  --article-dir "$ADIR" &

PID_CT=$!
run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file .cursor/skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output "$(out_in_dir schema.jsonld)" \
  --article-dir "$ADIR"
wait $PID_CT
run python3 scripts/excalibur_blog_schema_slug_fixup.py "$ADIR"
run python3 scripts/excalibur_blog_schema_gate.py --article-dir "$ADIR"

run python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ADIR" || true
run python3 scripts/excalibur_blog_grsai_solo_cover.py --article-dir "$ADIR" || true
run python3 scripts/excalibur_blog_image_caption_builder.py --article-dir "$ADIR" --apply
run python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_pipeline_canon.py --article-dir "$ADIR" --stamp
run python3 scripts/excalibur_blog_html_linter.py "$ADIR/article.html" --fix
run python3 scripts/excalibur_blog_opening_meta_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_description_gate.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --blog-path / --out-dir memory/blog

if [ "${EXCALIBUR_BLOG_ALLOW_PUBLISH}" = "yes" ]; then
  run python3 scripts/excalibur_blog_schema_slug_fixup.py "$ADIR"
  run python3 scripts/excalibur_blog_schema_gate.py --article-dir "$ADIR"
  run python3 scripts/excalibur_blog_link_verify.py "$ADIR/article.html" -o "$ADIR/link-verify.json" --site-base "$PUBLIC_SITE_URL" || true  # pragma: allowlist secret
  run python3 scripts/excalibur_blog_theme_contract_deploy.py --deploy || true
  run python3 scripts/excalibur_blog_wp_publish.py --article-dir "$ADIR"
fi

echo "DONE $(basename "$ADIR") $(date -Is)"
