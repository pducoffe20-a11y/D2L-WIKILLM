---
id: template-relationship-mapping
title: Relationship Mapping Template
type: template
status: active
created: 2026-08-02
tags:
  - template/relationships
  - ontology/connections
  - system/metadata
---

# Relationship Mapping Template

Use this template when adding or enhancing relationships between notes. Copy the relevant sections into your note's frontmatter and body.

---

## Frontmatter Fields for Rich Relationships

Add these to your note's YAML frontmatter:

```yaml
---
# ... existing fields ...

# RELATIONSHIPS (select which apply)
related_notes:
  - title: "Related Note Title"
    id: "note-id-if-known"
    relationship: "[see taxonomy below]"
    why: "Specific explanation of how/why they connect and what insight it creates"
    
  - title: "Another Related Note"
    id: "note-id"
    relationship: "demonstrates-outcome"
    why: "This customer story shows the outcome claimed in that note"

# CONTEXT (optional but powerful)
see_also:
  - "[[Quick link without explanation]]"
  - "[[Particularly relevant for specific use cases]]"

context_hints:
  - "This note assumes you understand [[Prerequisite Note]]"
  - "Combined with [[Related Note]], this reveals..."
  - "Similar pattern in [[Comparable Note]]"

# CONTENT SUMMARY (for AI processing)
content_summary:
  key_entities:
    - entity_type: customer
      value: Organization Name
    - entity_type: industry
      value: Higher Education
    - entity_type: product
      value: Performance Plus
    - entity_type: outcome
      value: Administrative Efficiency
  
  connections: "Demonstrates effectiveness in [X] environment; suggests applicability to [Y]"
  gaps: "Doesn't address [X]; would pair well with [Y]"

---
```

---

## Relationship Taxonomy

Use one of these values for the `relationship` field:

### Problem-Solution Relationships
- `solves-problem`: Product/feature directly addresses this use case
- `enables`: This enhances or unlocks another capability
- `prerequisite`: Must understand/do this first

### Proof & Validation Relationships
- `demonstrates-outcome`: Customer story shows claimed value is real
- `overcomes-objection`: Proof that this objection was successfully handled
- `validates-context`: Provides context explaining why something matters
- `provides-evidence`: Source material or data backing up a claim

### Competitive Relationships
- `differentiates-from`: Shows how we're different/better than alternative
- `alternative-to`: Different approach to solving same problem
- `contradicts`: Challenges or disputes this claim

### General Relationships
- `related-to`: General relevance (use only if none above fit)

---

## Common Connection Patterns

### Pattern 1: Proof Point for an Outcome

**When:** You have a customer story and want to link it to a claimed buyer outcome.

```yaml
---
type: customer-proof
title: "SAIT - Analytics-Led LMS Adoption"

related_notes:
  - title: "Buyer Outcome: Analytics-Led Improvement in Engagement"
    relationship: "demonstrates-outcome"
    why: "SAIT's case shows measurable engagement improvement through analytics, proving this outcome is achievable in technical colleges"
  
  - title: "Performance Plus Public Capabilities"
    relationship: "uses-product"
    why: "Analytics-driven improvement was enabled by Performance Plus capabilities; link shows which feature created the value"
  
  - title: "Higher Education Playbook"
    relationship: "validates-context"
    why: "SAIT is a technical college fitting this playbook; context explains why this story is relevant to similar institutions"

see_also:
  - "[[Proof Card - Singapore Polytechnic]]"  # Similar outcome in different region
  - "[[Objection - Learner Adoption]]"  # This story overcomes this objection
---
```

### Pattern 2: Persona with Complete Sales Journey

**When:** You're mapping what a buyer cares about, their concerns, and how to address them.

```yaml
---
type: persona
title: "CIO"

related_notes:
  - title: "Higher Education Playbook"
    relationship: "validates-context"
    why: "CIOs in higher ed face specific platform and integration challenges; this playbook explains their operating environment"
  
  - title: "Objection - Integration Risk"
    relationship: "raises-concern"
    why: "Integration complexity is a CIO's primary concern during platform evaluation"
  
  - title: "Value Model - Platform Consolidation"
    relationship: "addresses-concern"
    why: "Directly quantifies the ROI of consolidation vs. maintaining multiple platforms—CIO's economic argument"
  
  - title: "Purdue Global - Platform Migration Case Study"
    relationship: "demonstrates-outcome"
    why: "Shows a successful consolidation from CIO perspective; proof that complexity can be managed"

context_hints:
  - "CIO decisions are driven by risk, cost, and reliability—use these three lenses"
  - "This persona's timeline: evaluate 6-9 months, implement 12-18 months"
  - "Key metric: cost per engaged user (combines licensing, support, and training)"
---
```

### Pattern 3: Product with Competitive Context

**When:** You're positioning a product and need to show differentiation.

```yaml
---
type: product
title: "D2L Lumi"

related_notes:
  - title: "Brightspace Core"
    relationship: "enhances"
    why: "Lumi is the AI layer on top of Brightspace; sells best when framed as integrated capability"
  
  - title: "Creator Plus"
    relationship: "complements"
    why: "Creator Plus handles course design; Lumi handles AI-assisted content creation—together they accelerate content creation"
  
  - title: "Competitor Card - Canvas"
    relationship: "differentiates-from"
    why: "Canvas AI is bolt-on and slower; our Lumi integration is native and faster—key selling point vs. Canvas"
  
  - title: "Buyer Outcome - Time to Content Launch"
    relationship: "enables"
    why: "AI-assisted content creation reduces time from weeks to days—Lumi is the enabler"

see_also:
  - "[[D2L Lumi Public Capabilities]]"
  - "[[Product and Solution Knowledge]]"

context_hints:
  - "Lumi sells strongest when tied to time savings and content quality"
  - "Common competitor positioning: 'We have AI too'—Counter: 'Integrated vs. bolt-on'"
---
```

### Pattern 4: Objection with Resolution Path

**When:** You're mapping how to handle a common buyer concern.

```yaml
---
type: objection
title: "Objection - Migration Risk"

related_notes:
  - title: "Implementation Lifecycle and Ownership"
    relationship: "provides-evidence"
    why: "Explains our structured migration methodology; addresses concern about chaos/disruption"
  
  - title: "[NEED: Customer migration success story]"
    relationship: "overcomes-objection"
    why: "Real example of successful migration from competitor platform"
  
  - title: "Services and Implementation Positioning"
    relationship: "enables-resolution"
    why: "Professional services take on migration risk; our guarantee structure addresses buyer concern"
  
  - title: "Change Management Consulting Positioning"
    relationship: "addresses-adoption"
    why: "Migration risk includes change management; our positioning shows we've solved this"

context_hints:
  - "This objection typically raised by: IT staff, instructional designers, faculty"
  - "Time-sensitive: most acute 6-12 months before implementation"
  - "Overcome with: proof (customer stories) + methodology + services guarantees"
---
```

### Pattern 5: Industry with Vertical Integration

**When:** You're showing how an industry's specific challenges map to solutions.

```yaml
---
type: industry-playbook
title: "Association Industry Playbook"

related_notes:
  - title: "Expanded Persona Coverage - Association Learning Director"
    relationship: "validates-context"
    why: "Specific roles in associations face these challenges; persona research confirms needs"
  
  - title: "Use Case - Credentialing Workflow Friction"
    relationship: "highlights-pain"
    why: "Associations particularly struggle with credential management at scale"
  
  - title: "AACSB - Competency Academy Launch"
    relationship: "demonstrates-outcome"
    why: "Shows how Brightspace enables association to launch credential programs"
  
  - title: "Money Management Institute - Professional Designation"
    relationship: "demonstrates-outcome"
    why: "Another association using D2L to scale professional credentials"
  
  - title: "Objection - Learner Adoption"
    relationship: "addresses-risk"
    why: "Associations worried about low adoption among busy professionals; these stories show high adoption"

see_also:
  - "[[Proof Card - AACSB]]"
  - "[[Proof Card - Money Management Institute]]"

context_hints:
  - "Associations have unique budget cycles (often annual memberships)"
  - "ROI is measured in credential currency and member retention, not hours saved"
  - "Key decision-makers: Executive Director, Learning Director, Tech Director"
---
```

---

## Step-by-Step: Adding Relationships to Existing Notes

### 1. Identify What This Note Relates To (5 min)

Ask yourself:
- What problem does this note address/solve?
- What evidence or proof supports this note?
- What personas/industries care about this?
- What would this note be stronger with?

### 2. Add Frontmatter Relationships (5 min)

For each relationship you identified:
- Find the related note's ID (or leave blank to add later)
- Choose the relationship type from taxonomy
- Write a 1-2 sentence explanation of WHY and WHAT INSIGHT it creates

**Quality check:** If you can't explain WHY in one sentence, the connection might be weak.

### 3. Add Wikilinks in Body (5 min)

In your note's body text, add [[wikilinks]] for key related notes.

**Best practices:**
- Link when relevant to the paragraph, not just random links
- Add a brief inline explanation if the connection isn't obvious
- Examples:
  ```markdown
  This outcome is similar to [[Buyer Outcome - Learner Retention]] but more specific to...
  
  See [[SAIT Case Study]] for proof this works in technical colleges.
  
  This is one way to address the [[Objection - Migration Risk]] concern.
  ```

### 4. Check Both Directions

If Note A links to Note B:
- Does Note B link back to Note A?
- If not, should it? (Usually yes)

Example:
- Customer Story links to Outcome: ✓  
- Outcome links back to Customer Story: ⚠️ Add reciprocal link

### 5. Update see_also and context_hints (3 min)

- **see_also:** Other notes worth reading alongside this
- **context_hints:** What should readers know before reading this?

---

## Validation Checklist

Before finishing, verify:

- [ ] Each `related_notes` entry has a clear "why" explanation
- [ ] Relationships use specific taxonomy (not "related-to")
- [ ] Wikilinks in body are relevant to context
- [ ] Reciprocal relationships exist where appropriate
- [ ] context_hints help readers understand prerequisites
- [ ] A reader could follow relationships and gain new insight

---

## Quick Examples

### Example 1: Two-Line Relationship
```yaml
related_notes:
  - title: "Higher Education Playbook"
    relationship: "validates-context"
    why: "SAIT is a technical college; this explains their strategic context"
```

### Example 2: Multi-Step Insight Chain
```yaml
related_notes:
  - title: "Learner Engagement Visibility Use Case"
    relationship: "solves-problem"
    why: "Performance Plus directly addresses this challenge"
  
  - title: "SAIT Case Study"
    relationship: "demonstrates-outcome"
    why: "Shows measurable engagement lift through analytics use"
  
  - title: "Performance Plus Public Capabilities"
    relationship: "enables"
    why: "Specific analytics features (predictive scoring, dashboards) created the outcome"
  
  - title: "Objection - Feature Parity with Competitors"
    relationship: "overcomes-objection"
    why: "SAIT chose us over Canvas specifically because our analytics were stronger"
```

Insight path: **Problem** → **Solution** → **Proof** → **Product** → **Competitive win**

---

## When to Stop Adding Relationships

✓ Add relationship when:
- It answers a real question someone might ask
- It creates a path from problem → solution → proof
- It provides necessary context
- It shows competitive advantage

✗ Skip relationship when:
- It's vague ("related-to everything")
- The connection requires 3+ steps of explanation
- It's duplicated by another, clearer relationship
- It's about the same topic but different scope (use hierarchy instead)

---

**Version**: 1.0  
**Created**: 2026-08-02  
**See Also**: [[Relationship Framework]], [[Insight Catalyst Matrix]]
