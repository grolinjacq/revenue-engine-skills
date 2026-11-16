---
name: crm-log-call
description: Log a call, meeting or conversation in any CRM - a note, next step, deal stage, follow-up task and the contact's stage - live in HubSpot on a go, or as rows in out/crm-import.csv for any other CRM. Use when the user reports a finished interaction - "just got off the phone with X", "had a call with X", "log a call with X", "post-call notes for X", "debrief from my meeting with X".
---

# Log a call (any CRM)

Adapter, contract and write rules: `crm` (Job C). With the `hubspot` adapter, run `hubspot-log-call` (its safety box applies). Otherwise:

1. Parse what the user said: who, when, outcome, next step and date, deal changes (stage, amount, close date), objections, and any person named for a follow-up. Ask once only for what blocks the log (usually who).
2. Find the person and company (`find_contact`, `find_company`) and any open deal (`open_deals`).
3. Plan, one line per change: a note starting `[<team>]` with the summary (plain text, at most 500 characters); stage moves forward only; a task for the next step with its date; a deal change only if the user said so. A person who said no, stop or remove me goes to `out/suppress.csv` (safe mode `out/safe/suppress.csv`) at once and gets no task; with `outreach: lemlist`, also offer to add them to Lemlist's unsubscribes (`RULES.md`, "Opt-outs").
4. Show the plan. On a go, write the rows to `out/crm-import.csv` (safe mode `out/safe/crm-import.csv`) in the CRM's own field names, and tell the team where to import it. Append one line to `out/run-log.md`.
