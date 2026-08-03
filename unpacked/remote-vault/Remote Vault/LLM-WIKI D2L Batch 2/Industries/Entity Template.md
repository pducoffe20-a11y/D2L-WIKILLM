---
id: template-entity-customer
title: "Entity Template - Customer/Product/Industry"
type: template
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [template, ontology/template, entity/template]
category: template
see_also:
  - "00-System/SCHEMA.md"
  - "templates/Standard Note Template.md"
  - "templates/MOC Template.md"
---

# {{Entity Name}}

> {{One-line description of entity}}

---

## Quick Facts

| Property | Value |
|----------|-------|
| **Type** | Customer / Product / Industry / Use Case |
| **Status** | Active / Prospect / Archived |
| **Added** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Key Contact** | {{Name}} ({{Title}}) |

---

## Overview

[2-3 sentence overview of this entity and why it matters in our knowledge base]

### Key Information

- **Description**: {{Detailed description}}
- **Size/Scale**: {{Details}}
- **Location/Context**: {{Details}}
- **Key Metrics**: {{Key numbers or statistics}}

---

## Related Connections

### Belongs To
- Industry: [[Industry Name]]
- Segment: [[Segment Name]]
- Geography: [[Region Name]]

### Relationships

#### For Customer Entities:
- **Uses Products**: [[Product 1]], [[Product 2]]
- **Implements Use Cases**: [[Use Case 1]], [[Use Case 2]]
- **Case Studies**: [[Case Study 1]], [[Case Study 2]]
- **Contact**: [[Contact Name]]

#### For Product Entities:
- **Capabilities**: [[Capability 1]], [[Capability 2]]
- **Customer Base**: [[Customer 1]], [[Customer 2]]
- **Use Cases**: [[Use Case 1]], [[Use Case 2]]
- **Competitors**: [[Competitor 1]], [[Competitor 2]]
- **Owned by**: [[D2L / Division Name]]

#### For Industry Entities:
- **Key Players**: [[Customer 1]], [[Customer 2]]
- **Typical Use Cases**: [[Use Case 1]], [[Use Case 2]]
- **Relevant Products**: [[Product 1]], [[Product 2]]
- **Market Research**: [[Market Analysis]]

#### For Use Case Entities:
- **Industries**: [[Industry 1]], [[Industry 2]]
- **Products That Enable**: [[Product 1]], [[Product 2]]
- **Customer Examples**: [[Customer 1]], [[Customer 2]]
- **Related Use Cases**: [[Related Use Case 1]]

---

## Detailed Information

### Background

[Detailed background information about this entity]

### Key Characteristics

- Characteristic 1: {{Details}}
- Characteristic 2: {{Details}}
- Characteristic 3: {{Details}}

### Market Position / Capabilities / Outcomes

[Section depends on entity type - customize as needed]

---

## Notable Examples & Stories

### Example 1: [Title]
- **Relevance**: {{Why this example matters}}
- **Details**: {{Key points}}
- **Related Notes**: [[Related Note 1]], [[Related Note 2]]

### Example 2: [Title]
- **Relevance**: {{Why this example matters}}
- **Details**: {{Key points}}
- **Related Notes**: [[Related Note 1]]

---

## Competitive Context

[If relevant to the entity type]

### Market Alternatives
- [[Alternative 1]] - {{How it differs}}
- [[Alternative 2]] - {{How it differs}}

### Differentiation
- {{Unique aspect 1}}
- {{Unique aspect 2}}
- {{Unique aspect 3}}

---

## Research & References

### Primary Sources
- [Source 1: Title](https://example.com)
- [Source 2: Title](https://example.com)

### Secondary Resources
- [[Internal Research Note]]
- [[Related Documentation]]

### External Links
- [Company Website](https://example.com)
- [Market Report](https://example.com)

---

## Metadata

| Property | Value |
|----------|-------|
| **Type** | Customer / Product / Industry / Use Case |
| **Category** | [Specific classification] |
| **Tags** | {{tag1}}, {{tag2}}, {{tag3}} |
| **Related Entities** | {{5-10 related entities}} |
| **Confidence Level** | High / Medium / Low |
| **Information Currency** | Current / Dated / Needs Review |
| **Last Verified** | {{YYYY-MM-DD}} |

---

## Notes for AI Processing

**Context Hints**:
- {{Hint about how to use this information}}
- {{Special considerations}}

**Relevance Score**: {{0.0 - 1.0}}

**Use in Queries**: This entity is useful when researching {{topics}}.

---

## Template Instructions

When creating an entity note using this template:

1. **Update frontmatter**:
   - Set unique `id` (e.g., `customer-acme-001`)
   - Set `type: entity`
   - Set `category` to the entity type (customer, product, industry, usecase)
   - Add hierarchical tags (e.g., `customer/industry/higher-ed`)
   - Fill `linked_entities` array with related entities and relationships

2. **Quick Facts Table**: Fill in all relevant properties for this entity

3. **Overview Section**:
   - Write clear, concise description
   - Add 3-5 key information points
   - Keep it AI-scannable

4. **Related Connections**:
   - Choose relevant subsection(s) for your entity type
   - Link to all related entities
   - Use wikilink syntax: `[[path/to/Entity.md]]`

5. **Detailed Information**:
   - Provide substantive information specific to this entity
   - Organize into logical subsections
   - Keep language clear for AI processing

6. **Examples & Stories**:
   - Add 2-3 key examples or stories
   - Link to supporting notes
   - Explain relevance

7. **Metadata**:
   - Keep metadata table updated
   - Update "Last Verified" date regularly
   - Set "Information Currency" status

**For AI Memory Layer**: 
- Add `content_summary` in frontmatter (1-2 sentences)
- Use `context_hints` for special processing needs
- Keep `linked_entities` comprehensive and accurate
- Set appropriate `confidentiality` level

---

**See Also**: 
- [[00-System/SCHEMA.md]] - Complete schema documentation
- [[Ontology/MOCs/MOCs.md]] - MOC methodology

