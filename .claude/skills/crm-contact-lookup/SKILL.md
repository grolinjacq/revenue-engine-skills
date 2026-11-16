---
name: crm-contact-lookup
description: Pull a full view of one person from any CRM - stage, owner, company, open deals, last interaction, notes and tasks - as a short summary in chat. Read-only. Works with HubSpot, any CRM connector, a CSV export, or safe mode. Use on "pull up X", "who is X", "what do we know about X", "when did we last contact X", "look up X", or a pasted email address, where X is a person. Not for a company (crm-account-brief) or a meeting (crm-call-prep).
---

# Contact lookup (any CRM)

Adapter and contract: `crm`. Read-only. With the `hubspot` adapter, run `hubspot-contact-lookup`. Otherwise:

1. `find_contact` by email if given, else by name (and company if given). Several matches: show up to 3 (name, title, company) and ask.
2. Pull: title, company, stage, owner, opt-out status (`opted_out`), open deals for the person or their company (`open_deals`), the last 5 `activities`, open tasks if the CRM or export has them. Check `out/suppress.csv` too.
3. Answer in chat, under 12 lines: who they are, where they stand (stage, deals), last touch and by whom, anything open, opt-out status, and one suggested next step. Fields the adapter couldn't read: say which.
4. Nothing is written. Logging something about this person is `crm-log-call`.
