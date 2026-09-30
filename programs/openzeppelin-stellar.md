# OpenZeppelin on Stellar

- Page: https://immunefi.com/bug-bounty/openzeppelin-stellar/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: (none)
- End date: (none)

## Assets in scope (1)

- [smart_contract] https://github.com/OpenZeppelin/stellar-contracts/releases — OpenZeppelin Stellar Contracts Library (only the packages folder of the latest release is in scope)

## Asset notes

(none)

## Impacts in scope (15)

- [smart_contract] Critical: Access control is bypassed, including privilege escalation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] High: Governance voting result manipulation
- [smart_contract] High: Permanent denial of service (smart contract is made unable to operate)
- [smart_contract] High: Permanent freezing of funds
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Invalid events are emitted, potentially confusing indexers (internal storage is unaffected)
- [smart_contract] Low: Temporary denial of service (smart contract is made unable to operate for one block, functionality is restored in the next block)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$25,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the Immunefi Vulnerability Severity Classification System V2.3. This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

The rewards stated here are additive to any existing bug bounty programs hosted by projects that are currently using OpenZeppelin on Stellar contracts.

Bounty rewards are given according to an [impact/likelihood matrix for assessing threat levels. ](https://raw.githubusercontent.com/OpenZeppelin/immunefi-assets/main/impact-likelihood-matrix.png?utm_source=immunefi)Each issue is assessed considering the likelihood of the vulnerability being successfully exploited and the expected impact in scope to a single instance of the affected smart contract. Note that, as can be seen in the matrix, if the impact is Critical then the threat is always Critical, for other impacts the maximum reduction is one level only if the likelihood is low, and if the likelihood is high then the threat is increased one level above the impact.

__Critical Reward Calculation__
Mainnet assets:
- Reward amount is 10% of the funds directly affected up to a maximum of: $25,000
- Minimum reward to discourage security researchers from withholding a bug report: $5,000

__Reward Payment Terms__

- Total maximum payout for this bug bounty contest is $250,000.
- Maximum single bounty payout is capped at $25,000.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (2)

- Added the signing contract as part of `AuthDigestPreimage` (https://github.com/OpenZeppelin/stellar-contracts/pull/868)
- This issue is being addressed in the following PR. (https://github.com/OpenZeppelin/stellar-contracts/pull/837)
