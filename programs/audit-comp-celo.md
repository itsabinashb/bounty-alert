# Audit Comp | Celo

- Page: https://immunefi.com/bug-bounty/audit-comp-celo/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2024-12-06T19:00:00.000Z

## Assets in scope (29)

- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts-0.8/common/CeloUnreleasedTreasury.sol — CeloUnreleasedTreasury - 48
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts-0.8/common/EpochManager.sol — EpochManager - 488
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts-0.8/common/EpochManagerEnabler.sol — EpochManagerEnabler - 63
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts-0.8/common/GasPriceMinimum.sol — GasPriceMinimum - 160
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts-0.8/common/MentoFeeCurrencyAdapter.sol — MentoFeeCurrencyAdapter - 55
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts/common/FeeHandler.sol — FeeHandler - 4
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts/common/GoldToken.sol — GoldToken - 155
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/contracts/governance/LockedGold.sol — LockedGold - 573
- [smart_contract] https://github.com/celo-org/celo-monorepo/blob/release/core-contracts/12/packages/protocol/test-sol/unit/common/FeeHandler.t.sol — FeeHandler.t - 37
- [smart_contract] https://github.com/celo-org/celo-monorepo/commit/03d20ee25e4c2f4de40a6d922a5904d313166ef7 — Stcelo fix #2
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/ancients.go — ancients - 193
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/db.go — db - 106
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/genesis.go — genesis - 636
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/main.go — main - 378
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/non-ancients.go — ancients - 76
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/state.go — state - 304
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/state_test.go — state_test - 134
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/celo-migrate/transform.go — transform - 76
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/cmd/check-derivation/main.go — main - 391
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/deployer/broadcaster/keyed.go — keyed - 193
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/genesis/config.go — config - 776
- [smart_contract] https://github.com/celo-org/optimism/blob/celo10/op-chain-ops/genesis/genesis.go — genesis - 191
- [smart_contract] https://github.com/celo-org/staked-celo/blob/master/contracts/Account.sol — Account - 53
- [smart_contract] https://github.com/celo-org/staked-celo/blob/master/contracts/DefaultStrategy.sol — DefaultStrategy - 56
- [smart_contract] https://github.com/celo-org/staked-celo/blob/master/contracts/Manager.sol — Manager - 36
- [smart_contract] https://github.com/celo-org/staked-celo/blob/master/contracts/SpecificGroupStrategy.sol — SpecificGroupStrategy - 59
- [smart_contract] https://github.com/celo-org/staked-celo/blob/master/contracts/Vote.sol — Vote - 4
- [smart_contract] https://github.com/celo-org/staked-celo/blob/master/contracts/interfaces/IDefaultStrategy.sol — IDefaultStrategy - 8
- [smart_contract] https://github.com/celo-org/staked-celo/pull/211/files — Stcelo fix #1

## Asset notes

Celo’s up to date codebase can be found at [https://github.com/celo-org](https://github.com/celo-org). 

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Celo adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

Celo will be requesting KYC information in order to pay for successful bug submissions. The following information will be required:
- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFAC's SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this Audit Competition bug bounty and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Celo has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (15)

- [smart_contract] Critical: Critical hot wallets compromised (batcher, proposer, sequencer)
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: L1 contract manipulation (sequencer address, malicious state root update)
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds on L1
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: L2 re-org
- [smart_contract] High: Permanent freezing of funds on L2
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds

## Impact notes

__Technical Resources__

**Roadmap** 

[https://forum.celo.org/t/cel2-roadmap-update/6815](https://forum.celo.org/t/cel2-roadmap-update/6815)

**Technical**

- [https://specs.celo.org/](https://specs.celo.org/)
- [https://docs.celo.org/](https://docs.celo.org/)

**Non-technical**
[https://www.youtube.com/watch?v=mkpTmbkRv4A](https://www.youtube.com/watch?v=mkpTmbkRv4A)

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

Celo is transitioning from a standalone EVM-compatible Layer 1 blockchain to an Ethereum Layer 2. This shift, proposed by cLabs in July 2023, aims to maintain the seamless user experience that Celo is known for—characterized by speed, low costs, and ease of use—while leveraging Ethereum's security and ecosystem.

__Where do you suspect there may be bugs? Which parts of the code are you most concerned about?__

Experimental Features, Custom Gas Token, Alternate Data Availability Layer implementation in the OP Stack.

__What attack vectors are you most concerned about?__

Migration to L2 and Sequencer 

__Which part(s) of the system do you want whitehats to attempt to break the most?__

Custom Gas Currency (https://docs.celo.org/cel2/fee-currencies)

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

All ERC20 / ERC721 / ERC777 / ERC1155 standards are supported. 

__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

Test on Testnet: [https://docs.celo.org/cel2/network-information](https://docs.celo.org/cel2/network-information)

__What monitoring systems may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

Third-party security review
Blockchain Explorer

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

Any is fine on Testnet

__What external dependencies are there?__

[https://github.com/ethereum-optimism/op-geth](https://github.com/ethereum-optimism/op-geth)

__Where might whitehats confuse out-of-scope code to be in-scope?__

Open source code in defined repos are in scope. Anything on testnet is in scope. Cel2 code is not deployed to Mainnet. 

stCelo (staked-celo) is live and on Mainnet, this is in scope.  

__What is the test suite setup information?__

- [https://docs.celo.org/cel2/network-information](https://docs.celo.org/cel2/network-information)
- [https://celo.academy/t/exploring-alfajores-testnet-a-comprehensive-guide-to-celos-test-network/2618](https://celo.academy/t/exploring-alfajores-testnet-a-comprehensive-guide-to-celos-test-network/2618)

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

- [https://github.com/celo-org/staked-celo/pull/211/files](https://github.com/celo-org/staked-celo/pull/211/files)

__Previous Audits__

Celo’s previous audit reports can be found here: [https://celo.org/audits](https://celo.org/audits)

Celo’s is currently running an audit. Bugs in the audit report that aren't disclosed pre-launch are valid for rewards.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary. For the full details read our [Celo Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/30062321013393-Celo-Audit-Competition-Reward-Terms)

A reward pool of $50,000 USD will be distributed among participants, even if no valid bugs are found. 

Duplicates and private known issues are valid for a reward.

**This Audit Competition has an audit running in parallel. Bugs in the audit report that aren't disclosed pre-launch are valid for rewards.**

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

*Insight Rewards*: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

**Duplicates of Insight reports are not eligible for a reward.**

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
