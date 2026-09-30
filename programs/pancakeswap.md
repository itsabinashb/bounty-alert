# PancakeSwap

- Page: https://immunefi.com/bug-bounty/pancakeswap/scope/
- Max bounty: $1,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - high, smart_contract - critical, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://github.com/pancakeswap/infinity-core — Pancakeswap Infinity Core
- [smart_contract] https://github.com/pancakeswap/infinity-periphery — Pancakeswap Infinity Periphery
- [smart_contract] https://github.com/pancakeswap/infinity-universal-router — Pancakeswap Infinity Router
- [smart_contract] https://github.com/pancakeswap/pancake-swap-periphery — Pancakeswap V2 Periphery
- [smart_contract] https://github.com/pancakeswap/pancake-v3-contracts — Pancakeswap V3
- [websites_and_applications] https://pancakeswap.finance/

## Asset notes

Please note that for Website/App, only [https://pancakeswap.finance](https://pancakeswap.finance) is in scope. Other subdomains are not in scope.

OFT related contracts are not in the scope of this program, unless the logic is specific to PancakeSwap’s implementation.

If you have found an issue with OFT related contracts, please report it to [https://immunefi.com/bounty/layerzero/](https://immunefi.com/bounty/layerzero/).

## Impacts in scope (25)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield (dependent on the value at stake)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Permanent freezing of funds (dependent on the value at stake)
- [smart_contract] Critical: Protocol Insolvency (dependent of the shortfall in value)
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Complete theft of unclaimed yield (dependent on the value at stake)
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Permanent freezing of unclaimed yield (dependent on the value at stake and duration of freeze)
- [smart_contract] High: Temporary freezing of funds (dependent on the value at stake and duration of freeze)
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notification
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Medium: Subdomain takeover without already-connected wallet interaction

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$1,000,000, rewardCalculationPercentage=5, rewardModel=up_to
- [smart_contract] High: maxReward=$20,000, rewardModel=up_to
- [websites_and_applications] Critical: maxReward=$7,500, otherImpactMaxReward=$0, rewardModel=up_to
- [websites_and_applications] High: maxReward=$4,000, rewardModel=up_to
- [websites_and_applications] Medium: maxReward=$1,500, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on
the [Immunefi Vulnerability Severity Classification System 2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

Smart Contract rewards are classified by __Group 1__ and __Group 2__. 

__Group 1__ consists of the core swap and reward components such as:

AMM: Pancakeswap V2, V3, Stableswap and related periphery contracts
Staking: Masterchef V2, V3, Smart Chef (Syrup pools), Cake Pool

__Group 2__ consists of other contracts not mentioned in group 1.

Group 1 rewards are notated in the rewards table by the higher ranges listed by severity level, while Group 2 rewards are notated by the lower ranges listed by severity level.

All bug reports must include a Proof of Concept demonstrating how the vulnerability can be exploited to be eligible for a reward. 

The final reward amount for critical vulnerabilities is capped at 5% of the funds at risk based on the vulnerability reported.

Critical smart contract vulnerability payouts for Group 1 are a minimum of __USD $50,000__, or 5% of the value at risk at the time of report submission, with a hard cap of __USD $1,000,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum __USD $50,000__ or 5% of value at risk is at the discretion of the team.

Critical smart contract vulnerability payouts for Group 2 are a minimum of __USD $20,000__, or 5% of the value at risk at the time of report submission, with a hard cap of __USD $100,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum __USD $20,000__ or 5% of value at risk is at the discretion of the team.

All non-critical rewards for the project bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. Rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program.

This program follows the policy where a report is eligible for bounty only if a fix is implemented.

XSS reports are restricted to those that have an impact of prompting a user to  sign a transaction or a redirect.

All payouts are done by the **PancakeSwap** team and are pegged to the **USD** values set here and are payable in **CAKE** or **USDT**.

## Out of scope (program-specific)

- Best practice critiques
- Internal SSRF
- Path Traversal
- SPF/DKIM/DMARC Configuration Problems
- Clickjacking 
- Attacks requiring privileged access from within the organization

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- Exact Output gives lesser than expected for partial fills (https://github.com/Uniswap/v4-periphery/commit/545a5d2a87228167edde48f3b9eda122d1e3c4d6)
- Insufficient Slippage Protection in MINT_POSITION_FROM_DELTAS and _increaseFromDeltas in CLPositionManager (https://github.com/Uniswap/v4-periphery/pull/517)
- UniversalRouter “OnlyMintAllowed” bypass drains Infinity CL position fees via INCREASE_FROM_DELTAS + TAKE_PAIR (https://cantina.xyz/code/ea552420-8bd6-4119-815d-3d5203d0377a/findings/78)
