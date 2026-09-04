# Schema inputs — B22

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени застройщик потребовал акт с дефектами — иначе без ключей",
  "h1": "В Тюмени застройщик потребовал акт с дефектами — иначе без ключей",
  "slug": "v-tyumeni-na-priemke-naschitali-defekty-zastrojschik-potreboval-podpisat-akt",
  "topic_id": "B22",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-04",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B22",
  "h1": "В Тюмени застройщик потребовал акт с дефектами — иначе без ключей",
  "title": "В Тюмени застройщик потребовал акт с дефектами — иначе без ключей",
  "subject": "приёмка квартиры в тюменской новостройке и давление подписать передаточный акт с дефектами"
}
```

## description-brief.json

```json
{
  "topic_id": "B22",
  "description": "Ключи обещали выдать после одной подписи, но семья в тюменской новостройке оставила в бумагах десятки дефектов. Что делать, если ипотека уже идёт, а застройщик торопит?"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-priemke-naschitali-defekty-zastrojschik-potreboval-podpisat-akt/`
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

- headline: В Тюмени застройщик потребовал акт с дефектами — иначе без ключей
- description: Ключи обещали выдать после одной подписи, но семья в тюменской новостройке оставила в бумагах десятки дефектов. Что делать, если ипотека уже идёт, а застройщик торопит?
- datePublished: 2026-09-04
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
