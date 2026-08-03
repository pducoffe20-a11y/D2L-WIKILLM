---
name: d2l-brain-search
description: Search the private D2L Sales Brain before answering D2L sales questions. Use for product, association, persona, customer proof, competitor, objection, implementation, account, or meeting questions requiring provenance, freshness, confidence, contradictions, and live-source escalation.
tags:
  - ai/agent-skill
  - skill/category/knowledge-search
  - resource/sales-tools---

# D2L Brain Search

1. Read `../../AGENTS.md` and `../../00-System/Knowledge Standards.md`.
2. Identify the seller job and entities.
3. Run:

```bash
python3 ../../scripts/brain_search.py "<question>" --json
```

4. Prefer current `verified` notes. Label `reviewed`, `inbox`, `disputed`, `stale`, low-confidence, and restricted results.
5. After reading the strongest vault evidence, invoke the vendored `last30days` skill for every substantive seller answer. Derive a narrow topic from the material findings, gaps, stale claims, or contradictions, and follow `../last30days/SKILL.md` completely.
6. Check an approved internal live connector when no verified result exists, evidence is missing/disputed/stale, or the user asks for current internal information.
7. Return vault findings first. Then reconcile the `last30days` public research as corroboration, update, contradiction, context, or no evidence found. Keep public facts, vendor claims, community signals, and vault verification status separate.
8. Return facts, signals, interpretation, gaps, contradictions, source links and dates, confidence, seller decision, and next check.
9. Never silently modify reviewed or verified notes or auto-capture public research.
