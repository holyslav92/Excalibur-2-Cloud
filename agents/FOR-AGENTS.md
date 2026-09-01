# Excalibur-2-Cloud — субагенты

Карта: [shared/pipeline-task-map.md](../shared/pipeline-task-map.md)

**Всего 19 ролей** (17 прежних pipeline + `description` + `cover-qa` + **`stylo`**).

## Директор и Setup (не Task)

| Роль | Файл | Skill |
|------|------|-------|
| Setup (первый запуск) | `excalibur-blog-setup.md` | `setup-excalibur-blog` |
| Директор (пайплайн) | `excalibur-blog-director.md` | `director-excalibur-blog` |

## Setup Task trio

| Task | Роль |
|------|------|
| setup-voice | SOUL + examples + article-style |
| setup-visual | cover configs + assets |

## Субагенты пайплайна (Task)

| # | Task | Роль |
|---|------|------|
| 🔍 | scout | Klyshin × Wordstat тема |
| ① | research | Facts |
| ①b | title | H1 |
| ② | writer | Смысл → `drafts/writer.html` |
| ②b | **sol** | **Финал `article.html` (слог SOUL)** |
| ②c | **stylo** | **Голос vs gold; ≤1 Sol с notes** |
| ②d | **description** | **Дзен-карточка → `description-brief.json`** |
| ④a | cover-text | RU надписи |
| ④b | schema | JSON-LD |
| ④c | cover | Image API + figures |
| ④d | **cover-qa** | **Визуальный gate → `cover/cover_qa.json`** |
| ⑤ | indexer | llms |
| ⑥ | publish | WP |
| ⑦ | fixer | Incidents |
| ⑦b | content-learner | Metrika |

## Канон порядка

```text
Scout? → Research → Title → Writer → Sol → Stylo
→ Description → Cover-text || Schema → Cover → Cover-QA → Indexer → Publish
→ Fixer → Content-learner
```

После **Stylo**: shell `pipeline_canon --stamp` + opening_meta / html_linter.

Пока setup не complete — только Setup (+ setup-voice/visual).

## Полный список имён (19)

1. `excalibur-blog-setup`
2. `excalibur-blog-setup-voice`
3. `excalibur-blog-setup-visual`
4. `excalibur-blog-director`
5. `excalibur-blog-scout`
6. `excalibur-blog-research`
7. `excalibur-blog-title`
8. `excalibur-blog-writer`
9. `excalibur-blog-sol`
10. `excalibur-blog-stylo`
11. `excalibur-blog-description`
12. `excalibur-blog-cover-text`
13. `excalibur-blog-schema`
14. `excalibur-blog-cover`
15. `excalibur-blog-cover-qa`
16. `excalibur-blog-indexer`
17. `excalibur-blog-publish`
18. `excalibur-blog-fixer`
19. `excalibur-blog-content-learner`
