# Excalibur-SUBARENDA — отдельная фабрика «Добрый дом»

**Не мерджить** ветку `excalibur-subarenda-copy` в `main` этого репозитория.
`main` здесь — пайплайн **The Риэлтор** (tymenrieltor.ru).

## Целевой репозиторий

https://github.com/holyslav92/Excalibur-SUBARENDA (создать вручную — Cloud Agent
не имеет `createRepository` для holyslav92).

## Готовая адаптация

Ветка **`excalibur-subarenda-copy`** в этом репо содержит полную копию пайплайна
для **«Добрый дом»** (посуточная аренда / субаренда, Тюмень).

Инструкция переноса в новый репозиторий: см. `docs/EXCALIBUR-SUBARENDA-CREATE.md`
на ветке `excalibur-subarenda-copy`.

## Сайт тенанта

- Unicode: https://добрыйдом-72.рф/
- Punycode: https://xn---72-9cdob8azaodt6k.xn--p1ai/
- Блог: https://добрыйдом-72.рф/blog

## Publish

Live publish **OFF** по умолчанию (`EXCALIBUR_BLOG_ALLOW_PUBLISH=no`).
Не копировать WP/FTP credentials из Excalibur-2-Cloud.
