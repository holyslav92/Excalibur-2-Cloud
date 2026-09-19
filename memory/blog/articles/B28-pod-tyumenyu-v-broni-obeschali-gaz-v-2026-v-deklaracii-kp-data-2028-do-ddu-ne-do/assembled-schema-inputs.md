# Schema inputs — B28

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч",
  "h1": "Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч",
  "slug": "pod-tyumenyu-v-broni-obeschali-gaz-v-2026-v-deklaracii-kp-data-2028-do-ddu-ne-do",
  "topic_id": "B28",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "description": "Газ в коттеджном посёлке и проектная декларация"
}
```

## title-brief.json

```json
{
  "topic_id": "B28",
  "h1": "Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч",
  "title": "Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч",
  "subject": "Газ в коттеджном посёлке и проектная декларация"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/pod-tyumenyu-v-broni-obeschali-gaz-v-2026-v-deklaracii-kp-data-2028-do-ddu-ne-do/`
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

- headline: Газ в КП обещали — декларация указала 2028, семья потеряла 60 тысяч
- description: Газ в коттеджном посёлке и проектная декларация
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет h3 FAQ-пар).

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
