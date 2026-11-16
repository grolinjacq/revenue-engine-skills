---
name: crm-account-brief
description: One-page brief on a whole company (account) from any CRM - firmographics, everyone we know there, open and past deals, last touches, gaps and a next step - saved to out/. Read-only. Works with HubSpot, any CRM connector, a CSV export, or safe mode. Use on "brief me on <company or domain>", "account summary", "who do we know at <company>", "what do we know about <company>". For one person use crm-contact-lookup; for a meeting use crm-call-prep.
---

# Account brief (any CRM)

Adapter and contract: `crm`. This skill only reads. With the `hubspot` adapter, run `hubspot-account-brief` (same output). Otherwise:

1. `find_company` by domain, then by name. Several matches: show the top 3 and ask. A person's name: use their company, or hand off to `crm-contact-lookup`.
2. Pull: firmographics (industry, employees, country, stage, owner); contacts at the company (`find_contact` by domain; name, title, stage, last activity; up to 15, most recent first); `open_deals` and deals closed in the last 12 months (won or lost, with the reason); the last 5 `activities`.
3. Fill gaps only if asked. With `lists: clay`, offer to enrich missing firmographics or titles with `clay-build-list` (credits rules apply). Never write enrichment back without `crm` Job C.
4. Write `out/brief-<domain>.md` (safe mode: `out/safe/brief-<domain>.md`):

```
# <Company> - brief (<date>), from <CRM> via <adapter>
Snapshot: <industry>, <employees>, <country>. Owner: <name>. Stage: <stage>.
Relationship: <customer | open deal | past lost deal | never engaged>, one line why.
People we know: <name, title, last touch> x up to 5
Deals: <open deals, one line each>; <recent closed deals, one line each>
Last touches: <up to 5 lines>
Gaps: <what the CRM doesn't know that matters, including columns the export lacked>
Suggested next step: <one concrete action, grounded in the above>
```

5. Show it in chat, under 20 lines. If the CRM holds nothing on the company, say so plainly; never pad with guesses.
