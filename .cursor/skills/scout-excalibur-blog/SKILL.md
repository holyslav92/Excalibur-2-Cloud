---
name: scout-excalibur-blog
description: Pick P0 Tyumen news-casus topic — Wordstat demand + 30d story-cluster anti-repeat; Klyshin optional.
---

# Scout — Wordstat demand + 30d story-cluster anti-repeat

## OWNER LOCK — newbuild only + top-energy angles (2026-09-05, permanent)

**Читай:** `shared/newbuild-focus-lock.md` + `shared/dzen-top-angle-newbuild-lock.md` + `shared/pipeline-canon.json` → `owner_lock_permanent.newbuild_focus`.

- **ONLY** новостройки в Тюмени: квартиры **и** дома (коттедж / КП / ИЖС / таунхаус от застройщика).
- **Top-energy mirror:** кради **эмоцию** top-10 Дзена (almost lost / stopped before money / paper clean then broke / someone else took object / clock ran out / number vs zero paid) — **plot ONLY newbuild**. FORBIDDEN: retitle secondary (бабушка, банкрот продавца, чистая ЕГРН-вторичка, опека/маткапитал secondary…).
- **Аудитория:** семьи с детьми + инвесторы → конверсия в TG/MAX/телефон за **покупку новостройки**.
- **DENY:** вторичка как сюжет; calm «гайд / N шагов / как устроена».
- **Klyshin:** optional, только свежий TG/YouTube, **и только если hook = новостройка**.
- **Frozen secondary clusters** — не retitle. **HARD anti-dupe:** 30d cluster + H1 fingerprint + formula spam (last 3). См. `memory/scout/used-clusters.json`.

Gate: `python3 scripts/excalibur_blog_topic_focus.py --text "<title>"` → `NEWBUILD FOCUS BLOCKER` на вторичку.

## Thin conductor + Derouter utility (HARD)

Handoff-проза (topic, rework log, title draft) — **только** через Derouter utility tier (gpt-5.6-terra).
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

## Источники темы

**Обязательно (HARD):**

1. **Wordstat (demand spine)** — MCP-KV buyer-спрос в Тюмени/области (55 + 11176), сравнение с RU **225**.
2. **Dzen news-casus shape** — `shared/dzen-news-casus.md`: hot **news-casus актуалочка** с финалом и **comment magnet**, не how-to checklist.
3. **Anti-repeat 30д** — live blog (~20) + ledger + `memory/scout/used-clusters.json` (same story/cluster = FAIL даже при новом title).

**Опционально:**

- **Klyshin** — `memory/scout/klyshin-topic-bank.*` + **только свежий** `https://t.me/klyshin_A` или **свежий** YouTube. Старые посты **не** брать, если кластер закрыт. Новый hot Tyumen casus **без** Klyshin — OK и **предпочтителен**, когда Klyshin дублировал бы закрытый plot.

**Цель каждой темы — вовлечение в Дзен** (лайки, комментарии, подписки): stakes в Тюмени, завершённое событие, финал. Scout намечает **угол спора** для comment magnet.

Klyshin **не** заменяет частоты. Wordstat **не** binary skip gate. Слабый Wordstat **не** повод сменить shape на чеклист.

## Перед topic lock (HARD)

```text
1. Fetch live PUBLIC_SITE_URL/blog/ — последние ~20 заголовков (не тела)
2. Прочитать shared/published-articles.md + shared/published-titles.md (+ published-titles-only.md)
3. python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters
4. Прочитать memory/scout/used-clusters.json + memory/scout/next-cluster-guidance.md
5. Выбрать кластер, которого НЕТ в closed list (30д)
```

Каждый weekday-слот (09/12/15/17 YEKT) = **другой** story-cluster равного engagement-качества.

## Алгоритм (канон)

```text
1. shared/dzen-news-casus.md (champion formula + forbidden hooks)
2. shared/dzen-top-angle-newbuild-lock.md (top-energy → newbuild ONLY)
3. Live blog + ledger + used-clusters → список закрытых кластеров
3. Свежий Tyumen casus angle (Klyshin optional) → news-casus (событие + риск + время + финал)
4. wordstat_get_top_requests: hook phrase + tyumen analogs (55, 11176; compare 225)
5. Слабый объём → rework **newbuild** news angle (семейная ипотека, эскроу, ДДУ, уступка, срок сдачи, отделка, КП), НЕ drop casus и **НЕ** вторичка
6. Title draft — news headline. P0 Wordstat — demand spine под H1
7. scout_helper.py --check-query → BLOCKER если duplicate cluster / fingerprint / formula spam
8. Лог: top_energy_mirror + newbuild_mechanism + why_newbuild_not_secondary + klyshin_hook (optional) + final P0 + dzen_casus_shape: PASS + comment_magnet_angle + anti_dupe_hard: PASS
```

## Klyshin — OPTIONAL (если используешь)

- Только **свежий** пост @klyshin_A или **свежий** YouTube — не архив, если plot уже в `used-clusters.json`
- После Scout **обнови** банк: `last_seen`, `wordstat_rework_log`, `final_p0`, `used_in_articles`
- **Не копируй** Москву/Дубай как P0 — локализуй на Тюмень
- Факты в статье: **Святослав Шакин / Тюмень**, не копипаст канала

`scout_signal_urls` (tenant-config): site blog + dzen holyslav + t.me/holyslav92 (+ klyshin_A optional)

## Wordstat — HARD GATE (MCP-KV)

**Частоты не выдумывать.** Если MCP-KV Wordstat недоступен → **SCOUT BLOCK**.

```bash
python3 scripts/excalibur_blog_wordstat_gate.py config
```

Preflight: `wordstat_get_user_info` → OK. Регионы: **Тюмень=55**, **область=11176**, **RU=225**.

### Handoff (обязательно)

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: <almost_lost_home|stopped_before_money|…>
newbuild_mechanism: «…»
why_newbuild_not_secondary: «…»
klyshin_hook: optional | <hook_id> | original: «…» | signal: https://t.me/klyshin_A/… (или none)
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: <ids>
dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «…» | finale: «…»
comment_magnet_angle: «…?»
wordstat_rework: probe «…» <freq> → … → final P0 «…» <freq>
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «…» <freq>
story_dup_check: PASS | cluster_id: <новый уникальный>
h1_fingerprint_check: PASS | fingerprint: <…>
formula_spam_check: PASS | last3_mechanisms: <…>
anti_dupe_hard: PASS
```

## HARD anti-dupe (30 дней + fingerprint + formula spam)

**Wordstat may refine phrasing — must NOT recycle the same story/cluster/formula.**

```bash
python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters
python3 scripts/excalibur_blog_scout_helper.py --check-query "<title draft + hook + slug>"
python3 scripts/excalibur_blog_scout_story_dup.py --text "<title + hook + slug>"
```

| Gate | BLOCKER |
|------|---------|
| Same `cluster_id` 30d | `SCOUT STORY DUPLICATE` |
| Same H1 fingerprint (number+mechanism) 30d / same-day | `H1 FINGERPRINT DUPLICATE` |
| Last 3 published = same skeleton without new mechanism | `FORMULA SPAM` |
| Frozen secondary plot retitle | `FROZEN SECONDARY RECYCLE` |

`research_start` повторяет gate **до Writer**. См. `shared/dzen-top-angle-newbuild-lock.md`.

**4 slots/day (09/12/15/17 YEKT) — не резать.** Качество > retitle.

## Чеклист

1. Live blog ~20 + ledger + published-titles
2. `--sync-used-clusters` + read closed clusters
3. `wordstat_get_user_info` → OK
4. Pick **новый** cluster (не в used-clusters 30д)
5. Wordstat probes + rework if weak
6. `scout_helper.py --check-query` → PASS
7. handoff + `wordstat_gate.py handoff` → стоп
