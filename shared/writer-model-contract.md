# Writer / Sol — модель текста (Derouter REST)

**Тенант:** The Риэлтор  
**Провайдер:** Derouter REST API (PRIMARY для прозы Writer/Sol)  
**Endpoint:** `POST https://api.derouter.ai/openai/v1/chat/completions`  
**Fallback endpoint:** `https://api.apikey.cloud/openai/v1/chat/completions` (если primary down)  
**Модель:** `claude-opus-5` (или `DEROUTER_TEXT_MODEL` в Cloud Secrets — семейство Claude Opus 5)  
**Auth:** `DEROUTER_API_KEY` только из Cloud Secrets

## Правило

Writer и Sol генерируют черновик/финал через **Derouter REST chat/completions**, не через «тихий» fallback на Composer или слабую модель Cursor.

Если `DEROUTER_API_KEY` не задан или API недоступен после retry:

```text
DEROUTER WRITER BLOCKER | DEROUTER SOL BLOCKER
reason: DEROUTER_API_KEY missing or Derouter chat API unavailable; claude-opus-5 not invoked
```

Директор **останавливает** пайплайн и пишет blocker в handoff / `memory/pipeline-fix-queue.md`.  
**Запрещено:** молча переключиться на weaker writer без явного blocker.

## Cursor subagents (Task)

Когда Writer/Sol запускаются как Cursor subagents с inherit-моделью, в промптах Director/Task указывать:

- intended model id: **`claude-opus-5` via Derouter**
- не «random Cursor default»

Если агент вызывает HTTP напрямую — `claude-opus-5` на `https://api.derouter.ai/openai/v1`.

**Не использовать:** `mcp-derouter/start-mcp.sh` (stdio MCP сломан); только REST.

## Тон

- Допустим **ритм Klyshin** (кейс, разговорная первая реплика, короткие абзацы).
- **Автор и факты:** Святослав Шакин, Тюмень, research-notes — не копипаст канала Клышина.
- Sol накладывает `shared/SOUL.md` поверх смысла Writer.

## Cover (отдельно)

Обложки — Derouter REST (`scripts/excalibur_blog_derouter_gpt_image2_api.py`).  
См. `shared/derouter-gpt-image-api-contract.md`. Этот контракт — только **текст** Writer/Sol.
