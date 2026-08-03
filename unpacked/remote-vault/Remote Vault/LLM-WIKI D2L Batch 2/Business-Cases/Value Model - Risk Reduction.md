---
id: d2l-value-model-risk-reduction-20260730
title: Value Model - Risk Reduction
type: value-model
status: verified
aliases:
  - risk-adjusted value model
  - compliance risk model
tags:
  - content/audience/sales
  - content/type/guide
  - content/use-case/deal-support
  - entity/use-case/benefit/cost-reduction
  - sales/stage/evaluation
source_system: multi-source
source_title: NIST IR 8286A Rev. 1, Healthcare and Regulated Training Playbook, and Epworth customer proof
source_url: https://csrc.nist.gov/pubs/ir/8286/a/r1/final
source_date: 2025-12-01
captured_at: 2026-07-30T21:30:00-04:00
last_verified: 2026-07-30
review_after: 2026-09-28
source_owner: D2L Sales Brain operator
confidence: high
verification_scope: seller-guidance
verification_basis: The current NIST scenario, likelihood, and impact approach was adapted to learning-related risk without asserting legal compliance or guaranteed prevention.
external_use: source-check-required
confidentiality: internal
seller_relevance: Creates a bounded risk conversation for regulated learning, audit evidence, accessibility and operational continuity.
related:
  - Business Case Toolkit
  - Healthcare and Regulated Training Playbook
  - Proof Card - Epworth HealthCare - Compliance Learning Efficiency---

# Value Model - Risk Reduction

## Use when

A risk owner can define a specific event, exposure, likelihood, impact and control response.

## Required risk scenario

**If** a defined event occurs, **because** of a stated vulnerability or process weakness, **then** a named business asset or objective experiences a defined impact.

Examples may include missing renewal evidence, delayed mandatory training, inaccessible content remediation, operational disruption or data/process failure. Legal, regulatory and security conclusions require the appropriate D2L and buyer specialists.

## Required inputs

- Baseline event frequency or annual probability.
- Financial impact range per event.
- Nonfinancial impact and risk tolerance.
- Proposed control's expected effect on likelihood or impact.
- Residual risk after the change.
- Control, implementation and monitoring costs.
- Risk owner and evidence source.

## Formula

```text
Baseline expected annual loss =
  baseline annual probability × baseline impact

Residual expected annual loss =
  residual annual probability × residual impact

Net risk-adjusted value =
  baseline expected annual loss
  - residual expected annual loss
  - annualized control cost
```

Use ranges. Do not imply precision when probability or impact is ordinal.

## Discovery

- What exact event are we trying to reduce?
- What evidence supports frequency and impact?
- Which existing controls already reduce exposure?
- Which part of the proposed solution changes likelihood, impact, detection or response?
- Who accepts the residual risk?

## Proof boundary

[[Proof Card - Epworth HealthCare - Compliance Learning Efficiency]] demonstrates a healthcare customer's delivery-model change and cost outcomes. It does not prove regulatory compliance or reduced incident probability.

## Claims to avoid

- The platform eliminates compliance, security, accessibility or operational risk.
- Training completion proves competence or compliant behavior.
- A regulatory fine or breach cost can be used without buyer/legal validation.
- Risk reduction is added to avoided costs that already represent the same event.

