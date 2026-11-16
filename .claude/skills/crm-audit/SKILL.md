---
name: crm-audit
description: Read-only data-quality audit of any CRM from its connector or exports - duplicates, missing key fields, contacts with no company, stuck or missing stages, stale and past-due deals, ownerless records - graded with a fix plan and an import file of the fixes. Use on "audit our CRM", "how clean is our CRM", "CRM health check", "fix our CRM data", "find missing fields". For HubSpot's full portal audit use hubspot-audit.
---

# CRM audit (any CRM)

Adapter and contract: `crm`. The audit reads only. Safe mode: inputs from `samples/` only (the `safe` adapter in `crm`), outputs under `out/safe/`, opt-outs read from and written to `out/safe/suppress.csv`; never the live `out/` files. Where the samples hold no data for a field (open deals, activities, last activity), say "no sample data" for it, never invent it. With the `hubspot` adapter, `hubspot-audit` and `hubspot-sales-audit` give the deeper HubSpot version; this one works everywhere.

1. Get the data: contacts, companies and deals through the connector (read calls only, paged), or the team's exports in `out/crm-export-<object>.csv`. Say record counts and the date of each export.
2. Check, with counts and 3 examples each:
   - Duplicates: run `crm-duplicate-detector` (analysis only).
   - Missing key fields: contacts without email or company; companies without domain, industry or size; deals without amount, close date or owner.
   - Stages: records with no stage; contacts with open deals still at subscriber or lead; customers with no won deal.
   - Deals: past their close date, no activity in 30 days, no next step.
   - Ownership: records with no owner, owners with no recent activity.
3. Grade each area A to D, and write `out/crm-audit-<date>.md`: grades, findings, and fixes in priority order (biggest impact on outreach and forecasting first).
4. Fixes: write `out/crm-import.csv` with the safe ones only (fill a domain from the email, set a missing stage forward, flag duplicates for review), every row marked `review`. Never merge, delete or move a stage backwards here: those need the team, in their CRM, after reading the report. With the `hubspot` adapter, the admin skills (`fix-lifecycle-stages`, `merge-duplicate-companies`, `cleanup-deals`) can apply some fixes under `RULES.md`.
