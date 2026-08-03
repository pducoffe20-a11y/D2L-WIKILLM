---
tags:
  - navigation/entry-point
  - resource/documentation
  - system/orientation---
# D2L Sales Brain

The D2L Sales Brain is an Obsidian-compatible knowledge layer for Codex and other LLMs. It gives an assistant durable, searchable, source-linked sales knowledge without treating the model's memory as truth.

Its job is to help an LLM retrieve what D2L can safely say, understand the buyer and market context, select relevant proof, construct a defensible point of view, and identify what still needs validation.

## What this vault is

- A governed knowledge base for D2L product, industry, persona, proof, competitive, discovery, account, deal, engagement, objection, value, and business-case knowledge.
- A retrieval layer that Codex searches before answering.
- A provenance layer that preserves sources, dates, freshness, confidence, verification scope, and contradictions.
- A reasoning layer that connects evidence to seller decisions and buyer outcomes.
- A controlled learning loop for capturing and promoting useful new evidence.

It is not a CRM, a document dump, an autonomous source of customer truth, or permission for an LLM to send, publish, or update external systems.

## The core model

```text
approved sources
      ↓
capture and preserve engagement evidence
      ↓
90-Inbox
      ↓
review, deduplicate, verify, link, and project
      ↓
curated knowledge and account timelines
      ↓
brain_search.py
      ↓
LLM answer or seller artifact
      ↓
new evidence and gaps return to review
```

The reasoning contract is:

```text
verified fact
→ signal
→ interpretation
→ why it matters
→ seller decision
→ next action
→ desired buyer outcome
```

## Start here

The approved D2L-managed vault is:

`/Users/pducoffe/Library/CloudStorage/OneDrive-D2LCorporation/Documents/D2L-Sales-Brain`

### In Obsidian

1. Choose **Open folder as vault**.
2. Select the path above.
3. Open `00-System/Brain Dashboard.md`.
4. Keep personal vaults separate from this managed sales brain.

### In Codex

1. Open the vault as the workspace.
2. Codex reads `AGENTS.md` as its operating contract.
3. Ask the sales question naturally.
4. Codex searches the local brain first and checks approved live sources only when the evidence calls for it.

Example:

```bash
python3 scripts/brain_search.py \
  "build a business case for an association replacing a basic LMS" \
  --json
```

Useful prompts include:

- “Prepare discovery for a continuing-education leader evaluating Brightspace.”
- “Find approved customer proof for administrative efficiency in corporate learning.”
- “Compare Brightspace with Canvas, separating safe differentiation from claims to avoid.”
- “Build an account brief and label verified facts, hypotheses, unknowns, and next-best questions.”
- “Create a quantified business-case model, showing assumptions and sensitivity ranges.”

## Knowledge architecture

| Area | What the LLM should retrieve from it |
|---|---|
| `00-System` | policy, templates, dashboards, and governance |
| `01-Products` | capabilities, integrations, services, and safe claim boundaries |
| `02-Use-Cases` | buyer problems and solution patterns |
| `03-Industries` | pressures, buyers, proof, discovery, and objections |
| `04-Personas` | priorities, influence, questions, and messaging |
| `05-Customer-Proof` | curated, source-linked customer evidence |
| `06-Competitors` | fit, buyer rationale, discovery, differentiation, and unsafe claims |
| `07-Discovery` | qualification and current-state diagnosis |
| `08-Accounts` | account intelligence, hypotheses, risks, and open questions |
| `09-Meetings` | preparation and meeting artifacts |
| `13-Signals` | minimally copied, source-linked engagement events and reviewed engagement projections |
| `10-Objections` | objection diagnosis, evidence, response, and next step |
| `11-Deal-Advancement` | demo, validation, business-case, consensus, procurement, and proposal guidance |
| `12-Internal-Processes` | approved internal operating knowledge |
| `14-Buyer-Outcomes` | controlled outcome and value hypotheses |
| `15-Business-Cases` | templates, quantified models, assumptions, and sensitivity analysis |
| `90-Inbox` | unpromoted captured evidence |
| `95-Source-Index` | provenance and source inventory |
| `98-Needs-Review` | conflicts and proposed changes to governed knowledge |
| `99-Archive` | superseded or historical material |

## How the LLM decides what to trust

Every claim is evaluated across separate dimensions:

- **Status:** `verified`, `reviewed`, `disputed`, `stale`, or `synthetic`
- **Verification scope:** what exactly was confirmed
- **External-use posture:** `approved`, `source-check-required`, or `internal-only`
- **Authority:** how suitable the source is for the claim
- **Freshness:** whether the evidence is current enough
- **Confidence:** how strongly the available evidence supports the claim

`Verified` does not automatically mean “approved for any external statement.” A synthetic value model can be useful without being customer proof. A current Slack signal can be fresh without outranking canonical product documentation.

When credible sources conflict, the brain preserves the contradiction. It does not average or silently resolve it.

## Retrieval and live sources

The default order is:

1. Search the local vault.
2. Read the strongest matching notes and their sources.
3. Prefer current verified knowledge.
4. Check a live source when evidence is absent, stale, disputed, time-sensitive, or explicitly requested as current.
5. Return an evidence-bounded answer with gaps and next checks.

Approved connector roles:

- **SharePoint:** collateral, enablement, case studies, proposals, and product or service materials
- **Atlassian Rovo:** cross-system Confluence and Jira discovery
- **Slack:** bounded field intelligence, never approved messaging by itself
- **Sales:** read-only account and seller context
- **Public web:** D2L product pages, reputable industry sources, standards, regulators, and competitors' own current materials

Live connector use remains bounded by `config/source-allowlist.yaml`. Model memory is never a source.

## Knowledge lifecycle

```text
capture → normalize → classify → deduplicate → link
→ assess authority and freshness → review → verify → refresh or archive
```

New evidence enters through a dry-run capture:

```bash
python3 scripts/capture_note.py \
  --input path/to/selected-evidence.json \
  --dry-run
```

Persistence requires an approved storage path and allowlisted source. Captured content enters `90-Inbox`; it never becomes verified automatically. A proposed change to a verified claim goes to `98-Needs-Review`.

Store concise summaries and minimal excerpts rather than full documents or conversations.

### Live engagement data

The vault can hold a governed, source-linked record of meaningful buyer engagement: meeting evidence, buyer-stated commitments, approved email summaries, call summaries, and seller observations that remain explicitly labeled as internal activity. The model is defined in [[Live Engagement Data Model]] and the phased rollout in [[Live Engagement Data Implementation Plan]].

The engagement layer is deliberately not a CRM replica or an autonomous sync. Each event has an immutable source reference, a source date, a capture date, relationship links, a classification, and a confidence/status posture. The account, opportunity, person, and meeting notes are curated projections of that evidence; they never silently replace it. Ingestion remains allowlist-checked, dry-run first, and review-gated. Raw private contact details, full email bodies, DMs, restricted pricing, and customer-confidential material remain excluded under [[Source Policy]].

## Operating boundaries

The configured ingestion mode is `approved` for this exact D2L-managed OneDrive vault. Confirm the current state in `config/storage-approval.json` before writing.

Do not store credentials, private contact details, restricted pricing, customer-confidential content, personnel-sensitive material, DMs, group DMs, or other content excluded by `00-System/Source Policy.md`.

The brain supports research, assessment, and drafting. Sending messages, changing CRM records, creating tasks, modifying calendars, publishing, or writing to other external systems requires explicit authorization.

## Health and maintenance

Run from the vault root:

```bash
python3 scripts/validate_vault.py
python3 scripts/build_source_index.py
python3 scripts/detect_duplicates.py
python3 scripts/check_links.py
python3 scripts/check_stale.py
python3 scripts/refresh_queue.py
python3 scripts/vault_health.py
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Use the complete manual maintenance entrypoint:

```bash
./scripts/manual_refresh.sh
```

No recurring automation is implied by this repository. A scheduler requires separate, explicit authorization.

## Extending the brain

Add content when it improves a repeatable seller decision, not merely because a document exists.

A strong addition:

- answers a clear seller or buyer question;
- uses the correct folder and note type;
- cites the source and date;
- records status, verification scope, external-use posture, freshness, and confidence;
- separates evidence from interpretation;
- links to related product, persona, industry, proof, competitor, outcome, and account notes;
- states contradictions and missing evidence;
- identifies the decision or next action it supports.

`AGENTS.md` is the authoritative execution contract for an LLM. `00-System/Brain Dashboard.md` is the human navigation entrypoint. The templates in `00-System/Templates` define the preferred structure for new knowledge.
