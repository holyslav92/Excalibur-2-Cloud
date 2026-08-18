---
name: cover-excalibur-blog
description: "④a Cover: 2× quad mcp-derouter 2K, light/meme/Wordstat stickers, anti-repeat 14d."
---

# Cover Agent — longform 8 images, light/meme canon

## Когда

После Sol PASS + Description gate PASS + Cover-text gate PASS. Параллельно Schema.

**После Cover:** `excalibur-blog-cover-qa` → `cover/cover_qa.json` PASS → Indexer.

**Канон:** `memory/cover/cover-canon.json` · Skill agent: `agents/excalibur-blog-cover.md`

## Архитектура

```text
identity-real i2i → 2× quad canvas 2048×1152 (mcp-derouter 2K)
  canvas 1: cover + inline_1..3
  canvas 2: inline_4..7
→ split 2×2 → cover.png + inline-01..07.png → inject
```

PRIMARY: **mcp-derouter** 2K. Kie — legacy fallback only.

## Cover canon (v2)

1. **Invent from scratch** — no inventory lock; no default keys/hologram/desk/balcony.
2. **Anti-repeat 14д** — `used-motifs.json` + `excalibur_blog_cover_motif_gate.py`.
3. **Light & bright** — high-key, sun flare, light leak, glow; **no dark cinematic**.
4. **Memes required** — meme cats + meme people stickers; host Святослав; 8-set includes people.
5. **Wordstat stickers** — 1–3 readable labels from live Wordstat (Тюмень regions 55+11176).
6. **Identity + body lock** — `identity-real/*` i2i; medium slim build как refs; NOT chubby/puffy/thick neck.
7. **REJECTED daypart formula** — never morning desk / day street / evening close / night split.

## Inline canon (v3 utility-first)

Канон: `memory/cover/inline-visual-types.json` + `cover-canon.json` → `inline_utility`.

1. **Стиль** = одобренная обложка B02: #FFFFFF high-key, gold/black, torn paper, tape, sun flare, collage.
2. **NO host face** on inline — host только на cover.
3. **Тест пользы (FAIL):** без абзаца читатель выносит факт/порядок/число/сравнение по H2; ряд иконок+3 слова = FAIL.
4. **Типы:** comparison_table → process_flow → bar_timeline_chart → structure_diagram → labeled_checklist.
5. **Labels** = факты из статьи. Cover-QA: `inline_utility_all_7` + `inline_no_host_face`.

## Runbook

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# Agent fills scene_hint, cover_motifs, wordstat_stickers in quad-manifest.json
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> \
  --composition "..." --location "..." --meme "..." --sticker-set "..."

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
# mcp-derouter: 2 jobs (canvas-index 1 and 2)

python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html

python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## manifest fields (agent)

- `cover_hook`, `cover_hook_highlight` — from cover-text.json
- `slots.cover.scene_hint` — bright invented scene (~80–140 chars)
- `cover_motifs` — composition, location, meme, prop_set, sticker_set, joke
- `wordstat_stickers` — 1–3 phrases from Scout/Research Wordstat
- `slots.inline_1…7` — H2 anchors, `visual_type` (utility catalog), scene_hint, fact labels (3–6)

## Self-check before derouter

- [ ] `cover_motifs` filled + motif gate PASS
- [ ] light/bright language in scene_hint (no dark cinematic)
- [ ] Wordstat stickers tied to topic demand
- [ ] meme cat and/or meme people planned
- [ ] `jobs.length === 1` per canvas batch; `input_urls` on canvas 1
- [ ] `prompt_chars <= 3500`

## Blockers

- COVER MOTIF BLOCKER (14-day collision)
- COVER HERO BLOCKER (identity-real missing)
- DEROUTER/KIE BLOCKER
- daypart formula / inventory default / doc-only office / dark cinematic

## QA

- cover.png + inline-01…07 exist
- inject `data-slot=inline_1…7` after H2
- fragment `cover.md` PASS
