---
tags:
  - resource/reference
  - source/policy
  - system/governance
  - navigation/system---
# Source Policy

## Security gate

The exact D2L-managed OneDrive vault path is approved for D2L internal information. Source access remains default-deny and is limited to the explicit container IDs and paths in `config/source-allowlist.yaml`. Approval does not authorize indiscriminate ingestion, publishing, messaging, CRM changes, tasks, or calendar changes.

## Authority hierarchy

1. Current approved SharePoint or Confluence documentation
2. Current product, enablement, policy, or implementation documentation
3. Approved customer stories, proposals, and win summaries
4. Current Jira evidence about actual behavior
5. Slack decisions from identifiable owners
6. Slack field observations and seller commentary
7. Personal notes
8. Model inference

Authority and freshness are separate scores. Preserve conflicts. Never let newer, lower-authority Slack content silently overwrite canonical documentation.

## Minimum-copy rule

Store a concise summary, minimal excerpt when necessary, exact source link, source date, capture time, owner, confidence, verification scope, verification basis, external-use posture, confidentiality, and review date. Do not archive full documents or threads by default.

Published portal pages and navigation hubs may be used to locate evidence, but their link labels are not themselves proof of a product capability, customer outcome, implementation behavior, or competitive claim. Validate the underlying source before filling a gap.

## Verification scope

`verified` means the note passed review at its declared `verification_scope`; it does not mean every sentence is an externally approved universal claim.

- `approved-library`: The source is stored in an allowlisted D2L SharePoint sales-content library. Its existence, provenance, and status as real internal sales content are verified. Content may be used internally according to its own audience, speaker notes, confidentiality, freshness, and caveats.
- `document-read`: The source document was opened and the note accurately represents its relevant content.
- `record-confirmed`: The underlying record and source link are confirmed, but exact claim wording or metrics may still require source readback.
- `seller-guidance`: Seller interpretation, questions, talk tracks, or playbook guidance were reviewed against approved sources. Reasonable interpretation is allowed when labeled and bounded.
- `gap-confirmed`: A defined search did not locate supporting content. This verifies the gap, not the missing claim.

All sales-relevant content stored within the approved SharePoint Sales Portal and allowlisted SharePoint sites may pass verification at `approved-library` scope. It does not require sentence-by-sentence claim extraction. This scope includes current decks, playbooks, templates, internal guidance, customer-proof indexes, and enablement material.

`external_use` is evaluated separately:

- `approved`: explicitly approved for the stated external use.
- `source-check-required`: valid internal sales content; confirm the current source, context, permissions, and exact wording before external reuse.
- `internal-only`: internal guidance, working material, restricted context, or a gap record.

Verification scope, confidence, freshness, confidentiality, and external-use posture are independent. Internal notes, placeholders, indicative timelines, customer-scoped metrics, and speaker instructions remain valid library content but must not be stripped of their context.

## Exclusions

No DMs, group DMs, bot noise, credentials, private contact information, restricted pricing, customer-confidential content, secrets, personnel-sensitive information, or unsupported opinions.
