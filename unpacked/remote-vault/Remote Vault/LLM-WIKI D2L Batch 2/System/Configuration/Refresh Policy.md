---
tags:
  - resource/reference
  - system/governance
  - system/maintenance
  - navigation/system---
# Refresh Policy

Review cadence is based on materiality and source volatility:

- Pricing, packaging, roadmap, legal, security: never ingest unless explicitly authorized; always live-check.
- Product behavior and implementation: 30 days.
- Enablement, services, competitive positioning: 60 days.
- Approved customer proof: 90 days.
- Personas and discovery patterns: 180 days.

Manual refresh runs `scripts/manual_refresh.sh`. It detects stale, missing, changed, deleted, or superseded sources and writes a queue before altering claims. Scheduling requires separate explicit authorization.
