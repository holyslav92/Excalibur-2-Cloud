# Schema inputs — B27

ROLE: schema. Ты вызываешься через `excalibur_blog_derouter_opus_chat.py` — gate запустит оркестратор отдельно.
**Запрещено** возвращать BLOCKER или пустой ответ. Твоя задача — собрать JSON-LD BlogPosting по данным ниже.
Выход: только валидный JSON-LD (@context + @graph). Без markdown fences, без пояснений.

## article.meta.json

```json
{
  "title": "На 47-й день срока приостановили регистрацию детских долей в новостройке с маткапиталом",
  "h1": "На 47-й день срока приостановили регистрацию детских долей в новостройке с маткапиталом",
  "slug": "v-tyumeni-kupili-novostrojku-s-matkapitalom-cherez-polgoda-opeka-ne-prinyala-dol",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-17",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "На 47-й день срока приостановили регистрацию детских долей в новостройке с маткапиталом",
  "title": "На 47-й день срока приостановили регистрацию детских долей в новостройке с маткапиталом",
  "subject": "Новостройка с маткапиталом и приостановка регистрации детских долей после получения ключей."
}
```

## description-brief.json

Четверо в семье — значит, квартиру поровну? Святослав Шакин из Тюмени разбирает сюжет, где готовый шаблон соглашения выглядел безупречно — пока документы не попали в Росреестр.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-kupili-novostrojku-s-matkapitalom-cherez-polgoda-opeka-ne-prinyala-dol/`
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

- headline: На 47-й день срока приостановили регистрацию детских долей в новостройке с маткапиталом
- description: Четверо в семье — значит, квартиру поровну? Святослав Шакин из Тюмени разбирает сюжет, где готовый шаблон соглашения выглядел безупречно — пока документы не попали в Росреестр.
- datePublished: 2026-09-17
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
