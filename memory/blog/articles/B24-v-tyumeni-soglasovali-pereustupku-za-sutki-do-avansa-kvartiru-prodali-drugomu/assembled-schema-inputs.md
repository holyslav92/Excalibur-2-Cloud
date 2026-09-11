# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса",
  "h1": "В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса",
  "slug": "v-tyumeni-soglasovali-pereustupku-za-sutki-do-avansa-kvartiru-prodali-drugomu",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-11",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса",
  "title": "В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса",
  "subject": "переуступка квартиры в строящейся новостройке Тюмени"
}
```

## description

В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-soglasovali-pereustupku-za-sutki-do-avansa-kvartiru-prodali-drugomu/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса
- description: В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса
- datePublished: 2026-09-11
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
