# Kie image API — FORBIDDEN FOREVER (The Риэлтор)

> **OWNER OVERRIDE (2026-08-22):** Kie is **banned forever** for cover/inline images on this tenant.
> Do not call `excalibur_blog_kie_gpt_image2_api.py` — it exits with `KIE IMAGE BLOCKER`.

## Mandatory order (images only)

```text
1. DEROUTER_API_KEY → scripts/excalibur_blog_derouter_gpt_image2_api.py
   Host: https://api-direct.derouter.ai/openai/v1 (fallback: api-direct.apikey.cloud)
2. REST exhausted     → DEROUTER MCP server (conductor invokes image tool)
3. Derouter down      → DEROUTER IMAGE BLOCKER — diagnose/retry/fix; STOP
```

**NEVER:** Kie, PIL template mashup (`excalibur_blog_cover_pil_compose.py`), Flux, Seedream, nano_banana*, z-image.

## Historical note

This file documented the legacy Kie async path. It is retained only as a **forbidden** reference so agents do not reintroduce Kie fallbacks.

See: `shared/derouter-gpt-image-api-contract.md`, `memory/cover/cover-canon.json` → `image_allowlist.forbidden_forever`.
