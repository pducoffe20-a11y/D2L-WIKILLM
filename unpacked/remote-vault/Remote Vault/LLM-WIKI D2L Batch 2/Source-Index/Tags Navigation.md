---
id: ontology-tag-hierarchy
title: "Tag Hierarchy & Taxonomy"
type: documentation
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [ontology/metadata, ontology/taxonomy, navigation/core]
category: system
related_notes:
  - id: vault-schema-001
    title: "Vault Frontmatter Schema"
see_also:
  - "00-System/SCHEMA.md"
  - "Ontology/Tag Index.md"
---

# Tag Hierarchy & Taxonomy

This document defines the hierarchical tag structure used throughout the vault. Consistent tag usage enables:
- Semantic classification for AI understanding
- Browse-by-category navigation
- Related content discovery
- Powerful search filtering
- Structured taxonomy for machine learning

## Tag Hierarchy Rules

All tags follow this pattern: **`category/subcategory/specific`**

- **Category**: Broad classification (e.g., `customer`, `product`, `entity`)
- **Subcategory**: More specific classification (e.g., `industry`, `feature`, `type`)
- **Specific**: Most granular level (e.g., `higher-ed`, `assessment`, `case-study`)

### Levels
- **1-level tags** (category): `entity`, `ontology`, `navigation`
- **2-level tags** (category/subcategory): `customer/industry`, `product/suite`
- **3-level tags** (category/subcategory/specific): `customer/industry/higher-ed`

**Best practice**: Use the most specific tag available.

---

## Complete Tag Hierarchy

### ENTITY TAGS

Tags for marking entity types and classifications.

```
entity/
├── type/
│   ├── customer
│   ├── product
│   ├── industry
│   ├── use-case
│   ├── competitor
│   └── persona
├── customer/
│   ├── industry/
│   │   ├── higher-ed
│   │   ├── k12
│   │   ├── corporate
│   │   ├── healthcare
│   │   ├── government
│   │   └── nonprofit
│   ├── size/
│   │   ├── enterprise
│   │   ├── mid-market
│   │   └── smb
│   ├── type/
│   │   ├── multi-story
│   │   ├── new-customer
│   │   ├── expansion
│   │   └── renewal
│   └── region/
│       ├── north-america
│       ├── emea
│       ├── apac
│       └── latam
├── product/
│   ├── suite/
│   │   ├── brightspace-learning
│   │   ├── brightspace-colleague
│   │   ├── brightspace-ledger
│   │   └── edlink
│   ├── feature/
│   │   ├── assessment
│   │   ├── engagement
│   │   ├── analytics
│   │   ├── collaboration
│   │   └── reporting
│   ├── capability/
│   │   ├── lms
│   │   ├── erp
│   │   ├── mobile
│   │   ├── api
│   │   └── integration
│   └── component/
│       ├── mobile-app
│       ├── web-interface
│       ├── api-gateway
│       └── data-warehouse
├── industry/
│   ├── higher-ed
│   ├── k12
│   ├── corporate
│   ├── healthcare
│   ├── government
│   └── nonprofit
├── use-case/
│   ├── area/
│   │   ├── learning-management
│   │   ├── assessment
│   │   ├── engagement
│   │   ├── analytics
│   │   ├── training
│   │   ├── compliance
│   │   └── performance-management
│   └── benefit/
│       ├── time-to-value
│       ├── engagement-improvement
│       ├── cost-reduction
│       ├── efficiency-gains
│       └── outcome-improvement
├── competitor/
│   ├── blackboard
│   ├── moodle
│   ├── canvas
│   ├── schoology
│   └── other-lms
└── persona/
    ├── role/
    │   ├── c-suite
    │   ├── department-head
    │   ├── instructor
    │   ├── learner
    │   └── administrator
    └── seniority/
        ├── executive
        ├── manager
        └── individual-contributor
```

---

### CONTENT TYPE TAGS

Tags for marking content type and purpose.

```
content/
├── type/
│   ├── case-study
│   ├── guide
│   ├── research
│   ├── competitive-analysis
│   ├── product-brief
│   ├── use-case-guide
│   ├── template
│   └── resource
├── format/
│   ├── narrative
│   ├── data-driven
│   ├── visual
│   ├── interactive
│   └── reference
├── audience/
│   ├── sales
│   ├── sales-engineer
│   ├── product
│   ├── marketing
│   └── customer-success
└── use-case/
    ├── prospecting
    ├── qualification
    ├── negotiation
    ├── deal-support
    ├── rfp-response
    └── customer-retention
```

---

### SALES STAGE TAGS

Tags for marking content by sales stage and process.

```
sales/
├── stage/
│   ├── discovery
│   ├── qualification
│   ├── evaluation
│   ├── negotiation
│   ├── closed-won
│   ├── closed-lost
│   └── renewal
├── activity/
│   ├── prospecting
│   ├── outreach
│   ├── needs-analysis
│   ├── proposal
│   ├── demo
│   └── negotiation
├── outcome/
│   ├── successful-implementation
│   ├── faster-adoption
│   ├── expansion
│   ├── reduced-churn
│   └── higher-satisfaction
└── process/
    ├── buying-committee
    ├── rfp-process
    ├── poc
    ├── implementation
    └── adoption
```

---

### ONTOLOGY & SYSTEM TAGS

Tags for metadata, structure, and system content.

```
ontology/
├── metadata/
│   ├── schema
│   ├── taxonomy
│   ├── relationships
│   └── frontmatter
├── moc/
│   ├── map-of-content
│   ├── topic-index
│   └── navigation-hub
├── template/
│   ├── note-template
│   ├── entity-template
│   └── moc-template
├── methodology/
│   ├── structure
│   ├── principles
│   └── best-practices
└── system/
    ├── configuration
    ├── documentation
    └── maintenance

navigation/
├── core/
│   ├── dashboard
│   ├── hub
│   └── index
├── pathway/
│   ├── learning-path
│   ├── sales-path
│   └── research-path
├── relationship/
│   ├── connections
│   ├── graph
│   └── traversal
└── discovery/
    ├── search
    ├── browse
    └── exploration
```

---

### AI & CONTEXT TAGS

Tags for AI memory layer and processing hints.

```
ai/
├── context/
│   ├── retrieval-optimization
│   ├── relationship-mapping
│   ├── entity-extraction
│   └── semantic-search
├── processing/
│   ├── high-priority
│   ├── low-priority
│   ├── needs-summarization
│   └── relationship-rich
├── confidence/
│   ├── high-confidence
│   ├── medium-confidence
│   └── low-confidence
├── recency/
│   ├── current
│   ├── recent
│   ├── dated
│   └── archived
└── quality/
    ├── comprehensive
    ├── partial
    ├── sparse
    └── needs-expansion
```

---

### METADATA QUALITY TAGS

Tags tracking content status and review needs.

```
status/
├── active
├── draft
├── review-needed
├── outdated
└── archived

quality/
├── complete
├── comprehensive
├── partial
├── sparse
└── stub

review/
├── current
├── needs-update
├── needs-verification
├── accuracy-check
└── refresh-scheduled

maintenance/
├── recent-update
├── stale-content
├── broken-links
└── incomplete-metadata
```

---

## Tag Usage Guidelines

### Apply Multiple Tags

Notes should typically have 3-5 tags:
- **One type tag** (entity/type, content/type, or sales/stage)
- **One classification tag** (what it's about)
- **One or two context tags** (for navigation or AI processing)
- **Optional**: quality or status tags

### Example Tag Sets

**Case Study Note**:
```yaml
tags:
  - entity/customer
  - entity/customer/industry/higher-ed
  - content/type/case-study
  - sales/stage/closed-won
  - ai/context/high-priority
```

**Product Feature Documentation**:
```yaml
tags:
  - entity/product
  - entity/product/suite/brightspace-learning
  - entity/product/feature/assessment
  - content/type/product-brief
  - ontology/documentation
```

**Competitive Analysis**:
```yaml
tags:
  - entity/competitor
  - entity/competitor/blackboard
  - content/type/competitive-analysis
  - sales/activity/prospecting
  - ai/context/retrieval-optimization
```

**Use Case Guide**:
```yaml
tags:
  - entity/use-case
  - entity/use-case/area/assessment
  - entity/use-case/benefit/outcome-improvement
  - content/type/use-case-guide
  - navigation/pathway/sales-path
```

### Avoid These Mistakes

❌ Don't use vague single-word tags: `sales`, `customer`, `important`  
✅ Instead use hierarchical tags: `sales/stage/closed-won`, `entity/customer`, `ai/context/high-priority`

❌ Don't create custom tags that don't fit hierarchy  
✅ Use only tags from this defined hierarchy

❌ Don't tag everything with all possible tags  
✅ Select 3-5 most relevant tags

❌ Don't ignore AI/navigation tags for discovery  
✅ Include navigation and AI context tags for better retrieval

---

## Dynamic Tag Index

See [[Ontology/Tag Index.md]] for a dataview-generated index of all tags with usage counts.

---

## Tag-Based Navigation in Omnisearch

Use omnisearch with tag syntax to find content:

```
tag:entity/customer/industry/higher-ed
tag:sales/stage/closed-won
tag:content/type/case-study
tag:ai/context/retrieval-optimization
```

Combine multiple tags:
```
tag:entity/product tag:entity/product/feature/assessment
tag:entity/use-case tag:sales/stage/evaluation
```

---

## Tag Maintenance & Evolution

### Adding New Tags

Only add new tags if they represent a distinct category not covered by existing tags.

**Process**:
1. Verify it fits into an existing hierarchy
2. Document in this file
3. Add to [[Ontology/Tag Index.md]]
4. Use in appropriate notes
5. Review quarterly to ensure utility

### Deprecating Tags

When a tag becomes obsolete:
1. Document the deprecation
2. Migrate notes to new tag
3. Keep old tag for 3 months for backward compatibility
4. Remove from active use

### Quarterly Review

Each quarter:
- Review tag usage statistics
- Identify unused tags for potential removal
- Identify new categories needed
- Update this documentation

---

## Tag Usage Statistics

See [[Ontology/Tag Index.md]] for:
- Count of notes per tag
- Most commonly used tags
- Unused tags (candidates for removal)
- Emerging tag patterns

---

## Integration with Metadata Schema

Tags are part of the vault's standardized metadata (see [[00-System/SCHEMA.md]]):

```yaml
tags: 
  - entity/customer
  - entity/customer/industry/higher-ed
  - sales/stage/closed-won
  - content/type/case-study
```

All notes should have tags from this hierarchy.

---

## For AI Memory Layer

**How AI uses tags**:

1. **Semantic Clustering**: Similar tags group related content
2. **Context Enrichment**: Tags provide semantic hints for better retrieval
3. **Relevance Scoring**: Tag match contributes to retrieval ranking
4. **Entity Recognition**: Entity tags help identify note types and cross-references
5. **Relationship Mapping**: Tags reveal how content relates to other content

**Best Practices for AI**:
- Always include hierarchical tags (full path: `entity/type/specific`)
- Include `ai/context/*` tags for retrieval optimization
- Use entity tags to enable relationship inference
- Keep tags consistent across related notes

---

## Quick Reference by Use Case

### For Sales Users
Use these tags: `sales/stage/*`, `sales/activity/*`, `entity/customer/*`, `entity/use-case/*`

### For Content Creators
Use these tags: `content/type/*`, `ontology/template`, `status/draft`

### For Competitive Intelligence
Use these tags: `entity/competitor/*`, `sales/outcome/*`, `content/type/competitive-analysis`

### For Product Team
Use these tags: `entity/product/*`, `entity/use-case/*`, `content/type/product-brief`

### For AI Processing
Use these tags: `ai/context/*`, `ai/processing/*`, `entity/*` (for structure)

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative  
**See Also**: [[00-System/SCHEMA.md]] | [[Ontology/Tag Index.md]]

