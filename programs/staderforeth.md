# Stader for ETH

- Page: https://immunefi.com/bug-bounty/staderforeth/scope/
- Max bounty: $1,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (22)

- [smart_contract] https://etherscan.io/address/0x03ABEEC03BF39ac5A5C8886cF3496326d8164E1E — VaultFactory
- [smart_contract] https://etherscan.io/address/0x09134C643A6B95D342BdAf081Fa473338F066572 — PermissionedPool
- [smart_contract] https://etherscan.io/address/0x1DE458031bFbe5689deD5A8b9ed57e1E79EaB2A4 — Permissionless Socializing Pool
- [smart_contract] https://etherscan.io/address/0x3073cC90aD39E0C30bb0d4c70F981FbD00f3458f — validatorWithdrawalVault
- [smart_contract] https://etherscan.io/address/0x4ABEF2263d5A5ED582FC9A9789a41D85b68d69DB — StaderConfig
- [smart_contract] https://etherscan.io/address/0x4f4Bfa0861F62309934a5551E0B2541Ee82fdcF1 — PermissionlessNodeRegistry
- [smart_contract] https://etherscan.io/address/0x62e0b431990Ea128fe685E764FB04e7d604603B0 — PoolSelector
- [smart_contract] https://etherscan.io/address/0x7Af4730cc8EbAd1a050dcad5c03c33D2793EE91f — SDCollateral
- [smart_contract] https://etherscan.io/address/0x84645f1B80475992Df2C65c28bE6688d15dc6ED6 — Penalty
- [smart_contract] https://etherscan.io/address/0x84ffDC9De310144D889540A49052F6d1AdB2C335 — OperatorRewardCollector
- [smart_contract] https://etherscan.io/address/0x85A22763f94D703d2ee39E9374616ae4C1612569 — Auction
- [smart_contract] https://etherscan.io/address/0x97c92752DD8a8947cE453d3e35D2cad5857367af — NodeELRewardVault
- [smart_contract] https://etherscan.io/address/0x9F0491B32DBce587c50c4C43AB303b06478193A7 — User Withdrawal Manager
- [smart_contract] https://etherscan.io/address/0x9d4C3166c59412CEdBe7d901f5fDe41903a1d6Fc — Permissioned Socializing Pool
- [smart_contract] https://etherscan.io/address/0xA35b1B31Ce002FBF2058D22F30f95D405200A15b — ETHx Token
- [smart_contract] https://etherscan.io/address/0xF64bAe65f6f2a5277571143A24FaaFDFC0C2a737 — StaderOracle
- [smart_contract] https://etherscan.io/address/0xaf42d795A6D279e9DCc19DC0eE1cE3ecd4ecf5dD — PermissionedNodeRegistry
- [smart_contract] https://etherscan.io/address/0xbe3781CE437Cc3fC8c8167913B4d462347D11F20 — StaderInsuranceFund
- [smart_contract] https://etherscan.io/address/0xcf5EA1b38380f6aF39068375516Daf40Ed70D299 — Stader Stake Pool Manager
- [smart_contract] https://etherscan.io/address/0xd1a72Bd052e0d65B7c26D3dd97A98B74AcbBb6c5 — PermissionlessPool
- [smart_contract] https://etherscan.io/address/0xeDA89ed8F89D786D816F8E14CF8d2F90c6BF763f — PoolUtils
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user deposited funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of staked funds
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Protocol insolvency
- [smart_contract] High: Theft of unclaimed yield on a recurring basis
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$1,000,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$100,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$20,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Reward Calculation for Critical Level Reports__

For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 1 000 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 100 000 is to be rewarded in order to incentivize security researchers against withholding a bug report.   

__Repeatable Attack Limitations__

In cases of repeatable attacks for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs acknowledged below are not eligible for any reward through the bug bounty program. 
- SD Auction final bid price can be gamed by MEV optimization. (This is intended)
- Node Operator can avoid small portion of validator penalty by exiting at the right time. (This is limited to once per validator and cost of exiting and reactivation does not justify penalty saved)
- ER update via chainlink may return incorrect or state data as it is not implemented yet, Currently ER data is submitted by oracle members.
- Protocol will not benefit from slashing mechanism when remaining penalty bigger than minThreshold of SD 

__Previous Audits__

Stader has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.
- [https://www.staderlabs.com/audits/ethereum/smartcontracts/ETHx_SmartContract_Audit_Report_by_Halborn_v2.pdf](https://www.staderlabs.com/audits/ethereum/smartcontracts/ETHx_SmartContract_Audit_Report_by_Halborn_v2.pdf)
- [https://www.staderlabs.com/audits/ethereum/smartcontracts/ETHx_SmartContract_audit_report_by_SigmaPrime_v2.pdf](https://www.staderlabs.com/audits/ethereum/smartcontracts/ETHx_SmartContract_audit_report_by_SigmaPrime_v2.pdf)

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart Contract - Critical
- Smart Contract - High
- Smart Contract - Medium

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the Stader team directly and are denominated in USD. However, payments are done in USDC.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
