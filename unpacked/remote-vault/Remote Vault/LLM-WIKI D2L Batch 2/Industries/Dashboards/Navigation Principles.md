---
id: ontology-navigation-principles
title: Navigation Principles & Best Practices
type: documentation
created: 2026-08-02
updated: 2026-08-02
status: verified
tags:
  - navigation/principles
  - navigation/system
  - resource/reference
  - system/governance
category: system
related_notes:
  - id: vault-schema-001
    title: Vault Frontmatter Schema
  - id: ontology-tag-hierarchy
    title: Tag Hierarchy & Taxonomy
see_also:
  - 00-System/SCHEMA.md
  - Ontology/Tag Hierarchy.md
  - Navigation - MOC/00-Start Here.md---

# Navigation Principles & Best Practices

This document outlines the fundamental principles behind the vault's navigation system and best practices for effective information discovery and traversal.

---

## Core Navigation Principles

### 1. Multiple Pathways to Same Information

**Principle**: Knowledge should be discoverable through multiple navigation routes.

**Implementation**:
- A customer story should be findable by:
  - Customer name ([[Customer Story Navigator]])
  - Industry (via [[03-Industries/]] tags)
  - Products used (via [[MOC]] references)
  - Use cases implemented (via [[02-Use-Cases/]] tags)
  - Success metrics (via [[Navigation - MOC/Entity Relationships.md]])

**Why**: Different users think about information differently. Salesperson might think "industry," Product Manager might think "use case," Competitive analyst might think "competitor."

### 2. Explicit Over Implicit

**Principle**: Make relationships explicit via metadata rather than requiring readers to infer connections.

**Implementation**:
- Use `related_notes` frontmatter field to explicitly link related content
- Use `linked_entities` to encode entity relationships
- Use tags to mark entity types and classifications
- Add "Related Connections" sections to notes

**Why**: AI systems (and humans) can traverse explicit links easily. Implicit relationships are invisible to search and require reading entire documents.

### 3. Semantic Hierarchy

**Principle**: Organize by meaning/relationships, not just alphabetical or arbitrary grouping.

**Implementation**:
- Folder structure: `00-99` prefix represents business workflow stages
- MOCs: Organize by topic/domain rather than author or date
- Tags: Use 3-level hierarchy (category/subcategory/specific)
- Relationships: Connect by meaning (customer→industry, product→use-case)

**Why**: Semantic grouping helps both human browsing and AI inference.

### 4. Information Density with Traversal

**Principle**: Each note should be focused and complete, with easy traversal to related notes.

**Implementation**:
- Each note addresses one primary topic
- Related content accessed via wikilinks and metadata
- MOCs aggregate and organize related notes
- Navigation hubs provide entry points and pathway guidance

**Why**: Focused documents are easier to parse (for AI and humans) while links enable exploration without overwhelming a single document.

### 5. Progressive Disclosure

**Principle**: Start with essential information, make deeper dives available through navigation.

**Implementation**:
- MOCs provide overview and structure
- Summary sections provide quick context
- Detailed sections available for deep dives
- Links to related/dependent content
- Progressive navigation from simple to complex

**Why**: Allows quick lookup without requiring full document reading.

---

## Navigation Modes

### Mode 1: Structured Browse

**When to use**: You know what category you're looking for

**How it works**:
1. Start at relevant MOC or index ([[MOC]], [[03-Industries/]], etc.)
2. Browse organized list of contents
3. Click through to specific notes
4. Follow related links for deeper exploration

**Best For**: Learning, comprehensive overview, structured research

**Example**: "I want to understand all our Higher Ed customers"
1. Go to [[03-Industries/]]
2. Find Higher Education industry section
3. Browse customers in that industry
4. Read relevant case studies

### Mode 2: Tag Navigation

**When to use**: You want to find all content about a specific topic or classification

**How it works**:
1. Use omnisearch with tag syntax: `tag:entity/customer/industry/higher-ed`
2. Filter results to specific tag
3. Browse related content with same tag
4. Follow wikilinks to explore deeper

**Best For**: Categorical discovery, filtering, AI queries

**Example**: "Show me all corporate training content"
1. Search: `tag:entity/industry/corporate tag:entity/use-case/area/training`
2. Browse results
3. Click through to expand context

### Mode 3: Relationship Traversal

**When to use**: You're starting from one entity and want to find related entities

**How it works**:
1. Start from any note (customer, product, use case, industry)
2. Look at `related_notes` and `linked_entities` in frontmatter
3. Follow wikilinks to related content
4. Explore networks of connections

**Best For**: Discovering connections, gap analysis, context enrichment

**Example**: "What else should I know about this customer?"
1. Read customer case study
2. Check `linked_entities` for related products/industries
3. Follow links to product documentation
4. Check competitive context

### Mode 4: Pathway Navigation

**When to use**: You have a specific research goal or workflow

**How it works**:
1. Identify your goal (from [[Navigation - MOC/Content Pathways.md]])
2. Follow recommended sequence
3. Read materials in order
4. Build comprehensive understanding

**Best For**: Learning, preparation, structured research

**Example**: "I need customer proof for Higher Ed industry"
1. See [[Navigation - MOC/Content Pathways.md#Pathway 1: "I Need Customer Proof for a Prospect"]]
2. Follow Path A (industry-based)
3. Gather 2-3 representative customer stories
4. Extract key metrics

### Mode 5: Search-Driven Discovery

**When to use**: You have a specific topic or keyword in mind

**How it works**:
1. Use omnisearch to find notes containing term
2. Review results with emphasis on metadata
3. Follow tags and relationships
4. Browse related content

**Best For**: Quick lookups, specific information needs

**Example**: "Where's information about assessments?"
1. Search: "assessment"
2. Review search results
3. Follow highest-relevance results
4. Use tags to find related content

---

## Best Practices by Role

### For Sales Users

1. **Start with customer**: [[Customer Story Navigator]]
2. **Then explore related**:
   - Products they use: Go to [[MOC]]
   - Their industry: Go to [[03-Industries/]]
   - Competitive context: Go to [[06-Competitors/MOC.md]]
3. **Leverage pathways**: Use [[Navigation - MOC/Content Pathways.md]] for call prep
4. **Use tags**: Search by industry or product

**Quick wins**:
- Bookmark frequently used customer stories
- Use pathways for consistent call prep
- Follow "see also" links for broader context

### For Product Teams

1. **Start with products**: [[MOC]]
2. **Explore use cases**: [[02 - Use-Cases MOC]]
3. **See customer proof**: [[05-Customer-Proof/]] - Filter by relevant use cases
4. **Check competitive**: [[06-Competitors/MOC.md]]
5. **Review roadmap**: In product documentation

**Quick wins**:
- Track which use cases have customer examples
- Monitor adoption patterns from case studies
- Follow competitive positioning

### For Competitive Intelligence

1. **Start with competitors**: [[06-Competitors/MOC.md]]
2. **Understand each competitor**:
   - Features and capabilities
   - Customer base (find in [[05-Customer-Proof/]])
   - Industry focus
3. **Win-loss analysis**: Review customer stories for competitive mentions
4. **Positioning**: Check [[MOC]] for how we differentiate
5. **Identify gaps**: Use [[Navigation - MOC/Coverage Map.md]]

**Quick wins**:
- Create competitive feature matrix from [[MOC]]
- Track win-loss patterns from case studies
- Monitor emerging competitors via tags

### For Content Creators

1. **Understand schema**: [[00-System/SCHEMA.md]]
2. **Pick template**: [[Standard Note Template]], [[MOC Template]], [[LLM-WIKI D2L/templates/Entity Template]]
3. **Place in structure**: Identify appropriate folder and MOC
4. **Add relationships**: Link to related content via `related_notes`
5. **Tag appropriately**: Use [[Ontology/Tag Hierarchy.md]]
6. **Review**: Check [[Navigation - MOC/Coverage Map.md]] to understand context

**Quick wins**:
- Use templates for consistency
- Link to existing related content
- Apply hierarchical tags from taxonomy
- Follow existing patterns in similar notes

---

## Traversal Patterns

### Customer-Centric Traversal

Starting from a customer, explore:
```
Customer
  ├─ Products (what they use)
  ├─ Industry (context)
  ├─ Use Cases (what they implemented)
  ├─ Competitors (what they evaluated)
  └─ Related Customers (similar profiles)
```

### Product-Centric Traversal

Starting from a product, explore:
```
Product
  ├─ Features (what it does)
  ├─ Use Cases (problems it solves)
  ├─ Industries (where it applies)
  ├─ Customers (who uses it)
  ├─ Competitors (alternatives)
  └─ Integrations (related products)
```

### Industry-Centric Traversal

Starting from an industry, explore:
```
Industry
  ├─ Customers (companies in it)
  ├─ Use Cases (common problems)
  ├─ Products (relevant solutions)
  ├─ Market Research (trends)
  └─ Success Stories (proof)
```

### Use Case-Centric Traversal

Starting from a use case, explore:
```
Use Case
  ├─ Industries (where relevant)
  ├─ Products (that enable it)
  ├─ Customers (who implement it)
  ├─ Benefits (what it delivers)
  └─ Related Use Cases (similar problems)
```

---

## Information Architecture Principles

### 1. Folder Structure = Workflow Stages

The `00-99` numbered folder system represents a business workflow:
- `00-System`: Configuration and management
- `01-Products` through `14-Buyer-Outcomes`: Sales funnel stages
- `90-99`: Administrative and archive sections

**Navigating by folder**: Understand business context of content

### 2. MOCs = Topic Hubs

Maps of Content organize information by topic, not folder hierarchy.

**MOC characteristics**:
- Aggregates related content from multiple folders
- Provides navigation and discovery
- Shows relationships between topics
- Often cross-cuts the numbered folder system

**Navigating by MOC**: Topic-oriented discovery

### 3. Entities = Discrete Resources

Customer, product, industry, use-case, and competitor entities are discrete, linkable resources.

**Entity characteristics**:
- Complete information in one place
- Rich metadata (relationships, tags)
- Referenceable from multiple contexts
- Foundation for knowledge graph

**Navigating by entity**: Relationship-based discovery

### 4. Tags = Semantic Dimension

Tags provide a semantic overlay across all content.

**Tag characteristics**:
- Hierarchical (category/subcategory/specific)
- Consistent across vault
- Enables cross-cutting queries
- Foundation for AI processing

**Navigating by tags**: Classification-based discovery

---

## Navigation Efficiency Guidelines

### Minimize Clicks to Information

**Principle**: Important, frequently-accessed information should be 2-3 clicks from entry points.

**Implementation**:
- [[VAULT DASHBOARD]] - Main entry point
- [[Navigation - MOC/00-Start Here.md]] - Navigation hub
- MOCs - Quick access to major topics
- Frequently used content - Bookmarked

### Optimize for Common Workflows

**Principle**: Structure should support most common use cases.

**Common workflows**:
- Find customer proof for prospect: 3-4 steps
- Understand product capabilities: 3-4 steps
- Explore competitive positioning: 4-5 steps
- Prepare for meeting: 4-5 steps

### Balance Breadth and Depth

**Principle**: Provide quick overviews and deep dives without forcing one or the other.

**Implementation**:
- MOC overview + detailed links
- Summary sections + full content
- Quick pathways + comprehensive exploration
- Tag-based filtering + manual browsing

---

## Relationship Best Practices

### Creating Links (for Content Creators)

**Bidirectional links**: If A links to B, B should link back to A
```yaml
# In Customer A note:
related_notes:
  - id: product-b
    title: Product B
    
# In Product B note:
related_notes:
  - id: customer-a
    title: Customer A
```

**Relationship precision**: Include relationship type, not just linkage
```yaml
linked_entities:
  - type: product
    name: Brightspace Learning
    relationship: uses-product
  - type: industry
    name: Higher Education
    relationship: belongs-to-industry
```

**Cross-reference consistency**: Related content should all reference each other
```yaml
# Content about Assessment use case should reference:
- Products that enable it: Brightspace
- Industries that use it: Higher Ed, K-12
- Customers who implemented it: [multiple examples]
```

---

## For AI Memory Layer

### How to Structure for AI Traversal

1. **Frontmatter relationships**: Use `related_notes` and `linked_entities` for explicit navigation
2. **Semantic tags**: Include entity and classification tags for inference
3. **Cross-references**: Mention related content in text with wikilinks
4. **Consistent metadata**: Structured frontmatter enables reliable parsing
5. **Hierarchical organization**: Folder structure aids context understanding

### Building AI Context

**Recommended sequence for AI retrieval**:
1. Retrieve primary note based on query
2. Follow `related_notes` to expand context
3. Use `linked_entities` to find related entities
4. Explore tags to find similar content
5. Combine results for comprehensive context

### Quality Indicators for AI

- Metadata completeness (all frontmatter fields filled)
- Relationship density (many cross-links)
- Tag consistency (hierarchical tags applied)
- Link validity (all references point to existing notes)
- Content freshness (recently updated)

---

## Navigation Troubleshooting

### Can't Find Something?

1. **Try multiple methods**:
   - Search by keyword
   - Browse by tag
   - Start from related note and follow links
   - Use MOC index

2. **Check related content**:
   - Is the information in a related topic?
   - Should it be cross-referenced?

3. **Check vault status**:
   - Is the information in a different folder?
   - Might it be archived?
   - See [[Navigation - MOC/Coverage Map.md]] for gaps

### Links are Broken?

1. **Verify the file exists**: The target note may have been moved or deleted
2. **Check the path**: Wikilink paths are case-sensitive in some environments
3. **Report**: Note should be added to [[98-Needs-Review/]]

### Tags Not Working?

1. **Use omnisearch syntax**: `tag:entity/customer`
2. **Verify tag hierarchy**: Check [[Ontology/Tag Hierarchy.md]]
3. **Check frontmatter**: Ensure tags are in YAML frontmatter, not body
4. **Review tag path**: Use full hierarchical path (category/subcategory/specific)

---

## Continuous Improvement

The vault's navigation system evolves. See:
- [[Navigation - MOC/Coverage Map.md]] - Content gaps and priorities
- [[00-System/SCHEMA.md]] - Schema improvements
- [[Ontology/Tag Hierarchy.md]] - Tag updates

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative  
**See Also**: [[00-System/SCHEMA.md]] | [[Navigation - MOC/00-Start Here.md]]

