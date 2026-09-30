# Audit Comp | Folks Finance: Staking Contracts

- Page: https://immunefi.com/bug-bounty/audit-comp-folks-finance-staking-contracts/scope/
- Max bounty: $25,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2026-03-17T15:00:00.000Z

## Assets in scope (3)

- [smart_contract] https://github.com/Folks-Finance/folks-staking-contracts/blob/main/src/Staking.sol — Staking.sol
- [smart_contract] https://github.com/Folks-Finance/folks-staking-contracts/blob/main/src/interfaces/IMigratorV1.sol — IMigratorV1.sol
- [smart_contract] https://github.com/Folks-Finance/folks-staking-contracts/blob/main/src/interfaces/IStakingV1.sol — IStakingV1.sol

## Asset notes

**Insight Reporting**

Insight reports may be reported to this program and require a PoC. Insights are rewarded according to [Immunefi’s Standardized Competition Reward Terms.](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms)

**Dispute Resolution**

If there is any dispute over bug reports between projects and security researchers, Immunefi has final say on validity and severity based on the terms of this program.

**Responsible Publication Policy**

- Immunefi will publish bug reports, earnings, and a leaderboard for this Audit Competition.
- Security Researchers may publish their bug reports as well, but only after Immunefi has published the valid bug reports as part of the competition results.

**Eligibility Criteria**

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in an audit review of the code in scope (Such auditors may still participate in this program only if they receive project permission)

## Impacts in scope (11)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Build Commands, Test Commands, and How to Run Them** 
See https://github.com/Folks-Finance/folks-staking-contracts?tab=readme-ov-file#usage.

**Asset Accuracy Assurance**
Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**
Code of the assets in scope is frozen while the program is live.

**Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.**

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

**Public Disclosure of Known Issues**

These aren’t necessarily “issues”, some are design decisions and tradeoffs:
- Not checking zero address
- StakeParams slippage is one directional by design
- User will have to use new account if they reach staking limit
- Not deleting “UserStake” state after everything has been withdrawn
- Not deleting “StakingPeriod” state after deactivating 
- Updates to a “StakingPeriod” only impact new stakes by design
- We allow stake with 0 rewards
- We allow withdrawal of 0 amount
- We intentionally don’t allow a partial stake amount if the entire amount would cause cap to be exceed
- Operational risk of migration
- MIGRATOR_ROLE persists for user after migration
- State “migrationPermits” may contain migrator which had its MIGRATOR_ROLE later revoked
- After migration, the indexes of the “userStakes” are shuffled. This could lead to a user referencing an outdated index.
- Paused contract only prevents new stakes
- “UserStake.aprBps” is for informational purposes 
- The function “stakeWithPermit” silently ignores permit failure
- Reward and accrual calculations round down
- Intentional to not decrease “capUsed” on withdrawal / migration
     - Staking contract designed for ERC20 which doesn't have any fee on transfer or rebasing logic


**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

---


**Where might Security Researchers confuse out-of-scope code to be in-scope?**

The MigratorV1 contract is out of scope - it’s included for testing. In addition, the potential new version of the Staking which we would migrate to, is also out of scope. 


**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

An attacker being able to manipulate their rewards/stake in order to steal FOLKS from other stakers. Flows to look at should include migration. 

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

ERC20 which doesn’t have any fee on transfer or rebasing logic. 

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

Ability to pause contract with PAUSER_ROLE and migrate to new Staking contract with MIGRATOR_ROLE. 

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

Default admin, manager, pauser, migrator. 

**Which chains and/or networks will the code in scope be deployed to?**

BNB Chain

**What external dependencies are there?**

FOLKS Token https://bscscan.com/address/0xFF7F8F301F7A706E3CfD3D2275f5dc0b9EE8009B  

**Are there any unusual points about your protocol that may confuse Security Researchers?**

When the staking period ends, both principal and reward unlock linearly over a separate unlock duration, allowing partial withdrawals at any point.

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

https://github.com/Folks-Finance/folks-staking-contracts?tab=readme-ov-file#staking-contract

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of Reward Pool, pocRequired=False
- [smart_contract] High: level=high, payout=Portion of Reward Pool, pocRequired=False
- [smart_contract] Medium: level=medium, payout=Portion of Reward Pool, pocRequired=False
- [smart_contract] Low: level=low, payout=Portion of Reward Pool, pocRequired=False

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants. 

Rewards are denominated in USD and distributed in USDC on Ethereum.

Flat Rewards:
The reward pool is **$25,000 USD** if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

If not a single bug is found (Insights do not count as bugs) the reward pool is **$3,750 USD**.
Private known issues, meaning known issues that were not publicly disclosed, are valid and unlock the corresponding reward pool.

**Proof of Concept (PoC) Requirements**
A **runnable PoC**, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
