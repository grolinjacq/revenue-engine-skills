# Running this pack for another workshop (forking)

The pack has two layers:

- **Engine** (same everywhere): `RULES.md`, the skills in `.claude/skills/` (mirrored to `.agents/skills/` for Codex), `samples/`, `.mcp.json`, `.codex/config.toml`, `.claude/settings.json`. Change these only to improve the product for every workshop, then rerun `python3 scripts/build-codex.py`.
- **Workshop settings** (one file): `event.md`. Host, date, language, goal, `start_mode`, default stack, sign-up links, trials and codes, who helps. Nothing else in the pack names a workshop.

## Make a fork

1. Copy the closest file in `forks/` (today `tashkent.md`) to `forks/<place>-<yyyy-mm>.md` and edit it. Leave a value as `<...>` when you don't know it yet: setup asks the attendee instead of guessing. Codes and promo links never go in this public repo: they are shown to attendees on the access card, so put them there and point the field to it.
2. Copy it over `event.md`.
3. Run `python3 scripts/build-codex.py --check` (it should say up to date).
4. Run safe mode once in Claude Code and once in Codex, and compare with `samples/README.md`.
5. Tag the commit (`git tag fork-<place>-<yyyy-mm>`) and share the ZIP of that tag.

## What usually changes per workshop

| Setting | Example |
|---|---|
| `start_mode` | `safe` for beginners (no accounts on arrival), `live` when attendees set up tools beforehand |
| `default_crm` | `none` (bring your own), `hubspot-demo` when a partner gives portals |
| `clay_signup_url`, `clay_credits` | the partner's promo link |
| `date`, `session_start`, `session_end` | the workshop day and hours, local time (on that day the skill reads the time to hand over files before the end; the demo runs only when asked) |
| `lemlist_trial`, `lemlist_trial_code` | trial rules or a partner code |
| `language` | the language the assistant talks to attendees in |

Decks, briefs and use-case pages are tailored per workshop and live outside this repo.

## Publish the claude.ai ZIP

After `event.md` is set for the fork and merged to main: Actions > "Release claude.ai ZIP" > Run workflow, tag `<fork>` (for example `tashkent-2026-11`). The attendee link is `https://github.com/<owner>/<repo>/releases/download/<fork>/gtm-start.zip`. Promo codes stay on the access card: the build refuses to package one.
