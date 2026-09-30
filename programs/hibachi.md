# Hibachi

- Page: https://immunefi.com/bug-bounty/hibachi/scope/
- Max bounty: $20,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (2)

- [websites_and_applications] https://api.hibachi.xyz
- [websites_and_applications] https://data-api.hibachi.xyz

## Asset notes

(none)

## Impacts in scope (18)

- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:
- Email address
- Phone number
- Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$20,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [websites_and_applications] Medium: maxReward=$2,500, rewardModel=up_to
- [websites_and_applications] Low: maxReward=$1,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

For critical web/apps bug reports will be rewarded with **USD $40,000**, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

Rewards are subject to adjustment based on the nature of the vulnerability, exploitability, and how practical the attack vector is in a real-world scenario.

__Reward Payment Terms__

Payouts are handled by the Hibachi team directly and are denominated in USD. However, payments are done in USDC on Ethereum

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

The assessment of the extent of any potential indirect economic damage, defined as damage other than that evidenced by a PoC that showcases the direct exploitation of the vulnerability leading to impact, is at the full discretion of the Project. This decision is final and non-negotiable. Rewards are based on severity, impact, and report quality.

## Out of scope (program-specific)

1. Unauthorized Access & Exploited Attacks
- Attacks already exploited by the reporter, causing real-world damage.
- Vulnerabilities requiring access to leaked credentials, API keys, or secrets, unless proven to be actively used in production.
- Exploits requiring privileged access (e.g., governance, strategist roles), except when the contract is explicitly designed to have no privileged access to affected functions.
- Attacks requiring access to internal test files, configuration files, or non-production environments, unless explicitly stated as in-scope.
- Attacks requiring physical access to devices, internal systems, or restricted networks.

2. Third-Party & Environmental Limitations
- Issues in third-party services, infrastructure, or dependencies not owned or managed by Hibachi.
- Bugs related to outdated software versions beyond Hibachi's control (e.g., unsupported browsers).
- Attacks relying on the depegging of external stablecoins unless directly caused by a flaw in Hibachi's code.
- Reflected plain text injection (e.g., URL parameters, paths) without proof of real-world impact.
  - Note: This does not exclude reflected HTML injection (with or without JavaScript) or persistent plain text injection.
- Any vulnerability requiring browser bugs for exploitation (e.g., CSP bypass).
- Server-side non-confidential information disclosure (e.g., IPs, server names, most stack traces).
- SPF/DMARC misconfigured records without security impact.

3. Social Engineering & User Manipulation
- Phishing, social engineering, or coercion of Hibachi employees, partners, or users.
- CSRF vulnerabilities without state-modifying impact (e.g., logout CSRF).
- Automated testing of services generating excessive traffic (e.g., brute force, spam).

4. Automated Attacks & Service Disruptions
- Denial of Service (DoS), brute force, or rate-limiting bypass attacks.
- Captcha bypass using OCR without impact demonstration.
- DDoS-only attacks with no security relevance.
- Enumeration of user existence (e.g., checking if an email is registered).

5. Theoretical & Non-Exploitable Vulnerabilities
- Theoretical vulnerabilities without a working proof-of-concept (PoC).
- Issues requiring in-app user actions that are not part of normal workflows.
- Impacts requiring access to a victim’s local network (e.g., ARP spoofing, MITM).
- Lack of SSL/TLS best practices without proven exploitation.
- Leaked non-sensitive API keys (e.g., Etherscan, Infura, Alchemy).
- Automated scanner reports without impact demonstration.
- Missing HTTP headers or cookie flags (e.g., httponly, X-FRAME-OPTIONS) unless leading to an exploitable vulnerability.
- UX/UI-related bugs that do not materially impact security.
- Non-future-proof NFT rendering vulnerabilities.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
