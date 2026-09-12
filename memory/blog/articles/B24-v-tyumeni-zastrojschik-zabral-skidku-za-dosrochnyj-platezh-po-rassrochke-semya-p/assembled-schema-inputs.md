# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Застройщик забрал скидку за досрочный платёж: семья потеряла 320 тысяч",
  "h1": "Застройщик забрал скидку за досрочный платёж: семья потеряла 320 тысяч",
  "slug": "v-tyumeni-zastrojschik-zabral-skidku-za-dosrochnyj-platezh-po-rassrochke-semya-p",
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
  "h1": "Застройщик забрал скидку за досрочный платёж: семья потеряла 320 тысяч",
  "slug": "v-tyumeni-zastrojschik-zabral-skidku-za-dosrochnyj-platezh-po-rassrochke-semya-p",
  "subject": "Рассрочка от застройщика и скидка за досрочный платёж"
}
```

## description (article.meta — description-brief ещё нет)

Застройщик забрал скидку за досрочный платёж: семья потеряла 320 тысяч

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-zabral-skidku-za-dosrochnyj-platezh-po-rassrochke-semya-p/`
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

- headline: Застройщик забрал скидку за досрочный платёж: семья потеряла 320 тысяч
- description: Застройщик забрал скидку за досрочный платёж: семья потеряла 320 тысяч
- datePublished: 2026-09-12
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
