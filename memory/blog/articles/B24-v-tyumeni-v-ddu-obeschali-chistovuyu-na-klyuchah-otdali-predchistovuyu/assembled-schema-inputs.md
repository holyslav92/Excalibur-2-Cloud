# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (from title-brief + research-context)

```json
{
  "title": "В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую",
  "h1": "В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую",
  "slug": "v-tyumeni-v-ddu-obeschali-chistovuyu-na-klyuchah-otdali-predchistovuyu",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую",
  "title": "В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую",
  "subject": "Новостройка в Тюмени: вместо четырёх позиций чистовой отделки по ДДУ семье передали квартиру с предчистовой отделкой."
}
```

## description-brief.json

```json
{
  "topic_id": "B24",
  "description": "В приложении к ДДУ — обои, двери и сантехника. На приёмке в Тюмени семья увидела whitebox и выбор: подписать акт или доплатить за уже купленное."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-obeschali-chistovuyu-na-klyuchah-otdali-predchistovuyu/`
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

- headline: В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую
- description: В приложении к ДДУ — обои, двери и сантехника. На приёмке в Тюмени семья увидела whitebox и выбор: подписать акт или доплатить за уже купленное.
- datePublished: 2026-09-10
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
