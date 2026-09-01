# Schema inputs — B19

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ипотеку одобрили — эскроу сорвал маткапитал",
  "h1": "В Тюмени ипотеку одобрили — эскроу сорвал маткапитал",
  "slug": "semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli",
  "topic_id": "B19",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-01",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B19",
  "h1": "В Тюмени ипотеку одобрили — эскроу сорвал маткапитал",
  "title": "В Тюмени ипотеку одобрили — эскроу сорвал маткапитал",
  "subject": "семейная ипотека на новостройку в Тюмени: банк не открыл эскроу из-за обязательств по прошлому маткапиталу"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli/`
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

- headline: В Тюмени ипотеку одобрили — эскроу сорвал маткапитал
- description: В Тюмени ипотеку одобрили — эскроу сорвал маткапитал
- datePublished: 2026-09-01
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
