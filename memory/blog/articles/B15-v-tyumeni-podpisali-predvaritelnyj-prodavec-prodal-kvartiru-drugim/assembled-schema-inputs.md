# Schema inputs — B15

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени подписали предварительный договор — квартиру продали другим",
  "h1": "В Тюмени подписали предварительный договор — квартиру продали другим",
  "slug": "v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim",
  "topic_id": "B15",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-29",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B15",
  "h1": "В Тюмени подписали предварительный договор — квартиру продали другим",
  "title": "В Тюмени подписали предварительный договор — квартиру продали другим"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени подписали предварительный договор — квартиру продали другим».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim/`
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

- headline: В Тюмени подписали предварительный договор — квартиру продали другим
- description: В Тюмени подписали предварительный договор — квартиру продали другим
- datePublished: 2026-08-29
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
