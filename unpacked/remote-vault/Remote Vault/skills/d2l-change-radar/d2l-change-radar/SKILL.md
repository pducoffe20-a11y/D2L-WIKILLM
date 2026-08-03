---
name: d2l-change-radar
description: Detect material seller-relevant changes across approved D2L sources, compare old and new evidence, explain seller impact, identify affected notes, and queue review while suppressing routine noise.
tags:
  - ai/agent-skill
  - skill/category/change-detection
  - resource/sales-tools---

# D2L Change Radar

1. Run `python3 ../../scripts/refresh_queue.py` and `python3 ../../scripts/check_stale.py`.
2. Read affected vault notes and cited sources, then invoke the vendored `last30days` skill for current public changes affecting positioning, proof, discovery, implementation, risk, process, or external claims. Follow `../last30days/SKILL.md` completely.
3. Separate canonical changes, Jira implementation reality, owner decisions, and field observations.
4. Show old versus new evidence, authority, freshness, affected notes, seller impact, proposed action, and whether public research corroborates, updates, contradicts, or contextualizes the vault.
5. Suppress routine edits, bot noise, unsupported opinions, and changes without seller impact.
6. Queue review before changing verified knowledge; never treat roadmap enablement as a commitment.
