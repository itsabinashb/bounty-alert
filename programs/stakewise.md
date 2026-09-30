# StakeWise Mainnet

- Page: https://immunefi.com/bug-bounty/stakewise/scope/
- Max bounty: $200,000
- KYC required: no
- Paused: yes
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (15)

- [smart_contract] https://etherscan.io/address/0x002932e11E95DC84C17ed5f94a0439645D8a97BC — PoolValidators
- [smart_contract] https://etherscan.io/address/0x144a98cb1CdBb23610501fE6108858D9B7D24934 — Gnosis Safe
- [smart_contract] https://etherscan.io/address/0x20BC832ca081b91433ff6c17f85701B6e92486c5 — RewardEthToken
- [smart_contract] https://etherscan.io/address/0x2296e122c1a20Fca3CAc3371357BdAd3be0dF079 — PoolEscrow
- [smart_contract] https://etherscan.io/address/0x3EB0175dcD67d3AB139aA03165e24AA2188A4C22 — Proxy Admin
- [smart_contract] https://etherscan.io/address/0x48C3399719B582dD63eB5AADf12A40B4C3f52FA2 — StakeWiseToken
- [smart_contract] https://etherscan.io/address/0x7B910cc3D4B42FEFF056218bD56d7700E4ea7dD5 — VestingEscrowFactory
- [smart_contract] https://etherscan.io/address/0x8a887282E67ff41d36C0b7537eAB035291461AcD — Oracles
- [smart_contract] https://etherscan.io/address/0xA3F21010e8b9a3930996C8849Df38f9Ca3647c20 — MerkleDistributor
- [smart_contract] https://etherscan.io/address/0xC486c10e3611565F5b38b50ad68277b11C889623 — Roles
- [smart_contract] https://etherscan.io/address/0xC874b064f465bdD6411D45734b56fac750Cda29A — Pool
- [smart_contract] https://etherscan.io/address/0xFe2e637202056d30016725477c5da089Ab0A043A — StakedEthToken
- [smart_contract] https://etherscan.io/address/0xaE678D2A911400a55e06f4A1F0C0B363F3eE2e42 — VestingEscrow
- [smart_contract] https://etherscan.io/address/0xb5cf5363c3e766e64b37b2fb9554bfe8d48ed1a0 — DAO Module
- [websites_and_applications] https://app.stakewise.io/ — Web/App

## Asset notes

In addition, all implementation contracts linked to the proxies listed in the assets in scope are also considered as in-scope of this program. 

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If an impact can be caused to any other asset managed by StakeWise that isn’t on this table but for which the impact is in the Impacts in Scope section, you are encouraged to submit it for the consideration of the project.

## Impacts in scope (10)

- [smart_contract] Critical: Loss of Treasury Funds
- [smart_contract] Critical: Loss of users funds
- [smart_contract] Critical: Theft of unclaimed yield
- [smart_contract] High: Freezing of other funds for at least 1 week
- [smart_contract] High: Freezing of unclaimed yield for at least 1 week
- [websites_and_applications] Critical: Loss of Treasury funds
- [websites_and_applications] Critical: Loss of user funds
- [websites_and_applications] High: Freezing of other funds for at least 1 week
- [websites_and_applications] High: Freezing of unclaimed yield for at least 1 week
- [websites_and_applications] High: Theft of unclaimed yield

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$200,000, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] High: fixedReward=$50,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$200,000, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$50,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. In addition, all bug reports must also come with a suggestion for a fix in order to be considered for a reward. 

Known issues highlighted in their previous audits here are considered out of scope of this program:
  - [https://github.com/stakewise/contracts/tree/master/audits](https://github.com/stakewise/contracts/tree/master/audits) 

Payouts are handled by the __StakeWise__ team directly and are denominated in USD. Payouts are done in __SWISE__ or __USDC__, at the discretion of the team.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
