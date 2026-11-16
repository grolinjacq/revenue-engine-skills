---
name: crm-pipeline-pulse
description: Pipeline snapshot from any CRM - open deals by stage, age and last activity, stalled deals flagged, a simple forecast and suggested follow-ups - saved to out/. Read-only. Works with HubSpot, any CRM connector or a deals CSV export. Use on "how's my pipeline", "show me my deals", "which deals are stalling", "pipeline review", "forecast this quarter".
---

# Pipeline pulse (any CRM)

Adapter and contract: `crm`. Read-only. With the `hubspot` adapter, run `hubspot-pipeline-pulse`. Otherwise:

1. `open_deals` for the user (or everyone, if asked), with stage, amount, close date, owner and last activity. The export misses last activity: say the stall check is by close date only.
2. Flag: no activity in 21 days; close date passed; no next step or amount; stuck in one stage longer than the others' median.
3. Forecast: sum by stage for deals closing this quarter, plus a weighted total using the CRM's stage probabilities if the export has them (else say none were given and show the unweighted sum only). Never invent probabilities.
4. Write `out/pipeline-<date>.md`: table by stage, flagged deals with one suggested action each, the forecast. Show the top 5 flags in chat.
5. Follow-up tasks or drafts are suggestions only; writing them is `crm-log-call` or `crm` Job C, on a go.
