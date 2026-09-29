Assembled schema inputs — B34

Derouter schema utility. Output schema.jsonld BlogPosting only (FAQ skip — theme_blocks.faq=skip).

H1: В Тюмени аренда на 3 года в ЕГРН остановила сделку
topic_id: B34
slug: v-tyumeni-zaregistrirovannaya-arenda-na-tri-goda-ostanovila-pokupku-vtorichki-za
datePublished: 2026-09-29 (from research-context)
author_id: svyatoslav-shakin (shared/authors-registry.json)
canonical: {{SITE_BASE}}/v-tyumeni-zaregistrirovannaya-arenda-na-tri-goda-ostanovila-pokupku-vtorichki-za/
NO /blog/ prefix. Use {{SITE_BASE}} placeholder not live host.

Article lead (plain):
В Тюмени семья остановила покупку вторички за 7 дней до аванса: на повторном осмотре в квартире обнаружился жилец с зарегистрированным в ЕГРН договором найма на 3 года.

theme_blocks: faq skip, quiz skip

OUTPUT CONTRACT (HARD): respond with ONLY one JSON-LD document (@context + @graph). No markdown fences, no Russian prose, no shell instructions. Mirror B33 structure: Organization, Person author, BlogPosting with {{SITE_BASE}} placeholders.

Example shape (adapt headline/url/slug/description for B34):
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "{{SITE_BASE}}/#organization", "name": "The Риэлтор", "url": "{{SITE_BASE}}/" },
    { "@type": "Person", "@id": "{{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin", "name": "Святослав Шакин", "jobTitle": "Личный риэлтор в Тюмени", "worksFor": { "@id": "{{SITE_BASE}}/#organization" } },
    { "@type": "BlogPosting", "@id": "{{SITE_BASE}}/SLUG/#blogposting", "url": "{{SITE_BASE}}/SLUG/", "headline": "...", "description": "...", "datePublished": "2026-09-29", "inLanguage": "ru-RU", "author": { "@id": "{{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin" }, "publisher": { "@id": "{{SITE_BASE}}/#organization" }, "mainEntityOfPage": { "@type": "WebPage", "@id": "{{SITE_BASE}}/SLUG/" } }
  ]
}
```

description teaser (Dzen-style, one sentence): Семья не внесла аванс за вторичку в Тюмени: на повторном осмотре нашли жильца с договором найма на три года, зарегистрированным в ЕГРН.
