# 1inch - Business

- Page: https://immunefi.com/bug-bounty/1inch-business/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - high, websites_and_applications - critical, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (4)

- [websites_and_applications] https://api.1inch.com — API
- [websites_and_applications] https://business.1inch.com/ — Business Subdomain
- [websites_and_applications] https://business.1inch.com/portal/ — Business Portal
- [websites_and_applications] https://business.1inch.com/portal/documentation/ — Business Documentation Page

## Asset notes

(none)

## Impacts in scope (24)

- [websites_and_applications] Critical: Authentication or authorization bypass leading to unauthorized access to other users' accounts, data, or API keys (including but not limited to IDOR vulnerabilities)
- [websites_and_applications] Critical: Cache poisoning leading to serving malicious or manipulated content (including modified transaction data, contract addresses, or swap routes) to other users
- [websites_and_applications] Critical: Cloud infrastructure misconfiguration or container escape leading to unauthorized access to production infrastructure, other tenants' data, or internal services
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Manipulation of payment or billing logic resulting in unauthorized access to paid services or financial loss to the project
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Session hijacking or authentication bypass leading to full account takeover without user interaction
- [websites_and_applications] Critical: Session hijacking or authentication bypass requiring limited user interaction (up to one click)
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
- [websites_and_applications] Medium: Bypassing subscription-level rate limits in a way that allows consumption of API resources beyond the authorized plan (must be reproducible and demonstrate measurable excess usage)
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
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

- [websites_and_applications] Critical: maxReward=$100,000, minReward=$30,000, rewardModel=range
- [websites_and_applications] High: maxReward=$30,000, minReward=$10,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [websites_and_applications] Low: maxReward=$2,000, minReward=$100, rewardModel=range

## Reward notes

### Rewards by Threat Level

Rewards are distributed according to the impact of the vulnerability based on the Impacts in Scope table. 

#### Reward Calculation for Critical Level Reports

For critical web/apps bugs, reports will be rewarded with 100000, only if the impact leads to:

* A loss of funds involving an attack that does not require any user action  
* Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts for assets with those designations that would be classified as Critical would be rewarded a flat amount of 30000\. 

#### Reward Calculation for Other Levels

High, Medium, and Low reports are rewarded at a flat rate of USD 10 000, USD 2 000, and USD 100, respectively. At the discretion of 1inch, it may decide to increase the reward paid out to security researchers for exceptional cases. However, it makes no commitment to rewarding above these base amounts. 

#### Other Restrictions and Limitations

Only the listed subdomains and exact pages in the Assets in Scope table are considered as in-scope. All other subdomains and pages are out of scope for this bug bounty program. 

Vulnerabilities reported for business.1inch.com and business.1inch.com/portal/documentation are capped at Medium severity. The maximum reward for these assets is USD 10000\.

Vulnerabilities found in non-production environments (including but not limited to staging, development, and preview deployments) are capped at High severity. The maximum reward for non-production vulnerabilities is USD 30000\.

#### Reward Payment Terms

Payouts are handled by the 1inch team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. 

Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.

## Out of scope (program-specific)

### Out of Scope & Rules 

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
* Impacts on public API endpoints not explicitly listed in the Assets in Scope table  
* Session fixation attacks without demonstration of account takeover or other meaningful impact  
* Manipulation of password reset tokens without demonstrated real-world impact (e.g., token reuse without account takeover)
* Vulnerabilities affecting users of outdated browsers or platforms
* Vulnerabilities involving active content, such as web browser add-ons
* Most brute-forcing issues
* Open redirects (unless a serious impact is demonstrated)
* OPTIONS/TRACE HTTP method enabled
* Content spoofing
* Text injection
* Reflected file download (RFD)
* Mixed HTTP/HTTPS content
* CSRF in forms that are available to anonymous users (e.g., contact forms)


**Prohibited Activities:**

* Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet  
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
