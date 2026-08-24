# Schema inputs — B10

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Квартиру зарегистрировали без денег — наследники оспорили сделку",
  "h1": "Квартиру зарегистрировали без денег — наследники оспорили сделку",
  "slug": "sdelku-zaregistrirovali-deneg-po-faktu-ne-bylo-v-tyumeni-nasledniki-osporili-pok",
  "topic_id": "B10",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-24",
  "description": "Квартиру зарегистрировали без денег — наследники оспорили сделку",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

- h1: Квартиру зарегистрировали без денег — наследники оспорили сделку
- subject: Зарегистрированная продажа квартиры без реального расчёта, которую оспаривают наследники продавца

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/sdelku-zaregistrirovali-deneg-po-faktu-ne-bylo-v-tyumeni-nasledniki-osporili-pok/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: {{SITE_BASE}}/, {{SITE_BASE}}/rieltor-tyumen/, {{SITE_BASE}}/kontakty/, dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/holyslav92, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: Квартиру зарегистрировали без денег — наследники оспорили сделку
- description: Квартиру зарегистрировали без денег — наследники оспорили сделку
- datePublished: 2026-08-24
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет h2 FAQ + h3/p пар). theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
