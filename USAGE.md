# When to call which skill

Full list of skills: `SKILLS.md`.

You do not need to name skills. Say what you want and Claude picks the skill from its description. The prompts below are known to route well. To force a skill, start with its name, for example `/clay-build-list`.

## Just say it

After `make it ours`, one sentence is enough, typed or dictated (Wispr Flow works well): "find twenty CFOs at Spanish fintechs that raised this year, draft a Spanish campaign, don't launch". Claude says the plan in one line, then runs it.

## The one-glance table

| You want to... | Skill | Type something like |
|---|---|---|
| Set up or check everything is connected | `hackathon-setup` | "set me up", "check my connections" |
| Brief me before a call | `hubspot-account-brief` | "brief me on acme.com" |
| See how the pipeline looks | `hubspot-pipeline-review` | "pipeline review for this quarter" |
| Log a call or move a deal | `hubspot-log-activity` | "log my call with Marta at Acme, demo next week" |
| Work the new leads | `hubspot-lead-triage` | "triage leads from the last 2 weeks" |
| Know who to target | `hubspot-crm` | "look at our closed-won deals in HubSpot and write our ICP" |
| Propose our ICP from our website, or change target | `hackathon-setup` (steps 1b-1d) | "read our website and propose our ICP", "we want to target Germany now, redo the ICP" |
| Use your own ICP instead | `revenue-engine` | "our ICP is Spanish SaaS, 50-500 people, Heads of Sales. Save it and build the list" |
| Find companies and people | `clay-build-list` | "build a list of 30 companies from the ICP and find 2 sales leaders at each" |
| Make sure you're not prospecting customers | `hubspot-crm` | "dedupe out/leads.csv against HubSpot" |
| Find an angle or write copy | Lemlist skills (`campaign-angle-finder`, `copywriting-first-touch`...) | "find 3 campaign angles for this ICP", "write the first-touch email" |
| Put it in Lemlist | `lemlist-campaign` | "create a lemlist campaign with email and LinkedIn for these leads, keep it paused" |
| Show the data coming back | `close-the-loop` | "sync replies from the campaign back to HubSpot" |
| Do it all | `revenue-engine` | "run the engine end to end, stop before launch" |

## Suggested flow for the day

Each block matches a sprint. Teams with their own use case swap step 1 for their own ICP and keep the rest.

1. Setup (5 to 15 min). Unzip, run `claude`, type "set me up", give your website, and confirm or change the target Claude proposes. Fix anything red before moving on.
2. HubSpot sprint. Setup already wrote `out/icp.md` from your website. With closed-won deals in HubSpot, "check our ICP against closed-won deals" compares it with real wins. Correct `out/icp.md` by hand if it is off: this file drives everything after it.
3. Clay sprint. "Build the list from the ICP, 20 companies, 2 people each." Look at the first 10 companies when Claude shows them; say no early if they are wrong. Then "dedupe against HubSpot".
4. Lemlist sprint. "Find angles", pick one (or keep all three and say "A/B test the subject lines"), say "one sequence per segment" if your list has segments, "write a 2-email plus LinkedIn sequence", then "create the campaign, paused". Check the two rendered sample emails and the sending settings Claude lists.
5. Loop sprint. Start a seed campaign with only teammates' addresses, reply to it from a teammate's inbox, or tag a lead interested in Lemlist, then "close the loop". Show the note and lifecycle change in HubSpot.
6. Demo prep. Open `out/run-log.md`: it is your demo script, one line per step with counts.

## Going for the bonus (an AI agent)

The judges give a bonus for an agent. Two easy routes:

- Headless run: the exact command and its permissions are in `revenue-engine` under "Bonus: agent mode" (it builds the list and drafts the campaign, then stops for your review).
- Recurring check: `/loop 1h close the loop` in an open session prepares the CRM updates every hour; you approve each batch.

## When something breaks

| Symptom | Fix |
|---|---|
| "tool not found" or a server is missing | `/mcp`, check the server is connected, re-authenticate |
| HubSpot returns nothing for deals | Your demo portal may have no closed-won deals. Give your ICP in words instead. |
| Clay out of credits | Claude stops and offers a cheaper plan (email only, fewer companies); pick one |
| HubSpot connector missing after setup | Logged in with an API key? Run `/login` with your Claude account, or ask the organisers for the HubSpot client ID (path B) |
| Clay plugin won't install (network) | Add the Clay connector at claude.ai/settings/connectors instead, then restart |
| Your leads come from Apollo or another tool | "Here's my CSV": Claude maps the columns and lists the rows it dropped |
| Lemlist channel not allowed | Ask the Lemlist team for the one-week multi-channel code |
| Clay's `campaigns` skill answered instead of Lemlist | Clay also has email campaigns. Say "in lemlist", or start with `/lemlist-campaign` |
| Claude picked the wrong skill | Start your message with the skill name, for example `/hubspot-crm` |
