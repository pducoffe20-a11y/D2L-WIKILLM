---
name: d2l-brain-curate
description: Review D2L Sales Brain inbox notes for duplicates, provenance, authority, freshness, conflicts, claim scope, and relationships. Use to propose merges, links, promotion, dispute, archive, or human review while preserving source history.
tags:
  - ai/agent-skill
  - skill/category/knowledge-curation
  - resource/sales-tools---

# D2L Brain Curate

1. Run:

```bash
python3 ../../scripts/validate_vault.py
python3 ../../scripts/detect_duplicates.py
python3 ../../scripts/check_links.py
```

2. Compare authority and freshness independently and preserve contradictions.
3. Separate source facts from seller interpretation and bind material claims to provenance.
4. Retain source records and relationship history before merging synthesis.
5. Promote only after authoritative source readback and record the review date.
6. Put uncertain or material changes in `98-Needs-Review`.
