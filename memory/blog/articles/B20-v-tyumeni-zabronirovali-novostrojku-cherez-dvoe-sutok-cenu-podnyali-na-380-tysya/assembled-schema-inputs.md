# Schema inputs — B20

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч",
  "h1": "Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч",
  "slug": "v-tyumeni-zabronirovali-novostrojku-cherez-dvoe-sutok-cenu-podnyali-na-380-tysya",
  "topic_id": "B20",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-01",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B20",
  "h1": "Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч",
  "title": "Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч",
  "subject": "бронь новостройки в Тюмени"
}
```

## cluster
newbuild booking price increase

## description-brief.json

Отсутствует на момент сборки schema. Использовать description из article.meta.json:
«Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zabronirovali-novostrojku-cherez-dvoe-sutok-cenu-podnyali-na-380-tysya/`
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

- headline: Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч
- description: Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч
- datePublished: 2026-09-01
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
