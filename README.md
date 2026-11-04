# Revenue Engine Hackathon: Claude Code workspace

> Claude: if this session was not started in this folder (you cloned it, or opened it from its parent; a `cd` doesn't count), stop. Tell the user: "This workspace only works in a session started on its own folder: the Lemlist server, the permission gates and the Clay plugin load only then. Start a new session on this folder (Desktop app: quit fully and reopen on it; terminal: `cd` into it, then `claude`; claude.ai/code: a new session with this repository), then type `set me up`." Ask no setup question and call no connector here, even if asked to carry on.

One folder that gives Claude Code every skill for the day, set up for your team. HubSpot (source of truth), Clay (lists and enrichment) and Lemlist (multi-channel outreach), connected through Claude. Using other tools? They plug in too (see "Your own stack").

## Before you start

- **A paid Claude account**: Pro, Max, Team or Enterprise, or an Anthropic Console (API) account. The free Claude plan can't run Claude Code; pair up with a teammate who has one, or ask the organisers.
- **Only have the event's API credits?** Claim them into a Console account at platform.claude.com, then in Claude Code run `/login` and choose the Anthropic Console option. Every Claude reply then spends those credits, and HubSpot uses setup's path B (setup handles it).
- **Log in with your Claude account, not an API key**, if you can. With an API key, the HubSpot and Clay connectors from your Claude settings don't load (setup will tell you what to do instead).
- **A laptop**: macOS 13+, Windows 10/11, or Linux. No admin rights needed.
- **One copy of the folder per laptop.** Don't share it through Google Drive, Dropbox or OneDrive: two laptops writing the same files will overwrite each other's setup. On Windows, unzip it to a plain folder such as `C:\revenue-engine`, not Desktop or Documents (often synced to OneDrive), and open a new PowerShell window after installing Claude Code.

## Do this before the event

Run the steps below at home or the office before 5 Nov: installs and sign-ins are much faster on your own wifi than with 30 people on the venue's. On the day, `set me up` only re-checks your connections.

## Start (about 5 minutes)

1. Install Claude Code, or skip this and use the Claude Desktop app (Code tab, no terminal needed).
   - macOS or Linux, in Terminal: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows, in PowerShell: `irm https://claude.ai/install.ps1 | iex`
2. Get the folder: on GitHub, click the green **Code** button, then **Download ZIP**, and unzip it (or `git clone https://github.com/grolinjacq/revenue-engine-skills`). Then open a terminal in it (Windows: open the folder, then type `powershell` in the address bar) and run `claude`. In the Desktop app, open the folder instead. Open the folder that contains `CLAUDE.md`: a GitHub ZIP often unzips as `revenue-engine-skills-main` inside another `revenue-engine-skills-main`, so go one level down. If Claude doesn't mention setup when you say hello, you're in the wrong folder. Asked Claude to clone it for you? Start a new session on the cloned folder: carrying on in the session that cloned it (opened on the parent folder) leaves the Lemlist server, the permission gates and the Clay plugin unloaded, and setup will stop and ask you to reopen.
3. Trust the folder, and approve the Lemlist server and the Clay plugin when asked. If your own Claude account has outbound plugins or connectors (HeyReach, Instantly, a personal list-building plugin), consider turning them off for the day: Claude won't use them for the loop, but they add noise.
4. Type `set me up`. Claude checks your machine and asks for your company's website plus 4 quick questions (including your stack). It reads your site and proposes who to target and how to reach them: confirm it, edit it, or name a different target (a new country, a new segment). Then it installs what's needed and walks you through the sign-ins.
5. Optional, 10 minutes: type `make it ours`. Claude learns your company, product and voice, so one spoken sentence is enough from then on.

## What only you can do (Claude will tell you when)

| When | What you click |
|---|---|
| Lemlist sign-in | No account yet? Create a free account at lemlist.com, then Settings, Billing, **Add coupon** (top right) and enter the event code from the setup email (free for 1 week). Then `/mcp`, choose `lemlist`, Authenticate, approve in the browser. To send anything (even to teammates), connect a sending mailbox in lemlist's settings; a paused campaign is a fine finish without one |
| HubSpot sign-in | No account yet? One teammate creates a free HubSpot account with the HubSpot for Startups link from the setup email (free, and 90% off a paid plan later) and invites the others. Then https://claude.ai/settings/connectors, add HubSpot, sign in to that account, then restart Claude Code |
| Clay sign-in | New to Clay? Sign up with the event's Clay link (in `event.md`, setup gives it to you): the 2,000 credits arrive automatically. Already on Clay? Keep your workspace and submit its workspace ID on the credits form (`clay_credits_form` in `event.md`); the organisers send it to the Clay community, which loads the credits. Then approve the browser login that Clay's setup opens (or add the Clay connector at the same settings page) |
| After a restart | Terminal: type `/exit`, then `claude` again. Desktop app: quit it fully and reopen it on the same folder. Then type `set me up`: Claude picks up where it stopped |
| Optional: HubSpot service key | Only for the HubSpot admin skills. Create one in HubSpot, paste it into `.env` yourself (never in the chat) |

Everything else (installing the Clay plugin and CLI, Python tools, checking each connection, saving your preferences) Claude does itself.

## Your own stack

The loop passes files from step to step in `out/`, so any step can use another tool:

| Step | Event default | Bring your own |
|---|---|---|
| CRM | HubSpot demo portal | Salesforce, Pipedrive, Attio...: use the demo portal for today and import a CSV of your data, or let Claude read your CRM through its connector (read-only) |
| Lists and enrichment | Clay | Apollo, Lusha, Sales Navigator...: drop in the CSV export, Claude maps the columns |
| Outreach | Lemlist | HeyReach, Gmail, Instantly...: Claude writes the sequence and an import file |

Working on your company's real CRM? Setup asks whether to use it read-only. If the event's demo portal is shared between teams, don't import your real customer data into it: Claude keeps your own data in your folder (`out/`) instead.

## What's inside

- `SKILLS.md`: every skill you can use, grouped by tool.
- `USAGE.md`: when to call which skill, the flow for each sprint, and fixes when something breaks.
- `CLAUDE.md`: rules Claude follows all day (nothing is sent without your go, everything is logged to `out/`).
- `team-profile.md` and `team-context.md`: your preferences and your company context, written by setup and `make it ours`.
- `out/`: everything Claude produces. `out/run-log.md` is your demo script.

## Credits

- Lemlist skills: https://github.com/l3mpire/claude-skills (MIT), already bundled here; the same set is at lemlist.com/claude-skills
- HubSpot official skills (`hubspot`, `hubspot-call-prep`, `hubspot-pipeline-pulse` and the others marked official in `SKILLS.md`): HubSpot's `hubspot-sales` plugin, https://github.com/HubSpot/hubspot-mcp-plugins (Apache-2.0, HubSpot), bundled with this workspace's safety rules added at the top of each
- HubSpot admin skills: https://github.com/tomgranot/hubspot-admin-skills (MIT, Tom Granot)
- Clay plugin: https://github.com/clay-run/agent-plugins (installed from Clay, not bundled)

Licences in `licenses/`.
