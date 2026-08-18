# Scout rolling memory

**Обновляет:** `excalibur-blog-scout` после каждого прохода.

| Файл | Назначение |
|------|------------|
| `klyshin-topic-bank.md` | Человекочитаемый банк хуков Алексея Клышина |
| `klyshin-topic-bank.json` | Машиночитаемый банк для Scout / gates |

**Алгоритм (HARD):** Klyshin hook → candidate angle → Wordstat `top_requests` (Тюмень 55 + область 11176) → P0 только при живом объёме. Слабый Wordstat → **skip hook**.

Wordstat остаётся demand gate. Klyshin — angle/hook bank, не замена частот.
