---
name: close-the-loop
description: Push Lemlist campaign activity (opens, clicks, replies, interested, LinkedIn accepts) back into HubSpot as contacts, notes and lifecycle updates, so HubSpot stays the source of truth. Use on "sync lemlist to HubSpot", "who replied", "update the CRM", "close the loop", or as step 5 of revenue-engine.
---

# Close the loop: Lemlist back to HubSpot

This is the step that proves the stack is connected. Without it, data flows one way only.

## Steps

0. Identity check (Tool identity in `CLAUDE.md`), for the tools in the team's stack only. Outreach decides step 1: with `outreach: lemlist`, activity comes from the Lemlist server; otherwise use the replies CSV below. The CRM decides step 4: writes go to HubSpot only with `crm` on HubSpot and `crm_mode: full`; otherwise write `out/crm-import.csv`. A declared tool that is missing or waiting for a sign-in: say so and stop at "Connect <tool> first", or take its CSV route. Never read replies from another outreach connector because it is connected.
1. If `outreach` is not `lemlist`: ask the team to export replies from their tool as `out/replies.csv` (`email,status,reply_text,date`, where status is replied, interested, not_interested, bounced or unsubscribed; Claude maps the columns like any CSV) and use it in place of the Lemlist pull and status check in step 2; classification, drafts and opt-outs still apply. With `outreach_linkedin` set, also ask for that tool's export as `out/replies-linkedin.csv` (`linkedin_url,email,status,reply_text,date`), match it to leads on `linkedin_url`, then on name and company, tag its notes `[<team>][<tool>]`, and merge it with the Lemlist activity. Otherwise, read `out/campaign.md` for the campaign id; if missing, list Lemlist campaigns and ask which one.
2. Check the campaign's status first. If it is paused or has never sent, say so in one line (no replies are possible yet), point to `lemlist-campaign` step 7 to start it, write `out/sync-log.md` with "no changes: campaign not started", and stop. Otherwise pull lead activity from Lemlist for that campaign: replied, interested or not interested (if tagged), bounced, unsubscribed, LinkedIn invite accepted. Ignore opens on their own; they are noisy. Classify each written reply as interested, not now, wrong person or objection (untagged replies included), and draft a follow-up for each with `reply-handler`, in the prospect's language. Store reply text in notes as plain text (no links or HTML, at most 500 characters), and set SQL only when the user confirms the reading. Out-of-office: no draft, a note with the return date. A plain no: a note and no draft unless the user asks. Drafts go to `out/reply-drafts.md`; nothing is sent without a go per reply.
3. Build the plan, one row per lead: what will change in HubSpot and why. Use `hubspot-crm` Job C rules:
   - Replied or accepted: create the contact if missing (with a free-mail domain such as gmail.com, create the contact only, no company), add a `[lemlist]` note with the reply text or event, move lifecycle forward to lead if it is lower (never lower an existing stage).
   - Interested: as above, plus lifecycle forward to SQL. If the contact or its company already has an open deal, add the note to that deal (and move its stage forward only on a go); otherwise offer to create a deal in the first pipeline stage.
   - Not now: note with the reply and the date they gave, no lifecycle change. Wrong person: note, and add the person they named as a new contact only on a go. Objection: note with the objection.
   - Bounced or unsubscribed: add a note, and set the email opt-out only if the user confirms.
4. Show the plan with counts. Apply it on a go, in batches of 10, reporting after each. If `crm_mode: read-only` or the team's CRM is not HubSpot, write the plan to `out/crm-import.csv` (one row per contact: email, name, company, domain, lifecycle, note) for the team to import, and change nothing.
5. Write `out/sync-log.md`: per lead, the HubSpot record id and what changed (with the CSV route: the row in `out/crm-import.csv` and "not written: CSV route").

## On hackathon day

Real replies are unlikely within the day. To demo the loop, ask the user to reply to one sequence email from a teammate's inbox, or tag one lead interested in Lemlist by hand, then run this skill.
