---
name: hubspot-account-brief
description: One-page brief on a whole company (account) from HubSpot - firmographics, everyone we know there, open and past deals, last touches, gaps, and what to do next - saved to out/. Read-only. Use on "brief me on <company or domain>", "account summary", "who do we know at <company>", "what do we know about <company>". For one person or a meeting use hubspot-call-prep ("prep my call with Marta"); for a quick record on one person use hubspot-contact-lookup.
---

# HubSpot account brief

Connection and write rules: see `hubspot-crm`. This skill only reads. It covers a whole account; for a call or meeting with one person, HubSpot's official `hubspot-call-prep` (talking points, email and calendar context, company news) is the better fit.

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
