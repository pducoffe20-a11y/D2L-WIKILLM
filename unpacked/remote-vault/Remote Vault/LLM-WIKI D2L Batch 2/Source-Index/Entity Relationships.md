---
id: nav-entity-relationships
title: "Entity Relationships - Structured Navigation"
type: moc
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [navigation/core, ontology/moc, entity/index, ai/context]
category: navigation
related_notes:
  - id: nav-knowledge-graph
    title: "Knowledge Graph - Entity Relationships"
  - id: nav-content-pathways
    title: "Content Pathways"
see_also:
  - "Navigation - MOC/Knowledge Graph.md"
  - "05-Customer-Proof/Navigation - MOC/Customer Story Navigator.md"
  - "01-Products/MOC.md"
---

# Entity Relationships - Structured Index

This page provides a structured view of major entities in the vault and their relationships. Use this to:
- Find entities by type and classification
- Understand how entities connect
- Navigate from one entity to related entities
- Discover entity clusters and patterns

---

## Navigation by Entity Type

### Customers

**By Industry Segment**:

#### Higher Education
- [Generate using dataview if available]
- See: [[Customer Story Navigator]] for complete customer stories

#### K-12
- [Generate using dataview if available]
- See: [[Customer Story Navigator]] for complete customer stories

#### Corporate / Enterprise Training
- [Generate using dataview if available]
- See: [[Customer Story Navigator]] for complete customer stories

**By Customer Size**:
- **Enterprise**: Multi-product implementations, extensive case studies
- **Mid-Market**: Growing implementations, strategic use cases
- **SMB**: Emerging implementations, specific use case focus

**Multi-Story Customers** (Subject of Multiple Case Studies):
- See: [[Customer Story Navigator]] - Section on "Multi-Story Customers"

---

### Products

**D2L Product Suite Organization**:

#### Learning & Collaboration Suite
- **Brightspace Learning**: LMS, assessment, engagement
  - Key use cases: Course Management, Assessment, Engagement
  - Industries: Higher Ed, K-12, Corporate
  - See: [[MOC]]

#### Integration & Data Suite
- **Brightspace Ledger**: Analytics and reporting
- **Colleague**: ERP and student information system
- **Edlink**: Data integration and API platform
  - See: [[MOC]] for complete product documentation

#### Related Products
- See: [[06-Competitors/MOC.md]] for competitive alternatives

---

### Use Cases

**By Industry Applicability**:

#### Higher Education Use Cases
- Learning Management and Delivery
- Assessment and Evaluation
- Student Engagement and Success
- Analytics and Outcomes Tracking
- Institutional Effectiveness

#### K-12 Use Cases
- Primary/Secondary Education
- Remote Learning
- Student Assessment
- Parent Engagement
- Achievement Tracking

#### Corporate Use Cases
- Employee Training and Development
- Compliance Training
- Performance Management
- Onboarding
- Knowledge Management

**By Benefit Type**:
- Time-to-Value
- Cost Reduction
- Engagement Improvement
- Efficiency Gains
- Outcome Improvement

---

### Industries

**Served Industries**:

#### Higher Education
- Universities, colleges, community colleges
- Research institutions
- Online learning providers
- See: [[03-Industries/]] for industry-specific content

#### K-12
- Primary and secondary schools
- School districts
- Charter school systems
- See: [[03-Industries/]] for industry-specific content

#### Corporate
- Fortune 500 companies
- Mid-market enterprises
- Small businesses (emerging)
- Government agencies
- See: [[03-Industries/]] for industry-specific content

**Industries with Emerging Opportunity**:
- [Identify using [[Coverage Map]]]

---

### Personas & Decision-Makers

**By Role** (When documented):
- C-Suite (CTO, Chief Learning Officer, CFO)
- Department heads (Training, Learning & Development)
- End users (Faculty, instructors, learners)
- See: [[04-Personas/]] for detailed persona research

---

## Relationship Patterns

### Customer ↔ Products

**High-Value Connection Indicator**:
- Customer uses multiple D2L products
- Example: Acme Corp uses Brightspace Learning + Colleague + Ledger
- Significance: Multi-product customers have richer case studies

**How to Find**:
1. Go to [[Customer Story Navigator]]
2. Find customer
3. Check "Products Used" section
4. Link to product MOCs for feature details

### Customer ↔ Use Cases

**Connection Indicator**:
- Customer implements specific use cases
- Example: Acme Corp implemented Assessment, Engagement, and Analytics
- Significance: Shows completeness of implementation

**How to Find**:
1. Find customer in [[Customer Story Navigator]]
2. Check "Use Cases Implemented" section
3. Browse related use case documentation

### Product ↔ Industry

**Connection Indicator**:
- Products serve different industries with different focus
- Example: Brightspace widely used in Higher Ed, growing in Corporate
- Significance: Industry-specific positioning and messaging

**How to Find**:
1. Check [[MOC]] for product descriptions
2. Review customer base by industry
3. See [[03-Industries/]] for industry-specific product applications

### Use Case ↔ Industry

**Connection Indicator**:
- Different industries prioritize different use cases
- Example: Assessment critical in Higher Ed, Compliance key in Corporate
- Significance: Industry-specific value propositions

**How to Find**:
1. Review [[02 - Use-Cases MOC]]
2. Check which industries value each use case
3. Cross-reference with [[03-Industries/]]

### Customer ↔ Competitor

**Connection Indicator**:
- Customers evaluated alternatives before choosing D2L
- Indicates competitive positioning opportunity
- Significance: Win-loss analysis, competitive differentiation

**How to Find**:
1. Search [[05-Customer-Proof/]] for competitor mentions
2. See [[06-Competitors/MOC.md]] for competitive analysis
3. Look for "evaluated" or "migrated from" in customer stories

---

## Entity Clustering

### Customers in Same Industry

Navigate to an industry (e.g., [[03-Industries/]]), then browse customers in that industry:
- Find their case studies
- Compare their use cases
- Identify common product selections
- Look for shared challenges/opportunities

### Products Used Together

Common product combinations (when customers implement multiple products):
- **Learning + Engagement**: Core learning platform with engagement features
- **Learning + Analytics**: Learning platform with outcomes tracking
- **Brightspace + Colleague**: Education-focused comprehensive ERP
- **Brightspace + Edlink**: Learning platform with data integration

### Use Cases by Industry

**Higher Education Cluster**:
- Learning Management (foundational)
- Assessment (critical)
- Engagement (differentiator)
- Analytics (emerging)

**Corporate Cluster**:
- Compliance Training (foundational)
- Employee Development (core)
- Performance Management (integrated)
- Knowledge Management (emerging)

---

## Key Relationships for AI Traversal

These relationships enable effective AI context retrieval:

### Customer-Centric Traversal
```
Customer → Products → Features → Benefits → Competitive Context
        ↓
       Use Cases → Industry Applications → Success Metrics
        ↓
       Competitors → Win-Loss Analysis → Differentiation
        ↓
       Case Studies → Outcomes → References
```

### Product-Centric Traversal
```
Product → Capabilities → Use Cases → Industry Application
       ↓
      Customers → Success Stories → Metrics
       ↓
      Competitors → Comparison → Differentiation
       ↓
      Integration Points → Complementary Products
```

### Use Case-Centric Traversal
```
Use Case → Industries → Customers → Case Studies
        ↓
       Products → Enablement → Features
        ↓
       Benefits → Metrics → ROI
        ↓
       Competitive Context → Win-Loss
```

---

## Discovering Related Content

### From a Customer
- **Related customers**: Same industry, similar size
- **Product details**: Products this customer uses
- **Use cases**: What they implemented
- **Industry research**: Industry dynamics
- **Competitors**: Competitive alternatives they evaluated

### From a Product
- **Related products**: Complementary or integrated
- **Use cases**: Problems it solves
- **Industries**: Where it's applicable
- **Customers**: Who uses it
- **Competitors**: Alternative solutions

### From a Use Case
- **Related use cases**: Similar problems or benefits
- **Industries**: Where it matters most
- **Products**: Solutions that enable it
- **Customers**: Who implemented it
- **Success metrics**: How to measure impact

### From an Industry
- **Related industries**: Similar market dynamics
- **Customers**: Companies in this industry
- **Use cases**: Priority problems
- **Products**: Most applicable solutions
- **Market research**: Industry trends and opportunities

---

## Metadata for Relationship Navigation

The frontmatter schema stores relationships via:

- `related_notes`: Array of related note IDs and titles
- `linked_entities`: Typed relationships (customer→product→benefits)
- `see_also`: Quick cross-references
- `tags`: Hierarchical classification enabling semantic navigation

See [[00-System/SCHEMA.md]] for complete field documentation.

---

## Using Relationships for Content

When creating or updating notes:

1. **Identify related entities**: What other entities should link to this?
2. **Add to related_notes**: Include bidirectional references
3. **Add to linked_entities**: Specify relationship type
4. **Apply tags**: Use hierarchical tags for semantic grouping
5. **Cross-reference**: Mention related content in note text

---

## Maintaining Relationships

**Regular Review**:
- Quarterly: Check relationships are current
- When new customer stories added: Link to related entities
- When products/use cases change: Update relationships
- When competitors enter/exit market: Update competitive relationships

**Validation**:
- Use dataview queries to find broken references
- Verify bidirectional relationships (if A links to B, B should link to A)
- Check that related_notes IDs are still valid

---

## Related Navigation Resources

- **[[Navigation - MOC/Knowledge Graph.md]]** - Visual representation of relationships
- **[[Navigation - MOC/Content Pathways.md]]** - Recommended navigation sequences
- **[[Customer Story Navigator]]** - Customer stories by relationship
- **[[00-System/SCHEMA.md]]** - Frontmatter fields for encoding relationships
- **[[MOC]]** - Product index
- **[[03-Industries/]]** - Industry research
- **[[02 - Use-Cases MOC]]** - Use case documentation

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative  
**See Also**: [[Navigation - MOC/00-Start Here.md]] | [[Navigation - MOC/Knowledge Graph.md]]

