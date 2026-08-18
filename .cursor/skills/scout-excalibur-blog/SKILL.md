---
name: scout-excalibur-blog
description: Pick topic from live channel/news hype with Wordstat hard gate (Tyumen geo).
---

# Scout — тема из живого сигнала + Wordstat hard gate

Ты **не придумываешь** тему из старых заголовков. Сначала — живой сигнал **и** подтверждённый спрос Wordstat с affinity **Тюмень / Тюменская область**.

## Wordstat — HARD GATE (не optional)

**Без настроенного Wordstat Scout = BLOCK.** Перед выбором темы:

```bash
python3 scripts/excalibur_blog_wordstat_gate.py config
```

Должен быть `OK`. Иначе — `WORDSTAT NOT CONFIGURED`, handoff не пишем.

### MCP

- PRIMARY: `mcp-yandex-wordstat` (`npx -y mcp-yandex-wordstat`) — см. `.cursor/mcp.json.example`
- Legacy `user-mcp-kv` — сохранить если уже есть; **не заменяет** official Wordstat
- Tool: `wordstat_get_top_requests` (или эквивалент пакета)

### Регион (не угадывать)

`memory/cover/wordstat-geo.json`:

- город **Тюмень** = `55`
- **Тюменская область** = `11176`

**Каждый** Wordstat-вызов: `regions: [55, 11176]` (или параметр пакета с этими id).

### Вызовы

2–4 **отдельных** solo `CallMcpTool` (по одному за turn):

1. родительская фраза + «Тюмень»
2. синоним / угол сделки
3. смежный риск (ЕГРН, аванс, доверенность…)
4. optional — район/ЖК если уместно

Смотришь **частотности** и **топ-похожие**. Тема без регионального спроса → **другой угол или BLOCK**.

### Handoff wordstat field (обязательно)

```text
wordstat: Тюмень regions 55,11176 | «квартира тюмень» 12400 | «проверить квартиру перед покупкой» 3200 | …
```

Запрещено: `skip`, `PARTIAL`, пустое поле, только national без Тюмени.

После handoff:

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

## Откуда брать тему

1. **Новости/хайп** недвижимости, сделок, ипотеки, законов — с датой доступа.
2. Каналы тенанта (`scout_signal_urls`) + 1–2 чужих источника.
3. **Wordstat** — подтверждение спроса (см. выше).
4. `published-titles-only.md` — только anti-dup.

## Выход

`.cursor/excalibur-blog-handoff.md`:

```text
=== EXCALIBUR BLOG SCOUT ===
topic_id: B111
title: <короткий title>
external_signal: ...
signal_urls:
- ...
- ...
signal_accessed: YYYY-MM-DD
wordstat: Тюмень 55,11176 | «фраза» частота | ...
incident_report: none
```

Без `signal_urls` + сегодня + **live wordstat с Тюменью** — Scout **BLOCK**.

## Жёсткие запреты

- Тема без Wordstat / без регионального affinity Тюмень
- Invent из published-titles / «продолжим серию»
- RF DENY heroes (`rf-blocked-entities.json`, `dzen-content-rules.md`)
- `memory/topics/`, SEO-хвосты, research_start, publish
- Читать live-статьи сайта как образец

## Алгоритм

1. `wordstat_gate.py config` → OK
2. WebFetch / SERP → сигнал + URL
3. 2–4 Wordstat calls с regions 55+11176
4. `--suggest-next` → один title из спроса
5. handoff + `wordstat_gate.py handoff` → стоп
