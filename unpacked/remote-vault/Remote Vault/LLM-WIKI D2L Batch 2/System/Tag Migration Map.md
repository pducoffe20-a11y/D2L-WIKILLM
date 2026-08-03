---
id: tag-migration-map
title: "Tag Migration Map: Old → New System"
type: documentation
created: 2026-08-02
updated: 2026-08-02
status: active
tags: [ontology/metadata, ontology/system]
---

# Tag Migration Map: Old → New System

This document maps old tags to new consolidated tags during the system consolidation.

## Migration Rules

### OLD SYSTEM (10 categories) → NEW SYSTEM (9 categories)

| Old Category | New Category | Migration Rule |
|---|---|---|
| `entity/*` | `entity/*` | **Keep as-is** — no change |
| `content/*` | `content/*` | **Keep as-is** — no change |
| `sales/*` | `sales/*` | **Keep as-is** — no change |
| `navigation/*` | `navigation/*` | **Keep as-is** — no change |
| `ontology/*` | `ontology/*` | **Keep as-is** — no change |
| `ai/*` | `ai/*` | **Simplify** — drop confidence/recency, use status instead |
| `status/*` | `status/*` | **Keep as-is** — no change |
| `quality/*` | `status/*` | **Merge into status** |
| `review/*` | `status/*` | **Merge into status** |
| `maintenance/*` | `status/*` | **Merge into status** |
| `source-*` (ad-hoc) | `source/*` | **Formalize new category** |
| `topic/*` (ad-hoc) | `topic/*` | **Formalize new category** |

---

## Detailed Tag Mappings

### AI Tags (Simplified)

**Keep:**
- `ai/context/*` ✅
- `ai/processing/*` ✅

**Drop (migrate to status):**
- `ai/confidence/*` → Use `status/high-confidence`, `status/medium-confidence`, `status/low-confidence`
- `ai/recency/*` → Use `status/current`, `status/recent`, `status/dated`, `status/archived`
- `ai/quality/*` → Use `status/comprehensive`, `status/partial`, `status/sparse`

### Quality Tags (Merge into Status)

| Old Tag | New Tag |
|---|---|
| `quality/complete` | `status/complete` |
| `quality/comprehensive` | `status/comprehensive` |
| `quality/partial` | `status/partial` |
| `quality/sparse` | `status/sparse` |
| `quality/stub` | `status/stub` |

### Review Tags (Merge into Status)

| Old Tag | New Tag |
|---|---|
| `review/current` | `status/current` |
| `review/needs-update` | `status/needs-update` |
| `review/needs-verification` | `status/needs-verification` |
| `review/accuracy-check` | `status/accuracy-check` |
| `review/refresh-scheduled` | `status/refresh-scheduled` |

### Maintenance Tags (Merge into Status)

| Old Tag | New Tag |
|---|---|
| `maintenance/recent-update` | `status/recent-update` |
| `maintenance/stale-content` | `status/stale-content` |
| `maintenance/broken-links` | `status/broken-links` |
| `maintenance/incomplete-metadata` | `status/incomplete-metadata` |

### Source Tags (New Category - Formalized)

| Ad-hoc Pattern | New Tag |
|---|---|
| `source-salesforce` | `source/salesforce` |
| `source-boostup` | `source/boostup` |
| `source-confluence` | `source/confluence` |
| `source-external` | `source/external` |
| `source-internal` | `source/internal` |
| `source-system` | `source/system` |

### Topic Tags (New Category - Formalized)

| Ad-hoc Pattern | New Tag |
|---|---|
| `associations` | `topic/associations` |
| `Training-Org` | `topic/training-org` |
| `product-enablement` | `topic/product-enablement` |
| `resource` | `topic/resource` |

---

## Notes Affected by Migration

**Total notes to update**: ~50+ notes with old tags

### By Category:
- **quality/** tags: ~15 notes
- **review/** tags: ~8 notes
- **maintenance/** tags: ~5 notes
- **ai/confidence**, **ai/recency**, **ai/quality**: ~12 notes
- **source-*** ad-hoc: ~10 notes
- **topic-related** ad-hoc: ~5 notes

---

## Migration Process

1. Create new consolidated Tags Navigation.md
2. Update all notes with old tags → new tags
3. Verify all tags match new hierarchy
4. Delete old tag categories from system
5. Update any tag-based searches/filters

---

**Status**: Ready for execution  
**Created**: 2026-08-02  
**Migration Target**: Complete by 2026-08-02
