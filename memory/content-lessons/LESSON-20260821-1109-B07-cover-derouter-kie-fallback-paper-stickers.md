## LESSON-20260821-1109-B07-cover-derouter-kie-fallback-paper-stickers
status: proposed
topic_id: B07
category: other
confidence: medium

### Evidence
- artifact: cover/quad-mcp-batch-01.json + cover/quad-mcp-result-01.json
  finding: Derouter REST image API вернул tempfile URL для canvas-01; cover TL из quad-split не прошёл pixel QA (text on clothes / wordstat on canvas).
- artifact: cover/quad-solo-batch-cover.json → cover/quad-solo-result-cover.json + cover/kie-image-task.json
  finding: solo regen cover через Kie i2i (`source: kie-api`, task success) после исчерпания Derouter REST retries.
- artifact: cover/quad-manifest.json#wordstat_pil_only + wordstat_overlay_style=paper_sticker_v2
  finding: Wordstat стикеры не на canvas — PIL top-left после render; cover_qa PASS с `wordstat=0 paper-gold regions`.
- artifact: cover/cover_qa.json — status PASS, pixel_qa=true
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (B07 content-learner, 2026-08-21)

### Named blockers
- DEROUTER_IMAGE_EXHAUSTED
- COVER_PIXEL_FAIL_RECOVERED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Контракт cover: Derouter REST primary → Kie fallback (`excalibur_blog_kie_gpt_image2_api.py`) при auth/5xx/exhaust.
- `wordstat_pil_only:true` — Wordstat только PIL paper stickers top-left, не на canvas/host chest.
- Solo panel regen (`quad_solo_panel_regen`) для cover TL после quad-split FAIL.

### Change
- Cover agent: при первом cover_qa pixel FAIL на quad-split TL — сразу solo regen + PIL wordstat, не повторять full canvas без смены prompt.
- Документировать в cover skill цепочку: Derouter exhausted → Kie → cover_fixer PIL → re-QA.

### Never again
- Не публиковать cover с canvas Wordstat на host chest — предсказуемый pixel FAIL.
- Не зацикливать Derouter REST image без перехода на Kie fallback.

### Proposed apply
- Подтвердить в `.cursor/skills/cover-excalibur-blog/SKILL.md` явный шаг Kie fallback после Derouter 5xx/exhaust (если ещё не в runbook).
- После второго run с Kie fallback на longform — durable checklist в director preflight Cover.

### Durable applied
- none (первый именованный run Kie recovery B07; cover_qa PASS после recovery)

### Resolution
status: recorded
article_dir: memory/blog/articles/B07-nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
wp_post_id: 8994
permalink: {{SITE_BASE}}/blog/vtorichka-i-riski/nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal/
