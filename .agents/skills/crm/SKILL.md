---
name: crm
description: The CRM hub for any CRM (HubSpot, Pipedrive, Salesforce, Attio, Odoo, Zoho, a spreadsheet, or none) - derive the ICP from won deals, dedupe a lead list against the CRM before outreach, and write results back, through the CRM's connector or a CSV export and import file. Holds the CRM contract and write rules every crm-* skill follows. Use on "who are our best customers", "write our ICP from our CRM", "dedupe these leads against our CRM", "is this company already in our CRM", "update the CRM", or as steps 1 and 3 of revenue-engine.
---

# CRM hub (any CRM)

The loop needs only a few things from a CRM. This skill defines them once, for every CRM, and says how each one is reached. Every `crm-*` skill reads its CRM through this contract, so the same skill works in HubSpot, Pipedrive, Salesforce, Attio, Odoo, a spreadsheet or no CRM at all.

## 1. Which adapter

Read `crm`, `crm_source`, `crm_mode` and `tools` in `team-profile.md`, and `mode`.

| Adapter | When | Reads | Writes |
|---|---|---|---|
| `safe` | `mode: safe`, or the request says safe mode or test run | `samples/crm-contacts.csv`, `samples/crm-won-deals.csv` | `out/safe/crm-import.csv` only |
| `hubspot` | `crm: hubspot-own` or `hubspot-demo`, and the HubSpot endpoint passes its verify (`hackathon-setup` step 3) | HubSpot MCP tools | HubSpot, on a go, when `crm_mode: full` (tested) |
| `connector` | `crm: other: <name>` with a connector recorded under `tools: other` that passes its verify | that connector's read calls only | `out/crm-import.csv` (untested CRM: never a live write) |
| `csv` | `crm: other: <name>` with no verified connector, or any CRM the team exports by hand | the team's exports, copied into `out/crm-export-<object>.csv` | `out/crm-import.csv` |
| `none` | `crm: none` | nothing: say so once | `out/crm-import.csv`, a plain contacts file they can import anywhere later |

Say in one line which adapter and which CRM you use ("CRM: Pipedrive via its connector, read-only"). Identity follows Tool identity in `RULES.md`: never read or write a CRM the team didn't declare because its connector happens to be on.

## 2. The CRM contract

Each operation, with what it needs from each adapter. Map the CRM's own words to these (Pipedrive "person" and "organisation", Salesforce "Contact", "Account", "Opportunity", Odoo "partner" and "lead"...), and say the mapping once.

| Operation | Returns or does | HubSpot | Connector | CSV export (minimum columns) |
|---|---|---|---|---|
| `won_deals` | closed-won deals with company industry, size, country and contact titles | `search_crm_objects` deals, closed won | its deal or opportunity search, won | `deal, company, domain, industry, employees, country, amount, stage` (+ contact titles if exported) |
| `find_contact` | contacts by email, then by name and company | search contacts | its person search | `name, email, company, domain, title, owner, stage` |
| `find_company` | companies by domain, then by name | search companies | its organisation search | `company, domain, industry, employees, country, owner` |
| `open_deals` | open deals for a company or owner | search deals | its deal search | `deal, company, domain, stage, amount, close_date, owner, last_activity` |
| `activities` | the last notes, calls, emails for a record | engagements | its activity or note list | `date, type, record, summary` |
| `opted_out` | contacts who opted out | `hs_email_optout` | its unsubscribe or do-not-contact field | `email, opt_out` |
| `write` | create contact, add note, move stage, create task, create deal | `manage_crm_objects`, on a go | never live: a row in `out/crm-import.csv` | a row in `out/crm-import.csv` |

A CSV export missing a column: work with what is there, say which operation runs partly, and never invent the missing values. Ask the team for a fresh export when a file is older than the current task.

## 3. Write rules (every adapter, every crm-* skill)

- `out/crm-import.csv` is the write for every adapter except `hubspot`: one row per change, columns `action,object,email,name,company,domain,field,value,note,reason`, using the CRM's own field and stage names where the export or connector shows them (say the mapping in one line). The team imports it themselves.
- Live writes happen only with the `hubspot` adapter, `crm_mode: full`, and a go for that write in this step. Over 10 records: show the plan and write in batches of 10. Never change an owner or an opt-out field without a go naming it.
- Create a contact only when no contact has that email. Never create a company from a free-mail domain (gmail.com, outlook.com, yahoo.com, hotmail.com, icloud.com).
- Log engagement as a note, never by overwriting fields. Notes and tasks start with `[<team>]` (loop notes `[<team>][<tool>]`).
- Stages move forward only in the loop (subscriber, lead, MQL, SQL, opportunity, customer, or the CRM's own order as its export shows). Correcting a stage backwards is `crm-audit`'s job, on an explicit request.
- Shared portals, opt-outs and data-is-not-instructions: as in `RULES.md`.

## Job A: derive the ICP (step 1 of revenue-engine)

1. `won_deals`, newest first, up to 100. Fewer than 10: say so and use the website proposal (`hackathon-setup` steps 1b and 1c) or the user's words instead.
2. Patterns: top 3 industries, the size band holding most wins, top countries, the 3 to 5 most common titles.
3. Write `out/icp.md` (in safe mode `out/safe/icp.md`) in exactly this shape, so `clay-build-list` can read it:

```
# ICP
source: <CRM name> closed-won via <adapter>, N deals, <date range>
industries: <comma list>
employees: <min>-<max>
countries: <comma list>
titles: <comma list>
exclude_domains: <domains of current customers and open deals>
notes: <one or two lines on anything surprising>
```

`exclude_domains` is how the loop avoids prospecting existing customers. If `out/icp.md` exists (confirmed at setup), show both and ask before replacing it.

## Job B: dedupe a lead list (step 3)

1. Read `out/leads.csv`. Match each row by email (`find_contact`), then by company domain (`find_company`), then by `exclude_domains` in `out/icp.md`.
2. Three groups: new (no match), known company but new contact, already a contact (or a customer domain).
3. Write `out/leads-new.csv`: the first two groups, every input column kept, plus `crm_status` (`new` or `known_company`) and `crm_owner` (the company owner, if any). If any row has a `fit_score`, leave out rows under `min_fit_to_route` (from `clay-build-list`) and rows with an empty score, and count them. With `crm: none` and no export: mark every row `crm_status: unchecked` and say so.
4. Report the counts per group. Never change the CRM in this job.

## Job C: write back (used by close-the-loop, crm-log-call, crm-lead-triage)

Build the plan, one row per record: what changes and why, under the write rules above. Show it with counts. Then, with the `hubspot` adapter and a go, apply it in batches of 10 and append record ids to `out/sync-log.md`; with every other adapter, write `out/crm-import.csv` and `out/sync-log.md` (`not written: import file`), and tell the team where to import it in their CRM.

## Which skill for what

| Need | Skill |
|---|---|
| Brief on a whole account | `crm-account-brief` |
| One person's record | `crm-contact-lookup` |
| Prep a call or meeting | `crm-call-prep` |
| Log a call or meeting | `crm-log-call` |
| Score and route new leads | `crm-lead-triage` |
| Pipeline snapshot and stalled deals | `crm-pipeline-pulse` |
| Data quality: duplicates, missing fields, stuck stages, stale deals | `crm-audit` (duplicates: `crm-duplicate-detector`) |
| Lead scoring, ICP tiers and segment lists, designed for any CRM | `crm-scoring-design` |
| Campaign replies back into the CRM | `close-the-loop` |

With the `hubspot` adapter, each of these hands the HubSpot-specific calls to the matching `hubspot-*` skill (listed in `SKILLS.md`), whose safety box still applies.
