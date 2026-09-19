# Schema inputs — B29

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (synthesized from title-brief + research-context)

```json
{
  "title": "Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала",
  "h1": "Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала",
  "slug": "v-tyumeni-za-shest-dnej-do-ddu-bank-snyal-ipoteku-bez-vznosa-ot-zastrojschika",
  "topic_id": "B29",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "description": "За шесть дней до ДДУ банк снял программу с нулевым взносом — семья остановила сделку: своих денег на первоначальный платёж не было, ежемесячный платёж вырос примерно на 18 тысяч.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B29",
  "h1": "Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала",
  "title": "Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала",
  "subject": "ипотека без первоначального взноса на новостройку"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-za-shest-dnej-do-ddu-bank-snyal-ipoteku-bez-vznosa-ot-zastrojschika/`
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

- headline: Банк отменил нулевой взнос за 6 дней до ДДУ — сделка встала
- description: За шесть дней до ДДУ банк снял программу с нулевым взносом — семья остановила сделку: своих денег на первоначальный платёж не было, ежемесячный платёж вырос примерно на 18 тысяч.
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
