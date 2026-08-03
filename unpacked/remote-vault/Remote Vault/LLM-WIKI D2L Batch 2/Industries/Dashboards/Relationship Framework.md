---
id: framework-relationships
title: Relationship Framework - Building Knowledge Connections
type: framework
status: active
created: 2026-08-02
updated: 2026-08-02
tags:
  - ontology/framework
  - navigation/connections
  - system/knowledge-architecture
  - ai/context/retrieval
see_also:
  - Ontology/MOCs/MOCs.md
  - Navigation Hub - Start Here
  - Knowledge Graph
  - Dashboards/Insight Catalyst Matrix
---

# Relationship Framework: Building Insight Connections

The vault contains 372 notes across 9 major domains. **Only 16% have explicit relationships defined.** This framework builds bridges that turn scattered facts into actionable insights.

## Why Relationships Matter

**Without connections:**
- A customer story is just a story
- A product feature is just a capability list
- An industry playbook is just background

**With connections:**
- A customer story + industry context = proof that the playbook works
- A feature + objection + customer outcome = a persuasive sales path
- An objection + business case + proof point = a complete rebuttal

## Core Relationship Types

### 1. **Problem → Solution** (Insight Ladder)
Links use cases to products that solve them.

**Pattern:**
- [[Use-Case]] describes a pain point
- [[Industry]] validates the pain is widespread  
- [[Product]] offers the solution
- [[Customer-Proof]] shows it works

**Example Chain:**
`Fragmented Learner Experience` → `Consistent Content Delivery` → `Brightspace Mobile and Pulse` → `York Technical College proof`

**How to use:** When someone asks "who faces this problem," follow the chain backward. When they ask "what solves it," follow forward.

---

### 2. **Persona → Context → Objection → Answer** (Sales Path)
Maps who cares about what, what they worry about, and how to address it.

**Pattern:**
- [[Persona]] has specific goals
- [[Industry Playbook]] provides context for that role
- [[Objection]] names their concern
- [[Business-Cases]] quantifies the ROI
- [[Customer-Proof]] shows peers solved it

**Example Chain:**
`CIO` → `Higher Education Playbook` → `Integration Risk` → `Value Model: Platform Consolidation` → `SAIT case study`

**How to use:** When preparing for a specific buyer type, start at the persona, understand their context, anticipate their objections, and gather proof.

---

### 3. **Outcome → Proof Diversity** (Verification Paths)
Shows that a claimed outcome is real through multiple, independent sources.

**Pattern:**
- [[Buyer-Outcomes]] claims value
- Multiple [[Customer-Proof]] notes demonstrate it independently
- [[Business-Cases]] quantifies it
- Multiple [[Industries]] show it's cross-vertical

**Example Chain:**
`Administrative Efficiency` proven by:
- AACSB (associations)
- Professional Development Institute (corporate)
- Singapore Polytechnic (higher ed)
- Cross-referenced with `Value Model: Administrative Efficiency`

**How to use:** When validating a claim, trace it across 3+ customer stories and 2+ industries. Stronger proof = stronger conviction.

---

### 4. **Product → Differentiation → Competitor** (Competitive Path)
Links what we do, why it matters, and how it differs.

**Pattern:**
- [[Product]] capability described
- [[Buyer-Outcomes]] explains the value
- [[Competitor Theme]] describes how others approach it
- [[Competitive Card]] shows side-by-side difference

**Example Chain:**
`Brightspace Core Positioning` → `Learner Engagement Visibility` → `Competitor Theme: Suite Platform` → `Competitive Card: Blackboard`

**How to use:** In competitive situations, show we solve the same problem differently (better).

---

### 5. **Gap → Priority → Source** (Content Planning)
Identifies what we don't know and what to research.

**Pattern:**
- [[Coverage Map]] shows what's documented
- Missing connections reveal gaps
- [[Review-Queue]] flags outdated content
- Priority list emerges from strategic questions

**Example Chain:**
"No connection between `Credentialing Workflow` and any Higher Ed proof" → Add Higher Ed credentialing case study → Creates new insight path

**How to use:** Missing relationships = content opportunities. Prioritize by strategic impact.

---

## Implementation: Adding Relationships

### Step 1: Identify the relationship type
Look at two notes. Which pattern does their connection fit?

### Step 2: Add frontmatter fields
Every note should have these optional fields:

```yaml
related_notes:
  - title: "Note Title"
    id: "note-id"
    relationship: "solves-problem"  # problem, context, proof, alternative, enables, contradicts
    why: "Explains the connection and why it matters"

see_also:
  - "[[Note Title]]"  # Quick reference without explanation

context_hints:
  - "This note assumes knowledge of [[Other Note]]"
  - "Combined with [[Another Note]], this shows..."

content_summary:
  connections: "3-5 word summary of how this connects to others"
```

### Step 3: Use wikilinks strategically
Wikilinks in note bodies create discoverable paths.

```markdown
This is relevant to [[Higher Education Playbook|higher-ed buyers]] because...
See also [[Proof Card - SAIT]] for similar results in a technical college.
This is one answer to the [[Learner Engagement Visibility|engagement challenge]].
```

### Step 4: Cross-reference in MOCs
Maps of Content should show relationship chains, not just lists.

```markdown
## From Problem to Proof

**If your buyer worries about:** Learner retention
**Start here:** [[Limited Learner Engagement Visibility]] (the problem)
**Consider this product:** [[Performance Plus Public Capabilities]] (the solution)
**For proof:** [[Proof Card - SAIT - Analytics-Led LMS Adoption]] (it works)
**For context:** [[Higher Education Playbook]] (why it matters in their world)
```

---

## Quick-Start: High-Impact Relationships

### Must-Have Connections (Add First)

1. **Each customer story** → industry + products used + use cases solved
2. **Each persona** → industries where this role exists + relevant objections
3. **Each objection** → business case that addresses it + customer proof that overcame it
4. **Each product** → customer proof using it + competitors with similar features
5. **Each industry playbook** → 3+ customer stories in that industry

### Creates These Insights

✓ "Which products solve *this specific problem*?"  
✓ "Who else in *this industry* solved *this challenge*?"  
✓ "What overcomes *this objection* with *proof*?"  
✓ "What's our advantage over *competitor X* on *this feature*?"  
✓ "What's the complete sales path for *this buyer type*?"

---

## Examples of Relationship Metadata

### Example 1: Customer Story with Rich Relationships
```yaml
related_notes:
  - title: "Higher Education Playbook"
    relationship: "validates-context"
    why: "SAIT is a technical college; this playbook explains their sector dynamics"
  
  - title: "Value Model - Administrative Efficiency"
    relationship: "demonstrates-outcome"
    why: "This story shows operational efficiency gains with specific time savings"
  
  - title: "Performance Plus Public Capabilities"
    relationship: "uses-product"
    why: "Analytics capabilities drove the LMS adoption success described"
  
  - title: "Objection - Administration Effort"
    relationship: "overcomes-objection"
    why: "Proof that admin effort was cut, not added, with Brightspace"

see_also:
  - "[[Proof Card - Singapore Polytechnic]]"  # Similar outcome in different region
  - "[[Buyer Outcomes - Analytics-Led Learning]]"  # The outcome this story validates
```

### Example 2: Product with Competitive Relationships
```yaml
related_notes:
  - title: "D2L Lumi Public Capabilities"
    relationship: "enables"
    why: "Lumi's AI capabilities enhance content authoring; core positioning includes this"
  
  - title: "Competitor Card - Canvas"
    relationship: "differentiates-from"
    why: "Canvas lacks native AI; our Lumi integration is differentiation"
  
  - title: "Creator Plus Public Capabilities"
    relationship: "complements"
    why: "Creator Plus handles course design; Lumi handles AI-assisted content"

context_hints:
  - "Brightspace Core is the foundation; Lumi is the AI layer"
  - "When Canvas is mentioned, note that they require third-party AI integration"
```

### Example 3: Objection with Resolution Path
```yaml
related_notes:
  - title: "Value Model: Platform Consolidation"
    relationship: "quantifies-counter-argument"
    why: "Addresses cost of maintaining multiple platforms vs. one integrated suite"
  
  - title: "Proof Card - AACSB"
    relationship: "demonstrates-resolution"
    why: "AACSB reduced process from 50 steps to few clicks through consolidation"
  
  - title: "CIO Persona"
    relationship: "raised-by"
    why: "Integration risk is typically a CIO concern during procurement"

see_also:
  - "[[Proof Card - Purdue Global]]"  # Another consolidation success
  - "[[Competitive Card - Blackboard]]"  # Alternative that doesn't consolidate as well
```

---

## Relationship Taxonomy

When adding `relationship` field, use these types:

| Type | Meaning | Example |
|------|---------|---------|
| `solves-problem` | Product solves use case | Brightspace → Learner Engagement |
| `validates-context` | Note provides context | Industry Playbook → Customer Story |
| `demonstrates-outcome` | Proof shows claimed value | Customer Story → Buyer Outcome |
| `overcomes-objection` | Proof that objection was resolved | Customer Story → Objection |
| `enables` | This enhances another capability | Lumi → Brightspace Core |
| `uses-product` | Customer used this product | SAIT → Performance Plus |
| `contradicts` | Note challenges this claim | Competitive Card → Product Claim |
| `related-to` | General relevance (avoid—be specific) | - |
| `prerequisite` | Should read this first | Ontology → Advanced Topic |
| `alternative-to` | Different approach to same problem | Competitor → Our Product |

---

## Surfacing Insights: Questions to Ask

Once relationships are mapped, ask these to find insights:

### Discovery Questions
- "Which products solve problems in this industry?" → product + industry connection
- "Who succeeded despite this objection?" → proof + objection connection
- "What does a typical buying journey look like for this persona?" → persona → playbook → use-case → product → proof
- "Where do we have proof gaps?" → missing connections

### Competitive Questions  
- "How do we differentiate on this feature vs. Competitor X?" → product → competitor
- "What can we claim that competitors can't back up with proof?" → product claim + proof diversity

### Content Planning
- "Which outcomes have minimal proof?" → buyer-outcome with few connected proof points
- "Which use-cases aren't connected to any product?" → use-case with no product relationships
- "Which industries have incomplete coverage?" → industry with few customer stories

---

## Next Steps

1. **Review existing relationships** — Check which notes already have `related_notes`
2. **Add missing relationships** — Focus on must-haves (customer stories, personas, objections)
3. **Test insight paths** — Follow a relationship chain and verify it answers a real sales question
4. **Iterate and refine** — Relationships will strengthen over time as content grows

---

**Version**: 1.0  
**Created**: 2026-08-02  
**See Also**: [[Insight Catalyst Matrix]], [[Knowledge Graph]], [[Ontology/MOCs/MOCs.md]]
