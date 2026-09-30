# Immutable

- Page: https://immunefi.com/bug-bounty/immutable/scope/
- Max bounty: $1,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (10)

- [smart_contract] https://etherscan.io/address/0x177EaFe0f1F3359375B1728dae0530a75C83E154 — L1 Ethereum Mainnet Chain ID 1 - Bridge Implementation
- [smart_contract] https://etherscan.io/address/0x4f49b53928a71e553bb1b0f66a5bcb54fd4e8932 — L1 Ethereum Mainnet Chain ID 1 - Adapter Proxy
- [smart_contract] https://etherscan.io/address/0xBa5E35E26Ae59c7aea6F029B68c6460De2d13eB6 — L1 Ethereum Mainnet Chain ID 1 - Bridge Proxy
- [smart_contract] https://etherscan.io/address/0xE2E91C1Ae2873720C3b975a8034e887A35323345 — L1 Ethereum Mainnet Chain ID 1 - Adapter Implementation
- [smart_contract] https://explorer.immutable.com/address/0x1d49c44dc4BbDE68D8D51a9C5732f3a24e48EFA6 — L2 zkEVM Chain ID 13371 - Adapter Implementation
- [smart_contract] https://explorer.immutable.com/address/0x4f49B53928A71E553bB1B0F66a5BcB54Fd4E8932 — L2 zkEVM Chain ID 13371 - Adapter Proxy
- [smart_contract] https://explorer.immutable.com/address/0x8804A8aA1F18f23aE8A456dD73806FdA3219FaD1 — L2 zkEVM Chain ID 13371 - ChildERC20 Token Template
- [smart_contract] https://explorer.immutable.com/address/0xBa5E35E26Ae59c7aea6F029B68c6460De2d13eB6 — L2 zkEVM Chain ID 13371 - Bridge Proxy
- [smart_contract] https://explorer.immutable.com/address/0xb4c3597e6b090A2f6117780cEd103FB16B071A84 — L2 zkEVM Chain ID 13371 - Bridge Implementation
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (7)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] Medium: Griefing i.e. an attack with no direct profit motive for an attacker, but which results in notable, persistent or permanent damage to the protocol, its assets or users. This excludes transient or minor inconveniences (like a user needing to resubmit a transaction)
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$1,000,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 1,000,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 50,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 
- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

- High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 5,000 to USD 20,000 depending on the funds at risk, capped at the maximum high reward.

- In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
