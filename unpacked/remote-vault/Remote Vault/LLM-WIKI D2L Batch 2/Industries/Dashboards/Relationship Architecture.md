---
id: relationship-architecture
title: Relationship Architecture - Visual Guide
type: framework
status: active
created: 2026-08-02
updated: 2026-08-02
tags:
  - ontology/framework
  - navigation/visual
  - system/architecture
see_also:
  - Relationship Framework
  - Knowledge Graph
  - Insight Catalyst Matrix
---

# Relationship Architecture: Visual Guide

This page shows **how different types of notes connect** and what insights emerge from their combinations.

---

## Architecture 1: Problem → Solution → Proof

The strongest insight path. Shows a problem is real, solvable, and solved by our product.

```
USE CASE (Problem)
    ↓
PRODUCT (Solution)
    ↓
CUSTOMER PROOF (Evidence)
    ↓
BUYER OUTCOME (Validated Benefit)

Example path:
"Learner Engagement Visibility" (use-case)
    ↓ solves-problem
"Performance Plus" (product)
    ↓ uses-product
"SAIT Analytics-Led LMS Adoption" (proof)
    ↓ demonstrates-outcome
"Engagement Improvement Through Analytics" (outcome)

Insight: "This is a real, solvable, proven outcome"
```

### Adding Depth: Context Layer

```
USE CASE
    ↓
INDUSTRY PLAYBOOK ← (validates-context)
    ↓
PRODUCT
    ↓
CUSTOMER PROOF
    ↓
BUYER OUTCOME

Example:
"Low Engagement Visibility" (use-case)
    ↓
"Higher Education Playbook" (explains why this matters in higher ed)
    ↓
"Performance Plus" (solution)
    ↓
"SAIT" (proof in education context)
    ↓
"Analytics-Driven Engagement" (outcome)

Insight: "This specific use case matters in this industry; proof exists there"
```

---

## Architecture 2: Persona Journey (Sales Path)

Shows who cares about what, what they worry about, and how to address it.

```
PERSONA
    ↓ validates-context
INDUSTRY PLAYBOOK
    ↓ raises-concern
OBJECTION
    ↓ addresses-concern
VALUE MODEL
    ↓ finds-proof
CUSTOMER PROOF (same industry/role)
    ↓ demonstrates
BUYER OUTCOME

Example (CIO at Higher Ed):
"CIO" (persona)
    ↓
"Higher Education Playbook" (CIO's context)
    ↓
"Integration Risk" (what CIOs worry about)
    ↓
"Platform Consolidation Value Model" (quantified counter)
    ↓
"Purdue Global" (CIO succeeded with consolidation)
    ↓
"Platform Integration Success" (proven outcome)

Insight: "Here's a complete conversation script for this buyer type"
```

---

## Architecture 3: Outcome Validation (Proof Diversity)

Shows an outcome is credible through multiple, independent sources.

```
BUYER OUTCOME
    ├─ demonstrates-outcome → CUSTOMER PROOF 1 (Industry A)
    ├─ demonstrates-outcome → CUSTOMER PROOF 2 (Industry B)
    ├─ demonstrates-outcome → CUSTOMER PROOF 3 (Industry C)
    └─ addresses-concern → VALUE MODEL (Quantified proof)

Example (Administrative Efficiency):
"Administrative Efficiency Outcome"
    ├─ AACSB (Associations: 50-step process → clicks)
    ├─ PDI (Corporate: days of work saved)
    ├─ Singapore Poly (International: automation gains)
    └─ Value Model: Admin Efficiency (ROI calculation)

Insight: "This outcome is real, cross-vertical, and quantified"
Strength: HIGH [3+ proofs across industries]
```

---

## Architecture 4: Competitive Differentiation Chain

Shows feature → proof → advantage in a structured way.

```
PRODUCT CAPABILITY
    ├─ enables → BUYER OUTCOME
    ├─ proof → CUSTOMER PROOF
    ├─ vs. COMPETITOR CARD
    └─ differentiates-from → COMPETITIVE ADVANTAGE

Example (Analytics):
"Performance Plus Analytics"
    ├─ enables "Learner Engagement Improvement"
    ├─ proof "SAIT Case Study" (chose us for this)
    ├─ vs. "Blackboard Analytics"
    └─ difference: "Predictive vs. Retrospective"

Insight: "We don't just have feature X; we have better X with proof"
```

---

## Architecture 5: Multi-Product Solution Path

Shows how multiple products work together to solve a complex problem.

```
USE CASE (Complex Problem)
    ├─ solves → PRODUCT A (Part of solution)
    ├─ solves → PRODUCT B (Another part)
    ├─ solves → PRODUCT C (Integrates them)
    └─ together → CUSTOMER PROOF (Complete solution)

Example (Consistent Delivery Across Modalities):
"Consistent Course Delivery" (use-case)
    ├─ Brightspace Core (centralized design)
    ├─ Brightspace Mobile (on-the-go access)
    ├─ Brightspace Pulse (engagement tracking)
    └─ York Tech story (implemented all three for success)

Insight: "This complex problem has a complete solution; proof exists"
```

---

## Architecture 6: Gap Discovery Pattern

Shows where relationships DON'T exist—revealing content needs.

```
OUTCOME → (no customer proof in Industry X)
         → FLAG: Need proof in this industry

OBJECTION → (no value model addressing it)
          → FLAG: Need quantified counter-argument

USE CASE → (no product solving it)
         → FLAG: Need feature/product or positioning

PERSONA → (no industry playbook)
        → FLAG: Need industry-specific context

Example gaps to fill:
- "Global Scale Outcome" → Zero customer proof → Create international case study
- "Change Management Objection" → No proof → Target customer with transformation story
- "Revenue Growth Outcome" → 1 proof (MMI) → Need 2+ more
- "Association Learning Director" → No industry playbook → Create association playbook
```

---

## Architecture 7: The Complete Knowledge Graph

All architecture patterns interconnected:

```
                    INDUSTRY PLAYBOOK
                         ↑↓
    USE CASE ←→ PRODUCT ←→ PERSONA
        ↓         ↓         ↓
   OBJECTION ←→ VALUE MODEL
        ↓         ↓
   CUSTOMER PROOF ←→ BUYER OUTCOME
                ↓
        COMPETITIVE POSITION

Dense connections = rich knowledge
Sparse connections = content gaps

Example traversal:
Start: "I'm talking to a CIO"
  → PERSONA (CIO)
  → PLAYBOOK (Higher Ed context)
  → OBJECTION (Integration risk)
  → VALUE MODEL (Consolidation ROI)
  → PROOF (Purdue Global)
  → OUTCOME (Validated integration success)
  → COMPETITIVE (vs Blackboard)
  → USE CASE (Related challenges)

Result: Complete conversation framework
```

---

## Relationship Density: Current State vs. Target

### Current Relationship Density (Low)

```
CUSTOMER STORY
    └─ Maybe linked to industry
        (other 3+ connections missing)

PERSONA
    └─ Maybe linked to industry
        (journey incomplete)

OBJECTION
    └─ Standalone
        (no counter-arguments linked)

PRODUCT
    └─ Standalone
        (no proof, no competitive context)

OUTCOME
    └─ Standalone
        (few or no proofs linked)

Result: Notes are like isolated islands; hard to navigate
```

### Target Relationship Density (Rich)

```
CUSTOMER STORY
    ├─ Industry (validates context)
    ├─ 2-3 Products (shows what was used)
    ├─ 2-3 Outcomes (shows what was achieved)
    ├─ 1-2 Objections (shows what it overcame)
    └─ 1-2 Related stories (similar context)

PERSONA
    ├─ Industry playbook (their context)
    ├─ 3-5 Objections (their concerns)
    ├─ 3-5 Value models (counters to concerns)
    └─ 3+ Proofs (in their industry)

OBJECTION
    ├─ Value model (quantified counter)
    ├─ 3+ Customer proofs (overcame it)
    └─ 1-2 Methodologies (how we solve it)

PRODUCT
    ├─ 1-2 Outcomes (what value it creates)
    ├─ 3+ Customer proofs (who used it)
    ├─ Competitive cards (vs. alternatives)
    └─ Use cases (problems it solves)

OUTCOME
    ├─ 3+ Customer proofs (validated)
    ├─ Value model (quantified)
    ├─ 2+ Industries (cross-vertical)
    └─ Related outcomes (connections)

Result: Dense web; easy navigation; insights emerge
```

---

## Insight Generation: The Mechanics

### How Relationships → Insights

**No relationships:**  
"SAIT case study exists"  
→ A fact

**2-3 relationships:**  
"SAIT used Performance Plus; showed engagement improvement"  
→ Anecdote

**5+ relationships:**  
"SAIT (higher ed) used Performance Plus (analytics); achieved engagement improvement (outcome). Similar pattern in Singapore Poly. This outcome matters in higher-ed playbook. Overcomes learner adoption objection. Value model shows ROI."  
→ **Insight:** "Analytics-driven engagement is a validated, cross-vertical, profitable outcome for higher-ed institutions"

**Complete architecture:**  
Above + competitive context + persona journey + use case coverage + alternative solutions  
→ **Strategy:** "Here's our strongest proof point. Here's how to position it. Here's who to target. Here's how to overcome objections."

---

## Relationship Patterns by Note Type

### Customer Proof (Highest Connection Target)
Should have 4-6 outgoing relationships:
```
Customer Proof
├─ validates-context → Industry Playbook
├─ uses-product → Product(s)
├─ demonstrates-outcome → Outcome(s)
├─ overcomes-objection → Objection(s)
├─ related-to → Similar story (by industry/outcome)
└─ see_also → Complementary proof
```

### Persona (Must Have Complete Journey)
Should have 5-8 relationships:
```
Persona
├─ validates-context → Industry Playbook
├─ raises-concern → Objection 1
├─ raises-concern → Objection 2
├─ raises-concern → Objection 3
├─ addresses-concern → Value Model 1
├─ addresses-concern → Value Model 2
└─ finds-proof → Customer Proof (in their industry)
```

### Objection (Needs Resolution Path)
Should have 3-4 relationships:
```
Objection
├─ addresses-concern → Value Model
├─ overcomes → Customer Proof 1
├─ overcomes → Customer Proof 2
├─ overcomes → Customer Proof 3
└─ methodology → Implementation approach
```

### Product (Needs Value + Proof + Difference)
Should have 3-5 relationships:
```
Product
├─ solves-problem → Use Case(s)
├─ enables-outcome → Buyer Outcome(s)
├─ proof → Customer Proof 1
├─ proof → Customer Proof 2
├─ differentiates-from → Competitor Card
└─ complements → Related Product
```

### Outcome (Needs Proof Diversity)
Should have 4-6 relationships:
```
Outcome
├─ demonstrates → Customer Proof 1 (Industry A)
├─ demonstrates → Customer Proof 2 (Industry B)
├─ demonstrates → Customer Proof 3 (Industry C)
├─ quantified-by → Value Model
├─ addressed-by → Product(s)
└─ enabled-by → Capability/Feature
```

---

## Reading These Visualizations

**Arrow direction matters:**
- `→` = "is described by" or "is solved by"
- `←` = "applies to" or "is verified by"  
- `↔` = "mutually reinforce"

**Connection strength:**
- Single arrow = weak relationship (informational)
- Double arrow = strong relationship (causal/proof)
- Multiple arrows = complex relationship (multiple dimensions)

**Gaps (missing arrows):**
- Shows content needs or connection opportunities

---

## Quick Architecture Check

Use this to evaluate relationship health of any note:

```
This note has strong relationships if:

☑ Inbound relationships (other notes link to this)
☑ Outbound relationships (this links to others)
☑ Relationship descriptions explain WHY (not just THAT)
☑ At least 3 relationships pointing to diverse note types
☑ Clear insight emerges from combination

This note needs work if:

☐ Zero inbound/outbound relationships
☐ Only links to similar note types (all customers, all products)
☐ Vague descriptions ("related-to")
☐ <3 total relationships
☐ No clear insight emerges
```

---

## Next: Implement This

- **Week 1:** Add relationships following these architectures
- **Week 2:** Build out specific patterns (complete personas, diversify outcomes)
- **Week 3:** Fill gaps revealed by architecture review

→ Start at [[Relationships - START HERE]]

---

**Version:** 1.0  
**Created:** 2026-08-02  
**See Also:** [[Relationship Framework]], [[Insight Catalyst Matrix]], [[Relationship Quick-Start]]
