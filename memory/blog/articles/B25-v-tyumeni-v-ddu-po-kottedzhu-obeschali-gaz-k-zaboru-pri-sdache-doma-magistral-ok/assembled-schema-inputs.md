# Schema inputs — B25

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м",
  "h1": "В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м",
  "slug": "v-tyumeni-v-ddu-po-kottedzhu-obeschali-gaz-k-zaboru-pri-sdache-doma-magistral-ok",
  "topic_id": "B25",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-07",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B25",
  "h1": "В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м",
  "title": "В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м",
  "subject": "коттедж по ДДУ и обещанный газ"
}
```

## description (Дзен-карточка)

Под Тюменью семья покупала коттедж с газом «к забору», а перед передачей нашла трубу в 180 метрах. Святослав Шакин — что сверить в ДДУ до акта и почему доплата 620 тысяч не закрывает спор.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-po-kottedzhu-obeschali-gaz-k-zaboru-pri-sdache-doma-magistral-ok/`
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

- headline: В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м
- description: Под Тюменью семья покупала коттедж с газом «к забору», а перед передачей нашла трубу в 180 метрах. Святослав Шакин — что сверить в ДДУ до акта и почему доплата 620 тысяч не закрывает спор.
- datePublished: 2026-09-07
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
