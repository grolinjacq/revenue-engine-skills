---
name: revenue-engine
description: Run the full CRM to list to outreach to CRM loop (HubSpot, Clay, Lemlist, or the team's own tools via CSV), or route any plain-language GTM request to the right step. Use when the user says "run the engine", "build me a campaign end to end", "connect the stack", "find me people like our best customers and reach out", "what's next", imports a CSV from another tool, or describes a goal in one spoken sentence.
---

# Revenue engine (orchestrator)

The hackathon's winning criterion is that data flows across the whole stack. This skill is the spine: it decides which step to run and passes the output of one step into the next. Each step has its own skill; call it, do not re-implement it here. Read `team-profile.md` first: its stack decides which tool fills each step.

## The loop

| Step | Default skill | Reads | Writes | Hand-off artefact |
|---|---|---|---|---|
| 1. Learn the ICP | `hubspot-crm` Job A | Closed-won deals, their companies and contacts | Nothing | `out/icp.md` |
| 2. Build the list | `clay-build-list` | `out/icp.md` | Clay table | `out/leads.csv` |
| 3. Dedupe against CRM | `hubspot-crm` Job B | `out/leads.csv` | Nothing | `out/leads-new.csv` |
| 4. Launch outreach | `lemlist-campaign` | `out/leads-new.csv` | Lemlist campaign (paused) | `out/campaign.md` |
| 5. Close the loop | `close-the-loop` | Lemlist activity | HubSpot contacts, notes, deals | `out/sync-log.md` |

Every step writes its artefact into `out/`. If an artefact already exists, say where it came from (its `source` line or file date) and ask whether to reuse it. This lets a team pick the loop up at any step, and gives the demo a visible trail.

## Step contracts (how other tools plug in)

Any step can be filled by another tool, as long as its artefact matches:

- `out/icp.md`: the format in `hubspot-crm` Job A. From another CRM: read it through that CRM's connector if one is on (read-only), or from a CSV export of closed-won deals, or from the user's words.
- `out/leads.csv`: header `email,first_name,last_name,job_title,company_name,company_domain,linkedin_url,country,employees,industry,personalization`. Optional trailing columns `fit_score,fit_reason,fit_source` (from `clay-build-list` scoring) travel with the rows, and so does any other enrichment column (for example `segment`, `latest_news`, `current_challenges`, `customer_list`): later steps use them as copy variables. From Apollo, Lusha, Sales Navigator or any CSV: normalise it (below).
- `out/leads-new.csv`: `out/leads.csv` plus `hubspot_status` and `hubspot_owner`. Without HubSpot: dedupe against a CSV export of the team's CRM with `crm-duplicate-detector`, or skip and say so.
- `out/campaign.md`: campaign name, id or tool, lead count, sequence and copy. With another outreach tool: the sequence plus `out/outreach-import.csv` in that tool's import format.
- `out/sync-log.md`: what changed in the CRM. Without HubSpot: `out/crm-import.csv` for the team to import.

### Normalising a CSV from anywhere

1. Read the header. Map each column to the contract by meaning ("Email Address" to `email`, "First" to `first_name`, "Company" to `company_name`, "Website" to `company_domain` after stripping `https://` and `www.`). Show the mapping in one table and ask once if a column is ambiguous.
2. Derive `company_domain` from the email domain when missing, except free-mail domains.
3. Rows with no email and no LinkedIn: keep them out, count them, and write them to `out/leads-dropped.csv` with the reason.
4. Write `out/leads.csv` in the contract format, and report rows in, rows out, rows dropped.

## Routing

- No ICP yet, or "start from the CRM": step 1.
- The user brings their own ICP or target companies: write `out/icp.md`, then step 2.
- The user brings a CSV of leads: normalise it, then step 3.
- Copy, angles, personas or sequence strategy: the Lemlist skills (`campaign-angle-finder`, `copywriting-*`, `linkedin-sequence`, `outbound-campaign-architect`; listed in `SKILLS.md`), in `copy_language`, then step 4.
- Outreach goes through Lemlist when the team has it; Clay's `campaigns` skill is not used for outreach here.
- "Did anyone reply?", "update the CRM": step 5.
- One spoken sentence that names a goal ("find 20 CFOs at Spanish fintechs and get a campaign ready"): restate it as the steps you will run, in one line, and start. Ask only what blocks the first step.

## Rules for the whole loop

1. Check connections first, for the tools in the team's stack only: list the HubSpot and Lemlist tools, run `clay whoami` (or list the Clay connector's tools). If one is missing, say which, offer `hackathon-setup` for that tool, or the CSV route for that step. Never fake a step with invented data.
2. Nothing leaves the building without a yes. Campaigns are created paused. No campaign start, email or LinkedIn message without the user's explicit go in the current step; no CRM write over 10 records without a go.
3. Respect `crm_mode`. With `read-only`, steps 1 and 3 read, step 5 writes a CSV instead of the CRM.
4. Keep a run log. Append one line per step to `out/run-log.md`: time, step, tool used, counts in and out, anything skipped. Judges see this.
5. Stop at a step boundary if a count looks wrong (for example 0 leads, or more than 500), and show the user before continuing.

## Bonus: agent mode

For the AI-agent bonus, the list-and-draft part of the loop runs headless. Agent mode never touches Lemlist or writes to the CRM: it ends with files a human reviews.

1. Run the same steps once interactively first, so the team has seen every gate.
2. The canonical command (also in `USAGE.md`), from the workspace folder:

```
claude -p "Agent mode: run revenue-engine steps 2 and 3 from out/icp.md, then write the sequence for step 4 to out/campaign.md. Stay within clay_credit_cap. Do not call Lemlist and do not write to the CRM. Wherever a go would be needed, write what you would do to out/agent-report.md and continue." --allowedTools "Read" "Write(./out/**)" "Edit(./out/**)" "Bash(clay *)"
```

3. Clay through the connector instead of the CLI, or HubSpot reads for the dedupe: add those tools to `--allowedTools` by the names `/mcp` shows (read tools only, never create or update tools).
4. Then, interactively: review `out/agent-report.md`, and run `lemlist-campaign` and `close-the-loop` with the usual gates.
5. With an API-key login, headless runs bill that key and claude.ai connectors are not available.
