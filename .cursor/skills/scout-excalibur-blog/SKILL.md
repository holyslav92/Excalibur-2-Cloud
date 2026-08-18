---
name: scout-excalibur-blog
description: Pick P0 topic from Klyshin hooks × MCP-KV Wordstat buyer demand (Tyumen geo).
---

# Scout — Klyshin hooks × Wordstat (dual gate)

Тему выбираешь из **двух обязательных источников**:

1. **Wordstat (demand gate)** — buyer-спрос в Тюмени/области (55 + 11176).
2. **Алексей Клышин (angle bank)** — `memory/scout/klyshin-topic-bank.md` + `.json`, канал `https://t.me/klyshin_A`.

Klyshin **не** заменяет частоты. Алгоритм:

```text
Klyshin hook → candidate angle → Wordstat top_requests (Tyumen analog) → P0 or SKIP
```

Слабый Wordstat → **skip hook**, даже если пост Клышина яркий.

## Klyshin — ALWAYS joint with Wordstat

- Читай `memory/scout/klyshin-topic-bank.md` + свежий `https://t.me/s/klyshin_A`
- После Scout **обнови** банк: `last_seen`, новые hooks, `used_in_articles`
- **Не копируй** Москву/Дубай/МКАД как P0 — локализуй на Тюмень или drop
- Факты в статье: **Святослав Шакин / Тюмень**, не копипаст канала

`scout_signal_urls` (tenant-config): **klyshin_A** + dzen holyslav + site blog + t.me/holyslav92

## Wordstat — HARD GATE (MCP-KV)

**Частоты не выдумывать.** Если `CallMcpTool` на MCP-KV Wordstat недоступен → **SCOUT BLOCK**.

```bash
python3 scripts/excalibur_blog_wordstat_gate.py config
```

### Preflight (обязательно, первый solo CallMcpTool)

`MCP-KV` → `wordstat_get_user_info`  
Если ошибка / tool missing → **WORDSTAT MCP BLOCKER**, handoff не пишем.

### Регионы (lookup, не гадать)

1. `wordstat_get_regions_tree` — если `memory/cover/wordstat-geo.json` устарел
2. Канон после lookup: **Тюмень=55**, **Тюменская область=11176**, **Россия=225**

### P0 buyer seeds (gold)

`wordstat_get_top_requests` с `regions: ["55","11176"]`, `numPhrases` 10–50:

- купить квартиру тюмень
- новостройки тюмень
- ипотека тюмень
- проверка егрн / выписка егрн
- эскроу / дду
- аренда квартира тюмень

Для каждого Klyshin-hook — **отдельный** `top_requests` по `wordstat_probes` из json.

**Сравнение:** тот же `phrase` с `regions: ["225"]` когда нужен national контекст.

**Optional:** `wordstat_get_dynamics` на выбранный P0.

### НЕ P0 (brand vanity — только справка)

«риэлтор тюмень», «услуги риэлтора тюмень» — низкий объём. Не строить тему только из них.

### Handoff (обязательно)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat: mcp_kv live | regions 55,11176 vs RU 225 | P0 «купить квартиру в тюмени» 23060 | …
klyshin_hook: <hook_id> | angle: <…> | signal: https://t.me/klyshin_A/…
```

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

## Внешний сигнал

1. **klyshin_A** + ≥1 другой URL из `scout_signal_urls` (сегодня)
2. Wordstat P0 buyer volume для выбранного hook
3. `published-titles-only.md` — anti-dup only

## Выход

`.cursor/excalibur-blog-handoff.md` — topic_id, title (Klyshin rhythm draft OK), external_signal, signal_urls, wordstat + klyshin_hook lines.

## Алгоритм

1. `wordstat_get_user_info` → OK
2. Fetch klyshin_A + holyslav/dzen signals
3. Pick hook from bank or fresh post → update bank
4. 3–4× `wordstat_get_top_requests` (P0 seeds + hook probes, regions 55+11176)
5. If volume weak → next hook or SCOUT BLOCK
6. Title angle from hook; P0 phrase from Wordstat, not brand vanity
7. handoff + `wordstat_gate.py handoff` → стоп
