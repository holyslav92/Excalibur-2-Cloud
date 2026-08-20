# Factory brain — Derouter Opus REST (все текстовые роли)

**Тенант:** The Риэлтор  
**Провайдер:** Derouter REST API (PRIMARY для **всей прозы** фабрики)  
**Скрипт:** `scripts/excalibur_blog_derouter_opus_chat.py`  
**Endpoint:** `POST https://api.derouter.ai/openai/v1/chat/completions`  
**Fallback endpoint:** `https://api.apikey.cloud/openai/v1/chat/completions` (если primary down)  
**Модель:** `claude-opus-5` (или `DEROUTER_TEXT_MODEL` в Cloud Secrets — семейство Claude Opus 5)  
**Auth:** `DEROUTER_API_KEY` только из Cloud Secrets

## Thin Cursor conductor (HARD)

Cursor Cloud Agent — **тонкий дирижёр**: git, shell, MCP Wordstat, image REST, gates.  
**Запрещено** писать прозу Scout/Research/Title/Writer/Sol/Description/Cover-text/Schema/Cover-scene своей моделью (Composer/Auto/inherit).

Для каждой текстовой роли:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role <scout|research|title|writer|sol|description|cover-text|schema|cover-scene> \
  --system-file <skill-or-agent.md> \
  --user-file <assembled-inputs.md> \
  --output <role-output-file> \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

1. Cursor **собирает** `--user-file` из входов (research, handoff, article.html…).
2. Cursor **вызывает** скрипт; берёт `--output` **как есть**.
3. Cursor **не переписывает** HTML/JSON/надписи после Derouter.
4. Stamp `derouter-opus-stamp-<role>.json` — доказательство вызова HIS Opus.

## Роли на Derouter Opus (обязательно)

| Роль | Выход | Wordstat / прочее |
|------|-------|-------------------|
| Scout | handoff prose (topic, rework log) | live MCP-KV Wordstat — отдельно |
| Research | `research-notes.md` synthesis | live sources + MCP-KV |
| Title | `title-brief.json` | demand spine из Scout handoff |
| Writer | `drafts/writer.html` | — |
| Sol | `article.html` | — |
| Description | `description-brief.json` | — |
| Cover-text | `cover/cover-text.json` | stickers из live Wordstat |
| Schema | `schema.jsonld` text | — |
| Cover scene | `scene_hint`, `cover_emotion`, prompt fields в manifest | PNG — image REST |

## Не Derouter (остаётся Cursor / Python / MCP)

- **Director** — оркестрация, Task, git, merge
- **Wordstat** — MCP-KV (`wordstat_get_*`), не выдумывать частоты
- **Cover PNG** — Derouter image REST (`shared/derouter-gpt-image-api-contract.md`)
- **Cover-QA** — `scripts/excalibur_blog_cover_qa_gate.py` (pixel/gates, не «глаз» агента)
- **Indexer / Publish / Fixer** — shell, WP, SFTP

## Fail loud (весь brain)

`tenant-config.json` → `writing_model.fail_loud_if_unavailable: true` для **всех** ролей выше.

Если `DEROUTER_API_KEY` не задан или chat API недоступен после retry:

```text
DEROUTER <ROLE> BLOCKER
reason: DEROUTER_API_KEY missing or Derouter chat API unavailable; claude-opus-5 not invoked
```

Директор **останавливает** пайплайн и пишет blocker в handoff / `memory/pipeline-fix-queue.md`.  
**Запрещено:** молча переключиться на Cursor Composer/Auto для article text.

## Smoke

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py --role smoke --smoke
```

Stamp: `memory/setup/derouter-opus-stamp.json` (без article-dir).

## Запрещено

- `mcp-derouter/start-mcp.sh` (stdio MCP сломан) — только REST
- Cursor-authored prose для любой роли из таблицы
- Тихий fallback на weaker model

## Legacy alias

`shared/writer-model-contract.md` — ссылка на этот контракт (Writer/Sol были первыми).
