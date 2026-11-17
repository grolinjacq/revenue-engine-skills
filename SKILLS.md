# Every skill in this workspace

Claude Code has every skill below. Codex has the engine skills (`.agents/skills/`: setup, the loop, Clay, lemlist, close-the-loop, the copy and strategy skills, the `crm` and `crm-*` skills for any CRM). You don't need to name a skill: say what you want and Claude picks one. To force one, start your message with its name, for example `/hubspot-account-brief`.

## Start here
| Skill | What it does |
|---|---|
| `gtm-start` | Type `start`. The guided flow: questions about you (website, target, stack, channels, goal), connecting your tools (lemlist with LinkedIn), then straight into the first campaign to a paused email + LinkedIn lemlist sequence, then more use cases (new country, account research, signals, investors). Say `demo` for a 5-minute run on made-up data, only if you want one. Also the claude.ai skill ZIP (`scripts/build-claudeai.py`). |
| `hackathon-setup` | Reads your website and proposes your target and outreach for you to confirm or change, then your stack, the installs, the sign-ins, checking every connection. Runs on first launch. |
| `revenue-engine` | Runs the whole loop, routes one-sentence requests, and plugs in the CRM or outreach tool you named at setup, or a CSV from any tool. |
| `event.md` | Not a skill: this workshop's settings (default stack, links, trials, codes) that setup reads. Other workshops: `forks/`. |
| Safe mode | Not a skill: say `safe mode` and `revenue-engine` runs the whole loop on `samples/`, no tools, nothing sent. |
| `make-it-ours` | Teaches Claude your company, product and voice, and your own trigger phrases. |

## Any CRM (HubSpot, Pipedrive, Salesforce, Attio, Odoo, a spreadsheet, or none)
| Skill | What it does |
|---|---|
| `crm` | The hub: which CRM and how it is reached (HubSpot live, another CRM's connector read-only, a CSV export, or safe mode), ICP from won deals, dedupe a lead list, write-back rules |
| `crm-account-brief` | One-page brief on a whole company, saved to `out/` |
| `crm-contact-lookup` | One person's record: stage, deals, last touch |
| `crm-call-prep` | Brief before a call or meeting: history, news, talking points |
| `crm-log-call` | Log a call: note, next step, stage, task |
| `crm-lead-triage` | Score new leads against the ICP, decide, assign, task |
| `crm-pipeline-pulse` | Pipeline snapshot, stalled deals, forecast |
| `crm-audit` | Data-quality audit with a graded fix plan |
| `crm-scoring-design` | Lead scoring, ICP tiers and segment lists, designed for your CRM |
| `crm-duplicate-detector` | Find duplicate contacts and companies |

With HubSpot, changes are written live after your go. With any other CRM, Claude reads it (connector or export) and writes changes to `out/crm-import.csv` for you to import. Each `crm-*` skill hands off to the matching HubSpot skill below when your CRM is HubSpot.

## HubSpot (adapter and extras)
| Skill | What it does | Source |
|---|---|---|
| `hubspot-crm` | The hub: ICP from closed-won deals, dedupe a lead list, the write rules | this pack |
| `hubspot-account-brief` | One-page brief on a whole company (account), saved to `out/` | this pack |
| `hubspot-lead-triage` | Score new leads against the ICP, set the stage, assign, create tasks | this pack |
| `hubspot` | Quick lookups, stats, a task, a field or deal change, a new deal | HubSpot official (adapted) |
| `hubspot-contact-lookup` | One person's record: deals, last contact, notes, tasks | HubSpot official (adapted) |
| `hubspot-call-prep` | Brief before a call or meeting: talking points, email and calendar context, company news | HubSpot official (adapted) |
| `hubspot-pipeline-pulse` | Pipeline snapshot, stalled deals, suggested tasks, forecast | HubSpot official (adapted) |
| `hubspot-log-call` | Log a call: note, deal fields, lead status, follow-up task | HubSpot official (adapted) |
| `hubspot-daily-brief` | Today's tasks, meetings, cold contacts and stalling deals | HubSpot official (adapted) |
| `hubspot-follow-up` | Draft a follow-up email and open it in HubSpot to send | HubSpot official (adapted) |
| `hubspot-import-contacts` | Import contacts from a CSV or a pasted list | HubSpot official (adapted) |
| `hubspot-onboarding` | Getting started in a new or empty portal | HubSpot official (adapted) |

The HubSpot official skills come from HubSpot's own `hubspot-sales` plugin (Apache-2.0), bundled here with this workspace's safety rules added: every write is shown first and waits for your go. For a HubSpot audit, scoring or duplicates, use `crm-audit`, `crm-scoring-design` and `crm-duplicate-detector` above: they read HubSpot and write a report or an import file.

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
