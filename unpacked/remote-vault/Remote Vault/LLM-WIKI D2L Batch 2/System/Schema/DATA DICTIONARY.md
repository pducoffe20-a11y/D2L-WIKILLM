# Data Dictionary

Required fields: `id`, `title`, `type`, `status`, `aliases`, `tags`, `source_system`, `source_title`, `source_url`, `source_date`, `captured_at`, `last_verified`, `review_after`, `source_owner`, `confidence`, `verification_scope`, `verification_basis`, `external_use`, `confidentiality`, `seller_relevance`, `related`.

`confidence` describes support strength within the declared scope, not source authority. `status` describes curation state. `verification_scope` states what was verified. `verification_basis` records why the scope passed. `external_use` controls whether source recheck or internal-only handling is required. `source_date` is when the source was authored or updated; `captured_at` is when evidence entered the workflow; `last_verified` is the last verification action; `review_after` is the next mandatory check.

Allowed verification scopes: `approved-library`, `document-read`, `record-confirmed`, `seller-guidance`, and `gap-confirmed`


Allowed external-use values: `approved`, `source-check-required`, and `internal-only`.

Relation labels supported in body or metadata: `supersedes`, `duplicate-of`, `conflicts-with`, `supports`, `derived-from`, `related-to`.

## Live engagement fields

`13-Signals` uses the required fields above plus these optional fields for `type: engagement-event`:

- `engagement_date`: ISO date of the observed interaction or signal; do not substitute an inferred date.
- `engagement_kind`: one of `meeting`, `email-summary`, `call-summary`, `research-signal`, `buyer-commitment`, `seller-observation`, or `other`.
- `engagement_party`: `buyer`, `seller`, `internal`, `public`, or `unknown`. This declares whose activity the event describes; it does not establish engagement quality.
- `account`, `opportunity`, `meeting`, and `people`: links or names only when identity is sufficiently certain.
- `source_ref`: a linked source record in `95-Source-Index` or permitted immutable source identifier. It is required for a material claim.
- `projection_status`: `unprojected`, `reviewed`, or `needs-review`; it tracks whether the event has safely informed a curated note, not whether a buyer acted.

An event is an append-only evidence record. Account, opportunity, meeting, and person notes are curated projections and must link back to the event and source. Do not add CRM identifiers, probability, stage, budget, timing, ownership, or buyer intent unless explicitly supported by a permitted source.

