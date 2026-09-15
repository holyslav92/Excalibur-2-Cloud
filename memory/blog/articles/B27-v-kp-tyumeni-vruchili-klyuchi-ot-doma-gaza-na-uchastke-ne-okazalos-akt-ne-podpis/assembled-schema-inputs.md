# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В КП Тюмени вручили ключи от дома без газа — семья не подписала акт",
  "h1": "В КП Тюмени вручили ключи от дома без газа — семья не подписала акт",
  "slug": "v-kp-tyumeni-vruchili-klyuchi-ot-doma-gaza-na-uchastke-ne-okazalos-akt-ne-podpis",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "description": "Ключи от дома в КП Тюмени вручили без газа — семья отказалась подписывать акт приёма",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В КП Тюмени вручили ключи от дома без газа — семья не подписала акт",
  "title": "В КП Тюмени вручили ключи от дома без газа — семья не подписала акт",
  "subject": "Дом в коттеджном посёлке Тюмени: ключи вручили без подключения газа, семья отказалась подписывать акт приёма."
}
```

## research-notes

research_date: 2026-09-15

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-kp-tyumeni-vruchili-klyuchi-ot-doma-gaza-na-uchastke-ne-okazalos-akt-ne-podpis/`
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

- headline: В КП Тюмени вручили ключи от дома без газа — семья не подписала акт
- description: Ключи от дома в КП Тюмени вручили без газа — семья отказалась подписывать акт приёма
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
