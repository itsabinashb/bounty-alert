# 1inch - Web

- Page: https://immunefi.com/bug-bounty/1inch-web/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - low, websites_and_applications - medium, websites_and_applications - high, websites_and_applications - critical
- End date: (none)

## Assets in scope (3)

- [websites_and_applications] http://1inch.com/ — 1inch Web - Homepage
- [websites_and_applications] http://blog.1inch.com/ — 1inch Web - Blog Page
- [websites_and_applications] https://1inch.network — 1inch Web - Network Homepage

## Asset notes

(none)

## Impacts in scope (21)

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
- [websites_and_applications] Critical: Server-Side Request Forgery (SSRF) leading to access to internal services, cloud metadata endpoints, or sensitive internal resources
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Supply chain compromise leading to execution of malicious code in the production application (e.g., compromised dependencies, build pipeline injection)
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
- [websites_and_applications] High: Server-Side Request Forgery (SSRF) leading to access to non-sensitive internal resources or enabling port/service enumeration of internal infrastructure
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] High: Use of broken or weak cryptographic algorithms or implementations that could deterministically lead to compromise of session tokens, authentication mechanisms, or transaction signing integrity
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$50,000, minReward=$15,000, otherImpactMaxReward=$15,000, rewardModel=range
- [websites_and_applications] High: maxReward=$15,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Low: maxReward=$1,000, minReward=$100, rewardModel=range

## Reward notes

## Rewards by Threat Level

Rewards are distributed according to the impact of the vulnerability based on the Impacts in Scope table. 

## Reward Calculation for Critical Level Reports

For critical web/apps bugs, reports will be rewarded with 50000, only if the impact leads to:

* A loss of funds involving an attack that does not require any user action  
* Private key or private key generation leakage leading to unauthorized access to user funds causing a final impact of “Direct Theft of User Funds” 

All other impacts for assets with those designations that would be classified as Critical would be rewarded a flat amount of 15000\. 

## Reward Calculation for Other Levels

High, Medium, and Low reports are rewarded at a flat rate of USD 5 000, USD 1 000, and USD 100, respectively. At the discretion of 1inch, it may decide to increase the reward paid out to security researchers for exceptional cases. However, it makes no commitment to rewarding above these amounts. 


Only the listed subdomains and exact pages in the Assets in Scope table are considered as in-scope. All other subdomains and pages are out of scope for this bug bounty program. 

For the impact “Taking over broken or expired outgoing links”, this does not apply to broken links on blog.1inch.com when referencing an external link on a blog post. This also doesn’t apply to social media assets and posts, unless it only involves an internal link. 

Vulnerabilities reported for blog.1inch.com are capped at Medium severity regardless of the impact demonstrated. The maximum reward for blog.1inch.com is USD 5000 at the discretion of the 1inch team with a base reward of USD 1000.

## Additional Terms

Any vulnerability discovered must be reported no later than 24 hours after the initial discovery. Reports submitted after this window may be considered at 1inch's discretion but are not guaranteed eligibility for a reward.

In cases where the same vulnerability is reported through multiple platforms, priority will be determined by the earlier submission timestamp, regardless of the platform used.

Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

**All Categories:**

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage  
* Impacts caused by attacks requiring access to leaked keys/credentials  
* Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible  
* Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code  
* Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production  
* Best practice recommendations  
* Feature requests  
* Impacts on test files and configuration files unless stated otherwise in the bug bounty program  
* Impacts requiring phishing or other social engineering attacks against project's employees and/or customers

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
* Clickjacking and tapjacking attacks without demonstration of a meaningful state-modifying impact
* OPTIONS/TRACE HTTP method enabled
* Open redirects (unless a serious impact is demonstrated)
* Host header issues without PoC
* Reflected file download (RFD)
* Mixed HTTP/HTTPS content

**Prohibited Activities:**

* Any testing with pricing oracles or third-party smart contracts  
* Attempting phishing or other social engineering attacks against our employees and/or customers  
* Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)  
* Any denial of service attacks that are executed against project assets  
* Automated testing of services that generates significant amounts of traffic  
* Public disclosure of an unpatched vulnerability in an embargoed bounty  
* Accessing or modifying data belonging to other users  
* Submitting AI-generated reports  
* Spamming forms or account creation flows (even with low volume)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
