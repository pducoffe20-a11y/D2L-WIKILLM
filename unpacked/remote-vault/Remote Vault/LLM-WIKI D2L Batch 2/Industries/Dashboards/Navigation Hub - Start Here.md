---
id: nav-start-here
title: Navigation Hub - Start Here
type: MOC
created: 2026-08-02
updated: 2026-08-02
status: verified
tags:
  - navigation/entry-point
  - navigation/hub
  - resource/navigation
  - system/orientation
category: navigation
see_also:
  - 00-System/VAULT DASHBOARD.md
  - Ontology/MOCs/MOCs.md---

# Vault Navigation Hub

Welcome to the **Navigation Hub** for the LLM-WIKI Brain. This section guides you through the vault's enhanced navigation layer, making it easier to find, connect, and understand knowledge across the system.

## What Is This?

This is your command center for navigating the vault. Whether you're:
- **Finding specific content** (customer stories, products, competitors)
- **Understanding relationships** (which customers use which products)
- **Discovering knowledge gaps** (what should we document next)
- **Traversing context** (how to get from point A to point B)

You'll find tools and guides here.

---

## Quick Navigation by Goal

### 🔍 I Want to Find Something

- **Find customer stories by industry**: [[Customer Story Navigator|Browse customers]]
- **Find products and capabilities**: [[Product and Solution Knowledge]]
- **Search by topic**: [[LLM-WIKI D2L/95-Source-Index 1/Tags Navigation]] (browse hierarchical tags)
- **Find content pathways**: [[Contentways]] (recommended reading flows)

### 🔗 I Want to Understand Connections

- **How entities relate to each other**: [[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships]] (customers ↔ products ↔ industries)
- **Knowledge graph view**: [[Knowledge Graph]] (visual relationship map)
- **Who uses what**: [[Knowledge Graph#Products and Customers|Product-customer matrix]]
- **Content dependencies**: [[Content Pathways]] (what builds on what)

### 📊 I Want Data & Analysis

- **Coverage map**: [[Coverage Map]] (what's documented, what's missing)
- **Content status**: [[Content Status]] (what's current, what needs review)
- **Tag index**: [[LLM-WIKI D2L/95-Source-Index 1/Tags Navigation]] (all tags with usage counts)
- **Recent additions**: [[Recent Content]] (latest notes added)

### 🧠 AI Memory Layer Specific

- **Improving AI retrieval**: See [[00-System/SCHEMA.md]] (metadata for AI parsing)
- **Entity extraction**: [[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships]] (structured entity information)
- **Semantic navigation**: [[Knowledge Graph]] (relationship maps)
- **Context hints**: Use tags and `related_notes` for better AI context

---

## Core Navigation Hubs

### [[Knowledge Graph]]
A visual map showing how different elements of the vault relate:
- **Customers** → **Products** → **Features**
- **Industries** → **Use Cases** → **Products**
- **Products** → **Competitors** → **Features**

**Use When**: You want to see relationships visually or trace connections between entities.

### [[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships]]
Structured view of all key entities and their connections:
- Customers organized by industry and size
- Products organized by suite and capability
- Use cases linked to industries and products
- Industries with representative customers

**Use When**: You need to see how specific entities connect or find similar entities.

### [[Content Pathways]]
Recommended reading sequences for different use cases:
- "I'm learning about Product X"
- "I need customer proof for Industry Y"
- "I want to understand Use Case Z"

**Use When**: You're starting research on a topic and want guidance on where to begin.

### [[LLM-WIKI D2L/95-Source-Index 1/Tags Navigation]]
Browse content organized by hierarchical tags:
- Customer tags (industry, size, type)
- Product tags (suite, feature, capability)
- Sales tags (stage, outcome, process)
- Use case tags (area, benefit, metric)

**Use When**: You want to explore by category or find all content tagged a certain way.

### [[Coverage Map]]
Analysis of vault coverage and content gaps:
- What's well documented
- What's sparse or missing
- Suggested areas for new content
- Content status by category

**Use When**: You're planning what to document or assessing vault completeness.

---

## Foundational Documents

### Schema & Metadata
- **[[00-System/SCHEMA.md]]** - Complete frontmatter schema
  - Define required metadata for all notes
  - Examples of each field type
  - Tag hierarchy documentation
  - Implementation guidelines

### Templates
- **[[Standard Note Template]]** - Use for most notes
- **[[MOC Template]]** - Use for Maps of Content
- **[[LLM-WIKI D2L/templates/Entity Template]]** - Use for customer/product/industry/use-case entities

### Navigation Methodology
- **[[Ontology/MOCs/MOCs.md]]** - What are MOCs and how they work
- **[[Ontology/Tag Hierarchy.md]]** - Complete tag taxonomy
- **[[Ontology/Navigation Principles.md]]** - How to navigate effectively

---

## Quick Reference

### Navigation by Use Case

| Use Case | Start Here | Then See | Then Check |
|----------|-----------|----------|-----------|
| Finding customer proof for a prospect | [[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships\|Entity Relationships]] | [[Content Pathways\|Content Pathways]] | Customer story MOC |
| Understanding product capabilities | [[Knowledge Graph\|Knowledge Graph]] | [[MOC\|Products MOC]] | Product entity page |
| Finding competitors for a product | [[Knowledge Graph\|Knowledge Graph]] | [[06-Competitors/MOC.md\|Competitors MOC]] | Competitive analysis |
| Assessing coverage & planning content | [[Coverage Map\|Coverage Map]] | [[Content Status\|Content Status]] | Relevant MOC |
| Learning the vault structure | This page | [[00-System/SCHEMA.md\|Schema]] | [[Ontology/MOCs/MOCs.md\|MOC methodology]] |

### Search Tips

- **By tag**: Use omnisearch with `tag:customer/industry/higher-ed`
- **By type**: Filter notes by type field in Notebook Navigator
- **By relationship**: Browse through [[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships]] or [[Knowledge Graph]]
- **By path**: Use folder navigation in sidebar (01-Products, 03-Industries, etc.)

---

## Understanding the Vault Structure

The vault is organized into numbered sections by workflow/topic:

- **00-System**: Configuration, schema, dashboards
- **01-Products**: Product features, positioning, capabilities
- **02-Use-Cases**: Use case descriptions and benefits
- **03-Industries**: Industry-specific content
- **04-Personas**: Buyer persona and decision-maker research
- **05-Customer-Proof**: Customer stories and case studies
- **06-Competitors**: Competitive intelligence
- **90-Inbox**: New content staging area
- **95-Source-Index**: Source tracking and references
- **98-Needs-Review**: Content needing verification
- **99-Archive**: Archived content
- **Navigation - MOC**: Enhanced navigation hubs (this folder)
- **Ontology**: Methodology, schemas, taxonomies
- **templates**: Template files for new notes

See [[VAULT DASHBOARD]] for the main dashboard.

---

## For AI Memory Layer

This navigation hub is designed to make the vault semantically structured for AI processing:

- **Standardized metadata** (frontmatter schema) enables consistent parsing
- **Related_notes field** creates explicit knowledge graph edges
- **Hierarchical tags** provide semantic classification
- **Entity templates** structure key information for extraction
- **Dynamic relationship maps** show connection patterns
- **Relationship descriptions** explain WHY entities connect

**To use effectively for AI**:
1. Follow the schema when adding new notes
2. Add `related_notes` to build the knowledge graph
3. Use hierarchical tags from the tag hierarchy
4. Add `context_hints` and `content_summary` for AI processing
5. Leverage relationship maps in prompts for better context retrieval

---

## Getting Help

- **Learn the schema**: Read [[00-System/SCHEMA.md]]
- **See examples**: Check out established MOCs like [[MOC]]
- **Understand relationships**: Browse [[LLM-WIKI D2L/95-Source-Index 1/Entity Relationships]]
- **Find navigation methods**: See [[Content Pathways]]
- **Plan new content**: Use templates listed above

---

## Recent Updates

| Date | Change | Impact |
|------|--------|--------|
| 2026-08-02 | Enhanced navigation layer launched | Better content discoverability |
| 2026-08-02 | Schema standardization (Phase 1) | Consistent metadata across vault |
| 2026-08-02 | Dynamic relationship maps (Phase 4) | Visual entity connections |

---

**Welcome to the enhanced navigation layer! Start exploring with the links above.** 🚀

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Maintained by**: Navigation Enhancement Initiative  
**See Also**: [[VAULT DASHBOARD]] | [[Ontology/MOCs/MOCs.md]]
