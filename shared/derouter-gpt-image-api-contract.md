# Derouter image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas generation.

## Order of preference (mandatory — owner override 2026-08-22)

```text
1. DEROUTER_API_KEY → scripts/excalibur_blog_derouter_gpt_image2_api.py (api-direct, 2K)
2. REST exhausted     → DEROUTER MCP server (conductor invokes when REST auth/5xx/timeout)
3. Derouter down      → DEROUTER IMAGE BLOCKER — diagnose/retry/fix; STOP
```

**FORBIDDEN FOREVER:** Kie (`excalibur_blog_kie_gpt_image2_api.py`, `KIE_API_KEY` for images), PIL template mashup, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`, broken stdio `mcp-derouter/start-mcp.sh`.

## Host (images — failover 2026-08-22)

Пробуй **все** base URL до первого реального PNG (`data[0].b64_json`):

| # | Base URL |
|---|----------|
| 1 | `https://api.derouter.ai/openai/v1` |
| 2 | `https://api.apikey.cloud/openai/v1` |
| 3 | `https://api-direct.derouter.ai/openai/v1` |
| 4 | `https://api-direct.apikey.cloud/openai/v1` |

- Env override: `DEROUTER_IMAGE_BASE_URL` — одна URL или comma-separated список (полный путь с `/openai/v1` или host root).
- Probe: `python3 scripts/excalibur_blog_derouter_image_probe.py`
- Management API (key check, not images): `GET https://cf-api.derouter.ai/balance` with same Bearer key
- Timeout: **≥240s** client; default script **600s**
- `api.derouter.ai` может дать HTTP **524** на длинной gen — script failover на следующий host
- **Text chat** (Opus/Terra) остаётся на рабочем text endpoint — меняем только image base

## Text → image

`POST /images/generations` (JSON):

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

Script decodes b64 → `cover/canvas-quad-NN.png` (from batch `output_canvas`) and writes `quad-mcp-result-NN.json` with `local_path` for `quad_apply`.

## Image → image

`POST /images/edits` (multipart/form-data):

```text
-F model=<DEROUTER_IMAGE_MODEL>
-F prompt="..."
-F image=@identity-real.png
```

- **No** `input_urls`, no JSON data-URL
- Multi-ref: repeat `-F image[]=@file`
- Output still `b64_json`

Canvas 1: `prefer_local_reference` + `identity_reference_local` → local file attach only.

Canvas 2: no local ref → `/images/generations` (t2i).

## Auth

- `DEROUTER_API_KEY` or alias `DEROUTE_API_KEY` (Cursor Cloud Secrets). Missing → `DEROUTER API KEY MISSING`
- `DEROUTER_IMAGE_MODEL` required (id from GET `/v1/models`)
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

Solo panel regen:

```bash
python3 scripts/excalibur_blog_quad_regen_panels.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --slots cover
```

## Retry / BLOCKER

- Auth/5xx/524/400 discontinued: failover по списку base URL (`DEROUTER_IMAGE_BASE_URL` или 4 canonical hosts)
- Still failing: conductor may invoke **DEROUTER MCP** image tool with same prompt/refs
- **Never** Kie, **never** PIL mashup — `DEROUTER IMAGE BLOCKER` + clear stderr

## PIL mashup ban

`excalibur_blog_cover_pil_compose.py` → BLOCKER. One coherent generated cover only.
