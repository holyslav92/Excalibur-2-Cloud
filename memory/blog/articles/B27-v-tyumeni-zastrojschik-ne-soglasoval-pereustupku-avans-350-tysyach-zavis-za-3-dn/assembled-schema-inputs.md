# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня",
  "h1": "В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня",
  "slug": "v-tyumeni-zastrojschik-ne-soglasoval-pereustupku-avans-350-tysyach-zavis-za-3-dn",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "description": "В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня",
  "title": "В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня",
  "subject": "Переуступка прав по ДДУ в новостройке"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-ne-soglasoval-pereustupku-avans-350-tysyach-zavis-za-3-dn/`
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

- headline: В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня
- description: В Тюмени сорвалась переуступка — аванс 350 тысяч завис за 3 дня
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
