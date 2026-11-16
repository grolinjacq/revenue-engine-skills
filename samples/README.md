# Safe-mode sample data (all fictional)

This folder holds the synthetic data that safe mode runs on (see "Safe mode" in `revenue-engine`). Every person, company and number is made up: emails end in `.example` (a domain that can never receive mail) and LinkedIn URLs point to `linkedin.example`.

| File | Stands in for | Used by |
|---|---|---|
| `company.md` | The team's own company (`team-context.md`) | every copy step |
| `icp.md` | `out/icp.md`, the target | step 1 |
| `leads.csv` | What Clay returns: 31 people, enriched and scored (`out/leads.csv` contract plus `fit_*` and `segment`) | step 2 |
| `crm-contacts.csv` | A contacts export from any CRM | step 3 (dedupe) |
| `crm-won-deals.csv` | A closed-won deals export from any CRM | step 1 from a CRM |
| `suppress.csv` | `out/suppress.csv` (opt-outs) | step 4 |
| `replies.csv` | Campaign replies and statuses, email and LinkedIn | step 5 |
| `inbound.csv` | Inbound form fills | inbound routing |
| `first-campaign-leads.csv` | A first campaign in the home market (Uzbekistan, 20 people) | use case: first campaign |
| `expansion-leads.csv` | A new market (Kazakhstan, 22 people) | use case: international expansion |
| `research-accounts.csv` | Accounts to research and qualify | use case: account research |
| `signals.csv` | People with a dated, sourced buying signal | use case: signal-based outreach |
| `investors.csv` | Investors and partner programmes | use case: investor and partner finding |

The use-case files come from the use-case library (its playbooks list what each run should produce). The answer key below is for the core loop on `leads.csv`.

## What a correct safe run produces (the answer key)

Use it to check a run in Claude or Codex, step by step.

Step 2, list (31 rows in):
- 2 dropped, no email and no LinkedIn: Peter Walsh (Walsh Haulage), Andes Mudanzas.
- 1 field flagged and blanked: Mark Evans (BrightGrid Services), `personalization` reads like an instruction.
- 1 LinkedIn-only row kept: Miriam Koch (Koch Logistik), LinkedIn steps only.

Step 3, dedupe against `crm-contacts.csv` and `exclude_domains`:
- 1 excluded as a customer domain: Ana Ruiz (transleon.example).
- 1 already a contact, left out: Lucía Moreno (Norte Flota).
- 1 known company, kept with owner Ana Ruiz: Jordi Puig (Vallès Energia).
- 6 not routed: fit under 4 (Pablo Serrano 2, Carmen López 3, Lucy Turner 3, Katrin Wolf 3, Marta Ruiz 1) and fit empty (Hugo Prieto, "not enough data").

Step 4, campaign:
- 1 suppressed: Daniel Moss (in `suppress.csv`).
- **20 leads** in the campaign file: 8 Spain (`spain`), 6 United Kingdom (`uk`), 6 Germany (`de`); 19 with email, 1 LinkedIn only.

Step 5, close the loop (`replies.csv`):
- Inés García: interested, draft a reply proposing Thursday 10:00, lifecycle forward to SQL.
- Tom Hale: not now, note "try again February", no lifecycle change.
- Jonas Becker: wrong person, note; adding Stefan Braun waits for a go.
- Elena Vidal: unsubscribed, goes to the suppress file at once.
- Olivia Price: out of office until 20 November, note, no draft.
- Lena Schmidt: bounced, goes to the suppress file at once.
- Miriam Koch (LinkedIn): pricing question, matched by `linkedin_url`, draft a reply.
