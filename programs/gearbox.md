# Gearbox

- Page: https://immunefi.com/bug-bounty/gearbox/scope/
- Max bounty: $150,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://github.com/Gearbox-protocol/security/blob/main/bug-bounty/v3_1-scope.md — The list of repositories containing all relevant contracts, as well as sources for discovering active deployments.
- [smart_contract] https://wwwimmunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

If you have found a bug that you think is within the security interests of the protocol but is outside of the scope (e.g., the contract is not yet deployed), please notify the team anyway. You can decide ad-hoc together with them in such cases. 1/1 payouts have been done before based on this.

## Impacts in scope (14)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Governance voting manipulation that would result in loss of funds
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$150,000, minReward=$6,000, primacy=primacy_of_impact, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$6,000, minReward=$3,000, primacy=primacy_of_impact, rewardModel=range
- [smart_contract] Medium: maxReward=$3,000, minReward=$1,000, rewardModel=range
- [smart_contract] Low: maxReward=$1,000, minReward=$1,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

- Critical smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team.
For Critical vulnerabilities affecting assets with no funds currently at risk (for example, integrations not yet launched or systems with no active exposure), rewards will be calculated using the minimum Critical reward amount. 

__Repeatable Attack Limitations__

  - If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

  - For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

  - High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of __USD 3 000__ to __USD 6 000__ depending on the funds at risk, capped at the maximum high reward.  

  - In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Payment Terms__

Payouts are handled by the __Gearbox__ team directly and are denominated in __USD__. However, payments are done in __USDC__

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
