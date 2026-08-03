---
id: product-relationship-map
title: Product Relationship Map - Features, Capabilities & Connections
type: moc
created: 2026-08-02
updated: 2026-08-02
status: verified
tags:
  - navigation/system
  - product/relationships
  - resource/reference
  - system/reference
category: navigation
related_notes:
  - id: nav-entity-relationships
    title: Entity Relationships
  - id: nav-knowledge-graph
    title: Knowledge Graph
see_also:
  - Navigation - MOC/Entity Relationships.md
  - 01-Products/MOC.md
  - 03-Industries/Industry-Entity Map.md---

# Product Relationship Map

This page maps relationships between D2L products and other key entities in the vault. Use it to:
- Understand how D2L products relate to features, use cases, and industries
- Find customer implementations of specific products
- Discover product combinations and integrations
- Navigate product-specific content

---

## D2L Product Suite Overview

The D2L product suite consists of interconnected solutions:

### Brightspace Learning

**Purpose**: Learning management, engagement, and assessment platform

**Core capabilities**:
- Course delivery and management
- Student assessment and evaluation
- Engagement tools and features
- Collaboration capabilities
- Mobile learning support

**Use cases enabled**:
- Learning management (foundational)
- Assessment and evaluation
- Student engagement
- Content delivery
- Learning analytics

**Typical deployments**:
- Higher Education (core market)
- K-12 schools
- Corporate training
- Healthcare education

**Related products**:
- Works with: [[#Brightspace Colleague]] (student data), [[#Brightspace Ledger]] (analytics), [[#Edlink]] (data integration)

**Customer examples**: See [[Customer Story Navigator]] for implementations

---

### Brightspace Colleague

**Purpose**: Enterprise resource planning (ERP) and student information system

**Core capabilities**:
- Student information management
- Enrollment and registration
- Financial aid processing
- Business process management
- Integration hub

**Use cases enabled**:
- Student lifecycle management
- Institutional integration
- Data governance
- Business process automation
- Reporting and analytics

**Typical deployments**:
- Higher Education (core market)
- Large institutions with complex workflows
- Multi-campus systems
- International institutions

**Related products**:
- Works with: [[#Brightspace Learning]] (data sharing), [[#Brightspace Ledger]] (analytics), [[#Edlink]] (API-driven integration)

**Integration focus**:
- Central repository for institutional data
- Enables learning platform data flow
- Powers institutional analytics

**Customer examples**: See [[Customer Story Navigator]] for implementations

---

### Brightspace Ledger

**Purpose**: Analytics, insights, and learning intelligence platform

**Core capabilities**:
- Learning analytics and dashboards
- Student success prediction
- Institutional effectiveness reporting
- Curriculum analytics
- Custom reporting and data export

**Use cases enabled**:
- Analytics and outcomes tracking (foundational)
- Learning intelligence
- Institutional effectiveness
- Predictive analytics
- Evidence-based decision making

**Typical deployments**:
- Higher Education (analytics-focused)
- K-12 (outcome tracking)
- Corporate (training ROI)
- Any organization with learning data

**Related products**:
- Works with: [[#Brightspace Learning]] (data source), [[#Brightspace Colleague]] (institutional data), [[#Edlink]] (external data sources)

**Data integration**:
- Aggregates data from learning platform
- Enriches with institutional data
- Supports external data feeds

**Customer examples**: See [[Customer Story Navigator]] for implementations

---

### Edlink

**Purpose**: Data integration, API access, and third-party ecosystem

**Core capabilities**:
- API platform and developer tools
- Third-party integrations
- Data synchronization
- Ed-tech ecosystem connectivity
- Real-time data access

**Use cases enabled**:
- Third-party integrations
- Data synchronization
- Custom application development
- Ecosystem connectivity
- Data portability

**Typical deployments**:
- Institutions with third-party ed-tech stacks
- Organizations with custom integrations
- API-first technology strategies
- Growing market with developer focus

**Related products**:
- Works with: All D2L products (data access), third-party applications (integration)

**Ecosystem focus**:
- Connects D2L to broader ed-tech ecosystem
- Enables custom integrations
- Powers data portability

**Customer examples**: See [[Customer Story Navigator]] for implementations

---

## Product ↔ Use Case Mapping

This matrix shows which products enable which use cases:

| Use Case | Brightspace Learning | Colleague | Ledger | Edlink |
|----------|----------------------|-----------|--------|--------|
| **Learning Management** | 🟢 Primary | 🟡 Supporting | 🟡 Analytics | 🟡 Integration |
| **Assessment** | 🟢 Primary | 🔴 — | 🟡 Analytics | 🟡 Integration |
| **Engagement** | 🟢 Primary | 🔴 — | 🟡 Analytics | 🟡 Integration |
| **Analytics/Outcomes** | 🟡 Data source | 🟡 Data source | 🟢 Primary | 🟡 Integration |
| **Student Mgmt** | 🔴 — | 🟢 Primary | 🟡 Analytics | 🟡 Integration |
| **Integration** | 🔴 — | 🔴 — | 🔴 — | 🟢 Primary |
| **Compliance Training** | 🟢 Platform | 🔴 — | 🟡 Tracking | 🟡 Integration |
| **Performance Mgmt** | 🟡 Learning | 🟡 HR data | 🟡 Analytics | 🟡 Integration |

🟢 = Primary/Core capability | 🟡 = Supporting/Secondary | 🔴 = Not primary

---

## Product ↔ Industry Mapping

This matrix shows which industries typically adopt each product:

| Industry | Brightspace Learning | Colleague | Ledger | Edlink |
|----------|----------------------|-----------|--------|--------|
| **Higher Education** | 🟢 Core | 🟢 Core | 🟢 Core | 🟡 Growing |
| **K-12** | 🟢 Core | 🔴 Limited | 🟢 Core | 🟡 Emerging |
| **Corporate** | 🟢 Core | 🟡 Some | 🟢 Core | 🟡 Emerging |
| **Healthcare** | 🟡 Growing | 🔴 Limited | 🟡 Potential | 🔴 Limited |
| **Government** | 🟡 Potential | 🟡 Potential | 🟡 Potential | 🟡 Potential |
| **Nonprofit** | 🟡 Potential | 🔴 Limited | 🟡 Potential | 🔴 Limited |

---

## Product Combinations (Common Deployments)

### Combination 1: Learning Only
**Products**: Brightspace Learning + Edlink (optional)
**Industries**: K-12, Corporate, small Higher Ed
**Use cases**: Course delivery, basic engagement
**Customer examples**: [Browse case studies by use case]

### Combination 2: Learning + Analytics
**Products**: Brightspace Learning + Brightspace Ledger + Edlink (optional)
**Industries**: Higher Ed (analytics-focused), Corporate (ROI tracking)
**Use cases**: Learning management, analytics, outcomes tracking
**Customer examples**: [Browse case studies by use case]

### Combination 3: Comprehensive ERP Integration
**Products**: Brightspace Learning + Colleague + Ledger + Edlink
**Industries**: Large Higher Ed institutions, multi-campus systems
**Use cases**: Complete student lifecycle, institutional integration, analytics
**Customer examples**: [Browse case studies by use case]

### Combination 4: API-First Integration
**Products**: One or more D2L products + Edlink + third-party applications
**Industries**: Tech-forward organizations, custom development focus
**Use cases**: Custom integration, ecosystem connectivity, data portability
**Customer examples**: [Browse case studies by use case]

---

## Feature-Level Relationships

### Learning Management Features

Key features of Brightspace Learning:
- **Content Management**: Course structure, resources, modules
- **Assessment Tools**: Quizzes, assignments, rubrics, auto-grading
- **Engagement**: Discussion forums, email, alerts, gamification
- **Collaboration**: Group work, peer review, wikis
- **Mobile**: Native app for iOS and Android

**Industries using these features most**:
- All industries (foundational platform)

**Related use cases**:
- Learning management (primary)
- Assessment (key feature)
- Engagement (key feature)

---

### Analytics Features

Key analytics in Brightspace Ledger:
- **Learning Analytics**: Course performance, engagement metrics
- **Student Success**: Predictive alerts, at-risk identification
- **Institutional Reporting**: Program outcomes, effectiveness metrics
- **Custom Dashboards**: Role-specific views and KPIs
- **Data Export**: Integration with institutional BI tools

**Industries using these features most**:
- Higher Education (comprehensive analytics)
- Corporate (training ROI)
- K-12 (outcome tracking)

**Related use cases**:
- Analytics and outcomes (primary)
- Institutional effectiveness (key use case)
- Evidence-based decision making

---

### Integration Capabilities

Key integration scenarios:
- **Edlink API**: Programmatic access to all D2L data
- **LTI (Learning Tools Interoperability)**: Third-party tool integration
- **Single Sign-On (SSO)**: Integration with institutional identity systems
- **Data Sync**: Real-time or batch data synchronization
- **Custom Development**: Custom integrations via APIs

**Industries leveraging integration most**:
- Large institutions with complex ecosystems
- Organizations with third-party ed-tech stacks
- Enterprise customers with custom requirements

---

## Product-Focused Navigation

### Learning Platform Deep Dive

1. **Overview**: [[MOC#Brightspace Learning]]
2. **Use cases**: [[02 - Use-Cases MOC]] - filter for learning management
3. **Customer examples**: [[Customer Story Navigator]] - filter for Brightspace Learning
4. **Industry focus**: [[03-Industries/Industry-Entity Map.md]] - see where it's used
5. **Competitive context**: [[06-Competitors/MOC.md]]

### ERP & Student Information

1. **Overview**: [[MOC#Brightspace Colleague]]
2. **Use cases**: [[02 - Use-Cases MOC]] - filter for student management
3. **Customer examples**: [[Customer Story Navigator]] - filter for Colleague users
4. **Industry focus**: [[03-Industries/Industry-Entity Map.md]] - Higher Ed heavy
5. **Integration**: Check with Ledger and Edlink

### Analytics & Insights

1. **Overview**: [[MOC#Brightspace Ledger]]
2. **Use cases**: [[02 - Use-Cases MOC]] - filter for analytics
3. **Customer examples**: [[Customer Story Navigator]] - filter for Ledger users
4. **Industry focus**: [[03-Industries/Industry-Entity Map.md]] - diverse adoption
5. **Benefits**: Outcomes tracking, institutional effectiveness

### API & Integration Platform

1. **Overview**: [[MOC#Edlink]]
2. **Use cases**: [[02 - Use-Cases MOC]] - filter for integration
3. **Customer examples**: [[Customer Story Navigator]] - filter for Edlink users
4. **Ecosystem**: Third-party ed-tech integrations
5. **Developer focus**: API-first platform

---

## Product Adoption Patterns

### Typical Implementation Path

1. **Phase 1**: Adopt Brightspace Learning (core platform)
2. **Phase 2**: Add analytics (Brightspace Ledger or reports)
3. **Phase 3**: Expand to student system (Colleague) or integrations (Edlink)
4. **Phase 4**: Optimize and customize with additional products/features

**Timeline**: Varies by organization (3 months to 2 years)

### Multi-Product Benefits

Organizations using multiple products typically see:
- Better institutional data integration
- Stronger analytics and insights
- Improved decision-making
- More comprehensive solution
- Higher customer lifetime value

See [[Customer Story Navigator]] for examples.

---

## Finding Product-Specific Content

### By Product Features
→ Go to [[MOC]] and browse product sections

### By Use Case
→ Go to [[02 - Use-Cases MOC]] to find use cases, then see enabling products

### By Industry
→ Go to [[03-Industries/Industry-Entity Map.md]] to find industry, then see applicable products

### By Customer
→ Go to [[Customer Story Navigator]] to find customer, then see products used

### By Tag
→ Search: `tag:entity/product/suite/brightspace-learning`

---

## Maintaining Product Relationships

When adding new content:

1. **Identify product focus** (if applicable)
2. **Link to product MOC** (add to related_notes)
3. **Tag appropriately** (use `entity/product/*` tags)
4. **Update this map** (if new relationships discovered)
5. **Cross-reference related entities** (use cases, industries, competitors)

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative  
**See Also**: [[03-Industries/Industry-Entity Map.md]] | [[Navigation - MOC/Knowledge Graph.md]]
