# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше",
  "h1": "В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше",
  "slug": "v-tyumeni-v-ddu-obeschali-54-metra-na-priemke-kvartira-okazalas-na-2-kvadrata-me",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-14",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше",
  "title": "В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше",
  "subject": "Расхождение площади квартиры в ДДУ и при итоговом обмере на приёмке новостройки в Тюмени."
}
```

## description-brief.json

В Тюмени семье предложили 90 тысяч за недостающие метры — погодите, а почему не 210 тысяч по предварительному расчёту? Ключи остались у застройщика, а спор упёрся в пункт ДДУ.

## research-notes

research_date: 2026-09-14

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-obeschali-54-metra-na-priemke-kvartira-okazalas-na-2-kvadrata-me/`
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

- headline: В Тюмени в ДДУ обещали 54 метра — на приёмке квартира оказалась на 2 квадрата меньше
- description: В Тюмени семье предложили 90 тысяч за недостающие метры — погодите, а почему не 210 тысяч по предварительному расчёту? Ключи остались у застройщика, а спор упёрся в пункт ДДУ.
- datePublished: 2026-09-14
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
