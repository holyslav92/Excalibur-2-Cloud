---
name: scout-excalibur-blog
description: Pick P0 topic from Klyshin hooks × MCP-KV Wordstat — evaluate and rework for Tyumen demand.
---

# Scout — Klyshin hooks × Wordstat (evaluate + rework)

## Thin conductor + Derouter powerful (HARD)

Handoff-проза (topic, rework log, title draft) — **только** через Derouter powerful tier (claude-opus-5).
Wordstat частоты — live MCP-KV (не Derouter). Cursor не пишет handoff своей моделью.

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role scout \
  --system-file skills/scout-excalibur-blog/SKILL.md \
  --user-file <assembled-scout-inputs.md> \
  --output .cursor/excalibur-blog-handoff.md \
  --article-dir <article_dir_or_memory/scout>
```

`DEROUTER SCOUT BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

Тему выбираешь из **трёх обязательных источников** (все три — HARD):

1. **Алексей Клышин (angle bank)** — `memory/scout/klyshin-topic-bank.md` + `.json`, канал `https://t.me/klyshin_A`.
2. **Wordstat (demand spine)** — MCP-KV buyer-спрос в Тюмени/области (55 + 11176), сравнение с RU **225**.
3. **Dzen news-casus shape** — `shared/dzen-news-casus.md`: default = **новость-казус** с финалом, не how-to checklist.

Klyshin **не** заменяет частоты. Wordstat **не** binary skip gate. Слабый Wordstat **не** повод сменить shape на чеклист.

## Алгоритм (канон)

```text
1. Прочитать shared/dzen-news-casus.md (champion formula + forbidden hooks)
2. Klyshin hook/angle (bank + live @klyshin_A) → news-casus angle (событие + риск + метка времени + финал)
3. wordstat_get_top_requests: hook phrase + tyumen analogs (regions 55, 11176; compare 225)
4. Слабый объём → НЕ drop casus. Rework:
   - локализовать на Тюмень
   - переформулировать **новостной** angle (не «чеклист / N шагов»)
   - заменить жаргон на buyer-поиск (егрн, наследство, ипотека, аванс, доверенность…)
   - wordstat_get_top_requests по similar queries
   - выбрать ближайший high-frequency cluster с тем же risk/story + casus shape
5. Title draft — news headline в ритме Klyshin. P0 Wordstat — demand spine под H1; stickers/H2 из reworked live queries
6. Skip ТОЛЬКО если после rework нет честного buyer-intent **или** нельзя casus с финалом
7. Лог: original Klyshin hook + final Wordstat P0 phrase+volume + dzen_casus_shape: PASS (+ rework steps)
```

## Klyshin — ALWAYS joint with Wordstat

- Читай `memory/scout/klyshin-topic-bank.md` + свежий `https://t.me/s/klyshin_A`
- После Scout **обнови** банк: `last_seen`, `wordstat_rework_log`, `final_p0`, `used_in_articles`
- **Не копируй** Москву/Дубай/МКАД как P0 — локализуй на Тюмень или rework до Tyumen cluster
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

### Rework vocabulary (buyer search spine)

При слабом объёме на «юридическом» hook — пробуй живые кластеры:

- егрн / выписка егрн / проверка егрн
- наследство / наследники / отказ от наследства
- ипотека / новостройка / вторичка
- аванс / задаток / безопасный расчёт / аккредитив
- пенсионер / пожилой продавец / опека
- доверенность / банкротство / торги
- маткапитал / детская доля

Для каждого rework-раунда — **отдельный** `top_requests` по probe; сохраняй частоты.

**Сравнение:** тот же `phrase` с `regions: ["225"]` когда нужен national контекст.

**Optional:** `wordstat_get_dynamics` на выбранный final P0.

### НЕ P0 (brand vanity — только справка)

«риэлтор тюмень», «услуги риэлтора тюмень» — низкий объём. Не строить тему только из них.

### Dzen news-casus gate (обязательно)

Перед handoff проверь shape по `shared/dzen-news-casus.md`:

- **PASS:** завершённое событие + именованный риск + временная метка + «думал, что безопасно» + финал (суд/отмена/деньги).
- **FAIL shape:** главный hook = «чеклист», «N шагов», «стоит ли покупать», «как купить без риелтора» без casus.
- **Слабый Wordstat:** rework **news-формулировки**, не меняй default на how-to.

В handoff строка:

```text
dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «через год» | finale: «суд отменил регистрацию»
```

### Handoff (обязательно)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: <hook_id> | original: «…» | angle: <…> | signal: https://t.me/klyshin_A/…
dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «…» | finale: «…»
wordstat_rework: probe «…» <freq> → … → final P0 «купить квартиру в тюмени» 23060 | clusters tried: …
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «…» <freq> | …
```

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

## Внешний сигнал

1. **klyshin_A** + ≥1 другой URL из `scout_signal_urls` (сегодня)
2. Wordstat final P0 buyer volume после rework-цикла
3. `published-titles-only.md` + **`shared/published-articles.md` + live WP titles** — anti-dup title AND **HARD story-duplicate** (same legal risk + plot)

## HARD story-duplicate (не только title)

**Wordstat may refine phrasing — must NOT recycle the same story.**

Перед handoff прогони:

```bash
python3 scripts/excalibur_blog_scout_helper.py --check-query "<title draft + hook + slug>"
# или явно:
python3 scripts/excalibur_blog_scout_story_dup.py --text "<title + hook + slug>"
```

Кластеры: `shared/scout-story-clusters.json` — наследство+сын первого брака без отказа, маткапитал без долей, доверенность+СВО, задаток/торги, −2 млн и т.д.

**BLOCKER `SCOUT STORY DUPLICATE`** если hook/title попадает в тот же cluster, что уже опубликованный sibling (ledger **или** live WP, напр. `/bez-rubriki/nasledstvo-ne-proshlo-tri-goda-avans-uzhe-nesut/` vs B07). Skip hook — другой legal risk + другой family-plot, не перефраз.

## Выход

`.cursor/excalibur-blog-handoff.md` — topic_id, title draft (Klyshin rhythm), external_signal, signal_urls, klyshin_hook + wordstat_rework + wordstat lines.

## Чеклист

1. `wordstat_get_user_info` → OK
2. Fetch klyshin_A + holyslav/dzen signals
3. Pick hook from bank or fresh post → update bank
4. `wordstat_get_top_requests` на hook + probes (55+11176; compare 225)
5. Слабый объём → rework (локализация + buyer jargon + similar queries) — **не** мгновенный skip
6. Final P0 + title angle (news headline, не checklist hook); лог original hook + final phrase+volume + `dzen_casus_shape`
7. **`scout_helper.py --check-query`** (focus + story-dup + slug overlap) → BLOCKER если duplicate
8. handoff + `wordstat_gate.py handoff` → стоп
