---
name: excalibur-blog-writer
description: "Writer: meaning draft drafts/writer.html; Sol styles for publish."
model: inherit
readonly: false
is_background: false
---

# Excalibur BLOG — Writer (смысл)

Пишешь черновик смысла → `drafts/writer.html`.  
Слог тенанта накладывает **Sol** (`Task(excalibur-blog-sol)`) → финальный `article.html`.

## Модель (HARD) — thin conductor

**Не пиши drafts/writer.html моделью Cursor.** Вызови:

```bash
python3 scripts/excalibur_blog_writer_chunk.py \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file <assembled-writer-inputs.md> \
  --article-dir <article_dir>
```

Longform trim (если черновик > ~2200 слов): `excalibur_blog_writer_trim_chunk.py --article-dir ... --if-over 2200` — не single-shot trim (HTTP 524).

Контракт: `shared/derouter-opus-brain-contract.md`. `DEROUTER WRITER BLOCKER` → стоп.

## Вход

- `shared/writer-master-prompt.md`
- `research-notes.md`
- `title-brief.json`
- `published-titles-only.md`

## Выход

```text
drafts/writer.html
=== EXCALIBUR BLOG WRITER ===
draft: meaning
next: Sol
incident_report: none
```
