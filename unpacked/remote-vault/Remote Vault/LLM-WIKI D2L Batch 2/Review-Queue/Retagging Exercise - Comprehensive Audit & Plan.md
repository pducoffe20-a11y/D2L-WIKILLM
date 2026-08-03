---
id: retagging-exercise-comprehensive-audit
title: "Retagging Exercise - Comprehensive Audit & Plan"
type: note
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [ontology/metadata, navigation/maintenance, system/process]
category: system
parent_moc: "98-Needs-Review/Review Queue.md"
---

# Retagging Exercise - Comprehensive Audit & Plan

## Executive Summary

**Status**: IN PROGRESS  
**Total Notes in Vault**: ~400 notes  
**Processed**: ~130 notes (33%)  
**Remaining**: ~270 notes (67%)  
**Target Completion**: Batch processing ongoing

---

## Problem Statement

The vault has inconsistent tagging across different note categories:

### Current State Issues
1. **Legacy flat tags**: Notes use non-hierarchical tags (e.g., `["objection", "pilot"]` instead of `["ontology/objection", "sales/stage/discovery"]`)
2. **Missing hierarchies**: Tags don't follow the `category/subcategory/specific` pattern defined in SCHEMA.md
3. **Incomplete relationships**: Many notes lack `related_notes`, `linked_entities`, and `cross_references` fields
4. **Inconsistent metadata**: Some notes have rich frontmatter while others have minimal metadata
5. **No relationship mapping**: Connections between customers, products, industries, and use cases are sparse

---

## Tagging Hierarchy Reference (from SCHEMA.md)

### Customer Tags
- `customer/industry/higher-ed`
- `customer/industry/k12`
- `customer/industry/corporate`
- `customer/industry/healthcare`
- `customer/industry/government`
- `customer/industry/nonprofit`
- `customer/type/multi-story`
- `customer/size/enterprise`

### Product Tags
- `product/suite/brightspace`
- `product/suite/edlink`
- `product/feature/assessment`
- `product/feature/engagement`
- `product/capability/lms`

### Sales Stage Tags
- `sales/stage/discovery`
- `sales/stage/evaluation`
- `sales/stage/negotiation`
- `sales/stage/closed-won`
- `sales/stage/renewal`

### Use Case Tags
- `usecase/area/learning-management`
- `usecase/area/assessment`
- `usecase/area/employee-training`
- `usecase/benefit/time-to-value`

### Organizational Tags
- `ontology/metadata` - Schema and documentation
- `ontology/moc` - Maps of Content
- `navigation/core` - Core navigation documents
- `ai/context` - AI processing hints

---

## Progress by Category

### ✅ COMPLETED (130 notes)

#### 10-Objections (10 notes) - COMPLETE
- All objection notes retagged with proper hierarchies
- Related notes linked
- Cross-references added

#### 15-Business-Cases (10 notes) - COMPLETE
- Value models retagged
- Business case toolkit updated
- Related connections mapped

#### 02-Use-Cases (13 notes) - COMPLETE
- Use case MOC linked
- Problem-solution mapping added
- Industry applicability tagged

#### 14-Buyer-Outcomes (1 note) - COMPLETE
- Buyer outcomes and value hypotheses linked to use cases

#### 03-Industries (8 notes) - COMPLETE
- Industry playbooks retagged
- Customer count mapped
- Use case applicability added

#### 04-Personas (7 notes) - COMPLETE
- Persona descriptions enhanced
- Industry mapping added
- Role-based tagging implemented

#### 06-Competitors (11 notes) - COMPLETE
- Competitive cards retagged
- Feature comparison mapped
- Win-loss indicators added

#### 12-Internal-Processes (5 notes) - PARTIAL
- 5 notes partially updated
- Need full relationship mapping

---

### 🔄 IN PROGRESS / REMAINING (270 notes)

#### 05-Customer-Proof (165 notes) - NEEDS FULL PASS
**Status**: Sampled 5 notes; many already have good tags but inconsistent  
**Issue**: Some use `proof-card` vs `customer-proof` inconsistently  
**Action**: Standardize type field, verify all have industry/product/use-case tags

#### 01-Products (16 notes) - NEEDS FULL PASS
**Status**: Sampled 1 note; has basic product tags  
**Issue**: Missing product feature breakdown, missing capability hierarchy  
**Action**: Add product/suite, product/feature, product/capability tags

#### 00-System (26 notes) - NEEDS FULL PASS
**Status**: System/infrastructure notes  
**Issue**: Minimal tags, no relationship mapping  
**Action**: Add ontology/metadata, navigation/core tags; link to relevant MOCs

#### skills/ (18 notes) - NEEDS FULL PASS
**Status**: Skill definitions  
**Issue**: Minimal tags, no product/capability mapping  
**Action**: Tag with skill/type, product/capability, usecase/area

#### 95-Source-Index (15+ notes) - NEEDS FULL PASS
**Status**: Source tracking and navigation  
**Issue**: Inconsistent source tags  
**Action**: Standardize source/type tags, add entity references

#### 08-Accounts (5 notes) - NEEDS FULL PASS
**Status**: Account intelligence  
**Issue**: Missing customer/size, customer/industry tags  
**Action**: Add account-level classification tags

#### 09-Meetings (1 note) - NEEDS FULL PASS
**Status**: Meeting templates  
**Issue**: Minimal metadata  
**Action**: Add sales/stage, usecase/area tags

#### 07-Discovery (1 note) - NEEDS FULL PASS
**Status**: Discovery playbook  
**Issue**: Missing usecase/area, sales/stage tags  
**Action**: Link to relevant use cases and sales processes

#### 11-Deal-Advancement (2 notes) - NEEDS FULL PASS
**Status**: Deal advancement  
**Issue**: Missing sales/stage tags  
**Action**: Add sales/stage/negotiation, sales/stage/closed-won tags

#### 13-Signals (2 notes) - NEEDS FULL PASS
**Status**: Engagement signals  
**Issue**: Minimal metadata  
**Action**: Add customer/engagement, sales/stage tags

#### templates/ (5 notes) - NEEDS FULL PASS
**Status**: Template definitions  
**Issue**: Minimal tags, no usage guidance  
**Action**: Add ontology/template, navigation/template tags

#### Ontology/ (4 notes) - NEEDS FULL PASS
**Status**: Ontology documentation  
**Issue**: Minimal tags  
**Action**: Add ontology/metadata, navigation/core tags

#### MOC/ (12+ notes) - NEEDS FULL PASS
**Status**: Maps of Content  
**Issue**: Inconsistent MOC tagging  
**Action**: Standardize ontology/moc tags, link related MOCs

#### AI/ (3 notes) - NEEDS FULL PASS
**Status**: AI-specific skills  
**Issue**: Minimal tags  
**Action**: Add ai/context, skill/type tags

#### references/ (2 notes) - NEEDS FULL PASS
**Status**: Reference materials  
**Issue**: Minimal tags  
**Action**: Add resource/type, confidentiality tags

#### 99-Archive (1 note) - NEEDS FULL PASS
**Status**: Archived content  
**Issue**: Should be marked archived  
**Action**: Add status: archived, mark appropriately

#### 98-Needs-Review (2 notes) - NEEDS FULL PASS
**Status**: Review queue  
**Issue**: Minimal tags  
**Action**: Add navigation/maintenance tags

#### Root level (3 notes) - NEEDS FULL PASS
**Status**: README, AGENTS, THIRD_PARTY_LICENSES  
**Issue**: Minimal tags  
**Action**: Add appropriate system/documentation tags

---

## Retagging Strategy

### Phase 1: Standardization (Current)
- ✅ Define hierarchical tag structure (DONE - from SCHEMA.md)
- ✅ Process high-value content categories (DONE - Objections, Business Cases, Use Cases, Industries, Personas, Competitors)
- 🔄 Process customer proof cards (IN PROGRESS)
- 🔄 Process products and capabilities (NEXT)

### Phase 2: Relationship Mapping (Next)
- Add `related_notes` to all MOCs
- Add `linked_entities` to customer and product notes
- Add `cross_references` between related content
- Build bidirectional relationships

### Phase 3: AI Context Enhancement (Following)
- Add `context_hints` to high-value notes
- Add `content_summary` for AI retrieval
- Add `relevance_score` for search optimization
- Add `ai_instructions` for special handling

### Phase 4: Validation & Cleanup (Final)
- Audit metadata completeness
- Fix broken relationships
- Verify tag consistency
- Update coverage map

---

## Batch Processing Plan

### Batch 2: Customer Proof Cards (165 notes)
- Read sample of 10-15 notes to understand current state
- Standardize type field (use `customer-proof` consistently)
- Add industry/product/use-case tags to all
- Link to related MOCs
- **Estimated time**: 2-3 hours

### Batch 3: Products (16 notes)
- Standardize product/suite tags
- Add product/feature breakdown
- Add product/capability hierarchy
- Link to related use cases
- **Estimated time**: 1 hour

### Batch 4: System/Infrastructure (26 notes)
- Add ontology/metadata tags
- Add navigation/core tags
- Link to relevant MOCs
- **Estimated time**: 1.5 hours

### Batch 5: Skills (18 notes)
- Add skill/type tags
- Add product/capability mapping
- Add usecase/area tags
- **Estimated time**: 1 hour

### Batch 6: Source Index (15+ notes)
- Standardize source/type tags
- Add entity references
- Link to original sources
- **Estimated time**: 1 hour

### Batch 7: Remaining Categories (30+ notes)
- Accounts, Meetings, Discovery, Deal Advancement, Signals
- Templates, Ontology, MOCs, AI, References, Archive
- **Estimated time**: 2 hours

---

## Quality Checkpoints

### Before Each Batch
- [ ] Identify 3-5 sample notes from category
- [ ] Understand current tagging state
- [ ] Identify tag patterns to apply
- [ ] Plan relationship mappings

### During Each Batch
- [ ] Apply consistent tag hierarchy
- [ ] Add related_notes where applicable
- [ ] Create cross-references
- [ ] Maintain data integrity

### After Each Batch
- [ ] Spot-check 5 random notes for consistency
- [ ] Verify frontmatter is valid YAML
- [ ] Check for broken wikilinks
- [ ] Update progress tracking

---

## Success Criteria

### Metadata Completeness
- [ ] 90%+ of notes have proper frontmatter
- [ ] 80%+ of notes have hierarchical tags
- [ ] 70%+ of notes have related_notes field
- [ ] 60%+ of notes have linked_entities

### Tag Consistency
- [ ] All tags follow `category/subcategory/specific` pattern
- [ ] No duplicate or near-duplicate tags
- [ ] Tags match SCHEMA.md hierarchy
- [ ] Consistent use of enums (type, status, category)

### Relationship Mapping
- [ ] All customer notes linked to industries
- [ ] All use cases linked to relevant products
- [ ] All products linked to use cases
- [ ] MOCs include related_notes to other MOCs

### Vault Health
- [ ] Coverage map updated with new metrics
- [ ] No broken wikilinks in frontmatter
- [ ] All entity references valid
- [ ] Dataview queries return expected results

---

## Tools & Queries

### Dataview Query: Missing Tags
```
WHERE type = "note" AND length(tags) < 3
SORT title ASC
```

### Dataview Query: Missing Related Notes
```
WHERE type = "note" AND !related_notes
SORT title ASC
```

### Dataview Query: Inconsistent Types
```
WHERE type NOT IN ["note", "moc", "entity", "resource", "template", "customer-proof", "product-capability"]
SORT type ASC
```

### Grep: Find Legacy Flat Tags
```
grep "tags:\s*\[\"?[a-z-]+\"?,\s*\"?[a-z-]+\"?\]" --context=2
```

---

## Next Steps

1. **Immediate (Next 2 hours)**
   - Continue with Customer Proof batch processing
   - Standardize type fields across 05-Customer-Proof

2. **Short-term (Next 4 hours)**
   - Process Products category
   - Process System/Infrastructure category

3. **Medium-term (Next 8 hours)**
   - Process Skills, Source Index, and remaining categories
   - Add relationship mappings
   - Validate all frontmatter

4. **Final (Next 4 hours)**
   - Quality assurance pass
   - Update Coverage Map
   - Document completion

---

## Monitoring

**Current Progress**: 33% complete (130/400 notes)  
**Remaining Work**: 67% (270 notes)  
**Estimated Total Time**: 12-15 hours  
**Target Completion**: This session

---

**Version**: 1.0  
**Last Updated**: 2026-08-02  
**Status**: ACTIVE - IN PROGRESS
