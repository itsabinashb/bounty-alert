# Obyte

- Page: https://immunefi.com/bug-bounty/obyte/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Blockchain/DLT, Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, smart_contract - medium, smart_contract - high, smart_contract - critical, blockchain_dlt - medium, blockchain_dlt - high, blockchain_dlt - critical
- End date: (none)

## Assets in scope (11)

- [blockchain_dlt] https://github.com/byteball/ocore — Core Library
- [smart_contract] https://github.com/byteball/city-aa — Autonomous Agent for Obyte City (city.obyte.org)
- [smart_contract] https://github.com/byteball/coop-aa — Autonomous Agent for Obyte Coop
- [smart_contract] https://github.com/byteball/counterstake-bridge — Smart Contracts and Autonomous Agents for Counterstake cross-chain bridge
- [smart_contract] https://github.com/byteball/friend-aa — Smart Contract - Autonomous Agent for Obyte Friends (friends.obyte.org)
- [smart_contract] https://github.com/byteball/obyte-cascading-donations — Autonomous Agent for cascading donations to github repos (kivach.org)
- [smart_contract] https://github.com/byteball/oswap-token-aa — Autonomous Agent for OSWAP token (token.oswap.io)
- [smart_contract] https://github.com/byteball/perpetual-aa — Autonomous Agent for Pythagorean perpetual futures (pyth.ooo)
- [smart_contract] https://github.com/byteball/prediction-markets-aa — Autonomous Agent for prediction markets (prophet.ooo)
- [smart_contract] https://github.com/byteball/token-registry-aa — Autonomous Agent for Obyte token registry (tokens.ooo)
- [websites_and_applications] https://github.com/byteball/obyte-gui-wallet — Wallet

## Asset notes

(none)

## Impacts in scope (18)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network permanently unable to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying adequate processing for at least 1 day. Requires network coordination to resolve
- [blockchain_dlt] Medium: Temporary freezing of network transactions by delaying adequate processing for at least 1 hour. Requires network coordination to resolve.
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds for at least 1 year
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:         - database passwords usable from the open internet ,        - wallet private keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking state-modifying authenticated actions that lead to loss of funds on behalf of other users without any interaction by that user.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:         - HTML injection without JavaScript         - Replacing existing text with arbitrary text         - Arbitrary file uploads, etc.
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:         - Reflected HTML injection         - Loading external site data

## Impact notes

All Smart Contract impacts are only related to the Autonomous Agent assets.

## Rewards

- [blockchain_dlt] Critical: maxReward=$50,000, minReward=$2,500, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: fixedReward=$1,700, rewardModel=fixed
- [blockchain_dlt] Medium: fixedReward=$1,000, rewardModel=fixed
- [smart_contract] Critical: fixedReward=$2,500, rewardCalculationPercentage=10, rewardModel=fixed
- [smart_contract] High: fixedReward=$1,700, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$2,500, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$1,700, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below.

__Repeatable Attack Limitations__

Given that the reward for High is flat, there is no distinction between a one-time attack and an attack that is repeated and the reward stays the same. 

__Restrictions on Security Researcher Eligibility__

Security researchers who fall under any of the following are ineligible for a reward:

- Compensated team members of the Obyte Foundation
- Employees and team members of third-party suppliers to an Obyte Foundation affiliate that operate in a technical capacity and have assets covered in this bug bounty program

__Reward Calculation for Critical Level Reports__

For Blockchain/DLT bug reports, in order to qualify for the reward of USD 50 000, the bug reported must be able to cause **unrecoverable total network shutdown of the entire Obyte network or allow the unpermitted execution of transactions from accounts of other users without their private keys**. All other critical bug reports are capped at a flat rate of USD 2 500.

For Critical Smart Contract and Web/App reports, the reward amount is 10% of the funds directly affected up to a maximum of USD 2 500.

__Poc Requirements__
All web and app bug reports must come with a PoC. All bug reports submitted without PoC will be rejected with instructions to provide PoC.

Payouts are handled by the Obyte Foundation directly and are denominated in USD. The payout can be completed in GBYTE, BTC, or USDT.

## Out of scope (program-specific)

__Out of Scope__

- For all impacts directly involving funds being lost or frozen, the minimum impact is USD 1000. Anything below is considered out-of-scope. 

-For Blockchain/DLT bug reports, temporary disruptions of network availability, such as node crashes and DoS, are out of scope when they can be resolved by deploying a fix without network coordination. Temporary disruptions that require network coordination to resolve are in scope and are assessed under the 'Temporary freezing of network transactions' impacts in the Impacts in Scope table

- The web/app  impacts of “Stealing User Cookies” and “Bypassing Authentication” are only accepted if they result in a loss of at least USD 1 000. The web/app impact of “Ability to execute system commands” is only accepted if the actions are done as root.

- Impacts with direct financial damage whereby the total is less than or equal to 200% of the total expense used by the attacker

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
