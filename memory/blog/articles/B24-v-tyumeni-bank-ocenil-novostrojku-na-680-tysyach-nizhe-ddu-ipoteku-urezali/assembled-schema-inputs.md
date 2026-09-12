# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "За 5 дней до эскроу — банк урезал ипотеку на 680 тысяч",
  "h1": "За 5 дней до эскроу — банк урезал ипотеку на 680 тысяч",
  "slug": "v-tyumeni-bank-ocenil-novostrojku-na-680-tysyach-nizhe-ddu-ipoteku-urezali",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-12",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "За 5 дней до эскроу — банк урезал ипотеку на 680 тысяч",
  "title": "За 5 дней до эскроу — банк урезал ипотеку на 680 тысяч",
  "subject": "Новостройка в Тюмени, ДДУ и банковская оценка квартиры"
}
```

## description (description-brief.json)

«Одобрено» — а квартира всё равно вернулась в продажу. Святослав Шакин разбирает случай в Тюмени: цена в ДДУ осталась прежней, банк посчитал иначе, а плату за бронь семье вернули не полностью.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-bank-ocenil-novostrojku-na-680-tysyach-nizhe-ddu-ipoteku-urezali/`
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

- headline: За 5 дней до эскроу — банк урезал ипотеку на 680 тысяч
- description: «Одобрено» — а квартира всё равно вернулась в продажу. Святослав Шакин разбирает случай в Тюмени: цена в ДДУ осталась прежней, банк посчитал иначе, а плату за бронь семье вернули не полностью.
- datePublished: 2026-09-12
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
