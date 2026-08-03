---
id: vault-schema-001
title: Vault Frontmatter Schema
type: documentation
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [ontology/metadata, navigation/core, ai/context]
category: system
---

# Standardized Vault Frontmatter Schema

This document defines the standardized metadata schema for all notes in this vault. Consistent frontmatter enables AI traversal, better search, and clearer content organization.

## Core Fields (Required for All Notes)

```yaml
id: unique-identifier-001
title: "Human-readable title"
type: "note|moc|entity|resource|template"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: "active|draft|archived|review"
```

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **id** | string | Unique identifier for the note | `customer-acme-001` |
| **title** | string | Human-readable title | `Acme Corp Case Study` |
| **type** | enum | Note category for AI parsing | `note`, `moc`, `entity`, `resource`, `template` |
| **created** | date | Creation date (YYYY-MM-DD) | `2026-08-02` |
| **updated** | date | Last modification date | `2026-08-02` |
| **status** | enum | Content maturity level | `active`, `draft`, `archived`, `review` |

## Navigation Fields (Recommended)

```yaml
parent_moc: "name-of-parent-map"
related_notes: 
  - id: related-note-id-001
    title: "Related Note Title"
  - id: related-note-id-002
    title: "Another Related Note"
see_also: 
  - "VAULT DASHBOARD"
  - "01-Products/MOC.md"
```

| Field | Type | Description | Use Case |
|-------|------|-------------|----------|
| **parent_moc** | string | Primary Map of Content this note belongs to | For notes in a topic, link back to their MOC |
| **related_notes** | array | List of related notes with id and title | Build bidirectional relationships |
| **see_also** | array | String references to related files | Quick cross-references |

## Taxonomy Fields (For Classification)

```yaml
tags: 
  - ontology/metadata
  - customer/industry/higher-ed
  - sales/stage/closed-won
  - product/suite/brightspace
category: "broad classification"
entities: 
  - type: "customer|product|industry|use-case"
    name: "Entity Name"
topics: [topic1, topic2]
```

| Field | Type | Description | Examples |
|-------|------|-------------|----------|
| **tags** | array | Hierarchical tags (category/subcategory/specific) | `customer/industry/higher-ed`, `sales/stage/discovery` |
| **category** | string | Broad classification for filtering | `customer`, `product`, `use-case`, `competitive-intel` |
| **entities** | array | Named entities mentioned in note | `{type: "customer", name: "Acme Corp"}` |
| **topics** | array | Key topics covered | `[assessment, onboarding, engagement]` |

## Relationships Fields (For Knowledge Graphs)

```yaml
linked_entities: 
  - type: "customer"
    name: "Acme Corp"
    relationship: "uses-products"
  - type: "product"
    name: "Brightspace Learning"
    relationship: "feature-benefit"
dependency_notes: 
  - "01-Products/Brightspace.md"
  - "03-Industries/Higher Education.md"
cross_references:
  - path: "05-Customer-Proof/Acme Corp Case Study.md"
    reason: "related-customer-story"
```

| Field | Type | Description | Relationship Types |
|-------|------|-------------|-------------------|
| **linked_entities** | array | Entities mentioned with relationships | `uses-products`, `implements-use-case`, `belongs-to-industry` |
| **dependency_notes** | array | Files that should be read for context | Use for prerequisite knowledge |
| **cross_references** | array | External references with reason | `related-customer-story`, `competitive-comparison` |

## AI Context Fields (For LLM Processing)

```yaml
context_hints: 
  - "This is a real customer success story"
  - "Focus on time-to-value metrics"
  - "Emphasizes remote work benefits"
relevance_score: 0.95
content_summary: "Brief 1-2 sentence summary of key points"
confidentiality: "public|internal|restricted"
ai_instructions: "Any special instructions for AI processing"
```

| Field | Type | Description | Notes |
|-------|------|-------------|-------|
| **context_hints** | array | Hints for AI to understand document context | `["real-customer", "recent-win", "similar-to-acme"]` |
| **relevance_score** | number (0-1) | Relevance for given query context | Set manually or via automated scoring |
| **content_summary** | string | Brief 1-2 sentence summary | For quick context in AI retrieval |
| **confidentiality** | enum | Access level for sharing | `public`, `internal`, `restricted` |
| **ai_instructions** | string | Special processing instructions for AI | E.g., "Treat as future-looking, not current state" |

## Field Usage by Note Type

### Standard Note
```yaml
id: ~
title: ~
type: note
created: ~
updated: ~
status: ~
tags: [...]
category: ~
parent_moc: ~
related_notes: [...]
entities: [...]
linked_entities: [...]
cross_references: [...]
```

### Map of Content (MOC)
```yaml
id: ~
title: ~
type: moc
created: ~
updated: ~
status: ~
tags: [ontology/moc, ...]
category: ~
related_notes: [...]  # Other MOCs
topics: [...]         # Topics covered
cross_references: [...]
ai_instructions: "Index of content on this topic"
```

### Entity (Customer/Product/Industry)
```yaml
id: ~
title: ~
type: entity
created: ~
updated: ~
status: ~
category: [customer|product|industry|use-case]
tags: [entity/type, ...]
linked_entities: [...]  # Related entities
dependency_notes: [...]
entities: 
  - type: self
    name: ~
topics: [...]
content_summary: "1-2 sentence description"
```

### Resource
```yaml
id: ~
title: ~
type: resource
created: ~
updated: ~
status: ~
tags: [resource/type, ...]
category: ~
confidentiality: ~
cross_references: [...]
```

## Tag Hierarchy

Tags should follow this hierarchy: `category/subcategory/specific`

### Customer Tags
- `customer/industry/higher-ed`
- `customer/industry/k12`
- `customer/industry/corporate`
- `customer/type/multi-story` (companies with multiple case studies)
- `customer/size/enterprise`

### Product Tags
- `product/suite/brightspace`
- `product/suite/edlink`
- `product/feature/assessment`
- `product/feature/engagement`
- `product/capability/lms`

### Sales Stage Tags
- `sales/stage/discovery`
- `sales/stage/evaluation`
- `sales/stage/negotiation`
- `sales/stage/closed-won`
- `sales/stage/renewal`

### Use Case Tags
- `usecase/area/learning-management`
- `usecase/area/assessment`
- `usecase/area/employee-training`
- `usecase/benefit/time-to-value`

### Organizational Tags
- `ontology/metadata` - Schema and documentation
- `ontology/moc` - Maps of Content
- `navigation/core` - Core navigation documents
- `ai/context` - AI processing hints

## Minimal Example

A minimal note following this schema:

```yaml
---
id: note-20260802-001
title: "Quick Example Note"
type: note
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [example]
category: documentation
related_notes:
  - id: vault-schema-001
    title: "Vault Frontmatter Schema"
---

# Quick Example Note

Your content here...
```

## Implementation Guidelines

1. **Phased Adoption**: Start with core fields (id, title, type, created, updated, status) across all notes
2. **Priority Sequence**: 
   - Tier 1: Core fields (required immediately)
   - Tier 2: Navigation and Taxonomy fields (week 1-2)
   - Tier 3: Relationships fields (week 2-3)
   - Tier 4: AI context fields (week 3-4)

3. **Validation**: Use dataview queries to check schema compliance:
   - Missing required fields
   - Invalid type values
   - Malformed dates
   - Broken related_notes references

4. **Maintenance**: Review schema quarterly for additions based on vault evolution

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative
