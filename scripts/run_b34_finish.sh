#!/usr/bin/env bash
set -euo pipefail
cd /workspace
ADIR="memory/blog/articles/B34-v-tyumeni-za-4-dnya-do-eskrou-vsplyl-zalog-zastrojschika-na-kvartiru-v-novostroj"
LOG="/opt/cursor/artifacts/b34-pipeline.log"
mkdir -p /opt/cursor/artifacts "$ADIR/cover"
exec >>"$LOG" 2>&1
export EXCALIBUR_BLOG_SLOT=12:00

run() { echo "=== FINISH $(date -Is) $* ==="; "$@"; }

{
  echo "Description B34"
  head -c 5000 "$ADIR/article.html"
  cat "$ADIR/title-brief.json"
} > "$ADIR/assembled-description-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output "$ADIR/description-brief.json" \
  --article-dir "$ADIR"

python3 -c "
import json, re
from pathlib import Path
p = Path('$ADIR/description-brief.json')
t = p.read_text(encoding='utf-8')
m = re.search(r'\{.*\}', t, re.S)
if m:
    obj = json.loads(m.group(0))
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
"

{
  echo "Cover-text B34"
  cat "$ADIR/title-brief.json"
} > "$ADIR/assembled-cover-text-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-cover-text-inputs.md" \
  --output "$ADIR/cover/cover-text.json" \
  --article-dir "$ADIR" &

PID_CT=$!
{
  echo "Schema B34"
  head -c 8000 "$ADIR/article.html"
} > "$ADIR/assembled-schema-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output "$ADIR/schema.jsonld" \
  --article-dir "$ADIR"
wait $PID_CT || true

python3 -c "
import json, re
from pathlib import Path
p = Path('$ADIR/cover/cover-text.json')
if p.exists():
    t = p.read_text(encoding='utf-8')
    m = re.search(r'\{.*\}', t, re.S)
    if m:
        p.write_text(json.dumps(json.loads(m.group(0)), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
"

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
run python3 scripts/excalibur_blog_structure_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_description_gate.py --article-dir "$ADIR"
run python3 scripts/excalibur_blog_stylo.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_indexer.py --article-dir "$ADIR"

if [ "${EXCALIBUR_BLOG_ALLOW_PUBLISH:-}" = "yes" ]; then
  run python3 scripts/excalibur_blog_link_verify.py "$ADIR/article.html" -o "$ADIR/link-verify.json" --site-base "${PUBLIC_SITE_URL}"
  run python3 scripts/excalibur_blog_wp_publish.py --article-dir "$ADIR"
fi

echo "FINISH DONE $(date -Is)"
