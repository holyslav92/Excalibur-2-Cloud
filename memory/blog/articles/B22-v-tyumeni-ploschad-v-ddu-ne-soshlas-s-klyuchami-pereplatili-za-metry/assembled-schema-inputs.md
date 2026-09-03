# Schema inputs — B22

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте",
  "h1": "В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте",
  "slug": "v-tyumeni-ploschad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry",
  "topic_id": "B22",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-03",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B22",
  "h1": "В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте",
  "title": "В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте",
  "subject": "Квартира в новостройке по ДДУ и расхождение фактической площади при передаче"
}
```

## description (из article.meta / лид)

В Тюмени на приёмке не хватило двух метров: по ДДУ оплатили больше, застройщик отказал в пересчёте. Святослав Шакин разбирает, как не потерять деньги на квадратах и что писать в акте.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-ploschad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/[REDACTED], vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте
- description: В Тюмени на приёмке не хватило двух метров: по ДДУ оплатили больше, застройщик отказал в пересчёте. Святослав Шакин разбирает, как не потерять деньги на квадратах и что писать в акте.
- datePublished: 2026-09-03
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
