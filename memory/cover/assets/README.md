# Cover assets — The Риэлтор

Локальные референсы для `cover_mode=host_reference`. Чужие CDN/catbox не использовать.

## Hero identity lock (PRIMARY)

Два эталона от владельца + запасной likeness:

| Файл | Роль |
|------|------|
| `hero-ref-office-risk-hologram.jpg` | Лицо + mood «риск всплывёт позже» (офис, документы, нотариус). **Не копировать композицию на каждый пост.** |
| `hero-ref-balcony-keys-sunset.jpg` | Лицо + mood success/ключи (балкон, закат). **Не копировать композицию на каждый пост.** |
| `portrait.jpg` | Запасной full-body likeness (navy blazer, тёмная стена). |
| `portrait-landing.jpg` | Поясной, сумерки, берёзы. |
| `portrait-640.webp` | Webp-вариант. |

Публичный URL для i2i (тема сайта):

`{{SITE_BASE}}/wp-content/themes/tymenrieltor-light/assets/images/portrait.jpg`

## Emotion bank (Cover выбирает одну на статью)

- спокойная уверенность
- настороженность
- жёсткий стоп
- лёгкая ирония
- сосредоточенный разбор документов
- тёплое «ключ получен»

Правило: **новая эмоция + новая поза + новый фон** каждый раз. Лицо узнаваемое, сцена не штамп.

## Longform visuals

8 изображений на статью: `cover.png` 1200×675 + `inline-01…07.png` (7× `figure.inline-quad`).
2 quad-canvas × 2K (mcp-derouter) → split 2×2.

## Марка / mood (`style-refs/`)

См. `style-refs/README` в каталоге. Inbox: `memory/setup/visual-inbox/` (копии hero-ref + logo).

## Запреты

Чужое лицо, pink-cat, белое худи, EXCALIBUR stamp, beige gradient, клон композиции эталонных hero-ref.
