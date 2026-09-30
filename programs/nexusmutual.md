# Nexus Mutual

- Page: https://immunefi.com/bug-bounty/nexusmutual/scope/
- Max bounty: $25,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (3)

- [smart_contract] https://github.com/NexusMutual/smart-contracts/tree/master — Master candidate Branch - excluding /contracts/modules/assessment and /contracts/modules/governance
- [smart_contract] https://github.com/NexusMutual/smart-contracts/tree/release-candidate — Release candidate Branch - excluding /contracts/modules/assessment and /contracts/modules/governance
- [smart_contract] https://www.immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (8)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting, resulting in deviation from voted outcome - must bypass Advisory Board privileges that could otherwise mitigate the situation
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered as in-scope, even if they affect something in the assets in scope table.

## Rewards

- [smart_contract] Critical: maxReward=$25,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$3,000, rewardModel=range
- [smart_contract] Medium: maxReward=$3,000, minReward=$1,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

For critical smart contract bugs, the reward amount is __10%__ of the funds directly affected up to a maximum of __USD 25 000__.  The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. A minimum reward of __USD 5 000__ is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

  - If the smart contract where the vulnerability exists can be upgraded/paused/killed, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading, pausing, or in some cases, killing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

  - For critical repeatable attacks on smart contracts that can not be upgraded/paused/killed, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

  - High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are considered at the full amount of funds at risk, capped at the maximum high reward. This is to incentivize security researchers to uncover and responsibly disclose vulnerabilities that may have not have significant monetary value today, but could still be damaging to the project if it goes unaddressed.   

  - In the event of temporary freezing, the reward increases at a multiplier of two from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lenghents, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Payment Terms__

Payouts are handled by __Nexus Mutual__ directly and are denominated in __USD__. However, payouts are done in __USDC__.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
