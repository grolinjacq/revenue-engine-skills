#!/usr/bin/env python3
"""Build the claude.ai skill ZIP (gtm-start) from this workspace.

claude.ai has no workspace folder: one uploaded skill carries everything. This script writes
  dist/gtm-start.zip  = .claude/skills/gtm-start/ plus, under references/:
    event.md          = this workshop's settings (placeholders only, no codes)
    samples/          = the safe-mode data
    skills/<name>.md  = the step skills the flow reads (their SKILL.md bodies)

Upload: claude.ai > Customize > Skills > + > Create skill > Upload a skill (Settings > Capabilities >
"Create and edit files" must be on). Works on every Claude plan.

  python3 scripts/build-claudeai.py
dist/ is not committed: hand the ZIP to attendees from the workshop's access card or chat.
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = "gtm-start"

STEP_SKILLS = [
    "clay-build-list", "crm", "crm-lead-triage", "lemlist-campaign", "close-the-loop",
    "icp-definer", "persona-definer", "pain-identifier", "trigger-finder", "campaign-angle-finder",
    "copywriting-first-touch", "copywriting-follow-up", "linkedin-sequence", "reply-handler",
    "copywriting-refiner", "copywriting-vp-sequence", "copywriting-manager-sequence",
    "copywriting-ic-sequence", "outbound-campaign-architect",
]

HEADER = (
    "<!-- Bundled for claude.ai chat by scripts/build-claudeai.py. In chat: `out/<file>` means a file in "
    "the outputs folder that you give the user; rules are references/chat-rules.md plus the Chat additions "
    "in SKILL.md (they replace mentions of RULES.md, CLAUDE.md and team settings files); event settings are "
    "references/event.md; samples are references/samples/. Workshop overrides in SKILL.md win over this file "
    "(no campaign start, no mailbox step, list size from event.md). Ignore Claude Code commands (/mcp, claude mcp, "
    ".claude/, SKILLS.md); a skill named here but not bundled is done from the SKILL.md flow. -->\n\n"
)

# Anything that looks like a promo code or a promo sign-up link must never ship.
LEAK = re.compile(r"promoCode=|[?&]source=clay|utm_content=|coupon[:=]\s*[A-Z0-9]{6,}", re.I)


def main() -> int:
    src = ROOT / ".claude" / "skills" / SKILL
    stage = ROOT / "dist" / SKILL
    shutil.rmtree(stage, ignore_errors=True)
    shutil.copytree(src, stage)
    ref = stage / "references"
    shutil.copy(ROOT / "event.md", ref / "event.md")
    shutil.copytree(ROOT / "samples", ref / "samples")
    (ref / "skills").mkdir(exist_ok=True)
    for name in STEP_SKILLS:
        body = (ROOT / ".claude" / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        body = re.sub(r"\A---\n.*?\n---\n", lambda m: m.group(0) + "\n" + HEADER, body, count=1, flags=re.S)
        (ref / "skills" / f"{name}.md").write_text(body, encoding="utf-8")

    leaks = [str(p.relative_to(stage)) for p in stage.rglob("*") if p.is_file()
             and LEAK.search(p.read_text(encoding="utf-8", errors="ignore"))]
    if leaks:
        print("Refusing to build: promo code or promo link found in " + ", ".join(leaks), file=sys.stderr)
        return 1

    zpath = ROOT / "dist" / f"{SKILL}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(stage.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(stage.parent))  # top folder = skill name, as claude.ai expects
    n = sum(1 for p in stage.rglob("*") if p.is_file())
    print(f"Built {zpath.relative_to(ROOT)}: {n} files, {zpath.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
