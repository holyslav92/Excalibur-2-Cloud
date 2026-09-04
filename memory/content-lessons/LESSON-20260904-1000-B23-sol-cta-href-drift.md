# LESSON-20260904-1000-B23-sol-cta-href-drift

- topic_id: B23
- status: proposed
- category: structure
- confidence: medium (no Metrika; evidence SKIP)

## Evidence refs
- none (content-evidence-report.json skipped)
- quality-bar-9 FAIL before manual CTA repair: brand_first_person_tyumen, early_cta_tg_max_only, mid_cta_tg_max_nudge, end_cta_full_channels, interlink_siblings_2_4, dual_cta_soft

## Named blockers
- Sol chunk 3 emitted CTAs as plain «Telegram/MAX» without href; interlink comment placeholder instead of sibling `<a>` from writer.html
- Duplicate comment magnet paragraph in sol merge

## Keep
- quality-bar-9 gate catches all CTA/interlink regressions before Indexer
- B22 article.html as structural CTA template

## Change (proposal — review only)
- Sol assembled inputs: explicit «copy href from writer.html interlinks; never leave interlink HTML comment»
- structure_gate after Sol: fail if excalibur-cta-early lacks t.me href before quality-bar

## Never again
- Manual article.html CTA surgery without re-stamping quality-bar-9.json
- Accepting Sol output with `<!-- interlink:` artifact comments

## Metrika
- METRIKA CREDENTIALS BLOCKER (INC-20260821-0615) — behavioral validation skipped

## Proposed apply
- Review-only until repeat in B24+ or Sol contract update approved by owner
