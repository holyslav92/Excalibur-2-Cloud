# Schema inputs — B34

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "За 5 дней до ДДУ в Тюмени рассрочка разошлась с ценой на 340 тысяч",
  "h1": "За 5 дней до ДДУ в Тюмени рассрочка разошлась с ценой на 340 тысяч",
  "slug": "za-5-dnej-do-ddu-rassrochka-ne-shodilas-s-cenoj-na-340-tysyach",
  "topic_id": "B34",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-27",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B34",
  "h1": "За 5 дней до ДДУ в Тюмени рассрочка разошлась с ценой на 340 тысяч — семья остановила регистрацию",
  "title": "За 5 дней до ДДУ в Тюмени рассрочка разошлась с ценой на 340 тысяч — семья остановила регистрацию",
  "subject": "Рассрочка от застройщика и её график в договоре на новостройку"
}
```

## description-brief.json (Dzen teaser for BlogPosting.description)

Ежемесячный платёж семью устроил, но финальный взнос внезапно добавил к цене 340 тысяч ₽. В тюменской новостройке документы остановили у порога Росреестра — пока не выяснилась причина.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/za-5-dnej-do-ddu-rassrochka-ne-shodilas-s-cenoj-na-340-tysyach/`
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

- headline: За 5 дней до ДДУ в Тюмени рассрочка разошлась с ценой на 340 тысяч — семья остановила регистрацию
- description: (из description-brief выше)
- datePublished: 2026-09-27
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
