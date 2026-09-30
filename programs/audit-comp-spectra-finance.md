# Audit Comp | Spectra Finance

- Page: https://immunefi.com/bug-bounty/audit-comp-spectra-finance/scope/
- Max bounty: $40,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-04-17T14:00:00.000Z

## Assets in scope (25)

- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/RateOracleRegistry.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/amm/RateAdjustmentOracle.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/factory/Factory.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/factory/FactorySNG.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/libraries/CurveOracleLib.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/libraries/CurvePoolUtil.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/libraries/RateAdjustmentMath.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/router/Dispatcher.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/router/util/RouterUtil.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/cryptoswap-ng/BaseFeedCurveLPTAsset.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/cryptoswap-ng/BaseFeedCurveLPTIBT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/cryptoswap-ng/BaseFeedCurvePTAsset.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/cryptoswap-ng/BaseFeedCurvePTIBT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/cryptoswap-ng/BaseFeedCurveYTAsset.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/cryptoswap-ng/BaseFeedCurveYTIBT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/stableswap-ng/BaseFeedCurveLPTAsset.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/stableswap-ng/BaseFeedCurveLPTIBT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/stableswap-ng/BaseFeedCurvePTAsset.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/stableswap-ng/BaseFeedCurvePTIBT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/stableswap-ng/BaseFeedCurveYTAsset.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/chainlinkFeeds/stableswap-ng/BaseFeedCurveYTIBT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/oracles/BaseOracleCurveLPT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/oracles/BaseOracleCurvePT.sol
- [smart_contract] https://github.com/immunefi-team/Spectra-Audit-Competition/blob/main/src/spectra-oracles/oracles/BaseOracleCurveYT.sol

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Spectra adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

No KYC is required for the Spectra Finance Audit Competition

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this Audit Competition bug bounty and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

When there is uncertainty about how feasible an attack is Immunefi will use our feasibility limitation standards to determine the severity of the report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Spectra has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Build commands, Test commands, and instructions on how to run them:**

The project uses Foundry as a development framework. 

To build the project and install all the dependencies run: forge build

For running tests run: forge test

For running specific test cases please refer to foundry documentation or run: forge test --help


**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?**

The Router handle any ERC20 tokens and ERC4626 vaults


**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

Contracts can be paused and upgraded


**Which chains and/or networks will the code in scope be deployed to?**

Ethereum Mainnet, Optimism, Arbitrum, Sonic, Base


**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

This audit covers the integration of Curve NG and Curve Stableswap NG pools into Spectra’s core protocol. Spectra is currently using Cryptoswap pools, and this audit concerns the migration to these two new sets of pools. All other Spectra features remain intact, including the implementation of the Principal Token and the Yield Token. Below is a high-level overview of the integration tasks:
Integration of Cryptoswap NG pools

- The next generation of Curve pools on which Spectra is currently based.
- Integration of a new type of pool: oracle-based Stableswap NG pools
- Upgradeable rate oracles for Stableswap NG pools that reports the rate of the PT in underlying based on its initial price
- Deployment of Spectra with Stableswap NG pools through a new factory
- Registration of rate oracles in a new dedicated registry
- Addition of previews and interaction execution with the new pools in the router


**Where do you suspect there may be bugs?**

The main focus should be the StableSwap NG integration. correctness, robustness and resilience of the rate adjustment oracles for the Principal Token should be thoroughly examined.
Secondly, the new commands of the router should be examined.


**What external dependencies are there?**

Curve smart contracts and Open Zeppelin libraries.

Stableswap-NG documentation at [(https://docs.curve.fi/stableswap-exchange/stableswap-ng/overview/)]

Open Zeppelin v5 at [(https://docs.openzeppelin.com/contracts/5.x/)]


**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Security problems related to the implementation of Curve Finance pools and their internal oracle manipulations. Only Spectra’s rate oracle implementation and its influence on Stableswap’s pricing shall be considered in scope, besides Spectra’s core components. 


**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

Any address controlled by the Spectra DAO

**Previous Audits**

Spectra’s completed audit reports can be found at [](https://docs.spectra.finance/security/audits). Unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the reward pool, pocRequired=True

## Reward notes

**Reward pool:**

The following reward terms are a summary. For the full details read our [Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

A reward pool of $40,000 USD will be distributed among participants, if any valid bugs are found. 

If not a single bug is found (Insights do not count as bugs) the reward pool is $15% of $40,000 USD rewards → $6,000

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

*Insight Rewards*: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

**Duplicates of Insight reports are not eligible for a reward.**

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.
For unclear reports or to resolve disputes Immunefi may still require a runnable PoC.Read more about it in [Audit Competition Proof-of-Concept Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/33260632501777-Audit-Competition-Proof-of-Concept-Rules)

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Spectra Protocol Hack Analysis (https://lunaray.medium.com/spectra-protocol-hack-analysis-06b877498757)
