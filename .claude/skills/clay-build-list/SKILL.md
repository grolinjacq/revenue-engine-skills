---
name: clay-build-list
description: "Turn an ICP into an enriched, scored lead list with Clay - find companies, find the right people at them, enrich with work email and LinkedIn, score fit 1 to 5 with a reason and a source, export a CSV. Use on 'build a list', 'find me 20 companies like', 'find the VP Sales at', 'get the rest of the people at', 'get me their emails', 'enrich these leads', 'score these accounts', 'who's hiring salespeople', 'ICP workflow in Clay', or as step 2 of revenue-engine. Not for a CSV from Apollo or another tool: revenue-engine normalises those."
---

# Clay: build the list

Clay sits in the middle: it turns the ICP from the CRM (or the website) into people Lemlist can reach.

Connection: Clay's official plugin (`clay@clay-plugins`, from github.com/clay-run/agent-plugins). It is enabled in `.claude/settings.json`, so Claude Code offers to install it when you trust this folder. It works through the `clay` CLI: if `clay whoami` fails, run Clay's `setup` skill first. Fallback: the Clay connector in your Claude account settings (no CLI; use the connector's company search, contact search and data-point tools for the same steps). If neither is connected, say "Connect Clay first" and offer the CSV route in `revenue-engine`. Never fill the list with another list or enrichment connector (Apollo, Lusha, ZoomInfo, a HeyReach list...) because it is connected: that needs the user's own request naming the tool (Tool identity in `RULES.md`). A personal skill with this name from another plugin (one that exports to HeyReach, for example) is not this one.

Clay's plugin brings its own skills. This skill chains them for the loop and fixes the hand-off format; let them do the Clay-specific work:
- `searches`: find companies and people in Clay's database (steps 2 and 3).
- `routines`: run a saved Clay function, for example a work-email finder or a Claygent scoring prompt (steps 4 and 5).
- `credits-quotas-plans`: check the credit balance before enriching (step 4).
- `signals`: trigger-based filters (Advanced).
- `clay`: Clay's own table of contents, if a team wants to go further.

Safe mode (`mode: safe` in `team-profile.md`, or the request says so): don't call Clay and spend nothing. Follow `revenue-engine`, "Safe mode", step 2: `samples/leads.csv` stands in for Clay's results, and steps 6 to 8 below run on it into `out/safe/leads.csv`.

## Our defaults (edit these)

Teams tune this block once, by hand or with `make-it-ours`; the steps below read it. A number the user says in the request ("thirty companies", "three people each") wins over the block for that run.

```
companies: 25            # 20 to 50 in a workshop session; credits are limited
people_per_company: 2    # most senior ICP title first
titles_local: true       # add the market's-language titles (for a Spanish-speaking market: "Director Comercial", "Director Financiero")
data_points: work_email, linkedin_url   # add more only if a later step uses them
score: true              # step 5; false skips scoring
min_fit_to_route: 4      # rows below this stay in out/leads.csv but are flagged, not routed
saved_functions: []      # names of the team's own Clay functions to prefer, e.g. ["ICP score", "Waterfall email"]
```

## Steps

1. Read `out/icp.md`. If it is missing and `team-profile.md` has a `website`, propose the ICP from the site and let the team confirm or retarget it (`hackathon-setup` steps 1b and 1c); with `website: none`, use `about` if set, else ask for industries, size band, countries and titles; with no profile at all, ask for the team's website first. Write the file in the `crm` Job A format first. With `titles_local`, add titles in the market's language (for Spain or Mexico: "Director Financiero", "Dueño", "Propietario").
2. Companies. Search with industries, employee band and countries. Exclude every domain in `exclude_domains`. Aim for `companies`. Show the user the first 10 and ask if the list looks right before going further.
3. People. For each company, search contacts by the ICP titles. Keep at most `people_per_company`, the most senior match first.
   After each search or table Clay creates, give the user the link Clay's result returns for it (table, search or workbook), and write it in `out/run-log.md`; never build or guess a Clay URL; with none, name the table.
4. Enrich. Add the `data_points`. On the Clay connector, the work email is the standard type `Email` (`add-contact-data-points` with `dataPoints: [{"type": "Email"}]`; its only standard types are `Email`, `Summarize Work History` and `Find Thought Leadership`, never names like `work_email`); the LinkedIn URL comes with the people search result and needs no data point. Read the results with `get-task-context`. If a name in `saved_functions` does this job, run it with `routines` instead. Each data point costs credits: check the balance, then say records x data points and the credits, priced from Clay (its credits skill or a tool's quote); with no price source, say the cost is unknown and wait for a go (`RULES.md`). Wait for a go when `write_mode` is A, today's running total in `out/run-log.md` plus this estimate is above `clay_credit_cap`, or the balance is short (on the connector path with no balance tool, say so and wait for a go); when short, offer the cheaper plan (email only, or fewer companies) and run only what the user picks.
5. Score (when `score` is true, or the user asks). Give each company a fit score from 1 to 5 against `out/icp.md`, with a one-line reason and the source it rests on (a URL or the Clay field). Prefer a saved Claygent or scoring function from `saved_functions`. Otherwise, when `out/icp.md` has `fit_checks` (yes/no questions built from the ICP's must-haves), answer them first, with a source per answer: Claude reads each company's site (home page plus one relevant page) with web search or fetch, never from memory; for the sites it can't read, Clay research: on the Clay connector, `add-company-data-points` with one `Custom` data point per check on the companies to score, answers read with `get-task-context`; with the CLI or plugin, the equivalent Claygent column. Score on the firmographics plus the check answers (a "no" drops the company, "unknown" never counts as a yes, each answer keeps its source). Without checks, score from the data Clay already returned, and say which. Never score from a guess: no evidence means `fit_score` empty and the reason "not enough data". Include any scoring credits in step 4's estimate.
6. Qualify. Drop rows with no email and no LinkedIn. Flag catch-all or risky emails if Clay returns a status. Flag rows under `min_fit_to_route`, and rows scored "not enough data" (empty `fit_score` while `score` is on): both stay in the file but are not routed, the same as a low score. When scoring was skipped, every row routes.
7. Export `out/leads.csv` with these columns, in this order, so the next steps can read it:

```
email,first_name,last_name,job_title,company_name,company_domain,linkedin_url,country,employees,industry,personalization,fit_score,fit_reason,fit_source
```

The first eleven columns are the contract every step reads; the three `fit_` columns are extra (empty when scoring was skipped), and later steps ignore what they don't use. When the team asks for copy at scale, also add the enrichment columns they name, after the `fit_` columns, in snake_case: for example `segment`, `latest_news`, `current_challenges`, `customer_list`. Count them in step 4's credit estimate; `lemlist-campaign` turns them into variables and writes one sequence per `segment`. Each value comes from Clay with its source, or stays empty. `personalization` is one short sentence, grounded in something Clay returned (a hire, a funding round, a product launch). Leave it empty rather than invent one.

8. Report: companies found, people found, enriched, scored (count per score), dropped and why, and credits spent. Say how many rows reach `min_fit_to_route`: those are the ones `crm` (Job B, dedupe) and `lemlist-campaign` should take next. If you found fewer than asked (common for SMB, local or owner-operated markets), say so and suggest a wider filter or another source; never pad the list.

## Advanced (for teams that want more)

- Workspace functions: list the team's saved Clay functions (`routines`) and offer to add the useful ones to `saved_functions`, so every later run uses them without being asked.
- Signals: filter companies on a trigger (hiring for sales roles, recent funding) and put the trigger in `personalization`.
- Lookalikes: take the top 5 customers from the CRM and find similar companies, instead of filtering by firmographics.
- The rest of the buying committee: given one account, find the next 2 or 3 people by title and add them to the same file.
