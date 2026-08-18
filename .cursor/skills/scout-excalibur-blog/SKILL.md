---
name: scout-excalibur-blog
description: Pick P0 topic from live signal + MCP-KV Wordstat buyer demand (Tyumen geo).
---

# Scout — живой сигнал + MCP-KV Wordstat (buyer P0)

Тему выбираешь из **buyer-спроса** (купить квартиру, новостройки, ипотека, ЕГРН…)
в Тюмени/области — **не** из brand vanity «риэлтор тюмень» (~низкий объём).

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

**Сравнение:** тот же `phrase` с `regions: ["225"]` когда нужен national контекст.

**Optional:** `wordstat_get_dynamics` на выбранный P0.

### НЕ P0 (brand vanity — только справка)

«риэлтор тюмень», «услуги риэлтора тюмень» — низкий объём. Не строить тему только из них.

### Handoff (обязательно)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat: mcp_kv live | regions 55,11176 vs RU 225 | P0 «купить квартиру в тюмени» 23060 | «новостройки тюмень» … | brand_vanity «риэлтор тюмень» 1164 (not P0)
```

Запрещено: `skip`, `PARTIAL`, выдуманные частоты, только brand query.

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

## Внешний сигнал

1. Новости/хайп недвижимости + `scout_signal_urls` (≥2 URL, сегодня)
2. Wordstat P0 buyer volume (см. выше)
3. `published-titles-only.md` — anti-dup only

## Выход

`.cursor/excalibur-blog-handoff.md` — см. шаблон выше + `topic_id`, `title`, `external_signal`, `signal_urls`.

## Алгоритм

1. `wordstat_get_user_info` → OK
2. 3–4× `wordstat_get_top_requests` (P0 seeds, regions 55+11176)
3. WebFetch сигнал → URL
4. Title из **buyer P0**, не из «риэлтор тюмень»
5. handoff + `wordstat_gate.py handoff` → стоп
