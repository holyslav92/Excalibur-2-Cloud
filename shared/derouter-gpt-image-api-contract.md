# Derouter image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas generation.

## Order of preference (mandatory — owner override 2026-08-22)

```text
1. DEROUTER_API_KEY → scripts/excalibur_blog_derouter_gpt_image2_api.py (api-direct, 2K)
2. REST exhausted     → DEROUTER MCP server (conductor invokes when REST auth/5xx/timeout)
3. Derouter down      → DEROUTER IMAGE BLOCKER — diagnose/retry/fix; STOP
```

**FORBIDDEN FOREVER:** Kie (`excalibur_blog_kie_gpt_image2_api.py`, `KIE_API_KEY` for images), PIL template mashup, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`, broken stdio `mcp-derouter/start-mcp.sh`.

## Host (images — HARD)

**Always** `https://api-direct.derouter.ai/openai/v1` for image gen/edits.

- Timeout: **≥240s** client; default script **600s**
- **Do not** use `https://api.derouter.ai` for images — Cloudflare ~100s → **HTTP 524** on long gen
- Fallback alias: `https://api-direct.apikey.cloud/openai/v1`

Text (factory brain): `scripts/excalibur_blog_derouter_opus_chat.py` — powerful `claude-opus-5` (writer, sol), utility `gpt-5.6-terra` (scout, title, research, description, cover-text, schema, cover-scene). См. `shared/derouter-opus-brain-contract.md`.

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

- `DEROUTER_API_KEY` only (Cursor Cloud Secrets). Missing → `DEROUTER API KEY MISSING`
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

- Auth/5xx/524: retry alternate api-direct host (script built-in)
- Still failing: conductor may invoke **DEROUTER MCP** image tool with same prompt/refs
- **Never** Kie, **never** PIL mashup — `DEROUTER IMAGE BLOCKER` + clear stderr

## PIL mashup ban

`excalibur_blog_cover_pil_compose.py` → BLOCKER. One coherent generated cover only.
