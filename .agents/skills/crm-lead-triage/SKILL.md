---
name: crm-lead-triage
description: Triage new or unworked leads from any CRM or a list - score each against the ICP, decide work now, nurture or park, pick an owner and a follow-up task - live in HubSpot on a go, or as an import file for any other CRM. Use on "triage new leads", "who should we call first", "route these leads", "qualify the inbound", "work the leads that replied".
---

# Lead triage (any CRM)

Adapter, contract and write rules: `crm` (Job C). With the `hubspot` adapter, run `hubspot-lead-triage`. Otherwise:

1. The set: contacts created in the last 14 days with no owner, from the connector or the export; or a list or CSV the user names (normalise it with `revenue-engine`). Safe mode: `samples/inbound.csv`.
2. The ICP: `out/icp.md` (safe mode `samples/icp.md`). Missing: `crm` Job A, or ask.
3. Fit, 0 to 3, one point each: industry in the ICP, size in the band, title matches. Intent flag: replied, booked, filled a form, asked for pricing or a call.
4. Decide: fit 3, or fit 2 with intent, work now (stage forward to MQL, or SQL after a positive reply; task "Call <name>" next business day); fit 2 without intent, nurture (no task); fit 0 or 1, park (no change). Students, competitors and free-mail with no company: park, and say why.
5. Owner: the company owner if there is one, else the rule the user gives (round robin, by country, all to me). Ask once if there is none.
6. Show the table (lead, company, fit, intent, decision, owner). On a go, write the changes to `out/crm-import.csv` (safe mode `out/safe/crm-import.csv`), and `out/triage-<date>.md` with the table and counts.
