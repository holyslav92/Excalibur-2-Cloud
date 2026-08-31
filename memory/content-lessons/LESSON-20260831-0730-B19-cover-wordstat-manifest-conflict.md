# LESSON-20260831-0730-B19-cover-wordstat-manifest-conflict

topic_id: B19
run_date: 2026-08-31
status: proposed
category: structure
confidence: high

## evidence_refs
- none (content-evidence SKIP)
- run: cover_qa.json FAIL `pixel_no_wordstat_query_strips`, `pixel_wordstat_not_opaque_bars`
- cover-budget-result.json: 2/2 grsai attempts FAIL; cover_fixer 2 rounds FAIL

## named_blockers
- Cover-QA FAIL после fail-fast (2/2 solo + fixer regen)
- quality-bar-9: `cover_qa_pass` false; `word_count_1800_2200` false (2232)
- Publish STOP (канон: all_pass required)

## keep
- Scout cluster `double_sale_two_buyers_same_apartment` + Wordstat P0 «купить квартиру в тюмени вторичка» 4146
- Текстовые гейты PASS (CTA, interlink, image_alt после caption builder)
- Fail-fast → Indexer без infinite Cover-QA

## change
- `quad-manifest.json` не должен содержать `wordstat_stickers` при `cover-canon` `wordstat_on_cover: FORBIDDEN_FOREVER`
- Preflight не требовать 1–3 wordstat phrases когда strips на cover запрещены

## never_again
- Писать Scout P0 phrases в manifest.wordstat_stickers для cover panel (модель рисует query strips → pixel FAIL)

## proposed_apply
- applied in fixer: `excalibur_blog_quad_manifest.py` + `excalibur_blog_quad_manifest_preflight.py`

## metrika_feedback
- SKIP: METRIKA CREDENTIALS BLOCKER (нет OAuth/counter в env)
