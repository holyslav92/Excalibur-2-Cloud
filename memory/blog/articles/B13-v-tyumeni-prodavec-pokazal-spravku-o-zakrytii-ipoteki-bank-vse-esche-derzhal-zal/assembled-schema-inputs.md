# Schema inputs — B13

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени",
  "h1": "Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени",
  "slug": "v-tyumeni-prodavec-pokazal-spravku-o-zakrytii-ipoteki-bank-vse-esche-derzhal-zal",
  "topic_id": "B13",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-30",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B13",
  "h1": "Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени",
  "title": "Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-prodavec-pokazal-spravku-o-zakrytii-ipoteki-bank-vse-esche-derzhal-zal/`
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

- headline: Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени
- description: Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени
- datePublished: 2026-08-30
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
