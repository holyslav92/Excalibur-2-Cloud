#!/usr/bin/env bash
set -euo pipefail
cd /workspace
ADIR="memory/blog/articles/B34-za-4-dnya-do-avansa-v-tyumeni-vsplyla-darstvennaya-bank-ostanovil-sdelku"
LOG="/opt/cursor/artifacts/b34-finish.log"
exec > >(tee -a "$LOG") 2>&1
run() { echo "=== $(date -Is) $* ==="; "$@"; }

run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR"

# assembled-description-inputs.md — подготовлен дирижёром (без обрезки UTF-8)

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output description-brief.json \
  --article-dir "$ADIR"

{
  echo "Cover-text B34; hook 5-7 words"
  cat "$ADIR/title-brief.json"
} > "$ADIR/assembled-cover-text-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-cover-text-inputs.md" \
  --output cover/cover-text.json \
  --article-dir "$ADIR" &

PID_CT=$!
{
  echo "Schema B34 BlogPosting — use title-brief + article.meta.json; FAQ optional"
  cat "$ADIR/title-brief.json"
} > "$ADIR/assembled-schema-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output schema.jsonld \
  --article-dir "$ADIR"
wait $PID_CT

# Move stray root outputs if derouter wrote to cwd
for f in description-brief.json schema.jsonld; do
  [ -f "$f" ] && mv "$f" "$ADIR/"
done
[ -f cover/cover-text.json ] && mv cover/cover-text.json "$ADIR/cover/" 2>/dev/null || true
mkdir -p "$ADIR/cover"

run python3 scripts/excalibur_blog_description_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ADIR"
export EXCALIBUR_COVER_MAX_ATTEMPTS=2
run python3 scripts/excalibur_blog_grsai_solo_cover.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_image_caption_builder.py --article-dir "$ADIR" --apply
run python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ADIR"

run python3 scripts/excalibur_blog_pipeline_canon.py --article-dir "$ADIR" --stamp
run python3 scripts/excalibur_blog_html_linter.py "$ADIR/article.html" --fix
run python3 scripts/excalibur_blog_opening_meta_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_structure_gate.py --article-dir "$ADIR" || true
run python3 scripts/excalibur_blog_indexer.py --article-dir "$ADIR"

if [ "${EXCALIBUR_BLOG_ALLOW_PUBLISH:-}" = "yes" ]; then
  run python3 scripts/excalibur_blog_link_verify.py "$ADIR/article.html" -o "$ADIR/link-verify.json" --site-base "${PUBLIC_SITE_URL}"
  run python3 scripts/excalibur_blog_wp_publish.py --article-dir "$ADIR"
else
  echo "SKIP publish"
fi
echo "FINISH DONE $(date -Is)"
