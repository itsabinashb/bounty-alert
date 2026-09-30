# dHEDGE

- Page: https://immunefi.com/bug-bounty/dhedge/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: (none)
- End date: (none)

## Assets in scope (7)

- [smart_contract] https://arbiscan.io/address/0xffFb5fB14606EB3a548C113026355020dDF27535 — PoolFactory and linked contracts
- [smart_contract] https://basescan.org/address/0x49Afe3abCf66CF09Fab86cb1139D8811C8afe56F — PoolFactory and linked contracts
- [smart_contract] https://dhedge.org/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://etherscan.io/address/0x96D33bCF84DdE326014248E2896F79bbb9c13D6d — PoolFactory and linked contracts
- [smart_contract] https://hyperevmscan.io/address/0x615037C2Df6FA97634c5aD2d8144708b9dd3B176 — PoolFactory and linked contracts
- [smart_contract] https://optimistic.etherscan.io/address/0x5e61a079A178f0E5784107a4963baAe0c5a680c6 — PoolFactory and linked contracts
- [smart_contract] https://polygonscan.com/address/0xfdc7b8bFe0DD3513Cc669bB8d601Cb83e2F69cB0 — PoolFactory and linked contracts

## Asset notes

Deployed contracts that are currently linked to the PoolFactory are considered in scope. Linked contracts include, but not limited to: vault implementation contracts (PoolLogic, PoolManagerLogic), numerous contract/asset guards (3rd party integrations related code) and price aggregator contracts used for assets pricing.

## Impacts in scope (2)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds

## Impact notes

dHEDGE vaults are trust minimized, meaning that the vault manager may not follow a set strategy, or may make bad trades, including trades with poor slippage. A complete loss of funds is possible via poor risk-management strategies by the manager. These types of losses are not in scope for the bounty.

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$1,000, rewardCalculationPercentage=0.1, rewardModel=range

## Reward notes

If a vulnerability is found in integration-related contracts (such as contract guards or asset guards), the funds at risk should be calculated per chain, based on which deployments actually include the affected integration.

In the dHEDGE system, managers/traders are generally not considered trusted, and issues exploitable by a manager/trader are typically treated as putting user funds at risk. However, this assumption does not apply to vaults managed directly by the protocol team. Vaults operated by dHEDGE itself or by incubated protocols under its operational control (e.g., Toros, mStable) should be considered trusted. Therefore, if a vulnerability is exploitable only by a permissioned manager/trader, the funds at risk should exclude vaults under direct team management.

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk.

## Out of scope (program-specific)

- Attacks by privileged manager accounts which relate to poor trading practices or slippage. 
  - Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
