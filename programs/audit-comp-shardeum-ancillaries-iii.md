# Audit Comp | Shardeum: Ancillaries III

- Page: https://immunefi.com/bug-bounty/audit-comp-shardeum-ancillaries-iii/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: 2025-02-12T17:00:00.000Z

## Assets in scope (4)

- [websites_and_applications] https://github.com/shardeum/archive-server/tree/itn4 — WebApp - 14144
- [websites_and_applications] https://github.com/shardeum/json-rpc-server/tree/itn4 — WebApp - 8015
- [websites_and_applications] https://github.com/shardeum/validator-cli/tree/itn4 — Command line app - 2051
- [websites_and_applications] https://github.com/shardeum/validator-gui/tree/itn4 — WebApp - - 7313

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward equal to that of a bug one severity lower.

__Known Issue Assurance__

Shardeum commits to providing Known Issue Assurance to bug submissions through their program. This means that Shardeum will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission. 

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in-scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

Shardeum adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page. 


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

## Impacts in scope (18)

- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
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
- [websites_and_applications] High: Taking down the application/website
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Medium: RPC API crash affecting projects with greater than or equal to 25% of the market capitalization on top of the respective layer
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Medium: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

__Proof of Concept (PoC) Requirements__

POCs should be tested against the most recent changes on the /tree/dev github repo.

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

**Which parts of the code are you most concerned about?**
Communication between the archiver and validators
Communication between the RPC and the validators
The GUI

**What attack vectors are you most concerned about?**
Priv escalation from the GUI
Crashing archivers
Priv escalation in  archivers. Archivers will not be public at launch
Priv escalation in RPC
Loss of data integrity on archive/RPC servers  Ex: changing receipts
**Which part(s) of the system do you want whitehats to attempt to break the most?**
Archiver and RPC server. We want them to break all of it obviously but we believe these two components need more attention

**What external dependencies are there?**

Things listed in package.json

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

The default config in the branch is in scope. Whitehats are free to configure, patch, and modify their own malicious hosts however they want. However, target service must be running the default config in the target branch running in production mode. Vulns involving a service attacking itself are not in scope. This is to prevent the whitehats from wasting time reporting things we specifically allow in debug mode. If the researchers can enable debug mode options remotely then that is valid and can be paid out.
Attacks that require the attacker to own an archive server will have their severity reduced to insight by default, but may be raised at the project’s discretion.
Attacks that require the network to still be initializing/bootstrapping are out of scope. Wait until the network mode reaches “processing” + 15 cycles after startup before launching attacks. The rules for staking/join are a little different and the network will not be public during this time. Attacks on a network that is repairing itself (was once in “processing” mode but has since degraded to “safety” or “recovery”) are in scope.
Attacks that require lots of network traffic, large messages, or many connections will be given an severity of “insight”. The project may increase this at our discretion.
0day vulnerabilities in dependencies will have a max impact of insight. Any other vuln in dependencies is out of scope.
Any report based on unit tests, simulations, or anything not a fully functioning service, will have a max impact of low.
Smart contracts and smart contract related code/functions are out of scope
Finally, the more nodes that are required to launch an attack, the more at risk the vuln is of being downgraded. If it takes 33% (for example) of the nodes in the network being malicious to cause damage, then it becomes difficult to distinguish the impact from a brute-force/51% attack, which is completely out of scope.

**Are there any unusual points about your protocol that may confuse Security Researchers?**

The archive server is designed to store the history of the network. Archivers are not a part of the core protocol, do not have any part in consensus, and do not affect joining/rotation. Another quirk is that currently, the transaction history is not chained. The cycle certificates are chained which contains information like joined and lost nodes per cycle, active nodes, archiver list, standby list, etc. The transaction history will have a Merkle root published while the chaining is developed.

## Rewards

- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Ancillaries III Boost Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31797437799441-Shardeum-Ancillaries-III-Audit-Competition-Reward-Terms)


The reward pool will be entirely distributed among participants. The size depends on the bugs found:
* If one or more Critical severity bugs are found, **the reward pool will be 100% of the respective reward pool, $100,000 USD**
* If one or more High severity bugs are found, the **reward pool will be 75% of the respective reward pool, $75,000 USD** 
* If one or more Medium severity bugs are found, **the reward pool will be 50% of the respective reward pool, $50,000 USD**
* Otherwise, the reward pool will be **25% of the respective reward pool, $25,000 USD**

For this Audit Competition, duplicates and private known issues are valid for a reward. 

Private known issues will unlock higher reward pools according to their severity level without any downgrade. For example, a Critical severity bug which was a private known issue would unlock the reward pool conditional on a Critical severity bug being found.


Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3.](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/) 

**Duplicates of Insight reports are not eligible for a reward.** 

**Reward Payment Terms**
Payouts are handled by the Shardeum team directly and are denominated in USD. However, payments are done in USDC

**Insight Rewards Payment Terms**
Insight Rewards: Portion of the Rewards Pool

The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights.](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

## Out of scope (program-specific)

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
Bugs from previous bounties are in scope unless explicitly said otherwise. Reports 33428, 33655, 33963, 34508, 33576, 34053, 36024, 36025, 36025 are OOS.

[https://reports.immunefi.com/shardeum-ancillaries](https://reports.immunefi.com/shardeum-ancillaries-ii)

[https://reports.immunefi.com/shardeum-ancillaries-ii](https://reports.immunefi.com/shardeum-ancillaries-ii)


**Other Known issues**

- AJV Validation error on archiver can cause missing receipts [https://github.com/shardeum/archiver/blob/bugbounty/src/Data/Collector.ts#L280](https://github.com/shardeum/archiver/blob/bugbounty/src/Data/Collector.ts#L280)

- getTxTimestampBinary endpoint could be used as a memory overflow mechanism [https://github.com/shardeum/core/blob/9dae0abe5232ed532a9285da82118b41a04b3711/src/state-manager/TransactionConsensus.ts#L1796](https://github.com/shardeum/core/blob/9dae0abe5232ed532a9285da82118b41a04b3711/src/state-manager/TransactionConsensus.ts#L1796)

- SQL injection in inputs at https://github.com/shardeum/shardeum/blob/dev/src/storage/sqlite3storage.ts#L257-L289

- Tx data : ( ORIGINAL_TX_DATA) getting saved in originalTxData, processedData and transaction table without any verification [https://github.com/shardeum/archiver/blob/cbe1d515e91058d17fa483f84361992cd3d1cf9c/src/archivedCycle/StateMetaData.ts#L156](https://github.com/shardeum/archiver/blob/cbe1d515e91058d17fa483f84361992cd3d1cf9c/src/archivedCycle/StateMetaData.ts#L156)

## Out of scope and rules

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
Bugs from previous bounties are in scope unless explicitly said otherwise. Reports 33428, 33655, 33963, 34508, 33576, 34053, 36024, 36025, 36025 are OOS.

[https://reports.immunefi.com/shardeum-ancillaries](https://reports.immunefi.com/shardeum-ancillaries-ii)
[https://reports.immunefi.com/shardeum-ancillaries-ii](https://reports.immunefi.com/shardeum-ancillaries-ii)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Known Issues before BB1 (https://drive.google.com/file/d/1H6o8IPtrlTDvr_cfTRhvgr1Vvh4EYwb8/view)
