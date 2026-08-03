---
name: d2l-objection-coach
description: Retrieve and coach the strongest grounded D2L response to a buyer objection with a concise talk track, supporting evidence, diagnostic discovery question, cautions, and next step.
tags:
  - ai/agent-skill
  - skill/category/objection-handling
  - resource/sales-tools---

# D2L Objection Coach

1. Identify the objection, persona, stage, and underlying risk hypothesis.
2. Run `python3 ../../scripts/brain_search.py "<buyer objection and context>" --json`.
3. Read the strongest notes and cited sources, then invoke the vendored `last30days` skill for current public competitor, regulatory, market, or buyer-context research. Follow `../last30days/SKILL.md` completely.
4. Prefer verified objection, product, proof, and implementation notes; label reviewed coaching, public signals, and evidence gaps.
5. Return acknowledgment, one clarifying question, bounded response, evidence, public-research reconciliation, caution, and next step.
6. Keep language human and concise.
7. Never promise capability, scope, timing, pricing, or roadmap.
