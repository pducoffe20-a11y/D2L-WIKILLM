---
id: live-engagement-data-model-v1
title: Live Engagement Data Model
type: internal-process
status: reviewed
aliases:
  - engagement data model
  - engagement curation model
tags:
  - navigation/system
  - resource/reference
  - system/architecture
  - system/data-model
source_system: internal-design
source_title: Knowledge curator specification supplied by Pat
source_url: urn:d2l-sales-brain:design:live-engagement-data-model:2026-07-31
source_date: 2026-07-31
captured_at: 2026-07-31T00:00:00-04:00
last_verified: 2026-07-31
review_after: 2026-08-30
source_owner: Pat
confidence: high
verification_scope: seller-guidance
verification_basis: Reviewed against the vault operating contract, storage approval, and source policy; no connector or external system behavior is asserted.
external_use: internal-only
confidentiality: internal
seller_relevance: Defines how permitted live engagement evidence becomes connected, reviewable sales knowledge without becoming CRM truth.
related:
  - Live Engagement Data Implementation Plan
  - Engagement Event Template
  - Data Dictionary
  - Source Policy
  - Account Intelligence Templates---

# Live Engagement Data Model

## Purpose

Add a governed engagement-evidence layer to the Obsidian brain so a seller can retrieve meaningful interactions alongside reusable product and market knowledge. It supports meeting preparation, opportunity advancement, discovery continuity, and evidence freshness. It is not a CRM replacement, an automatic sync, or a claim that the buyer has progressed.

## Canonical record and projections

```text
permitted source or source summary
        -> source record / immutable reference
        -> 13-Signals engagement event
        -> review and relationship check
        -> curated projections: account, opportunity, meeting, person, decision
```

The source reference and the engagement event are canonical for this layer. Curated notes may summarize durable conclusions, but each material conclusion must link back to the source and event. Preserve a conflict as competing source-linked events; do not overwrite a prior conclusion.

## What qualifies as an event

Create a small `engagement-event` only for material buyer interaction, buyer-stated need or constraint, commitment, decision, risk, public account development, or clearly labeled seller/internal observation. Use [[Engagement Event Template]]. Routine activity, copies of raw content, and duplicate summaries do not qualify.

Classify who the event represents. `buyer` indicates buyer-originated evidence, `seller` or `internal` indicates D2L activity, and `public` indicates public research. None of these labels establishes deal stage, intent, probability, budget, ownership, or timing.

## Evidence and privacy boundary

Follow [[Source Policy]] and the approved source allowlist. Preserve a concise summary and an immutable source reference rather than copying full transcripts, full emails, or conversations. Exclude DMs, private contact information, credentials, customer-confidential content, restricted pricing, personnel-sensitive information, and non-allowlisted data.

Meeting and email evidence must retain source date, capture date, participants or author only when permitted, confidentiality, and reliability. Attribute important statements. A seller’s draft, a Sales lookup, and internal preparation are not buyer engagement.

## Required relationships

Link an event only where identity and relevance are clear:

- event -> source record
- event -> account
- event -> opportunity, when one is evidenced
- event -> meeting and people, when applicable
- event -> decision, commitment, risk, discovery question, capability, proof need, or competitor note when it changes seller reasoning

Update a map or curated note only when the link makes the item materially easier to retrieve. Do not create links for graph density.

## Curation workflow

1. Inspect the provided source and search the vault for existing account, person, meeting, opportunity, and source records.
2. Deduplicate; flag identity ambiguity rather than merging similar names or organizations.
3. Preserve the source reference and capture a minimal event with frontmatter defined in [[00-System/Data Dictionary]].
4. Separate direct evidence, buyer language, interpretation, unknowns, and recommended action.
5. Update a curated projection only with source-backed, durable knowledge; link it back to the event.
6. Route conflicts, proposed changes to verified content, or unclear identity to `98-Needs-Review`.
7. Run vault validation, duplicate detection, and link checks.

## Dashboard implications

The dashboard shows an evidence timeline and routes to account, meeting, opportunity, and source context. It must not present inferred pipeline fields as facts, hide confidence/freshness, or imply live connector synchronization. The Dataview block in [[Brain Dashboard]] is optional and read-only.

## Sources

- [[Source Policy]]
- [[00-System/Data Dictionary]]
- [[Engagement Event Template]]

## Change history

- 2026-07-31: Created as reviewed internal design from the supplied curator specification; connector ingestion remains out of scope.
