# Charm

- Page: https://immunefi.com/bug-bounty/charm/scope/
- Max bounty: $6,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (3)

- [smart_contract] https://github.com/charmfinance/alpha-vaults-v2-contracts/blob/main/contracts/AlphaProVault.sol
- [smart_contract] https://github.com/charmfinance/alpha-vaults-v2-contracts/blob/main/contracts/AlphaProVaultFactory.sol
- [smart_contract] https://github.com/charmfinance/alpha-vaults-v2-contracts/blob/main/contracts/CloneFactory.sol

## Asset notes

(none)

## Impacts in scope (14)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
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

- [smart_contract] Critical: fixedReward=$6,000, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] High: fixedReward=$3,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$1,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on
the [Immunefi Vulnerability Severity Classification System](/severity-system/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

Payouts are handled by the **Charm** team directly and are denominated in
**USD**. However, payouts are done in **ETH or USDC**.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
