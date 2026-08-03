---
id: relationship-resources-index
title: Relationship Resources - Complete Index
type: resource-index
status: active
created: 2026-08-02
tags:
  - navigation/index
  - ontology/reference
  - system/resources
---

# Relationship Resources: Complete Index

**One-stop reference for all relationship-building documents.**

---

## Entry Points (Start Here)

| Document | Purpose | Read Time | When |
|----------|---------|-----------|------|
| [[Relationships - START HERE]] | Overview + reading roadmap | 15 min | First |
| [[Relationship Framework]] | Theory of 5 relationship types | 20 min | Second |
| [[Insight Catalyst Matrix]] | Your vault's gaps + priorities | 20 min | Third |

---

## How-To Guides

| Document | Purpose | Read Time | When |
|----------|---------|-----------|------|
| [[Relationship Mapping Template]] | YAML patterns + step-by-step | 25 min | Before implementing |
| [[Relationship Architecture]] | Visual patterns + connection types | 20 min | For reference |
| [[Relationship Quick-Start]] | 30 specific connections to add | 15 min | For action list |

---

## Implementation Roadmap

### Week 1: Foundation (6-8 hours)

**Day 1-2:**
- [ ] Read [[Relationships - START HERE]] (15 min)
- [ ] Read [[Relationship Framework]] (20 min)
- [ ] Read [[Insight Catalyst Matrix]] (20 min)
- [ ] Total: ~1 hour of learning

**Day 3:**
- [ ] Read [[Relationship Mapping Template]] (25 min)
- [ ] Do 10 quick wins from [[Relationship Quick-Start]] (30 min)
- [ ] Total: ~1 hour

**Day 4-5:**
- [ ] Connect all customer stories: 15-20 stories × 10 min = 2.5-3 hours
  - Each story gets: industry + products + outcomes + objections
  - Pattern: Use [[Relationship Mapping Template]] Example 1

**Day 6:**
- [ ] Connect key personas: 5 personas × 30 min = 2.5 hours
  - Each persona gets: industry + objections + values + proof
  - Pattern: Use [[Relationship Mapping Template]] Example 2

**Day 7:**
- [ ] Connect 5 major objections: 5 × 20 min = 1.5 hours
  - Each objection gets: value model + 2-3 proofs + methodology
  - Pattern: Use [[Relationship Mapping Template]] Example 4

**Week 1 Total:** 6-8 hours → Foundation complete

### Week 2: Enhancement (4-5 hours)

**Day 1-2:**
- [ ] Build proof density for outcomes (1-2 hours)
  - Identify outcomes with <2 proofs
  - Link related customer stories
  - Create diverse proof chains

**Day 3-4:**
- [ ] Competitive differentiation chains (1.5-2 hours)
  - Link products → outcomes → competitor cards
  - Show feature → proof → advantage
  - Pattern: Use [[Relationship Mapping Template]] Example 2

**Day 5:**
- [ ] Review and gap analysis (1-1.5 hours)
  - Use [[Insight Catalyst Matrix]] to identify gaps
  - Flag content to create
  - Prioritize by strategic impact

### Week 3+: Continuous Improvement

- [ ] Fill gaps with new content (as identified)
- [ ] Add relationships to new notes immediately
- [ ] Quarterly relationship health review

---

## By Use Case

### "I'm a Sales Person"

**You want:** Quick paths from buyer → problem → solution → proof

**Read:**
1. [[Relationships - START HERE]] (context)
2. [[Relationship Quick-Start]] (use "Sales Scenario Questions" section)

**Use patterns:**
- [[Relationship Mapping Template]] Example 2 (Persona journey)
- [[Relationship Architecture]] section on Persona Journey

**Questions it answers:**
- "What's the strongest proof for this objection?"
- "Who else in their industry succeeded?"
- "Why should they choose us vs. Competitor X?"

---

### "I'm a Marketer"

**You want:** Proof density analysis, outcome validation, content gaps

**Read:**
1. [[Insight Catalyst Matrix]] (shows proof gaps + priorities)
2. [[Relationship Quick-Start]] (content planning section)
3. [[Relationship Architecture]] (Proof Diversity pattern)

**Questions it answers:**
- "Which outcomes have weak proof?"
- "Which industries need more coverage?"
- "What content would create the most leverage?"

---

### "I'm a Content Creator"

**You want:** How to weave new content into the network

**Read:**
1. [[Relationship Mapping Template]] (all sections)
2. [[Relationships - START HERE]] (understand what relationships matter)
3. [[Relationship Quick-Start]] (see patterns of high-impact connections)

**When creating new notes:**
- Always add `related_notes` field (use taxonomy from template)
- Add wikilinks in body text where relevant
- Use context_hints for prerequisites
- Check reciprocal links (if A→B, should B→A?)

---

### "I'm Leading Implementation"

**You want:** Full picture of architecture + prioritized roadmap

**Read (In order):**
1. [[Relationship Framework]] (philosophy)
2. [[Insight Catalyst Matrix]] (what's missing)
3. [[Relationship Architecture]] (how it all connects)
4. [[Relationship Quick-Start]] (implementation timeline)

**Use for:**
- Team alignment on what we're building
- Prioritizing work by impact
- Measuring progress (relationship density metrics)
- Identifying gaps to communicate to team

---

## Reference: Relationship Types

### By Name

| Type | Meaning | Example | Read |
|------|---------|---------|------|
| `solves-problem` | Product addresses use case | Brightspace → Engagement | Framework |
| `validates-context` | Provides context explaining why | Industry Playbook → Story | Template |
| `demonstrates-outcome` | Proof shows claimed value works | Customer Story → Outcome | Template |
| `overcomes-objection` | Proof that objection was handled | Story → Objection | Framework |
| `enables` | Feature enhances another capability | Lumi → Brightspace Core | Framework |
| `uses-product` | Customer used this product | SAIT → Performance Plus | Framework |
| `differentiates-from` | Shows competitive advantage | Our Analytics → Canvas Analytics | Architecture |
| `alternative-to` | Different approach to same problem | Competitor → Our Product | Architecture |
| `prerequisite` | Should read this first | Ontology → Advanced Topic | Template |
| `related-to` | General relevance (avoid) | - | (Don't use) |

### By Pattern

| Pattern | Relationships | Example | Read |
|---------|---------------|---------|------|
| Problem → Solution | solves-problem | Use Case → Product | Architecture 1 |
| Solution → Proof | uses-product, demonstrates-outcome | Product → Story → Outcome | Architecture 1 |
| Persona Journey | validates-context, raises-concern, addresses-concern, finds-proof | Persona → Playbook → Objection → Counter → Proof | Architecture 2 |
| Proof Diversity | demonstrates-outcome (×3+) | Outcome ← Stories (3+ industries) | Architecture 3 |
| Competitive Advantage | enables, differentiates-from | Feature → Outcome → Competitive Card | Architecture 4 |
| Multi-Product Solution | solves-problem (×2+) | Use Case → Product A + B + C → Proof | Architecture 5 |

---

## Key Insights by Document

### Relationship Framework
✓ Why relationships matter (facts vs. arguments)  
✓ 5 core patterns and when to use them  
✓ How to implement relationships  
✓ Relationship taxonomy with examples

### Insight Catalyst Matrix
✓ 8 areas where connections create value  
✓ Your vault's specific gaps (which outcomes need proof)  
✓ Priority connections ranked by impact  
✓ Missing content flagged (association playbook, healthcare, etc.)

### Relationship Mapping Template
✓ YAML frontmatter fields (related_notes, see_also, context_hints)  
✓ Step-by-step process for adding relationships  
✓ 5 common patterns with complete examples  
✓ Validation checklist

### Relationship Quick-Start
✓ 30 prioritized connections (no new content needed)  
✓ 10 quick wins (30 min, high impact)  
✓ 3-week implementation timeline  
✓ Measurement criteria

### Relationship Architecture
✓ 7 visual connection patterns  
✓ How relationships turn facts into insights  
✓ Current state vs. target relationship density  
✓ Quick architecture health check for any note

---

## Measurement: Am I Doing This Right?

### After Week 1
✓ All customer stories have 4+ relationships  
✓ All personas have 5+ relationships  
✓ All objections link to counter-arguments  
✓ Random note check: Can follow 3-4 wikilinks and learn something new?

### After Week 2
✓ Each outcome has 3+ customer proof links  
✓ Each product links to customer proof + competitive position  
✓ Persona journeys are complete (context → concern → counter → proof)  
✓ Competitive differentiation chains show feature → advantage

### Long-term Success
✓ Salespeople report: "Can find answer paths to questions"  
✓ Content creators report: "It's clear what content gaps exist"  
✓ Leaders report: "Can see which outcomes have strongest proof"  
✓ Readers report: "Easy to navigate between related notes"

---

## Quick Help Reference

### "How do I add a relationship?"
→ Read [[Relationship Mapping Template]] (5-step process)

### "What relationships should this note have?"
→ Find your note type in [[Relationship Architecture]] (section: "Relationship Patterns by Note Type")

### "What's the highest-impact connection to add next?"
→ Check [[Relationship Quick-Start]] (Priority 1 list)

### "What's missing from my vault?"
→ Read [[Insight Catalyst Matrix]] (Gap Analysis section)

### "How do I validate my relationships are good?"
→ Use checklist in [[Relationship Mapping Template]] (Validation section)

### "What does a complete relationship look like?"
→ See [[Relationship Mapping Template]] (5 complete examples)

### "How should I structure YAML frontmatter?"
→ Copy from [[Relationship Mapping Template]] (Frontmatter section)

---

## Files Created

All documents in: `LLM-WIKI D2L/Dashboards/` and `LLM-WIKI D2L/templates/`

**Dashboards folder:**
- Relationships - START HERE.md (entry point)
- Relationship Framework.md (theory)
- Insight Catalyst Matrix.md (strategy)
- Relationship Architecture.md (visual patterns)
- Relationship Quick-Start.md (action list)
- Relationship Resources Index.md (this file)

**Templates folder:**
- Relationship Mapping Template.md (how-to guide)

---

## Timeline: 30-Day Impact

**Week 1:** Foundation (6-8 hours)
→ Basic relationship network in place

**Week 2:** Enhancement (4-5 hours)
→ Proof density built; competitive advantage clear

**Week 3:** Gaps & Strategy (3-4 hours)
→ Content priorities identified; gaps flagged

**Week 4+:** Continuous Improvement (1-2 hours/week)
→ New notes connect immediately; quarterly reviews

**30-Day Total:** 20-25 hours of active work  
**Payoff:** Insight paths that answer real questions; strategic clarity on proof gaps

---

## Support & Updates

**Have questions?**
- See "Quick Help Reference" above
- Check document that answers your specific need

**Want to improve this framework?**
- This is your knowledge system—customize as needed
- Add domains specific to your work
- Create additional patterns as you discover them

**Found gaps?**
- Update [[Insight Catalyst Matrix]] with new gaps
- Flag as content priorities
- These become your content roadmap

---

**Version:** 1.0  
**Created:** 2026-08-02  
**Last Updated:** 2026-08-02  
**See Also:** [[Navigation Hub - Start Here]], [[Knowledge Graph]], [[Dashboards/VAULT DASHBOARD]]

---

## Next Steps

1. **Today:** Open [[Relationships - START HERE]]
2. **This Week:** Follow the roadmap (6-8 hours)
3. **Week 2:** Enhance and expand (4-5 hours)
4. **Ongoing:** Continuous improvement

You're building a knowledge system that scales. Start now.
