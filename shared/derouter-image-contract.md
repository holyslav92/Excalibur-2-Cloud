# Derouter MCP — генерация картинок (без Kie)

Тенант The Риэлтор: **Kie API не использовать.** Ключ Kie не нужен.

## Канон

Две генерации **2K** (каждая холст `2048×1152`, сетка 2×2, панели 16:9):

| Job | Файл | Панели |
|-----|------|--------|
| 1 | `cover/canvas-quad-01.png` | cover, inline_1, inline_2, inline_3 |
| 2 | `cover/canvas-quad-02.png` | inline_4, inline_5, inline_6, inline_7 |

После split: `cover.png` + `inline-01.png` … `inline-07.png`.  
**Первая панель первого кадра — обложка.** Остальные семь — в статью после H2.

`jobs.length === 2`. Resolution каждой: `2K`.

## Кто вызывает

Cover-агент вызывает **MCP server `DEROOTER`** (image-to-image / generate по схеме сервера).  
Промпты и `input_urls` — из `cover/quad-mcp-batch.json`.

Запись результата:

```bash
python3 scripts/excalibur_blog_derouter_image.py \
  --article-dir memory/blog/articles/<id>-<slug> \
  --url-1 <result_url_canvas_1> \
  --url-2 <result_url_canvas_2>
```

Скрипт пишет `cover/quad-mcp-result.json` (`urls` длина 2) и вызывает apply+split.

## Запреты

- `excalibur_blog_kie_gpt_image2_api.py` и `KIE_API_KEY` для этого тенанта
- 8 отдельных генераций «по панели»
- quality-redo без явного запроса человека
