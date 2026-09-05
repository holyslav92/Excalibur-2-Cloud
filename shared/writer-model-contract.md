# Writer / Sol — powerful tier (Derouter GPT-6 Astra REST)

> Канонический контракт всего «мозга» фабрики:
> **`shared/derouter-opus-brain-contract.md`**

Writer и Sol — **powerful tier** (`gpt-6-astra` via Derouter REST).

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role writer|sol \
  --system-file <skill.md> \
  --user-file <inputs.md> \
  --output <drafts/writer.html|article.html> \
  --article-dir <article_dir>
```

- **Model:** `gpt-6-astra` (env `DEROUTER_POWERFUL_MODEL`, семейство GPT-6 Astra)
- **Auth:** `DEROUTER_API_KEY` только из Cloud Secrets
- **Endpoint:** `https://api.derouter.ai/openai/v1/chat/completions`

Utility tier (`gpt-5.6-terra`) — Scout, Title, Research, Description, Cover-text, Schema, Cover-scene. См. brain contract.

## Fail loud

`DEROUTER WRITER BLOCKER` / `DEROUTER SOL BLOCKER` — без тихого fallback на Composer или Terra.

Полный контракт: `shared/derouter-opus-brain-contract.md`.
