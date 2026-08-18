# Cloud First Run — Excalibur-2-Cloud

Официальные источники Cursor (перечитайте при сомнении):

- https://cursor.com/docs/cloud-agent
- https://cursor.com/docs/cloud-agent/setup
- https://cursor.com/docs/cloud-agent/automations
- https://cursor.com/docs/cloud-agent/security

## 1. Environment

1. Dashboard → Cloud Agents → Environments.
2. Подключите этот репозиторий.
3. ` .cursor/environment.json` уже задаёт `install` (pip + doctor).
4. Дождитесь успешного Build.

## 2. Secrets

В Secrets (не в git) положите минимум:

| Secret | Зачем |
|--------|--------|
| `PUBLIC_SITE_URL` | Live сайт; в артефактах остаётся `{{SITE_BASE}}` |
| `FTP_HOST` / `FTP_USER` / `FTP_PASS` / `FTP_ROOT` | SFTP publish (имена FTP_*, транспорт SFTP) |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` только когда готовы публиковать |
| Image API (mcp-derouter 2K) | Cover longform 2× quad canvas |
| `WORDSTAT_API_KEY` + `WORDSTAT_FOLDER_ID` (или `YANDEX_SEARCH_API_KEY` + `YANDEX_FOLDER_ID`) | **Scout hard gate** — без Wordstat тема не берётся |
| MCP Wordstat (`mcp-yandex-wordstat`, см. `.cursor/mcp.json.example`) | live спрос + регион Тюмень (55, 11176) |
| MCP tokens (legacy) | `MCP_KV_TOKEN` — сохранить если уже есть |
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

Подключите нужные MCP в Cloud / automation tools:

- **Wordstat (Scout — обязательно):** `npx -y mcp-yandex-wordstat` + Secrets `WORDSTAT_API_KEY` / `WORDSTAT_FOLDER_ID` (шаблон `.cursor/mcp.json.example`). Scout **FAIL**, если Wordstat не настроен или нет регионального спроса Тюмень (region ids `55`, `11176` — `memory/cover/wordstat-geo.json`).
- Image generation **mcp-derouter** 2K (Cover PRIMARY)
- WordPress content blob (если используете MCP publish helpers)
- Legacy `user-mcp-kv` — сохранить если уже подключён; не заменяет official Wordstat

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

4×/день YEKT (09, 12, 16, 20). См. `CLOUD-AUTOMATION.md`.

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
