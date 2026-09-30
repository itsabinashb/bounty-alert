# Aevo

- Page: https://immunefi.com/bug-bounty/Aevo/scope/
- Max bounty: $300,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://arbiscan.io/address/0x80d40e32fad8be8da5c6a42b8af1e181984d137c — Aevo Deposit Contract Arbitrum
- [smart_contract] https://etherscan.io/address/0x4082C9647c098a6493fb499EaE63b5ce3259c574 — Aevo Deposit Contract Ethereum

## Asset notes

(none)

## Impacts in scope (13)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$300,000, minReward=$50,000, rewardCalculationPercentage=0, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$25,000, minReward=$5,000, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on
the [Immunefi Vulnerability Severity Classification System](/severity-system/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

Smart Contracts Critical:
  - Loss of user funds:
    - 1% of all assets at risk, minimum __50 000 USD__, maximum __300 000 USD__
  - Loss of non-user funds (e.g. treasury):
    - 1% of assets at risk, minimum __50 000 USD__ , maximum __150 000 USD__

Smart Contracts High:
  - 1% of all assets at risk when attack persists for 1 month minimum __10 000 USD__, maximum of __50 000 USD__

Smart Contracts Medium:
  - 1% of all assets at risk when attack persists for 1 month minimum __5 000 USD__, maximum __25 000 USD__

Smart Contracts Low:
  - __2 000 USD__

Payouts are handled by the **Aevo** team directly and are denominated in USD. However, payouts are done in **USDC**.

## Out of scope (program-specific)

- Best practice critiques
 
-  Oracle failure/manipulation
- Novel governance attacks 
- Congestion and scalability
  - including running out of gas
  - including block stuffing
  - including susceptibility to frontrunning
- Consensus failures
- Cryptography problems
  - Signature malleability
  - Susceptibility to replay attacks
  - Weak randomness
- Weak encryption

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
