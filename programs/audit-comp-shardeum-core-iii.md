# Audit Comp | Shardeum: Core III

- Page: https://immunefi.com/bug-bounty/audit-comp-shardeum-core-iii/scope/
- Max bounty: $250,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low
- End date: 2025-02-12T17:00:00.000Z

## Assets in scope (4)

- [blockchain_dlt] https://github.com/shardeum/lib-crypto-utils/tree/bugbounty — Library–499
- [blockchain_dlt] https://github.com/shardeum/lib-net/tree/bugbounty — Library–2321
- [blockchain_dlt] https://github.com/shardeum/shardeum/tree/bugbounty — DLT- - 22264
- [blockchain_dlt] https://github.com/shardeum/shardus-core/tree/bugbounty — DLT - 48906

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward equal to that of a bug one severity lower.

__Known Issue Assurance__

Shardeum commits to providing Known Issue Assurance to bug submissions through their program. This means that Shardeum will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission. 

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in-scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

Shardeum adheres to the Primacy of Rules for all impacts. Which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page. 



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

- [blockchain_dlt] Critical: Bypassing Penalties
- [blockchain_dlt] Critical: Bypassing Staking Requirements
- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Blocking specific wallet addresses from making transactions
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network

## Impact notes

**Which chains and/or networks will the code in scope be deployed to?**

Shardeum

**Which parts of the code are you most concerned about?**
We are concerned with the web3 and business logic within all four repositories in this boost. Things like transaction queuing, penalties, and consensus. This includes any internal transactions or things involving the global account.

**What attack vectors are you most concerned about?**

Parsing/signature errors, cheating the rotation system, and transaction processing. We received quite a few message parsing and signature related reports in the previous boosts and feel like there may still be some vulns to find. Secure accounts and multisig transactions involving them will be valuable targets and need extra scrutiny.
**Which part(s) of the system do you want whitehats to attempt to break the most?**
transaction queuing, penalties, and consensus.
**Are there any assumed invariants that you want whitehats to attempt to break?**
Sum of EOA account balances before attack == Sum of EOA account balances after attack + transaction fees. This should cover SHM disappearing from the network or being created out of thin air

**What external dependencies are there?**

These are listed in package.json

**Where might Security Researchers confuse out-of-scope code to be in-scope?**


A note on Shardeum and Shardus Core scope: the default config in release mode in the branch is in scope. Whitehats are free to configure, patch, and modify their own malicious nodes however they want. However, target nodes must be running the default config in the target branch in release mode. This is to prevent the whitehats from wasting time reporting things we specifically allow in debug mode. The only exception is minNodes and maxNodes settings, which allow different size networks to be created. Certain vulnerabilities may only exist in certain network sizes, and we do not wish to limit Whitehat activity and participation for lack of computing power attempting to run a large local network. However, network-wide attacks that only work under 128 nodes may be rejected or reduced in severity at our discretion. If the researchers can enable debug mode options remotely then that is valid and can be paid out.

Attacks that require the network to still be initializing/bootstrapping are out of scope. Wait until the network mode reaches “processing” + 15 cycles after startup before launching attacks. The rules for staking/join are a little different and the network will not be public during this time. Attacks on a network that is repairing itself (was once in “processing” mode but has since degraded to “safety” or “recovery”) are in scope.
This bounty introduces the concept of a KYC-required “genesis node”. Attacks performed with genesis nodes are in scope, attacks performed against genesis nodes are in scope. Nodes attacking themselves are out of scope.

0day vulnerabilities in dependencies are in scope. Any other vuln in dependencies is out of scope. Smart contracts are out of scope

Finally, the more nodes that are required to launch an attack, the more at risk the vuln is of being downgraded. If it takes 33% (for example) of the nodes in the network being malicious to cause damage, then it becomes difficult to distinguish the impact from a brute-force/51% attack, which is completely out of scope.

**Are there any unusual points about your protocol that may confuse Security Researchers?**

Please consider how your vulnerability will behave on a network with a shard size of 129 nodes. We will accept reports with a PoC on a smaller network, but the severity may be affected if the impact is less feasible on network with a shard size of 129 nodes.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Shardeum Core III Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31793771662865-Shardeum-Core-III-Audit-Competition-Reward-Terms)

The reward pool size is determined by the greatest condition met. If multiple conditions are met only the largest reward pool applies.

If one or more Critical severity bugs are found, the reward pool will be **100% of the respective reward pool, $250,000 USD**
If one or more High severity bugs are found, the reward pool will be **75% of the respective reward pool, $187,500 USD**
If one or more Medium severity bugs are found, the reward pool will be **50% of the respective reward pool, $125,000 USD**
Otherwise, the reward pool will be **25% of the respective reward pool, $62,500 USD**

Duplicates and private known issues are valid for a reward.

**Duplicates of Insight reports are not eligible for a reward.**
Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3.](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

**Reward Payment Terms**
Payouts are handled by the Shardeum team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

**Insight Rewards Payment Terms**
Insight Rewards: Portion of the Rewards Pool
The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights.](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

## Out of scope (program-specific)

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

Bugs from previous bounties are in scope unless explicitly said otherwise.

Reports 33428, 33655, 33963, 34508, 33576, 34053, 36024, 36025, 36025 are OOS.


Shardeum Core full list of [reports](https://app.gitbook.com/o/SXzCm0g2yGtKdYxV9Y1d/s/eYmXU5PPPCrUVU4AeKnd/shardeum-core) 
Shardeum Core II full list of [reports](https://app.gitbook.com/o/SXzCm0g2yGtKdYxV9Y1d/s/eYmXU5PPPCrUVU4AeKnd/shardeum-core-ii)

**Other Known issues**

- AJV Validation error on archiver can cause missing receipts [https://github.com/shardeum/archiver/blob/bugbounty/src/Data/Collector.ts#L280](https://github.com/shardeum/archiver/blob/bugbounty/src/Data/Collector.ts#L280)

- getTxTimestampBinary endpoint could be used as a memory overflow mechanism [https://github.com/shardeum/core/blob/9dae0abe5232ed532a9285da82118b41a04b3711/src/state-manager/TransactionConsensus.ts#L1796](https://github.com/shardeum/core/blob/9dae0abe5232ed532a9285da82118b41a04b3711/src/state-manager/TransactionConsensus.ts#L1796)

- SQL injection in inputs at https://github.com/shardeum/shardeum/blob/dev/src/storage/sqlite3storage.ts#L257-L289

- Tx data : ( ORIGINAL_TX_DATA) getting saved in originalTxData, processedData and transaction table without any verification [https://github.com/shardeum/archiver/blob/cbe1d515e91058d17fa483f84361992cd3d1cf9c/src/archivedCycle/StateMetaData.ts#L156](https://github.com/shardeum/archiver/blob/cbe1d515e91058d17fa483f84361992cd3d1cf9c/src/archivedCycle/StateMetaData.ts#L156)

## Out of scope and rules

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

Bugs from previous bounties are in scope unless explicitly said otherwise.
Reports 33428, 33655, 33963, 34508, 33576, 34053, 36024, 36025, 36025 are OOS.


Shardeum Core full list of [reports](https://app.gitbook.com/o/SXzCm0g2yGtKdYxV9Y1d/s/eYmXU5PPPCrUVU4AeKnd/shardeum-core) 
Shardeum Core II full list of [reports](https://app.gitbook.com/o/SXzCm0g2yGtKdYxV9Y1d/s/eYmXU5PPPCrUVU4AeKnd/shardeum-core-ii)

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- Known Issues before BB1 (https://drive.google.com/file/d/1H6o8IPtrlTDvr_cfTRhvgr1Vvh4EYwb8/view)
- Shardeum Core II Audit Competition (https://reports.immunefi.com/shardeum-core-ii)
- https://reports.immunefi.com/shardeum-core (https://reports.immunefi.com/shardeum-core)
