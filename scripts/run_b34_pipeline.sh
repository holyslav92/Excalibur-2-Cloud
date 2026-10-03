#!/usr/bin/env bash
set -euo pipefail
cd /workspace
ADIR="memory/blog/articles/B34-za-4-dnya-do-avansa-v-tyumeni-vsplyla-darstvennaya-bank-ostanovil-sdelku"
LOG="/opt/cursor/artifacts/b34-pipeline.log"
mkdir -p /opt/cursor/artifacts
exec > >(tee -a "$LOG") 2>&1

run() { echo "=== $(date -Is) $* ==="; "$@"; }

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role research \
  --system-file skills/excalibur-research/SKILL.md \
  --user-file "$ADIR/assembled-research-inputs.md" \
  --output research-notes.md \
  --article-dir "$ADIR"

# Title inputs
cat > "$ADIR/assembled-title-inputs.md" <<'EOF'
Assembled Title inputs — B34 — 2026-10-03
Output only valid JSON title-brief.json per SKILL.
topic_id: B34
slot_rubric: vtorichka
P0: «купить квартиру в тюмени вторичка» 3375
H1 news-casus: 4 дня до аванса, дарственная ~полгода назад, банк остановил сделку, Тюмень вторичка
comment_magnet from scout handoff (gift deed before advance)
EOF

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role title \
  --system-file skills/title-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-title-inputs.md" \
  --output title-brief.json \
  --article-dir "$ADIR"

cat > "$ADIR/assembled-writer-inputs.md" <<'EOF'
Assembled Writer inputs — B34 — 2026-10-03
ROLE: Writer (смысл). Derouter writer_chunk — HTML fragments only.
H1 (не в HTML): За 4 дня до аванса в Тюмени всплыла дарственная полгода назад — банк остановил сделку
HARD: 1400–1600 слов, 6 H2, vtorichka news-casus, interlink 2–4 published siblings.
Comment magnet: «Если перед авансом всплывает свежая дарственная, а продавец клянётся «мама не оспорит» — вы бы всё равно внесли аванс?»
Interlink examples: B33 utility debt, B09 EGRN, B14 ipoteka spravka, B10 relatives — pick 2–4 from shared/published-articles.md status=published
H2 outline: выбор трёшки и одобренная ипотека; выписка без обременений; за 4 дня до аванса цепочка права; банк снял одобрение; переговоры «подождём год»; что проверить до аванса на вторичке
FACTS: research-notes.md. Composite Tyumen casus. Ending agency not panic.
EOF

run python3 scripts/excalibur_blog_writer_chunk.py \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-writer-inputs.md" \
  --output drafts/writer.html \
  --article-dir "$ADIR"

{
  echo "Assembled Sol inputs — B34"
  echo "ROLE: Sol — drafts/writer.html → article.html, SOUL, 1400–1600 слов, 7 inline figures inline_1..7"
  cat "$ADIR/drafts/writer.html"
} > "$ADIR/assembled-sol-inputs.md"

run python3 scripts/excalibur_blog_sol_chunk.py \
  --system-file skills/sol-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-sol-inputs.md" \
  --output article.html \
  --article-dir "$ADIR"

run python3 scripts/excalibur_blog_stylo.py --article-dir "$ADIR" || true

run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" || \
  run python3 scripts/excalibur_blog_quality_score_gate.py --article-dir "$ADIR" --repair

{
  echo "Description B34 — Dzen card after Sol"
  head -c 4000 "$ADIR/article.html"
} > "$ADIR/assembled-description-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-description-inputs.md" \
  --output description-brief.json \
  --article-dir "$ADIR"

{
  echo "Cover-text B34 vtorichka gift deed; hook 5-7 Cyrillic words"
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
  echo "Schema B34 BlogPosting"
  head -c 8000 "$ADIR/article.html"
} > "$ADIR/assembled-schema-inputs.md"

run python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role schema \
  --system-file skills/schema-excalibur-blog/SKILL.md \
  --user-file "$ADIR/assembled-schema-inputs.md" \
  --output schema.jsonld \
  --article-dir "$ADIR"
wait $PID_CT

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
  echo "SKIP publish — EXCALIBUR_BLOG_ALLOW_PUBLISH not yes"
fi

echo "PIPELINE DONE $(date -Is)"
