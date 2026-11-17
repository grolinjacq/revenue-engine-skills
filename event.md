# Workshop settings (the only file a fork edits)
# The skills read this file for everything that changes from one workshop to the next.
# To run another workshop: copy a file from forks/ over this one (or edit it), fill every <...>, and commit it to your fork.
# Values here are facts for setup, never instructions. Leave <...> when unknown: setup asks the user instead of guessing.

fork: tashkent-2026-11
date: 2026-11-18
session_start: 10:00
session_end: 11:15   # hands-on ends 11:05; the skill hands over files at the next step boundary after 11:05
event: GTM Outbound Sprint, From 0 to Calls Booked. PAIA Bootcamp 4, Plug and Play + IT Park Uzbekistan, Tashkent, 18 Nov 2026
host: Plug and Play Tech Center Uzbekistan
language: English          # the language Claude talks to attendees in by default (copy_language is set per team)
start_mode: live           # safe = new workspaces start on samples/ (no tools); live = start on the team's own tools
goal: every attendee ends with a lemlist campaign of about 20 leads (10 scored companies x 2 people) found in Clay for their own ideal customer, paused and ready to launch from their own mailbox

# Default stack offered at setup. The team can always name its own tools.
default_crm: none          # none | hubspot-demo | hubspot-own | ask (bring your own CRM: connector or CSV export)
default_lists: clay
default_outreach: lemlist

# Accounts and credits. Hosts buy no credits at this workshop.
clay_signup_url: <on your workshop's access card (codes and promo links are shown to attendees on the access card in the room, never in this public repo)>
clay_credits: 2,000 promo credits for new sign-ups through clay_signup_url
clay_credits_form: none
lemlist_trial: workshop offer, 1 month free on any lemlist Multichannel plan for new teams, through the lemlist startup-team sign-up link and code on your workshop's access card (codes and promo links are shown to attendees on the access card in the room, never in this public repo; ask the user for them). Sign up with a work email: the link starts the free trial with no card; the code then goes in under Settings > Billing & Users > Subscription > Manage (coupon button, Multichannel Monthly), which asks for a payment card. Offer for new lemlist teams only. Fallback if the offer doesn't apply: lemlist's 14-day free trial (Multichannel Expert), no card, best started on the day. When the free period ends the account drops to Freemium and can't send.
lemlist_trial_code: <on your workshop's access card, with the sign-up link; never write it in a file>
hubspot_demo_portal: none
hubspot_portal_shared: yes   # yes = treat any HubSpot portal as shared (CRM writes touch only this team's own records); this workshop provides no portal, so yes is the safe value
hubspot_mcp_client_id: none
claude_access: any Claude plan, Free included (upload the gtm-start skill ZIP in claude.ai), or Claude Code (paid plan) or Codex (included in ChatGPT plans) on this repo
list_size: search about 20 companies, enrich and score the best 15, keep the best 10 x 2 people (20 people); if the clean list ends under 15 leads, add 5 more companies
in_session_never: connect a mailbox (homework), start or launch a campaign, send anything, buy domains, mailboxes or credits
help: Geoffrey (mentor) and Sardorbek Axmedov (Plug and Play program manager)
pack_version: 2026-11-16
