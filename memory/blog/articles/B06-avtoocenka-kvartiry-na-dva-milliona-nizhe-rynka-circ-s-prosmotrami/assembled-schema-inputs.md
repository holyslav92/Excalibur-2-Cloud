# Schema inputs — B06

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Автооценка занизила цену — и квартира подорожала за сутки",
  "h1": "Автооценка занизила цену — и квартира подорожала за сутки",
  "slug": "avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami",
  "topic_id": "B06",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-21",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami/`
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

- headline: Автооценка занизила цену — и квартира подорожала за сутки
- description: Автооценка занизила цену — и квартира подорожала за сутки
- datePublished: 2026-08-21
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
