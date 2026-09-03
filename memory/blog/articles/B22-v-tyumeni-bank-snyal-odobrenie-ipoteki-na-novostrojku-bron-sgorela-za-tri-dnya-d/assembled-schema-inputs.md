# Schema inputs — B22

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела",
  "h1": "В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела",
  "slug": "v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela-za-tri-dnya-d",
  "topic_id": "B22",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-03",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B22",
  "h1": "В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела",
  "title": "В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела",
  "subject": "Предварительное одобрение ипотеки на новостройку, бронь и ДДУ"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela-za-tri-dnya-d/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/[REDACTED], vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела
- description: В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела
- datePublished: 2026-09-03
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
