---
id: nav-knowledge-graph
title: Knowledge Graph - Entity Relationships
type: moc
created: 2026-08-02
updated: 2026-08-02
status: verified
tags:
  - ai
  - business-case
  - moc
  - navigation
category: navigation
related_notes:
  - id: nav-entity-relationships
    title: Entity Relationships
  - id: nav-start-here
    title: Navigation Hub - Start Here
see_also:
  - Navigation - MOC/Entity Relationships.md
  - Navigation - MOC/Content Pathways.md
  - 05-Customer-Proof/Navigation - MOC/Customer Story Navigator.md---

# Knowledge Graph - Vault Relationships

This page visualizes how major elements of the vault connect to form an integrated knowledge graph. Use this to:
- Understand the web of relationships in the vault
- Trace paths between different entities
- Discover related content by following connections
- Plan content based on connection patterns

---

## Core Relationship Model

```
                        INDUSTRIES
                             │
                    ┌────────┼────────┐
                    ↓        ↓        ↓
          ┌──────────────┬──────────────┬──────────────┐
          │              │              │              │
      CUSTOMERS    USE CASES      PERSONAS      PRODUCTS
          │              │              │              │
          ├──────────────┴──────────────┴──────────────┤
          │                                            │
        CASE STUDIES ─────────────────── COMPETITIVE ANALYSIS
          │                                            │
          └──────────────────┬───────────────────────┘
                             ↓
                     CUSTOMER PROOF
                             │
                    ┌────────┼────────┐
                    ↓        ↓        ↓
               SUCCESS   BENEFITS   OUTCOMES
              METRICS    REALIZATION  ACHIEVED
```

### Key Relationships

#### 1. Customer ↔ Industry
- **Connection**: Each customer belongs to one or more industries
- **Example**: Acme Corp → Higher Education Industry
- **Use**: Find customers by industry, understand market segment

#### 2. Customer ↔ Product
- **Connection**: Customers use specific D2L products/suites
- **Example**: Acme Corp → Uses Brightspace Learning
- **Use**: Product adoption insights, customer fit analysis

#### 3. Product ↔ Use Case
- **Connection**: Products enable specific use cases and deliver benefits
- **Example**: Brightspace → Assessment Use Case
- **Use**: Feature-benefit mapping, capability discovery

#### 4. Industry ↔ Use Case
- **Connection**: Certain use cases are more prevalent in specific industries
- **Example**: Higher Ed → Learning Management, Assessment
- **Use**: Industry-specific positioning, relevant features

#### 5. Customer ↔ Competitor
- **Connection**: Customers evaluated or migrated from competitors
- **Example**: Acme Corp → Evaluated Blackboard, chose Brightspace
- **Use**: Competitive positioning, win-loss analysis

#### 6. Product ↔ Competitor
- **Connection**: Direct competitive alternatives exist
- **Example**: Brightspace Learning → Competes with Blackboard Learn
- **Use**: Feature differentiation, market positioning

---

## Navigation Patterns

### Finding Customer Proof for a Prospect

```
Industry → [Browse Customers in Industry]
         → [Select Customer]
         → [View Case Studies]
         → [Related Products/Use Cases]
         → [Competitive Context]
```

**Example Path**: Higher Education → Acme Corp → Case Study → Brightspace Benefits

### Understanding Product Positioning

```
Product → [Product Capabilities]
        → [Use Cases Enabled]
        → [Customer Examples]
        → [Industry Application]
        → [Competitive Alternatives]
```

**Example Path**: Brightspace → Assessment Features → Education Industry Adoption

### Exploring by Use Case

```
Use Case → [Industries with this use case]
         → [Products enabling this]
         → [Customer implementations]
         → [Related use cases]
         → [Benefits achieved]
```

**Example Path**: Assessment → Education, Corporate → Brightspace, Colleague → Customer Success Stories

### Discovering Competitive Insights

```
Competitor → [Feature Comparison]
           → [Customer Base]
           → [Industries Served]
           → [Win/Loss Information]
           → [D2L Differentiation]
```

---

## Entity Type Relationships

### Customers as Central Nodes

Each customer entity can connect to:
- **Industry** (belongs to)
- **Products** (uses)
- **Use Cases** (implements)
- **Competitors** (evaluated/replaced)
- **Case Studies** (subject of)
- **Contact Information** (people involved)
- **Success Metrics** (measurable outcomes)

**High-Value Customers**: Serve as hubs with many connections = rich source of competitive intelligence

### Products as Central Nodes

Each product entity can connect to:
- **Features** (what it does)
- **Capabilities** (integrated functionality)
- **Use Cases** (enabled by this product)
- **Industries** (applicable to)
- **Customers** (users/adopters)
- **Competitors** (alternatives)
- **Success Stories** (customer proof)

### Industries as Classification Hubs

Each industry entity can connect to:
- **Customers** (in this industry)
- **Use Cases** (common in this industry)
- **Products** (applicable to this industry)
- **Market Research** (industry-specific insights)
- **Trends** (industry evolution)

### Use Cases as Benefit Nodes

Each use case entity can connect to:
- **Industries** (where this is relevant)
- **Products** (that enable it)
- **Customers** (who implement it)
- **Benefits** (outcomes achieved)
- **Success Metrics** (how to measure)

---

## Semantic Relationship Types

The knowledge graph uses these relationship types for precise modeling:

### Product Relationships
- `uses` (Customer uses Product)
- `enables` (Product enables Use Case)
- `implements` (Customer implements Feature)
- `competes-with` (Product A competes with Product B)
- `integrates-with` (Product A integrates with Product B)

### Customer Relationships
- `belongs-to` (Customer belongs to Industry)
- `uses` (Customer uses Product)
- `implements` (Customer implements Use Case)
- `evaluated` (Customer evaluated Competitor)
- `migrated-from` (Customer migrated from Competitor)

### Use Case Relationships
- `applicable-to` (Use Case applicable to Industry)
- `enabled-by` (Use Case enabled by Product)
- `implemented-by` (Use Case implemented by Customer)
- `achieves-benefit` (Use Case achieves Benefit)
- `related-to` (Use Case related to other Use Case)

### Industry Relationships
- `contains` (Industry contains Customers)
- `benefits-from` (Industry benefits from Use Case)
- `uses` (Industry typically uses Product)

---

## Browsing by Connection Density

### Highly Connected Entities (Rich Resources)

**Customers with many connections**:
- Multi-product implementations → rich case studies
- Multiple use cases → comprehensive proof
- Long history → success metrics available
- Multiple contact relationships → decision-maker insights

**Products with many connections**:
- Used across many industries → broad applicability
- Enables many use cases → versatile platform
- Many customer implementations → proven adoption
- Significant competitive differentiation → worth studying

**Industries with rich content**:
- Large customer base → many examples
- Multiple use cases → comprehensive coverage
- Active market → current research available
- Strategic focus → priority coverage

### Sparsely Connected Entities (Content Gaps)

Areas with few connections indicate:
- Emerging market segments (newer industries)
- Emerging use cases (not yet widely adopted)
- New product features (limited customer examples)
- Underserved segments (opportunity for growth)

Use [[Coverage Map]] to identify and prioritize content gaps.

---

## Relationship Query Examples

### For Sales Enablement

- "Show me customers in Higher Ed using Brightspace"
- "What use cases do K-12 customers typically implement?"
- "Which customers have implemented Assessment and Engagement?"
- "How does our product compare to Blackboard for this use case?"

### For Product Strategy

- "Which features are most commonly implemented?"
- "What use cases have the highest adoption?"
- "Which industries have the most customer examples?"
- "Where are we missing competitive positioning?"

### For Content Planning

- "What customer stories do we need for Corporate segment?"
- "Which use cases lack implementation examples?"
- "What competitive analysis is outdated?"
- "Where are the knowledge gaps?"

---

## Related Navigation Resources

- **[[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships]]** - Structured list of all entities and their connections
- **[[Content Pathways]]** - Recommended reading sequences
- **[[LLM-WIKI D2L/95-Source-Index 1/Tags Navigation]]** - Browse by hierarchical tags
- **[[00-System/SCHEMA.md]]** - Metadata schema for relationships
- **[[Customer Story Navigator]]** - Customer stories organized by relationship

---

## For AI Memory Layer

This knowledge graph enables AI to:

1. **Traverse context**: Follow relationship chains to retrieve related information
   - "Given Acme Corp, find similar customers and their products"
   - "Given Brightspace, find all use cases and customer implementations"

2. **Infer missing information**: Understand typical connection patterns
   - "If customer is in Higher Ed, likely use cases include Assessment"
   - "If using Brightspace, likely also uses Colleague or Ledger"

3. **Identify opportunities**: Find connection gaps
   - "Customer using Product A but not Product B (competitors don't)"
   - "Industry with few documented use cases"

4. **Semantic search**: Better query interpretation
   - "Show me proof in my industry" → traverse Industry → Customers → Case Studies
   - "What can product X do for us?" → traverse Product → Use Cases → Benefits

**Implementation**: Leverage `linked_entities`, `related_notes`, and hierarchical `tags` in frontmatter to encode these relationships for AI processing.

---

## Updating the Graph

As new content is added:

1. **New Customer**: Add to industry, link to products and case studies
2. **New Product**: Add capabilities, link to use cases
3. **New Use Case**: Link to industries and products
4. **New Competitor Info**: Add relationships to products and customers

See [[00-System/SCHEMA.md]] for frontmatter fields used to encode these relationships.

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative  
**See Also**: [[Navigation - MOC/00-Start Here.md]] | [[Navigation - MOC/Entity Relationships.md]]
