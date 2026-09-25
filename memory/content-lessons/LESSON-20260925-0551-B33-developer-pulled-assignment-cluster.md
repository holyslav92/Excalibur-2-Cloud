## LESSON-20260925-0551-B33-developer-pulled-assignment-cluster
status: proposed
topic_id: B33
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-notes.md
  finding: new cluster `newbuild_developer_pulled_assignment_sold_direct_tyumen`; distinct from B30 (3y resale ban in assignment), B31 (insurance +18k), B32 (wrong escrow entity); top_energy_mirror `someone_else_took_object`.
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: «переуступка тюмень» 8 (weak); rework anchor P0 «купить новостройку в тюмени» **897** (55+11176) | compare 225 **1921**; mechanism in H1/casus not narrow SEO tail.
- artifact: research-notes.md
  finding: composite casus — застройщик снимает согласованную переуступку, продаёт прямым ДДУ ~+400k, удержание 150k «за согласование»; comment magnet on suing vs new lot.
- artifact: wp-publish-result.json
  finding: publish PASS post **10939**, live-page PASS, 7 inline uploads, categories=31, inbound interlink 3/3 with post_id.
- artifact: quality-bar-9.json + article-quality-score.json
  finding: `word_count` **1401** (1400–1600), `spine_once_no_recap: true`, `comment_magnet_question: true`, `no_composite_disclaimer: true`; quality-score gate required **one** Sol `--repair` pass (`sol_rewrite_applied: true`) then PASS.
- artifact: stylo-report.json + stylo/history.jsonl
  finding: first stylo FAIL (delta 3.20); after quality-score Sol rewrite stylo PASS (delta 2.22); no stylo-driven second Sol.
- artifact: cover/cover_qa.json
  finding: grsai solo **1** canvas attempt; `ocr_false_positive_escape: true` on residual flakes; **no** cover_fixer round; all layout/host/hook/phone core PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 10939)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat rework: weak «переуступка тюмень» (8) → P0 «купить новостройку в тюмени» 897 + переуступка/застройщик mechanism in casus.
- Dzen news-casus: event (письменное «лот в переуступке») + risk (лот ушёл в прямую продажу) + finale (150k удержали) + agency landing, not panic.
- Scout formula guard: not another «N дней до ДДУ» clone; not B30 assignment-ban recycle.
- Pipeline repair order: quality-score Sol repair before stylo re-measure (avoids stylo→Sol loop on structure-only FAIL).
- Cover: OCR escape without fixer when visual core OK (canonical B11/B19 path).

### Change
- Scout handoff memory: lock plot `newbuild_developer_pulled_assignment_sold_direct_tyumen` for 30d in operator notes; fingerprint «сорвал переуступку + удержал 150» vs B30/B31/B32.
- After Metrika ingest: cohort tag `cluster:newbuild_developer_pulled_assignment_sold_direct_tyumen` vs sibling assignment clusters (B30 ban, B23 apt mismatch).

### Never again
- P0 only on «переуступка тюмень» 8 without newbuild spine rework.
- Recycle B30 «запрет перепродажи 3 года» as «новый» newbuild casus.
- Cover fixer regen when solo attempt 1 + OCR escape PASS + layout/hook/phone core OK.

### Proposed apply
- Operator: add explicit row to `memory/scout/used-clusters.json` for `newbuild_developer_pulled_assignment_sold_direct_tyumen` / B33 when custom cluster ledger is adopted (same gap as B23 proposed cluster row).
- Metrika cohort compare after credentials fix (posts 10939 + backlog B06–B23).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B33-v-tyumeni-investor-soglasoval-pereustupku-zastrojschik-snyal-lot-i-prodal-po-pry
wp_post_id: 10939
