# Schema inputs — B11

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени открытая кухня остановила регистрацию квартиры",
  "h1": "В Тюмени открытая кухня остановила регистрацию квартиры",
  "slug": "v-tyumeni-kupili-kvartiru-s-otkrytoj-kuhnej-rosreestr-otkazal-v-registracii",
  "topic_id": "B11",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-28",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B11",
  "h1": "В Тюмени открытая кухня остановила регистрацию квартиры",
  "title": "В Тюмени открытая кухня остановила регистрацию квартиры"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени открытая кухня остановила регистрацию квартиры».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-kupili-kvartiru-s-otkrytoj-kuhnej-rosreestr-otkazal-v-registracii/`
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

- headline: В Тюмени открытая кухня остановила регистрацию квартиры
- description: В Тюмени открытая кухня остановила регистрацию квартиры
- datePublished: 2026-08-28
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
