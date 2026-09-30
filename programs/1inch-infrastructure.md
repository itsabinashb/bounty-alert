# 1inch - Infrastructure

- Page: https://immunefi.com/bug-bounty/1inch-infrastructure/scope/
- Max bounty: $20,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - high, websites_and_applications - critical, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (12)

- [websites_and_applications] https://*.1inch.com — One-level subdomains of 1inch.com only (e.g. app.1inch.com). Deeper subdomains (e.g. a.b.1inch.com) are out of scope.
- [websites_and_applications] https://*.1inch.network — One-level subdomains of 1inch.network only. Deeper subdomains are out of scope.
- [websites_and_applications] https://1inch.com — Homepage
- [websites_and_applications] https://api.1inch.com — API
- [websites_and_applications] https://blog.1inch.com — Blog Page
- [websites_and_applications] https://business.1inch.com — Business Subdomain
- [websites_and_applications] https://business.1inch.com/portal/ — Business Portal
- [websites_and_applications] https://business.1inch.com/portal/documentation/ — Documentation Page
- [websites_and_applications] https://discord.com/invite/1inch — Discord
- [websites_and_applications] https://t.me/OneInchNetworkNews — Telegram
- [websites_and_applications] https://www.reddit.com/r/1inch/ — Subreddit
- [websites_and_applications] https://x.com/1inch — X/Twitter Page

## Asset notes

(none)

## Impacts in scope (12)

- [websites_and_applications] Critical: Container escape leading to access to host system or other tenants
- [websites_and_applications] Critical: Disruption of critical backend services without overloading server with extensive traffic
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Exploiting misconfigured IAM policies to gain unauthorized access to cloud infrastructure (e.g., virtual machines, storage buckets).
- [websites_and_applications] Critical: Gain unauthorized access to critical internal services (e.g. databases, internal portals)
- [websites_and_applications] Critical: Network-level vulnerabilities allowing lateral movement, segmentation bypass, or unauthorized access to internal network segments
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Unauthorized access to internal communication platforms (e.g., internal Slack, email, ticketing systems) leading to disclosure of confidential operational data
- [websites_and_applications] High: Container security misconfigurations allowing privilege escalation within the container environment without full escape
- [websites_and_applications] High: Disclosure of large-scale PII or sensitive information
- [websites_and_applications] Medium: Gain read-only access to internal infrastructure data (logs, configs, metrics)
- [websites_and_applications] Low: Execute arbitrary system commands on non-core services

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [websites_and_applications] Medium: maxReward=$2,500, minReward=$1,000, rewardModel=range
- [websites_and_applications] Low: maxReward=$1,000, minReward=$100, rewardModel=range

## Reward notes

### Rewards by Threat Level

#### Reward Calculation for Critical Level Reports

For critical infrastructure bugs, reports will be rewarded with the maximum critical reward (USD 20,000) only if the impact leads to:

* Full compromise of production infrastructure (e.g., RCE on production servers, full IAM takeover)  
* Disclosure of credentials or secrets that grant attacker-level access to production systems and could lead to direct loss of user funds or critical data

All other impacts that would be classified as Critical would be rewarded a flat amount of 5000\. The rest of the severity levels are paid out according to the Impact in Scope table.  

#### Reward Calculation for High and Medium Level Reports

For High, Medium, and Low level reports, 1inch retains the full right to determine the reward amounts within the range provided due to the lack of objective scaling systems to determine the reward amount. It does not commit to rewarding anything above the base amounts. Rewards going above the base amounts are entirely within the discretion of the 1inch team.

#### Other Restrictions and Limitations

Vulnerabilities reported for blog.1inch.com, business.1inch.com (root subdomain), and assets falling under "Rest related to 1inch" are capped at Medium severity. The maximum reward for these assets is USD 2,500.

For the listed wildcard assets, only direct (one-level) subdomains of 1inch.com and 1inch.network are in scope. These cover any 1inch-controlled subdomain, asset, or service that is not explicitly listed in the Assets in Scope table but is verifiably operated by 1inch (e.g., reachable via DNS records under \*.1inch.com or \*.1inch.network and serving production traffic). Vulnerabilities in such assets are capped at Medium severity. 1inch reserves sole discretion to determine whether an asset qualifies.

Vulnerabilities affecting social media accounts (Telegram, Reddit, X/Twitter, Discord, and similar) are eligible only for impacts that result from a technical vulnerability directly attributable to 1inch's configuration or infrastructure, not from compromise of individual employee credentials, third-party platform vulnerabilities, or platform-wide issues affecting all users of that platform. Such reports are capped at High severity.

Reports combining multiple lower-severity findings into a meaningful impact will be evaluated based on the final combined demonstrated impact, not on individual components. Each component must still be a valid technical finding, and the chain must be reproducible end-to-end with a working PoC.

Gaps in logging, monitoring, or alerting are not eligible as standalone reports. They will only be considered as part of a report demonstrating exploitation of another in-scope vulnerability, where the absence of detection materially extends the attacker's window of opportunity. This must be demonstrated within the PoC, not asserted theoretically.

#### Additional Terms

#### For social media accounts, only impacts that affect those specific accounts/channels but do not affect all or others on those respective platforms on a platform-wide basis are considered as in-scope. All others are considered out-of-scope. 

Any vulnerability discovered must be reported no later than 24 hours after the initial discovery. Reports submitted after this window may be considered at 1inch's discretion but are not guaranteed eligibility for a reward.

In cases where the same vulnerability is reported through multiple platforms, priority will be determined by the earlier submission timestamp, regardless of the platform used.

#### Reward Payment Terms

Payouts are handled by the 1inch team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. 

Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

**All Categories:**

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage  
* Impacts caused by attacks requiring access to leaked keys/credentials  
* Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production  
* Best practice recommendations  
* Feature requests  
* Impacts on test files and configuration files unless stated otherwise in the bug bounty program  
* Impacts requiring phishing or other social engineering attacks against project's employees and/or customers  
* Vulnerabilities affecting users of outdated browsers or platforms  
* Most brute-forcing issues without a clear impact
* Vulnerabilities in third-party components (excluding critical vulnerabilities) 

**Websites and Apps**

* Theoretical impacts without any proof or demonstration  
* Impacts involving attacks requiring physical access to the victim device  
* Impacts involving attacks requiring access to the local network of the victim  
* Reflected plain text injection (e.g. url parameters, path, etc.)  
* This does not exclude reflected HTML injection with or without JavaScript  
* This does not exclude persistent plain text injection  
* Any impacts involving self-XSS  
* Captcha bypass using OCR without impact demonstration  
* CSRF with no state modifying security impact (e.g. logout CSRF)  
* Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact  
* Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces  
* Impacts causing only the enumeration or confirmation of the existence of users or tenants  
* Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows  
* Lack of SSL/TLS best practices  
* Impacts that only require DDoS  
* UX and UI impacts that do not materially disrupt use of the platform  
* Impacts primarily caused by browser/plugin defects  
* Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)  
* Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)  
* SPF/DMARC misconfigured records  
* Missing HTTP Headers without demonstrated impact  
* Automated scanner reports without demonstrated impact  
* UI/UX best practice recommendations  
* Reports of open ports, exposed service banners, or fingerprinting of running services without demonstrated exploitation
* Subdomain takeover findings on abandoned or non-production subdomains without demonstrated impact on production systems or users


  
**Prohibited Activities:**

* Attempting phishing or other social engineering attacks against our employees and/or customers  
* Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)  
* Any denial of service attacks that are executed against project assets  
* Automated testing of services that generates significant amounts of traffic  
* Public disclosure of an unpatched vulnerability in an embargoed bounty  
* Testing infrastructure vulnerabilities that may degrade, modify, or disrupt production systems is strictly prohibited. Researchers should demonstrate impact through read-only or proof-of-access actions whenever possible. Any active exploitation that modifies production state requires prior written approval from 1inch.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
