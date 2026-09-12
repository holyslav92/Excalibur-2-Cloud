# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (synthetic — файл отсутствует, данные из title-brief + research-context)

```json
{
  "title": "В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль",
  "h1": "В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль",
  "slug": "v-ddu-v-tyumeni-ukazali-4-2-mln-za-nedelyu-do-podpisaniya-na-eskrou-byl-nol",
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
  "h1": "В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль",
  "title": "В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль",
  "subject": "ДДУ на новостройку и счёт эскроу",
  "slug": "v-ddu-v-tyumeni-ukazali-4-2-mln-za-nedelyu-do-podpisaniya-na-eskrou-byl-nol"
}
```

## description-brief.json

Семья в Тюмени перевела взнос застройщику: менеджер обещал «зачтём в эскроу». Но банк денег на счёте не увидел — семье предложили внести 4,2 млн ещё раз.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-ddu-v-tyumeni-ukazali-4-2-mln-za-nedelyu-do-podpisaniya-na-eskrou-byl-nol/`
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

- headline: В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль
- description: Семья в Тюмени перевела взнос застройщику: менеджер обещал «зачтём в эскроу». Но банк денег на счёте не увидел — семье предложили внести 4,2 млн ещё раз.
- datePublished: 2026-09-12
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
