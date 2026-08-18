# Excalibur-2-Cloud Instructions

Язык: русский (тенант может сменить в `shared/tenant-config.json`).

## Первый запуск

Если `memory/setup/status.json` → `complete != true` **или**
`shared/tenant-config.json` → `setup_complete != true`:

→ работай как **`excalibur-blog-setup`** (skill `setup-excalibur-blog`).  
→ **Не** запускай Scout / Research / Publish.

См. `CLOUD-FIRST-RUN.md`, `SETUP.md`.

## Канон (после setup)

```text
Scout? → research_start → Research → Title → Writer(смысл)
→ Sol(слог) → Description → Cover-text || Schema → Cover → Cover-QA
→ Indexer(llms) → Publish → Fixer → merge → Content-learner
```

**Writer** → `drafts/writer.html` (факты и смысл).  
**Sol** (`excalibur-blog-sol`) → финальный `article.html` слогом тенанта
(`shared/SOUL.md` + `shared/soul-examples/`).  
После Sol — stamp `pipeline_canon` + structural checks. Прозу после Sol
не переписывают (кроме возврата Sol при FAIL гейтов слога).

**Title** → `title-brief.json`. **Description** → `description-brief.json` (Дзен-карточка, после Sol).

**18 ролей** (см. `.cursor/agents/FOR-AGENTS.md`): 16 pipeline + `excalibur-blog-description` + `excalibur-blog-cover-qa`.

Никто не читает уже опубликованные статьи сайта — только
`published-titles-only.md` / `shared/published-titles.md` для anti-dup.

`memory/topics/` запрещена. Scout → handoff + `signal_urls` + **dual gate: Klyshin hooks (`memory/scout/klyshin-topic-bank.*`) × MCP-KV Wordstat** (Tyumen 55+11176, compare RU 225). Klyshin = angle/hook; Wordstat = **evaluate + rework for demand** (не binary skip: слабый объём → локализация/переформулировка до buyer P0; skip только если после rework нет честного buyer-intent кластера). В handoff логировать **original Klyshin hook** + **final P0 phrase+volume**. Cover canon: `memory/cover/cover-canon.json`.

**Writer/Sol:** текст через **mcp-derouter** + `DEROUTER_TEXT_MODEL` (Opus). Если derouter down → `DEROUTER WRITER/SOL BLOCKER`, без тихого fallback. См. `shared/writer-model-contract.md`.

```bash
python3 scripts/excalibur_blog_research_start.py --topic-id B111 --title "…"
```

## Ошибка

- Второй автор / rewrite-loop **поверх Sol** (Sol — единственный стилевой рерайт)
- Термин-дамп / research-брифинг в открытии финала
- topics / SEO-хвосты
- Writer/Sol читают старые article.html / live-сайт как образец
- Publish без pipeline_canon stamp
- Publish без `cover/cover_qa.json` PASS или без `description-brief.json`
- Scout/тема без **Klyshin×Wordstat dual gate**, без rework-лога или с выдуманными частотами
- Scout **drop hook** при слабом Wordstat без цикла rework (локализация Тюмень, buyer-жаргон: егрн, наследство, ипотека, аванс…)
- Scout/тема про RF-blocked heroes без Дзен-канона (если `dzen_rf_pack`)
- Sol выдумывает факты, которых нет в `drafts/writer.html` / research
- Запуск пайплайна до завершения Setup

## Preflight

**До Scout (если dzen_rf_pack):** прочитать `shared/dzen-content-rules.md` +
`shared/rf-blocked-entities.json`.

```bash
python3 scripts/excalibur_blog_doctor.py
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_research_start.py --topic-id <id> --title "<short>"
```

Директор: `.cursor/agents/excalibur-blog-director.md` (не Task).  
Setup: `.cursor/agents/excalibur-blog-setup.md` (не Task).
