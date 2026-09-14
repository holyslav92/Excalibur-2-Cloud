# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась",
  "h1": "Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась",
  "slug": "v-tyumeni-matkapital-na-novostrojku-zavis-nakanune-eskrou-rebenku-ispolnilos-7-l",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-14",
  "description": "Ребёнку исполнилось 7 лет между одобрением и кредитным договором — семейная ипотека под 6% сорвалась, бронь сняли",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась",
  "title": "Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась",
  "subject": "Семейная ипотека на новостройку: ребёнку исполнилось 7 лет до заключения кредитного договора.",
  "slug": "v-tyumeni-matkapital-na-novostrojku-zavis-nakanune-eskrou-rebenku-ispolnilos-7-l"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Ребёнку исполнилось 7 лет между одобрением и кредитным договором — семейная ипотека под 6% сорвалась, бронь сняли».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-matkapital-na-novostrojku-zavis-nakanune-eskrou-rebenku-ispolnilos-7-l/`
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

- headline: Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась
- description: Ребёнку исполнилось 7 лет между одобрением и кредитным договором — семейная ипотека под 6% сорвалась, бронь сняли
- datePublished: 2026-09-14
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
