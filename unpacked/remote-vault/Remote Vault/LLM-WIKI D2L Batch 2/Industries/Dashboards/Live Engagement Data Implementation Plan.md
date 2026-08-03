---
id: live-engagement-data-implementation-plan-v1
title: Live Engagement Data Implementation Plan
type: internal-process
status: reviewed
aliases:
  - engagement rollout plan
tags:
  - navigation/system
  - resource/reference
  - system/architecture
  - system/implementation
source_system: internal-design
source_title: Knowledge curator specification supplied by Pat
source_url: urn:d2l-sales-brain:design:live-engagement-rollout:2026-07-31
source_date: 2026-07-31
captured_at: 2026-07-31T00:00:00-04:00
last_verified: 2026-07-31
review_after: 2026-08-30
source_owner: Pat
confidence: high
verification_scope: seller-guidance
verification_basis: Implementation plan reviewed against current vault controls; it proposes no source ingestion or external-system action.
external_use: internal-only
confidentiality: internal
seller_relevance: Phases engagement-data adoption without compromising evidence, privacy, or review controls.
related:
  - Live Engagement Data Model
  - Brain Dashboard
  - Engagement Event Template
  - Source Policy---

# Live Engagement Data Implementation Plan

## Outcome

The Obsidian brain gains a source-linked, reviewable engagement timeline that connects durable meeting and account intelligence to the existing knowledge map. It remains distinct from CRM state and requires no connector writeback.

## Phase 1 - Foundation (completed in this change)

- Define the canonical event/projection model in [[Live Engagement Data Model]].
- Add `13-Signals` as the engagement-event location and add [[Engagement Event Template]].
- Extend [[00-System/Data Dictionary]], [[Brain Dashboard]], [[LLM-WIKI D2L/README]], and `AGENTS.md` with the same governance and retrieval model.
- Add dashboard links and an optional read-only Dataview timeline.

Acceptance: a curator can capture a permitted, source-linked event without inferring pipeline or buyer facts; it is discoverable from the dashboard and passes vault checks.

## Phase 2 - Controlled pilot (requires selected permitted sources)

- Choose a small, explicit batch of source summaries or transcripts that are allowed for this vault.
- Run dry-run capture, duplicate checks, and identity review.
- Create source records and event notes; project only durable facts into account, meeting, opportunity, and people notes.
- Review the resulting account timeline for retrieval usefulness, source traceability, privacy, and false engagement risk.

Acceptance: every material claim points to a source/event; the pilot includes no prohibited content, ambiguous merges, or unsupported CRM-like fields.

## Phase 3 - Connector design (requires explicit authorization and allowlist change)

- Name the connector, source containers, data minimization rule, retention scope, cadence, and owner.
- Extend `config/source-allowlist.yaml` only after approval.
- Implement dry-run, deduplication, provenance, and review-queue behavior before persistent ingestion.
- Verify that the connector is read-only and does not create CRM records, tasks, calendar objects, or messages.

Acceptance: a test run produces reviewable, minimally copied candidate records with no side effects.

## Phase 4 - Operational dashboard (after pilot validation)

- Add curated views for recent buyer-originated evidence, stale account evidence, commitments with explicitly stated owners/dates, unresolved conflicts, and unprojected events.
- Keep source, status, confidence, freshness, and party visible on every card or query result.
- Provide drill-through to the event and source rather than a dashboard-only summary.

Acceptance: the dashboard answers “what changed, what is evidenced, what is unknown, and what should I review next?” without conflating internal activity with buyer engagement.

## Relationship audit standard

After each capture batch, inspect the event-to-source link, identity links, and relevant account/opportunity/meeting projections. Run duplicate detection and broken-link validation. Treat a missing material link as a review item; do not create speculative or decorative links.

## Sources

- [[Live Engagement Data Model]]
- [[Source Policy]]
- [[Engagement Event Template]]

## Change history

- 2026-07-31: Initial phased plan created; no source ingestion or connector configuration performed.
