# Schema inputs — B16

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали",
  "h1": "На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали",
  "slug": "na-priemke-novostrojki-v-tyumeni-nashli-mokruyu-styazhku-klyuchi-ne-vydali",
  "topic_id": "B16",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-01",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B16",
  "h1": "На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали",
  "title": "На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/na-priemke-novostrojki-v-tyumeni-nashli-mokruyu-styazhku-klyuchi-ne-vydali/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/holyslav92, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали
- description: На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали
- datePublished: 2026-09-01
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
