# Excalibur-2-Cloud Instructions

Язык: русский (тенант может сменить в `shared/tenant-config.json`).

## OWNER LOCK (permanent — main, не chat memory)

Три столпа зафиксированы в `shared/pipeline-canon.json` → `owner_lock_permanent`. **Не ослаблять** без явного owner override.

| # | Столп | Канон |
|---|--------|--------|
| 1 | **Engagement bomb** | Цель поста = **вовлечение в Дзен** (лайки, комментарии, подписки). Форма = hot **news-casus актуалочка** (Тюмень, stakes, финал). **Прозаический лид 4–6 предложений** → **early TG+MAX** → история → практика → **ending landing (agency, not panic)** → CTAs + **comment magnet** (один острый вопрос). Heat casus сохраняем; посадка = ручка до аванса, не «бегите». **Запрещено:** TL;DR, «Быстрый инсайт», bullet-dump в первом экране, how-to checklist вместо casus; sugar-happy ending; checklist как эмоциональный финал; «риски везде — как покупать». |
| 2 | **Meme canon v1** | Covers + inlines: **only** `memory/cover/meme-top100.json` real templates. **People + cats** (NOT cats-only). **On-topic + funny**. Stickers ≤15%, **never** hook title / host face / phone (+80px). Anti-repeat **14д** (`used-motifs.json`). `meme_picks` in cover-text → quad-manifest. |
| 3 | **Cover fail-fast** | `excalibur_blog_grsai_solo_cover.py`: max **2** full attempts (`EXCALIBUR_COVER_MAX_ATTEMPTS`). **grsai standard only** — VIP tier отключён. Timebox **≤15–20 мин** на cover. После бюджета → `cover/cover-budget-result.json` → **Indexer** (не бесконечный Cover-QA). OCR escape без PIL mashup/Kie. Short hook **5–7** кириллических слов. |
| 4 | **Newbuild focus** | **ONLY новостройки Тюмень** (квартиры + дома от застройщика). Аудитория: семьи с детьми + инвесторы. Конверсия → TG/MAX/телефон за покупку новостройки. **DENY** вторичка как сюжет; слабый Wordstat → rework newbuild hook, не drop. Frozen secondary clusters — не retitle. Gate: `scripts/excalibur_blog_topic_focus.py` + `shared/newbuild-focus-lock.md`. |

Доки: `shared/quality-bar-9.md`, `shared/dzen-news-casus.md`, `shared/newbuild-focus-lock.md`, `memory/cover/cover-canon.json`, Writer/Sol/Cover skills, `CLOUD-AUTOMATION.md`.

## Первый запуск

Если `memory/setup/status.json` → `complete != true` **или**
`shared/tenant-config.json` → `setup_complete != true`:

→ работай как **`excalibur-blog-setup`** (skill `setup-excalibur-blog`).  
→ **Не** запускай Scout / Research / Publish.

См. `CLOUD-FIRST-RUN.md`, `SETUP.md`.

## Канон (после setup)

```text
Scout? → research_start → Research → Title → Writer(смысл)
→ Sol(слог) → Stylo(голос) → Description → Cover-text || Schema → Cover → Cover-QA
→ Indexer(llms) → Publish → Fixer → merge → Content-learner
```

**Writer** → `drafts/writer.html` (факты и смысл).  
**Sol** (`excalibur-blog-sol`) → финальный `article.html` слогом тенанта
(`shared/SOUL.md` + `shared/soul-examples/`).  
**Stylo** (`excalibur-blog-stylo`) → `excalibur_blog_stylo.py` vs `memory/stylo/gold`; при FAIL — **≤1** Sol с `stylo-notes.md` (только ритм, не факты). Gold-сюжеты **не** для Scout.  
После Stylo — stamp `pipeline_canon` + structural checks. Прозу после Sol
не переписывают (кроме одного stylo-driven Sol или возврата Sol при FAIL гейтов слога).

**Title** → `title-brief.json`. **Description** → `description-brief.json` (Дзен-карточка, после Sol).

**Цель каждого поста — вовлечение в Дзен** (лайки, комментарии, подписки): hot **news-casus актуалочка** (Тюмень, stakes, финал), прозаический лид → early TG+MAX → история → практика → **ending landing (agency, not panic)** → CTAs + **comment magnet** (один острый вопрос). Не чеклист, не TL;DR, не robotic insider bullets. Последние 1–2 абзаца — ручка до аванса, не «риски везде — никогда не покупать». См. `shared/dzen-news-casus.md`, `shared/quality-bar-9.md`.

**19 ролей** (см. `.cursor/agents/FOR-AGENTS.md`): 17 pipeline + `excalibur-blog-description` + `excalibur-blog-cover-qa` (включая **stylo**).

Никто не читает уже опубликованные статьи сайта — только
`published-titles-only.md` / `shared/published-titles.md` для anti-dup.

`memory/topics/` запрещена. Scout → handoff + `signal_urls` + **quad gate: Wordstat Tyumen (55+11176, compare RU 225) × Dzen news-casus** (`shared/dzen-news-casus.md`) × **newbuild only** (`shared/newbuild-focus-lock.md`, `topic_market_focus: newbuild_only`) × **30d story-cluster anti-repeat** (`shared/scout-story-clusters.json` + `memory/scout/used-clusters.json`; live blog ~20 + ledger перед lock; same cluster = FAIL даже при новом title). **Klyshin OPTIONAL** — только свежий @klyshin_A / YouTube **и только если hook = новостройка**; новый hot Tyumen newbuild casus без Klyshin предпочтителен при риске дубля. Wordstat = **evaluate + rework for demand** (не binary skip; слабый → newbuild jargon, **не** вторичка). В handoff: **final P0 phrase+volume** + **`dzen_casus_shape: PASS`** + **`comment_magnet_angle`** + **`story_dup_check: PASS`**. Cover canon: `memory/cover/cover-canon.json`.

**Factory brain (двухуровневый split):** Cursor — **тонкий дирижёр** (default Composer; не переключать модель Cursor).
Прозу пишет только `scripts/excalibur_blog_derouter_opus_chat.py` → Derouter REST (`DEROUTER_API_KEY`):
- **powerful** `gpt-6-astra` (`DEROUTER_POWERFUL_MODEL`): Writer, Sol (article prose only)
- **utility** `gpt-5.6-terra` (`DEROUTER_TERRA_MODEL`): Scout, Title, Research synthesis, Description, Cover-text, Schema, Cover-scene
При недоступности → `DEROUTER <ROLE> BLOCKER`, без тихого fallback на Composer. См. `shared/derouter-opus-brain-contract.md`.
**Cover PNG:** grsai grsai standard image model REST (`shared/grsai-gpt-image-api-contract.md`). Optional Derouter image fallback only. **Kie FORBIDDEN forever.** PIL mashup FORBIDDEN.
**Meme canon:** `memory/cover/meme-top100.json` + `cover-canon.json` → meme_canon_v1: real top memes, people+cats variety, on-topic funny stickers ≤15%, never on hook/face/phone, anti-repeat 14д.
**Cover budget (HARD):** `excalibur_blog_grsai_solo_cover.py` — max **2** full attempts (standard only; **VIP tier disabled**); override `EXCALIBUR_COVER_MAX_ATTEMPTS`. После исчерпания бюджета → `cover/cover-budget-result.json` + **Indexer** (не бесконечный Cover-QA loop). **≤15–20 мин** на cover; не копать `cover_qa_pixels.py` как дебаг-хобби.
**Short hook:** ONE line, **5–7** кириллических слов (B08-style), prefer слова ≥5 букв; em dash OK; novel-length hooks запрещены (`cover-text` gate).
**Cover-QA OCR escape:** если лицо + кириллический hook + телефон на PNG, а падают только OCR truncation / opaque-title flakes → `apply_ocr_false_positive_escape` (как B08/B09 live); без PIL mashup/Kie.
**Image alt/caption (HARD):** `scene_hint` / prompt / meme-manifest **никогда** не попадают в `alt`, figcaption, WP Media. Builder: `scripts/excalibur_blog_image_caption_builder.py --apply` (после Cover, до Indexer/Publish). Gate `image_alt_human` в quality-bar-9 — FAIL на hook|CTA|мемы|semicolon prompt list.
**Wordstat:** MCP-KV. **Cover-QA:** Python gates, не «глаз» агента.

```bash
python3 scripts/excalibur_blog_research_start.py --topic-id B111 --title "…"
```

## Ошибка

- Второй автор / rewrite-loop **поверх Sol** (Sol — единственный стилевой рерайт)
- Термин-дамп / research-брифинг в открытии финала
- TL;DR / «Быстрый инсайт» / bullet-dump в первом экране (канон: прозаический лид 4–6 предложений)
- Пост без **comment magnet** (острый вопрос для комментариев Дзена) или how-to checklist вместо news-casus
- **Ending landing FAIL:** pure dread без действия; takeaway «риски везде — как покупать»; «все риэлторы плохие» / «вторичка — мина»; sugar happy ending; чеклист N шагов как эмоциональный финал (практика в H2 — ок, последний beat = story+agency)
- topics / SEO-хвосты
- Writer/Sol читают старые article.html / live-сайт как образец
- Publish без pipeline_canon stamp
- Publish без `cover/cover_qa.json` PASS или без `description-brief.json`
- Publish **без рубрик WP** (`wp_category_slugs` / `topic_defaults`) при `wp_categories_required=true`
- Publish **без outbound interlink** (2–4 ссылки на опубликованные sibling) при `interlink_old_articles=true`
- Scout/тема без **Wordstat×news-casus×newbuild-only×30d anti-repeat**, без rework-лога или с выдуманными частотами
- Scout **повтор story-cluster** в 30д (новый title ≠ разрешение; см. `used-clusters.json`)
- Scout **drop hook** при слабом Wordstat без цикла rework (локализация Тюмень, **newbuild**-жаргон: новостройки, ДДУ, эскроу, семейная ипотека, переуступка, срок сдачи, отделка, КП…)
- Scout **вторичка как тема** при `topic_market_focus: newbuild_only` — **BLOCKER** (`NEWBUILD FOCUS BLOCKER`)
- Scout/тема про RF-blocked heroes без Дзен-канона (если `dzen_rf_pack`)
- Sol выдумывает факты, которых нет в `drafts/writer.html` / research
- **Spine once FAIL:** пересказ одной сцены в лиде + середине + «итоге»; recap («коротко если некогда»); повтор одних цифр/флагов трижды; lecture-хвост после финала casus
- **Composite disclaimer FAIL:** «случай собирательный», «без фамилий/адреса ЖК/названия банка», «механика в Тюмени повторяется», modeled/anonymized/«не репортаж» meta-text в теле; gate `no_composite_disclaimer`
- **Plain language FAIL:** академический/lawyer-blog тон, стопки юртерминов, «заумно»; термин без мгновенного перевода; снять heat casus чеклистом/lecture
- **Length FAIL:** > ~2400 слов или Дзен 14+ мин; раздутый текст «как раньше» 2600+
- Cursor пишет Scout/Title/Writer/Sol/Description/Cover-text/Schema prose своей моделью вместо `excalibur_blog_derouter_opus_chat.py`
- `alt` / caption / WP Media с production-токенами (hook, CTA, memes, scene_hint, semicolon prompt list)
- Запуск пайплайна до завершения Setup
- Cover regen >2 full attempts или >15–20 мин на cover / deep-dive pixel OCR source вместо Indexer
- **Inline placement FAIL:** обязательная схема «1 PNG под каждым H2»; <2 или >4 realistic inline; stock-man hero на inline
- Novel-length cover hook (>7 слов / многострочный) — ломает OCR

## Preflight

**До Scout (если dzen_rf_pack):** прочитать `shared/dzen-content-rules.md` +
`shared/rf-blocked-entities.json`.

```bash
python3 scripts/excalibur_blog_doctor.py
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_research_start.py --topic-id <id> --title "<short>"
```

Директор: `.cursor/agents/excalibur-blog-director.md` (не Task).  
Setup: `.cursor/agents/excalibur-blog-setup.md` (не Task).

## Publish (рубрики + перелинковка)

**Рубрики:** перед каждым publish в `article.meta.json` задай `wp_category_slugs`
или положись на `shared/wp-blog-categories.json` → `topic_defaults`. Скрипт publish
всегда вызывает `wp_set_post_categories`; без рубрики — **BLOCKER**
(`wp_categories_required=true`).

**Перелинковка:** при `interlink_old_articles=true` Writer/Sol добавляют 2–4
контекстные ссылки на sibling из `shared/published-articles.md` (`status=published`).
После publish — inbound «Читайте также» в 1–3 старых постах (авто из
`publish_options.auto_interlink_after_publish`). Контракт: `shared/interlink-contract.md`.
