# Schema inputs — B08

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Квартиру в Тюмени ищут четвёртый месяц. Уже согласны на риск",
  "h1": "Квартиру в Тюмени ищут четвёртый месяц. Уже согласны на риск",
  "slug": "tri-mesyaca-iskali-kvartiru-v-tyumeni-i-soglasilis-na-risk",
  "topic_id": "B08",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-21",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/tri-mesyaca-iskali-kvartiru-v-tyumeni-i-soglasilis-na-risk/`
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

- headline: Квартиру в Тюмени ищут четвёртый месяц. Уже согласны на риск
- description: use description from description-brief when available; else headline-based teaser about buyer fatigue and risk in Tyumen secondary market
- datePublished: 2026-08-21
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
