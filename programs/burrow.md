# Burrow

- Page: https://immunefi.com/bug-bounty/burrow/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (1)

- [smart_contract] https://nearblocks.io/address/contract.main.burrow.near# — Burrow main contract

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Issues that are not directly caused by bugs in Burrow’s smart contracts should be considered out of scope. This includes:
1. bad debt due to rapid changing market conditions
2. price manipulation due to external data source exploit

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Smart contract fails to deliver promised returns, but doesn’t lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$25,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [ Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported. 

All Critical, High, and Medium bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. In addition, all bug reports must come with a suggestion for a fix in order to be considered for a reward. 

Rewards for critical smart contract vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum reward of USD 25 000 for Critical smart contract bug reports.

High smart contract vulnerabilities are capped at 10% of economic damage, primarily based on value at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward for high vulnerabilities of __USD 5 000__.

Medium smart contract vulnerabilities are capped at 10% of economic damage, primarily based on value at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward for medium vulnerabilities of __USD 1 000__.

Known issues highlighted in the following audit reports are considered out of scope:
- [https://docs.burrow.cash/product-docs/introduction/audits-and-risks](https://docs.burrow.cash/product-docs/introduction/audits-and-risks)

Burrow requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. For individuals, the information needed is proof of address and government-issued photo ID for each authorized representative. For companies, the requirements will vary based on the type of the entity. 
Payouts are handled by the __Burrow__ team directly and are denominated in USD. However, payouts are done in __USDC__ or __USDT__.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
