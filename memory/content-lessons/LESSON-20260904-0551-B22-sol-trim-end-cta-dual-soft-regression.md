## LESSON-20260904-0551-B22-sol-trim-end-cta-dual-soft-regression
status: proposed
topic_id: B22
category: cta
confidence: medium

### Evidence
- artifact: drafts/variant-a.html (post Sol TRIM, pre-director)
  finding: `excalibur-cta-end` collapsed to compact 3-paragraph block; channels merged («Telegram · MAX · tel» one line); **no** `href="/"` site root; **no** deal-phrase (`подключаюсь`, `веду сделк`, `до аванса`) → would FAIL `dual_cta_soft`; marginal `end_cta_full_channels` (missing labeled full set + site `/`).
- artifact: article.html (director fix, published)
  finding: end CTA restored — soft consult («Напишите для консультации»), deal beat («Подключаюсь к сделке от брони до ключей»), labeled channels (Telegram / MAX / Телефон / Дзен / ВКонтакте), site · gajdy · rieltor links; `end_cta_full_channels: true`, `dual_cta_soft: true` in quality-bar-9.
- artifact: assembled-sol-inputs.md
  finding: Sol brief explicitly required full end CTA template with all channels — Sol TRIM pass did not preserve gate-compliant end block.
- artifact: quality-bar-9.json
  finding: final all PASS on CTA checks after director manual edit.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- SOL_TRIM_CTA_REGRESSION
- DIRECTOR_MANUAL_FIX_REQUIRED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- `dual_cta_soft` pattern: consult phrase + deal/service phrase in end block (не hype).
- Full labeled channel list in `excalibur-cta-end` — TG, MAX, tel, Dzen, VK, site, gajdy, rieltor.

### Change
- `assembled-sol-trim-inputs.md` MUST include: «DO NOT collapse excalibur-cta-end; preserve exact channel hrefs and dual_cta consult+deal phrases verbatim».
- Post-Sol-TRIM gate: run `quality-bar-9` CTA checks before Publish; if FAIL → director CTA restore, not another Sol pass.
- Sol TRIM chunking: end CTA block = frozen zone (like comment magnet).

### Never again
- Sol TRIM переписывать end CTA «для краткости» — это отдельный frozen template.
- Публиковать без `end_cta_full_channels` + `dual_cta_soft` PASS после любого trim pass.

### Proposed apply
- Add frozen CTA zone to Sol TRIM brief template (review-only; не Writer master-prompt).
- First named instance of CTA regression after Sol TRIM — watch B23+ for repeat before durable script guard.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-na-priemke-naschitali-defekty-zastrojschik-potreboval-podpisat-akt
wp_post_id: 9614
