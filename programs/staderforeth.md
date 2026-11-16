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

**1.) SD Auction final bid price can be gamed by MEV optimization.** (This is intended)

**2.) Node Operator can avoid small portion of validator penalty by exiting at the right time.** (This is limited to once per validator and cost of exiting and reactivation does not justify penalty saved)

**3.) ER update via Chainlink may return incorrect or stale data as it is not implemented yet; currently ER data is submitted by oracle members.**

**4.) Protocol will not benefit from slashing mechanism when remaining penalty bigger than minThreshold of SD.**

**5.) ETHx exchange rate: deposits settle at the last applied oracle rate**

The ETHx exchange rate updates only when a quorum of oracle nodes agrees on a report for a past reporting block. Until quorum, deposits mint at the previously applied rate, so a depositor who enters after the reporting block and before an upward update receives a share of rewards accrued before entry, and can redeem after the update. This is a known trade-off of a committee-reported rate and was raised in the Code4rena June 2023 audit (issues 332 and 351). Reports that a depositor can "sandwich", "front-run" or "snipe" an exchange-rate update, act on a rate revealed by an earlier oracle submission, deposit during ER inspection mode or before it closes, or capture rewards not yet reflected in the rate, are variants of this known issue, regardless of the configured withdrawal delay.

**6.) ETHx exchange rate: withdrawals finalize at the last applied rate; inspection mode does not block finalization**

Withdrawal requests finalize at the lower of the rate at request time and the rate at finalization, after the configured delay. Between a loss-reporting block and quorum, mature requests finalize at the previous rate. A single node's pre-quorum submission does not change the applied rate. Large rate movements put the oracle in ER inspection mode for manual review; inspection mode does not itself gate withdrawal finalization, and the safe-mode switch exists for that purpose. See Code4rena June 2023 issues 222, 250, 293 and 338. Reports that a withdrawer can exit before a negative report is applied, or that inspection mode should freeze finalization, are variants of this known issue.

**7.) SD Utility Pool: slashed SD collateral is not written back to the pool ledger**

When an operator's SD collateral is slashed, SDCollateral.slashSD does not reduce the operator's utilized position in SDUtilityPool, and the slashed SD is auctioned with proceeds going to ETHx stakers, as the operator bond intends. The pool keeps the amount as a receivable owed by the operator, so the cToken exchange rate can exceed the SD recoverable until the position is repaid, liquidated or written off. This is the documented lending risk of the Utility Pool (Sigma Prime SD Utility Pool audit SDP-14, acknowledged; Stader documentation on SD delegation risks). Reports of "phantom debt", "phantom interest", pool insolvency after a slash, delegator SD routed to ETH stakers, or an early withdrawer receiving more than a later one, are variants of this known issue.

**8.) Operator rewards collector: partial liquidation settlement when the operator has no active keys**

When a liquidated operator's keys have all exited and the collector balance is below the outstanding liquidation amount, the collector pays the available balance and marks the liquidation complete. Liquidators are expected to assess recoverability before calling liquidationCall; the protocol does not guarantee full recovery from an operator whose validators have already exited. Operator-side variants (remaining debt or protocol fee forgiven) and liquidator-side variants (liquidator under-paid) share this root cause.

**9.) Permissioned pool operators may utilize SD without an SD bond**

Permissioned operators are approved individually by the protocol, operate validators funded by user ETH, and post no on-chain ETH or SD collateral; their participation relies on trust and accountability rather than collateral. SDUtilityPool.utilize is not restricted by pool, getOperatorTotalEth credits collateral per active key regardless of pool, and OperatorRewardsCollector.claim() applies liquidation settlement and the withdrawable-amount cap only to permissionless operators. A liquidator of a permissioned operator should call claimLiquidation in the same transaction as liquidationCall. Reports that a permissioned operator could borrow and default, leave unpaid interest in the pool's exchange rate, skip liquidation settlement on claim, or front-run a liquidator's settlement, fall under the trusted-role exclusion and this known issue.

**10.) SD collateral: withdrawOnBehalf is permissionless**

SDCollateral.withdrawOnBehalf may be called by anyone for any operator. It can only move SD above the operator's withdrawal threshold, first repays any Utility Pool debt, and sends the remainder to the operator's own reward address. The caller gains nothing. This is intended.

**11.) Withdrawal queue: sequential finalization and small-request griefing**

UserWithdrawalManager finalizes requests strictly in order, after the configured delay, and only when the pool holds enough ETH for the next request. Anyone can submit many minimum-size requests or one large request and delay later requests until theirs are finalized. The requester locks their own ETHx for the duration and gains nothing; finalization is permissionless and resumes as ETH arrives. Delays caused by available liquidity are out of scope. Reports of "head-of-line blocking", "queue poisoning", "withdrawal spamming" or request-id manipulation are variants of this known issue.

**12.) SD price oracle: trusted nodes can move the SD price within the quorum rules**

SD price updates are the median of values submitted by trusted oracle nodes, which source prices from external data and are applied under the quorum rules in StaderOracle. The risk of a compromised or faulty price source was reviewed and accepted (Halborn ETHx oracle audit HAL-02). Reports that a compromised or colluding minority of trusted nodes or price sources can influence the SD price or the ETHx rate fall under the trusted-role exclusion.

**13.) Auction: lots may be created with zero SD**

Auction.createLot does not reject a zero _sdAmount. A zero lot holds no SD, receives no bids worth anything, and costs only the creator's gas. Storage spam of this kind is informational.

**14.) SD Utility Pool: timing of delegation around withdrawal finalization**

Queued withdrawal requests remain in the cToken supply until finalized, and finalization pays the lower of the SD value at request time and at finalization. Any surplus stays in the pool and accrues to cToken holders at that block, including late entrants. This is inherent to a queue-based, snapshot-priced withdrawal (Sigma Prime SD Utility Pool audit SDP-14).

**15.) Gas cost of iterating an operator's validator history**

Functions that count or iterate an operator's keys are linear in the operator's key count, and for operators with large key histories some may exceed the per-transaction gas limit. A cache has been deployed for permissionless operators; residual gas-cost reports on these paths are informational.

**16.) Operator rewards collector: a maximum claim can leave a position at the liquidation threshold**

claim() lets an operator withdraw down to the amount retained for unpaid utilization fees, which can leave its health factor at or near 1. Liquidation at a health factor of 1 or below is the documented recovery path for unpaid utilization fees, and operators avoid it by repaying before claiming. Reports that a claim makes an operator immediately liquidatable, or that the liquidation bonus can be captured afterwards, are variants of this known issue.

**17.) Permissioned pool: defective-key reimbursement is limited by the insurance fund balance**

When the oracle reports front-run or invalid-signature keys, the pre-deposit amount per key is reimbursed from StaderInsuranceFund. A report whose defective keys exceed the fund balance reverts and must be resubmitted in smaller batches or after the fund is topped up (depositFund is permissionless). Defective keys are created only by whitelisted permissioned operators, so reports built on an operator submitting invalid keys fall under the trusted-role exclusion and this known issue.

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
