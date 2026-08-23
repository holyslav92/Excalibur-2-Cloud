# Quality bar 9/10 — hard gate before Publish

Порог **9/10** для longform The Риэлтор. Статья **не публикуется**, пока не PASS все пункты ниже **и** `quality-bar-9.json` в каталоге статьи не содержит `"all_pass": true`.

Контракт для Writer, Sol, Description, Cover-QA и Cloud Automation. Cursor — дирижёр; прозу пишет Derouter по `shared/derouter-opus-brain-contract.md`.

**Главная задача статьи — conversion:** увести читателя в **Telegram** или **MAX** до того, как он уйдёт. Не оставлять единственный CTA в футере.

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

### 3. End — финал

Dual CTA (мягко): «напишите на консультацию» **или** «сразу к делу / подключусь в сделку». Плюс **полный набор:** TG, MAX, сайт, Дзен, VK, гайды. Дзен + TG — как «смотреть разборы», не корпоративная выдумка. About/contact — только реальные URL из repo (`/rieltor-tyumen/`, `/kontakty/`).

Класс: `excalibur-cta-end`.

## BRAND (видно в теле, не только в футере)

- **Первое лицо:** Святослав Шакин, The Риэлтор, Тюмень. Лично ведёт сделку от звонка до регистрации.
- **Телефон в `article.html`:** `+7 922 001 65 05`, кликабельный `tel:+79220016505`. Тот же номер на **cover**.

## INTERLINK (HARD при `interlink_old_articles=true`)

**2–4** контекстные ссылки на опубликованные sibling из `shared/published-articles.md` (`status=published`). Якорь по смыслу H2: доверенность ↔ расписка / ЕГРН / аванс / задаток. Только реальные path из ledger — без выдуманных URL.

## TEXT

- **2000–2600 слов** (не 2900+). Короткие абзацы. Klyshin rhythm, Shakin facts. Тюмень — конкретика.
- **Без выдуманных адресов/лотов/цен.** Таблица «живых лотов» только из research-notes с источником; иначе удалить или явно пометить **как пример**, не live inventory.
- **Сравнительные таблицы:** левый столбец **отличается** от правого (запрещён copy-paste «ошибки» = «правильно»).
- **7+ полезных H2**, каждый с inline `figure.inline-quad` где по канону.

## COVER

- Identity `face-studio-2026-06-23` — **FACE i2i only** (кости, hairline, eyes, stubble, 28yo, medium-slim). **Не** копировать одежду/позу/студийный bust референса.
- **Variety lock (HARD):** каждый cover **INVENTS** outfit, location, action, emotion, pose/framing. Не default «black blazer + left talking-head bust + side-eye»; FAIL если последние 2–3 обложки повторяют эту связку.
- **Телефон на cover:** `+7 922 001 65 05`.
- Wordstat-стикеры **1–3**, **не перекрывают** главный заголовок (positions x≥0.68; PIL overlay если модель накрыла title).
- Мемы TOP-100 — **маленькие**, не hero; host = единственный крупный человек.
- Cover-QA checks: `title_not_occluded`, `outfit_invented`, `action_invented`, `emotion_not_copied_from_recent_covers`.

## INLINES

- Только инфографика. **Без** другого человека как co-host. Мемы маленькие, 2–3 из 7.
- **Utility test:** картинка одна учит факт/порядок/цифру. FAIL: идентичные двухколоночные таблицы, пустые ячейки.

## Self-score gate

После Sol + Cover-QA дирижёр запускает:

```bash
python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir memory/blog/articles/<topic>-<slug>
```

Скрипт пишет `quality-bar-9.json`. **Publish** только при `"status": "PASS"` и `"all_pass": true`.

## Связанные гейты

- `scripts/excalibur_blog_cover_qa_gate.py` — визуал (включая phone, stickers, inline utility)
- `scripts/excalibur_blog_community_cta_gate.py` — обязательные CTA из tenant-config
- `scripts/excalibur_blog_structure_gate.py` — вызывает quality-bar-9 перед Publish
