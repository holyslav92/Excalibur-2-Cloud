# Derouter image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas generation.

## Order of preference (mandatory — owner override 2026-08-22, responses 2026-08-22)

```text
1. DEROUTER_API_KEY → scripts/excalibur_blog_derouter_gpt_image2_api.py
   a) POST /openai/v1/images/generations or /images/edits (4 hosts failover, 2K)
   b) if discontinued on all hosts → POST /openai/v1/responses + tools image_generation
      (model DEROUTER_RESPONSES_IMAGE_MODEL default gpt-5.4; i2i via input_image)
2. Solo cover CLI: scripts/excalibur_blog_derouter_responses_image.py (same /responses path)
3. REST + responses exhausted → DEROUTER MCP (conductor invokes when REST auth/5xx/timeout)
4. Derouter down → DEROUTER IMAGE BLOCKER — diagnose/retry/fix; STOP
```

**FORBIDDEN FOREVER:** Kie (`excalibur_blog_kie_gpt_image2_api.py`, `KIE_API_KEY` for images), PIL template mashup, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`, broken stdio `mcp-derouter/start-mcp.sh`.

## Host (images — failover 2026-08-22)

Пробуй **все** base URL до первого реального PNG:

| # | Base URL |
|---|----------|
| 1 | `https://api.derouter.ai/openai/v1` |
| 2 | `https://api.apikey.cloud/openai/v1` |
| 3 | `https://api-direct.derouter.ai/openai/v1` |
| 4 | `https://api-direct.apikey.cloud/openai/v1` |

- Env override: `DEROUTER_IMAGE_BASE_URL` — одна URL или comma-separated список (полный путь с `/openai/v1` или host root).
- Probe: `python3 scripts/excalibur_blog_derouter_image_probe.py` (generations, then responses fallback)
- Management API (key check, not images): `GET https://cf-api.derouter.ai/balance` with same Bearer key
- Timeout: **≥240s** client; default script **600s**
- `api.derouter.ai` может дать HTTP **524** на длинной gen — script failover на следующий host
- **Text chat** (Opus/Terra) остаётся на рабочем text endpoint — меняем только image base

## Text → image (`/images/generations`)

`POST /openai/v1/images/generations` (JSON):

```json
{
  "model": "<DEROUTER_IMAGE_MODEL>",
  "prompt": "...",
  "size": "2048x1152",
  "quality": "auto"
}
```

- `size` / `quality` optional; omit → 2K medium tier
- Explicit quad 16:9 2K = **`2048x1152`**
- Response: **`data[0].b64_json`** (PNG base64) — **not** a URL

**Note (2026-08-22):** platform may return HTTP 400 `image generation has been discontinued on this platform` on all hosts. Script auto-falls back to `/responses` (below).

## Image → image (`/images/edits`)

`POST /images/edits` (multipart/form-data):

```text
-F model=<DEROUTER_IMAGE_MODEL>
-F prompt="..."
-F image=@identity-real.png
```

- **No** `input_urls`, no JSON data-URL on this path (i2i on `/responses` uses `input_image` data-URL)
- Multi-ref: repeat `-F image[]=@file`
- Output still `b64_json`

Canvas 1: `prefer_local_reference` + `identity_reference_local` → local file attach only.

Canvas 2: no local ref → `/images/generations` (t2i).

## Responses fallback (`/openai/v1/responses`)

When `/images/*` discontinued on all hosts, `excalibur_blog_derouter_gpt_image2_api.py` calls:

`POST {base}/responses` (JSON):

```json
{
  "model": "gpt-5.4",
  "input": [{
    "role": "user",
    "content": [
      {"type": "input_text", "text": "<prompt>"},
      {"type": "input_image", "detail": "high", "image_url": "data:image/jpeg;base64,..."}
    ]
  }],
  "tools": [{"type": "image_generation"}]
}
```

- Model: `DEROUTER_RESPONSES_IMAGE_MODEL` (default **`gpt-5.4`**), not `DEROUTER_IMAGE_MODEL`
- Response: `output[].type=image_generation_call` → `result` (PNG base64)
- Script resizes to `DEROUTER_IMAGE_SIZE` (default `2048x1152`) for quad canvas
- Solo cover regen: `scripts/excalibur_blog_derouter_responses_image.py` → `1200x675` cover.png

## Auth

- `DEROUTER_API_KEY` or alias `DEROUTE_API_KEY` (Cursor Cloud Secrets). Missing → `DEROUTER API KEY MISSING`
- `DEROUTER_IMAGE_MODEL` required for `/images/*` probe (id from GET `/v1/models`)
- `DEROUTER_RESPONSES_IMAGE_MODEL` optional (default `gpt-5.4`) for `/responses` fallback
- Optional: `DEROUTER_IMAGE_SIZE` (default `2048x1152`), `DEROUTER_IMAGE_QUALITY` (default `auto`)
- Never commit, print, or copy keys into git/PR/logs

Doctor: **WARN** when `DEROUTER_API_KEY` or `DEROUTER_IMAGE_MODEL` missing; Cover gen **BLOCKs**.

## Cover command

```bash
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --batch cover/quad-mcp-batch-01.json \
  --result cover/quad-mcp-result-01.json
```

Solo panel regen (cover slot uses same fallback inside gpt_image2_api, or direct CLI):

```bash
python3 scripts/excalibur_blog_quad_regen_panels.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --slots cover
```

```bash
python3 scripts/excalibur_blog_derouter_responses_image.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

## Retry / BLOCKER

- Auth/5xx/524/400 discontinued on `/images/*`: failover по списку base URL → auto `/responses image_generation`
- Still failing: conductor may invoke **DEROUTER MCP** image tool with same prompt/refs
- **Never** Kie, **never** PIL mashup — `DEROUTER IMAGE BLOCKER` + clear stderr

## PIL mashup ban

`excalibur_blog_cover_pil_compose.py` → BLOCKER. One coherent generated cover only.
