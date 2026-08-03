---
id: industry-playbook-k12
title: K-12 Playbook
type: industry-playbook
status: verified
aliases:
  - Schools Playbook
  - District Learning Playbook
tags:
  - content/audience/sales
  - content/type/guide
  - entity/customer/industry/k12
  - entity/industry/k12
  - navigation/pathway/sales-path
  - sales/stage/discovery
source_system: crawlberg-and-firecrawl
source_title: NCES School Pulse Panel Interactive Results
source_url: https://nces.ed.gov/surveys/spp/results.asp
source_date: 2026-07-30
captured_at: 2026-07-30T17:15:00-04:00
last_verified: 2026-07-30
review_after: 2026-10-28
source_owner: National Center for Education Statistics
confidence: high
verification_scope: seller-guidance
verification_basis: The NCES School Pulse Panel results were retrieved with Firecrawl and re-checked with Crawlberg; national survey estimates and stated limitations are retained.
external_use: source-check-required
confidentiality: internal
seller_relevance: Industry context, stakeholder hypotheses, discovery prompts, objections, and proof requirements for K-12 opportunities.
related:
  - "[[Expanded Persona Coverage]]"
  - "[[Customer Proof by Industry and Use Case]]"---
# K-12 Playbook

## Evidence boundary

NCES School Pulse Panel findings are weighted U.S. public-school estimates based largely on school-reported conditions. They are discovery context, not proof about a particular district and not causal evidence.

## Verified pressures

- Schools estimated that 31% of public-school students were behind grade level at the end of the 2024–25 school year.
- 91% of public schools reported using diagnostic-assessment data to identify individual academic needs.
- 85% reported providing some type of tutoring during the school year.
- 60% of schools offering academically focused after-school programming did so, but estimated participation was 13% of students.
- 60% of schools characterized engaging families as somewhat or very difficult, even while 98% reported contacting families at least monthly.
- These estimates have survey, response and sampling limitations; reported effectiveness does not prove measured academic impact.

Source: [NCES School Pulse Panel interactive results](https://nces.ed.gov/surveys/spp/results.asp).

## Likely buyers and stakeholders

- Superintendent or cabinet sponsor: district priorities, equity, outcomes and governance
- Chief academic officer or curriculum leader: instructional model, intervention and professional learning
- CIO or technology director: platform, identity, integrations, security and support
- Teaching-and-learning or professional-development leader: educator capacity and course quality
- School leader: implementation, teacher workload and family experience
- Data or student-services leader: screening, intervention and attendance workflows
- Procurement and finance: funding constraints, accessibility and public purchasing requirements

## Trigger events

- Districtwide digital-learning or curriculum initiative
- Learning-recovery, tutoring or intervention program
- Teacher professional-learning redesign
- LMS renewal, consolidation or standardization
- Family-engagement or attendance initiative
- State requirement, grant-funded program or expiring relief funding
- Accessibility, privacy or cybersecurity review

## Priority use cases

- Consistent digital course and resource access
- Differentiated learning and release pathways
- Educator professional learning
- Intervention, tutoring and supplemental-program delivery
- Family visibility and communication coordination
- Progress monitoring and early-warning workflows
- Districtwide content and template governance

## Proof to use

The current curated proof-card set does not yet include a dedicated K–12 customer card. Use [[Customer Proof by Industry and Use Case]] to locate an approved, current K–12 story before using customer metrics externally.

## Discovery questions

- Which student groups and grades are furthest from the desired outcome?
- How are diagnostic results converted into an instructional response today?
- Which interventions happen inside the core learning environment and which happen elsewhere?
- What adds work for teachers rather than removing it?
- How consistent is the digital experience across schools and classrooms?
- What must families be able to see or do?
- Which privacy, accessibility, identity and rostering requirements are non-negotiable?

## Likely objections

### "Teachers do not have capacity for another platform"

**Diagnose:** Identify duplicate entry, content recreation, inconsistent templates, training expectations and support ownership.

**Response direction:** Demonstrate only the workflows tied to reduced friction. Do not position feature breadth as teacher value.

### "Our students need instruction, not more screen time"

**Diagnose:** Clarify whether the use case is core instruction, teacher-led support, tutoring, communication or access outside class.

**Response direction:** Position technology as supporting the instructional model, not replacing educators. Do not equate usage with learning.

### "Funding is temporary"

**Diagnose:** Identify funding source, renewal horizon, total operating cost and which capabilities must remain sustainable after the grant.

**Response direction:** Build a phased scope tied to durable priorities. Do not assume future funding.

## Safe claim boundary

Safe: national survey data shows persistent learning-recovery, intervention, family-engagement and capacity pressures across U.S. public schools.

Unsafe: a named district has the national average problem, a platform will close learning gaps, or increased digital activity will improve achievement.

## Business cases

### 1. Teacher time returned

**Value hypothesis:** Common course structures, reusable content and fewer duplicate workflows may return teacher preparation or administration time.

**Inputs required:**

- teachers, courses and schools in scope
- current minutes per repeated task
- task frequency
- realistic adoption rate
- district-approved value for released capacity

**Model:** `teachers × occurrences × avoidable minutes ÷ 60 × adopted percentage`

Report this first as capacity. Do not present it as budget savings unless paid workload or staffing will change.

### 2. Professional-learning delivery

**Value hypothesis:** A districtwide professional-learning model may reduce repeated delivery and improve access across schools.

**Inputs required:**

- annual sessions, participants and facilitators
- travel, substitute, venue and facilitator cost
- content-development and update effort
- components that must remain live or coached
- expected participation and completion

**Model:** `avoidable delivery cost + avoidable backfill cost − new delivery and support cost`

### 3. Intervention capacity

**Value hypothesis:** Better coordination of diagnostic information, tutoring resources and supplemental learning may expand the number of students an existing intervention team can support.

**Inputs required:**

- identified students and current service capacity
- staff hours per intervention cycle
- waiting time or unserved demand
- workflow steps that technology can actually change
- academic measures owned by the district

Do not monetize assumed achievement gains. Track service capacity and instructional outcomes separately.

### 4. Funding sustainability

Show the three-year operating cost after grants expire, including content, training, rostering, identity, accessibility, support and change management. A viable case identifies which recurring budget owner inherits the program.
