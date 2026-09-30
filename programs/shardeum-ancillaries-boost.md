# Audit Comp | Shardeum: Ancillaries

- Page: https://immunefi.com/bug-bounty/shardeum-ancillaries-boost/scope/
- Max bounty: $200,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: 2024-08-14T06:00:00.000Z

## Assets in scope (8)

- [websites_and_applications] https://github.com/shardeum/archive-server/tree/dev — Archive Server [13421]
- [websites_and_applications] https://github.com/shardeum/explorer-server/tree/dev — Explorer Server [14856]
- [websites_and_applications] https://github.com/shardeum/json-rpc-server/tree/dev — JSON RPC Server [7936]
- [websites_and_applications] https://github.com/shardeum/lib-net/tree/dev — LIB NET [2742]
- [websites_and_applications] https://github.com/shardeum/relayer-collector/tree/dev — Relayer Collection [8768]
- [websites_and_applications] https://github.com/shardeum/relayer-distributor/tree/dev — Relayer Distributor [2830]
- [websites_and_applications] https://github.com/shardeum/validator-cli/tree/dev — Validator CLI [1871]
- [websites_and_applications] https://github.com/shardeum/validator-gui/tree/dev — Validator GUI [3048]

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

## Impacts in scope (16)

- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as: Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as: /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as: Changing registration information, Commenting, Voting, Making trades, Withdrawals, etc.
- [websites_and_applications] High: Taking down the application/website
- [websites_and_applications] Medium: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Email, Password of the victim etc.
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (persistent), such as: HTML injection without JavaScript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] Medium: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as: Iframing leading to modifying the backend/browser state (must have a PoC)
- [websites_and_applications] Low: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, e.g: Changing the first/last name of user, Enabling/disabling notifications
- [websites_and_applications] Low: Improperly disclosing confidential user information, such as: Email address, Phone number, Physical address, etc.
- [websites_and_applications] Low: Injecting/modifying the static content on the target application without JavaScript (reflected), such as: Reflected HTML injection, Loading external site data
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as: Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as: Locking up the victim from login, Cookie bombing, etc.

## Impact notes

__Proof of Concept (PoC) Requirements__

POCs should be tested against the most recent changes on the /tree/dev github repo.

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info__
Architecture documents: [https://docs.shardeum.org/docs/architecture/high-level-architecture](https://docs.shardeum.org/docs/architecture/high-level-architecture)

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

No

__Where do you suspect there may be bugs? Useful aspects of this question are:__

- **Which parts of the code are you most concerned about?**
    RPC server, Archive server, and GUI
- **What attack vectors are you most concerned about?**
    Highly concerned with the Validator GUI. At the time of writing and likely at the time of launch, the GUI will be homogenous for most of the nodes in the network. A critical bug here can quickly destroy the network as it will instantly impact every node.
- **Which part(s) of the system do you want whitehats to attempt to break the most?**
	All of it
- **Are there any assumed invariants that you want whitehats to attempt to break?**
    No

__What external dependencies are there?__

Just the packages listed in the package.json of each repo.

__Where might whitehats confuse out-of-scope code to be in-scope?__

Since we are doing two concurrent audit competitions with repositories that interact with each other, the specific boundaries of which vulnerability belongs to which audit competition may become confusing. A vulnerability may exist in the communication between an archive server and a validator for example. We would like to assure researchers that regardless of the final decision of which audit competition a particular vulnerability belongs to, the researcher will get paid. We may have final say over where a vuln belongs but the researcher will get their bounty pending the other eligibility factors.

__Are there any unusual points about your protocol that may confuse whitehats?__

The role of archivers in the Shardeum network is a little different from similar components in other networks. Archivers have no role in a node joining or leaving the network. Archivers have no role in consensus or syncing. They are merely an archive of the history of the network.

Weak subjectivity solutions do not apply to the Shardeum network because long range attacks are not relevant. Shardeum does not have probabilistic finality so there is no risk of a competing chain becoming valid.

__What is the test suite setup information?__

The simple network test suite: [https://github.com/shardeum/simple-network-test](https://github.com/shardeum/simple-network-test)
Larger test suite setup: [https://github.com/shardeum/json-rpc-server/tree/localtest/src/__tests__/integration](https://github.com/shardeum/json-rpc-server/tree/localtest/src/__tests__/integration)

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

List of [Shardeum’s Known Issues](https://immunefisupport.zendesk.com/hc/en-us/articles/26510185034641-List-of-Known-Issues-for-Shardeum-Core-and-Shardeum-Ancillaries-Audit-Competitions).

__Previous Audits__

Shardeum’s completed audit reports can be found here: [Arcadia (draft)](https://docs.google.com/document/d/1OlmijVY2ga_7QEe8DYU-NTEXfAqMRpuwlduIofjmEwA/edit#heading=h.5uoc4mfz7mn4), [HashCloack](https://docs.google.com/document/d/1n11d40JZYgL33-F-Lw6FMuBP9AJSXvyg-xBpJhwOkUE/edit). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Shardeum | Ancillaries Reward Distribution Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/26482375730577-Shardeum-Ancillaries-Audit-Competition-Reward-Terms). 

The reward pool will be distributed among participants. The size depends on the bugs found:
- If no High or Critical severity bugs are found the reward pool will be **$100,000 USD**
- If one or more High severity bugs are found the reward pool will be **$120,000 USD**
- If 1 Critical severity bug is found the reward pool will be **$160,000 USD**
- If 2 Critical severity bugs are found the reward pool will be **$180,000 USD**
- If 4 or more Critical severity bugs are found the reward pool will be **$200,000 USD**

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
