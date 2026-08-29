## LESSON-20260829-1010-B13-cover-budget-alt-dedup
status: proposed
topic_id: B13
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: grsai solo 2/2 + fixer 2 rounds exhausted; pixel OCR flakes on hook/phone despite visual OK PNG (host close-up, hook Cyrillic, phone +7 922 001 65 05, sticky, cat meme).
- artifact: cover/cover_qa.json
  finding: ocr_false_positive_escape applied (B08/B09/B10 pattern); gate_status PASS.
- artifact: wp-publish-result.json
  finding: post 9290 published; live-page PASS; featured + 7 inline media OK.
- artifact: scripts/excalibur_blog_image_caption_builder.py
  finding: repeated `--apply` duplicated cover_hook in alt until >240 chars → publish BLOCKER.
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- ALT_HOOK_DEDUP_ON_REAPPLY
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast → budget result → OCR escape when PNG visually OK.
- Short hook 5–7 слов «Аккредитив открыли — деньги не ушли» + sticky «Документы не сошлись».
- letter_of_credit_seller_no_money_tyumen cluster — fresh vs FSSP/rent-to-buy daily WP.

### Change
- `build_cover_alt`: strip trailing duplicate stakes before append (fixed in image_caption_builder.py).
- После budget exhaust: visual manual escape, не deep-dive pixel source.

### Never again
- Многократный `--apply` без dedup hook в manifest alt.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Fixer merged alt dedup guard — B13 first proof after B10 lesson.
- После 2-й content-learner run с тем же alt-dedup без regression → close INC.

### Durable applied
- `scripts/excalibur_blog_image_caption_builder.py` — stakes dedup loop

### Resolution
status: recorded
article_dir: memory/blog/articles/B13-akkreditiv-otkryli-prodavcu-dengi-ne-doshli-sdelku-v-tyumeni-sorvali
wp_post_id: 9290
