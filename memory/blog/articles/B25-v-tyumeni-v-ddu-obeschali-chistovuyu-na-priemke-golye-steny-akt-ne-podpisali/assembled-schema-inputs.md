# Schema inputs — B25

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали",
  "h1": "В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали",
  "slug": "v-tyumeni-v-ddu-obeschali-chistovuyu-na-priemke-golye-steny-akt-ne-podpisali",
  "topic_id": "B25",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-13",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B25",
  "h1": "В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали",
  "title": "В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали",
  "subject": "Чистовая отделка в ДДУ и приёмка квартиры в новостройке"
}
```

## description-brief.json

«Доделаем потом», — услышала семья на приёмке в Тюмени. Но в приложении к ДДУ были пол, двери и сантехника, а перед ними — white box. Подписывать акт или фиксировать расхождения?

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-obeschali-chistovuyu-na-priemke-golye-steny-akt-ne-podpisali/`
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

- headline: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали
- description: «Доделаем потом», — услышала семья на приёмке в Тюмени. Но в приложении к ДДУ были пол, двери и сантехника, а перед ними — white box. Подписывать акт или фиксировать расхождения?
- datePublished: 2026-09-13
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
