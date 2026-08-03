# D2L Skills Inventory

## Overview
This document catalogs all D2L Claude Code skills available in this repository, their purposes, and their LLM provider assignments.

## Skills Registry

### 1. **d2l-brain-search**
- **Category**: Knowledge Search / Research
- **Purpose**: Search the private D2L Sales Brain for product, association, persona, customer proof, competitor, objection, implementation, account, or meeting questions
- **Key Features**:
  - Vault-based knowledge retrieval
  - Source verification and confidence levels
  - Status labels: verified, reviewed, inbox, disputed, stale
  - Integration with `last30days` for public research reconciliation
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/knowledge-search, resource/sales-tools

### 2. **d2l-sales-brief**
- **Category**: Sales Enablement / Brief Generation
- **Purpose**: Generate evidence-first D2L account, meeting, persona, industry, competitor, or opportunity briefs
- **Key Features**:
  - Verified context and evidence
  - Likely relevance assessment
  - Discovery questions and next seller moves
  - Separation of vault facts, public facts, vendor claims, and signals
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/sales-enablement, resource/sales-tools

### 3. **d2l-objection-coach**
- **Category**: Objection Handling / Sales Coaching
- **Purpose**: Retrieve and coach the strongest grounded D2L response to buyer objections
- **Key Features**:
  - Objection identification and diagnostic questions
  - Evidence-backed talk tracks
  - Competitor and market context research
  - Cautions and risk assessment
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/objection-handling, resource/sales-tools

### 4. **d2l-proof-finder**
- **Category**: Evidence Discovery / Proof Points
- **Purpose**: Locate and verify D2L proof points and customer success evidence
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/proof-discovery, resource/sales-tools

### 5. **d2l-brain-capture**
- **Category**: Knowledge Capture / Documentation
- **Purpose**: Capture and structure new D2L sales intelligence into the brain vault
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/knowledge-management, resource/sales-tools

### 6. **d2l-brain-curate**
- **Category**: Knowledge Curation / Quality Assurance
- **Purpose**: Review and curate existing D2L sales brain entries for accuracy and relevance
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/knowledge-management, resource/sales-tools

### 7. **d2l-brain-refresh**
- **Category**: Knowledge Refresh / Maintenance
- **Purpose**: Update and refresh stale D2L sales brain entries with current information
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/knowledge-management, resource/sales-tools

### 8. **d2l-change-radar**
- **Category**: Change Detection / Market Intelligence
- **Purpose**: Monitor and identify significant changes in D2L, customers, competitors, or market conditions
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus
- **Status**: Production Ready
- **Tags**: ai/agent-skill, skill/category/market-intelligence, resource/sales-tools

### 9. **firecrawl**
- **Category**: Web Crawling / Data Collection
- **Purpose**: Crawl and extract structured data from web pages for sales research
- **Recommended LLM Providers**: Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
- **Status**: Utility / Integration
- **Tags**: ai/agent-skill, skill/category/data-collection, resource/tools

## Skills by Category

### Sales Enablement
- d2l-sales-brief
- d2l-objection-coach
- d2l-proof-finder

### Knowledge Management
- d2l-brain-capture
- d2l-brain-curate
- d2l-brain-refresh
- d2l-brain-search

### Market Intelligence
- d2l-change-radar

### Utilities
- firecrawl

## LLM Provider Compatibility Matrix

| Skill | Claude 3.5 Sonnet | Claude 3 Opus | Claude 3 Haiku | Codex | Gemini Pro |
|-------|-------------------|---------------|----------------|-------|-----------|
| d2l-brain-search | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-sales-brief | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-objection-coach | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-proof-finder | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-brain-capture | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-brain-curate | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-brain-refresh | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| d2l-change-radar | ✅ Primary | ✅ Supported | ⚠️ Limited | ❌ | ⚠️ Partial |
| firecrawl | ✅ Primary | ✅ Supported | ✅ Full | ⚠️ Limited | ⚠️ Limited |

**Legend**:
- ✅ Primary: Optimized and recommended
- ✅ Supported: Fully compatible
- ⚠️ Limited: May require prompt adjustments
- ⚠️ Partial: Limited capability match
- ❌: Not recommended

## Recommended Provider Selection

### Claude (Primary - Recommended)
- **Versions**: Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
- **Use Case**: All sales skills, primary platform for D2L implementation
- **Advantages**: 
  - Best context understanding
  - Strongest reasoning for objection handling
  - Optimal for knowledge search and synthesis

### Google Gemini (Secondary Support)
- **Versions**: Gemini Pro, Gemini Ultra
- **Use Case**: Parallel processing, secondary validation
- **Limitations**:
  - May require prompt adjustments
  - Different tokenization affects context windows
  - Support for complex multi-step reasoning varies

### OpenAI Codex (Limited Support)
- **Use Case**: Legacy integration only
- **Status**: Not recommended for new implementations
- **Reason**: Limited support for complex sales reasoning patterns
