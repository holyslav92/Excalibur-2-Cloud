# Schema inputs — B11

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Маткапитал был, опека промолчала: дети через три года отменили сделку",
  "h1": "Маткапитал был, опека промолчала: дети через три года отменили сделку",
  "slug": "matkapital-byl-opeka-molchala-cherez-tri-goda-deti-osporili-sdelku-v-tyumeni",
  "topic_id": "B11",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-26",
  "description": "Почему чистая выписка ЕГРН не закрывает риск маткапитала: детские доли, молчание опеки и отмена сделки спустя годы.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

- headline: Маткапитал был, опека промолчала: дети через три года отменили сделку

## description-brief.json

- description: В тюменской вторичке чистый ЕГРН успокоил покупателя: маткапитал был, а детских долей не оказалось. Через три года дети через суд забрали квартиру.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/matkapital-byl-opeka-molchala-cherez-tri-goda-deti-osporili-sdelku-v-tyumeni/`
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

- headline: Маткапитал был, опека промолчала: дети через три года отменили сделку
- description: В тюменской вторичке чистый ЕГРН успокоил покупателя: маткапитал был, а детских долей не оказалось. Через три года дети через суд забрали квартиру.
- datePublished: 2026-08-26
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
