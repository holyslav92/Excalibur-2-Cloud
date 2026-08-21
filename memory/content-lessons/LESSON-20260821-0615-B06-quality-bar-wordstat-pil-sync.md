## LESSON-20260821-0615-B06-quality-bar-wordstat-pil-sync
status: applied
topic_id: B06
category: other
confidence: high

### Evidence
- artifact: cover/quad-manifest.json#wordstat_pil_only + wordstat_sticker_positions [[0.128,0.12],[0.128,0.219]]
  finding: quality-bar-9 `check_wordstat_overlap` требовал x≥0.68 для всех стикеров, но при `wordstat_pil_only:true` cover_qa_gate проверяет sacred top-left (x≤0.42, y≤0.36) — gate mismatch, quality-bar-9 FAIL до фикса.
- artifact: quality-bar-9.json — status PASS после синхронизации
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- GATE_CONTRACT_MISMATCH
- EVIDENCE_SKIPPED

### Keep
- `wordstat_pil_only:true` + PIL positions в top-left sacred zone (согласовано с cover_qa_gate).
- Paper Wordstat overlay на обложке B06 — cover_qa PASS.

### Change
- quality-bar-9 ветвится по `wordstat_pil_only`: PIL → top-left bounds; canvas overlay → x≥0.68.

### Never again
- Не дублировать противоречивые координатные правила в quality-bar-9 и cover_qa_gate.

### Proposed apply
- При добавлении нового cover gate — один source of truth для sticker zones в shared/cover-canon или cover_qa_gate helper.

### Durable applied
- `scripts/excalibur_blog_quality_bar_9_gate.py` — `check_wordstat_overlap` ветка `wordstat_pil_only` (rollback: revert commit с B06 fixer)

### Resolution
status: applied
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami
wp_post_id: 8984
