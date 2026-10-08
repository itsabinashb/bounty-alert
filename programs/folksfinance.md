# Folks Finance

- Page: https://immunefi.com/bug-bounty/folksfinance/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (21)

- [smart_contract] https://lora.algokit.io/mainnet/application/1040271396 — Oracle
- [smart_contract] https://lora.algokit.io/mainnet/application/1134695678 — xALGO
- [smart_contract] https://lora.algokit.io/mainnet/application/1258515734 — GOLD$ Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/1258524099 — SILVER$ Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/2611131944 — xALGO Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/3184317016 — ALGO Pool (Isolated)
- [smart_contract] https://lora.algokit.io/mainnet/application/3184324594 — USDC Pool (Isolated)
- [smart_contract] https://lora.algokit.io/mainnet/application/3184325123 — TINY Pool (Isolated)
- [smart_contract] https://lora.algokit.io/mainnet/application/3184333108 — Algorand Ecosystem Loan Type
- [smart_contract] https://lora.algokit.io/mainnet/application/3343137163 — FOLKS Pool (Isolated)
- [smart_contract] https://lora.algokit.io/mainnet/application/3514794123 — WBTC Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/3514795114 — WETH POOL
- [smart_contract] https://lora.algokit.io/mainnet/application/971333964 — Oracle Adapter
- [smart_contract] https://lora.algokit.io/mainnet/application/971350278 — Pool Manager
- [smart_contract] https://lora.algokit.io/mainnet/application/971353536 — Deposits Escrow
- [smart_contract] https://lora.algokit.io/mainnet/application/971368268 — ALGO Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/971372237 — USDC Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/971373361 — goBTC Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/971373611 — goETH Pool
- [smart_contract] https://lora.algokit.io/mainnet/application/971388781 — General Loan Type
- [smart_contract] https://lora.algokit.io/mainnet/application/971389489 — ALGO Efficiency Loan Type

## Asset notes

(none)

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 48 hours
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol) - excludes freezing of funds
- [smart_contract] Medium: Protocol unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 24 hours
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported. 

Smart Contract bug reports require a PoC and a suggestion for a fix to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

High and Critical smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward of __USD 50 000__ for Critical and __USD 10 000__ for High. 

All vulnerabilities marked in the following Github repository [https://github.com/Folks-Finance/audits](https://github.com/Folks-Finance/audits) are ineligible for a reward

Bug reports related solely to external incentives distributed on top of the protocol are downgraded in severity by one level. 

Bug reports covering previously-discovered bugs are not eligible for any reward through the bug bounty program. If a bug report covers a known issue, it may be rejected together with proof of the issue being known before escalation of the bug report via Immunefi.

__KYC__ shall be completed for bug bounty hunters submitting a vulnerability report and requesting a reward for Critical and High Smart Contracts vulnerabilities. The basic information needed is full name, residential address, and passport details (DOB, issuing country and passport number). Based on the basic information submitted, Folks Finance team may request further information at its sole discretion for compliance with applicable
Laws.

Additionally, all levels of bug bounty hunters submitting a vulnerability report and requesting a reward need to submit certification that 
- (i) they are not acting, directly or indirectly, for or on behalf of any person, group entity, or nation named by any Executive Order or the United States Treasury Department as a terrorist, “Specially Designated National and Blocked Person,” or other banned or blocked person, entity, nation, or transaction pursuant to any law, order, rule or regulation that is
enforced or administered by the Office of Foreign Assets Control; and  
- (ii) they are not engaging in, instigating or facilitating this transaction, directly or indirectly, on behalf of any such person, group,
entity, or nation. They also need to submit an attestation that all information provided is true, correct, up-to-date and not misleading. The collection of this information will be done by the Folks Finance team.

Payouts are handled by the __Folks Finance__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

The following vulnerabilities are excluded from the rewards for this bug bounty program:

- Attacks that the reporter has already exploited themselves, leading to damage
- Attacks requiring access to leaked keys/credentials
- Attacks requiring access to privileged addresses (governance, strategist)

__Smart Contracts and Blockchain__

- Any smart contracts or logic related to incentives
- Incorrect data supplied by third party oracles and market manipulation
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts relying on the depegging of an external token where the attacker does not directly cause the depegging from a bug in the in-scope contracts
- Basic economic governance attacks (e.g. 51% attack)
- Lack of liquidity
- Best practice critiques
- Sybil attacks
- Centralization risks

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- An attacker sends some fAsset, whose pool's collateral cap is zero, to a loan such that it prevents the loan from being closed out. Other similar examples such as when an escrow has opted into a different asset prior to being used (https://lora.algokit.io/mainnet/application/971388781)
