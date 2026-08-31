# Schema inputs — B16

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени семья остановила бронь — третий транш раскрыл платёж",
  "h1": "В Тюмени семья остановила бронь — третий транш раскрыл платёж",
  "slug": "transhevaya-ipoteka-novostrojka-tyumen",
  "topic_id": "B16",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-31",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B16",
  "h1": "В Тюмени семья остановила бронь — третий транш раскрыл платёж",
  "title": "В Тюмени семья остановила бронь — третий транш раскрыл платёж",
  "subject": "Траншевая ипотека на новостройке в Тюмени",
  "angle": "Семья почти забронировала новостройку из-за рекламного платежа «как аренда», но остановилась, увидев полный график и рост платежа после третьего транша."
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени семья остановила бронь — третий транш раскрыл платёж».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/transhevaya-ipoteka-novostrojka-tyumen/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/holyslav92, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени семья остановила бронь — третий транш раскрыл платёж
- description: В Тюмени семья остановила бронь — третий транш раскрыл платёж
- datePublished: 2026-08-31
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
