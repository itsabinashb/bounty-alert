# Twyne

- Page: https://immunefi.com/bug-bounty/twyne/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (17)

- [smart_contract] https://etherscan.io/address/0x0aF56aFBDDCb140323445BD7211Ba90E54e5FD1C — aPT22Oct2026 Wrapper
- [smart_contract] https://etherscan.io/address/0x0acd3A3c8Ab6a5F7b5A594C88DFa28999dA858aC — Vault Manager
- [smart_contract] https://etherscan.io/address/0x229fE10bC00bBE99Ac99703647D4f74F31605e91 — Aave V3 Deleverage Operator
- [smart_contract] https://etherscan.io/address/0x451949bde57aBe2F5DBD4758Cd50C6DCfC093A4C — Aave V3 Leverage Operator
- [smart_contract] https://etherscan.io/address/0x75029a47f28550C93Ad5A3BbD2d9b5315204B561 — aWSTETH Intermediate Credit Vault
- [smart_contract] https://etherscan.io/address/0x7613D202Af490c3d1cE1873b0a7022a34E89815f — eWSTETH Intermediate Credit Vault
- [smart_contract] https://etherscan.io/address/0x79CF33e623555E899d4EE122b9BfA0214fa5A4A1 — aPT22Oct2026 Intermediate Credit Vault
- [smart_contract] https://etherscan.io/address/0x868a21426852A775395d4b90De23B3e3E662bd78 — Aave V3 Teleport Operator
- [smart_contract] https://etherscan.io/address/0x87b8081A3ace680f35125F469526Ac10f5418Ca7 — eWETH Intermediate Credit Vault
- [smart_contract] https://etherscan.io/address/0xB5Eb1d005e389Bef38161691E2083b4d86FF647a — Intermediate Vault Factory
- [smart_contract] https://etherscan.io/address/0xFaBA8f777996C0C28fe9e6554D84cB30ca3e1881 — awstETH Wrapper
- [smart_contract] https://etherscan.io/address/0xa1517cCe0bE75700A8838EA1cEE0dc383cd3A332 — Collateral Vault Factory
- [smart_contract] https://etherscan.io/address/0xb001f039D76bA48E577A17c04b6940DB37aF8648 — Euler Oracle Router
- [smart_contract] https://etherscan.io/address/0xb7a7Cf5EB16C124562857632F8f86Ed627e6cc35 — Aave V3 Leverage Operator
- [smart_contract] https://etherscan.io/address/0xd07e1dd26f415fed3e8c490623a80ab55cf7bdbb — Euler Leverage Operator
- [smart_contract] https://etherscan.io/address/0xef39D6493884C4C84D38a4bFF879Ce16CEdE702a — Twyne EVC
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (6)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds (for at least 24 hours)
- [smart_contract] High: Theft of unclaimed yield

## Impact notes

All vaults deployed using `CollateralVaultFactory` are considered in scope

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$3,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 50 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 20 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 10 000 to USD 3 000 depending on the funds at risk, capped at the maximum high reward.  

In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Payment Terms__

Payouts are handled by the Twyne team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

- Reverts in/through Operator contracts that solely prevent the execution of batched transactions shall be deemed out of scope.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
