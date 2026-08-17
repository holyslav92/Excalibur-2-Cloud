# Cloud checklist — The Риэлтор

Ответы yes/no. **Секреты сюда не писать.**

| Пункт | Статус | Комментарий |
|-------|--------|-------------|
| Репозиторий подключён к Cursor Cloud Environment | yes | origin: holyslav92/Excalibur-2-Cloud |
| Automation Tools → **Memories = OFF** | action_needed | Выключить вручную; docs: Memories ON by default |
| Secrets: PUBLIC_SITE_URL | action_needed | Значение: сайт тенанта (https в Secrets, в git — {{SITE_BASE}}) |
| Secrets: FTP_HOST / FTP_USER / FTP_PASS / FTP_ROOT | yes | Хост tymenrieltor.ru (Beget). Значения только в Secrets / site.env.local, не в git |
| MCP Wordstat (если нужен Scout) | optional | Желателен для запросов «квартира Тюмень» |
| MCP WordPress blob / image API (если нужны) | optional | WP уже на сайте тенанта |
| Image API key (Kie / provider) | skip | Kie не используем. Картинки: MCP DEROOTER, 2×2K |
| Yandex Metrika tokens | optional | Content-learner |
| First-run automation = Setup prompt | yes | Этот прогон |
| Daily automation = CLOUD-AUTOMATION.md (после setup) | pending | Включать после complete=true |

## Разница First-run vs Daily

- **First-run:** заполнить тенанта, SOUL, визуал. Не Scout/Publish.
- **Daily:** после setup — канон Scout → Research → … → Publish.
