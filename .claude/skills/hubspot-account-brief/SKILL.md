---
name: hubspot-account-brief
description: One-page brief on a company or contact from HubSpot before a call or outreach - who they are, people we know there, open and past deals, last touches, and what to say next. Use on "brief me on", "prep my call with", "what do we know about", "account summary", "who do we know at".
---

# HubSpot account brief

Connection and write rules: see `hubspot-crm`. This skill only reads.

## Steps

1. Find the record. Search companies by domain first, then by name. For a person, search contacts by email, then by name plus company. If more than one match, show the top 3 and ask.
2. Pull, for the company:
   - Firmographics: industry, employees, country, lifecycle stage, owner.
   - Contacts associated: name, title, lifecycle stage, last activity date. Cap at 15, most recently active first.
   - Deals: open ones (stage, amount, close date, owner, last activity) and closed ones from the last 12 months (won or lost, and the lost reason if set).
   - Activities: the last 5 notes, emails, calls or meetings, newest first, one line each.
3. Fill gaps only if asked. If firmographics or titles are missing and the Clay plugin is installed, offer to enrich with Clay's `searches` skill. Do not write the enrichment back without a go (use `hubspot-crm` Job C).
4. Write the brief to `out/brief-<domain>.md`:

```
# <Company> - brief (<date>)
Snapshot: <industry>, <employees>, <country>. Owner: <name>. Stage: <lifecycle>.
Relationship: <customer | open deal | past lost deal | never engaged>, one line why.
People we know: <name, title, last touch> x up to 5
Deals: <open deals one line each>; <recent closed deals one line each>
Last touches: <up to 5 lines>
Gaps: <what HubSpot doesn't know that matters>
Suggested next step: <one concrete action, grounded in the above>
```

5. Show the brief in chat too. Keep it under 20 lines. If HubSpot holds nothing on the company, say so plainly; do not pad it with guesses.
