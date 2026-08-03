# D2L Skills Testing - Quick Start Guide

## Overview
This guide provides a quick reference for testing D2L skills and understanding their workflow assignments across different LLM providers.

## Quick Reference

### What Are These Documents?

1. **SKILLS_INVENTORY.md** - Catalog of all 9 D2L skills with:
   - Detailed descriptions and purposes
   - LLM provider compatibility matrix
   - Recommended provider selection
   - Status and categorization

2. **WORKFLOW_ASSIGNMENTS.md** - Skill orchestration guide with:
   - 5 major workflow categories
   - Skill-to-workflow routing
   - Multi-LLM provider orchestration
   - Fallback chains and validation strategies

3. **SKILLS_TESTING_FRAMEWORK.md** - Comprehensive test framework defining:
   - Unit, integration, cross-provider, performance tests
   - Test scenarios and data sets
   - Continuous testing strategy
   - LLM provider test matrix

4. **test_skills.py** - Automated test runner that validates:
   - Skill file structure integrity
   - Skills registry completeness
   - Workflow assignment requirements
   - Provider support coverage

## Running Tests

### Basic Test Run
```bash
python3 test_skills.py
```

### View Test Results
```bash
cat test_results.json
```

### Expected Output
```
D2L Skills Testing Framework
Timestamp: 2026-08-03...

=== Skill Structure Validation ===
  ✓ PASS | structure_d2l-brain-search: Skill structure valid...
  ✓ PASS | structure_d2l-sales-brief: Skill structure valid...
  ... (all 9 skills)

=== Skills Registry Tests ===
  ✓ PASS | registry_skills_count: Registry contains 9 skills
  ✓ PASS | registry_categories: Skills organized in 7 categories...
  ✓ PASS | registry_providers: Multi-provider support...

=== Workflow Assignment Tests ===
  ✓ PASS | workflow_sales_research: Workflow has all required skills
  ... (5 workflows)

=== Test Summary ===
  Total: 17
  Passed: 17
  Pass Rate: 100.0%
```

## Skills at a Glance

### By Category

**Sales Enablement (3 skills)**
- d2l-sales-brief: Generate evidence-first briefs
- d2l-objection-coach: Coach objection responses
- d2l-proof-finder: Find customer proof points

**Knowledge Management (4 skills)**
- d2l-brain-search: Search vault intelligence
- d2l-brain-capture: Capture new insights
- d2l-brain-curate: Quality assurance
- d2l-brain-refresh: Update stale entries

**Market Intelligence (1 skill)**
- d2l-change-radar: Monitor changes

**Utilities (1 skill)**
- firecrawl: Web crawling & extraction

### By Primary Use

**Sales Research** → d2l-brain-search, d2l-change-radar
**Sales Coaching** → d2l-objection-coach, d2l-brain-search
**Account Planning** → d2l-sales-brief, d2l-brain-search
**Competitive Intel** → d2l-change-radar, d2l-brain-search
**Knowledge Mgmt** → d2l-brain-capture, d2l-brain-curate, d2l-brain-refresh

## Workflow Selection Guide

### Need to prepare for a sales call?
1. **Research Phase**: Use `d2l-brain-search` to gather vault intelligence
2. **Brief Phase**: Run `d2l-sales-brief` for comprehensive brief
3. **Coaching Phase**: Use `d2l-objection-coach` for anticipated objections
→ **Best Provider**: Claude 3.5 Sonnet

### Need to handle a buyer objection?
1. **Identify Objection**: Classify type and context
2. **Get Evidence**: Run `d2l-objection-coach` for talk track
3. **Supplement**: Use `d2l-brain-search` if gaps found
→ **Best Provider**: Claude 3.5 Sonnet or Opus (for complex objections)

### Need to plan an account strategy?
1. **Research**: Run `d2l-brain-search` for account context
2. **Brief**: Generate `d2l-sales-brief` for opportunity
3. **Monitor**: Use `d2l-change-radar` for changes
4. **Evidence**: Find `d2l-proof-finder` for relevant proof
→ **Best Provider**: Claude 3.5 Sonnet

### Need to update the knowledge base?
1. **Capture**: Use `d2l-brain-capture` to structure new insight
2. **Curate**: Run `d2l-brain-curate` for quality check
3. **Refresh**: Use `d2l-brain-refresh` for versioning
→ **Best Provider**: Claude 3.5 Sonnet (primary), Opus (complex), Haiku (bulk)

### Need current web data?
1. **Crawl**: Use `firecrawl` to extract web content
2. **Supplement**: Feed results to other skills
→ **Best Provider**: Claude 3.5 Sonnet, Opus, or Haiku

## LLM Provider Quick Reference

### Claude 3.5 Sonnet ⭐ (Recommended Default)
- **Best for**: All skills, complex reasoning, primary orchestration
- **Strengths**: Strongest reasoning, best objection handling, optimal synthesis
- **Use when**: You need the best quality, have complex requirements
- **Cost**: Standard

### Claude 3 Opus
- **Best for**: Complex scenarios, enterprise deals, detailed analysis
- **Strengths**: Enhanced reasoning, long context window, detailed synthesis
- **Use when**: Dealing with complex competitive dynamics or enterprise accounts
- **Cost**: Standard

### Claude 3 Haiku
- **Best for**: Quick queries, bulk processing, routine tasks
- **Strengths**: Fast, efficient, lower cost, good for simple questions
- **Use when**: High-volume processing, quick turnaround needed
- **Cost**: Lower

### Google Gemini Pro (Secondary Support)
- **Best for**: Parallel validation, cross-provider verification
- **Strengths**: Different model perspective, good for validation workflows
- **Limitations**: May require prompt adjustments, limited reasoning depth
- **Use when**: Need cross-validation on high-stakes decisions
- **Cost**: Comparable

## Test Results Interpretation

### What Does 100% Pass Rate Mean?
- All 9 skills have proper structure and documentation
- Skills are correctly categorized (7 categories)
- All workflows have required skills
- Multi-LLM provider support is configured

### What If a Test Fails?
1. **Structure Failure**: Skill file missing or incorrectly organized
2. **Registry Failure**: Skill not registered in SKILLS_INVENTORY.md
3. **Workflow Failure**: Workflow missing required skills
→ See SKILLS_TESTING_FRAMEWORK.md for detailed diagnostics

## Next Steps

### To Implement a Workflow
1. Read relevant section in WORKFLOW_ASSIGNMENTS.md
2. Select skills from Skill-to-Workflow Matrix
3. Choose LLM provider based on use case
4. Implement orchestration logic
5. Run tests with test_skills.py
6. Monitor performance with test framework

### To Test a New Feature
1. Add test case to SKILLS_TESTING_FRAMEWORK.md
2. Create test data set in Test Data Sets section
3. Add validation to test_skills.py
4. Run full test suite
5. Review results in test_results.json

### To Add a New Skill
1. Create skill directory structure: `skills/skill-name/skill-name/SKILL.md`
2. Register in SKILLS_INVENTORY.md with:
   - Name, category, description
   - Supported LLM providers
   - Workflow assignments
3. Update WORKFLOW_ASSIGNMENTS.md if needed
4. Run test_skills.py to validate
5. Commit and push changes

## File Structure

```
D2L-WIKILLM/
├── README.md                           # Repository overview
├── SKILLS_INVENTORY.md                 # Skills catalog & matrix
├── WORKFLOW_ASSIGNMENTS.md             # Workflow orchestration guide
├── SKILLS_TESTING_FRAMEWORK.md        # Testing methodology
├── SKILLS_TESTING_QUICKSTART.md       # This file
├── test_skills.py                      # Automated test runner
├── test_results.json                   # Latest test results
├── .github/workflows/main.yml          # GitHub Actions workflow
└── unpacked/remote-vault/
    └── Remote Vault/skills/
        ├── d2l-brain-search/
        ├── d2l-sales-brief/
        ├── d2l-objection-coach/
        ├── d2l-proof-finder/
        ├── d2l-brain-capture/
        ├── d2l-brain-curate/
        ├── d2l-brain-refresh/
        ├── d2l-change-radar/
        └── firecrawl/
```

## Troubleshooting

### Test Script Not Found
```bash
cd /home/user/D2L-WIKILLM
chmod +x test_skills.py
python3 test_skills.py
```

### Skills Directory Not Found
The skills are extracted from `Remote Vault.zip` into `unpacked/` directory during GitHub Actions workflow. If missing, check that unpacking completed successfully.

### Import Errors
Ensure Python 3.6+ is available:
```bash
python3 --version
```

## Support & Documentation

- **SKILLS_INVENTORY.md**: Full skill catalog with provider matrix
- **WORKFLOW_ASSIGNMENTS.md**: Workflow design and routing
- **SKILLS_TESTING_FRAMEWORK.md**: Testing methodology and scenarios
- **test_skills.py**: Validation framework (runnable)

## Key Metrics to Monitor

After deploying workflows, track:

1. **Skill Performance**
   - Response latency (p50, p95, p99)
   - Success rate per skill
   - Error rate by provider

2. **Workflow Effectiveness**
   - Time to generate brief/coaching/research
   - User satisfaction scores
   - Accuracy against ground truth

3. **Provider Comparison**
   - Quality variance between providers (< 15% is good)
   - Cost per task
   - Latency comparison

4. **Knowledge Base Health**
   - Vault entry quality
   - Update frequency
   - Search result relevance

## Questions?

Refer to:
1. SKILLS_INVENTORY.md for skill details
2. WORKFLOW_ASSIGNMENTS.md for routing decisions
3. SKILLS_TESTING_FRAMEWORK.md for test methodology
4. test_skills.py for validation implementation
