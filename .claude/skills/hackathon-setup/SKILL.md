---
name: hackathon-setup
description: Set up this hackathon workspace for a team - check the environment, ask their preferences and stack, install what's needed, walk through the HubSpot, Lemlist and Clay sign-ins, verify every connection, and write team-profile.md. Use on first launch, on "set me up", "set up the workspace", "connect my tools", "check my connections", or when a tool is not connected.
---

# Hackathon setup

Goal: the team goes from unzipped folder to a working stack in about 5 minutes, doing only what Claude cannot do for them (browser sign-ins, clicks in a tool's UI). Do everything else yourself. One action at a time in each message.

Read `event.md` first: it holds the organisers' facts (demo portal, client ID for path B, Lemlist code, who to ask). If a value still shows `<...>`, it wasn't filled in: ask the user or the organisers instead of guessing.

Re-runnable and resumable: if `team-profile.md` exists, read it, skip what is done, and only fix what is red. Write the profile as soon as the questions are answered (every tool `pending`), and update it after each sign-in, so a restart never loses progress or asks the questions again. Several steps need a Claude Code restart; before each one, say: "After the restart, type `set me up` and I'll pick up where we stopped." Restart means: terminal, `/exit` then `claude`; Desktop app, quit it fully (Cmd+Q on Mac, Quit from the tray on Windows), not just close the window. If a skill or connector that a restart should have loaded is still missing, say that the app was probably not fully quit.

## 0. Preflight (silent, before any question)

Check these yourself and note the results; only mention a problem.

1. Claude login. Ask the user to run `/status` (or run `claude auth status` yourself) to see how Claude Code is signed in. If it is an API key or a Console account (or `ANTHROPIC_API_KEY` is set), claude.ai connectors (HubSpot path A, the Clay connector) are disabled. Tell the user, and offer: switch to their Claude account (macOS/Linux: `unset ANTHROPIC_API_KEY`; PowerShell: `Remove-Item Env:ANTHROPIC_API_KEY`; also remove it from their shell profile; then restart and run `/login`), or keep the key and use HubSpot path B. Users with only the event's API credits: they claim them into a Console account at platform.claude.com, run `/login` and choose the Anthropic Console option; tell them every Claude reply spends those credits, set `login: api-key`, and use HubSpot path B (or CSV if `hubspot_mcp_client_id` is still a placeholder: ask the organisers in the room).
2. OS and shell. Note Windows native (PowerShell), WSL, macOS or Linux. On Windows use `python` and PowerShell syntax; in WSL or headless Linux, browsers may not open, so print every sign-in URL for the user to open.
3. Network. If GitHub is unreachable (`claude plugin marketplace add` fails), Clay goes through the connector path in step 3, not the plugin: skip the plugin commands in step 2.
4. Python, only if the team wants the HubSpot admin skills: run `python --version` (Windows: `py --version`; the Microsoft Store stub doesn't count) and `python -m uv --version`. Use `python -m uv run ...` on Windows. If either fails, mark the admin skills unavailable and carry on.
5. Surface. In the Desktop app, slash commands like `/mcp` and `/plugin` may live in the app's settings instead; if one does nothing, say where to find it in the app.

## 1. Preferences and stack (one message, 7 short questions)

Ask all at once, each with a default so the team can answer "defaults":

1. Team name? (default: the user's first name)
2. Use case: your own, or the default loop (CRM ICP, build a list, multi-channel campaign, back to the CRM)? If your own, one line.
3. Who are you targeting? Industry, company size, country or city, job titles. ("don't know" is fine)
4. Your stack, one per line, or "event accounts":
   - CRM: HubSpot event demo portal (default) | your own HubSpot | other CRM (name it) | none
   - Lists and enrichment: Clay (default) | other tool (name it, we'll use its CSV export) | none
   - Outreach: Lemlist (default) | other tool (name it) | none
5. Language for outreach copy: English, Spanish, French...? (default: English)
6. How careful should I be? A: ask before every write and every credit spend. B: ask before CRM writes, credit spend over the cap, and anything sent to people. (default: B)
7. Credit cap for Clay today? (default: 200 credits)

Write `team-profile.md` in the workspace root:

```
# Team profile
team: <name>
setup: incomplete | complete | degraded
use_case: <default loop | one line>
target: <one line, or "derive from CRM">
copy_language: <language>
write_mode: <A | B>
clay_credit_cap: <number>
crm: <hubspot-demo | hubspot-own | none>
crm_source: <hubspot | other: <name, e.g. Salesforce> | none>   # where the team's own data lives
crm_mode: <full | read-only>   # hubspot-demo starts as full
lists: <clay | other: <name> | none>
outreach: <lemlist | other: <name> | none>
login: <claude.ai | api-key>
os: <windows | wsl | macos | linux>
tools:
  hubspot: <pending | connected (<portal>, path A or B) | not available (<reason>)>
  lemlist: <pending | connected (<team>) | not available (<reason>)>
  clay: <pending | connected (<workspace>, plugin|connector) | not available (<reason>)>
  hubspot_service_key: <not set | set>
updated: <date time>
```

If the team gave a target, also write `out/icp.md` in the format `hubspot-crm` uses (put a city in `notes`; fill `exclude_domains` from HubSpot customers and open deals once HubSpot is connected).

### Other stacks: what to tell the team (the loop works with any of them)

The loop runs on files in `out/` (see `revenue-engine`, "Step contracts"), so any step can be filled by another tool or a CSV:

- **Other CRM (Salesforce, Pipedrive, Attio...)**: recommend the event's HubSpot demo portal as today's CRM (`crm: hubspot-demo`, `crm_source: other: <name>`), so judges see the full loop, and still connect it in step 3. Their own data: read it for the ICP through their CRM's Claude connector (read-only) or a CSV export kept in `out/`. If `event.md` says `hubspot_portal_shared: yes`, never import their customer or prospect records into the demo portal: other teams can see it. Never run `hubspot-*` skills against another CRM.
- **Other list tool (Apollo, Lusha, Sales Navigator...)**: export a CSV; `revenue-engine` normalises it into `out/leads.csv`.
- **Other outreach tool (HeyReach, Gmail, Instantly...)**: `lemlist-campaign` writes the sequence and a ready-to-import CSV instead of creating a campaign. Mention that the Lemlist team hands out a one-week multi-channel code at the event.

## 2. Installs (do these yourself)

- Clay plugin, only if `lists: clay`. Check whether Clay's skills (`clay`, `searches`, `setup`) are available. If not, run `claude plugin marketplace add clay-run/agent-plugins` then `claude plugin install clay@clay-plugins`. If a command is refused or errors, try once with the user typing `/plugin marketplace add clay-run/agent-plugins` and `/plugin install clay@clay-plugins`; if that fails too (often GitHub blocked), switch Clay to the connector path in step 3. The plugin needs a restart to appear.
- HubSpot admin skills, only if the team wants audits, ICP tiers, lists or lifecycle fixes: their scripts run with `uv`. Install it (`python -m pip install uv` on Windows, `python3 -m pip install uv` elsewhere) and `requirements.txt` the same way. Skip this otherwise.
- Create `out/` and `out/run-log.md` if missing.

## 3. Sign-ins (the user's hands, one at a time)

Only for tools in the team's stack. Verify each before moving on.

**Lemlist** (already in `.mcp.json`).
- User action: `/mcp`, choose `lemlist`, Authenticate, approve in the browser, pick the team.
- Verify: call a Lemlist tool that lists campaigns or the team. Record the team name.
- No account yet: suggest the Lemlist trial with `lemlist_trial_code` from `event.md`, or set `outreach: none` and carry on.

**HubSpot** (not in `.mcp.json`: HubSpot's server can't be added from its URL alone).
- Path A, default, needs `login: claude.ai`: open https://claude.ai/settings/connectors, add HubSpot, sign in, pick the portal. Then restart Claude Code (connectors load at start; the user must be logged in with the same Claude account).
- Path B, for API-key logins, or when `event.md` has a `hubspot_mcp_client_id`: run `claude mcp add --transport http --client-id <ID from event.md> --client-secret --callback-port 8765 hubspot https://mcp.hubspot.com` (the user types the secret at the prompt; never in a file or the chat), then `/mcp`, choose `hubspot`, authenticate. Details in `connect-hubspot-mcp`.
- Verify: call the HubSpot user-details tool (`get_user_details`, or the closest tool that returns the portal) and report the portal and which objects are writable.
- No HubSpot account yet: give the sign-up link from `event.md` (`hubspot_demo_portal`); one teammate creates the free account and invites the others. A new account has no deals, so step 1 of the loop takes the ICP in words.
- Production check: compare the portal with `hubspot_demo_portal` in `event.md`. If it says each team uses its own new free account, ask whether this portal is the one created for the event (then `crm_mode: full`) or the company's real CRM (then B or C below). If it doesn't match (or `event.md` isn't filled in and the portal name doesn't say demo, test or sandbox), ask: A) switch to the demo portal (recommended), B) use this portal read-only, C) use it fully, I own it. Record the answer as `crm_mode` (C is `full`, B is `read-only`). Every HubSpot write skill reads `crm_mode` first.
- Optional service key for the admin skills: the user creates one in HubSpot (Settings, Integrations, Service keys) and pastes it into `.env` themselves (copy `.env.example`). If they paste a key into the chat instead, do not repeat it or store it, and tell them to rotate it in HubSpot and put the new one in `.env`.

**Clay**.
- No Clay account yet: send the user to `clay_signup_url` from `event.md` (the event's sign-up link, never a plain clay.com sign-up: the credits arrive automatically there). Then continue below.
- Already on Clay: keep that workspace; no new one is needed. Send the user to `clay_credits_form` from `event.md` to submit the workspace ID (the number after `/workspaces/` in the app.clay.com address bar); the organisers forward it to the Clay community, which loads the credits. Then continue below.
- Plugin path: run Clay's `setup` skill, which installs the `clay` CLI and runs `clay login` (browser; print the URL if it can't open). Verify with `clay whoami`.
- Connector path (plugin failed, or Windows/WSL CLI trouble): the user adds the Clay connector at https://claude.ai/settings/connectors and restarts. Verify by listing Clay's tools. Needs `login: claude.ai`.
- Check the credit balance (Clay's `credits-quotas-plans` skill or the workspace tool) and note it against `clay_credit_cap`. Event credits (`clay_credits` in `event.md`) may still be on their way for an existing workspace whose ID was just submitted; until then, work within the balance shown. If they're missing for a workspace created through the link, or long after the form, tell the user to flag it to the organisers (`help` in `event.md`), with their workspace name, and carry on.

If a sign-in fails twice, mark the tool `not available (<reason>)` and carry on.

## 4. Finish

1. Set `setup`:
   - `complete`: every tool in the team's stack is connected.
   - `degraded`: at least one step of the loop works but a tool is missing or replaced by CSV. This is a finished setup, not a pending one; do not re-run setup on the next session start.
   - `incomplete`: only while setup is still in progress (for example waiting on a restart). If the user wants to start working before finishing, set `degraded` and list what's missing, so the next session doesn't force setup.
2. Show a status table: tool, status, account, and which loop steps run as normal, by CSV, or not at all.
3. List any manual to-dos left, then point to `SKILLS.md` and suggest the first prompt for their use case and stack. If the team's HubSpot portal is new and empty, one of the suggestions is `hubspot-onboarding` ("onboard me to HubSpot").
