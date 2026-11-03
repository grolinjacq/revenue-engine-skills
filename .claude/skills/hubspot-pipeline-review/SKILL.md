---
name: hubspot-pipeline-review
description: Review the HubSpot deal pipeline - totals by stage, what's stale or past its close date, deals with no next step, and a simple forecast for the period. Read-only. Use on "pipeline review", "how's the pipeline", "which deals are stuck", "forecast this quarter", "deal health".
---

# HubSpot pipeline review

Connection and write rules: see `hubspot-crm`. This skill only reads. To act on what it finds at scale, hand off to `cleanup-deals` (routes flagged deals to owners as tasks) or `hubspot-log-activity` (one deal at a time).

## Steps

1. Scope. Ask which pipeline and period if there is more than one pipeline, default to the main pipeline and the current quarter. Ask whether to filter by owner.
2. Totals. For each stage: deal count and total amount. Use an aggregate query when the server offers one, rather than paging through every deal.
3. Flags. List open deals that match any of:
   - Past due: close date before today.
   - Stale: no activity in 21 days or more.
   - No next step: no open task associated, or the next-step property empty if the portal uses one.
   - Missing basics: no amount, no close date, or no contact associated.
   Show at most 15, worst first (past due, then largest amount).
4. Forecast. Sum open amount weighted by each stage's probability, if the pipeline defines them. If it doesn't, give unweighted totals for the late stages only, and say so.
5. Write `out/pipeline-<date>.md`: the totals table, the flagged list (deal, owner, amount, stage, flag), the forecast line, and the 3 actions that would move the most money.
6. If the user is on a demo portal with very few deals, say so and keep the review to what is there.
