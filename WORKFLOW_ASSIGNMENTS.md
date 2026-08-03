# D2L Skills - Workflow Assignments & Routing Guide

## Overview
This document defines how D2L skills are assigned to different workflow scenarios and LLM providers, enabling intelligent skill orchestration across multiple AI platforms.

## Workflow Categories

### 1. Sales Research & Preparation Workflow
**Purpose**: Equip sales teams with comprehensive research before customer interactions

#### Skills Assignment
```
research-request → d2l-brain-search → (findings + gaps)
                ↓
             last30days (public research)
                ↓
             d2l-change-radar (market changes)
                ↓
             consolidate → decision-ready brief
```

#### Assigned Skills
- **Primary**: d2l-brain-search, d2l-change-radar
- **Secondary**: d2l-sales-brief (for comprehensive briefs)
- **Supporting**: firecrawl (for current web data)

#### LLM Provider Assignment
| Provider | Model | Role | Conditions |
|----------|-------|------|-----------|
| Claude | 3.5 Sonnet | Primary orchestrator | Default routing |
| Claude | 3 Opus | Fallback orchestrator | If Sonnet unavailable |
| Gemini | Pro | Parallel validation | For verification workflows |

#### Workflow Routing Logic
```yaml
if urgent AND high_confidence_needed:
  provider: Claude-Sonnet
  model: claude-3-5-sonnet-20241022
elif bulk_processing:
  provider: Claude-Opus
  model: claude-3-opus-20240229
else:
  provider: Claude-Haiku
  model: claude-3-haiku-20240307
```

---

### 2. Sales Coaching & Enablement Workflow
**Purpose**: Provide just-in-time coaching and objection handling support

#### Skills Assignment
```
user-objection → d2l-objection-coach → talk-track + evidence
                ↓
             (if gap) d2l-brain-search
                ↓
             deliver → coaching-ready response
```

#### Assigned Skills
- **Primary**: d2l-objection-coach
- **Secondary**: d2l-brain-search (for evidence)
- **Supporting**: d2l-proof-finder (for case studies)

#### LLM Provider Assignment
| Provider | Model | Role | Conditions |
|----------|-------|------|-----------|
| Claude | 3.5 Sonnet | Primary coaching | Real-time requests |
| Claude | 3 Opus | Detailed coaching | Complex objections |
| Claude | 3 Haiku | Quick coaching | Simple/routine objections |

#### Workflow Routing Logic
```yaml
if objection_complexity == "high":
  provider: Claude-Opus
  context_window: 200k
elif objection_complexity == "medium":
  provider: Claude-Sonnet
  context_window: 200k
else:
  provider: Claude-Haiku
  context_window: 100k
```

---

### 3. Knowledge Management Workflow
**Purpose**: Maintain and evolve the D2L sales brain

#### Skills Assignment
```
new-insight → d2l-brain-capture → structured-entry
           ↓
        d2l-brain-curate → quality-check
           ↓
        d2l-brain-refresh → versioned-update
           ↓
        vault → searchable
```

#### Assigned Skills
- **Primary**: d2l-brain-capture, d2l-brain-curate, d2l-brain-refresh
- **Secondary**: d2l-brain-search (for context)
- **Supporting**: firecrawl (for source data)

#### LLM Provider Assignment
| Provider | Model | Role | Conditions |
|----------|-------|------|-----------|
| Claude | 3.5 Sonnet | Quality assurance | Curation phase |
| Claude | 3 Opus | Detailed analysis | Complex knowledge |
| Claude | 3 Haiku | Bulk processing | Routine updates |

#### Workflow Routing Logic
```yaml
if workflow_phase == "capture":
  provider: Claude-Sonnet
  context: full-source-materials
elif workflow_phase == "curate":
  provider: Claude-Opus
  context: vault-history + external-signals
else:  # refresh
  provider: Claude-Haiku
  context: existing-entry + updates
```

---

### 4. Competitive Intelligence Workflow
**Purpose**: Monitor and track competitive landscape changes

#### Skills Assignment
```
market-monitoring → d2l-change-radar → change-signals
                 ↓
              d2l-brain-search → historical-context
                 ↓
              d2l-proof-finder → competitive-proof
                 ↓
              consolidate → intelligence-brief
```

#### Assigned Skills
- **Primary**: d2l-change-radar, d2l-brain-search
- **Secondary**: d2l-proof-finder
- **Supporting**: firecrawl (for web sources)

#### LLM Provider Assignment
| Provider | Model | Role | Conditions |
|----------|-------|------|-----------|
| Claude | 3.5 Sonnet | Primary analysis | Default |
| Gemini | Pro | Parallel analysis | For cross-validation |
| Claude | 3 Opus | Detailed synthesis | Complex competitive dynamics |

---

### 5. Account Planning Workflow
**Purpose**: Create comprehensive account and opportunity strategies

#### Skills Assignment
```
account-research → d2l-brain-search → account-context
               ↓
            d2l-sales-brief → opportunity-brief
               ↓
            d2l-change-radar → change-impact
               ↓
            d2l-proof-finder → relevant-proof
               ↓
            consolidate → account-plan
```

#### Assigned Skills
- **Primary**: d2l-sales-brief, d2l-brain-search
- **Secondary**: d2l-change-radar, d2l-proof-finder

#### LLM Provider Assignment
| Provider | Model | Role | Conditions |
|----------|-------|------|-----------|
| Claude | 3.5 Sonnet | Primary planning | Default |
| Claude | 3 Opus | Complex scenarios | Enterprise accounts |
| Gemini | Pro | Parallel validation | Strategic reviews |

---

## Skill-to-Workflow Matrix

| Skill | Sales Research | Coaching | Knowledge Mgmt | Competitive Intel | Account Planning |
|-------|----------------|----------|----------------|-------------------|-----------------|
| d2l-brain-search | ✅ Primary | ⚠️ Secondary | ✅ Primary | ✅ Primary | ✅ Primary |
| d2l-sales-brief | ✅ Primary | ❌ | ❌ | ⚠️ Secondary | ✅ Primary |
| d2l-objection-coach | ❌ | ✅ Primary | ❌ | ❌ | ⚠️ Secondary |
| d2l-proof-finder | ⚠️ Secondary | ✅ Primary | ❌ | ✅ Primary | ✅ Primary |
| d2l-brain-capture | ❌ | ❌ | ✅ Primary | ❌ | ❌ |
| d2l-brain-curate | ❌ | ❌ | ✅ Primary | ❌ | ❌ |
| d2l-brain-refresh | ❌ | ❌ | ✅ Primary | ⚠️ Secondary | ❌ |
| d2l-change-radar | ✅ Primary | ❌ | ⚠️ Secondary | ✅ Primary | ✅ Primary |
| firecrawl | ✅ Primary | ⚠️ Secondary | ✅ Primary | ✅ Primary | ✅ Primary |

**Legend**:
- ✅ Primary: Core skill for this workflow
- ⚠️ Secondary: Supporting skill, may be used conditionally
- ❌: Not used in this workflow

---

## Multi-LLM Provider Orchestration

### Claude Ecosystem (Primary)
**Recommended Stack**: Claude 3.5 Sonnet + Claude 3 Opus + Claude 3 Haiku

**Routing Strategy**:
1. **Default Route** → Claude 3.5 Sonnet (all skills)
2. **High Complexity** → Claude 3 Opus (complex reasoning)
3. **Bulk/Routine** → Claude 3 Haiku (high throughput)
4. **Context Limit** → Select by available context window

### Cross-Provider Validation
For high-stakes workflows, enable multi-provider validation:

```yaml
validation_workflow:
  primary: Claude-Sonnet
  validator: Gemini-Pro
  triggers:
    - enterprise_deals
    - competitive_threats
    - strategic_decisions
  merge_strategy: consensus
```

### Fallback Chains
```
Claude-Sonnet (preferred)
    ↓ (if unavailable)
Claude-Opus
    ↓ (if unavailable)
Claude-Haiku
    ↓ (if unavailable)
Gemini-Pro (fallback)
```

---

## Workflow Implementation Checklist

### For New Workflow Implementation
- [ ] Identify primary skills needed
- [ ] Determine LLM provider (primary + fallback)
- [ ] Set up skill chaining logic
- [ ] Define success criteria
- [ ] Configure error handling
- [ ] Test with sample data
- [ ] Document workflow steps
- [ ] Train users on workflow

### For Skill Selection
- [ ] Check SKILLS_INVENTORY.md for skill details
- [ ] Verify LLM provider compatibility
- [ ] Review recommended context window
- [ ] Consider cost/performance trade-offs
- [ ] Test with your data
- [ ] Monitor performance metrics
