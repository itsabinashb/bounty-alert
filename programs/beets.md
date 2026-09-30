# Beets

- Page: https://immunefi.com/bug-bounty/beets/scope/
- Max bounty: $200,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (3)

- [smart_contract] https://sonicscan.org/address/0x2d0e0814e62d80056181f5cd932274405966e4f0#code — Beets Token
- [smart_contract] https://sonicscan.org/address/0x5f9a5CD0B77155AC1814EF6Cd9D82dA53d05E386#code — Beets Token Migrator
- [smart_contract] https://sonicscan.org/address/0xe5da20f15420ad15de0fa650600afc998bbe3955#code — Beets Staked Sonic

## Asset notes

All smart contracts of Beets can be found at [https://github.com/beethovenxfi](https://github.com/beethovenxfi). However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If an impact can be caused to any other asset managed by Beets that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project.

## Impacts in scope (6)

- [smart_contract] Critical: Direct theft of >10% of user funds, other than unclaimed yield, in excess of gas costs or swap fees
- [smart_contract] Critical: Permanent freezing of >10% of total funds in excess of gas costs or swap fees
- [smart_contract] High: Direct theft of >5% of user funds, other than unclaimed yield, in excess of gas costs or swap fees
- [smart_contract] High: Permanent freezing of >10% of total unclaimed yield
- [smart_contract] High: Permanent freezing of >5% of total funds in excess of gas costs or swap fees
- [smart_contract] High: Theft of >10% of total unclaimed yield

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$200,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All High and Critical Smart Contract bug reports require a PoC and a suggestion for a fix to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

Critical smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk. However, there is a minimum reward of __USD 20 000__. 

High severity smart contract vulnerabilities are also further capped at 10% of economic damage,  primarily taking into consideration funds at risk. However, there is a minimum reward of __USD 5 000__.

All vulnerabilities marked in the [audits](https://github.com/beethovenxfi/sonic-staking/tree/main/audits) are not eligible for a reward.

Payouts are handled by the __Beets DAO__ directly and are denominated in USD. However, payouts are done in __USDC and BEETS__.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
