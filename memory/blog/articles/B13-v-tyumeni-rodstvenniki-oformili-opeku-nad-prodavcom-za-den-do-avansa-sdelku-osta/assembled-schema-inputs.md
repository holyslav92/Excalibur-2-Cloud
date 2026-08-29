# Schema inputs — B13

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд",
  "h1": "Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд",
  "slug": "v-tyumeni-rodstvenniki-oformili-opeku-nad-prodavcom-za-den-do-avansa-sdelku-osta",
  "topic_id": "B13",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-29",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B13",
  "h1": "Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд",
  "title": "Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-rodstvenniki-oformili-opeku-nad-prodavcom-za-den-do-avansa-sdelku-osta/`
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

- headline: Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд
- description: Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд
- datePublished: 2026-08-29
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
