# Cloud First Run — Excalibur-2-Cloud

Официальные источники Cursor (перечитайте при сомнении):

- https://cursor.com/docs/cloud-agent
- https://cursor.com/docs/cloud-agent/setup
- https://cursor.com/docs/cloud-agent/automations
- https://cursor.com/docs/cloud-agent/security

## 1. Environment

1. Dashboard → Cloud Agents → Environments.
2. Подключите этот репозиторий.
3. `.cursor/environment.json` задаёт `install` (`scripts/excalibur_blog_cloud_install_deps.sh`: apt `tesseract-ocr` + `tesseract-ocr-rus`, pip, doctor).
4. Дождитесь успешного Build.

## 2. Secrets

В Secrets (не в git) положите минимум:

| Secret | Зачем |
|--------|--------|
| `PUBLIC_SITE_URL` | Live сайт; в артефактах остаётся `{{SITE_BASE}}` |
| `FTP_HOST` / `FTP_USER` / `FTP_PASS` / `FTP_ROOT` | SFTP publish (имена FTP_*, транспорт SFTP) |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` только когда готовы публиковать |
| Image API (Derouter REST 2K) | Cover longform 2× quad canvas |
| **MCP-KV** (Automation → Tools) | **Wordstat PRIMARY** — `wordstat_get_*` tools; personal connector from mcp-kv.ru dashboard (**never git**) |
| `MCP_KV_TOKEN` | Optional Cloud Secret if not using dashboard connector |
| `WORDSTAT_*` / `YANDEX_*` | Optional API fallback (secondary to MCP-KV) |
| `YANDEX_METRIKA_*` | Опционально Content-learner |

Рекомендуется Runtime Secrets для паролей (не светятся в transcript).

Шаблон имён: `.env.example`.

## 3. Memories — ВЫКЛЮЧИТЬ

В Automation → Tools: **Memories = OFF**.

По доке Cursor Memories **включены по умолчанию** и пишут `MEMORIES.md`
вне рабочей копии. Для блог-пайплайна это опасно: старый чужой прогон /
ошибочная «память» ломает следующие статьи. Setup и Daily prompt явно
говорят «игнорируй Automation Memory» — но UI-выключатель надёжнее.

## 4. MCP

**Обязательно для Scout:** включите **MCP-KV** в Automation → Tools (личный connector с dashboard mcp-kv.ru — **не коммитить** SSE URL / connector id / tokens в git).

Wordstat tools (server `MCP-KV`):

- `wordstat_get_user_info` — preflight
- `wordstat_get_top_requests(phrase, regions, numPhrases)`
- `wordstat_get_regions` / `wordstat_get_regions_tree` / `wordstat_get_dynamics`

Регионы тенанта: lookup → `memory/cover/wordstat-geo.json` (Тюмень / область; compare RU `225`).

Scout **FAIL**, если Wordstat MCP недоступен или handoff без live частот. P0 — buyer queries (купить квартиру, новостройки, ипотека, ЕГРН…), **не** brand «риэлтор тюмень».

Также подключите:

- Image generation **Derouter REST** (`DEROUTER_IMAGE_MODEL`), 2K (Cover PRIMARY; Kie secondary)
- WordPress content blob (если используете MCP publish helpers)

## 5. Two automations

### A) First-run (один раз)

```text
Прочитай AGENTS.md и SETUP.md.
Если memory/setup/status.json не complete — работай как excalibur-blog-setup
(skill setup-excalibur-blog): блоки 0–7, заполняй файлы, вызывай
Task(excalibur-blog-setup-voice) и Task(excalibur-blog-setup-visual).
Не запускай Scout/Publish. Игнорируй Automation Memory.
Memories в Tools должны быть OFF.
```

### B) Longform blog (после setup)

4×/будни YEKT (09, 12, 15, 17 — окно 9–17, **не** 20:00). См. `CLOUD-AUTOMATION.md`.

### Identity photos (host_reference)

Вложения в чат Cloud Agent **не попадают** на диск VM. Live-фото владельца кладите в
`memory/setup/visual-inbox/` с каноническими именами (`face-hoodie-airpods.jpeg`, …),
затем:

```bash
python3 scripts/excalibur_blog_identity_real.py --stage-from-inbox
python3 scripts/excalibur_blog_identity_real.py --check
```

Канон: `memory/cover/assets/identity-real/`. AI `scene-composition-only/` — не для лица.

## 6. Проверка

```bash
python3 scripts/excalibur_blog_doctor.py
```

Doctor должен видеть `setup complete` только после Setup.
До этого пайплайн публикации блокируется.
