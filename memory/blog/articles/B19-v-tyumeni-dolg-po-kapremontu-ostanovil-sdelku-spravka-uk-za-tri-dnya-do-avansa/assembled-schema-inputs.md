# Schema inputs — B19

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку",
  "h1": "В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку",
  "slug": "v-tyumeni-dolg-po-kapremontu-ostanovil-sdelku-spravka-uk-za-tri-dnya-do-avansa",
  "topic_id": "B19",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-31",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B19",
  "h1": "В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку",
  "title": "В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-dolg-po-kapremontu-ostanovil-sdelku-spravka-uk-za-tri-dnya-do-avansa/`
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

- headline: В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку
- description: В Тюмени чистая ЕГРН не спасла вторичку: долг остановил сделку
- datePublished: 2026-08-31
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
