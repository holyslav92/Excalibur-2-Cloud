# Writer / Sol — модель текста (mcp-derouter)

**Тенант:** The Риэлтор  
**Провайдер:** `mcp-derouter` (PRIMARY для прозы Writer/Sol)  
**Модель:** `DEROUTER_TEXT_MODEL` в Cloud Secrets — семейство **Claude Opus** (Opus 4.6 / Opus 5 / `claude-opus` latest, что отдаёт derouter)

## Правило

Writer и Sol генерируют черновик/финал через **mcp-derouter text**, не через «тихий» fallback на Composer или слабую модель.

Если DEROUTER MCP недоступен (`serverStatus=error`, нет tools, timeout):

```text
DEROUTER WRITER BLOCKER | DEROUTER SOL BLOCKER
reason: mcp-derouter unavailable; DEROUTER_TEXT_MODEL not invoked
```

Директор **останавливает** пайплайн и пишет blocker в handoff / `memory/pipeline-fix-queue.md`.  
**Запрещено:** молча переключиться на weaker writer без явного blocker.

## Тон

- Допустим **ритм Klyshin** (кейс, разговорная первая реплика, короткие абзацы).
- **Автор и факты:** Святослав Шакин, Тюмень, research-notes — не копипаст канала Клышина.
- Sol накладывает `shared/SOUL.md` поверх смысла Writer.

## Cover (отдельно)

Обложки — `DEROUTER_IMAGE_MODEL` / mcp-derouter 2K i2i. Этот контракт — только **текст** Writer/Sol.
