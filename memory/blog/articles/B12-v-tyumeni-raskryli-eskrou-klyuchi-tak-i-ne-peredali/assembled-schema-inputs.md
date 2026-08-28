# Schema inputs — B12

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Новостройку в Тюмени оплатили — ключи задержали на три месяца",
  "h1": "Новостройку в Тюмени оплатили — ключи задержали на три месяца",
  "slug": "v-tyumeni-raskryli-eskrou-klyuchi-tak-i-ne-peredali",
  "topic_id": "B12",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-28",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B12",
  "h1": "Новостройку в Тюмени оплатили — ключи задержали на три месяца",
  "title": "Новостройку в Тюмени оплатили — ключи задержали на три месяца"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Новостройку в Тюмени оплатили — ключи задержали на три месяца».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-raskryli-eskrou-klyuchi-tak-i-ne-peredali/`
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

- headline: Новостройку в Тюмени оплатили — ключи задержали на три месяца
- description: Новостройку в Тюмени оплатили — ключи задержали на три месяца
- datePublished: 2026-08-28
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
