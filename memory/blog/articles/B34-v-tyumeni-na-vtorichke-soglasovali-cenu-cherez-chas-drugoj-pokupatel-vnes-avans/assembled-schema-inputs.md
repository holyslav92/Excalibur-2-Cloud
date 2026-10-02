# Schema inputs — B34

You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **valid JSON-LD only** (single JSON object). No markdown fences, no prose, no BLOCKER refusals — you have all fields below.

## Meta (title-brief + research-context)

```json
{
  "title": "В Тюмени согласовали цену на двушку — через 1 час её забрали авансом",
  "h1": "В Тюмени согласовали цену на двушку — через 1 час её забрали авансом",
  "slug": "v-tyumeni-na-vtorichke-soglasovali-cenu-cherez-chas-drugoj-pokupatel-vnes-avans",
  "topic_id": "B34",
  "author_id": "svyatoslav-shakin",
  "datePublished": "2026-10-02",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Use `{{SITE_BASE}}` only (NOT [REDACTED], NOT live host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-vtorichke-soglasovali-cenu-cherez-chas-drugoj-pokupatel-vnes-avans/`
- Forbidden: `/blog/` in article URLs

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/

## BlogPosting

- headline: В Тюмени согласовали цену на двушку — через 1 час её забрали авансом
- description: Семья в Тюмени согласовала цену на двушку в мессенджере, но через час другой покупатель внёс аванс — объявление сняли до встречи.
- datePublished: 2026-10-02
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization
- url and @id under canonical slug path

## FAQPage

Do NOT create. No «Частые вопросы» section in article.html.

## Format

@context https://schema.org + @graph with Organization, Person, BlogPosting (match B33 structure).
