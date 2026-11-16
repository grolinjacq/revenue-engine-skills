---
name: crm-scoring-design
description: Design lead scoring (fit and engagement), ICP tiers and core segment lists for any CRM, from the ICP and won deals - written as a spec plus the fields and filters to create, and an import file that fills the tier for existing companies. Use on "lead scoring", "score our leads", "ICP tiers", "tier our accounts", "segment lists", "smart lists", "which accounts are T1". For HubSpot, the build-lead-scoring, create-icp-tiers and build-smart-lists skills can build it in the portal.
---

# Scoring, tiers and segments (any CRM)

Adapter and contract: `crm`. This skill designs and fills a file; it changes no CRM settings. Safe mode: inputs from `samples/` only (the `safe` adapter in `crm`), outputs under `out/safe/`, opt-outs read from and written to `out/safe/suppress.csv`; never the live `out/` files. Where the samples hold no data for a field (open deals, activities, last activity), say "no sample data" for it, never invent it.

1. Inputs: `out/icp.md` (or `crm` Job A first), won deals (`won_deals`), and the company fields the CRM actually has (from the connector's schema or the export header).
2. ICP tiers: T1 (industry and size and country match), T2 (two of three), T3 (one), not ICP. Say the exact rule and how many companies land in each tier.
3. Lead score: fit (tier, title match, country) and engagement (replied, clicked, booked, form, recent activity), each 0 to 50, with the points per signal and the threshold for MQL. Only signals the CRM records.
4. Segment lists, as filters in the CRM's own terms: sendable (has email, not opted out, not a customer), each ICP tier, each persona, engaged in the last 30 days, customers (exclusion list).
5. Write `out/scoring-design.md` (the spec, the fields to create with their type and options, the list filters, and where to click in that CRM to create them) and rows appended to `out/crm-import.csv` (the `crm` header: one row per existing company, `field` = `icp_tier`). The team creates the fields and imports the file. With the `hubspot` adapter and a request to build it live, hand off to `create-icp-tiers`, `build-lead-scoring` and `build-smart-lists`, under `RULES.md`.
