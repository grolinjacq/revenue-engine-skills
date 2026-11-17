# Revenue engine skills: Claude Code and Codex workspace

> Claude: if this session was not started in this folder (you cloned it, or opened it from its parent; a `cd` doesn't count), stop. Tell the user: "This workspace only works in a session started on its own folder: the Lemlist server, the permission gates and the Clay plugin load only then. Start a new session on this folder (Desktop app: quit fully and reopen on it; terminal: `cd` into it, then `claude`; claude.ai/code: a new session with this repository), then type `set me up`." Ask no setup question, write no file, run no tool CLI and call no connector here, even if asked to carry on.

One folder that turns Claude Code or Codex into an outbound GTM engine: find the right people in Clay, write the sequence, push it to lemlist (paused, nothing sent without your go), and log the results back to your CRM, whatever CRM you use, or none. Built for hands-on workshops; this workshop's settings are in `event.md`.

## Start here: one drop, then type `start`

| Your assistant | What you do | Plan needed |
|---|---|---|
| claude.ai (web or desktop chat) | Settings > Capabilities: turn on "Create and edit files". Then Customize > Skills > + > Create skill > Upload a skill, and upload `gtm-start.zip` (download it from this repo's Releases page, or your workshop's access card). New chat, type `start here` (or `use gtm-start`). | Any, Free included |
| Claude Code (desktop, terminal or claude.ai/code) | Open a session on this folder (claude.ai/code: pick this repository), type `start` | Paid Claude plan or Console |
| Codex (app or CLI) | Unzip, open the folder, trust it, type `start` | Any ChatGPT plan with Codex |

`start` runs the `gtm-start` flow, in a coach's voice: it opens with a short walkthrough of what's inside and what happens, then asks one question at a time as A, B or C, with A already filled in from what it can see (your website, your git email domain in Claude Code, earlier files), so you mostly press A, and pressing A on a step moves straight into the next one; safety settings are fixed defaults, never questions. It covers questions about you (website to target, stack, channels, your goal right now), connecting Clay, lemlist (with LinkedIn) and your CRM, then straight into your first campaign (ideal customer with up to 2 fit checks built from your must-haves, buyer persona, companies from Clay, an enrich-and-score step where Claude reads each company's site (Clay research for the rest) to answer the fit checks and score 1 to 5 with sources, people from Clay, a 5-step sequence to book 15-minute calls, built on P-L-V-A (Pitch, Legitimacy, Value, Ask spread across a connection note, an opener, a proof, an ask and a breakup, each message standing alone), inside a branching email + LinkedIn sequence that uses lemlist's conditions (has a LinkedIn URL, invite accepted) so each lead gets the best channel available, a paused lemlist campaign), then more use cases. On lemlist's 14-day trial it asks your sign-up and planned launch dates and keeps the sequence inside the trial: the last step goes out no later than 12 days after sign-up, on weekdays (for a sign-up on Wednesday 18 Nov and a weekend launch, Monday 23 to Monday 30 Nov). If that leaves under 6 sending days, you need the workshop offer's month or a paid plan. Nothing is sent: you press Launch yourself, later.

After each step it gives you the link to what it made (the Clay table or search, the lemlist campaign) when the tool returns one, so you can click straight to it. What it checks for you: only your own company's Clay and lemlist accounts; only emails Clay marks valid go into the campaign (unverified ones wait in `held.csv`, people with no email in `pending.csv`; if Clay gives no email status at all, it asks you first and adds them only on your say-so, counted apart, with the bounce risk named); business contacts only; opt-outs and existing customers removed. If the session ends before you're done, it hands you every file and the step to resume at home. In claude.ai chat, files don't persist between chats: keep the files it gives you and upload them to a new chat to resume.

While it runs, three things are worth remembering (`help` shows them, plus the create phrase below):

| Type | What it does |
|---|---|
| `use cases` | Switch to another playbook at any time (first campaign, international expansion, account research, signal-based outreach, investors and partners). It gives you your files first, cancels anything waiting for your go, and asks before reusing your ICP and persona. While a playbook is in progress the menu starts with "0. Resume": pick it to go back to your step, with the same campaign (never a second one). |
| `where am I` | The step you're on and the files so far. |
| `stop` | Stops and gives you every file so far. Nothing is launched. |

Everything else, say in your own words and your own language ("email only", "change the persona", "resume" after uploading your files in a new chat). Two exact phrases change lemlist: `go, create paused, 24 leads` creates the campaign, paused, and `go, add 6 leads` adds missing leads to your paused campaign, each with the number it shows you. `next`, `yes` or `ok` never create a campaign, and a bare `go` at the create step just shows the preview again. In the workshop you never deal with Clay credits: the run is sized to fit them: about 20 companies searched, the best 10 after enrich and score, 2 people at each (20 people), and up to two top-ups of 5 companies if fewer than 15 people come back with a valid email.

In the workshop room the goal is your paused campaign, through all seven campaign steps; whatever doesn't fit, you finish at home. Typing `start` again asks whether to restart (your old files kept as `-v1`) or continue. Each playbook names its files with its own prefix (`expansion-leads.csv`), so switching never overwrites another playbook's work, and a switch waits until a campaign the assistant created reads paused or draft.

## For hosts: test the workspace in safe mode (no accounts)

Attendees get no demo: the host runs it live in the room, and `start` goes straight from the questions about you into the campaign. To test the workspace yourself, open the folder in Claude Code or Codex and type `safe mode`: the loop runs on the sample startup Karvon AI and the sample files in `samples/`, with no credits and nothing sent, and its files land in `out/safe/` (`samples/README.md` lists what a correct run produces).

## Claude Code or Codex

| | Claude Code | Codex (included with ChatGPT plans) |
|---|---|---|
| Rules | `CLAUDE.md` (loads `RULES.md`) | `AGENTS.md` (same rules) |
| Skills | `.claude/skills/` (all skills) | `.agents/skills/` (the engine skills listed in `scripts/build-codex.py`; most `hubspot-*` skills stay in Claude) |
| lemlist | `.mcp.json` (server `lm`), sign in with `/mcp` | `.codex/config.toml`, sign in with `codex mcp login lm` (trust the folder first) |
| Clay | Clay plugin or Clay connector | `clay` CLI |
| Safe mode | yes | yes |

Plain ChatGPT chat (without Codex) can't open this folder or run the skills: use Codex on the unzipped folder.

## Before you start

- **For this folder (Claude Code)**: a paid Claude account (Pro, Max, Team or Enterprise) or an Anthropic Console (API) account. On the free Claude plan, use the `gtm-start.zip` skill in claude.ai instead (Start here, above).
- **Log in with your Claude account, not an API key**, if you can. With an API key, the HubSpot and Clay connectors from your Claude settings don't load (setup will tell you what to do instead).
- **A laptop**: macOS 13+, Windows 10/11, or Linux. No admin rights needed.
- **One copy of the folder per laptop.** Don't share it through Google Drive, Dropbox or OneDrive: two laptops writing the same files will overwrite each other's setup. On Windows, unzip it to a plain folder such as `C:\revenue-engine`, not Desktop or Documents (often synced to OneDrive), and open a new PowerShell window after installing Claude Code.

## In the workshop room

Nothing is needed before the session: everything is handed out in the room. In the workshop, use the claude.ai route on the access card: it needs no install, and installs on shared venue wifi are slow. Follow `event.md` for lemlist: sign up through the workshop's link (on your access card) to start the 14-day trial; the code for the free month is added later, when you are ready to launch.

## Start (about 5 minutes)

1. Install Claude Code, or skip this and use the Claude Desktop app (Code tab, no terminal needed).
   - macOS or Linux, in Terminal: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows, in PowerShell: `irm https://claude.ai/install.ps1 | iex`
2. Get the folder: on GitHub, click the green **Code** button, then **Download ZIP**, and unzip it (or `git clone https://github.com/grolinjacq/revenue-engine-skills`). Then open a terminal in it (Windows: open the folder, then type `powershell` in the address bar) and run `claude`. In the Desktop app, open the folder instead. Open the folder that contains `CLAUDE.md`: a GitHub ZIP often unzips as `revenue-engine-skills-main` inside another `revenue-engine-skills-main`, so go one level down. If Claude doesn't mention setup when you say hello, you're in the wrong folder. Asked Claude to clone it for you? Start a new session on the cloned folder: carrying on in the session that cloned it (opened on the parent folder) leaves the Lemlist server, the permission gates and the Clay plugin unloaded, and setup will stop and ask you to reopen.
3. Trust the folder, and approve the Lemlist server and the Clay plugin when asked. Already have a CRM or outreach tool? Name it at setup and Claude will use it. Clay can slot in alongside. Claude never uses a CRM or outreach tool you didn't name.
4. Type `set me up`. Claude checks your machine and asks one question at a time, starting with your company's website (proposed from your git email when it can), then your stack and your goal. It reads your site, then checks what it read with you point by point, five quick A/B/C questions: what you sell, who buys it today and your proof, today's target, who to contact, and the outreach angle. Change any point, or name a different target (a new country, a new segment). Then it installs what's needed and walks you through the sign-ins.
5. Your voice: Claude infers your tone and words to avoid from your website, and asks you to confirm them in one question just before it writes the sequence. Later, `make it ours` (10 minutes) adds your own trigger phrases, so one spoken sentence is enough from then on.

## What only you can do (Claude will tell you when)

| When | What you click |
|---|---|
| Lemlist sign-in | No account yet? Sign up the way `event.md` says (`lemlist_trial`: the sign-up link and code on your access card; then enter the code in lemlist under Settings > Billing & Users > Subscription > Manage, with the coupon button, on Multichannel Monthly; that step asks for a payment card). Then `/mcp`, choose `lm` (the lemlist server), Authenticate, approve in the browser. To send anything (even to teammates), connect a sending mailbox in lemlist's settings; a paused campaign is a fine finish without one |
| HubSpot sign-in | Only if HubSpot is your CRM. No account yet? Use the HubSpot link in `event.md` if your workshop gives one, or a free HubSpot account. Then https://claude.ai/settings/connectors, add HubSpot, sign in to that account, then restart Claude Code |
| Clay sign-in | New to Clay? Sign up with your workshop's Clay link (`clay_signup_url` in `event.md`, or the access card when it shows a placeholder), so the workshop's credits (`clay_credits`) apply. Already on Clay? Keep your workspace and submit its workspace ID on the credits form (`clay_credits_form` in `event.md`); the organisers send it to the Clay community, which loads the credits. Then approve the browser login that Clay's setup opens (or add the Clay connector at the same settings page) |
| After a restart | Terminal: type `/exit`, then `claude` again. Desktop app: quit it fully and reopen it on the same folder. Then type `set me up`: Claude picks up where it stopped |

Everything else (installing the Clay plugin and CLI, checking each connection, saving your preferences) Claude does itself. In Claude Code, lemlist reads (team, campaigns, leads, status) run without a prompt, every lemlist action that creates or changes something asks you to approve it first, and sends are blocked (`.claude/settings.json`).

## Optional: block launching from your assistant

By default the skills never launch, send or connect a mailbox, because their rules say so and Claude reads back that each campaign is paused. `gtm-start` mentions it in one line in your homework at the end of the session (never as a question in the room). One-to-one sends (`send_message`, `send_task`) are already blocked in this workspace's settings. If you want a hard block on top, so your assistant can't do these even by mistake, switch it on yourself (you edit the file; the assistant won't). After that, you launch, connect a mailbox and change a campaign's state only in lemlist itself, pausing included: if a campaign is ever running by mistake, pause it in lemlist yourself.

- **Claude Code:** add these to the `permissions.deny` list of `.claude/settings.local.json` in this folder (create the file if it is missing; it stays on your machine). A new file looks like:
  ```json
  {"permissions": {"deny": ["mcp__lm__launch_campaign", "mcp__lm__set_campaign_state", "mcp__lm__connect_email_account",
    "mcp__lemlist__launch_campaign", "mcp__lemlist__set_campaign_state", "mcp__lemlist__connect_email_account",
    "mcp__claude_ai_Lemlist__launch_campaign", "mcp__claude_ai_Lemlist__set_campaign_state", "mcp__claude_ai_Lemlist__connect_email_account"]}}
  ```
  Then restart Claude Code; it tells you if the file is invalid.
- **Codex:** in `.codex/config.toml`, add `"launch_campaign", "set_campaign_state", "connect_email_account"` to the `disabled_tools` list under `[mcp_servers.lm]`, then restart Codex. The file is part of the workspace, so keep your edit when you update it.
- **claude.ai:** in Settings > Connectors, open `lm`. If it lets you turn off single tools, turn off `launch_campaign`, `set_campaign_state` and `connect_email_account`. If it doesn't, answer Deny or no whenever a launch, start, resume or mailbox connection is asked for (approving a pause is fine; with these tools turned off, pause in lemlist yourself).

## Your own stack

Already have a CRM or outreach tool? Name it at setup and Claude will use it. Clay can slot in alongside. HubSpot, Clay and Lemlist are the tested path today; with any other tool, Claude reads it (through its Claude connector if it has one, or its CSV export) and prepares everything, and you do the final import or launch click yourself.

| Step | Tested path | Your own tool |
|---|---|---|
| CRM | HubSpot (event portal or your own) | Pipedrive, Salesforce, Attio, Odoo...: Claude reads it (or its CSV export) to find your best customers and skip people you already have. Updates come back as a file you import. Want to see a live update? Add the event's HubSpot portal too, when your workshop gives one |
| Lists and enrichment | Clay | Apollo, Lusha, Sales Navigator...: drop in the CSV export, Claude maps the columns, and Clay can enrich it |
| Outreach | Lemlist (Claude builds the campaign, paused) | HeyReach, Instantly, Smartlead...: Claude writes the messages and the list of people to import, and you click launch |

For the loop, Claude only uses the tools you name at setup, checked by their address, not their name: an outreach tool or CRM you didn't name is never used, even if it's switched on in your Claude account.

Working on your company's real CRM? Your own CRM is always read-only here, and if it's a HubSpot portal setup asks whether to use it read-only. If the event's demo portal is shared between teams, don't import your real customer data into it: Claude keeps your own data in your folder (`out/`) instead.

## Skills at a glance

44 skills in `.claude/skills/` (Claude Code); the 34 engine skills are mirrored to `.agents/skills/` for Codex. The full list, with what each does, is in `SKILLS.md`.

| Group | Skills |
|---|---|
| Start and setup | `gtm-start` (type `start`; also the claude.ai ZIP), `hackathon-setup` (the setup and sign-in steps `gtm-start` runs), `revenue-engine` (the loop, routing, safe mode, CSV import), `make-it-ours` |
| Any CRM | `crm`, `crm-account-brief`, `crm-contact-lookup`, `crm-call-prep`, `crm-log-call`, `crm-lead-triage`, `crm-pipeline-pulse`, `crm-audit`, `crm-scoring-design`, `crm-duplicate-detector` |
| HubSpot | `hubspot-crm`, `hubspot-account-brief`, `hubspot-lead-triage`, and HubSpot's official sales skills: `hubspot`, `hubspot-contact-lookup`, `hubspot-call-prep`, `hubspot-pipeline-pulse`, `hubspot-log-call`, `hubspot-daily-brief`, `hubspot-follow-up`, `hubspot-import-contacts`, `hubspot-onboarding` |
| Clay | `clay-build-list`, plus the Clay plugin's own skills |
| Lemlist and copy | `lemlist-campaign`, `icp-definer`, `persona-definer`, `pain-identifier`, `trigger-finder`, `campaign-angle-finder`, `outbound-campaign-architect`, `copywriting-first-touch`, `copywriting-follow-up`, `copywriting-vp-sequence`, `copywriting-manager-sequence`, `copywriting-ic-sequence`, `linkedin-sequence`, `copywriting-analyzer`, `copywriting-refiner`, `reply-handler` |
| Close the loop | `close-the-loop` |

## What's inside

- `SKILLS.md`: every skill you can use, grouped by tool.
- `USAGE.md`: when to call which skill, the flow for the session, and fixes when something breaks.
- `event.md`: this workshop's settings (links, trials, default stack). Each workshop's settings file is kept in `forks/`; `FORKING.md` explains how to make one.
- `samples/`: the made-up data safe mode runs on, with the expected results in `samples/README.md`.
- `scripts/build-claudeai.py` builds the claude.ai ZIP (`dist/gtm-start.zip`); `scripts/build-codex.py` rebuilds the Codex copy (`AGENTS.md`, `.agents/skills/`). `.github/workflows/` checks the Codex copy on every push; the ZIP release workflow runs only when started by hand from the Actions tab, with a tag.
- `RULES.md`, `CLAUDE.md`, `AGENTS.md`: rules the assistant follows all day (nothing is sent without your go, everything is logged to `out/`).
- `team-profile.md` and `team-context.md`: your preferences and your company context, written by setup and `make it ours`.
- `out/`: everything Claude produces. `out/run-log.md` is your record of the run, one line per step.

## Credits

- Lemlist skills: https://github.com/l3mpire/claude-skills (MIT), already bundled here; the same set is at lemlist.com/claude-skills
- HubSpot official skills (`hubspot`, `hubspot-call-prep`, `hubspot-pipeline-pulse` and the others marked official in `SKILLS.md`): HubSpot's `hubspot-sales` plugin, https://github.com/HubSpot/hubspot-mcp-plugins (Apache-2.0, HubSpot), bundled with this workspace's safety rules added at the top of each
- Clay plugin: https://github.com/clay-run/agent-plugins (installed from Clay, not bundled)

Licences in `licenses/`.
