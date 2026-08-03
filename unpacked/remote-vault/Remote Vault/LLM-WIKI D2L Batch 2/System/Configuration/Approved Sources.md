---
tags:
  - resource/reference
  - source/policy
  - system/governance
  - navigation/system---
# Approved Sources

Default deny. Pat approved the reusable sales-relevant source containers below on 2026-07-30. Approval permits bounded read-only discovery and inbox capture; it does not approve indiscriminate ingestion.

## SharePoint

Eleven D2L SharePoint sites are allowlisted in `config/source-allowlist.yaml`: Sales Assets, Product Marketing Assets, Proposal Hub, Customer Marketing, Customer Marketing Hub, Content Marketing, International Marketing, Sales Operations, Custom SOWs, D2LDEX, and Enterprise Sales.

### D2L Sales Assets site-wide approval

Pat explicitly approved all sales-relevant content stored within `/sites/D2LSalesAssets` for evidence-gap discovery and bounded ingestion on 2026-07-30. On 2026-07-30, the SharePoint connector resolved this site as **Sales Portal**.

Primary navigation hub:

- [Corporate (TOAS & D4B) Segment Home](https://d2lmail.sharepoint.com/sites/D2LSalesAssets/SitePages/Corporate-Sales.aspx), published 2026-07-15

The approval covers content stored beneath the Sales Assets site, including published portal pages, the Sales Library, Rep Repository, current corporate enablement resources, customer-story indexes, implementation/services navigation, and sales templates. This content may pass vault verification at `approved-library` scope. A portal link remains discovery metadata; linked content still retains its own hostname, site, confidentiality, freshness, internal-note context, and external-use posture.

Links from the portal to personal OneDrive, another SharePoint site, Grow, Rovo agents, Crayon, product roadmaps, finance, legal, security, pricing, or other systems are not automatically approved by this site-wide scope.

Pricing and packaging remain excluded.

## Confluence

Thirteen spaces are allowlisted in the `desire2learn` Atlassian cloud: Product Resources, Implementation Services, Learning Services, Product Management, Solutions Engineering, International SEs, Global Customer Onboarding, Customer Success Operations, Transition Services, D2L Link, the Implementation Services Knowledge Base, Optimization Services, and Global Events.

Jira projects remain unapproved.

## Slack

Twenty-four public channels are allowlisted by immutable channel ID. They cover sales, corporate sales, enablement, solutions engineering, associations, Course Merchant, competitive intelligence, proposals, customer stories, implementation, and implementation resourcing.

## Continuing exclusions

- DMs, group DMs, private and archived channels
- Bot messages and social/noise channels
- Customer project repositories and customer-specific Confluence spaces
- Job profiles, personnel-sensitive content, credentials, and private contact data
- Restricted pricing or packaging and customer-confidential content

Sales connector surfaces remain read-only. Captures must still be selected, deduplicated, and minimally copied. Approved-library records can be promoted without duplicating sentence-level claim verification when provenance, scope, freshness, confidentiality, and external-use handling are recorded.
