# Extra Finance

- Page: https://immunefi.com/bug-bounty/extrafinance/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (9)

- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://optimistic.etherscan.io/address/0x0353b6221b23b8320202320ca450eeb9fb0de9e5#code — Pool_Impl (Lending Market)
- [smart_contract] https://optimistic.etherscan.io/address/0x2B275176804dd01b6a90d61bDa3c80E3A470662E#code — A_Token (Lending Market)
- [smart_contract] https://optimistic.etherscan.io/address/0x345D2827f36621b02B783f7D5004B4a2fec00186#code — Pool_Proxy (Lending Market)
- [smart_contract] https://optimistic.etherscan.io/address/0xC0C88d2752C58263c2b7F4Ac6ecBedC78eDD5d5E#code — Debt_Token (Lending Market)
- [smart_contract] https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd — LendingPool (LYF)
- [smart_contract] https://optimistic.etherscan.io/address/0xe0bec4f45aef64cec9dcb9010d4beffb13e91466 — VeToken (LYF)
- [smart_contract] https://optimistic.etherscan.io/address/0xf9cfb8a62f50e10adde5aa888b44cf01c5957055 — VeloPositionManage (LYF)
- [smart_contract] https://optimistic.etherscan.io/token/0x2dad3a13ef0c6366220f989157009e501e7938f8 — EXTRA (LYF)

## Asset notes

(none)

## Impacts in scope (6)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$15,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$15,000, minReward=$3,000, rewardModel=range
- [smart_contract] Medium: maxReward=$3,000, minReward=$1,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Reward Calculation for Critical Level Reports__

For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 15 000 is to be rewarded in order to incentivize security researchers against withholding a bug report.  

__Repeatable Attack Limitations__

In cases of repeatable attacks for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.

__Previous Audits__

Extra Finance has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.
__LYF:__

- [https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-ExtraFi-v1.0.pdf](https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-ExtraFi-v1.0.pdf)
- [https://github.com/blocksecteam/audit-reports/blob/main/solidity/blocksec_extrafinance_v1.0-signed.pdf ](https://github.com/blocksecteam/audit-reports/blob/main/solidity/blocksec_extrafinance_v1.0-signed.pdf) 

__Lending Market:__

- [https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-ExtraFi-v1.0.pdf](https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-ExtraFi-v1.0.pdf)


__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart Contract - Critical
- Smart Contract - High
- Smart Contract - Medium

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

As part of the bug bounty matching program, Optimism will contribute __52,500__ OP tokens to match the rewards offered by Extra Finance. This means that for every reward paid out by Extra Finance to a security researcher, Optimism will provide an additional, matching reward, in OP tokens. The total reward pool for this program is __52,500__ OP tokens.

Payouts are handled by the Extra Finance team directly and are denominated in USD. However, payments are done in USDC.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (4)

- Debt Repayment Failure Due to Rounding Errors. Accumulated rounding differences between pool-level and individual position debt calculations can cause reserve.totalBorrows to fall below debtPosition.borrowed. This can prevent full repayment of the affected position. (https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd)
- LendingPool.repay() increases credit by the supplied repayment amount rather than the actual debt repaid. This can result in excess credit when the repayment amount exceeds the outstanding debt. Access to this function is restricted to whitelisted vault contracts. (https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd)
- The LendingPool contains a known first-depositor share-inflation pattern when a reserve is empty. The original attack path is mitigated by atomically minting and permanently locking initial shares when each reserve is initialized. (https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd)
- reserve.lastUpdateTimestamp is not updated when the pool has no outstanding borrows. As a result, interest on the first borrow is calculated from the reserve’s initialization time rather than the borrowing time, causing the first borrower’s debt to be overstated. (https://optimistic.etherscan.io/address/0xbb505c54d71e9e599cb8435b4f0ceec05fc71cbd)
