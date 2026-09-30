# Orca

- Page: https://immunefi.com/bug-bounty/orca/scope/
- Max bounty: $500,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://solscan.io/account/StaKE6XNKVVhG8Qu9hDJBqCW3eRe7MDGLz17nJZetLT — xORCA
- [smart_contract] https://solscan.io/account/whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc — Orca Whirlpools

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If any Critical/High severity impact can be caused to any other asset managed by Orca that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project.

## Impacts in scope (11)

- [smart_contract] Critical: Bugs that freeze user funds or drain the contract's holdings or involve theft of funds without user signatures
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Bugs that could temporarily freeze user funds or incorrectly assign value to user funds
- [smart_contract] High: Temporary freezing of unclaimed yield for any amount of time
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: fixedReward=$50,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$10,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Rewards for critical smart contract vulnerabilities can be further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum reward of __USD 100 000__ for Critical smart contract bug reports. 

Payouts are handled by the __Orca__ team directly and are denominated in USD. Payouts of up to __USD 250 000__ are done in __ORCA__ or __USDC__ (SPL Version) at the discretion of the team. Payouts above __USD 250 000__ will be done in __ORCA__ and will be vested monthly over a 12-month period.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
