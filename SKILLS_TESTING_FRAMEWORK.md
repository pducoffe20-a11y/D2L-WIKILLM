# D2L Skills Testing Framework

## Overview
This framework defines how to test, validate, and verify D2L skills across different LLM providers and use cases.

## Test Categories

### 1. Unit Tests (Skill-Level)
Test individual skills in isolation with predetermined inputs and expected outputs.

#### Test Structure
```yaml
test_id: brain_search_001
skill: d2l-brain-search
provider: claude-3-5-sonnet
test_type: unit
input:
  query: "D2L learning platform product capabilities"
  context: "sales engineer technical evaluation"
expected_output:
  - verified_facts: ✓ Present
  - source_citations: ✓ Present
  - confidence_scores: ✓ Present
  - status_labels: ✓ Present (verified/reviewed/disputed/stale)
validation_rules:
  - output_format: json
  - min_facts: 3
  - citation_required: true
success_criteria:
  confidence: "> 85%"
  latency: "< 10 seconds"
```

### 2. Integration Tests (Workflow-Level)
Test skill chains and orchestrated workflows.

#### Test Structure
```yaml
test_id: workflow_sales_brief_001
workflow: Sales Research & Preparation
provider: claude-3-5-sonnet
test_type: integration
skills_chain:
  - d2l-brain-search (research)
  - d2l-change-radar (market intel)
  - consolidate (synthesis)
input:
  account: "TechCorp Inc"
  topic: "D2L implementation at scale"
expected_flow:
  1: brain_search_returns_context
  2: change_radar_returns_updates
  3: consolidate_produces_brief
validation_rules:
  - chain_completion: true
  - data_flow_validated: true
success_criteria:
  - completeness: ">90%"
  - accuracy: ">85%"
  - coherence: ">90%"
```

### 3. Cross-Provider Tests
Validate skill performance consistency across LLM providers.

#### Test Structure
```yaml
test_id: cross_provider_objection_001
skill: d2l-objection-coach
test_type: cross_provider
providers:
  - claude-3-5-sonnet
  - claude-3-opus
  - gemini-pro
input:
  objection: "D2L is too expensive for our use case"
  persona: "CFO/Finance Decision Maker"
  stage: "evaluation"
comparison_metrics:
  - response_quality
  - talk_track_strength
  - evidence_relevance
  - handling_confidence
success_criteria:
  consistency: "> 80%"
  quality_variance: "< 15%"
```

### 4. Performance Tests
Test speed, cost, and resource efficiency.

#### Test Structure
```yaml
test_id: perf_brain_search_bulk_001
skill: d2l-brain-search
test_type: performance
scale: 100_concurrent_queries
metrics:
  - latency_p50
  - latency_p95
  - latency_p99
  - throughput_qps
  - cost_per_query
  - error_rate
success_criteria:
  latency_p95: "< 5 seconds"
  throughput: "> 20 qps"
  error_rate: "< 1%"
```

### 5. Quality Assurance Tests
Validate content quality, accuracy, and compliance.

#### Test Structure
```yaml
test_id: qa_sales_brief_001
skill: d2l-sales-brief
test_type: quality_assurance
review_criteria:
  - factual_accuracy: "verified against vault"
  - source_attribution: "all claims cited"
  - completeness: "covers key dimensions"
  - clarity: "written for target audience"
  - actionability: "includes clear next steps"
quality_standards:
  min_source_coverage: 80%
  hallucination_tolerance: 0%
  factual_error_tolerance: 5%
```

---

## Test Scenarios

### Scenario 1: Sales Discovery Call Preparation
**Workflow**: Sales Research → Brief Generation → Coaching

**Test Steps**:
1. Input: Account name + meeting context
2. Run d2l-brain-search (gather intelligence)
3. Run d2l-sales-brief (generate brief)
4. Run d2l-objection-coach (prepare coaching)
5. Validate: Completeness, accuracy, actionability

**Success Metrics**:
- Brief ready in < 2 minutes
- Accuracy score > 90%
- At least 3 proven proof points identified
- Objection responses supported by evidence

---

### Scenario 2: Competitive Intelligence Update
**Workflow**: Change Detection → Context → Intelligence Brief

**Test Steps**:
1. Input: Competitor + time period
2. Run d2l-change-radar (identify changes)
3. Run d2l-brain-search (gather history)
4. Run d2l-proof-finder (find proof points)
5. Consolidate into intelligence brief

**Success Metrics**:
- Changes identified within 24 hours
- Historical context accurate
- Competitive implications clear
- Actionable intelligence generated

---

### Scenario 3: Knowledge Base Maintenance
**Workflow**: Capture → Curate → Refresh

**Test Steps**:
1. Input: New sales insight
2. Run d2l-brain-capture (structure)
3. Run d2l-brain-curate (quality check)
4. Run d2l-brain-refresh (update versioning)
5. Validate: Vault integration, searchability

**Success Metrics**:
- Entry properly structured
- Quality gates passed
- Searchable within vault
- Version history maintained

---

## Test Data Sets

### Test Dataset A: Product Questions (General)
```
Test Cases:
1. "What are D2L's core LMS features?"
2. "How does D2L compare to Canvas?"
3. "What industries use D2L?"
4. "What are D2L pricing models?"
5. "Who are D2L's target customers?"

Expected Outcome: Factual, sourced answers with confidence levels
```

### Test Dataset B: Sales Scenarios (Real-world)
```
Test Cases:
1. Objection: "D2L is too complex for our organization"
2. Objection: "We've invested heavily in Blackboard"
3. Objection: "Our budget doesn't allow LMS replacements"
4. Objection: "We need mobile-first learning"
5. Objection: "Integration with our SIS is critical"

Expected Outcome: Evidence-backed coaching with talk tracks
```

### Test Dataset C: Account Research (Specific)
```
Test Cases:
1. Account: Large state university system
2. Account: K-12 school district
3. Account: Corporate training department
4. Account: Healthcare training compliance
5. Account: International education provider

Expected Outcome: Contextual briefs with proof points
```

---

## LLM Provider Test Matrix

| Skill | Claude 3.5 Sonnet | Claude 3 Opus | Claude 3 Haiku | Gemini Pro |
|-------|-------------------|---------------|----------------|-----------|
| d2l-brain-search | ✅ Full | ✅ Full | ⚠️ Limited | ⚠️ Partial |
| d2l-sales-brief | ✅ Full | ✅ Full | ⚠️ Limited | ⚠️ Partial |
| d2l-objection-coach | ✅ Full | ✅ Full | ⚠️ Limited | ⚠️ Partial |
| d2l-proof-finder | ✅ Full | ✅ Full | ⚠️ Limited | ⚠️ Partial |
| d2l-brain-capture | ✅ Full | ✅ Full | ✅ Full | ⚠️ Limited |
| d2l-brain-curate | ✅ Full | ✅ Full | ✅ Full | ⚠️ Limited |
| d2l-brain-refresh | ✅ Full | ✅ Full | ✅ Full | ⚠️ Limited |
| d2l-change-radar | ✅ Full | ✅ Full | ⚠️ Limited | ⚠️ Partial |
| firecrawl | ✅ Full | ✅ Full | ✅ Full | ✅ Full |

---

## Test Execution Checklist

### Pre-Test Setup
- [ ] Test environment isolated from production
- [ ] Test data sets prepared and versioned
- [ ] LLM API credentials configured
- [ ] Test runners installed and verified
- [ ] Baseline metrics established
- [ ] Monitoring/logging configured

### Test Execution
- [ ] Unit tests pass (all skills)
- [ ] Integration tests pass (all workflows)
- [ ] Cross-provider tests show < 15% variance
- [ ] Performance tests meet SLA targets
- [ ] QA tests validate accuracy > 85%
- [ ] No regression detected

### Post-Test Validation
- [ ] Results documented
- [ ] Performance metrics logged
- [ ] Anomalies investigated
- [ ] Issues tracked and prioritized
- [ ] Reports generated
- [ ] Teams notified of status

---

## Continuous Testing Strategy

### Daily Tests (Automated)
- Unit tests on all skills
- Core workflow smoke tests
- Performance baselines
- Error rate monitoring

### Weekly Tests (Scheduled)
- Cross-provider validation
- Full workflow integration tests
- Quality assurance spot checks
- Competitive accuracy validation

### Monthly Tests (Comprehensive)
- Full test suite execution
- New LLM model evaluation
- Performance optimization review
- Workflow effectiveness assessment

### As-Needed Tests (Triggered)
- After skill updates
- After provider API changes
- When issues detected
- Before major releases
