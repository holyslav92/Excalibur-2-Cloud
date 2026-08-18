# Excalibur-2-Cloud — Cloud Automation (4×/день, longform)

**Только после** `memory/setup/status.json` → `complete: true`.

Тенант: **The Риэлтор** / tymenrieltor.ru — longform ~2000–2600 слов, cover + 7 inline-quad.

## Расписание

4 запуска в сутки, **Asia/Yekaterinburg (YEKT, UTC+5)**:

| Слот | Время |
|------|-------|
| 1 | 09:00 |
| 2 | 12:00 |
| 3 | 16:00 |
| 4 | 20:00 |

В Cursor Automation задайте 4 триггера с этими часами (или cron `0 9,12,16,20 * * *` в TZ YEKT).

**Не публиковать на живой сайт**, пока в Secrets не включён осознанно `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`.

## Канон пайплайна

```text
Scout? → research_start → Research → Title → Writer → Sol
→ Cover-text || Schema → Cover (2× quad 2K) → Indexer → Publish
→ Fixer → merge → Content-learner
```

Writer = смысл (`drafts/writer.html`). Sol = слог Клышина / факты Шакина.

## Visual longform (8 изображений)

1. **Canvas 1** (mcp-derouter 2K i2i): cover + inline_1…3 → split 2×2
2. **Canvas 2** (mcp-derouter 2K): inline_4…7 → split 2×2
3. Итого: `cover.png` 1200×675 + `inline-01…07.png`, inject `figure.inline-quad` data-slot=inline_1…7

Hero lock: `memory/cover/assets/identity-real/*` (4 live фото) — лицо 28 лет, **новая выдуманная сцена** каждый раз. AI `scene-composition-only/hero-ref-*` — не для лица.

**Cover canon v2:** `memory/cover/cover-canon.json` — light/bright, мемы, Wordstat-стикеры, anti-repeat 14д. **Запрещена** daypart-формула (desk/street/close talk/night split).

**Wordstat:** Scout hard gate — live спрос + Тюмень/область (region ids 55, 11176 в `memory/cover/wordstat-geo.json`).

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
Cover-text || Schema → Cover (mcp-derouter 2K ×2 canvas); Indexer; Publish только если EXCALIBUR_BLOG_ALLOW_PUBLISH=yes.
Fixer → merge → content-learner.
```

Секреты только из Cloud Secrets (`PUBLIC_SITE_URL`, SFTP, image MCP, **Wordstat API**, `EXCALIBUR_BLOG_ALLOW_PUBLISH`).

## Отдельный поток Daily (не этот automation)

На сайте есть короткие посты ~800–900 слов (`/blog/bez-rubriki/<timestamp>/`, одна `cleaned_*.png`, без inline). Частота 07/10/13/16/19 YEKT — вне этого longform-расписания.
