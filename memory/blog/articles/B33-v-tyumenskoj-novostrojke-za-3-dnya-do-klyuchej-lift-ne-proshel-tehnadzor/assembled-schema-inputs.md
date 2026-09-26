# Schema inputs — B33

ROLE: schema. You are already inside `excalibur_blog_derouter_opus_chat.py`. Выход: **только** валидный JSON-LD (содержимое schema.jsonld), без markdown fences, без пояснений и отказов.

## title-brief.json

```json
{
  "topic_id": "B33",
  "h1": "За 3 дня до ключей в тюменской новостройке лифт не прошёл осмотр — заселение перенесли",
  "title": "За 3 дня до ключей в тюменской новостройке лифт не прошёл осмотр — заселение перенесли"
}
```

## research-context (datePublished)

today_iso: 2026-09-26

## slug

v-tyumenskoj-novostrojke-za-3-dnya-do-klyuchej-lift-ne-proshel-tehnadzor

## description (teaser)

За три дня до выдачи ключей выяснилось, что лифт не допущен к эксплуатации. Из-за этого заселение перенесли, а семьи остались одновременно с ипотекой и арендой.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumenskoj-novostrojke-za-3-dnya-do-klyuchej-lift-ne-proshel-tehnadzor/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (только эти URL, без [REDACTED]): https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://vk.ru/tymenrieltor, https://wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: За 3 дня до ключей в тюменской новостройке лифт не прошёл осмотр — заселение перенесли
- description: За три дня до выдачи ключей выяснилось, что лифт не допущен к эксплуатации. Из-за этого заселение перенесли, а семьи остались одновременно с ипотекой и арендой.
- datePublished: 2026-09-26
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
