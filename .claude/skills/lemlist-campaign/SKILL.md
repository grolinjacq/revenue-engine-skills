---
name: lemlist-campaign
description: Create a multi-channel Lemlist campaign (email plus LinkedIn), add leads from a CSV, write the sequence, and leave it paused for review; or, for teams on another outreach tool, produce the sequence and an import file. Use on "launch in lemlist", "create the campaign", "reach out to these people", "add these leads to lemlist", "write the sequence", or as step 4 of revenue-engine.
---

# Lemlist: launch the campaign

Connection: the `lemlist` MCP server (`https://app.lemlist.com/mcp`). Run `/mcp`, pick lemlist, Authenticate, and choose the team. List its tools before the first call.

Copy and strategy come from the Lemlist skills installed alongside this one (listed in `SKILLS.md`). This skill does the plumbing; it does not compete with them. All copy is in `copy_language` from `team-profile.md`.

Other outreach tool (`outreach` is not `lemlist`): do steps 1 to 3, then write the sequence to `out/campaign.md` and the leads with their variables to `out/outreach-import.csv`, and tell the team how to import it. Skip steps 4 to 7.

Expired sign-in (a 401 or auth error): stop, tell the user to run `/mcp`, choose lemlist, Authenticate, then retry the same step. Save any leads given in chat to `out/` first so nothing is lost.

## Steps

1. Read `out/leads-new.csv` (if any row has a `fit_score`, only rows at or above `min_fit_to_route` from `clay-build-list` go in, and empty scores wait, unless the user says otherwise). If it is missing, fall back to `out/leads.csv` and warn that it has not been checked against HubSpot.
2. Angle. If the user has no angle yet, use the Lemlist skills for it (Campaign Angle Finder, then Copywriting First Touch and Copywriting Follow Up, or the sequence skill that matches the persona's seniority). Feed them `out/icp.md` and three sample rows.
3. Sequence. Default to a short multi-channel sequence, and adjust to what the user asks:
   - Day 0: LinkedIn profile visit
   - Day 1: email 1 (first touch, uses `{{personalization}}`)
   - Day 3: LinkedIn invite, no note
   - Day 5: email 2 (new angle)
   - Day 8: LinkedIn message if connected
   If the user asks for email only, drop the LinkedIn steps. Segments: if the rows carry a `segment` column (or the user names segments, such as persona or industry), write one sequence per segment, using the enriched variables, so the copy really changes by segment; in Lemlist, one campaign per segment, suffixed with the segment name. The CSV must follow the `out/leads.csv` contract (normalise it with `revenue-engine` if not). Map columns to Lemlist's lead fields: `email` to email, `first_name` to firstName, `last_name` to lastName, `company_name` to companyName, `linkedin_url` to linkedinUrl, `job_title`, `company_domain`, `personalization`, the `fit_` columns and every other enrichment column as custom variables in camelCase (`latest_news` to `{{latestNews}}`, `current_challenges` to `{{currentChallenges}}`). Show the column-to-variable table once. Rewrite placeholders from the copy skills (`[first name]`, `[company]`) as `{{firstName}}`, `{{companyName}}`. Check that every variable used in the copy exists as a Lemlist column for every lead; for rows with an empty `personalization`, use a fallback opening line written with the copy, and show one such row in the step 7 preview.
   A/B test (optional, on "A/B" or "test subject lines"): take 3 angles from Campaign Angle Finder (pain-led, trigger-led, peer-proof), 2 subject lines each, and load them as A/B variants of email 1. Each variant tests one hypothesis; write it next to the variant in `out/campaign.md`.
4. Create the campaign, named `RE-Hack | <team> | <ICP short name> | <date>`. Leave it paused or draft.
5. Add the leads (show the count first; with `write_mode` A wait for a go). Skip any row whose email is already in another active Lemlist campaign, if the tools let you check. If the campaign is already running, adding leads sends to them: ask for an explicit go.
6. Write `out/campaign.md`: campaign name and id, lead count, sequence with the copy, and the variables used.
7. Ask before starting. Check the campaign's sending settings (sending mailbox, schedule and time zone, daily limit, LinkedIn account linked) and list anything missing. Show the user the first email rendered for two real leads, and start only on an explicit go.

## Discount code

Participants get one free week of Lemlist with the code in `event.md` (`lemlist_trial_code`; if it still shows a placeholder, ask the user for the code from the setup email). If a tool fails because a channel is not on the plan, say so and give the code.
