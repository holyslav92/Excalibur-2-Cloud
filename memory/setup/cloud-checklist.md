# Cloud checklist — The Риэлтор

Ответы yes/no. **Секреты сюда не писать.**

| Пункт | Статус | Комментарий |
|-------|--------|-------------|
| Репозиторий подключён к Cursor Cloud Environment | yes | origin: holyslav92/Excalibur-2-Cloud |
| Automation Tools → **Memories = OFF** | action_needed | Выключить вручную; docs: Memories ON by default |
| Secrets: PUBLIC_SITE_URL | action_needed | Значение: сайт тенанта (https в Secrets, в git — {{SITE_BASE}}) |
| Secrets: FTP_HOST / FTP_USER / FTP_PASS / FTP_ROOT | unknown | Нужны перед Publish |
| MCP Wordstat (Scout **hard gate**) | required in prod | `WORDSTAT_API_KEY` + `WORDSTAT_FOLDER_ID`; regions 55+11176 |
| MCP WordPress blob / image API (если нужны) | optional | WP уже на сайте тенанта |
| Image API key (Kie / provider) | unknown | Нужен для Cover |
| Yandex Metrika tokens | optional | Content-learner |
| First-run automation = Setup prompt | yes | Этот прогон |
| Daily automation = CLOUD-AUTOMATION.md (после setup) | pending | Включать после complete=true |

## Разница First-run vs Daily

- **First-run:** заполнить тенанта, SOUL, визуал. Не Scout/Publish.
- **Daily:** после setup — канон Scout → Research → … → Publish.
