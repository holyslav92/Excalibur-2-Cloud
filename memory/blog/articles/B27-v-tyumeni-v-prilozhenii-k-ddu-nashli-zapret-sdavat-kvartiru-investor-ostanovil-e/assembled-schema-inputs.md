# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч",
  "h1": "В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч",
  "slug": "v-tyumeni-v-prilozhenii-k-ddu-nashli-zapret-sdavat-kvartiru-investor-ostanovil-e",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-17",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч",
  "title": "В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч",
  "subject": "Приложение к ДДУ в новостройке с запретом сдавать квартиру"
}
```

## description-brief.json

Менеджер уверял: студию в Тюмени можно сдавать. Но одна строчка в приложении к ДДУ перечеркнула расчёт доходности — инвестору пришлось выбирать между сгоревшей бронью и доплатой 240 тысяч.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-prilozhenii-k-ddu-nashli-zapret-sdavat-kvartiru-investor-ostanovil-e/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени приложение к ДДУ запретило аренду — инвестор отказался от доплаты 240 тысяч
- description: Менеджер уверял: студию в Тюмени можно сдавать. Но одна строчка в приложении к ДДУ перечеркнула расчёт доходности — инвестору пришлось выбирать между сгоревшей бронью и доплатой 240 тысяч.
- datePublished: 2026-09-17
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
