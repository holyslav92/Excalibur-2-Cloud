## LESSON-20260907-1153-B24-installment-penalty-developer-cluster
status: proposed
topic_id: B24
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-context.json
  finding: new cluster `installment_penalty_developer`; story_dup PASS vs keys_delay_penalty_unpaid (delay keys/penalty unpaid), early-payoff discount loss (5 Sep live), B12 escrow; Klyshin none (fresh Tyumen installment casus).
- artifact: research-notes.md#wordstat_signal
  finding: final P0 «новостройки тюмень» regions 55+11176 freq **4670** (compare RU225 **8658**); exact «рассрочка застройщик новостройка» **11**, «рассрочка новостройка тюмень» **12** — weak tail; buyer spine via newbuild P0 + ДДУ/график платежей hook.
- artifact: research-notes.md#surprising_fact
  finding: 214-ФЗ запрещает зачёт неустойки дольщика при возврате при законном одностороннем отказе застройщика — core utility angle for comment magnet.
- artifact: wp-publish-result.json + live-page-report.json
  finding: publish PASS post **9888**, live-page PASS, 7 inline uploads, categories=31.
- artifact: quality-bar-9.json + article-quality-score.json
  finding: `comment_magnet_question: true`, `spine_once_no_recap: true`, `word_count` 1578 (target 1400–1600), `sol_rewrite_applied: true` (quality-score repair), `no_composite_disclaimer: true`.
- artifact: stylo-report.json
  finding: `stylo_pass: true`, `sol_rewrite_applied: false` (delta 2.61 < 2.85); elevated `legal_per_1k` 44 within gate.
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (7 flaky overrides); canonical B08/B09/B15 path — no budget_exhausted artifact.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 9888)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, no behavioral baseline)

### Keep
- Wordstat rework: при слабом exact «рассрочка» (11–12) — P0 через «новостройки тюмень» 4670; on-topic hook через просрочка графика → расторжение ДДУ + удержание взноса.
- Dzen news-casus: event (5 дней просрочки рассрочки) + risk (180 тыс взнос удержан, квартира снова в продаже) + comment magnet «законно ли удержать взнос за 5 дней».
- Scout anti-repeat: отклонены keys_delay_penalty_unpaid (неустойка за сдачу), досрочное погашение/сгорание скидки, B12 escrow cluster.
- Quality-score Sol trim довёл word_count в 1400–1600 без spine-once FAIL.
- Cover OCR escape без budget exhaust — штатный путь (cross_run B15/B20/B22/B23).

### Change
- Scout story-cluster ledger: `installment_penalty_developer` locked 2026-09-07 (B24).
- После Metrika ingest: cohort tag `cluster:installment_penalty_developer` vs sibling penalty clusters (keys_delay, acceptance_defects).

### Never again
- Брать «рассрочка новостройка тюмень» 12 как P0 без rework.
- Смешивать plot с keys_delay (задержка ключей/неустойка застройщика) или досрочным погашением со скидкой.
- Fixer regen cover при OCR escape PASS без budget exhaust.

### Proposed apply
- Scout `used-clusters.json`: cluster_id `installment_penalty_developer`.
- Metrika cohort compare после credentials fix (post 9888).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B24-prosrochili-rassrochku-zastrojschika-ddu-rastorgli
wp_post_id: 9888
