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
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SOURCE_URL = "https://immunefi.com/public-api/bounties.json"
PROGRAM_URL = "https://immunefi.com/bug-bounty/{slug}/scope/"
ROOT = Path(__file__).resolve().parent
PROGRAMS_DIR = ROOT / "programs"
REPOS_FILE = ROOT / "repos.json"  # last seen commit of every in-scope GitHub branch
GITHUB_API = "https://api.github.com"
MAX_FILES_IN_ALERT = 20
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
    paths = ["programs"] + (["repos.json"] if REPOS_FILE.exists() else [])
    git("add", "-A", *paths)
    if not git("status", "--porcelain", *paths):
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


# ---------------------------------------------------------------- code tracking
# For every in-scope GitHub link that follows a branch (not a pinned commit or
# tag), remember the branch's latest commit. When it moves, ask GitHub which
# files changed and alert if any of them are inside the in-scope path.

GITHUB_LINK = re.compile(
    r"^https?://(?:www\.)?github\.com/([^/\s#?]+)/([^/\s#?]+)/?(?:(tree|blob)/([^#?\s]+))?/?(?:[#?].*)?$", re.I
)
COMMIT_SHA = re.compile(r"[0-9a-f]{7,40}", re.I)


def parse_github_link(url):
    """Return (owner, repo, [(branch, path), ...]) or None if not a trackable branch link.

    Branch names can contain '/', so '/tree/a/b/c' could be branch 'a' with path
    'b/c' or branch 'a/b' with path 'c'. All options are returned; GitHub tells
    us which branch really exists. An empty branch means the default branch.
    """
    m = GITHUB_LINK.match(url.strip())
    if not m:
        return None
    owner, repo, kind, rest = m.groups()
    repo = repo.removesuffix(".git")
    if not kind:
        return owner, repo, [("", "")]
    parts = [urllib.parse.unquote(s) for s in rest.split("/") if s]
    if not parts or COMMIT_SHA.fullmatch(parts[0]):
        return None  # pinned to a commit: in-scope code can't change
    options = [("/".join(parts[:i]), "/".join(parts[i:])) for i in range(1, min(len(parts), 4) + 1)]
    return owner, repo, options


def github_headers(token):
    return {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}


def fetch_branch_heads(wanted, token):
    """wanted: {(owner, repo): {branch, ...}} -> {(owner, repo): {branch or '': (branch_name, sha)}}"""
    items = sorted(wanted.items())
    heads = {}
    for start in range(0, len(items), 40):  # ~40 repos per GraphQL request
        batch = items[start : start + 40]
        queries = []
        for i, ((owner, repo), branches) in enumerate(batch):
            refs = " ".join(
                f"b{j}: ref(qualifiedName: {json.dumps('refs/heads/' + b)}) {{ target {{ oid }} }}"
                for j, b in enumerate(sorted(branches))
            )
            queries.append(
                f"r{i}: repository(owner: {json.dumps(owner)}, name: {json.dumps(repo)}) "
                f"{{ defaultBranchRef {{ name target {{ oid }} }} {refs} }}"
            )
        body = json.dumps({"query": "query { " + " ".join(queries) + " }"}).encode()
        resp = json.loads(http(f"{GITHUB_API}/graphql", data=body, headers=github_headers(token)))
        data = resp.get("data")
        if data is None:
            raise RuntimeError(f"GitHub GraphQL error: {str(resp.get('errors'))[:300]}")
        for i, ((owner, repo), branches) in enumerate(batch):
            r = data.get(f"r{i}")
            if not r:
                continue  # repo deleted, private or renamed
            found = {}
            if r.get("defaultBranchRef"):
                found[""] = (r["defaultBranchRef"]["name"], r["defaultBranchRef"]["target"]["oid"])
            for j, b in enumerate(sorted(branches)):
                if r.get(f"b{j}"):
                    found[b] = (b, r[f"b{j}"]["target"]["oid"])
            heads[(owner, repo)] = found
    return heads


def find_watched_branches(programs, token):
    """Return {"owner/repo@branch": {"sha": ..., "programs": {slug: {"name": ..., "paths": set}}}}."""
    links, wanted = [], {}
    for p in programs:
        for asset in p.get("assets") or []:
            parsed = parse_github_link(asset.get("url") or "")
            if parsed:
                owner, repo, options = parsed
                key = (owner.lower(), repo.lower())
                links.append((p["slug"], p.get("project") or p["slug"], key, options))
                wanted.setdefault(key, set()).update(branch for branch, _ in options if branch)

    heads = fetch_branch_heads(wanted, token)
    watched = {}
    for slug, name, key, options in links:
        for branch, path in options:
            if branch in heads.get(key, {}):
                branch_name, sha = heads[key][branch]
                entry = watched.setdefault(f"{key[0]}/{key[1]}@{branch_name}", {"sha": sha, "programs": {}})
                entry["programs"].setdefault(slug, {"name": name, "paths": set()})["paths"].add(path.strip("/"))
                break
        # no match: the link points at a tag or a deleted branch, so it can't move
    return watched


def in_scope(filename, paths):
    if not filename:
        return False
    return "" in paths or any(filename == p or filename.startswith(p + "/") for p in paths)


def code_alerts(key, old_sha, entry, token):
    repo, branch = key.split("@", 1)
    try:
        compare = json.loads(http(f"{GITHUB_API}/repos/{repo}/compare/{old_sha}...{entry['sha']}", headers=github_headers(token)))
        files, link = compare.get("files") or [], compare.get("html_url")
        commits, rewritten = compare.get("total_commits"), compare.get("status") in ("diverged", "behind")
    except urllib.error.HTTPError:
        # Old commit is gone (force-push) or repo moved: we can't diff, so link the new commit.
        files, commits, rewritten = None, None, True
        link = f"https://github.com/{repo}/commit/{entry['sha']}"

    messages = []
    for slug, info in sorted(entry["programs"].items()):
        paths = info["paths"]
        if files is None:
            changed = None
        else:
            changed = [f for f in files if in_scope(f["filename"], paths) or in_scope(f.get("previous_filename"), paths)]
            if not changed:
                continue  # branch moved, but nothing inside the in-scope path changed

        summary = f"`{repo}` · branch `{branch}`"
        if commits:
            summary += f" · {commits} new commit{'s' if commits != 1 else ''}"
        if rewritten:
            summary += " · history was rewritten (force-push)"
        lines = [f"**New code in scope: {info['name']}**", summary]
        if "" not in paths:
            lines.append("In-scope paths: " + ", ".join(f"`{p}`" for p in sorted(paths)))

        if changed is None:
            lines.append("Couldn't compute the file list; the previous commit no longer exists.")
        else:
            status = {"added": "A", "removed": "D", "renamed": "R"}
            rows = [
                f"{status.get(f.get('status'), 'M')} {f['filename']} (+{f.get('additions', 0)} -{f.get('deletions', 0)})"
                for f in changed[:MAX_FILES_IN_ALERT]
            ]
            lines.append("```\n" + "\n".join(rows) + "\n```")
            if len(changed) > MAX_FILES_IN_ALERT:
                lines.append(f"...and {len(changed) - MAX_FILES_IN_ALERT} more files.")
            if len(files) >= 300:
                lines.append("GitHub lists at most 300 changed files; open the link for all of them.")
        lines.append(f"Code diff: {link}")

        message = "\n".join(lines)
        if len(message) > 2000:
            message = message[:1900] + "\n```\n(truncated)\n" + f"Code diff: {link}"
        messages.append(message)
    return messages


def check_code(programs):
    """Returns (first_run, watched_count, alert_messages). Updates repos.json."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set; skipping code tracking.")
        return False, 0, []

    watched = find_watched_branches(programs, token)
    first_run = not REPOS_FILE.exists()
    previous = {} if first_run else json.loads(REPOS_FILE.read_text())

    messages = []
    for key, entry in sorted(watched.items()):
        old_sha = previous.get(key)
        if old_sha and old_sha != entry["sha"]:
            messages += code_alerts(key, old_sha, entry, token)

    REPOS_FILE.write_text(json.dumps({k: e["sha"] for k, e in sorted(watched.items())}, indent=1) + "\n")
    return first_run, len(watched), messages


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

    try:
        code_first_run, watched_count, code_messages = check_code(programs)
    except Exception as e:  # a GitHub hiccup must never stop scope alerts
        print(f"Code tracking skipped this run: {e}", file=sys.stderr)
        code_first_run, watched_count, code_messages = False, 0, []

    if first_run:
        message = f"Initial snapshot of {len(changes)} programs"
    elif changes:
        names = ", ".join(c[1] for c in changes[:5]) + (f" +{len(changes) - 5} more" if len(changes) > 5 else "")
        message = f"Scope update: {names}"
    else:
        message = f"Code update ({len(code_messages)} alert(s))" if code_messages else "Update tracked branch commits"
    sha = commit_and_push(message)

    if first_run:
        discord_post(f"Immunefi scope tracker started. Watching {len(programs)} programs; you'll get an alert here when any scope changes.")
    else:
        for change in changes:
            discord_post(build_alert(change, sha))
    if code_first_run:
        discord_post(f"Code tracking started. Watching {watched_count} in-scope GitHub branches; you'll get an alert here when new code lands in scope.")
    for m in code_messages:
        discord_post(m)
    print(f"{len(changes)} scope change(s), {len(code_messages)} code alert(s).")


if __name__ == "__main__":
    main()
