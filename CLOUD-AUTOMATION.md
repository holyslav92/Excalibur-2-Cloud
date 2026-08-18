# Excalibur-2-Cloud — Cloud Automation (4×/будни, longform)

**Только после** `memory/setup/status.json` → `complete: true`.

Тенант: **The Риэлтор** / tymenrieltor.ru — longform ~2000–2600 слов, cover + 7 inline-quad.

## Расписание (owner: 9–17 YEKT)

**4 запуска в будни** (пн–пт), часовой пояс **Asia/Yekaterinburg (YEKT, UTC+5)**:

| Слот | Время YEKT |
|------|------------|
| 1 | 09:00 |
| 2 | 12:00 |
| 3 | 15:00 |
| 4 | 17:00 |

- Окно владельца: **09:00–17:00** YEKT. Слот **20:00 не используется**.
- Выходные (сб–вс): longform automation **не запускать**, если owner не попросил отдельно.

### Cursor Automation (не GitHub Actions)

Настройте **4 отдельных триггера** в [Cursor → Automations](https://cursor.com/docs/cloud-agent/automations) на будни:

| Триггер | Расписание (YEKT) | Пример cron (TZ=Asia/Yekaterinburg) |
|---------|-------------------|-------------------------------------|
| 1 | пн–пт 09:00 | `0 9 * * 1-5` |
| 2 | пн–пт 12:00 | `0 12 * * 1-5` |
| 3 | пн–пт 15:00 | `0 15 * * 1-5` |
| 4 | пн–пт 17:00 | `0 17 * * 1-5` |

Канонические слоты дублируются в `shared/tenant-config.json` → `publish_schedule.slots_local`.

**Не добавляйте** GitHub Actions cron для этого longform-потока — расписание живёт в **Cursor Automation**. Репозиторий не содержит отдельного `.cursor/automation.json`; триггеры задаются в UI.

**Memories = OFF** в Automation → Tools (см. `CLOUD-FIRST-RUN.md`).

## Один run = одна статья

Каждый запуск automation обрабатывает **ровно одну** longform-статью от темы до готовых PNG:

```text
Scout? → research_start → Research → Title → Writer → Sol
→ Description → Cover-text || Schema → Cover → Cover-QA → Indexer
→ Publish? → Fixer → merge → Content-learner
```

- **Scout?** — по handoff / needs_scout; иначе research_start с заданным `topic_id`.
- **Cover-QA** — обязательный финиш визуала (cover + 7 inline); без PASS дальше не идём.
- **Indexer** — `llms.txt` / `llms-full.txt` (без правок `article.html`).
- **Publish** — **только если одновременно**:
  1. в Cloud Secrets уже есть SFTP: `FTP_HOST`, `FTP_USER`, `FTP_PASS`, `FTP_ROOT` (и `PUBLIC_SITE_URL`);
  2. на **этот процесс** выставлен `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` (env / Runtime Secret, **не git**).
- Если allow flag или FTP **нет** — run завершается после Indexer + артефактов в репо (**без live publish**).
- **Не коммитить** `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` в репозиторий, `.env`, `tenant-config` или Cloud Secrets в git.

Writer = смысл (`drafts/writer.html`). Sol = слог тенанта (`shared/SOUL.md`).

## Visual longform (8 изображений)

1. **Canvas 1** (Derouter REST 2K i2i): cover + inline_1…3 → split 2×2
2. **Canvas 2** (Derouter REST 2K): inline_4…7 → split 2×2
3. Итого: `cover.png` 1200×675 + `inline-01…07.png`, inject `figure.inline-quad` data-slot=inline_1…7

Hero lock: `memory/cover/assets/identity-real/*` (4 live фото) — лицо 28 лет, **новая выдуманная сцена** каждый раз. AI `scene-composition-only/hero-ref-*` — не для лица.

**Cover canon v2:** `memory/cover/cover-canon.json` — light/bright, мемы, Wordstat-стикеры, anti-repeat 14д. **Запрещена** daypart-формула (desk/street/close talk/night split).

**Wordstat:** Scout hard gate via **MCP-KV** (`wordstat_get_*`). P0 buyer demand in Tyumen regions; Cover stickers from same live pull. Enable MCP-KV in Cloud Automation Tools (dashboard connector — never git).

## Automation prompt

```text
Прочитай AGENTS.md + shared/pipeline-canon.json + shared/tenant-config.json.
Если setup_complete != true — остановись (Setup).
Игнорируй Automation Memory. Memories = OFF.

doctor + today.
dzen_rf_pack: shared/dzen-content-rules.md + rf-blocked-entities.json.
needs_scout → Scout (signal_urls из tenant).
research_start → Research → Title → Writer → Sol.
После Sol: pipeline_canon stamp + opening_meta + html_linter.
Description → Cover-text || Schema → Cover → Cover-QA → Indexer.
Publish ТОЛЬКО если FTP secrets настроены И EXCALIBUR_BLOG_ALLOW_PUBLISH=yes на процессе; иначе STOP после Indexer.
Fixer → merge → content-learner.
```

Секреты только из Cloud Secrets (`PUBLIC_SITE_URL`, SFTP, image API, Wordstat MCP). Allow flag — **runtime only**, не в git.

## Отдельный поток Daily (не этот automation)

На сайте есть короткие посты ~800–900 слов (`/blog/bez-rubriki/<timestamp>/`, одна `cleaned_*.png`, без inline). Частота 07/10/13/16/19 YEKT — **вне** этого longform-расписания 09/12/15/17.
