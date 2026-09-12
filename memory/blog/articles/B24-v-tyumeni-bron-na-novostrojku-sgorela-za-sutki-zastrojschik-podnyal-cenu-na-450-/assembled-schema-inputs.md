# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч",
  "h1": "В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч",
  "slug": "v-tyumeni-bron-na-novostrojku-sgorela-za-sutki-zastrojschik-podnyal-cenu-na-450-",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч",
  "title": "В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч",
  "subject": "платная бронь новостройки в Тюмени"
}
```

## description (article.meta — description-brief ещё нет)

Семья внесла 50 тысяч за бронь новостройки в Тюмени, а через сутки цена выросла на 450 тысяч. Святослав Шакин разбирает, почему одобренная ипотека не защитила от пересчёта и удержания денег за бронь.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-bron-na-novostrojku-sgorela-za-sutki-zastrojschik-podnyal-cenu-na-450-/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч
- description: Семья внесла 50 тысяч за бронь новостройки в Тюмени, а через сутки цена выросла на 450 тысяч. Святослав Шакин разбирает, почему одобренная ипотека не защитила от пересчёта и удержания денег за бронь.
- datePublished: 2026-09-10
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
