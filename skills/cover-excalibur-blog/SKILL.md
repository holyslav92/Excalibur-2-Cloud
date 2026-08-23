---
name: cover-excalibur-blog
description: "④a Cover: 2× quad grsai grsai standard image model 2K, light/meme, NO Wordstat query strips, anti-repeat 14d."
---

# Cover Agent — longform 8 images, light/meme canon

## OWNER LOCK (permanent)

1. **Engagement bomb** — cover hook поддерживает news-casus (не checklist title); short hook **5–7** кириллических слов; телефон +7 922 001 65 05 на cover.
2. **Meme canon v1 (HARD)** — only `memory/cover/meme-top100.json`; people+cats (NOT cats-only); on-topic funny; stickers ≤15%; never hook/face/phone (+80px); anti-repeat 14д; `meme_picks` cover-text → quad-manifest.
3. **Cover fail-fast (HARD)** — `excalibur_blog_grsai_solo_cover.py`: max **2** full attempts (`EXCALIBUR_COVER_MAX_ATTEMPTS`); timebox **≤15–20 мин**; после бюджета → `cover/cover-budget-result.json` → **Indexer** (не бесконечный Cover-QA). Fixer max 2 rounds. OCR escape без PIL mashup/Kie.

Канон: `memory/cover/cover-canon.json`, `shared/pipeline-canon.json` → `owner_lock_permanent`.

## Thin conductor + Derouter utility (HARD)

**scene_hint, cover_emotion, prompt invention** — только Derouter utility tier (gpt-5.6-terra, `--role cover-scene`).
PNG generation — `excalibur_blog_grsai_gpt_image2_api.py` (не chat).

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-scene \
  --system-file skills/cover-excalibur-blog/SKILL.md \
  --user-file <assembled-cover-scene-inputs.md> \
  --output cover/scene-draft.json \
  --article-dir <article_dir>
```

Merge scene fields в `quad-manifest.json` без рерайта Cursor. `DEROUTER COVER-SCENE BLOCKER` → стоп.

## Когда

После Sol PASS + Description gate PASS + Cover-text gate PASS. Параллельно Schema.

**После Cover:** `excalibur-blog-cover-qa` → `cover/cover_qa.json` PASS → Indexer.

**Канон:** `memory/cover/cover-canon.json` · Skill agent: `agents/excalibur-blog-cover.md`

## Архитектура

```text
identity-real i2i → 2× quad canvas 2048×1152 (grsai grsai standard image model 2K)
  canvas 1: cover + inline_1..3
  canvas 2: inline_4..7
→ split 2×2 → cover.png + inline-01..07.png → inject
```

PRIMARY: **grsai grsai standard image model** (`GRSAI_API_KEY`, Global→China, 2K). Optional: Derouter image fallback (`EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1`). **Kie FORBIDDEN forever.**

## Image model lock (HARD)

| Allowed | Forbidden |
|---------|-----------|
| `excalibur_blog_grsai_gpt_image2_api.py` (PRIMARY REST) | `excalibur_blog_kie_gpt_image2_api.py` / Kie |
| `excalibur_blog_grsai_solo_cover.py` (solo cover regen) | flux2-pro-text-to-image |
| Derouter image REST (optional fallback only) | flux2-pro-image-to-image |
| | Seedream, nano_banana*, z-image |
| | `excalibur_blog_cover_pil_compose.py` / PIL mashup |
| | Off-pipeline «demo» canvases |

**On grsai auth/5xx:** retry alternate host (Global→China) → optional Derouter fallback or BLOCKER. **Never** Kie / PIL mashup / Flux / Seedream / nano_banana / z-image.

## Cover canon (v2)

1. **Invent from scratch** — no inventory lock; no default keys/hologram/desk/balcony.
2. **Anti-repeat 14д** — `used-motifs.json` + `excalibur_blog_cover_motif_gate.py`. **Обязательные поля:** outfit, emotion, pose_framing, action — не только meme/location. FAIL на связку «чёрный пиджак + бюст слева + боковой взгляд» если повтор в последних 2–3 обложках.
3. **Variety lock (HARD)** — FACE i2i = `face-studio-2026-06-23.jpg` (кости/hairline/eyes/stubble/28yo). **Каждый cover INVENTS:** outfit (не default black blazer), location, action (документ/ключи/телефон/доска…), emotion под hook, pose/framing (не always left talking-head bust).
4. **Title zone sacred** — hook title + phone + meme; **NO Wordstat query strips/bars** on cover (owner ban). Телефон +7 922 001 65 05 обязателен.
5. **Light & bright** — high-key, sun flare, light leak, glow; **no dark cinematic**.
6. **Memes (meme_canon_v1)** — **only** `memory/cover/meme-top100.json` real templates:
   - **Variety:** people-memes + cat-memes — **NOT cats-only** across cover+inlines.
   - **On-topic + funny** — reaction fits hook/stakes (skepticism, pain, WTF).
   - **Small stickers** ≤15% frame; **never** cover hook title, host face, or phone +7 922 001 65 05 (≥80px clearance).
   - **Anti-repeat 14д** — log `cover_motifs.meme` + `meme_picks` ids; motif gate before API.
   - Copy `meme_picks` from `cover-text.json` into `quad-manifest.json`.
7. **Wordstat** — Scout/Research live Wordstat for **topic choice only**; **never** paint query phrases on cover.png. Optional one yellow sticky from hook.
8. **Identity + body lock** — `face-studio-2026-06-23.jpg` i2i (WHO only); medium slim; NOT chubby.
9. **Expression invention (HARD)** — эмоция/мимика/поза **новые каждый run** под hook; `scene_hint` + `cover_emotion` + `cover_motifs.emotion/action/outfit/pose_framing`. i2i: «same person, NEW outfit+action+expression, do not copy reference clothes/pose/smile». Копия студийной улыбки 1:1 = FAIL.
10. **REJECTED daypart formula** — never morning desk / day street / evening close / night split.

## Inline canon (v3 utility-first)

Канон: `memory/cover/inline-visual-types.json` + `cover-canon.json` → `inline_utility`.

1. **Стиль** = одобренная обложка B02: #FFFFFF high-key, gold/black, torn paper, tape, sun flare, collage.
2. **NO host face** on inline — host только на cover.
3. **NO co-host human** on inline — stock model, handsome realtor, generated man, large meme person = FAIL.
4. **Meme stickers** — cats or catalog people-memes only; ≤15% frame; corner accent; real templates from `meme-top100.json`.
5. **Тест пользы (FAIL):** без абзаца читатель выносит факт/порядок/число/сравнение по H2; ряд иконок+3 слова = FAIL.
6. **Типы:** comparison_table → process_flow → bar_timeline_chart → structure_diagram → labeled_checklist.
7. **Labels** = факты из статьи. Cover-QA: `inline_utility_all_7` + `inline_no_host_face` + `inline_no_co_host_human` + `inline_meme_sticker_scale`.

## Runbook

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

python3 scripts/excalibur_blog_hero_reference_url.py
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir "$ARTICLE"
python3 scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# HARD canon + preflight BEFORE image API (fail cheap)
python3 scripts/excalibur_blog_quad_manifest_preflight.py --article-dir "$ARTICLE" --apply-canon

# Agent fills scene_hint, cover_motifs, wordstat_stickers in quad-manifest.json
python3 scripts/excalibur_blog_cover_motif_gate.py check --topic-id <id> \
  --composition "..." --location "..." --meme "..." --sticker-set "..."

python3 scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-01.json --result cover/quad-mcp-result-01.json
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py --article-dir "$ARTICLE" \
  --batch cover/quad-mcp-batch-02.json --result cover/quad-mcp-result-02.json

python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir "$ARTICLE" --canvas-index 2 --inject-html

# Wordstat overlay DISABLED — owner banned query strips on cover (canon v3)

python3 scripts/excalibur_blog_cover_motif_gate.py record --topic-id <id> --composition "..." ...
```

## manifest fields (agent)

- `cover_hook`, `cover_hook_highlight` — from cover-text.json
- `slots.cover.scene_hint` — bright invented scene (~80–140 chars) **+ named emotion**
- `slots.cover.cover_emotion` — hook-matched face (shock, side-eye, grimace, bewildered…); never «same as reference»
- `cover_motifs` — composition, location, meme, props, stickers, joke, **outfit, emotion, pose_framing, action**
- `wordstat_stickers` — Scout topic research only (manifest log); **not painted on cover**
- `slots.inline_1…7` — H2 anchors, `visual_type` (utility catalog), scene_hint, fact labels (3–6)

## Self-check before Derouter REST

- [ ] `cover_motifs` filled + motif gate PASS
- [ ] light/bright language in scene_hint (no dark cinematic)
- [ ] Wordstat stickers tied to topic demand
- [ ] meme cat and/or catalog people-meme planned (cover stickers; inline tiny only)
- [ ] `jobs.length === 1` per canvas batch; `input_urls` on canvas 1
- [ ] `prompt_chars <= 3500`

## Blockers

- COVER MOTIF BLOCKER (14-day collision)
- COVER HERO BLOCKER (identity-real missing)
- DEROUTER API KEY MISSING / DEROUTER BLOCKER / KIE API BLOCKER
- **IMAGE MODEL BLOCKER** — Flux/Seedream/nano_banana/z-image or off-pipeline demo canvas
- daypart formula / inventory default / doc-only office / dark cinematic

## QA

- cover.png + inline-01…07 exist
- inject `data-slot=inline_1…7` after H2
- fragment `cover.md` PASS
