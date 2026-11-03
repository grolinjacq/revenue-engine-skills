---
name: hubspot-crm
description: Derive the ICP from HubSpot closed-won deals, check a lead list against existing HubSpot contacts and companies before outreach, and hold the write rules every HubSpot skill follows. Use on "who are our best customers", "write our ICP from HubSpot", "dedupe these leads against HubSpot", "is this company already in HubSpot", or as steps 1 and 3 of revenue-engine. For a brief on one account use hubspot-account-brief; to log a note, task or deal change use hubspot-log-activity.
---

# HubSpot CRM

HubSpot is the source of truth in this stack. Clay and Lemlist feed it; nothing should overwrite it blindly.

Connection: HubSpot's remote MCP server, through the HubSpot connector in the Claude app or a registered MCP connector (see `hackathon-setup`, and `connect-hubspot-mcp` for the details). Call `get_user_details` first to confirm the portal and what is writable. List the tools before the first call; pick by what they do.

## The HubSpot skill set

This skill is the hub: ICP, dedupe, and the write rules every other HubSpot skill follows.

| Need | Skill |
|---|---|
| Brief on an account or contact before a call | `hubspot-account-brief` |
| Pipeline health and forecast | `hubspot-pipeline-review` |
| Log a call, note, task, deal change | `hubspot-log-activity` |
| Score, route and assign new leads | `hubspot-lead-triage` |
| Full portal audit (read-only) | `hubspot-audit`, `hubspot-sales-audit` |
| Persistent ICP tiers and lead scoring in HubSpot | `create-icp-tiers`, `build-lead-scoring` |
| Segment lists | `build-smart-lists` |
| Data quality | `merge-duplicate-companies`, `fix-lifecycle-stages`, `cleanup-deals` |

The last four rows come from hubspot-admin-skills (MIT, Tom Granot) and run Python scripts with a service key in `.env` (`HUBSPOT_ACCESS_TOKEN`). They are built for scale: always run their dry run or "before" stage first on hackathon day.

## Job A: derive the ICP (step 1 of `revenue-engine`)

1. Pull closed-won deals, newest first, up to 100. If there are fewer than 10, say so and ask the user to describe the ICP instead.
2. For each deal, get the associated company: industry, employee count, country, annual revenue if present, and the contacts' job titles.
3. Find the patterns: top 3 industries, the size band that holds most wins, top countries, the 3 to 5 titles that appear most among contacts on won deals.
4. Write `out/icp.md` in exactly this shape, so `clay-build-list` can read it:

```
# ICP
source: HubSpot closed-won, N deals, <date range>
industries: <comma list>
employees: <min>-<max>
countries: <comma list>
titles: <comma list>
exclude_domains: <domains of current customers and open deals>
notes: <one or two lines on anything surprising>
```

`exclude_domains` matters: it is how the loop avoids prospecting existing customers.

## Job B: dedupe a lead list (step 3)

1. Read `out/leads.csv`. Match each row against HubSpot contacts by email first, then against companies by domain.
2. Split into three groups: new (no match), known company but new contact, already a contact.
3. Write `out/leads-new.csv` with the first two groups (keep every input column, including any `fit_` columns; if any row has a `fit_score`, leave out rows below `min_fit_to_route` from `clay-build-list`, and rows with an empty `fit_score`, and count them; if no row has one, keep every row), adding a column `hubspot_status` (`new` or `known_company`) and `hubspot_owner` where a company owner exists.
4. Report the three counts. Never delete or edit HubSpot records in this job.

## Job C: write back (used by `close-the-loop`)

- Create a contact only if no contact with that email exists. Associate it to the company by domain; create the company only if none matches.
- Log engagement as a note on the contact, not by overwriting properties. Start the note with `[lemlist]`.
- Set lifecycle stage forward only (subscriber to lead to MQL to SQL), never backwards.
- Create a deal only when the user says so, or when a reply is tagged interested and the user approved deal creation for this run.
- Before any write, read `crm_mode` in `team-profile.md`: if `read-only`, write nothing and offer a CSV of the planned changes instead.
- Over 10 records: show the plan, wait for a go, write in batches of 10 (the HubSpot connector's limit).
- Never create a company from a free-mail domain (gmail.com, outlook.com, yahoo.com, hotmail.com, icloud.com).
- The "forward only" lifecycle rule is for the loop's write-backs. `fix-lifecycle-stages` deliberately corrects stages and may move one back; run it only on an explicit request, after its before stage, and never with `crm_mode: read-only`.

## Failure modes

- Auth expired: run `/mcp`, pick hubspot, re-authenticate.
- Missing scope (for example, deals): say which object failed and continue with what works.
