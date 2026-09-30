# Pragma Oracle

- Page: https://immunefi.com/bug-bounty/pragmaoracle/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (4)

- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://voyager.online/contract/0x024a55b928496ef83468fdb9a5430fe031ac386b8f62f5c2eb7dd20ef7237415 — PublisherRegistry
- [smart_contract] https://voyager.online/contract/0x02a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b — Oracle
- [smart_contract] https://voyager.online/contract/0x49eefafae944d07744d07cc72a5bf14728a6fb463c3eae5bca13552f5d455fd#readContract — TWAP/Volatility

## Asset notes

(none)

## Impacts in scope (12)

- [smart_contract] Critical: Allow unauthorized actors to manipulate/publish any data entry
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield.
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results.
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Reward Calculation for Critical Level Reports__

For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 50 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 5 000 is to be rewarded in order to incentivize security researchers against withholding a bug report.   

__Repeatable Attack Limitations__

In cases of repeatable attacks for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart Contract + Critical + PoC Required
- Smart Contract + High + PoC Required
- Smart Contract + Medium + PoC Required

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.


__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs acknowledged below are not eligible for any reward through the bug bounty program. 
- [https://github.com/NethermindEth/PublicAuditReports/blob/main/NM0147-FINAL_PRAGMA.pdf](https://github.com/NethermindEth/PublicAuditReports/blob/main/NM0147-FINAL_PRAGMA.pdf)

__Reward Payment Terms__

Payouts are handled by the Pragma team directly and are denominated in USD. However, payments are done in USDC.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
