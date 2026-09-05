# Quality bar 9/10 — hard gate before Publish

## OWNER LOCK (permanent)

Три столпа — **не ослаблять** без owner override. Полный JSON: `shared/pipeline-canon.json` → `owner_lock_permanent`.

| Столп | HARD rules |
|-------|------------|
| **Engagement bomb** | Dzen engagement goal; news-casus актуалочка; прозаический лид **4–6 предложений**; early TG+MAX only; comment magnet; **ending landing = agency, not panic** (heat сохраняем, меняем посадку); gates `no_tldr_opening`, `opening-meta-gate`, `comment_magnet_question`. **Forbidden:** TL;DR, «Быстрый инсайт», bullets до первого H2, checklist/how-to в лиде; sugar-happy ending; checklist как эмоциональный финал; «риски везде — как покупать». |
| **Meme canon v1** | `meme-top100.json` real ids only; people+cats (not cats-only); on-topic funny; ≤15% stickers; never hook/face/phone; anti-repeat 14д; `meme_variety_not_cats_only` when `meme_picks` present. |
| **Cover fail-fast** | Max **2** full cover attempts; ≤15–20 min timebox; `cover-budget-result.json` → Indexer; Fixer max 2 rounds; short hook 5–7 words; OCR escape without PIL/Kie. |

Порог **9/10** для longform The Риэлтор. Статья **не публикуется**, пока не PASS все пункты ниже **и** `quality-bar-9.json` в каталоге статьи не содержит `"all_pass": true`.

Контракт для Writer, Sol, Scout, Title, Description, Cover-QA и Cloud Automation. Cursor — дирижёр; прозу пишет Derouter по `shared/derouter-opus-brain-contract.md`.

**Главная задача каждого поста — вовлечение в Дзен:** лайки, комментарии, подписки.
Форма = **hot news-casus актуалочка** (Тюмень, конкретные stakes, финал): прозаический лид в слоге Святослава → early TG+MAX → история → практика → CTAs. **Не** чеклист, **не** TL;DR, **не** robotic insider bullets.

**Conversion (параллельная цель):** увести читателя в **Telegram** или **MAX** до ухода. Не оставлять единственный CTA в футере.

Канонические URL — `shared/tenant-config.json` → `cta_channels` / `cta_links` (PUBLIC_SITE_URL = tymenrieltor.ru):
- Telegram (PRIMARY): https://t.me/Tyumen_Rieltor
- MAX (PRIMARY): https://max.ru/id561413315447_biz
- Сайт / guides / about: `{{SITE_BASE}}`, `{{SITE_BASE}}/gajdy/`, `{{SITE_BASE}}/rieltor-tyumen/`
- Дзен: https://dzen.ru/holyslav
- VK: https://vk.ru/tymenrieltor
- Телефон: `+7 922 001 65 05` / `tel:+79220016505` — на cover + **один раз** в теле

## CONVERSION (три зоны CTA)

### 1. Early — первый экран (после hook + прозаический лид)

**Открытие:** после заголовка/hook — **4–6 предложений прозы** (news-casus, часть истории). **Не** TL;DR, **не** «Быстрый инсайт», **не** bullet-dump в первом экране. Gate: `opening-meta-gate` + `no_tldr_opening` в quality-bar-9.

Короткий brand beat: **Святослав Шакин, The Риэлтор, Тюмень** + одна строка curiosity, которую статья ещё не закрыла («полный разбор кейсов и как я это ловлю до аванса — в Telegram и MAX»).

**Только две кнопки/ссылки:** Telegram + MAX. Без дампа шести сетей в лиде. Без пустого «подпишись».

Класс разметки: `excalibur-cta-early`.

### 2. Mid — после главного чеклиста

Лёгкий nudge: TG + MAX, без полного списка каналов. Tease метода в статье, stream кейсов — в мессенджерах.

Класс: `excalibur-cta-mid`.

### 3. End — финал + landing (agency, not panic)

**Owner lock 2026-08-28:** casus остаётся **горячим** (stakes, финал, потери где есть). Меняется **посадка** — последние 1–2 абзаца **до** end CTA: читатель уходит с **ручкой**, не с паникой.

**Default landing (большинство постов):**
- Остановились **до аванса** / проверка **спасла сделку** / вторичку покупают каждый день, **если смотреть до денег**.
- Воздух + agency: «подключусь до аванса», «разберём до внесения», «напишите — разложу по шагам». **Не** «бегите» / «вторичка — мина» / «все риэлторы плохие».
- End CTA (dual + полный набор) — тот же набор каналов, **мягче тон**: консультация / «сразу в сделку до аванса».

**Exception (редко):** жёсткая потеря допустима, только если **вилка очевидна**: «если бы сделали X до аванса — не потеряли». Никогда не заканчивать чистым dread без действия.

**Ban (эмоциональный финал):**
- Sugar happy ending, убивающий casus.
- Чеклист из 6 шагов как **последний удар** (практика в H2 — ок; **последний beat** = story + agency).
- Takeaway «риски везде, как вообще покупать».

Dual CTA (мягко): «напишите на консультацию» **или** «сразу к делу / подключусь в сделку». Плюс **полный набор:** TG, MAX, сайт, Дзен, VK, гайды. Дзен + TG — как «смотреть разборы», не корпоративная выдумка. About/contact — только реальные URL из repo (`/rieltor-tyumen/`, `/kontakty/`).

Класс: `excalibur-cta-end`.

## BRAND (видно в теле, не только в футере)

- **Первое лицо:** Святослав Шакин, The Риэлтор, Тюмень. Лично ведёт сделку от звонка до регистрации.
- **Телефон в `article.html`:** `+7 922 001 65 05`, кликабельный `tel:+79220016505`. Тот же номер на **cover**.

## INTERLINK (HARD при `interlink_old_articles=true`)

**2–4** контекстные ссылки на опубликованные sibling из `shared/published-articles.md` (`status=published`). Якорь по смыслу H2: доверенность ↔ расписка / ЕГРН / аванс / задаток. Только реальные path из ledger — без выдуманных URL.

## TEXT

- **~1400–1600 слов** (≈8–10 мин чтения в Дзене). **Hard FAIL** если **> ~1750** слов или Дзен покажет **>10 мин**. Короткие абзацы. Klyshin rhythm, Shakin facts. Тюмень — конкретика.
- **Spine once (one-breath):** один проход casus — **не** пересказывать ту же сцену в лиде, середине и «итоге». Структура: прозаический лид (4–6 предложений) → история со stakes → **практика один раз** → agency ending. Gate: `spine_once_no_recap`.
- **Вырезать:** recap-абзацы («коротко если некогда», «в двух словах», «итого»), повтор одних и тех же цифр/флагов трижды, lecture-хвосты после финала casus.
- **Comment magnet (HARD):** один острый вопрос, с которым читатели спорят в комментариях Дзена — реплика «…?» или прямой вопрос с двумя полюсами; после финала casus или перед mid CTA. Gate: `comment_magnet_question`.
- **No composite disclaimer (HARD):** casus = конкретный день в комнате; **ban** «случай собирательный», «без фамилий/адреса ЖК/названия банка», «механика в Тюмени повторяется», modeled/anonymized/«не репортаж» meta-text. Gate: `no_composite_disclaimer`.
- **Без выдуманных адресов/лотов/цен.** Таблица «живых лотов» только из research-notes с источником; иначе удалить или явно пометить **как пример**, не live inventory.
- **Сравнительные таблицы:** левый столбец **отличается** от правого (запрещён copy-paste «ошибки» = «правильно»).
- **5–8 полезных H2** (не раздувать ради картинок). Inline **не обязан** стоять под каждым H2: допустимы **0, 1 или пара** (реалистичный кадр + схема) на бит. Всего в статье **7** `figure.inline-quad`; gate `inline_figures_7` + `inline_placement_flexible` + `inline_realistic_mix_2_4` (manifest).

## COVER

- Identity `face-studio-2026-06-23` — **FACE i2i only** (кости, hairline, eyes, stubble, 28yo, medium-slim). **Не** копировать одежду/позу/студийный bust референса.
- **Variety lock (HARD):** каждый cover **INVENTS** outfit, location, action, emotion, pose/framing. Не default «black blazer + left talking-head bust + side-eye»; FAIL если последние 2–3 обложки повторяют эту связку.
- **Телефон на cover:** `+7 922 001 65 05`.
- Wordstat-стикеры **1–3**, **не перекрывают** главный заголовок (positions x≥0.68; PIL overlay если модель накрыла title).
- Мемы TOP-100 — **маленькие**, не hero; host = единственный крупный человек.
- Cover-QA checks: `title_not_occluded`, `outfit_invented`, `action_invented`, `emotion_not_copied_from_recent_covers`.
- **Alt/caption (HARD):** одна короткая русская SEO-фраза **80–140 символов** — смысл кейса (cover) или раздела (inline). **Подпись featured (WP caption) = пустая** — Dzen показывает caption как текст в ленте. **Запрещено навсегда:** hook, CTA, memes, scene_hint, scene-painting («рядом лежит», «у стойки», дубль имени хоста, склейка с hook), sticky, prompt, i2i, quad, inline_N, «мемы» как тег, списки через `;`. Builder: `scripts/excalibur_blog_image_caption_builder.py`. Gate: `image_alt_human`.

## INLINES

- **Микс (owner lock 2026-08-29):** **2–4** реалистичных кадра (квартира, подъезд, МФЦ, документ, улица Тюмени — high-key, полезный, **без лица хоста**) + остальное — **информационная** инфографика (таблицы/схемы с цифрами). Не «7 одинаковых схем подряд».
- **Размещение:** не 1:1 под каждым H2. Допустима **пара подряд** (фото + диаграмма) на одном бите; другие H2 — без картинки.
- **Без** другого человека как co-host / stock-man hero (кроме cover = только Святослав). Мемы маленькие, 2–3 из 7.
- **Utility test:** диаграмма учит факт/порядок/цифру; фото — узнаваемый контекст кейса. FAIL: идентичные двухколоночные таблицы, пустые ячейки, decorative icon row.
- **Alt:** человеческий SEO-русский — что на кадре / что показывает схема; не scene_hint и не prompt.

## Article quality score (после Stylo)

Структурный гейт Grok Bot 7.5–9 bar — **до** Description/Cover:

```bash
python3 scripts/excalibur_blog_quality_score_gate.py --article-dir memory/blog/articles/<topic>-<slug>
# один repair Sol при FAIL:
python3 scripts/excalibur_blog_quality_score_gate.py --article-dir <dir> --repair
```

Контракт: `shared/article-quality-score-lock.md` → `article-quality-score.json` (`all_pass: true`).

## Self-score gate

После Sol + Cover-QA дирижёр запускает:

```bash
python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir memory/blog/articles/<topic>-<slug>
```

Скрипт пишет `quality-bar-9.json`. **Publish** только при `"status": "PASS"` и `"all_pass": true`.

## Связанные гейты

- `scripts/excalibur_blog_cover_qa_gate.py` — визуал (включая phone, stickers, inline utility)
- `scripts/excalibur_blog_image_caption_builder.py` — human alt/caption (не prompt-leak)
- `scripts/excalibur_blog_community_cta_gate.py` — обязательные CTA из tenant-config
- `scripts/excalibur_blog_structure_gate.py` — вызывает quality-bar-9 перед Publish
