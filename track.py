#!/usr/bin/env python3
"""Track Immunefi bug bounty scopes, commit changes, and alert Discord.

Each run:
  1. Downloads all programs from Immunefi's public JSON.
  2. Writes one readable text file per program into programs/.
  3. If any file changed: git commit + push, then post a Discord alert
     per changed program with a link to the exact diff on GitHub.

Only the Python standard library is used.
"""

import difflib
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SOURCE_URL = "https://immunefi.com/public-api/bounties.json"
PROGRAM_URL = "https://immunefi.com/bug-bounty/{slug}/scope/"
PROGRAMS_DIR = Path(__file__).resolve().parent / "programs"
MIN_EXPECTED_PROGRAMS = 50  # below this, assume a bad fetch and change nothing
USER_AGENT = "Mozilla/5.0 (compatible; immunefi-scope-tracker)"
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "none": 4}
MAX_DIFF_LINES_IN_ALERT = 15


# ---------------------------------------------------------------- fetching

def http(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def fetch_programs():
    last_error = None
    for attempt in range(3):
        try:
            programs = json.loads(http(SOURCE_URL))
            if isinstance(programs, list) and len(programs) >= MIN_EXPECTED_PROGRAMS:
                return programs
            last_error = f"unexpected response ({len(programs) if isinstance(programs, list) else type(programs).__name__})"
        except (urllib.error.URLError, ValueError, TimeoutError) as e:
            last_error = e
        time.sleep(10 * (attempt + 1))
    sys.exit(f"Fetch failed, nothing changed: {last_error}")


# ---------------------------------------------------------------- rendering
# Only scope-relevant fields are written. Volatile fields (timestamps, ids,
# logos, leaderboards) are left out so they never trigger an alert.

def text(value):
    if not value:
        return ""
    if isinstance(value, list):
        value = "\n".join(str(v) for v in value)
    return str(value).replace("\r\n", "\n").strip()


def money(n):
    return f"${n:,.0f}" if isinstance(n, (int, float)) else str(n)


def section(title, body):
    return f"## {title}\n\n{body if body else '(none)'}\n"


def render_program(p):
    slug = p["slug"]
    assets = sorted(
        f"- [{a.get('type')}] {a.get('url')}"
        + (f" — {text(a.get('description'))}" if a.get("description") else "")
        + (" (primacy of impact)" if a.get("isPrimacyOfImpact") else "")
        for a in p.get("assets") or []
    )
    impacts = sorted(
        p.get("impacts") or [],
        key=lambda i: (str(i.get("type")), SEVERITY_ORDER.get(str(i.get("severity")).lower(), 9), str(i.get("title"))),
    )
    impact_lines = [f"- [{i.get('type')}] {str(i.get('severity')).capitalize()}: {text(i.get('title'))}" for i in impacts]

    reward_lines = []
    for r in p.get("rewards") or []:
        details = ", ".join(
            f"{k}={money(v) if k.lower().endswith(('reward', 'payout')) else v}"
            for k, v in sorted(r.items())
            if k not in ("id", "assetType", "severity") and v not in (None, "")
        )
        reward_lines.append(f"- [{r.get('assetType')}] {str(r.get('severity') or r.get('level')).capitalize()}: {details}")
    reward_lines.sort(key=lambda line: (line.split("]")[0], SEVERITY_ORDER.get(line.split("] ")[1].split(":")[0].lower(), 9), line))

    known = sorted(
        f"- {text(k.get('description'))}" + (f" ({k.get('link')})" if k.get("link") else "")
        for k in p.get("knownIssues") or []
    )

    header = "\n".join([
        f"# {p.get('project')}",
        "",
        f"- Page: {PROGRAM_URL.format(slug=slug)}",
        f"- Max bounty: {money(p.get('maxBounty'))}",
        f"- KYC required: {'yes' if p.get('kyc') else 'no'}",
        f"- Paused: {'yes' if p.get('isPaused') else 'no'}",
        f"- Invite only: {'yes' if p.get('inviteOnly') else 'no'}",
        f"- Program type: {', '.join(p.get('programType') or [])}",
        f"- PoC required for: {', '.join(p.get('pocPerTypeAndSeverity') or []) or '(none)'}",
        f"- End date: {p.get('endDate') or '(none)'}",
        "",
    ])
    parts = [
        header,
        section(f"Assets in scope ({len(assets)})", "\n".join(assets)),
        section("Asset notes", text(p.get("assetsBodyV2"))),
        section(f"Impacts in scope ({len(impact_lines)})", "\n".join(impact_lines)),
        section("Impact notes", text(p.get("impactsBody"))),
        section("Rewards", "\n".join(reward_lines)),
        section("Reward notes", text(p.get("rewardsBody"))),
        section("Out of scope (program-specific)", text(p.get("customOutOfScopeInformation"))),
        section("Out of scope and rules", text(p.get("outOfScopeAndRules"))),
        section("Prohibited activities (program-specific)", text(p.get("customProhibitedActivities"))),
        section(f"Known issues ({len(known)})", "\n".join(known)),
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- git

def git(*args):
    return subprocess.run(["git", *args], cwd=PROGRAMS_DIR.parent, check=True, capture_output=True, text=True).stdout.strip()


def commit_and_push(message):
    git("add", "-A", "programs")
    if not git("status", "--porcelain", "programs"):
        return None
    git("commit", "-m", message)
    if git("remote"):
        git("push")
    return git("rev-parse", "HEAD")


def diff_link(sha, path):
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not (repo and sha):
        return None
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    anchor = hashlib.sha256(path.encode()).hexdigest()  # GitHub's per-file anchor
    return f"{server}/{repo}/commit/{sha}#diff-{anchor}"


# ---------------------------------------------------------------- discord

def discord_post(content):
    webhook = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook:
        print(content, "\n")
        return
    body = json.dumps({"content": content[:2000], "allowed_mentions": {"parse": []}}).encode()
    for _ in range(5):
        try:
            http(webhook, data=body, headers={"Content-Type": "application/json"})
            time.sleep(1)  # stay under Discord's webhook rate limit
            return
        except urllib.error.HTTPError as e:
            if e.code != 429:
                print(f"Discord error {e.code}: {e.read()[:300]!r}", file=sys.stderr)
                return
            time.sleep(float(json.loads(e.read() or b"{}").get("retry_after", 2)) + 0.5)


def section_of_each_line(lines):
    """Map each line to the name of the '## ' section it belongs to."""
    current, result = "Program details", []
    for line in lines:
        if line.startswith("## "):
            current = line[3:].split(" (")[0]
        result.append(current)
    return result


def build_alert(change, sha):
    kind, name, slug, old, new = change
    path = f"programs/{slug}.md"
    link = diff_link(sha, path)
    title = {"added": "New program", "removed": "Program removed", "changed": "Scope changed"}[kind]
    lines = [f"**{title}: {name}**", f"<{PROGRAM_URL.format(slug=slug)}>"]

    if kind == "changed":
        old_lines, new_lines = old.splitlines(), new.splitlines()
        old_sections, new_sections = section_of_each_line(old_lines), section_of_each_line(new_lines)
        diff, changed_sections = [], []
        opcodes = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False).get_opcodes()
        for tag, i1, i2, j1, j2 in opcodes:
            if tag == "equal":
                continue
            removed = [l for l in old_lines[i1:i2] if not l.startswith("## ")]
            added = [l for l in new_lines[j1:j2] if not l.startswith("## ")]
            unbullet = lambda l: l[2:] if l.startswith("- ") else l
            diff += ["- " + unbullet(l) for l in removed if l.strip()] + ["+ " + unbullet(l) for l in added if l.strip()]
            for sec in [old_sections[i] for i in range(i1, i2)] + [new_sections[j] for j in range(j1, j2)]:
                if sec not in changed_sections:
                    changed_sections.append(sec)
        if changed_sections:
            lines.append("Changed: " + ", ".join(changed_sections))
        shown = [d if len(d) <= 180 else d[:177] + "..." for d in diff[:MAX_DIFF_LINES_IN_ALERT]]
        lines.append("```diff\n" + "\n".join(shown) + "\n```")
        if len(diff) > MAX_DIFF_LINES_IN_ALERT:
            lines.append(f"...and {len(diff) - MAX_DIFF_LINES_IN_ALERT} more lines.")

    if link:
        lines.append(f"Full diff: {link}")
    message = "\n".join(lines)
    if len(message) > 2000:  # shrink the code block rather than cut the link
        overflow = len(message) - 1990
        block = next(l for l in lines if l.startswith("```diff"))
        lines[lines.index(block)] = block[: max(20, len(block) - overflow - 4)] + "\n```"
        message = "\n".join(lines)
    return message


# ---------------------------------------------------------------- main

def main():
    programs = fetch_programs()
    first_run = not PROGRAMS_DIR.exists() or not any(PROGRAMS_DIR.glob("*.md"))
    PROGRAMS_DIR.mkdir(exist_ok=True)

    changes, seen = [], set()
    for p in programs:
        slug, name = p["slug"], p.get("project") or p["slug"]
        seen.add(slug)
        path = PROGRAMS_DIR / f"{slug}.md"
        new = render_program(p)
        old = path.read_text() if path.exists() else None
        if old != new:
            path.write_text(new)
            changes.append(("added" if old is None else "changed", name, slug, old or "", new))

    for path in PROGRAMS_DIR.glob("*.md"):
        if path.stem not in seen:
            old = path.read_text()
            name = old.splitlines()[0].lstrip("# ") if old else path.stem
            path.unlink()
            changes.append(("removed", name, path.stem, old, ""))

    if not changes:
        print("No scope changes.")
        return

    names = ", ".join(c[1] for c in changes[:5]) + (f" +{len(changes) - 5} more" if len(changes) > 5 else "")
    sha = commit_and_push(f"Initial snapshot of {len(changes)} programs" if first_run else f"Scope update: {names}")

    if first_run:
        discord_post(f"Immunefi scope tracker started. Watching {len(programs)} programs; you'll get an alert here when any scope changes.")
        return
    for change in changes:
        discord_post(build_alert(change, sha))
    print(f"{len(changes)} program(s) changed.")


if __name__ == "__main__":
    main()
