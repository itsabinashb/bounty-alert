# Audit Comp | Shardeum: Ancillaries II

- Page: https://immunefi.com/bug-bounty/shardeum-ancillaries-ii-boost/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - low, websites_and_applications - medium, websites_and_applications - high, websites_and_applications - critical
- End date: 2024-10-16T12:00:00.000Z

## Assets in scope (5)

- [websites_and_applications] https://github.com/shardeum/archive-server/tree/dev — Archive server [13717]
- [websites_and_applications] https://github.com/shardeum/json-rpc-server/tree/dev — Json rpc server [7957]
- [websites_and_applications] https://github.com/shardeum/validator-cli/tree/dev — Command line app [1895]
- [websites_and_applications] https://github.com/shardeum/validator-gui/tree/dev — Validator gui [3200]
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

Shardeum’s up to date codebase can be found at [https://github.com/shardeum/](https://github.com/shardeum/).

__Mid-Contest Code Updates__

In this contest bug fixes may be applied mid-contest. This is required for Shardeum to test changes on their beta networks in preparation for an imminent mainnet launch.

The project is to keep changes private as far as possible. When changes need to be made public, then the changelog will be updated here & in the [Shardeum Audit Competition Discord channel](https://discord.com/invite/immunefi?utm_source=immunefi). Publicly fixed bugs are invalid and the scope is updated to the new code.

All bug reports before the fix was public will earn a reward. All bug reports after are invalid. If a new bug is introduced by their fix then it is valid for a reward.

__Mid-Contest Changelog__

Currently none.

POCs should be tested against the most recent changes on the /tree/dev github repo.

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward equal to that of a bug one severity lower.

__Known Issue Assurance__

Shardeum commits to providing Known Issue Assurance to bug submissions through their program. This means that Shardeum will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission. 

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in-scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

Shardeum adheres to the Primacy of Impact for all impacts.

Primacy of Impact means that the impact is prioritized rather than a specific asset. This encourages security researchers to report on all bugs with an in-scope impact, even if the affected assets are not in scope. For more information, please see [Best Practices: Primacy of Impact](https://immunefisupport.zendesk.com/hc/en-us/articles/12340245635089-Best-Practices-Primacy-of-Impact). 

When submitting a report on Immunefi’s dashboard, the security researcher should select the Primacy of Impact asset placeholder. If the team behind this project has multiple programs, those other programs are not covered under Primacy of Impact for this program. Instead, check if those other projects have a bug bounty program on Immunefi.

If the project has any testnet and/or mock files, those will not be covered under Primacy of Impact.

All other impacts are considered under the Primacy of Rules, which means that they are bound by the terms and conditions set within this program.

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

By adhering to Immunefi’s best practice recommendations, Shardeum has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (20)

- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as: Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:   /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as: Changing registration information, Commenting, Voting, Making trades, Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  Email Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as: Email address, Phone number, Physical address, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as: Email address, Phone number, Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as: HTML injection without JavaScript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] High: Taking down the application/website
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction: Changing the first/last name of user, Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as: Reflected HTML injection, Loading external site data
- [websites_and_applications] Medium: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Medium: RPC API crash affecting projects with greater than or equal to 25% of the market capitalization on top of the respective layer
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Medium: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction:  Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:  Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as: Locking up the victim from login, Cookie bombing, etc.

## Impact notes

__Proof of Concept (PoC) Requirements__

POCs should be tested against the most recent changes on the /tree/dev github repo.

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info__

- Shardeum’s up to date codebase can be found at [https://github.com/shardeum/](https://github.com/shardeum/)
- Shardeum’s youtube page: [https://www.youtube.com/@Shardeum](https://www.youtube.com/@Shardeum)
- Previous tech walkthroughs: [https://www.youtube.com/watch?v=U2ZHqQchBgA](https://www.youtube.com/watch?v=U2ZHqQchBgA), [https://www.youtube.com/watch?v=Lt-jI8FAQcQ](https://www.youtube.com/watch?v=Lt-jI8FAQcQ)
- Whitepaper: [https://docs.shardeum.org/docs/whitepaper](https://docs.shardeum.org/docs/whitepaper)
- Documentation: [https://docs.shardeum.org/](https://docs.shardeum.org/)

__Where do you suspect there may be bugs?__

- **Which parts of the code are you most concerned about?**
     - Communication between the archiver and validators
     - Communication between the RPC and the validators
     - The GUI

- **What attack vectors are you most concerned about?**
     - Priv escalation from the GUI
     - Crashing archivers
     - Priv escalation in  archivers. Archivers will not be public at launch
     - Priv escalation in RPC

- **Which part(s) of the system do you want whitehats to attempt to break the most?**
     - Archiver and RPC server. We want them to break all of it obviously but we believe these two components need more attention

__Where might whitehats confuse out-of-scope code to be in-scope?__

The default config in the dev branch is in scope. Whitehats are free to configure, patch, and modify their own malicious hosts however they want. However, target service must be running the default config in dev. This is to prevent the whitehats from wasting time reporting things we specifically allow in debug mode. If the researchers can enable debug mode options remotely then that is valid and can be paid out.

Attacks that require the network to still be initializing/bootstrapping are out of scope. Wait until the network mode reaches “processing” + 15 cycles after startup before launching attacks. The rules for staking/join are a little different and the network will not be public during this time. Attacks on a network that is repairing itself (was once in “processing” mode but has since degraded to “safety” or “recovery”) are in scope.

Attacks that require lots of network traffic, large messages, or many connections are at risk of being degraded to insight.

0day vulnerabilities in dependencies will have a max impact of insight. Any other vuln in dependencies is out of scope.

Any report based on unit tests, simulations, or anything not a fully functioning service, will have a max impact of low.

Smart contracts and smart contract related code/functions are out of scope

Finally, the more nodes that are required to launch an attack, the more at risk the vuln is of being downgraded. If it takes 33% (for example) of the nodes in the network being malicious to cause damage, then it becomes difficult to distinguish the impact from a brute-force/51% attack, which is completely out of scope.

__Are there any unusual points about your protocol that may confuse whitehats?__

The archive server is designed to store the history of the network. Archivers are not a part of the core protocol, do not have any part in consensus, and do not affect joining/rotation. Another quirk is that currently, the transaction history is not chained. The cycle certificates are chained which contains information like joined and lost nodes per cycle, active nodes, archiver list, standby list, etc. The transaction history will have a Merkle root published while the chaining is developed.


__What is the test suite setup information?__

Here is a helpful PoC scaffolding. Even though it targets the Core II audit competition, it may still be helpful here

[https://gist.github.com/kun6fup4nd4/162d491e07d0a84344abbf33bc602502](https://gist.github.com/kun6fup4nd4/162d491e07d0a84344abbf33bc602502)

RPC: [https://github.com/shardeum/json-rpc-server/tree/localtest#running-tests](https://github.com/shardeum/json-rpc-server/tree/localtest#running-tests)

Archiver: No specific doc, however an archiver is launched with the local network when following the directions here: [https://github.com/shardeum/shardeum?tab=readme-ov-file#running-the-network-locally](https://github.com/shardeum/shardeum?tab=readme-ov-file#running-the-network-locally).

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk.
- [List of Known Issues for Shardeum | Core II and Shardeum | Ancillaries II Audit Competitions](https://immunefisupport.zendesk.com/hc/en-us/articles/28112833600401-List-of-Known-Issues-for-Shardeum-Core-II-and-Shardeum-Ancillaries-II-Audit-Competitions)
- The list of previously discovered vulnerabilities will be published in a few days.

__Previous Audits__

Shardeum’s completed audit reports can be found here: [Arcadia (draft)](https://docs.google.com/document/d/1OlmijVY2ga_7QEe8DYU-NTEXfAqMRpuwlduIofjmEwA/edit#heading=h.5uoc4mfz7mn4), [HashCloack](https://docs.google.com/document/d/1n11d40JZYgL33-F-Lw6FMuBP9AJSXvyg-xBpJhwOkUE/edit). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Shardeum Ancillaries II Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/28077740315537-Shardeum-Ancillaries-II-Audit-Competition-Reward-Terms)

The reward pool will be entirely distributed among participants. The size depends on the bugs found:
- If one or more Critical severity bugs are found, **the reward pool will be 100% of the respective reward pool, $100,000 USD**
- If one or more High severity bugs are found, **the reward pool will be 75% of the respective reward pool, $75,000 USD**
- If one or more Medium severity bugs are found, **the reward pool will be 50% of the respective reward pool, $50,000 USD**
- If Low severity bugs or no bugs are found, **the reward pool will be 25% of the respective reward pool, $25,000 USD**

**Duplicates of Insight reports are not eligible for a reward.**

For this Audit Competition, duplicates and private known issues are valid for a reward. 

Private known issues will unlock higher reward pools according to their severity level without any downgrade. For example, a Critical severity bug which was a private known issue would unlock the reward pool conditional on a Critical severity bug being found.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Payment Terms__

Payouts are handled by the Shardeum team directly and are denominated in USD. However, payments are done in USDC.

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi).

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
