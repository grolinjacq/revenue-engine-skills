---
name: make-it-ours
description: Tune this workspace's skills to the team's own company, product, customers, vocabulary and voice, so one plain spoken sentence (for example dictated with Wispr Flow) triggers the right skills with the right context. Use on "make it ours", "tune the skills", "customise this for us", "teach it our product", "it keeps picking the wrong skill", or after setup when the team wants better results.
---

# Make it ours

Goal: after 5 to 10 minutes, the team can say one sentence out loud ("find twenty CFOs at Spanish fintechs who just raised and get a campaign ready in Spanish") and Claude runs the right chain with their context, no skill names needed.

## 1. Interview (one message, answer by voice or text)

Start from what is already known. Read `team-context.md` (setup writes a draft from the team's website), `out/icp.md` and `team-profile.md`. No draft and a `website` on file: read the site first (`hackathon-setup` step 1b only: the target confirmation and `out/icp.md` stay with setup). No website on file: ask for it as the first question, read it, then continue.

Show what the site gave you as short lines to confirm ("From your site: you sell X to Y; customers A, B, C; proof: 40% faster onboarding. Right?"), then ask only what a website can't answer:

1. Company and product in two lines, and price point. Skip if the site gave it: confirm instead.
2. Your best 3 customers (names or types) and why they bought. Keep the names the site shows; ask only the why.
3. Words your buyers use for the problem, and words you never use. Propose the "use" list from the site; ask for the "never use" list.
4. Tone: formal or casual, "tú" or "usted", emoji yes or no, sign-off name.
5. Proof points you can cite (numbers, logos, case studies). Skip if the site gave them: confirm instead, and ask for any that aren't public.
6. Phrases you'll actually say when you want each thing, for example "get me a list", "draft outreach", "who replied". Say them the way you'd dictate them.

## 2. Write `team-context.md` (workspace root)

Sections: Company, Product and offer, ICP and personas (link `out/icp.md` if it exists), Buyer vocabulary (use / avoid), Voice and tone, Proof points, Our phrases. Keep it under 80 lines. If it holds setup's website draft, complete that file: keep what the team confirmed, add the rest, and drop the `draft` source line. Any other existing `team-context.md`: show the changes and ask before overwriting. Then make sure `CLAUDE.md` imports it: add the line `@team-context.md` under `@team-profile.md` if it isn't there. From the next session it loads automatically; for the rest of this session, read it now and use it.

Never edit `CLAUDE.md`'s working rules, `.claude/settings.json` or `event.md` from this skill: tuning changes context and triggers, not the safety rules.

## 3. Tune the triggers

For each phrase from question 6, find the skill it should start (use `SKILLS.md`), and append the phrase in quotes to that skill's `description:` line in `.claude/skills/<skill>/SKILL.md`. Rules:

- Only edit the `description:` of this pack's own skills (`hackathon-setup`, `make-it-ours`, `revenue-engine`, `hubspot-crm`, `hubspot-account-brief`, `hubspot-lead-triage`, `clay-build-list`, `lemlist-campaign`, `close-the-loop`). For a phrase that belongs to a vendored Lemlist, hubspot-admin or official HubSpot skill (`hubspot`, `hubspot-call-prep` and the other `hubspot-*` skills marked official in `SKILLS.md`), or to a Clay plugin skill (it lives outside this folder), add it to `revenue-engine`'s description with the skill it should lead to.
- Append inside the existing text; never delete trigger phrases. If the line contains `: ` or quotes, keep the whole description wrapped in double quotes and use single quotes inside it. After editing, re-read the frontmatter and check it still has `name:` and one `description:` line, with matching quotes.
- Keep each description under 1,000 characters.
- If one phrase fits two skills, add it to `revenue-engine` instead: it routes.
- Show the list of changes (skill, phrase added) before writing, and apply on a go.

Also offer to fill the "Our defaults (edit these)" block in `clay-build-list` (companies, people per company, local titles, data points, scoring, minimum fit, the team's saved Clay functions) from the interview: show the new block, apply on a go.

## 4. Test it

Ask the team for three real requests, spoken as they would say them. For each, say which skill would run and what it would do first, without running it. If one routes wrong, fix its trigger and test again. Log the three tests to `out/run-log.md`.

## Voice tips to share

- Say the outcome, the number and the constraint in one breath: "twenty, Madrid, Heads of Sales, Spanish copy, don't send".
- "Don't send" and "just draft" are always safe words: nothing goes out without an explicit go anyway.
- Wispr Flow or any dictation works: Claude reads the text, not the audio.
