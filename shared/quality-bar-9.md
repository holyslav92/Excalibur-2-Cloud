# Quality bar 9/10 — hard gate before Publish

Порог **9/10** для longform The Риэлтор. Статья **не публикуется**, пока не PASS все пункты ниже **и** `quality-bar-9.json` в каталоге статьи не содержит `"all_pass": true`.

Контракт для Writer, Sol, Description, Cover-QA и Cloud Automation. Cursor — дирижёр; прозу пишет Derouter по `shared/derouter-opus-brain-contract.md`.

## BRAND (видно в теле, не только в футере темы)

- **Первое лицо:** Святослав Шакин, The Риэлтор, Тюмень. Лично ведёт сделку от звонка до регистрации.
- **Телефон в `article.html`:** `+7 922 001 65 05`, кликабельный `tel:+79220016505`. Тот же номер на **cover**.
- **Соцсети** — компактный блок в конце (и один раз после главного чеклиста допустимо, без спама в каждом H2):
  - Telegram канал https://t.me/Tyumen_Rieltor
  - Telegram личка https://t.me/holyslav92
  - WhatsApp https://wa.me/79220016505
  - VK https://vk.ru/tymenrieltor
  - Дзен https://dzen.ru/holyslav
  - MAX: тот же номер +7 922 001 65 05
  - сайт / (главная tymenrieltor.ru)
- **Dual CTA (мягко, после пользы):** «напишите на консультацию» **или** «сразу к делу / я подключаюсь в сделку». Без «лучший риэлтор», без гарантии нулевого риска.

## TEXT

- **2000–2600 слов** (не 2900+). Короткие абзацы. Klyshin rhythm, Shakin facts. Тюмень — конкретика.
- **Без выдуманных адресов/лотов/цен.** Таблица «живых лотов» только из research-notes с источником; иначе удалить или явно пометить **как пример**, не live inventory.
- **Сравнительные таблицы:** левый столбец **отличается** от правого (запрещён copy-paste «ошибки» = «правильно»).
- **7+ полезных H2**, каждый с inline `figure.inline-quad` где по канону.

## COVER

- Identity `face-studio-2026-06-23`, **новая эмоция**, medium-slim, **телефон на cover**.
- Wordstat-стикеры **1–3**, **не перекрывают** главный заголовок на обложке.
- Мемы TOP-100 — **маленькие**, не hero.

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
