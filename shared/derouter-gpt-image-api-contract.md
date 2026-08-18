# Derouter image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas generation.

## Order of preference (mandatory)

```text
1. DEROUTER_API_KEY set → scripts/excalibur_blog_derouter_gpt_image2_api.py
2. KIE_API_KEY set      → scripts/excalibur_blog_kie_gpt_image2_api.py (after Derouter auth/5xx + one retry)
3. neither              → BLOCKER (DEROUTER API KEY MISSING / KIE API BLOCKER)
```

**FORBIDDEN:** `flux2-pro-text-to-image`, `flux2-pro-image-to-image`, Seedream, `nano_banana*`, `z-image`, `mcp-derouter/start-mcp.sh` (broken stdio MCP).

## Endpoints (owner-verified)

| Mode | Endpoint | Host | Timeout |
|------|----------|------|---------|
| t2i (canvas 2, no ref) | `POST /images/generations` | `https://api-direct.derouter.ai/openai/v1` | 600s |
| i2i (canvas 1 + identity-real) | `POST /images/edits` multipart | same | 600s |
| fallback host (direct down) | same paths | `https://api-direct.apikey.cloud/openai/v1` | 600s |

Chat/text (Writer/Sol): `POST https://api.derouter.ai/openai/v1/chat/completions` — see `shared/writer-model-contract.md`.

## Auth

- Env var: `DEROUTER_API_KEY` (Cursor Cloud Secrets only)
- Required: `DEROUTER_IMAGE_MODEL` (image model id from GET /v1/models)
- Optional: `DEROUTER_IMAGE_SIZE` (default `1536x1024` = 2K-tier 16:9)
- Never commit, print, or copy the key into handoff, PR, logs, or article files.

If unset at Cover gen time:

```text
DEROUTER API KEY MISSING
```

Doctor: **WARN** (not FAIL) when `DEROUTER_API_KEY` missing; Cover run must BLOCK.

## Cover command

```bash
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --batch cover/quad-mcp-batch-01.json \
  --result cover/quad-mcp-result-01.json
```

With Kie fallback after Derouter auth/5xx:

```bash
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py \
  --article-dir <dir> --batch cover/quad-mcp-batch-02.json \
  --result cover/quad-mcp-result-02.json --fallback-kie
```

Reads `cover/quad-mcp-batch*.json` → `jobs[0].mcp_args`.  
Writes `cover/quad-mcp-result*.json` with `local_path` (b64 decode) or `url` — consumed by `quad_apply`.

Then:

```bash
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
```

## i2i identity-real

Canvas 1 batches set `prefer_local_reference` + `local_reference` / `identity_reference_local`.  
Derouter `/images/edits` attaches the **local file** — no Kie File Upload required.

Canvas 2: batch without `input_urls` → `/images/generations` (t2i).

## Retry

- One retry per host on auth/5xx (`--max-retries 1`, `--retry-wait 5`)
- Fallback host `api-direct.apikey.cloud` after primary exhausted
- `--fallback-kie` delegates to Kie script when Derouter still fails and `KIE_API_KEY` is set

## Price / quality

- Model env: `DEROUTER_IMAGE_MODEL`, **2K tier**, 16:9 (`1536x1024` default size)
- Do **not** request 4K unless owner asks (~$0.0126/image at 2K)

## Related

- Quad canvas workflow: `shared/blog-cover-quad-canvas-contract.md`
- Kie fallback: `shared/kie-gpt-image-api-contract.md`
