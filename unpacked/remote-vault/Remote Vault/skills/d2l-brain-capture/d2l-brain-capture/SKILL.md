---
name: d2l-brain-capture
description: Normalize intentionally selected SharePoint, Slack, Confluence, Jira, or sales evidence into D2L Sales Brain inbox records. Use when evidence must be allowlist-checked, minimally copied, deduplicated, classified, linked, and held for review.
tags:
  - ai/agent-skill
  - skill/category/knowledge-capture
  - resource/sales-tools---

# D2L Brain Capture

1. Read `../../config/storage-approval.json`, `../../config/source-allowlist.yaml`, and `../../00-System/Source Policy.md`.
2. Reject DMs, group DMs, secrets, credentials, private contacts, restricted pricing, customer-confidential material, personnel-sensitive content, and non-allowlisted sources.
3. Create normalized JSON with provenance, dates, owner, summary, confidentiality, confidence, seller relevance, tags, and relationships.
4. Run:

```bash
python3 ../../scripts/capture_note.py --input <normalized.json> --dry-run
python3 ../../scripts/detect_duplicates.py
```

5. Persist only a concise source record in `90-Inbox` when approved and requested.
6. Never promote new evidence automatically. Put uncertain synthesis in `98-Needs-Review`.
