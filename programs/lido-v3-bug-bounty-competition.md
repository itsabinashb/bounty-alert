# Bug Bounty Comp | Lido V3

- Page: https://immunefi.com/bug-bounty/lido-v3-bug-bounty-competition/scope/
- Max bounty: $2,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: 2025-12-09T12:00:00.000Z

## Assets in scope (30)

- [smart_contract] https://github.com/lidofinance/lido-oracle/releases/tag/7.0.0-beta.3 — [off-chain] Lido Accounting Oracle
- [smart_contract] https://hoodi.etherscan.io/address/0x1d10DB6a66EF8D2A6f6D36Ad4dc7092Ef7C12569 — VaultFactory.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x2A1d51BF3aAA7A7D027C8f561e5f579876a17B0a — EIP712StETH.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x2F0303F20E0795E6CCd17BD5efE791A586f28E03 — DepositSecurityModule.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x2a833402e3F46fFC1ecAb3598c599147a78731a9 — OracleDaemonConfig.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x30308CD8844fb2DB3ec4D056F1d475a802DCA07c — HashConsensus.sol for ValidatorsExitBusOracle
- [smart_contract] https://hoodi.etherscan.io/address/0x32EC59a78abaca3f91527aeB2008925D5AaC1eFC — HashConsensus.sol for AccountingOracle
- [smart_contract] https://hoodi.etherscan.io/address/0x3508A952176b3c15387C97BE809eaffB1982176a — Lido.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x3e144aEd003b5AE6953A99B78dD34154CF3F8c76 — PinnedBeaconProxy.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x4473dCDDbf77679A643BdB654dbd86D67F8d32f2 — WithdrawalVault.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x4C9fFC325392090F789255b9948Ab1659b797964 — VaultHub.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x4e3b9fd9f713e5dba86255febd4c402794135095 — LazyOracle.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x501e678182bB5dF3f733281521D3f3D1aDe69917 — OperatorGrid.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x53417BA942bC86492bAF46FAbA8769f246422388 — OracleReportSanityChecker.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x6679090D92b08a2a686eF8614feECD8cDFE209db — TriggerableWithdrawalsGateway.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x6d1a9bBFF97f7565e9532FEB7b499982848E5e07 — MinFirstAllocationStrategy.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x7D25D43D5a69ae0521440211C655C11840aF0FD6 — Dashboard.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x7E99eE3C66636DE415D2d7C880938F2f40f94De4 — wstETH.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x8664d394C2B3278F26A1B44B967aEf99707eeAB2 — ValidatorsExitBusOracle.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x9b108015fe433F173696Af3Aa0CF7CDb3E104258 — LidoExecutionLayerRewardsVault.sol
- [smart_contract] https://hoodi.etherscan.io/address/0x9b5b78D1C9A3238bF24662067e34c57c83E8c354 — Accounting.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xCc820558B39ee15C7C45B59390B503b83fb499A8 — StakingRouter.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xE96BE4FB723e68e7b96244b7399C64a58bcD0062 — StakingVault.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xa5F55f3402beA2B14AE15Dae1b6811457D43581d — PredepositGuarantee.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xa5F5A9360275390fF9728262a29384399f38d2f0 — ValidatorExitDelayVerifier.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xb2c99cd38a2636a6281a849C8de938B3eF4A7C3D — Burner.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xbf95Cd394cC03cD03fEA62A435ac347314877f1d — ValidatorConsolidationRequests.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xcb883B1bD0a41512b42D2dB267F2A2cd919FB216 — AccountingOracle.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xe2EF9536DAAAEBFf5b1c130957AB3E80056b06D8 — LidoLocator.sol
- [smart_contract] https://hoodi.etherscan.io/address/0xfe56573178f1bcdf53F01A6E9977670dcBBD9186 — WithdrawalQueueERC721.sol

## Asset notes

__Proof of Concept (PoC) Requirements__
A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

__Asset Accuracy Assurance__

- Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Code Freeze Assurance__

This competition is running on testnet.

Code of the assets in scope is frozen while the program is live.

Duplicate submissions of bugs are **invalid**. 

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

__Private Known Issues Rewards Policy__

- Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

- Lido adheres to the Primacy of Rules, which means that the whole program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

- No KYC is required for the Lido Bug Bounty Competition

__Eligibility Criteria__

- Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
   - On OFACs SDN list 
   - Official contributor, both past or present
   - Employees and/or individuals closely associated with the project 
   - Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

- Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
   - Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

- Immunefi may publish bug reports submitted to this Bug Bounty Competition and a leaderboard of the participants and their earnings.

__Proof of Concept (PoC) Requirements__
- A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Feasibility Limitations__

- The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed in the "Scope" section) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

__Immunefi Standard Badge__

- By adhering to Immunefi’s best practice recommendations, Lido has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (15)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Acquiring owner/admin rights or roles without contract’s owner/admin action
- [smart_contract] High: Economic/financial attacks
- [smart_contract] High: Missing access controls / unprotected internal interfaces
- [smart_contract] High: Off-chain apps sensitive data extraction (e.g. Oracle private keys)
- [smart_contract] High: Permanent freezing of tokenized staking yield
- [smart_contract] High: Reversible freezing of funds
- [smart_contract] High: Theft of tokenized staking yield
- [smart_contract] High: Theft or loss of funds from a treasury
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Susceptibility to frontrunning

## Impact notes

**Build Commands, Test Commands, and How to Run Them**

https://github.com/lidofinance/core/blob/feat/vaults/CONTRIBUTING.md


**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Lido V3 represents a fundamental expansion of the Lido staking protocol through the introduction of Staking Vaults (stVaults) – isolated vault contracts that enable specialized staking arrangements between stakers and node operators. stVaults allow stETH to be minted not only from the main Lido pool but also from ETH held in these external contracts. All stVaults are coordinated and monitored by a central VaultHub contract that ensures proper collateralization and operational health.

The upgrade implements EIP-7002 support for triggerable withdrawals for stVaults, enabling more flexible exit mechanisms for staked ETH. 

To handle the increased complexity of managing multiple isolated vaults, the oracle system has been significantly enhanced with a "Lazy Oracle" design that reports vault-specific data and processes updates asynchronously rather than requiring synchronous updates for all vaults simultaneously, improving scalability and reducing on-chain overhead.

New Node Operator Predeposit Guarantee mechanism addresses deposit frontrunning vulnerabilities by requiring node operators to pre-commit their deposit data on-chain before actual deposits occur. This system includes on-chain BLS signature verification to cryptographically validate the deposit credentials, ensuring that operators cannot substitute malicious validator keys at deposit time. 

All new components – core protocol accounting upgrade, stVaults architecture, oracle enhancements, and predeposit guarantees are included within the competition scope.

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

- Hoodi tokens: 
   - [ERC20] stETH
      - https://hoodi.etherscan.io/token/0x3508A952176b3c15387C97BE809eaffB1982176a 
   - [ERC20] wstETH
      - https://hoodi.etherscan.io/token/0x7E99eE3C66636DE415D2d7C880938F2f40f94De4 
   - [ERC721] unstETH
      - https://hoodi.etherscan.io/token/0xfe56573178f1bcdf53F01A6E9977670dcBBD9186 

- Mainnet tokens:
   - [ERC20] stETH
      - https://etherscan.io/token/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84 
   - [ERC20] wstETH
      - https://etherscan.io/token/0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0 
   - [ERC721] unstETH
      - https://etherscan.io/token/0x889edC2eDab5f40e902b864aD4d7AdE8E412F9B1 

**Which chains and/or networks will the code in scope be deployed to?**

- Ethereum Hoodi Testnet (chainId: 560048)
- Ethereum Mainned (chainId: 1)

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

Lido’s codebase can be found at
- Smart contracts:  https://github.com/lidofinance/core/releases/tag/v3.0.0-rc.4
- Oracle: https://github.com/lidofinance/lido-oracle/releases/tag/7.0.0-beta.3

Documentation and further resources can be found on: 
- Lido V3 Hoodi Testnet contracts: https://docs.lido.fi/deployed-contracts/hoodi
- Lido V3 Whitepaper: https://hackmd.io/@lido/B1NuB15-gx 
- Lido V3 Technical Design: https://hackmd.io/@lido/stVaults-design 
- Lido V3 — Design & Implementation Proposal
   - https://research.lido.fi/t/lido-v3-design-implementation-proposal/10665 
- Risk Assessment Framework for stVaults
   - https://research.lido.fi/t/risk-assessment-framework-for-stvaults/9978 
- Default risk assessment framework and fee parameters for stVaults
   - https://research.lido.fi/t/default-risk-assessment-framework-and-fees-parameters-for-lido-v3-stvaults/10504

## Rewards

- [smart_contract] Critical: level=critical, payout=Max: $2,000,000 - Min: 50,000 + *Portion of the bonus reward pool, pocRequired=True
- [smart_contract] High: level=high, payout=Max: $250,000 - Min: 10,000 + *Portion of the bonus reward pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Max: $50,000 - Min: 1,000 + *Portion of the bonus reward pool, pocRequired=True

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/) 

In addition to the regular [Lido Bug Bounty Competition](https://immunefi.com/bug-bounty/lido/information/) rewards per severity, this competition offers a **$200,000 bonus rewards pool** for valid, non-duplicate reports on the assets in scope on this program.

This **$200,000 bonus pool** will be distributed among researchers based on the severity of their valid, unique submissions, as determined at the end of the competition.

Bonus rewards are paid out in the following **priority order**:

1. Critical vulnerabilities
2. High vulnerabilities
3. Medium vulnerabilities

The **pool is allocated top-down**, meaning bonuses are paid to higher severity submissions first. If sufficient funds remain after paying critical submissions, bonuses will be issued to high severity findings, and so on.

**If fewer vulnerabilities are found than the total size of the pool, the full pool will not be spent.**

For example, if only a single valid Critical is found, the bonus paid will be **$75,000**, and the remaining **$125,000 will go unused**.

Bonus amounts for each unique, valid report are:

- Critical: $75,000
- High: $20,000
- Medium: $5,000

If the number of valid submissions in a given severity exceeds the available bonus pool for that severity category, then the funds will be **evenly split among all eligible submissions** in that category. For example, if 4 criticals are found, each critical severity report will be rewarded $50,000. 

##### *Note:

1. The **bonus rewards pool is limited to $200,000**.
2. If the bonus rewards pool is exhausted, **reports will still be rewarded** under the regular Bug Bounty Program reward terms.
3. Bug reports will be paid after the Bug Bounty Competition ends and rewards are calculated. 
4.** Insights are out of scope** for this Bug Bounty Competition.
5. Any reports on Lido assets that are NOT in scope for this Bug Bounty Competition should be submitted to [Lido Bug Bounty Program](https://immunefi.com/bug-bounty/lido/information/).
6. **Duplicate** submissions of bugs are **not valid**. 
7. Rewards are denominated in USD and distributed in USDC on Ethereum.
8. Reports submitted via the regular Bug Bounty Program page will not be eligible for bonus rewards.
9. If the same bug is submitted separately to both the Bug Bounty Program and the Bug Bounty Competition, the report will be eligible for rewards only under the program where it was submitted first. For example:
- If Security Researcher A submits a valid bug to the Bug Bounty Program, and Security Researcher B submits the same bug to the Bug Bounty Competition, then only Security Researcher A is eligible, under Bug Bounty Program terms.
- If the reverse happens, only Security Researcher B qualifies, under Bug Bounty Competition terms.

__Impacts Clarifications__

**Critical**

Loss of user funds:
- When a minimum of 2,000,000 USD of assets is at risk
- Reward: *Minimum 100,000 USD*, *Maximum 2,000,000 USD*

Loss of non-user funds (e.g., treasury):
- When a minimum of 1,000,000 USD of assets is at risk
- Reward: *Minimum 50,000 USD*, *Maximum 1,000,000 USD*

**High**

- When a minimum of 250,000 USD of assets is at risk
- Reward: *Minimum 10,000 USD*, *Maximum 250,000 USD*

**Medium**

- When a minimum of 50,000 USD of assets is at risk
- Reward: *Minimum 1,000 USD*, *Maximum 50,000 USD*

__Impact Estimation__

Impact estimation must correspond to the first phase of Lido V3 launch: https://research.lido.fi/t/lido-v3-design-implementation-proposal/10665#p-22926-rollout-plan-9

i.e., 
- Lido Core works as of now on mainnet
- stVaults global minting cap is 3% of TVL
- permissionned node operators
- each node operator has 50k mintable
- emergency msigs attached according to the post

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be paused, only the initial attack window of 1-hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by pausing the component where the vulnerability exists.
- If the smart contract where the vulnerability exists can only be upgraded, only the initial attack window of 5-days for Critical issues and 9 days for other issues will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading the component where the vulnerability exists.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (6)

- Certora Lido Oracle v7 Audit Report (https://github.com/lidofinance/audits/blob/317dc39fb8b7d97e10fd7d22099fdcc2c1ac7cd2/%5BDraft%5D%20Certora%20Lido%20Oracle%20v7%20Audit%20Report%2011-2025.pdf)
- Certora Lido V3 Audit Report (https://github.com/lidofinance/audits/blob/317dc39fb8b7d97e10fd7d22099fdcc2c1ac7cd2/%5BDraft%5D%20Certora%20Lido%20V3%20Audit%20Report%20-%2011-2025.pdf)
- Composable Security Lido Oracle V7 (Lido V3) (https://github.com/lidofinance/audits/blob/2b9ae85e6ca269736ccb5426f7ea8152b625eebc/%5BDraft%5D%20Composable%20Security%20Lido%20Oracle%20V7%20(Lido%20V3)%2011-2025.pdf)
- Consensys Diligence Lido V3 Security Audit (https://github.com/lidofinance/audits/blob/317dc39fb8b7d97e10fd7d22099fdcc2c1ac7cd2/%5BDraft%5D%20Consensys%E2%80%A9Diligence%20Lido%20V3%20Security%20Audit%20-%2011-2025.pdf)
- MixBytes Lido V3 Security Audit Report (https://github.com/lidofinance/audits/blob/317dc39fb8b7d97e10fd7d22099fdcc2c1ac7cd2/%5BDraft%5D%20MixBytes%20Lido%20V3%20Security%20Audit%20Report%2011-2025.pdf)
- Public V3 audit findings log (known issues) (https://github.com/orgs/lidofinance/projects/9/views/8)
