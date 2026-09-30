# Immunefi scope tracker

Checks every Immunefi bug bounty program every 15 minutes. When a scope changes,
it saves the new version in `programs/` (as a git commit) and posts an alert to Discord
with the changed lines and a link to the full diff on GitHub.

It also watches the GitHub repos that programs list as in scope. When new commits
change files inside an in-scope folder, it posts a "New code in scope" alert with the
changed files and a link to GitHub's compare page. Links pinned to a commit or tag are
skipped, since that code can't change. The latest seen commit per branch is kept in `repos.json`.

## Setup

1. Create a Discord webhook: channel settings → Integrations → Webhooks → New Webhook → Copy Webhook URL.
2. Create a GitHub repo and push this folder to it.
3. In the repo: Settings → Secrets and variables → Actions → New repository secret,
   name `DISCORD_WEBHOOK_URL`, value = the webhook URL.
4. Actions tab → "Track Immunefi scopes" → Run workflow.

The first run saves a starting snapshot and posts one "tracker started" message.
From then on you get one Discord message per changed program.

## Run locally

    DISCORD_WEBHOOK_URL=... GITHUB_TOKEN=... python3 track.py

Without `DISCORD_WEBHOOK_URL` set, alerts are printed instead of sent.
Without `GITHUB_TOKEN` set, repo code tracking is skipped. On GitHub Actions the token is provided automatically.


# bounty-alert
