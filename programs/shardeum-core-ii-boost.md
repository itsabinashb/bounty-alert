# Audit Comp | Shardeum: Core II

- Page: https://immunefi.com/bug-bounty/shardeum-core-ii-boost/scope/
- Max bounty: $150,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - low, blockchain_dlt - medium, blockchain_dlt - high, blockchain_dlt - critical
- End date: 2024-10-16T12:00:00.000Z

## Assets in scope (3)

- [blockchain_dlt] https://github.com/shardeum/shardeum/tree/dev — Validator [22461]
- [blockchain_dlt] https://github.com/shardeum/shardus-core/tree/dev — Core [53000]
- [blockchain_dlt] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

Shardeum’s up to date codebase can be found at [https://github.com/shardeum/](https://github.com/shardeum/).

A note on Shardeum and Shardus Core scope: the default config in the dev branch is in scope. Whitehats are free to configure, patch, and modify their own malicious nodes however they want. However, target nodes must be running the default config in dev. This is to prevent the whitehats from wasting time reporting things we specifically allow in debug mode. The only exception is minNodes and maxNodes settings, which allow different size networks to be created. Certain vulnerabilities may only exist in certain network sizes, and we do not wish to limit Whitehat activity and participation for lack of computing power attempting to run a large local network. However, network-wide attacks that only work under 128 nodes may be rejected or reduced in severity at our discretion. If the researchers can enable debug mode options remotely then that is valid and can be paid out.

Attacks that require the network to still be initializing/bootstrapping are out of scope. Wait until the network mode reaches “processing” + 15 cycles after startup before launching attacks. The rules for staking/join are a little different and the network will not be public during this time. Attacks on a network that is repairing itself (was once in “processing” mode but has since degraded to “safety” or “recovery”) are in scope.

Attacks that require lots of network traffic, large messages, or many connections are at risk of being degraded to insight.

0day vulnerabilities in dependencies will have a max impact of insight. Any other vuln in dependencies is out of scope.

Any report based on unit tests, simulations, or anything not a fully functioning network, will have a max impact of low.

Smart contracts are out of scope

Finally, the more nodes that are required to launch an attack, the more at risk the vuln is of being downgraded. If it takes 33% (for example) of the nodes in the network being malicious to cause damage, then it becomes difficult to distinguish the impact from a brute-force/51% attack, which is completely out of scope.

__Mid-Contest Code Updates__

In this contest bug fixes may be applied mid-contest. This is required for Shardeum to test changes on their beta networks in preparation for an imminent mainnet launch.

The project is to keep changes private as far as possible. When changes need to be made public, then the changelog will be updated here & in the [Shardeum Audit Competition Discord channel](https://discord.com/invite/immunefi?utm_source=immunefi). Publicly fixed bugs are invalid and the scope is updated to the new code.

All bug reports before the fix was public will earn a reward. All bug reports after are invalid. If a new bug is introduced by their fix then it is valid for a reward.

__Mid-Contest Changelog__

**Shardeum**
- fix: subtracting slashing penalty twice - [#158](https://github.com/shardeum/shardeum/pull/158/commits/22f537f277962a6379bb49b60f504a03332129b5)
- Remove unused method getDebugString - [#281](https://github.com/shardeum/shardus-core/pull/281/commits/2b42c2f4d8e68c70aa2d712f4778a539e436f596)

**Shardus Core**
- add cycle to unjoin request - [#279](https://github.com/shardeum/shardus-core/pull/279/commits/46e437bc54537a835534f497d37775ae391cfda0)
- getStoredCycleByTimestamp() adjusted slightly to return exclusive lower bound and inclusive upper bound - [d1a3507](https://github.com/shardeum/shardus-core/commit/d1a350783ce2f72ec51129643e7290b4de2500d7)
- comment out deprecated and unused "gossip-final-state" handler - [#272](https://github.com/shardeum/shardus-core/pull/272/commits/30e43d4c4a8a2282b11d1476f70a2f80681affdf)
- added signature verification to gossipValidJoinRequests handler - [#280](https://github.com/shardeum/shardus-core/pull/280/commits/ef57a48ee9bf7332844360b3d6c7fdac8f4bcceb)
- Improved error handling and input validation around join routes - [#286](https://github.com/shardeum/shardus-core/pull/286/commits/e18d7bd080f18311bf98024d5573d4cc5769f423)
- fix: foreign socket stream unsubscribing archiver on behalf of another socket stream - [#264](https://github.com/shardeum/shardus-core/pull/264/commits/7f75e01a85dc89bb21c5798ef15b288cca5787bb)
- fix(api): added account limit to get_account_data_with_queue_hints - [#283](https://github.com/shardeum/shardus-core/pull/283/commits/14d4b483e21b41151110971323bf71dfa82d6aa0)

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

## Impacts in scope (11)

- [blockchain_dlt] Critical: Bypassing Slashing
- [blockchain_dlt] Critical: Bypassing Staking Requirements
- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Blocking Specific Transactions
- [blockchain_dlt] Medium: Causing network processing nodes to process transactions from the transaction queue beyond set parameters
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network

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

We are concerned with the web3 and business logic within both repositories in this audit competition. Things like transaction queuing, slashing, and consensus. This includes any internal transactions or things involving the global account.

- **What attack vectors are you most concerned about?**

Parsing/signature errors, cheating the rotation system, cheating the slashing, and transaction processing. We received quite a few message parsing and signature related reports in the previous audit competitions and feel like there may still be some vulns to find.

- **Which part(s) of the system do you want whitehats to attempt to break the most?**

Transaction queuing, slashing, and consensus.

- **Are there any assumed invariants that you want whitehats to attempt to break?**

Sum of EOA account balances before attack == Sum of EOA account balances after attack + transaction fees. This should cover SHM disappearing from the network or being created out of thin ai

__Where might whitehats confuse out-of-scope code to be in-scope?__

A note on Shardeum and Shardus Core scope: the default config in the dev branch is in scope. Whitehats are free to configure, patch, and modify their own malicious nodes however they want. However, target nodes must be running the default config in dev. This is to prevent the whitehats from wasting time reporting things we specifically allow in debug mode. The only exception is minNodes and maxNodes settings, which allow different size networks to be created. Certain vulnerabilities may only exist in certain network sizes, and we do not wish to limit Whitehat activity and participation for lack of computing power attempting to run a large local network. However, network-wide attacks that only work under 128 nodes may be rejected or reduced in severity at our discretion. If the researchers can enable debug mode options remotely then that is valid and can be paid out.

Attacks that require the network to still be initializing/bootstrapping are out of scope. Wait until the network mode reaches “processing” + 15 cycles after startup before launching attacks. The rules for staking/join are a little different and the network will not be public during this time. Attacks on a network that is repairing itself (was once in “processing” mode but has since degraded to “safety” or “recovery”) are in scope.

Attacks that require lots of network traffic, large messages, or many connections are at risk of being degraded to insight.

0day vulnerabilities in dependencies will have a max impact of insight. Any other vuln in dependencies is out of scope.

Any report based on unit tests, simulations, or anything not a fully functioning network, will have a max impact of low.

Smart contracts are out of scope

Finally, the more nodes that are required to launch an attack, the more at risk the vuln is of being downgraded. If it takes 33% (for example) of the nodes in the network being malicious to cause damage, then it becomes difficult to distinguish the impact from a brute-force/51% attack, which is completely out of scope.

__Are there any unusual points about your protocol that may confuse whitehats?__

Please consider how your vulnerability will behave on a network with a shard size of 128 nodes. We will accept reports with a PoC on a smaller network, but the severity may be affected if the impact is less feasible on network with a shard size of 128 nodes.

__What is the test suite setup information?__

[https://gist.github.com/kun6fup4nd4/162d491e07d0a84344abbf33bc602502](https://gist.github.com/kun6fup4nd4/162d491e07d0a84344abbf33bc602502)

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
- [List of Known Issues for Shardeum | Core II and Shardeum | Ancillaries II Audit Competitions](https://immunefisupport.zendesk.com/hc/en-us/articles/28112833600401-List-of-Known-Issues-for-Shardeum-Core-II-and-Shardeum-Ancillaries-II-Audit-Competitions)
- The list of previously discovered vulnerabilities will be published in a few days.

__Previous Audits__

Shardeum’s completed audit reports can be found here: [Arcadia (draft)](https://docs.google.com/document/d/1OlmijVY2ga_7QEe8DYU-NTEXfAqMRpuwlduIofjmEwA/edit#heading=h.5uoc4mfz7mn4), [HashCloack](https://docs.google.com/document/d/1n11d40JZYgL33-F-Lw6FMuBP9AJSXvyg-xBpJhwOkUE/edit). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Shardeum Core II Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/28077659023505-Shardeum-Core-II-Audit-Competition-Reward-Terms)

The reward pool will be entirely distributed among participants. The size depends on the bugs found:
- If one or more Critical severity bugs are found, **the reward pool will be 100% of the respective reward pool, $150,000 USD**
- If one or more High severity bugs are found, **the reward pool will be 75% of the respective reward pool, $112,500 USD**
- If one or more Medium severity bugs are found, **the reward pool will be 50% of the respective reward pool, $75,000 USD**
- If Low severity bugs or no bugs are found, **the reward pool will be 25% of the respective reward pool, $37,500 USD**

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

__Blockchain/DLT & Smart Contract Specific:__

- Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks

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
