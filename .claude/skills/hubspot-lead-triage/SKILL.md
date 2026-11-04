---
name: hubspot-lead-triage
description: Triage new or unworked leads in HubSpot - score each against the ICP, set lifecycle stage, assign an owner, and create a follow-up task for the ones worth working. Use on "triage new leads", "who should we call first", "route these leads", "qualify the inbound", "work the leads that replied".
---

# HubSpot lead triage

Connection and write rules: see `hubspot-crm` (Job C).

## Steps

1. Pick the set. In a shared portal, only records the CLAUDE.md shared-portal rule allows. Skip contacts whose first name or name starts with `[DEMO]` (workshop records), unless the `workshop` skill is running. Default: contacts created in the last 14 days ("this week" means 7) with lifecycle stage subscriber or lead and no owner. Alternatives the user may name: a list or segment, contacts touched by a Lemlist campaign (notes starting `[lemlist]`), or a CSV.
2. Get the ICP. Read `out/icp.md`. If it is missing, run `hubspot-crm` Job A or ask the user for it.
3. Score each lead on fit, 0 to 3, one point each: company industry in the ICP, company size in the band, title matches an ICP title. Add an intent flag if the lead replied, booked, filled a form or clicked recently.
4. Decide, per lead:
   - Fit 3, or fit 2 with intent: work now. Lifecycle forward to MQL (SQL if they replied positively; never lower an existing stage), owner as below, task "Call <name>" due next business day.
   - Fit 2 without intent: nurture. Lifecycle stays lead. No task.
   - Fit 0 or 1: park. No change; list them in the report.
5. Owner. Use the company owner if the company has one. Otherwise use the rule the user gives (round robin over named owners, by country, or all to the user). Ask once if no rule is given.
6. Show the table: lead, company, fit, intent, decision, owner. Apply on a go, in batches of 10. With `crm_mode: read-only`, stop at the table and write it to `out/triage-<date>.md` only.
7. Write `out/triage-<date>.md` with the table and the counts per decision.

For a portal-wide, persistent version of this (a Fit and Engagement score that HubSpot keeps updated), point the user to `build-lead-scoring` and `create-icp-tiers`.
