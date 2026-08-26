# Schema inputs — B10 — 2026-08-26

ROLE: schema. Выход: **только** валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Купил квартиру в Тюмени — через год суд вернул её банкроту",
  "h1": "Купил квартиру в Тюмени — через год суд вернул её банкроту",
  "slug": "kupili-kvartiru-v-tyumeni-cherez-god-finupravlyayuschij-osporil-sdelku",
  "topic_id": "B10",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-26",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/kupili-kvartiru-v-tyumeni-cherez-god-finupravlyayuschij-osporil-sdelku/`
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

- headline: Купил квартиру в Тюмени — через год суд вернул её банкроту
- description: Купил квартиру в Тюмени — через год суд вернул её банкроту
- datePublished: 2026-08-26
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
