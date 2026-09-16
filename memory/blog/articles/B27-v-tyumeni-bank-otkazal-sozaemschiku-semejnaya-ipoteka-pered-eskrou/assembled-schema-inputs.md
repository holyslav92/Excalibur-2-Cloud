# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу",
  "h1": "В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу",
  "slug": "v-tyumeni-bank-otkazal-sozaemschiku-semejnaya-ipoteka-pered-eskrou",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-16",
  "description": "В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу",
  "title": "В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу",
  "subject": "Семейная ипотека в новостройке: отказ банка созаёмщику перед эскроу"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-bank-otkazal-sozaemschiku-semejnaya-ipoteka-pered-eskrou/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://vk.ru/tymenrieltor, https://wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png (ImageObject optional)

## BlogPosting

- headline: В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу
- description: В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу
- datePublished: 2026-09-16
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage. Без литерала [REDACTED].
