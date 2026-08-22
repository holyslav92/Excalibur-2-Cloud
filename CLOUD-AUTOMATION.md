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
- **Cover-QA** — обязательный финиш визуала (cover + 7 inline); **pixel gate** на `cover.png` bytes через `scripts/excalibur_blog_cover_qa_pixels.py` + `cover_qa.json` (`pixel_qa=true`, `cover_md5`). Без PASS дальше не идём. **Designed thumbnail gate:** hook H1 (справа, вне лица), телефон +7 922 001 65 05 (низ-право), мем-стикер (угол), optional yellow sticky from hook — **NO Wordstat query strips/bars** (`pixel_no_wordstat_query_strips`). FAIL: face-only collapse. **Fixer** — regen cover panel при layout FAIL; **never** PIL Wordstat overlay/repack → re-QA bytes.
- **Indexer** — `llms.txt` / `llms-full.txt` (без правок `article.html`).
- **Publish** — **только если одновременно**:
  1. в Cloud Secrets уже есть SFTP: `FTP_HOST`, `FTP_USER`, `FTP_PASS`, `FTP_ROOT` (и `PUBLIC_SITE_URL`);
  2. на **этот процесс** выставлен `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` (env / Runtime Secret, **не git**);
  3. `quality-bar-9.json` → `all_pass: true` (см. `shared/quality-bar-9.md`).
- Если allow flag или FTP **нет** — run завершается после Indexer + артефактов в репо (**без live publish**).
- Live = **SFTP replace** на tymenrieltor.ru; не жди merge `article.html` в `main` для выхода на сайт.
- **Код и канон** (scripts, shared/*, skills, gates) — в `main`. Артефакты статьи — в ветке run / PR automation.
- **Не коммитить** `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` в репозиторий, `.env`, `tenant-config` или Cloud Secrets в git.

Writer = смысл (`drafts/writer.html`). Sol = слог тенанта (`shared/SOUL.md`).

## Thin conductor + Derouter two-tier (HARD)

Cursor Automation — **тонкий дирижёр** (default Composer): doctor, git, MCP Wordstat, image REST, gates.
**Не** переключать модель Cursor. **Запрещено** писать прозу Scout/Research/Title/Writer/Sol/Description/Cover-text/Schema/Cover-scene моделью Cursor.

Для каждой текстовой роли вызывай `scripts/excalibur_blog_derouter_opus_chat.py` — tier по `--role`:

| Tier | Derouter model | Роли |
|------|----------------|------|
| powerful | `claude-opus-5` | writer, sol |
| utility | `gpt-5.6-terra` | scout, title, research, description, cover-text, schema, cover-scene |

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role <scout|research|title|writer|sol|description|cover-text|schema|cover-scene> \
  --system-file <skill-or-agent.md> \
  --user-file <assembled-inputs.md> \
  --output <role-output> \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Бери `--output` как есть; не переписывай HTML/JSON после Derouter.
`DEROUTER <ROLE> BLOCKER` в stderr → **стоп** пайплайна.
Контракт: `shared/derouter-opus-brain-contract.md`.

**Нет run_budget / circuit breaker** — не добавляй wall-clock или billed caps поверх Derouter.

## Conversion + quality bar 9/10 (HARD before Publish)

Главная задача статьи — увести читателя в **Telegram** или **MAX** до ухода с страницы.
Канон URL: `shared/tenant-config.json` → `cta_channels` / `cta_links`.

| Зона | Когда | Что |
|------|-------|-----|
| **Early** | после hook + TL;DR, первый экран | brand beat (Святослав, The Риэлтор, Тюмень) + curiosity + **только TG + MAX** |
| **Mid** | после практического блока (aftermath casus) | лёгкий nudge TG + MAX (`excalibur-cta-mid`) |
| **End** | финал | dual CTA «консультация» / «сразу в сделку» + полный набор (TG, MAX, site, Дзен, VK, guides, about) |

- Телефон `+7 922 001 65 05` — на **cover** + **один раз** в теле.
- **Interlink:** 2–4 контекстные ссылки на sibling из `shared/published-articles.md` (`status=published`).
- Gate: `python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir <dir>` → `quality-bar-9.json` all_pass.

## Visual longform (8 изображений)

1. **Canvas 1** (grsai grsai standard image model i2i): cover + inline_1…3 → split 2×2
2. **Canvas 2** (grsai grsai standard image model t2i): inline_4…7 → split 2×2
3. Итого: `cover.png` 1200×675 + `inline-01…07.png`, inject `figure.inline-quad` data-slot=inline_1…7

Hero lock: `memory/cover/assets/identity-real/*` (4 live фото) — лицо 28 лет, **новая выдуманная сцена** каждый раз. AI `scene-composition-only/hero-ref-*` — не для лица.

**Cover canon v3:** `memory/cover/cover-canon.json` — light/bright, мемы, **Wordstat query strips FORBIDDEN on cover** (Scout Wordstat = topic only), optional yellow sticky from hook, anti-repeat 14д. **Designed thumbnail:** hook H1 справа, телефон +7 922 001 65 05 низ-право, мем-стикер, **pixel_no_wordstat_query_strips PASS**. FAIL: beige/gold search-query bars top-left, face-only collapse.

**Inline visual law (HARD):** крупный человек = только Святослав на cover (`face-studio-2026-06-23.jpg`). Inline = инфографика (таблицы, схемы, графики) — **без** stock model / generated man / co-host. People-memes = маленькие стикеры (≤15% кадра) из `memory/cover/meme-top100.json`. Cover-QA FAIL на co-host human или meme person > sticker scale.

**Wordstat:** Scout hard gate via **MCP-KV** (`wordstat_get_*`). P0 buyer demand in Tyumen regions — **topic choice only**; never paint Wordstat queries on cover.png. Enable MCP-KV in Cloud Automation Tools (dashboard connector — never git).

## Image providers (HARD — owner override 2026-08-22, grsai 2026-08-22)

Cover + inline PNG **only grsai grsai standard image model** (Derouter image = optional last resort):

1. `scripts/excalibur_blog_grsai_gpt_image2_api.py` — REST: `grsaiapi.com` (Global) → `grsai.dakka.com.cn` (China). Paths: `/v1/api/generate` (json → async poll) → `/v1/images/generations` → `/v1/draw/completions` + poll. Model **`grsai standard image model`** (NOT vip). Face i2i from `face-studio-2026-06-23.jpg`.
2. Solo cover CLI: `scripts/excalibur_blog_grsai_solo_cover.py` (1200×675 + pixel QA stamp).
3. Optional last resort: `EXCALIBUR_IMAGE_FALLBACK_DEROUTER=1` → Derouter image REST (`excalibur_blog_derouter_gpt_image2_api.py`).
4. grsai down → `GRSAI IMAGE BLOCKER` — diagnose/retry; **STOP**

**Text roles unchanged:** Derouter Opus/Terra via `excalibur_blog_derouter_opus_chat.py`.

**FORBIDDEN FOREVER:** Kie (`KIE_API_KEY`, `excalibur_blog_kie_gpt_image2_api.py`), PIL template mashup (`excalibur_blog_cover_pil_compose.py`). Never `--fallback-kie`. Never upload mashup when APIs fail.

Контракты: `shared/grsai-gpt-image-api-contract.md`, `shared/derouter-gpt-image-api-contract.md` (Derouter image fallback only), `shared/kie-gpt-image-api-contract.md` (Kie = forbidden stub).

## Automation prompt

Скопируй блок ниже в **Instructions** каждого из 4 Cursor Automations (09/12/15/17 YEKT):

```text
Прочитай AGENTS.md + shared/pipeline-canon.json + shared/tenant-config.json + shared/quality-bar-9.md + shared/dzen-news-casus.md + CLOUD-AUTOMATION.md.
Если setup_complete != true — остановись (Setup).
Игнорируй Automation Memory. Memories = OFF.

Ты — ТОНКИЙ ДИРИЖЁР (default Composer — НЕ переключать модель). Прозу текстовых ролей пишет ТОЛЬКО
scripts/excalibur_blog_derouter_opus_chat.py:
  powerful claude-opus-5 → writer/sol (article prose only)
  utility gpt-5.6-terra → scout/title/research/description/cover-text/schema/cover-scene
Не пиши Scout/Research/Title/Writer/Sol/Description/Cover-text/Schema/Cover-scene своей моделью.
DEROUTER <ROLE> BLOCKER → стоп пайплайна. Нет run_budget / circuit breaker.

doctor + today.
dzen_rf_pack: shared/dzen-content-rules.md + rf-blocked-entities.json.
needs_scout → Scout (signal_urls из tenant) — handoff prose через derouter --role scout.
Scout HARD gates перед handoff: MCP-KV Wordstat + shared/dzen-news-casus.md (default news-casus shape, forbidden checklist hooks; слабый Wordstat → rework news phrasing, NOT drop casus) + `scout_helper.py --check-query` (topic focus + **story-duplicate** `shared/scout-story-clusters.json` vs ledger/live WP — Wordstat rework ≠ same legal risk+plot).
research_start → Research → Title → Writer → Sol — каждый шаг через derouter --role <…>.
Title/Writer/Sol: news headline + casus arc (событие → финал → практика после); H1 forbidden: «чеклист», «N шагов», «стоит ли покупать»; body 2000–2600, useful part AFTER story.
Description: news card energy (shared/dzen-description-rules.md), not SEO checklist blurb.

Conversion (shared/quality-bar-9.md + SOUL + tenant-config cta_channels):
  Early после hook+TL;DR: brand beat + curiosity + ТОЛЬКО Telegram https://t.me/Tyumen_Rieltor и MAX https://max.ru/id561413315447_biz
  Mid после практического блока (aftermath casus): лёгкий TG+MAX (excalibur-cta-mid)
  End: dual CTA консультация / сразу в сделку + полный набор (site, guides, Dzen, VK, about)
  Телефон +7 922 001 65 05 на cover + один раз в теле
  Interlink 2–4 sibling из shared/published-articles.md (status=published)

После Sol: pipeline_canon stamp + opening_meta + html_linter + quality-bar-9 gate → quality-bar-9.json all_pass.
Description → Cover-text || Schema → Cover (hook H1 + phone + meme + optional yellow sticky — **NO Wordstat query strips**) → Cover-QA pixel gate (`pixel_no_wordstat_query_strips`, `pixel_hook_title_present`, `pixel_phone_readable`, `pixel_meme_present`, `pixel_layout_not_collapsed`; Fixer: regen cover panel only) → Indexer.

Publish ТОЛЬКО если FTP secrets настроены И EXCALIBUR_BLOG_ALLOW_PUBLISH=yes на процессе И quality-bar-9.json all_pass (или `--media-refresh --featured-only` для cover-only: pixel Cover-QA PASS + wp_post_id); иначе STOP после Indexer.
Live = SFTP replace (не жди merge article в main для сайта). Код/канон — в main.

Один run = одна статья. Fixer → merge code fixes → content-learner.
```

Секреты только из Cloud Secrets (`PUBLIC_SITE_URL`, SFTP, image API, Wordstat MCP). Allow flag — **runtime only**, не в git.

## Отдельный поток Daily (не этот automation)

На сайте есть короткие посты ~800–900 слов (`/blog/bez-rubriki/<timestamp>/`, одна `cleaned_*.png`, без inline). Частота 07/10/13/16/19 YEKT — **вне** этого longform-расписания 09/12/15/17.
