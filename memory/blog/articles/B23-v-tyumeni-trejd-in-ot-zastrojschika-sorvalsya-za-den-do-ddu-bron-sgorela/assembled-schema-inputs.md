# Schema inputs — B23

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела",
  "h1": "В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела",
  "slug": "v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela",
  "topic_id": "B23",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B23",
  "h1": "В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела",
  "title": "В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела",
  "subject": "Трейд-ин от застройщика при покупке квартиры в новостройке"
}
```

## description (article.meta — description-brief ещё нет)

В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela/`
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

- headline: В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела
- description: В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
