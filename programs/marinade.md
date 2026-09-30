# Marinade

- Page: https://immunefi.com/bug-bounty/marinade/scope/
- Max bounty: $250,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (1)

- [smart_contract] https://github.com/marinade-finance/liquid-staking-program

## Asset notes

(none)

## Impacts in scope (6)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds excluding DOS attacks
- [smart_contract] High: Theft of unclaimed yield

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: maxReward=$15,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

All smart contract bug reports must come with a PoC in order to be considered for a reward.

Critical vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum of __USD 50 000__ for Critical bug reports.

Payouts are handled by the __Marinade Finance__ team directly and are denominated in USD. However, payouts are done in __mSOL__ and __MNDE__.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Deactive delinquent handled only after commit 3e7c090 (https://github.com/marinade-finance/liquid-staking-program/pull/84)
