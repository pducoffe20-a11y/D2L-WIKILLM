---
id: system-hub-readme
title: System Files Hub
type: resource
created: 2026-08-02
updated: 2026-08-02
status: active
category: system
---

# System Files Hub

Central repository for vault infrastructure, configuration, schema, and health monitoring. This folder contains everything needed to understand how the vault is structured and maintained.

## 📁 Folder Organization

### 01-Schema
Vault structure, data model, and standardization documents.

- **SCHEMA.md** — Standardized frontmatter schema for all notes (required metadata fields)
- **Data Dictionary.md** — Definitions of key terms, fields, and concepts used across vault
- **Knowledge Standards.md** — Quality standards for content, evidence, and claims

**Use**: Understanding vault structure, applying metadata, ensuring consistency

### 02-Configuration
System configuration, access controls, and source allowlists.

- **source-allowlist.yaml** — Approved sources for evidence capture (SharePoint, Slack, Confluence, Jira, Outlook)
- **storage-approval.json** — Storage permissions and site/space approvals
- **vault-settings.md** — Centralized reference for vault-level settings (generated on consolidation)

**Use**: Managing source access, understanding what external systems are connected

### 03-Integrations
Third-party skill integrations and external data connections.

**Contents** (mostly in `/skills/integrations/`):
- Integration documentation and routing contracts
- Setup and usage guides for external skills
- Evidence contracts and data validation rules

**Current Integrations**:
- `last30days` — Public web research (Reddit, X, YouTube, TikTok, HN, GitHub)

**Use**: Understanding external data sources, skill routing, evidence validation

### 04-Vault-Health
Monitoring, reporting, and quality metrics for vault operations.

- **Vault Health Report.md** — Current state of vault, metrics, issues
- **Retrieval Acceptance Report.md** — Success rates and quality metrics for retrieval
- **Promotion Review - 2026-07-30.md** — Latest promotion review and findings
- **Health Check Schedule.md** — Regular monitoring cadence (generated on consolidation)

**Use**: Tracking vault quality, identifying maintenance needs, monitoring trends

---

## 🔍 Key Documents

| Document | Purpose | Location |
|----------|---------|----------|
| Vault Schema | Metadata standards for all notes | `01-Schema/SCHEMA.md` |
| Data Dictionary | Definitions of vault terms | `01-Schema/Data Dictionary.md` |
| Quality Standards | Content and evidence standards | `01-Schema/Knowledge Standards.md` |
| Source Allowlist | Approved sources for capture | `02-Configuration/source-allowlist.yaml` |
| Health Reports | Vault metrics and status | `04-Vault-Health/` |

---

## 🚀 Common Tasks

### Understand Vault Structure
1. Read `01-Schema/SCHEMA.md` — Learn required metadata
2. Read `01-Schema/Data Dictionary.md` — Understand terminology
3. Check `/skills/_SKILLS_ROOT_INDEX.md` — Learn available skills

### Add New Evidence
1. Check `02-Configuration/source-allowlist.yaml` — Is source approved?
2. Use `d2l-brain-capture` skill — Normalize the evidence
3. Use `d2l-brain-curate` skill — Review quality

### Monitor Vault Health
1. Review `04-Vault-Health/Vault Health Report.md` — Current status
2. Run `d2l-change-radar` — Detect recent changes
3. Check `04-Vault-Health/Health Check Schedule.md` — Next review due

### Access External Data
1. Check `03-Integrations/` — Available integrations
2. Review integration docs (in `skills/integrations/`)
3. Use appropriate integration skill (e.g., `last30days`)

---

## 📋 Consolidation Notes

**Consolidation Date**: 2026-08-02  
**Version**: 1.0

This folder was created to centralize previously scattered system files:
- Schema documents (moved from `00-System/`)
- Configuration files (moved from `config/`)
- Integration docs (moved from `references/` and `skills/`)
- Health reports (moved from `00-System/`)

---

**Last Updated**: 2026-08-02
