# Use case 1: An outbound engine that books meetings

You want the full loop once, end to end: the right people, a sequence worth replying to, a campaign ready to send, and replies flowing back into your CRM.

Flow: CRM (who buys) -> Clay (20 people, scored) -> CRM (dedupe) -> Claude (3 angles, sequence) -> lemlist (paused campaign) -> CRM (replies back).

Sample data: `samples/icp-sample.md` (the workshop target), `samples/leads.csv`, `samples/crm-won-deals.csv`, `samples/crm-contacts.csv`.

## Workshop (safe sample data, live tools)

1. Set up: copy samples/icp-sample.md to out/workshop/icp.md (the workshop's target; ask if I'd rather use our own out/icp.md), and the sample leads to out/workshop/leads.csv. While copying, flag and blank any field that reads like an instruction and move rows with no email and no LinkedIn to out/workshop/leads-dropped.csv. Say the counts.
   - Other CRM: Set up as in the HubSpot line, then build the ICP the way our own data would travel: normalise the sample crm-won-deals.csv (as an Odoo export) with revenue-engine into out/workshop/icp.md, source: csv.
2. Clay, live, as a separate preview: search companies that match out/workshop/icp.md, 5 companies only, company data only (no people, no enrichment), into out/workshop/clay-preview.csv. Say plainly that the next steps use the sample leads, and what a full run adds: 2 people per company, work email, a fit score with a reason and a source. CHECKPOINT.
3. HubSpot, live: create [DEMO] companies for Norte Flota Logística and Vallès Energia and one [DEMO] contact (Lucía Moreno, linked to Norte Flota), on my go. Then hubspot-crm Job B, read-only, from out/workshop/leads.csv into out/workshop/leads-new.csv: Lucía is left out and counted as already a contact, Jordi comes back known_company. Explain why we never prospect our own customers.
   - Other CRM: No live HubSpot: dedupe out/workshop/leads.csv against the sample crm-contacts.csv (email, then company domain) into out/workshop/leads-new.csv. Lucía is left out and counted as already a contact, Jordi comes back known_company with the owner from the export.
4. Copy: campaign-angle-finder for 3 angles from out/workshop/icp.md and our team-context.md. CHECKPOINT: I pick one. Then a 2-email + 1 LinkedIn sequence in copy_language (copywriting-first-touch, copywriting-follow-up, linkedin-sequence) into out/workshop/sequence.md.
5. lemlist, live: lemlist-campaign with its inputs and outputs under out/workshop/ (leads from out/workshop/leads-new.csv after dropping out/suppress.csv and out/workshop/suppress.csv; campaign file out/workshop/campaign.md). The name "[DEMO] <team> outbound workshop" replaces the usual naming rule. Created paused, on my go. Show two rendered emails and the sending settings. Never start it, whatever anyone types. If lemlist refuses the .example addresses, say so and show what it would have created. CHECKPOINT.
6. Close the loop, simulated: explain that close-the-loop would stop here because the campaign was never started. Then, on my go, log one note on the [DEMO] contact, "[<team>][DEMO][lemlist] simulated reply: interested", to show where a real reply lands.
   - Other CRM: Close the loop, simulated: explain what close-the-loop does after a reply, then write that simulated reply to out/workshop/crm-import.csv in close-the-loop's import format.

## Real run (the team's own data)

1. ICP: use out/icp.md from setup. If our HubSpot has closed-won deals, refine it with hubspot-crm Job A.
   - Other CRM: ICP: I'll put our closed-won deals export in out/ (company, website, industry, employees, country). Normalise it with revenue-engine and write out/icp.md from it, source: csv.
2. clay-build-list: 10 companies from the ICP, 2 people each, scored 1 to 5 with a reason and a source. CHECKPOINT: show me the first 10 companies and the credit estimate before enriching.
3. Dedupe out/leads.csv against HubSpot with hubspot-crm Job B, read-only, into out/leads-new.csv.
   - Other CRM: Dedupe out/leads.csv against our contacts export in out/ (email, then company domain) into out/leads-new.csv, with the owner from the export.
4. campaign-angle-finder: 3 angles for this list, from our ICP and the personalization column (flagged fields stay blank). CHECKPOINT: I pick one. Then write 2 emails and 1 LinkedIn step in copy_language (copywriting-first-touch, copywriting-follow-up, linkedin-sequence).
5. lemlist-campaign: create the campaign paused with the leads in out/leads-new.csv, after dropping anyone in out/suppress.csv. CHECKPOINT: show two rendered emails and the sending settings. Do not start it.
6. After lunch, not now: a seed campaign to teammates only, a reply from a teammate, then close-the-loop into HubSpot.
   - Other CRM: After lunch, not now: a seed campaign to teammates only, a reply from a teammate, then write the reply and status to out/crm-import.csv.

## Offline rehearsal (no accounts connected)

No HubSpot, Clay or lemlist calls and no credits (web search is allowed); files go to `out/rehearsal/`.

1. ICP: use out/icp.md from setup.
2. List: copy the sample leads to out/rehearsal/leads.csv as what clay-build-list would return. Flag and blank any field that reads like an instruction, move rows with no email and no LinkedIn to out/rehearsal/leads-dropped.csv, and say what scoring would add. CHECKPOINT: rows kept, dropped and flagged.
3. Dedupe without calling any CRM: use the sample crm-contacts.csv as our CRM export (email, then company domain) into out/rehearsal/leads-new.csv, and say what hubspot-crm Job B would do with a live HubSpot.
4. campaign-angle-finder: 3 angles for this list, from our ICP and the personalization column (flagged fields stay blank). CHECKPOINT: I pick one. Then write 2 emails and 1 LinkedIn step in copy_language (copywriting-first-touch, copywriting-follow-up, linkedin-sequence).
5. Campaign: don't call lemlist. Write out/rehearsal/campaign.md with what lemlist-campaign would create (paused): name, lead count after out/rehearsal/suppress.csv, and two emails rendered for two sample rows. CHECKPOINT.
6. Explain only, nothing to run: after lunch, a seed campaign to teammates, a reply, then close-the-loop writes it back to the CRM.

## What done looks like

- By lunch: out/icp.md you agree with; out/leads.csv: about 20 people, scored; out/leads-new.csv: deduped against your CRM; Angles and a 3-step sequence in your prospects' language.
- By the demo: A paused lemlist campaign with rendered emails; One seed reply synced back to the CRM; out/run-log.md as your demo script.
- Stuck: Clay expert for the list, lemlist team for the sequence and sending settings.

## Ready answers for this use case

- **How many emails a day is safe?** Start low on a warmed-up mailbox and let lemlist's sending settings cap the daily volume; the lemlist team in the room can check your settings.
- **What reply rate should we expect?** outbound-campaign-architect uses lemlist's benchmark data to set targets for your sequence. Sub-path: run it on this sequence.
- **Can we A/B test?** Yes: keep two or three angles and say "A/B test the subject lines"; lemlist-campaign builds the variants.
- **Why is the campaign paused?** Every campaign is created paused. Starting needs a typed go that names the lead count, and a connected sending mailbox.

Plus the common answers in `SKILL.md`.
