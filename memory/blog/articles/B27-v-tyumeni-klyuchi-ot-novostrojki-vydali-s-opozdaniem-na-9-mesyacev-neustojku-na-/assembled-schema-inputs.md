# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени застройщик выдал ключи через 9 месяцев — неустойку не выплатил",
  "h1": "В Тюмени застройщик выдал ключи через 9 месяцев — неустойку не выплатил",
  "slug": "v-tyumeni-klyuchi-ot-novostrojki-vydali-s-opozdaniem-na-9-mesyacev-neustojku-na-",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-16",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени застройщик выдал ключи через 9 месяцев — неустойку не выплатил",
  "title": "В Тюмени застройщик выдал ключи через 9 месяцев — неустойку не выплатил",
  "subject": "новостройка по ДДУ, задержка передачи ключей и неустойка застройщика"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-klyuchi-ot-novostrojki-vydali-s-opozdaniem-na-9-mesyacev-neustojku-na-/`
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

- headline: В Тюмени застройщик выдал ключи через 9 месяцев — неустойку не выплатил
- description: Ключи от новостройки в Тюмени выдали с опозданием на девять месяцев, а неустойку на счёт так и не перевели — семья подала иск.
- datePublished: 2026-09-16
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
