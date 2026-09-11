Принял B21 в работу: сформирую handoff через обязательный Derouter и сохраню в указанный файл.Не могу выполнить запись в файловую систему или запустить Derouter из этого API-сеанса. Для обязательного формирования handoff запустите в репозитории:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role scout \
  --system-file skills/scout-excalibur-blog/SKILL.md \
  --user-file <assembled-scout-inputs-B21.md> \
  --output .cursor/excalibur-blog-handoff.md \
  --article-dir memory/scout
```

В `<assembled-scout-inputs-B21.md>` передайте предоставленный Scout brief без изменений, включая обязательные поля:

```text
topic_id: B21
cluster_id: newbuild_assignment_deposit_scam_tyumen
title_draft: В Тюмени за переуступку взяли 280 тысяч — ДДУ так и не подписали
slug: v-tyumeni-za-pereustupku-vzyali-280-tysyach-ddu-tak-i-ne-podpisali

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-01)
klyshin_hook: optional | energy only: casus+number+punch (280 тысяч, ДДУ не подписали) | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
dzen_casus_shape: PASS
comment_magnet_angle: «Переуступка в новостройке: вы бы перевели 280 тысяч до регистрации цессии в Росреестре, если скидка к застройщику — 400?»
wordstat_rework: «переуступка новостройка» 10 → «переуступка новостройки» 10 → final P0 «купить новостройку в тюмени» 1882
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 1882 | support «новостройки в тюмени от застройщика» 1268 | niche «переуступка новостройки» 10
story_dup_check: PASS | cluster_id: newbuild_assignment_deposit_scam_tyumen
```

После генерации обязательно прогоните handoff через `excalibur_blog_wordstat_gate.py handoff`; при `DEROUTER SCOUT BLOCKER` или Wordstat blocker публикацию не продолжать.
