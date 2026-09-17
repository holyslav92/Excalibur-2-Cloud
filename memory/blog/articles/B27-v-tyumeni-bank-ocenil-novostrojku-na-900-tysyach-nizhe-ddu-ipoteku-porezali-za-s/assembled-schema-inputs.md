# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени оценка новостройки на 900 тысяч ниже ДДУ — банк урезал кредит",
  "h1": "В Тюмени оценка новостройки на 900 тысяч ниже ДДУ — банк урезал кредит",
  "slug": "v-tyumeni-bank-ocenil-novostrojku-na-900-tysyach-nizhe-ddu-ipoteku-porezali-za-s",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-17",
  "description": "В Тюмени оценка новостройки на 900 тысяч ниже ДДУ — банк урезал кредит",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени оценка новостройки на 900 тысяч ниже ДДУ — банк урезал кредит",
  "title": "В Тюмени оценка новостройки на 900 тысяч ниже ДДУ — банк урезал кредит",
  "subject": "Банковская оценка новостройки ниже цены ДДУ и сокращение одобренного ипотечного кредита."
}
```

## description-brief.json

```json
{
  "topic_id": "B27",
  "description": "Предварительное одобрение уже в кармане, бронь держит квартиру. Но за сутки до ДДУ выяснилось: банк видит залог на 900 тысяч дешевле — семья решила не искать эти деньги в последний момент."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-bank-ocenil-novostrojku-na-900-tysyach-nizhe-ddu-ipoteku-porezali-za-s/`
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

- headline: В Тюмени оценка новостройки на 900 тысяч ниже ДДУ — банк урезал кредит
- description: Предварительное одобрение уже в кармане, бронь держит квартиру. Но за сутки до ДДУ выяснилось: банк видит залог на 900 тысяч дешевле — семья решила не искать эти деньги в последний момент.
- datePublished: 2026-09-17
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
