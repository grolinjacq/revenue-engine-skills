---
name: hubspot-log-activity
description: Log what just happened with a contact or deal in HubSpot - a call or meeting note, a follow-up task, a deal stage or close-date change, a new deal. Use on "log this call", "add a note to", "remind me to follow up with", "move the deal to", "create a deal for", "update HubSpot after my meeting".
---

# HubSpot log activity

Connection and write rules: see `hubspot-crm` (Job C). Every write here is shown first and applied on a go. With `crm_mode: read-only`, show the plan and stop.

## Steps

1. Identify the record: contact, company or deal. Search as in `hubspot-account-brief` step 1. Never create a duplicate contact or company to log against.
2. Turn what the user said into changes. One message can produce several:
   - Note: a short summary in the user's words, plus decisions and next steps as bullets. Associate it to the contact, the company and any open deal it concerns.
   - Task: title, due date (convert "next Tuesday" to a date and state it), owner (the user unless named), associated to the same records.
   - Deal update: stage, amount, close date. Stage moves forward freely; a move backwards, or to closed lost, needs a reason.
   - New deal: name `<Company> - <what>`, pipeline, stage, amount if given, close date if given, associated to company and contact.
3. Show the plan as a short list, one line per change, with the record each one touches. Apply on a go.
4. Confirm with the record ids and a one-line summary. If the user is running the revenue loop, append one line to `out/run-log.md`.

## Examples

- "Log my call with Marta at Acme: she wants a demo with her CTO next week, budget is ~20k" makes a note on Marta, a task "Book demo with Acme CTO" due 7 days out, and an offer to create a deal "Acme - pilot" at 20,000 in the first stage.
- "Move Globex to contract sent, closing end of month" makes a stage change and a close-date change on the open Globex deal (ask if there are two).
