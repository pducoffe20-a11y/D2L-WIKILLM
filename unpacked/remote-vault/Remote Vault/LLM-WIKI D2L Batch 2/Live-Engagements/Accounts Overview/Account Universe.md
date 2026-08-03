---
type: account
tags:
  - account/analysis/prioritization
  - account/category/universe
  - navigation/accounts
  - sales/strategy
territory:
  - PA
  - OH
  - MI
  - MN
  - WI
  - TN
  - KY
  - DE
verticals:
  - Healthcare
  - Banking / Financial Services
  - Nonprofits
  - Trade Associations & Credentialing Boards
total_unts_modeled:
top_accounts_ranked: 300
math_model: Linear combination of Target, Monitor Priority, ICP Alignment, Lifecycle Intent, and Sales Force Ownership---

# Strategic Prioritization & Rank-Order Analysis: D2L Account Universe

## Executive Summary
This vault section houses the operational prioritization framework for D2L’s Senior AE territory across the Great Lakes and Mid-Atlantic regions. The underlying analytical model moves beyond static tiers by blending real-time 6Sense intent data, Ideal Customer Profile (ICP) alignment, and named account ownership.

## Mathematical Scoring Model ($S_i$)
The cumulative priority score is determined by:
$$S_i = \omega_T T_i + \omega_P P_i + \omega_I I_i + \omega_L L_i + \omega_O O_i$$

* **Target Status ($T_i$):** Weight = 40 (1 if in top target list, 0 otherwise)
* **Monitor Priority ($P_i$):** Weight = 25 ($A=1.0$, $B=0.6$, $C=0.2$)
* **ICP Alignment ($I_i$):** Weight = 15 (1 if ICP "Yes", 0 if "No")
* **Lifecycle Intent Stage ($L_i$):** Weight = 15 (6Sense Qualified/Working = 1.0, Aware = 0.5, Nurture = 0.2, None = 0.0)
* **Sales Force Ownership ($O_i$):** Weight = 5 (1 if named AE assigned, 0 if generic Marketing)

## Pipeline Directory Structure
* [[Top 50 Accounts - TO-ENT]] — Crown Jewels, Tier 1 Targets, and High-Intent Enterprises (Ranks 1–50)
* [[Tier 1 Accounts - TO ENT]] — High-Intent Opportunity Tier & Strategic Industrial accounts (Ranks 51–100)
* [[Tier 2 Accounts - TO ENT]] — Broad Regional Nurture and Emerging Pipeline (Ranks 101–200)
