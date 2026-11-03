# Every skill in this workspace

You don't need to name a skill: say what you want and Claude picks one. To force one, start your message with its name, for example `/hubspot-account-brief`.

## Start here
| Skill | What it does |
|---|---|
| `hackathon-setup` | Your preferences, the installs, the sign-ins, checking every connection. Runs on first launch. |
| `revenue-engine` | Runs the whole loop, routes one-sentence requests, and plugs in CSVs from other tools. |
| `event.md` | Not a skill: the organisers' facts (demo portal, client ID, codes) that setup reads. |
| `make-it-ours` | Teaches Claude your company, product and voice, and your own trigger phrases. |

## HubSpot (source of truth)
| Skill | What it does | Source |
|---|---|---|
| `hubspot-crm` | The hub: ICP from closed-won deals, dedupe a lead list, the write rules | this pack |
| `hubspot-account-brief` | One-page brief on a company or contact before a call | this pack |
| `hubspot-pipeline-review` | Deal totals by stage, stale and past-due deals, forecast | this pack |
| `hubspot-log-activity` | Log a call or meeting, create a task, move a deal | this pack |
| `hubspot-lead-triage` | Score new leads against the ICP, set the stage, assign, create tasks | this pack |
| `connect-hubspot-mcp` | Detailed HubSpot connection guide | hubspot-admin-skills |
| `hubspot-audit`, `hubspot-sales-audit` | Read-only portal audit with prioritised fixes | hubspot-admin-skills |
| `create-icp-tiers` | ICP tier property on every company | hubspot-admin-skills |
| `build-lead-scoring` | Fit and engagement lead score | hubspot-admin-skills |
| `build-smart-lists` | Standard segment lists | hubspot-admin-skills |
| `merge-duplicate-companies` | Find duplicate companies by domain and name | hubspot-admin-skills |
| `fix-lifecycle-stages` | Backfill and fix lifecycle stages | hubspot-admin-skills |
| `cleanup-deals` | Flag stale deals and send each owner a review task | hubspot-admin-skills |

The hubspot-admin-skills ones need a HubSpot service key in `.env` (see `.env.example`).

## Clay (lists and enrichment)
| Skill | What it does | Source |
|---|---|---|
| `clay-build-list` | ICP to enriched lead CSV, in the format the next steps read | this pack |
| `clay` | Clay's own guide to everything it can do | Clay plugin |
| `searches` | Find companies and people in Clay's database | Clay plugin |
| `routines` | Run a saved Clay function (for example a work-email finder) | Clay plugin |
| `signals` | Trigger-based watches: hires, funding, job changes | Clay plugin |
| `credits-quotas-plans` | Check credits before enriching | Clay plugin |
| `setup` | Install and sign in to the Clay CLI | Clay plugin |

The Clay plugin has around 30 more skills (tables, workflows, audiences). Ask "what can Clay do?" to see them.

## Lemlist (outreach)
| Skill | What it does | Source |
|---|---|---|
| `lemlist-campaign` | Create a paused email and LinkedIn campaign from the lead CSV | this pack |
| `icp-definer`, `persona-definer` | Sharpen who to target | Lemlist |
| `campaign-angle-finder`, `trigger-finder`, `pain-identifier` | Find what to say | Lemlist |
| `outbound-campaign-architect` | Design the sequence from Lemlist's benchmark data | Lemlist |
| `copywriting-first-touch`, `copywriting-follow-up`, `linkedin-sequence` | Write the messages | Lemlist |
| `copywriting-vp-sequence`, `copywriting-manager-sequence`, `copywriting-ic-sequence` | Full sequences by seniority | Lemlist |
| `copywriting-analyzer`, `copywriting-refiner` | Score and fix the copy | Lemlist |
| `reply-handler` | Answer a prospect's reply | Lemlist |
| `crm-duplicate-detector` | Find duplicate contacts and companies in any CRM export | Lemlist |

## Closing the loop
| Skill | What it does |
|---|---|
| `close-the-loop` | Push Lemlist replies and engagement back into HubSpot |
