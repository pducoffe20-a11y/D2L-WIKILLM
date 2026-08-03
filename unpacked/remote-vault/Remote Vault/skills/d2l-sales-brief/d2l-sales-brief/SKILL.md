---
name: d2l-sales-brief
description: Generate evidence-first D2L account, meeting, persona, industry, competitor, or opportunity briefs with verified context, likely relevance, unknowns, proof, cautions, discovery questions, and a next seller move.
tags:
  - ai/agent-skill
  - skill/category/sales-enablement
  - resource/sales-tools---

# D2L Sales Brief

1. Run `python3 ../../scripts/brain_search.py "<subject and seller job>" --json`.
2. Read the strongest vault notes and cited sources, then invoke the vendored `last30days` skill with a narrow topic derived from the material findings and gaps. Follow `../last30days/SKILL.md` completely.
3. Use approved read-only internal connectors only for current internal context or surfaced gaps.
4. Keep vault facts, public facts, vendor claims, community signals, buyer engagement, internal activity, and hypotheses separate.
5. Return what matters, verified evidence, reviewed signals, the `last30days` public-research reconciliation, likely relevance, unknowns, discovery, proof, risks, next seller move, desired buyer outcome, and sources.
6. Never infer CRM fields, pricing, packaging, roadmap, buyer intent, or engagement.
7. Do not send or modify external systems without explicit authorization.
