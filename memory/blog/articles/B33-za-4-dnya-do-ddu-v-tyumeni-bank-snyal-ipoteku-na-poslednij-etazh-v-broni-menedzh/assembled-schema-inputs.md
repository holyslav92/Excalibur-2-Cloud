# Schema inputs — B33

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В новостройке Тюмени обещали «любой этаж» — банк снял ипотеку с последнего за 4 дня до ДДУ",
  "h1": "В новостройке Тюмени обещали «любой этаж» — банк снял ипотеку с последнего за 4 дня до ДДУ",
  "slug": "za-4-dnya-do-ddu-v-tyumeni-bank-snyal-ipoteku-na-poslednij-etazh-v-broni-menedzh",
  "topic_id": "B33",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-24",
  "description": "За четыре дня до ДДУ банк снял ипотеку с квартиры на последнем этаже в новостройке Тюмени: в брони писали «любой этаж», но одобрение заёмщика не равно одобрению конкретного лота.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B33",
  "h1": "В новостройке Тюмени обещали «любой этаж» — банк снял ипотеку с последнего за 4 дня до ДДУ",
  "title": "В новостройке Тюмени обещали «любой этаж» — банк снял ипотеку с последнего за 4 дня до ДДУ",
  "subject": "ипотека на квартиру на последнем этаже в тюменской новостройке"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/za-4-dnya-do-ddu-v-tyumeni-bank-snyal-ipoteku-na-poslednij-etazh-v-broni-menedzh/`
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

- headline: В новостройке Тюмени обещали «любой этаж» — банк снял ипотеку с последнего за 4 дня до ДДУ
- description: За четыре дня до ДДУ банк снял ипотеку с квартиры на последнем этаже в новостройке Тюмени: в брони писали «любой этаж», но одобрение заёмщика не равно одобрению конкретного лота.
- datePublished: 2026-09-24
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
