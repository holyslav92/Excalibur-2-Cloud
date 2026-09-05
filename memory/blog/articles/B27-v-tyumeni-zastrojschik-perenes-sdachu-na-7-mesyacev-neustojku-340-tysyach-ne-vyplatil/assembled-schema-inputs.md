# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил",
  "h1": "Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил",
  "slug": "v-tyumeni-zastrojschik-perenes-sdachu-na-7-mesyacev-neustojku-340-tysyach-ne-vyplatil",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил",
  "title": "Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил"
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-perenes-sdachu-na-7-mesyacev-neustojku-340-tysyach-ne-vyplatil/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/[REDACTED], vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил
- description: Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
