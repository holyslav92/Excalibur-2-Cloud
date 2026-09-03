## LESSON-20260903-1305-B22-cover-ocr-escape-attempt1-pass
status: proposed
topic_id: B22
category: structure
confidence: low

### Evidence
- artifact: cover/cover_qa.json
  finding: attempt-1 PNG PASS with `ocr_false_positive_escape: true` (B08/B09/B15 pattern); 6 flaky checks overridden (designed_thumbnail, meme_present, collage, wordstat strips, phone OCR); **no** `cover-budget-result.json` / budget not exhausted.
- artifact: cover/cover-text.json
  finding: hook 6 слов «Банк снял ипотеку перед сделкой», gold highlight «снял», sticky «Бронь уже не спасти»; meme_picks disappointed_black_guy + pop_cat (people+cats).
- artifact: cover/grsai-solo-batch.json
  finding: single grsai standard job → cover.png; no second attempt.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, `wordstat_stickers_not_title_overlap: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260831-0608-B15-cover-budget-ocr-escape-repeat — B22 подтверждает escape path без budget exhaust (attempt-1 publish-ready)

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Short hook 5–7 слов on-topic mortgage stakes; OCR escape при visual core OK (face + Cyrillic hook + phone).
- Cover fail-fast: 1 attempt + escape → Publish; не regen loop при flakes-only FAIL.
- Meme canon: people+cats (disappointed_black_guy + pop_cat), anti-repeat 14д PASS.

### Change
- none durable — canon validated; human review cover-scene phone-in-hand checklist из B10/B15 lesson остаётся open.

### Never again
- Deep-dive pixel OCR debug после visual PASS + escape stamp.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Director runbook note: B22 — пятый live proof OCR escape (B08/B09/B10/B15/B22); B22 = attempt-1 без exhaust.

### Durable applied
- none — observation only; rollback N/A

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela-za-tri-dnya-d
wp_post_id: 9601
