---
name: d2l-proof-finder
description: Match a buyer problem, use case, audience, or desired outcome to the strongest current D2L customer stories and proof points while making relevance and evidence strength explicit and refusing weak matches.
tags:
  - ai/agent-skill
  - resource/sales-tools
  - skill/category/proof-research
  - navigation/skills---

# D2L Proof Finder

1. Define the buyer problem, audience, industry, geography, outcome, and evidence standard.
2. Run `python3 ../../scripts/brain_search.py "<buyer problem and proof context>" --json`.
3. Read the strongest proof notes and cited sources, then invoke the vendored `last30days` skill for current public corroboration, material changes, and source availability. Follow `../last30days/SKILL.md` completely.
4. Rank vault proof by problem fit, context fit, outcome specificity, authority, freshness, customer scope, and approval.
5. Explain fit, mismatch, required validation, and whether public research corroborates, updates, contradicts, or merely contextualizes the vault.
6. Public research cannot create or upgrade D2L customer proof. Use only strong verified proof externally; reviewed source-deck metrics remain candidates.
7. If no strong match exists, say so and record or propose an unresolved evidence gap.
