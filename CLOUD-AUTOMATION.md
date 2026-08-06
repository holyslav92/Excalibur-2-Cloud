# Excalibur-2-Cloud — Cloud Automation (Daily)

**Только после** `memory/setup/status.json` → `complete: true`.

## Канон

```text
Scout? → research_start → Research → Title → Writer → Sol
→ Cover-text||Schema → Cover → Indexer → Publish
→ Fixer → merge → Content-learner
```

Writer = смысл (`drafts/writer.html`). Sol = финальный слог тенанта.

## Automation prompt

```text
Прочитай AGENTS.md + shared/pipeline-canon.json + shared/tenant-config.json.
Если setup_complete != true — остановись и запусти Setup (см. CLOUD-FIRST-RUN.md).
Игнорируй Automation Memory. Memories в Tools = OFF.

doctor + today.
Если dzen_rf_pack: прочитай shared/dzen-content-rules.md + rf-blocked-entities.json.
needs_scout → Scout (signal_urls из tenant + Wordstat; не RF-DENY heroes).
research_start --topic-id … --title "…".
Research → Title → Writer → Sol.
shell после Sol:
  python3 scripts/excalibur_blog_pipeline_canon.py --article-dir … --stamp
  + opening_meta / html_linter.
Cover-text || Schema → Cover; Indexer; Publish; merge; content-learner.
```

Секреты только из Cloud Secrets.
