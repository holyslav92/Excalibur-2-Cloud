# Schema inputs — B25

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку",
  "h1": "В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку",
  "slug": "v-tyumeni-vzyali-kvartiru-v-rassrochku-ot-zastrojschika-na-dosrochnom-zakrytii-v",
  "topic_id": "B25",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B25",
  "h1": "В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку",
  "title": "В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку",
  "subject": "Квартира в новостройке по рассрочке от застройщика",
  "angle": "Семья рассчитывала досрочно закрыть беспроцентную рассрочку, но столкнулась с пересчётом цены и потерей скидки."
}
```

## description (description-brief.json отсутствует — из article.meta)

В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-vzyali-kvartiru-v-rassrochku-ot-zastrojschika-na-dosrochnom-zakrytii-v/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (только внешние, без {{SITE_BASE}} и без [REDACTED]): dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку
- description: В Тюмени взяли квартиру в рассрочку — досрочно потеряли скидку
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
