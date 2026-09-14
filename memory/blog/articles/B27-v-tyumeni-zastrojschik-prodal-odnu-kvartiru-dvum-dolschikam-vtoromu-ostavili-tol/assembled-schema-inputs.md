# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени две брони на одну квартиру — семья потеряла лот и 180 тысяч",
  "h1": "В Тюмени две брони на одну квартиру — семья потеряла лот и 180 тысяч",
  "slug": "v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-dolschikam-vtoromu-ostavili-tol",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-14",
  "description": "В Тюмени две брони на одну квартиру — семья потеряла лот и 180 тысяч",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени две брони на одну квартиру — семья потеряла лот и 180 тысяч",
  "title": "В Тюмени две брони на одну квартиру — семья потеряла лот и 180 тысяч",
  "subject": "Две брони на одну квартиру в новостройке Тюмени — потеря лота и возврат 180 тысяч"
}
```

## description-brief.json

```json
{
  "description": "Две семьи внесли по 180 тысяч за одну квартиру в Тюмени. Первой достались ДДУ и эскроу, второй предложили похожий лот — но уже с доплатой 390 тысяч."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-dolschikam-vtoromu-ostavili-tol/`
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

- headline: В Тюмени две брони на одну квартиру — семья потеряла лот и 180 тысяч
- description: Две семьи внесли по 180 тысяч за одну квартиру в Тюмени. Первой достались ДДУ и эскроу, второй предложили похожий лот — но уже с доплатой 390 тысяч.
- datePublished: 2026-09-14
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
