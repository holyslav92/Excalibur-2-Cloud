# Schema inputs — B26

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч",
  "h1": "В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч",
  "slug": "v-tyumeni-novostrojku-sdali-bez-razresheniya-na-vvod-bank-ne-dal-vtoroj-transh",
  "topic_id": "B26",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-13",
  "description": "Застройщик позвал на ключи без РВЭ в реестре — банк заблокировал второй транш на 520 тысяч",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B26",
  "h1": "В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч",
  "title": "В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч",
  "subject": "Новостройка в Тюмени без разрешения на ввод и заблокированный второй транш ипотеки"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-novostrojku-sdali-bez-razresheniya-na-vvod-bank-ne-dal-vtoroj-transh/`
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

- headline: В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч
- description: Застройщик позвал на ключи без РВЭ в реестре — банк заблокировал второй транш на 520 тысяч
- datePublished: 2026-09-13
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
