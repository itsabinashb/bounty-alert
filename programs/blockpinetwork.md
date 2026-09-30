# BlockPI Network

- Page: https://immunefi.com/bug-bounty/blockpinetwork/scope/
- Max bounty: $5,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - low, websites_and_applications - medium, websites_and_applications - high
- End date: (none)

## Assets in scope (2)

- [websites_and_applications] https://blockpi.io/ — Main Web App
- [websites_and_applications] https://dashboard.blockpi.io/ — Dashboard

## Asset notes

(none)

## Impacts in scope (16)

- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notification
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction such as iframing leading to modifying the backend/browser state (demonstrate impact with PoC)
- [websites_and_applications] Low: Redirecting users to malicious websites (Open Redirect)
- [websites_and_applications] Low: Taking over broken or expired outgoing links such as social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as locking up the victim from login, cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$5,000, minReward=$2,500, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$1,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,200, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope and a suggestion for a fix in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If an impact can be caused to any other asset managed by BlockPI that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. This only applies to Critical and High impacts.

Payouts are handled by the __BlockPI__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
