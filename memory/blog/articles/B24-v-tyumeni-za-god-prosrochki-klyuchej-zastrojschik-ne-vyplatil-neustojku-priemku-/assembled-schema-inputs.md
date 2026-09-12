# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени застройщик год не платил неустойку — семья остановила приёмку",
  "h1": "В Тюмени застройщик год не платил неустойку — семья остановила приёмку",
  "slug": "v-tyumeni-za-god-prosrochki-klyuchej-zastrojschik-ne-vyplatil-neustojku-priemku-",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-09",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени застройщик год не платил неустойку — семья остановила приёмку",
  "title": "В Тюмени застройщик год не платил неустойку — семья остановила приёмку",
  "subject": "Приёмка квартиры в тюменской новостройке после годовой просрочки застройщика"
}
```

## description (из article.meta.json — description-brief ещё нет)

В Тюмени застройщик год не платил неустойку — семья остановила приёмку

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-za-god-prosrochki-klyuchej-zastrojschik-ne-vyplatil-neustojku-priemku-/`
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

- headline: В Тюмени застройщик год не платил неустойку — семья остановила приёмку
- description: В Тюмени застройщик год не платил неустойку — семья остановила приёмку
- datePublished: 2026-09-09
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
