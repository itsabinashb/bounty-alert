# IOP | SwayLend Frontend

- Page: https://immunefi.com/bug-bounty/swaylend-frontend-iop/scope/
- Max bounty: $30,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: 2024-12-17T10:00:00.000Z

## Assets in scope (2)

- [websites_and_applications] https://github.com/Swaylend/swaylend-monorepo/tree/develop/apps/frontend — Frontend
- [websites_and_applications] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Swaylend: frontend adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page. 

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this audit competition and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Swaylend has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (14)

- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] Critical: Taking down the application/website
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

__Whitehat Educational Resources & Technical Info__

Documentation: https://docs.swaylend.com/


**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Swaylend is the port of Compound V3 lending protocol and architecture in the Sway programming language for the Fuel Network.


**What external dependencies are there?**

The frontend uses many external libraries, the most important dependencies related to smart contracts are: 
1. Fuel libraries for handling wallet connections, contract types and calling of smart contract methods.
- @fuel-ts/contract
- @fuels/connectors
- @fuels/react
- fuels

2. Pyth libraries for handling fetching of price updates from their Hermes network and load Pyth contract ABI types. 
- @pythnetwork/hermes-client
- @pythnetwork/pyth-fuel-js

3. Other larger libraries used are:
- Next.js 14
- Tailwind
- @tanstack/react-query
- Zustand


**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?**

Only SRC-20 are supported, which are similar to ERC-20 standard but on the Fuel Network


**Where might whitehats confuse out-of-scope code to be in-scope?**

Bugs found inside external libraries related to contract calls, specifically Fuel and Pyth libraries.
Wrong usage of the above libraries, still counts as in-scope.

**Are there any unusual points about your protocol that may confuse whitehats?**

Pyth is used as a pull oracle by Swaylend. Pyth pull oracle information: https://docs.pyth.network/price-feeds/pull-updates

**Where do you suspect there may be bugs?**

Swaylend is the lending protocol that offers functionalities like other lending protocols, i.e., supplying base assets (in our case, USDC) and borrowing base assets in exchange for providing collateral assets. The most critical things that should be tested are:
- Withdrawing only assets that you supplied
- Borrowing only the amount you're allowed (based on supplied collateral asset and collateral factor)
- Repaying the borrowed amount before withdrawing collateral asset


__Public Disclosure of Known Issues__
Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

There are no known public disclosures for frontend

__Previous Audits__

Swaylend’s completed audit reports can be found at https://www.halborn.com/audits/swaylend. Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

## Rewards

- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

The following reward terms are a summary, for the full details read our [IOP | SwayLend: Frontend - Reward Distribution Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/29893062996881-IOP-SwayLend-Frontend-Rewards-Terms). 

A reward pool of $30,000 USD will be distributed among participants, even if no valid bugs are found. 

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

*The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

Duplicates of Insight are not rewarded.

## Out of scope (program-specific)

(none)

## Out of scope and rules

These impacts are out of scope for this bug bounty program. 

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program

__Websites and Apps__

- Theoretical impacts without any proof or demonstration
- Impacts involving attacks requiring physical access to the victim device
- Impacts involving attacks requiring access to the local network of the victim
- Reflected plain text injection (e.g. url parameters, path, etc.)
- This does not exclude reflected HTML injection with or without JavaScript
- This does not exclude persistent plain text injection
- Any impacts involving self-XSS
- Captcha bypass using OCR without impact demonstration
- CSRF with no state modifying security impact (e.g. logout CSRF)
- Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact
- Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces
- Impacts causing only the enumeration or confirmation of the existence of users or tenants
- Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows
- Lack of SSL/TLS best practices
- Impacts that only require DDoS
- UX and UI impacts that do not materially disrupt use of the platform
- Impacts primarily caused by browser/plugin defects
- Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)
- Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)
- SPF/DMARC misconfigured records)
- Missing HTTP Headers without demonstrated impact
- Automated scanner reports without demonstrated impact
- UI/UX best practice recommendations
- Non-future-proof NFT rendering

__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
