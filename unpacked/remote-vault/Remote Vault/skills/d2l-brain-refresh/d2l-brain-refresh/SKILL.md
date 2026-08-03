---
name: d2l-brain-refresh
description: Recheck verified D2L Sales Brain notes against original approved sources. Use for stale, changed, deleted, superseded, conflicting, or inaccessible evidence and produce a review queue before changing claims.
tags:
  - ai/agent-skill
  - skill/category/knowledge-refresh
  - resource/sales-tools---

# D2L Brain Refresh

1. Run:

```bash
python3 ../../scripts/refresh_queue.py
```

2. Resolve each due note’s exact approved source and fetch only relevant content.
3. Compare source availability, date, authority, content, and claim scope.
4. Connector failure means unknown, never unchanged.
5. Queue review before changing material claims; update `last_verified` only after successful readback.
6. Finish with:

```bash
python3 ../../scripts/vault_health.py
```
