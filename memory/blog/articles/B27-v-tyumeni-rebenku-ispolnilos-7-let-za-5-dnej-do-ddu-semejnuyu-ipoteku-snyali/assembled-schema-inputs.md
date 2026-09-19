# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли",
  "h1": "В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли",
  "slug": "v-tyumeni-rebenku-ispolnilos-7-let-za-5-dnej-do-ddu-semejnuyu-ipoteku-snyali",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "description": "В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли",
  "title": "В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли",
  "subject": "Семейная ипотека на новостройку в Тюмени и возраст ребёнка"
}
```

## description-brief.json

```json
{
  "topic_id": "B27",
  "description": "Банк одобрил — можно выдохнуть? Семья в Тюмени уже считала платёж по льготной ставке, но перед ДДУ получила неподъёмный пересчёт: бронь была, одобрение было — а гарантии ставки не оказалось."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-rebenku-ispolnilos-7-let-za-5-dnej-do-ddu-semejnuyu-ipoteku-snyali/`
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

- headline: В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли
- description: Банк одобрил — можно выдохнуть? Семья в Тюмени уже считала платёж по льготной ставке, но перед ДДУ получила неподъёмный пересчёт: бронь была, одобрение было — а гарантии ставки не оказалось.
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
