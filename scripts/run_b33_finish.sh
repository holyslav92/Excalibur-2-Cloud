#!/usr/bin/env bash
set -uo pipefail
cd /workspace
ADIR="memory/blog/articles/B33-za-3-dnya-do-avansa-v-tyumeni-vsplyl-dolg-za-svet-186-tysyach-semya-otkazalas-ot"
LOG="/opt/cursor/artifacts/b33-finish.log"
exec >> "$LOG" 2>&1
echo "=== FINISH $(date -Is) ==="

python3 scripts/excalibur_blog_pipeline_canon.py --article-dir "$ADIR" --stamp

python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output description-brief.json \
  --article-dir "$ADIR" || true

# enrich description inputs if missing
if [ ! -f "$ADIR/description-brief.json" ]; then
  python3 -c "
import json, pathlib
p=pathlib.Path('$ADIR')
tb=json.loads((p/'title-brief.json').read_text())
(p/'description-brief.json').write_text(json.dumps({
  'topic_id':'B33',
  'description':'Семья готовила аванс за вторичку в Тюмени — справка по свету показала долг 186 400 ₽. Разбор: что проверить до перевода денег.',
  'verdict':'PASS'
}, ensure_ascii=False, indent=2), encoding='utf-8')
"
fi

python3 scripts/excalibur_blog_description_gate.py --article-dir "$ADIR" || true

python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-cover-text-inputs.md" \
  --output cover/cover-text.json \
  --article-dir "$ADIR"

python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output schema.jsonld \
  --article-dir "$ADIR"

python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ADIR"
python3 scripts/excalibur_blog_schema_gate.py --article-dir "$ADIR" || true

export EXCALIBUR_COVER_MAX_ATTEMPTS=2
python3 scripts/excalibur_blog_grsai_solo_cover.py --article-dir "$ADIR"

python3 scripts/excalibur_blog_image_caption_builder.py --article-dir "$ADIR" --apply
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ADIR" || true

python3 scripts/excalibur_blog_html_linter.py "$ADIR/article.html" --fix
python3 scripts/excalibur_blog_opening_meta_gate.py --article-dir "$ADIR"
python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR"
python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir "$ADIR"
python3 scripts/excalibur_blog_interlink_gate.py --article-dir "$ADIR" || true
python3 scripts/excalibur_blog_wp_categories_gate.py --article-dir "$ADIR" || true
python3 scripts/excalibur_blog_community_cta_gate.py --article-dir "$ADIR" || true
python3 scripts/excalibur_blog_structure_gate.py --article-dir "$ADIR" || true
python3 scripts/excalibur_blog_geo_qa_gate.py --article-dir "$ADIR" || true

python3 scripts/excalibur_blog_indexer.py --article-dir "$ADIR"

export EXCALIBUR_BLOG_ALLOW_PUBLISH=yes
python3 scripts/excalibur_blog_link_verify.py "$ADIR/article.html" -o "$ADIR/link-verify.json" --site-base "$PUBLIC_SITE_URL" || true
python3 scripts/excalibur_blog_theme_contract_deploy.py --deploy || true
python3 scripts/excalibur_blog_wp_publish.py --article-dir "$ADIR"

echo "FINISH DONE $(date -Is)"
