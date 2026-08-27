# Scout rolling memory

**Обновляет:** `excalibur-blog-scout` после каждого прохода.

| Файл | Назначение |
|------|------------|
| `klyshin-topic-bank.md` | Человекочитаемый банк хуков Алексея Клышина (optional) |
| `klyshin-topic-bank.json` | Машиночитаемый банк для Scout / gates |
| `used-clusters.json` | Закрытые story-clusters (30д anti-repeat) |
| `next-cluster-guidance.md` | Открытые углы для следующих weekday-слотов |

**Алгоритм (канон):** live blog ~20 + ledger → `--sync-used-clusters` → Wordstat `top_requests` (Тюмень 55 + область 11176) → **evaluate + rework** → **новый** cluster (30д). Klyshin optional (только свежий). Логировать **final P0 phrase+volume** + **story_dup_check: PASS**.
