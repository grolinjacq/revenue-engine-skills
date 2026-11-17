# When to call which skill

Full list of skills: `SKILLS.md`.

You do not need to name skills. Say what you want and Claude picks the skill from its description. The prompts below are known to route well. To force a skill, start with its name, for example `/clay-build-list`.

## For hosts: test it in safe mode

Attendees skip this: the host shows the demo live. To test, say `safe mode` (or "test run"). The whole loop runs on the made-up company and leads in `samples/`, with no accounts, no credits and nothing sent, in Claude Code or Codex. Results land in `out/safe/`, and `samples/README.md` lists what a correct run produces. Say `switch to live` when you want to use your own data.

## Start the guided flow

Type `start`. The `gtm-start` flow asks about you, connects your tools, then goes straight into your first campaign on your own data, then more use cases (`use cases` switches between them).

## Just say it

After `make it ours`, one sentence is enough, typed or dictated (Wispr Flow works well): "find twenty CFOs at German fintechs that raised this year, draft a German campaign, don't launch". Claude says the plan in one line, then runs it.

## The one-glance table

| You want to... | Skill | Type something like |
|---|---|---|
| Set up or check everything is connected | `hackathon-setup` | "set me up", "check my connections" |
| Brief me on a company | `hubspot-account-brief` | "brief me on acme.com" |
| Prep a call with someone | `hubspot-call-prep` | "prep my call with Marta at Acme" |
| Look someone up | `hubspot-contact-lookup` | "pull up Marta Ruiz" |
| Get started in an empty HubSpot | `hubspot-onboarding` | "onboard me to HubSpot" |
| See how the pipeline looks | `hubspot-pipeline-pulse` | "how's my pipeline, with a forecast for this quarter" |
| Log a call | `hubspot-log-call` | "just got off the phone with Marta at Acme, demo next week" |
| A quick HubSpot change | `hubspot` | "create a deal for Acme, 20k", "move Globex to contract sent" |
| Plan my day | `hubspot-daily-brief` | "daily brief" |
| Draft a follow-up | `hubspot-follow-up` | "draft a follow-up to Marta" |
| Import contacts | `hubspot-import-contacts` | "import this CSV into HubSpot" |
| Work the new leads | `hubspot-lead-triage` | "triage leads from the last 2 weeks" |
| Know who to target | `hubspot-crm` | "look at our closed-won deals in HubSpot and write our ICP" |
| Propose our ICP from our website, or change target | `hackathon-setup` (steps 1b-1d) | "read our website and propose our ICP", "we want to target Germany now, redo the ICP" |
| Use your own ICP instead | `revenue-engine` | "our ICP is German SaaS, 50-500 people, Heads of Sales. Save it and build the list" |
| Find companies and people | `clay-build-list` | "build a list of 30 companies from the ICP and find 2 sales leaders at each" |
| Make sure you're not prospecting customers | `hubspot-crm` | "dedupe out/leads.csv against HubSpot" |
| Find an angle or write copy | Lemlist skills (`campaign-angle-finder`, `copywriting-first-touch`...) | "find 3 campaign angles for this ICP", "write the first-touch email" |
| Put it in Lemlist | `lemlist-campaign` | "create a lemlist campaign with email and LinkedIn for these leads, keep it paused" |
| Show the data coming back | `close-the-loop` | "sync replies from the campaign back to HubSpot" |
| Do it all | `revenue-engine` | "run the engine end to end, stop before launch" |

## Suggested flow for the session

`start` walks you through these in order; each block is one step of the loop. Without HubSpot, the CRM steps read your CRM's connector or a CSV export and write an import file. Teams with their own use case swap step 2 for their own ICP and keep the rest.

1. Setup (5 to 15 min). Type `start` (or "set me up"), give your website, and confirm or change the target Claude proposes. Fix anything red before moving on.
2. ICP. Setup already wrote `out/icp.md` from your website, so there's no ICP to type. Read it and correct it by hand if it is off: this file drives everything after it. Working on your own CRM with real closed-won deals? "Write our ICP from closed-won deals" gives a second opinion; Claude asks before replacing the confirmed one.
3. List. "Build the list from the ICP, 20 companies, 2 people each." Look at the first 10 companies when Claude shows them; say no early if they are wrong. Then "dedupe against our CRM".
4. Campaign. "Find angles", pick one, "write a 2-email plus LinkedIn sequence", then "create the campaign, paused". Check the two rendered sample emails and the sending settings Claude lists. You launch it yourself, later.
5. Close the loop. Once real replies come in, "close the loop" updates your CRM (or `out/crm-import.csv`). To see it work today, run it in safe mode.
6. Recap. Open `out/run-log.md`: one line per step with counts, your record of the run.

## Run it as an agent

Two easy routes:

- Headless run: the exact command and its permissions are in `revenue-engine` under "Agent mode (headless)" (Codex: `codex exec` with the same prompt) (it builds the list and drafts the campaign, then stops for your review).
- Recurring check: `/loop 1h close the loop` in an open session prepares the CRM updates every hour; you approve each batch.

## When something breaks

| Symptom | Fix |
|---|---|
| "tool not found" or a server is missing | `/mcp`, check the server is connected, re-authenticate |
| HubSpot returns nothing for deals | Your demo portal may have no closed-won deals. Give your ICP in words instead. |
| Clay out of credits | Claude stops and offers a cheaper plan (email only, fewer companies); pick one |
| HubSpot connector missing after setup | Logged in with an API key? Run `/login` with your Claude account, or use your CRM's CSV export (path B needs a client ID in `event.md`, and this workshop has none) |
| Clay plugin won't install (network) | Add the Clay connector at claude.ai/settings/connectors instead, then restart |
| Your leads come from Apollo or another tool | "Here's my CSV": Claude maps the columns and lists the rows it dropped |
| You named HeyReach, Instantly or another outreach tool at setup | Claude writes the sequence and `out/outreach-import.csv`; you import it and click launch in your tool. Lemlist is the only tool where Claude builds the campaign itself |
| You named Pipedrive, Salesforce, Odoo or another CRM at setup | Claude reads it (read-only, or from its CSV export) and writes CRM updates to `out/crm-import.csv` for you to import |
| Claude used, or offered to use, a tool you never named | Stop it and say so: it should only use the tools in `team-profile.md`. Re-run `set me up` to check the stack |
| Lemlist channel not allowed | Your plan doesn't include it: see the lemlist sign-up in `event.md` (trial or code) |
| Clay's `campaigns` skill answered instead of Lemlist | Clay also has email campaigns. Say "in lemlist", or start with `/lemlist-campaign` |
| Claude picked the wrong skill | Start your message with the skill name, for example `/hubspot-crm` |
