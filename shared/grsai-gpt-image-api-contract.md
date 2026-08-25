# grsai image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas generation (owner override 2026-08-22).

## Order of preference (mandatory)

```text
1. GRSAI_API_KEY → scripts/excalibur_blog_grsai_gpt_image2_api.py
   a) POST /v1/api/generate (replyType=json, then async+poll /v1/api/result)
   b) POST /v1/images/generations (OpenAI-compatible)
   c) POST /v1/draw/completions (webHook=-1) + poll /v1/draw/result
   Hosts: https://grsaiapi.com (Global) → https://grsai.dakka.com.cn (China)
2. Solo cover CLI: scripts/excalibur_blog_grsai_solo_cover.py (1200×675, face i2i; **max 2 full attempts** default, `EXCALIBUR_COVER_MAX_ATTEMPTS` override)
3. Optional last resort: EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1 → Derouter image REST
4. grsai down → GRSAI IMAGE BLOCKER — diagnose/retry; STOP
```

**Text roles** (Writer, Sol, Scout, …) remain on Derouter Opus/Terra — **only images** switch to grsai.

**FORBIDDEN FOREVER:** Kie (`excalibur_blog_kie_gpt_image2_api.py`, `KIE_API_KEY` for images), PIL template mashup, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`.

## Hosts

| # | Base URL |
|---|----------|
| 1 | `https://grsaiapi.com` |
| 2 | `https://grsai.dakka.com.cn` |

- Env override: `GRSAI_API_BASE_URL` — одна URL или comma-separated список.
- Timeout: **≥240s** client; default script **600s**
- Result URL TTL: **2 hours** — script downloads immediately after generation

## Model

- **Standard only (owner 2026-08-25):** grsai standard image model — **VIP tier DISABLED forever**
- `GRSAI_IMAGE_MODEL` override allowed only if **not** VIP suffix; env VIP model id → forced to standard
- Quality: `GRSAI_IMAGE_QUALITY` (default `high`; `auto` if supported)
- On API fail: retry standard on alternate hosts/paths — **never** escalate to vip

Implementation: `model_tier_standard()` → `generate_image()` only. Solo cover:
`excalibur_blog_grsai_solo_cover.py` — each attempt standard; next attempt on QA fail, not vip.

**Cover budget:** default `EXCALIBUR_COVER_MAX_ATTEMPTS=2` full standard attempts. Exhausted →
`cover/cover-budget-result.json` with `best_candidate`; conductor proceeds to Indexer (no infinite Cover-QA loop).

## Text → image (`/v1/api/generate`)

`POST {host}/v1/api/generate` (JSON):

```json
{
  "model": "<GRSAI_IMAGE_MODEL>",
  "prompt": "...",
  "images": [],
  "aspectRatio": "16:9",
  "replyType": "json",
  "quality": "high"
}
```

- Standard tier: `aspectRatio` `16:9`, pixel `1672x941`, or `2048x1152` for 2K (no vip required)
- Pipeline resizes/crops to **1200×675** for `cover.png` (quad canvas: **2048×1152**)
- Response: `status=succeeded` → `results[0].url` (download within 2h)
- Async: `replyType=async` → poll `GET /v1/api/result?id=<task_id>`

## Image → image (face lock)

Canvas 1 / cover slot: `prefer_local_reference` + `identity_reference_local` →
**only** `memory/cover/assets/identity-real/face-studio-2026-06-23.jpg` as base64 in `images[]`.

Optional hosted URL in batch `input_urls` (expanded via `PUBLIC_SITE_URL`).

## Legacy paths (failover inside script)

### `/v1/images/generations`

OpenAI-compatible; `image[]` for i2i refs; `size` = aspect ratio or pixel value.

### `/v1/draw/completions`

```json
{
  "model": "<GRSAI_IMAGE_MODEL>",
  "prompt": "...",
  "aspectRatio": "16:9",
  "quality": "high",
  "urls": ["<ref-url-or-base64>"],
  "webHook": "-1"
}
```

Poll: `GET /v1/draw/result?id=<task_id>`

## Auth

- `GRSAI_API_KEY` or alias `GRSAI_KEY` (Cursor Cloud Secrets). Missing → `GRSAI API KEY MISSING`
- Never commit, print, or copy keys into git/PR/logs

Doctor: **WARN** when `GRSAI_API_KEY` missing; Cover gen **BLOCKs**.

## Cover command

```bash
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --batch cover/quad-mcp-batch-01.json \
  --result cover/quad-mcp-result-01.json
```

Solo panel regen (cover slot):

```bash
python3 scripts/excalibur_blog_quad_regen_panels.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --slots cover
```

Direct solo cover (1200×675 + pixel QA stamp):

```bash
python3 scripts/excalibur_blog_grsai_solo_cover.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

## Retry / BLOCKER

- Auth/5xx: failover host Global → China; then path `/api/generate` → `/images/generations` → `/draw/completions`
- Optional Derouter: `EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1` (last resort only)
- **Never** Kie, **never** PIL mashup — `GRSAI IMAGE BLOCKER` + clear stderr

## PIL mashup ban

`excalibur_blog_cover_pil_compose.py` → BLOCKER. One coherent generated cover only.
